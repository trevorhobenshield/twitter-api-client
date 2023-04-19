import asyncio
import logging.config
import math
import platform
import random
import re
import time
from pathlib import Path

import aiohttp
import orjson
import requests

from .constants import *
from .util import set_qs

IN_PATH = Path('~/data/raw').expanduser()
OUT_PATH = Path(f'~/data/processed/search_results_{time.time_ns()}.json').expanduser()

reset = '\u001b[0m'
colors = [f'\u001b[{i}m' for i in range(30, 38)]
logging.config.dictConfig(log_config)
logger = logging.getLogger(__name__)

try:
    if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
        import nest_asyncio

        nest_asyncio.apply()
except:
    ...

if platform.system() != 'Windows':
    try:
        import uvloop

        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    except:
        ...
else:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def search(*args, out: str = 'data', **kwargs):
    out_path = make_output_dirs(out)
    return asyncio.run(process(args, search_config, out_path, **kwargs))


async def process(queries: tuple, config: dict, out: Path, **kwargs) -> list:
    conn = aiohttp.TCPConnector(limit=len(queries), ssl=False)
    async with aiohttp.ClientSession(headers=__get_headers(), connector=conn) as s:
        return await asyncio.gather(*(paginate(q, s, config, out, **kwargs) for q in queries))


async def paginate(query: str, session: aiohttp.ClientSession, config: dict, out: Path, **kwargs) -> list[dict]:
    api = 'https://api.twitter.com/2/search/adaptive.json?'
    config['q'] = query
    data, next_cursor = await backoff(lambda: get(session, api, config), query)
    all_data = [data]
    c = colors.pop() if colors else ''
    ids = set()
    while next_cursor:
        ids |= set(data['globalObjects']['tweets'])
        if len(ids) >= kwargs.get('limit', math.inf):
            logger.debug(f'[{GREEN}success{RESET}] returned {len(ids)} search results for {c}{query}{reset}')
            return all_data
        logger.debug(f'{c}{query}{reset}')
        config['cursor'] = next_cursor
        data, next_cursor = await backoff(lambda: get(session, api, config), query)
        data['query'] = query
        (out / f'raw/{time.time_ns()}.json').write_text(
            orjson.dumps(data, option=orjson.OPT_INDENT_2).decode(),
            encoding='utf-8'
        )
        all_data.append(data)
    return all_data


async def backoff(fn, info, retries=12):
    for i in range(retries + 1):
        try:
            data, next_cursor = await fn()
            if not data.get('globalObjects', {}).get('tweets'):
                raise Exception
            return data, next_cursor
        except Exception as e:
            if i == retries:
                logger.debug(f'Max retries exceeded\n{e}')
                return
            t = 2 ** i + random.random()
            logger.debug(f'No data for: \u001b[1m{info}\u001b[0m | retrying in {f"{t:.2f}"} seconds\t\t{e}')
            time.sleep(t)


async def get(session: aiohttp.ClientSession, api: str, params: dict) -> tuple[dict, str]:
    url = set_qs(api, params, update=True, safe='()')
    r = await session.get(url)
    data = await r.json()
    next_cursor = get_cursor(data)
    return data, next_cursor


def get_cursor(res: dict):
    try:
        for instr in res['timeline']['instructions']:
            if replaceEntry := instr.get('replaceEntry'):
                cursor = replaceEntry['entry']['content']['operation']['cursor']
                if cursor['cursorType'] == 'Bottom':
                    return cursor['value']
                continue
            for entry in instr['addEntries']['entries']:
                if entry['entryId'] == 'cursor-bottom-0':
                    return entry['content']['operation']['cursor']['value']
    except Exception as e:
        logger.debug(e)


def __get_headers(fname: str = None) -> dict:
    if fname:
        with open(fname) as fp:
            return {y.group(): z.group()
                    for x in fp.read().splitlines()
                    if (y := re.search('^[\w-]+(?=:\s)', x),
                        z := re.search(f'(?<={y.group()}:\s).*', x))}
    # default
    headers = {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; Nokia G20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36'
    }
    r = requests.post('https://api.twitter.com/1.1/guest/activate.json', headers=headers)
    headers['x-guest-token'] = r.json()['guest_token']
    return headers


def make_output_dirs(path: str) -> Path:
    p = Path(f'~/{path}').expanduser()
    (p / 'raw').mkdir(parents=True, exist_ok=True)
    (p / 'processed').mkdir(parents=True, exist_ok=True)
    (p / 'final').mkdir(parents=True, exist_ok=True)
    return p
