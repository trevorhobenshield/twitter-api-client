import ujson


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


def traverse_dict(d: dict, *args):
    for k in args:
        d = d.get(k, {})
    return d


def get_headers(session) -> dict:
    """
    Get the headers required for authenticated requests

    @param session: special requests.Session object, modified during login process. contains attribute `tokens`
    @return: dict representing headers
    """
    return {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'cookie': '; '.join(f'{k}={v}' for k, v in session.cookies.items()),
        'referer': 'https://twitter.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'x-csrf-token': session.cookies.get('ct0'),
        "x-guest-token": session.cookies.get('guest_token'),
        "x-twitter-auth-type": "OAuth2Session" if session.cookies.get("auth_token") else '',
        "x-twitter-active-user": "yes",
        "x-twitter-client-language": 'en',
    }


def build_query(params):
    return '&'.join(f'{k}={ujson.dumps(v)}' for k, v in params.items())
