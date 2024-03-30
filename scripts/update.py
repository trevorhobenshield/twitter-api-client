import re
from pathlib import Path

import orjson
from httpx import Client

PATH_OPS = Path('ops.json')
PATH_MAIN = Path('main.js')


def _get_ops(client: Client) -> None:
    r1 = client.get('https://twitter.com')
    m = re.findall('href="(https\:\/\/abs\.twimg\.com\/responsive-web\/client-web\/main\.\w+\.js)"', r1.text)
    r2 = client.get(m[0])
    PATH_MAIN.write_text(r2.text)

    expr = r'\{[^{}]*queryId:\s?"([^"]+)",\s*operationName:\s?"([^"]+)",\s*operationType:\s?"([^"]+)",\s*metadata:\s?\{\s*featureSwitches:\s?\[(.*?)\],\s*fieldToggles:\s?\[(.*?)\]\s*\}\s*\}'
    matches = re.findall(expr, r2.text, flags=re.A)
    D = {}
    for m in matches:
        D[m[1]] = {
            "queryId": m[0],
            "operationName": m[1],
            "operationType": m[2],
            "featureSwitches": sorted(re.sub(r'[\s"\']', '', x) for x in (m[3].split(',') if m[3] else [])),
            "fieldToggles": sorted(re.sub(r'[\s"\']', '', x) for x in (m[4].split(',') if m[4] else []))
        }
    PATH_OPS.write_bytes(orjson.dumps(D, option=orjson.OPT_INDENT_2 | orjson.OPT_SORT_KEYS))


def main():
    c = Client(headers={'user-agent': 'Chrome/110.0.0.0'}, follow_redirects=True)
    _get_ops(c)


if __name__ == '__main__':
    main()
