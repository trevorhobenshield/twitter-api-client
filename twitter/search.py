import asyncio
import atexit
import json
import logging.config
import platform
import random
import re
import time
from pathlib import Path
from urllib.parse import quote, urlencode, parse_qs, urlsplit, urlunsplit

import aiohttp
import requests

from .config.log import log_config
from .config.settings import search_config

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


def search(*args, out: str = 'data'):
    out_path = make_output_dirs(out)
    return asyncio.run(process(args, search_config, out_path))


async def process(queries: tuple, config: dict, out: Path) -> tuple:
    conn = aiohttp.TCPConnector(limit=len(queries), ssl=False)
    async with aiohttp.ClientSession(headers=__get_headers(), connector=conn) as s:
        return await asyncio.gather(*(paginate(q, s, config, out) for q in queries))


async def paginate(query: str, session: aiohttp.ClientSession, config: dict, out: Path) -> list[dict]:
    api = 'https://api.twitter.com/2/search/adaptive.json?'
    config['q'] = query
    data, next_cursor = await backoff(lambda: get(session, api, config), query)
    all_data = []
    c = colors.pop() if colors else ''
    while next_cursor:
        logger.debug(f'{c}{query}{reset}')
        config['cursor'] = next_cursor
        data, next_cursor = await backoff(lambda: get(session, api, config), query)
        data['query'] = query
        (out / f'raw/{time.time_ns()}.json').write_text(json.dumps(data, indent=4))
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
    url = set_qs(api, params, update=True)
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


def set_qs(url: str, qs: dict, update=False) -> str:
    *_, q, f = urlsplit(url)
    return urlunsplit((*_, urlencode(qs | parse_qs(q) if update else qs, doseq=True, quote_via=quote, safe='()'), f))


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
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
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


@atexit.register
def combine_results(in_path: Path = IN_PATH, out_path: Path = OUT_PATH):
    try:
        out_path.write_text(json.dumps({
            k: v
            for p in in_path.iterdir() if p.suffix == '.json'
            for k, v in json.loads(p.read_text())['globalObjects']['tweets'].items()
        }, indent=2))
    except Exception as e:
        logger.debug(f'FAILED to combine search results, {e}')
