import asyncio
import logging.config
import re
import subprocess
from pathlib import Path

import aiohttp
import bs4
import nest_asyncio
import orjson
import requests
import uvloop
from requests import Session

from twitter.config.log import log_config
from twitter.config.operations import operations as OLD

logger = logging.getLogger(__name__)
logging.config.dictConfig(log_config)
nest_asyncio.apply()
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

BOLD = '\u001b[1m'
SUCCESS = '\u001b[32m'
WARN = '\u001b[31m'
RESET = '\u001b[0m'

IDENTIFIER = 'a.js'
BASE_URL_JS = 'https://abs.twimg.com/responsive-web/client-web'

PATHS = Path('paths.txt')
ENDPOINTS = Path('endpoints.json')
OUT_PATH = Path('endpoints')
OPERATIONS = Path('operations_new')
OUT_PATH.mkdir(exist_ok=True, parents=True)


def find_api_script(res: requests.Response) -> str:
    """
    Find api script
    @param res: response from homepage: https://twitter.com
    @return: url to api script
    """
    for s in bs4.BeautifulSoup(res.text, 'html.parser').select('script'):
        # temp = s.text.split('+"."+')[-1].split('[e]+"a.js"')[0]
        # temp = s.text.split('function(e){return e+"."+')[-1].split('[e]+"a.js"')[0]
        temp = re.split(f'\[\w+\]\+"{IDENTIFIER}"', s.text.split('+"."+')[-1])[0]
        if temp.startswith('{'):
            endpoints = orjson.loads(temp.replace('vendor:', '"vendor":').replace('api:', '"api":'))
            ENDPOINTS.write_bytes(orjson.dumps(endpoints))
            js = 'api.' + endpoints['api'] + IDENTIFIER  # search for `+"a.js"` in homepage source
            return f'{BASE_URL_JS}/{js}'


def get_operations(session: Session) -> tuple:
    """
    Get operations and their respective queryId and feature definitions
    @return: list of operations
    """
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }
    r1 = session.get('https://twitter.com', headers=headers)
    script = find_api_script(r1)
    r2 = session.get(script, headers=headers)
    temp = '[{' + re.search('\d+:e=>\{e\.exports=\{.*?(?=,\d+:e=>\{"use strict";)', r2.text).group() + '}]'
    temp = re.sub('e\.exports=', 'return', temp)

    js = 'const obj={},out=Object.entries(O[0]).forEach(([e,t])=>{let a=t(),o={};for(let r of a.metadata.featureSwitches)o[r]=!0;obj[a.operationName]={queryId:a.queryId,variables:{},features:o}});require("fs").writeFile("' + OPERATIONS.with_suffix(
        '.json').name + '",JSON.stringify(obj,null,2),e=>e);'
    js_out = OPERATIONS.with_suffix('.js')
    js_out.expanduser().write_text(f"O={temp};" + js)
    subprocess.run(f'node {js_out}', shell=True)
    return js_out, orjson.loads(Path(OPERATIONS.with_suffix('.json')).read_bytes())


def update_operations(session: Session):
    """
    Update operations.json with queryId and feature definitions

    @param path: path to operations file
    @return: updated operations
    """
    fname, NEW = get_operations(session)
    out = fname.with_suffix('.py')
    for k in NEW:
        if k in OLD:
            OLD[k]['features'] |= NEW[k]['features']
            OLD[k]['queryId'] = NEW[k]['queryId']
        else:
            print(f'NEW operation: {k}')
            OLD[k] = NEW[k]
    out.write_text(f'operations = {OLD}')


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


def update_endpoints(res: list):
    # update endpoints, remove old files
    current_files = {p.name.split('.')[1]: p.name for p in OUT_PATH.iterdir()}
    for url, r in res:
        u = url.split('/')[-1]
        if x := current_files.get(u.split('.')[1]):
            (OUT_PATH / x).unlink()
            (OUT_PATH / u).write_text(r)
    subprocess.run(f'prettier --write "{OUT_PATH.name}/*.js" {ENDPOINTS}', shell=True)


def main():
    update_operations(Session())
    urls = (
        f'{BASE_URL_JS}/{k}.{v}{IDENTIFIER}'
        for k, v in orjson.loads(ENDPOINTS.read_text()).items() if 'endpoint' in k
    )
    headers = get_headers()
    res = asyncio.run(process(get, headers, urls))
    update_endpoints(res)
    find_paths()


if __name__ == '__main__':
    main()
