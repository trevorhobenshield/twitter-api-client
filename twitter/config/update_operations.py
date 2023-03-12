import re
import json
import requests
import bs4
from pathlib import Path


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


def update_operations(path=Path('operations.json')):
    """
    Update operations.json with queryId and feature definitions
    @param path: path to operations file
    @return: updated operations
    """
    operations = get_operations()
    # update operations file
    if path.stat().st_size == 0:
        # empty file, add all operations
        config = {}
        for o in operations:
            config[o['operationName']] = {
                'queryId': o['queryId'],
                'variables': {},
                'features': {k: True for k in o['metadata']['featureSwitches']}
            }
    else:
        config = json.loads(path.read_text())
        # update queryId and features for all operations
        for o in operations:
            config[o['operationName']]['queryId'] = o['queryId']
            config[o['operationName']]['features'] = {k: True for k in o['metadata']['featureSwitches']}
    path.write_text(json.dumps(config, indent=2))
    return config


def main() -> int:
    update_operations()
    # todo: currently need to manually convert json to python file
    return 0


if __name__ == '__main__':
    exit(main())