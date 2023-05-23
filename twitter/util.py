import re
import time
from pathlib import Path
from urllib.parse import urlsplit, urlencode, urlunsplit, parse_qs, quote
import orjson

from .constants import GREEN, MAGENTA, RED, RESET
import protonmail


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


def init_session(email: str, password: str) -> protonmail.api.Session:
    """
    Create an authenticated Proton Mail session

    @param email: your email. Can also use username
    @param password: your password
    @return: Proton Mail Session object
    """
    cwd = Path.cwd()
    log_dir_path = cwd / 'protonmail_log'
    cache_dir_path = cwd / 'protonmail_cache'
    try:
        session = protonmail.api.Session(
            api_url="https://api.protonmail.ch",
            log_dir_path=log_dir_path,
            cache_dir_path=cache_dir_path,
            user_agent="Ubuntu_20.04",
            tls_pinning=False,
        )
        session.enable_alternative_routing = False
        session.authenticate(email, password)
        return session
    except Exception as e:
        print('Failed to initialize Proton Mail Session:', e)


def get_inbox(session: protonmail.api.Session) -> dict:
    """
    Get inbox

    @param session: Proton Mail Session object
    @return: inbox data
    """
    try:
        return session.api_request(
            "/api/mail/v4/conversations",
            method="GET",
            params={
                'Page': 0,
                'PageSize': 50,
                'Limit': 100,
                'LabelID': 0,
                'Sort': 'Time',
                'Desc': 1,
            }
        )
    except Exception as e:
        print('Failed to get inbox:', e)


def get_verification_code(inbox: dict) -> str:
    """
    Get Twitter verification code from inbox.

    Crude implementation. Subject line contains verification code, no need to decrypt message body.

    @param inbox: inbox data
    @return: Twitter verification code
    """
    try:
        expr = '(\w+) is your Twitter verification code'
        return list(filter(len, (re.findall(expr, conv['Subject']) for conv in inbox['Conversations'])))[0][0]
    except Exception as e:
        print('Failed to get Twitter verification code:', e)


def get_confirmation_code(inbox: dict) -> str:
    """
    Get Twitter confirmation code from inbox.

    Crude implementation. Subject line contains confirmation code, no need to decrypt message body.

    @param inbox: inbox data
    @return: Twitter confirmation code
    """
    try:
        expr = 'Your Twitter confirmation code is (\w+)'
        return list(filter(len, (re.findall(expr, conv['Subject']) for conv in inbox['Conversations'])))[0][0]
    except Exception as e:
        print('Failed to get Twitter confirmation code:', e)
