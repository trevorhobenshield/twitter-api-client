import asyncio
import logging.config
import platform
import random
import re
import subprocess
from asyncio import Semaphore
from functools import partial
from logging import getLogger, Logger
from pathlib import Path
from typing import Generator

import aiofiles
import chompjs
import orjson
from httpx import AsyncClient, Response, Limits, Client
from selectolax.lexbor import LexborHTMLParser
from tqdm.asyncio import tqdm_asyncio

try:
    get_ipython()
    import nest_asyncio

    nest_asyncio.apply()
except:
    ...

if platform.system() != 'Windows':
    try:
        import uvloop

        uvloop.install()
    except:
        ...

dump_json = partial(orjson.dumps, option=orjson.OPT_INDENT_2 | orjson.OPT_SORT_KEYS)


def mkdir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(exist_ok=True, parents=True)
    return p


logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s.%(msecs)03d [%(levelname)s] :: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'filename': 'log.log',
            'mode': 'a'
        },
        'console_warning': {
            'class': 'logging.StreamHandler',
            'level': 'WARNING',
            'formatter': 'standard'
        },
        'console_info': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'filters': ['info_only']
        }
    },
    'filters': {
        'info_only': {
            '()': lambda: lambda record: record.levelno == logging.INFO
        }
    },
    'loggers': {
        'my_logger': {
            'handlers': ['file', 'console_warning', 'console_info'],
            'level': 'DEBUG'
        }
    }
})
logger = getLogger(list(Logger.manager.loggerDict)[-1])

PATH_DATA = mkdir('data')

PATH_HOMEPAGE = PATH_DATA / 'x.html'
PATH_INITIAL_STATE = PATH_DATA / 'initial_state.json'
PATH_FEATURES = PATH_DATA / 'features.json'
PATH_LIMITS = PATH_DATA / 'limits.json'
PATH_OPS = PATH_DATA / 'ops.json'
PATH_MAIN = PATH_DATA / 'main.js'
PATH_URLS = PATH_DATA / 'csp.txt'
STRINGS = PATH_DATA / 'strings.txt'
PATHS = PATH_DATA / 'paths.txt'
JS_FILES_MAP = PATH_DATA / 'js.json'
JS_FILES = mkdir(PATH_DATA / 'js')
OPERATIONS = PATH_DATA / 'operations'

USER_AGENTS = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.',
]

_a = 'a.js'
_base = 'https://abs.twimg.com/responsive-web/client-web'


async def backoff(fn: callable, sem: Semaphore, *args, m: int = 20, b: int = 2, max_retries: int = 8, **kwargs) -> any:
    ignore_status_codes = kwargs.pop('ignore_status_codes', [])
    for i in range(max_retries + 1):
        try:
            async with sem:
                r = await fn(*args, **kwargs)
                if r.status_code in ignore_status_codes:
                    return r
                r.raise_for_status()
                return r
        except Exception as e:
            if i == max_retries:
                logger.warning(f'Max retries exceeded\n{e}')
                return
            t = min(random.random() * (b ** i), m)
            logger.info(f'Retrying in {f"{t:.2f}"} seconds\n{e}')
            await asyncio.sleep(t)


def download(urls: list[str], out: str = 'tmp', sz: int = None, fname_fn: partial = None, **kwargs) -> Generator:
    async def get(client: AsyncClient, sem: Semaphore, url: str):
        fname = url.split('/')[-1] if not fname_fn else fname_fn(url)
        async with aiofiles.open(f'{_out}/{fname}', 'wb') as fp:
            r = await backoff(client.get, sem, url, **kwargs)
            async for chunk in r.aiter_bytes(sz):
                await fp.write(chunk)
            return r

    _out = mkdir(out)
    return (partial(get, url=u) for u in urls)


def send(cfgs: list[dict], **kwargs) -> Generator:
    async def f(client: AsyncClient, sem: Semaphore, cfg: dict) -> Response:
        return await backoff(client.request, sem, **cfg, **kwargs)

    return (partial(f, cfg=cfg) for cfg in cfgs)


async def process(fns: Generator, max_connections: int = 2000, **kwargs):
    client_defaults = {
        'cookies': kwargs.pop('cookies', None),
        'headers': {'user-agent': random.choice(USER_AGENTS)} | kwargs.pop('headers', {}),
        'timeout': kwargs.pop('timeout', 30.0),
        'verify': kwargs.pop('verify', False),
        'http2': kwargs.pop('http2', True),
        'follow_redirects': kwargs.pop('follow_redirects', True),
        'limits': kwargs.pop('limits', Limits(
            max_connections=max_connections,
            max_keepalive_connections=None,
            keepalive_expiry=5.0,
        ))
    }
    # tqdm
    desc = kwargs.pop('desc', None)
    sem = Semaphore(max_connections)
    async with AsyncClient(**client_defaults, **kwargs) as client:
        tasks = (fn(client=client, sem=sem) for fn in fns)
        if desc:
            return await tqdm_asyncio.gather(*tasks, desc=desc)
        return await asyncio.gather(*tasks)


def _get_endpoints(res: Response, out: Path = JS_FILES_MAP) -> dict:
    temp = re.findall('\+"\."\+(\{.*\})\[e\]\+?' + '"' + _a + '"', res.text)[0]
    endpoints = orjson.loads(temp.replace('vendor:', '"vendor":').replace('api:', '"api":'))
    if out:
        out.write_bytes(dump_json(endpoints))
    return endpoints


def get_js_files(r: Response, out: Path = JS_FILES) -> None:
    endpoints = _get_endpoints(r)
    csp = sorted({x.strip(';') for x in r.headers.get("content-security-policy").split() if x.startswith("https://")})
    PATH_URLS.write_text('\n'.join(csp))
    urls = [
        f'{_base}/{k}.{v}{_a}'
        for k, v in endpoints.items()
        if not re.search(r'participantreaction|\.countries-|emojipicker|i18n|icons\/', k, flags=re.I)
    ]
    asyncio.run(process(download(urls, out=out), desc='Downloading JS files'))


def parse_matches(matches: list[tuple]) -> dict:
    d = {}
    for m in matches:
        d[m[1]] = {
            "queryId": m[0],
            "operationName": m[1],
            "operationType": m[2],
            "featureSwitches": sorted(re.sub(r'[\s"\']', '', x) for x in (m[3].split(',') if m[3] else [])),
            "fieldToggles": sorted(re.sub(r'[\s"\']', '', x) for x in (m[4].split(',') if m[4] else []))
        }
    return d


def main():
    client = Client(headers={'user-agent': random.choice(USER_AGENTS)}, follow_redirects=True, http2=True)
    r1 = client.get('https://x.com')
    PATH_HOMEPAGE.write_text(r1.text)

    try:
        get_js_files(r1)
    except Exception as e:
        logger.warning(f'Failed to get js files\t\t{e}')

    main_js = re.findall(r'href="(https\:\/\/abs\.twimg\.com\/responsive-web\/client-web\/main\.\w+\.js)"', r1.text)[0]
    r2 = client.get(main_js)
    PATH_MAIN.write_text(r2.text)

    expr = r'\{[^{}]*queryId:\s?"([^"]+)",\s*operationName:\s?"([^"]+)",\s*operationType:\s?"([^"]+)",\s*metadata:\s?\{\s*featureSwitches:\s?\[(.*?)\],\s*fieldToggles:\s?\[(.*?)\]\s*\}\s*\}'

    matches = re.findall(expr, r2.text, flags=re.A)
    ops = parse_matches(matches)

    # search all js files for more GraphQL operation definitions
    for p in JS_FILES.iterdir():
        matches = re.findall(expr, p.read_text(), flags=re.A)
        ops |= parse_matches(matches)

    PATH_OPS.write_bytes(dump_json(ops))
    html = LexborHTMLParser(PATH_HOMEPAGE.read_text())
    k = 'window.__INITIAL_STATE__='
    PATH_INITIAL_STATE.write_bytes(dump_json(chompjs.parse_js_object([x for x in html.css('script') if k in x.text()][0].text().replace(k, '').strip(';'))))

    data = orjson.loads(PATH_INITIAL_STATE.read_bytes())
    config = data['featureSwitch']['defaultConfig'] | data['featureSwitch']['user']['config']
    features = {k: v.get('value') for k, v in config.items() if isinstance(v.get('value'), bool)}
    numeric = {k: v.get('value') for k, v in config.items() if isinstance(v.get('value'), int) and not isinstance(v.get('value'), bool)}
    PATH_FEATURES.write_bytes(dump_json(features))
    PATH_LIMITS.write_bytes(dump_json(numeric))


if __name__ == '__main__':
    main()
