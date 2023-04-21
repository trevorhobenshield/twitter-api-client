import asyncio
import logging.config
import math
import platform
import random
import time
from pathlib import Path

import aiohttp
import orjson
from httpx import AsyncClient

from .constants import *
from .login import login
from .util import set_qs, get_headers

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
    except ImportError as e:
        ...


class Search:
    def __init__(self, email: str, username: str, password: str):
        self.session = login(email, username, password)
        self.api = 'https://api.twitter.com/2/search/adaptive.json?'

    def run(self, *args, out: str = 'data', **kwargs):
        out_path = self.make_output_dirs(out)
        if platform.system() != 'Windows':
            with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
                return runner.run(self.process(args, search_config, out_path, **kwargs))
        return asyncio.run(self.process(args, search_config, out_path, **kwargs))

    async def process(self, queries: tuple, config: dict, out: Path, **kwargs) -> list:
        async with AsyncClient(headers=get_headers(self.session)) as s:
            return await asyncio.gather(*(self.paginate(q, s, config, out, **kwargs) for q in queries))

    async def paginate(self, query: str, session: AsyncClient, config: dict, out: Path, **kwargs) -> list[
        dict]:
        config['q'] = query
        r, data, next_cursor = await self.backoff(lambda: self.get(session, config), query)
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

            r, data, next_cursor = await self.backoff(lambda: self.get(session, config), query)
            data['query'] = query
            (out / f'raw/{time.time_ns()}.json').write_text(
                orjson.dumps(data, option=orjson.OPT_INDENT_2).decode(),
                encoding='utf-8'
            )
            all_data.append(data)
        return all_data

    async def backoff(self, fn, info, retries=12):
        for i in range(retries + 1):
            try:
                r, data, next_cursor = await fn()
                if not data.get('globalObjects', {}).get('tweets'):
                    raise Exception
                return r, data, next_cursor
            except Exception as e:
                if i == retries:
                    logger.debug(f'Max retries exceeded\n{e}')
                    return
                t = 2 ** i + random.random()
                logger.debug(f'No data for: \u001b[1m{info}\u001b[0m | retrying in {f"{t:.2f}"} seconds\t\t{e}')
                time.sleep(t)

    async def get(self, session: AsyncClient, params: dict) -> tuple:
        url = set_qs(self.api, params, update=True, safe='()')
        r = await session.get(url)
        data = r.json()
        next_cursor = self.get_cursor(data)
        return r, data, next_cursor

    def get_cursor(self, res: dict):
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

    def make_output_dirs(self, path: str) -> Path:
        p = Path(f'~/{path}').expanduser()
        (p / 'raw').mkdir(parents=True, exist_ok=True)
        (p / 'processed').mkdir(parents=True, exist_ok=True)
        (p / 'final').mkdir(parents=True, exist_ok=True)
        return p
