import json
import re
import subprocess
from pathlib import Path

import bs4
import requests
from requests import Session

from twitter.config.operations import operations as OLD

BOLD = '\u001b[1m'
SUCCESS = '\u001b[32m'
WARN = '\u001b[31m'
RESET = '\u001b[0m'

OUT_PATH = Path("endpoints/")
ENDPOINTS = Path('endpoints.json')
OPERATIONS = Path('operations_new')
OUT_PATH.mkdir(exist_ok=True, parents=True)


def find_api_script(res: requests.Response) -> str:
    """
    Find api script
    @param res: response from homepage: https://twitter.com
    @return: url to api script
    """
    for s in bs4.BeautifulSoup(res.text, 'html.parser').select('script'):
        temp = s.text.split('+"."+')[-1].split('[e]+"a.js"')[0]
        # temp = s.text.split('function(e){return e+"."+')[-1].split('[e]+"a.js"')[0]
        if temp.startswith('{'):
            endpoints = json.loads(temp.replace('vendor:', '"vendor":').replace('api:', '"api":'))
            ENDPOINTS.write_text(json.dumps(endpoints, indent=2))
            js = 'api.' + endpoints['api'] + "a.js"  # search for `+"a.js"` in homepage source
            return f'https://abs.twimg.com/responsive-web/client-web/{js}'


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

    js = 'const obj={},out=Object.entries(O[0]).forEach(([e,t])=>{let a=t(),o={};for(let r of a.metadata.featureSwitches)o[r]=!0;obj[a.operationName]={queryId:a.queryId,variables:{},features:o}});require("fs").writeFile("' + OPERATIONS.with_suffix('.json').name + '",JSON.stringify(obj,null,2),e=>e);'
    js_out = OPERATIONS.with_suffix('.js')
    js_out.expanduser().write_text(f"O={temp};" + js)
    subprocess.run(f'node {js_out}', shell=True)
    return js_out, json.loads(Path(OPERATIONS.with_suffix('.json')).read_text())


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


def main() -> int:
    update_operations(Session())
    return 0


if __name__ == '__main__':
    exit(main())
