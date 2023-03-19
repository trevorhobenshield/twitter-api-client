import json
import re
from pathlib import Path
import bs4
import requests
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


def get_operations() -> list[dict]:
    """
    Get operations and their respective queryId and feature definitions
    @return: list of operations
    """
    session = requests.Session()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    script = find_api_script(session.get('https://twitter.com', headers=headers))
    r = session.get(script, headers=headers)
    res = ''
    # find operations and their respective queryId and feature definitions
    for x in re.split(r'\d+:e=>{e.exports=', r.text)[1:]:
        res = res.replace('}}},{', '}},{')
        if x.startswith('{queryId:') and '"use strict"' not in x:
            for k in ['queryId', 'operationName', 'operationType', 'metadata', 'featureSwitches']:
                x = x.replace(k, f'"{k}"')
            res += x
    return json.loads(f'[{res[:-2]}]')


def update_operations(path=Path('operations_new.json')):
    """
    Update operations.json with queryId and feature definitions
    @param path: path to operations file
    @return: updated operations
    """

    def merge(new, out=Path('operations_new.py')):
        for k in new:
            if k in OLD:
                OLD[k]['features'] |= new[k]['features']
                OLD[k]['queryId'] = new[k]['queryId']
            else:
                print(f'new operation: {k}')
                OLD[k] = new[k]
        out.write_text(f'operations = {OLD}')

    operation_types = {}
    operations = get_operations()
    config = {}
    for o in operations:
        operation_types.setdefault(o['operationType'], []).append(o["operationName"])
        config[o['operationName']] = {
            'queryId': o['queryId'],
            'variables': {},
            'features': {k: True for k in o['metadata']['featureSwitches']}
        }
    # path.write_text(json.dumps(config, indent=2))
    # print(f'{operation_types = }')
    # print(f'{operation_types.keys() = }')
    merge(config)


def main() -> int:
    update_operations()
    return 0


if __name__ == '__main__':
    exit(main())
