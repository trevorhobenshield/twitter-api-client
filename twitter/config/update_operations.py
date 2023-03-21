import json
import re
import subprocess
from pathlib import Path

import bs4
import requests
from requests import Session

from operations import operations as OLD


def find_api_script(res: requests.Response) -> str:
    """
    Find api script
    @param res: response from homepage: https://twitter.com
    @return: url to api script
    """
    for s in bs4.BeautifulSoup(res.text, 'html.parser').select('script'):
        if x := re.search('(?<=api:")\w+(?=")', s.text):
            key = x.group() + 'a'  # wtf?
            return f'https://abs.twimg.com/responsive-web/client-web/api.{key}.js'


def get_operations(session: Session) -> tuple:
    """
    Get operations and their respective queryId and feature definitions
    @return: list of operations
    """
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }
    r1 = session.get('https://twitter.com', headers=headers)
    script = find_api_script(r1)
    r2 = session.get(script, headers=headers)
    temp = '[{' + re.search('\d+:e=>\{e\.exports=\{.*?(?=,\d+:e=>\{"use strict";)', r2.text).group() + '}]'
    temp = re.sub('e\.exports=', 'return', temp)

    fname = 'operations_new'
    js = 'const obj={},out=Object.entries(O[0]).forEach(([e,t])=>{let a=t(),o={};for(let r of a.metadata.featureSwitches)o[r]=!0;obj[a.operationName]={queryId:a.queryId,variables:{},features:o}});require("fs").writeFile("' + fname + '.json",JSON.stringify(obj,null,2),e=>e);'
    js_out = f'{fname}.js'
    Path(js_out).expanduser().write_text(f"O={temp};" + js)
    subprocess.run(f'node {js_out}', shell=True)
    return fname, json.loads(Path(f'{fname}.json').read_text())


def update_operations(session: Session):
    """
    Update operations.json with queryId and feature definitions
    @param path: path to operations file
    @return: updated operations
    """
    fname, NEW = get_operations(session)
    out = Path(f'{fname}.py')
    for k in NEW:
        if k in OLD:
            OLD[k]['features'] |= NEW[k]['features']
            OLD[k]['queryId'] = NEW[k]['queryId']
        else:
            print(f'NEW operation: {k}')
            OLD[k] = NEW[k]
    out.write_text(f'operations = {OLD}')


def main() -> int:
    update_operations(Session())
    return 0


if __name__ == '__main__':
    exit(main())
