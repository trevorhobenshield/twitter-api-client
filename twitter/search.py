import asyncio
import logging.config
import math
import platform
import random
import time
from logging import Logger
from pathlib import Path

import orjson
from httpx import AsyncClient

from .constants import *
from .login import login
from .util import set_qs, get_headers, find_key

reset = '\u001b[0m'
colors = [f'\u001b[{i}m' for i in range(30, 38)]

try:
    if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
        import nest_asyncio

        nest_asyncio.apply()
except:
    ...

if platform.system() != 'Windows':
    try:
        import uvloop

        uvloop.install()
    except ImportError as e:
        ...


class Search:
    def __init__(self, email: str, username: str, password: str, **kwargs):
        self.session = login(email, username, password, **kwargs)
        self.api = 'https://api.twitter.com/2/search/adaptive.json?'
        self.save = kwargs.get('save', True)
        self.debug = kwargs.get('debug', 0)
        self.logger = self.init_logger(kwargs.get('log_config', False))

    @staticmethod
    def init_logger(cfg: dict) -> Logger:
        logging.config.dictConfig(cfg or log_config)
        return logging.getLogger(__name__)

    def run(self, *args, out: str = 'data', **kwargs):
        out_path = self.make_output_dirs(out)
        if kwargs.get('latest', False):
            search_config['tweet_search_mode'] = 'live'
        return asyncio.run(self.process(args, search_config, out_path, **kwargs))

    async def process(self, queries: tuple, config: dict, out: Path, **kwargs) -> list:
        async with AsyncClient(headers=get_headers(self.session)) as s:
            return await asyncio.gather(*(self.paginate(q, s, config, out, **kwargs) for q in queries))

    async def paginate(self, query: str, session: AsyncClient, config: dict, out: Path, **kwargs) -> list[
        dict]:
        config['q'] = query
        data, next_cursor = await self.backoff(lambda: self.get(session, config), query, **kwargs)
        all_data = [data]
        c = colors.pop() if colors else ''
        ids = set()
        while next_cursor:
            ids |= set(data['globalObjects']['tweets'])
            if len(ids) >= kwargs.get('limit', math.inf):
                if self.debug:
                    self.logger.debug(
                        f'[{GREEN}success{RESET}] returned {len(ids)} search results for {c}{query}{reset}')
                return all_data
            if self.debug:
                self.logger.debug(f'{c}{query}{reset}')
            config['cursor'] = next_cursor

            data, next_cursor = await self.backoff(lambda: self.get(session, config), query, **kwargs)
            if not data:
                return all_data

            data['query'] = query

            if self.save:
                (out / f'raw/{time.time_ns()}.json').write_text(
                    orjson.dumps(data, option=orjson.OPT_INDENT_2).decode(),
                    encoding='utf-8'
                )
            all_data.append(data)
        return all_data

    async def backoff(self, fn, info, **kwargs):
        retries = kwargs.get('retries', 3)
        for i in range(retries + 1):
            try:
                data, next_cursor = await fn()
                if not data.get('globalObjects', {}).get('tweets'):
                    raise Exception
                return data, next_cursor
            except Exception as e:
                if i == retries:
                    if self.debug:
                        self.logger.debug(f'Max retries exceeded\n{e}')
                    return None, None
                t = 2 ** i + random.random()
                if self.debug:
                    self.logger.debug(
                        f'No data for: \u001b[1m{info}\u001b[0m | retrying in {f"{t:.2f}"} seconds\t\t{e}')
                time.sleep(t)

    async def get(self, session: AsyncClient, params: dict) -> tuple:
        url = set_qs(self.api, params, update=True, safe='()')
        r = await session.get(url)
        data = r.json()
        next_cursor = self.get_cursor(data)
        return data, next_cursor

    def get_cursor(self, res: dict):
        try:
            if live := find_key(res, 'value'):
                if cursor := [x for x in live if 'scroll' in x]:
                    return cursor[0]
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
            if self.debug:
                self.logger.debug(e)

    def make_output_dirs(self, path: str) -> Path:
        p = Path(f'{path}')
        (p / 'raw').mkdir(parents=True, exist_ok=True)
        (p / 'processed').mkdir(parents=True, exist_ok=True)
        (p / 'final').mkdir(parents=True, exist_ok=True)
        return p
