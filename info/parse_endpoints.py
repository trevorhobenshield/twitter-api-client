import asyncio
import logging.config
import re
from pathlib import Path

import aiohttp
import nest_asyncio
import orjson
import uvloop

from twitter.config.log import log_config

logger = logging.getLogger(__name__)
logging.config.dictConfig(log_config)
nest_asyncio.apply()
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

BOLD = '\u001b[1m'
SUCCESS = '\u001b[32m'
WARN = '\u001b[31m'
RESET = '\u001b[0m'

PATHS = Path('paths.txt')
ENDPOINTS = Path('endpoints.json')
OUT_PATH = Path("endpoints")
OUT_PATH.mkdir(exist_ok=True, parents=True)


def get_headers(filename: str = 'headers.txt') -> dict:
    if (path := Path(filename)).exists():
        return {y.group(): z.group()
                for x in path.read_text().splitlines()
                if (y := re.search('^[\w-]+(?=:\s)', x),
                    z := re.search(f'(?<={y.group()}:\s).*', x))}
    # default
    return {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}


async def process(fn: callable, headers: dict, urls: any, **kwargs) -> tuple:
    conn = aiohttp.TCPConnector(ssl=False, limit=420, ttl_dns_cache=69)
    async with aiohttp.ClientSession(headers=headers, connector=conn) as s:
        return await asyncio.gather(*(fn(s, u, **kwargs) for u in urls))


async def get(session: aiohttp.ClientSession, url: str, **kwargs) -> tuple[str, dict]:
    try:
        logger.debug(f"GET {url}")
        res = await session.get(url)
        data = await getattr(res, kwargs.get('res', 'text'))()
        return url, data
    except Exception as e:
        logger.debug(f"[{WARN}FAILED{RESET}]: {url}\n{e}")


def find_paths():
    res = set()
    for p in OUT_PATH.iterdir():
        data = p.read_text()
        if x := re.findall('"[^"]*"|`[^`]*`|\'[^\']*\'', data):
            res |= set(x[1:-1] for x in x if '/' in x)
    PATHS.write_text('\n'.join(sorted(res)))


def main():
    urls = (
        f'https://abs.twimg.com/responsive-web/client-web/{k}.{v}a.js'
        for k, v in orjson.loads(ENDPOINTS.read_text()).items() if 'endpoint' in k
    )
    headers = get_headers()
    res = asyncio.run(process(get, headers, urls))
    [(OUT_PATH / u.split('/')[-1]).write_text(r) for u, r in res]

    find_paths()


if __name__ == '__main__':
    main()
