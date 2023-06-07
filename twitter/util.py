import re
import time
from logging import Logger
from pathlib import Path
from urllib.parse import urlsplit, urlencode, urlunsplit, parse_qs, quote

import orjson
# import protonmail
from httpx import Response, Client

from .constants import GREEN, MAGENTA, RED, RESET, ID_MAP


def init_session():
    client = Client(headers={
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }, follow_redirects=True)
    r = client.post('https://api.twitter.com/1.1/guest/activate.json').json()
    client.headers.update({
        'content-type': 'application/json',
        'x-guest-token': r['guest_token'],
        'x-twitter-active-user': 'yes',
    })
    return client


def batch_ids(ids: list[int], char_limit: int = 4_500) -> list[dict]:
    """ To avoid 431 errors """
    length = 0
    res, batch = [], []
    for x in map(str, ids):
        curr_length = len(x)
        if length + curr_length > char_limit:
            res.append(batch)
            batch = []
            length = 0
        batch.append(x)
        length += curr_length
    if batch:
        res.append(batch)
    return res


def build_params(params: dict) -> dict:
    return {k: orjson.dumps(v).decode() for k, v in params.items()}


def save_json(r: Response, path: Path, name: str, **kwargs):
    try:
        data = r.json()
        kwargs.pop('cursor', None)
        out = path / '_'.join(map(str, kwargs.values()))
        out.mkdir(parents=True, exist_ok=True)
        (out / f'{time.time_ns()}_{name}.json').write_bytes(orjson.dumps(data))
    except Exception as e:
        print(f'Failed to save data: {e}')


def flatten(seq: list | tuple) -> list:
    flat = []
    for e in seq:
        if isinstance(e, list | tuple):
            flat.extend(flatten(e))
        else:
            flat.append(e)
    return flat


def get_json(res: list[Response], **kwargs) -> list:
    cursor = kwargs.get('cursor')
    temp = res
    if any(isinstance(r, (list, tuple)) for r in res):
        temp = flatten(res)
    results = []
    for r in temp:
        try:
            data = r.json()
            if cursor:
                results.append([data, cursor])
            else:
                results.append(data)
        except Exception as e:
            print('Cannot parse JSON response', e)
    return results


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
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-csrf-token': session.cookies.get('ct0', ''),
        'x-guest-token': session.cookies.get('guest_token', ''),
        'x-twitter-auth-type': 'OAuth2Session' if session.cookies.get('auth_token') else '',
        'x-twitter-active-user': 'yes',
        'x-twitter-client-language': 'en',
    }
    return dict(sorted({k.lower(): v for k, v in headers.items()}.items()))


def find_key(obj: any, key: str) -> list:
    """
    Find all values of a given key within a nested dict or list of dicts

    Most data of interest is nested, and sometimes defined by different schemas.
    It is not worth our time to enumerate all absolute paths to a given key, then update
    the paths in our parsing functions every time Twitter changes their API.
    Instead, we recursively search for the key here, then run post-processing functions on the results.

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


def log(logger: Logger, level: int, r: Response):
    def stat(r, txt, data):
        if level >= 1:
            logger.debug(f'{r.url.path}')
        if level >= 2:
            logger.debug(f'{r.url}')
        if level >= 3:
            logger.debug(f'{txt}')
        if level >= 4:
            logger.debug(f'{data}')

        try:
            limits = {k: v for k, v in r.headers.items() if 'x-rate-limit' in k}
            current_time = int(time.time())
            wait = int(r.headers.get('x-rate-limit-reset', current_time)) - current_time
            remaining = limits.get('x-rate-limit-remaining')
            limit = limits.get('x-rate-limit-limit')
            logger.debug(f"remaining: {MAGENTA}{remaining}/{limit}{RESET} requests")
            logger.debug(f'reset:     {MAGENTA}{(wait / 60):.2f}{RESET} minutes')
        except Exception as e:
            logger.error(f'Rate limit info unavailable: {e}')

    try:
        status = r.status_code
        txt, data, = r.text, r.json()
        if 'json' in r.headers.get('content-type', ''):
            if data.get('errors') and not find_key(data, 'instructions'):
                logger.error(f'[{RED}error{RESET}] {status} {data}')
            else:
                logger.debug(fmt_status(status))
                stat(r, txt, data)
        else:
            logger.debug(fmt_status(status))
            stat(r, txt, {})
    except Exception as e:
        logger.error(f'Failed to log: {e}')


def fmt_status(status: int) -> str:
    color = None
    if 200 <= status < 300:
        color = GREEN
    elif 300 <= status < 400:
        color = MAGENTA
    elif 400 <= status < 600:
        color = RED
    return f'[{color}{status}{RESET}]'


def get_ids(data: list | dict, operation: tuple) -> set:
    expr = ID_MAP[operation[-1]]
    return {k for k in find_key(data, 'entryId') if re.search(expr, k)}

# def init_protonmail_session(email: str, password: str) -> protonmail.api.Session:
#     """
#     Create an authenticated Proton Mail session
#
#     @param email: your email. Can also use username
#     @param password: your password
#     @return: Proton Mail Session object
#     """
#     cwd = Path.cwd()
#     log_dir_path = cwd / 'protonmail_log'
#     cache_dir_path = cwd / 'protonmail_cache'
#     try:
#         session = protonmail.api.Session(
#             api_url="https://api.protonmail.ch",
#             log_dir_path=log_dir_path,
#             cache_dir_path=cache_dir_path,
#             user_agent="Ubuntu_20.04",
#             tls_pinning=False,
#         )
#         session.enable_alternative_routing = False
#         session.authenticate(email, password)
#         return session
#     except Exception as e:
#         print('Failed to initialize Proton Mail Session:', e)
#
#
# def get_inbox(session: protonmail.api.Session) -> dict:
#     """
#     Get inbox
#
#     @param session: Proton Mail Session object
#     @return: inbox data
#     """
#     try:
#         return session.api_request(
#             "/api/mail/v4/conversations",
#             method="GET",
#             params={
#                 'Page': 0,
#                 'PageSize': 50,
#                 'Limit': 100,
#                 'LabelID': 0,
#                 'Sort': 'Time',
#                 'Desc': 1,
#             }
#         )
#     except Exception as e:
#         print('Failed to get inbox:', e)
#
#
# def get_verification_code(inbox: dict) -> str:
#     """
#     Get Twitter verification code from inbox.
#
#     Crude implementation. Subject line contains verification code, no need to decrypt message body.
#
#     @param inbox: inbox data
#     @return: Twitter verification code
#     """
#     try:
#         expr = '(\w+) is your Twitter verification code'
#         return list(filter(len, (re.findall(expr, conv['Subject']) for conv in inbox['Conversations'])))[0][0]
#     except Exception as e:
#         print('Failed to get Twitter verification code:', e)
#
#
# def get_confirmation_code(inbox: dict) -> str:
#     """
#     Get Twitter confirmation code from inbox.
#
#     Crude implementation. Subject line contains confirmation code, no need to decrypt message body.
#
#     @param inbox: inbox data
#     @return: Twitter confirmation code
#     """
#     try:
#         expr = 'Your Twitter confirmation code is (\w+)'
#         return list(filter(len, (re.findall(expr, conv['Subject']) for conv in inbox['Conversations'])))[0][0]
#     except Exception as e:
#         print('Failed to get Twitter confirmation code:', e)
