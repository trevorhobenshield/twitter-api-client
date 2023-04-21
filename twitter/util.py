import time
from pathlib import Path
from urllib.parse import urlsplit, urlencode, urlunsplit, parse_qs, quote

import orjson

from .constants import GREEN, MAGENTA, RED, RESET


def set_qs(url: str, qs: dict, update=False, **kwargs) -> str:
    *_, q, f = urlsplit(url)
    return urlunsplit((*_, urlencode(qs | parse_qs(q) if update else qs, doseq=True, quote_via=quote,
                                     safe=kwargs.get('safe', '')), f))


def get_cursor(data: list | dict) -> str:
    # inefficient, but need to deal with arbitrary schema
    entries = find_key(data, 'entries')
    if entries:
        for entry in entries.pop():
            entry_id = entry.get('entryId', '')
            if ('cursor-bottom' in entry_id) or ('cursor-showmorethreads' in entry_id):
                content = entry['content']
                if itemContent := content.get('itemContent'):
                    return itemContent['value']  # v2 cursor
                return content['value']  # v1 cursor


def get_headers(session, **kwargs) -> dict:
    """
    Get the headers required for authenticated requests
    """
    headers = kwargs | {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'cookie': '; '.join(f'{k}={v}' for k, v in session.cookies.items()),
        'referer': 'https://twitter.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; Nokia G20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36',
        'x-csrf-token': session.cookies.get('ct0', ''),
        'x-guest-token': session.cookies.get('guest_token', ''),
        'x-twitter-auth-type': 'OAuth2Session' if session.cookies.get('auth_token') else '',
        'x-twitter-active-user': 'yes',
        'x-twitter-client-language': 'en',
    }
    return dict(sorted({k.lower(): v for k, v in headers.items()}.items()))


def fmt_status(status: int) -> str:
    color = None
    if 200 <= status < 300:
        color = GREEN
    elif 300 <= status < 400:
        color = MAGENTA
    elif 400 <= status < 600:
        color = RED
    return f'[{color}{status}{RESET}]'


def save_data(data: list, op: str, key: str | int):
    try:
        path = Path(f'data/raw/{key}')
        path.mkdir(parents=True, exist_ok=True)
        (path / f'{time.time_ns()}_{op}.json').write_text(
            orjson.dumps(data, option=orjson.OPT_INDENT_2).decode(),
            encoding='utf-8'
        )
    except Exception as e:
        print(f'failed to save data: {e}')


def find_key(obj: any, key: str) -> list:
    """
    Find all values of a given key within a nested dict or list of dicts

    @param obj: dictionary or list of dictionaries
    @param key: key to search for
    @return: list of values
    """

    def helper(obj: any, key: str, L: list) -> list:
        if not obj:
            return L

        if isinstance(obj, list):
            for e in obj:
                L.extend(helper(e, key, []))
            return L

        if isinstance(obj, dict) and obj.get(key):
            L.append(obj[key])

        if isinstance(obj, dict) and obj:
            for k in obj:
                L.extend(helper(obj[k], key, []))
        return L

    return helper(obj, key, [])
