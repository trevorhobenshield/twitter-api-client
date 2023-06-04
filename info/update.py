import asyncio
import platform
import re
import subprocess
from pathlib import Path

import orjson
import requests
from httpx import AsyncClient, Client

from twitter.constants import *

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

_a = 'a.js'
_base = 'https://abs.twimg.com/responsive-web/client-web'

STRINGS = Path('strings.txt')
PATHS = Path('paths.txt')
JS_FILES_MAP = Path('js.json')
JS_FILES = Path('js')
OPERATIONS = Path('operations')
JS_FILES.mkdir(exist_ok=True, parents=True)


def find_api_script(res: requests.Response) -> str:
    """
    Find api script
    @param res: response from homepage: https://twitter.com
    @return: url to api script
    """
    temp = re.findall('\+"\."\+(\{.*\})\[e\]\+?' + '"' + _a + '"', res.text)[0]
    endpoints = orjson.loads(temp.replace('vendor:', '"vendor":').replace('api:', '"api":'))
    JS_FILES_MAP.write_bytes(orjson.dumps(dict(sorted(endpoints.items()))))
    js = 'api.' + endpoints['api'] + _a  # search for `+"a.js"` in homepage source
    return f'{_base}/{js}'


def get_operations(session: Client) -> None:
    """
    Get operations and their respective queryId and feature definitions
    @return: list of operations
    """
    r1 = session.get('https://twitter.com')
    script = find_api_script(r1)
    r2 = session.get(script)
    temp = '[{' + re.search('\d+:\w=>\{\w\.exports=\{.*?(?=,\d+:\w=>\{"use strict";)', r2.text).group() + '}]'
    temp = re.sub('\w\.exports=', 'return', temp)

    js = 'const obj={},out=Object.entries(O[0]).forEach(([e,t])=>{let a=t(),o={};for(let r of a.metadata.featureSwitches)o[r]=!0;obj[a.operationName]={queryId:a.queryId,variables:{},features:o}});require("fs").writeFile("' + OPERATIONS.with_suffix(
        '.json').name + '",JSON.stringify(obj,null,2),e=>e);'
    js_out = OPERATIONS.with_suffix('.js')
    js_out.expanduser().write_text(f"O={temp};" + js)
    subprocess.run(f'node {js_out}', shell=True)


async def process(session: Client, fn: callable, urls: any, **kwargs) -> list:
    async with AsyncClient(follow_redirects=True, headers=session.headers) as s:
        return await asyncio.gather(*(fn(s, u, **kwargs) for u in urls))


async def get(session: AsyncClient, url: str, **kwargs) -> tuple[str, str]:
    try:
        logger.debug(f"GET {url}")
        r = await session.get(url)
        return url, r.text
    except Exception as e:
        logger.error(f"[{RED}failed{RESET}] Failed to get {url}\n{e}")


def get_js(res: list):
    for url, r in res:
        u = url.split('/')[-1]
        (JS_FILES / u).write_text(r)
    subprocess.run(f'prettier --write "{JS_FILES.name}/*.js" {JS_FILES_MAP}', shell=True)


def get_strings():
    # find strings < 120 chars long
    # queryId's are usually 22 chars long
    s = set()
    for p in JS_FILES.iterdir():
        s |= set(x.strip() for x in re.split('["\'`]', p.read_text()) if
                 # ((len(x) == 22) and (not re.search('[\[\]\{\}\(\)]', x))))
                 ((len(x) < 120) and (not re.search('[\[\]\{\}\(\)]', x))))
    STRINGS.write_text('\n'.join(sorted(s, reverse=True)))
    PATHS.write_text('\n'.join(sorted(s for s in s if '/' in s)))


def get_features():
    operations = orjson.loads(OPERATIONS.with_suffix('.json').read_bytes())
    features = {}
    for k, v in operations.items():
        features |= v.get('features', {})
    Path('features.json').write_bytes(orjson.dumps(dict(sorted(features.items())), option=orjson.OPT_INDENT_2))


def main():
    session = Client(headers={
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }, follow_redirects=True)
    get_operations(session)
    urls = (
        f'{_base}/{k}.{v}{_a}'
        for k, v in orjson.loads(JS_FILES_MAP.read_text()).items()
        if not re.search('participantreaction|\.countries-|emojipicker|i18n|icons\/', k, flags=re.I)
        # if 'endpoint' in k
    )
    res = asyncio.run(process(session, get, urls))
    get_js(res)
    get_strings()
    get_features()


if __name__ == '__main__':
    main()
