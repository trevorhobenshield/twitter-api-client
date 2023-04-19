import math
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import wraps, partial

import orjson
from requests import Session, Response
from tqdm import tqdm

from .util import log_config, logging, find_key, save_data, get_cursor, SUCCESS, WARN, ERROR, RESET
from .operation import Operation

logging.config.dictConfig(log_config)
logger = logging.getLogger(__name__)


def log(fn=None, *, level: int = logging.DEBUG, info: int = 0) -> callable:
    if fn is None:
        return partial(log, level=level, info=info)

    @wraps(fn)
    def wrapper(*args, **kwargs):
        r = fn(*args, **kwargs)
        if not info:
            return r
        info_level = {
            1: f'({fn.__name__}) {r}',
            2: f'({fn.__name__}) {r} {r.url}',
            3: f'({fn.__name__}) {r} {r.url}\n{r.text}',
            4: f'({fn.__name__}) {r} {r.url}\n{r.text}\n{r.request.headers}\n{r.headers}\n{r.cookies}',
        }

        if 'json' in r.headers.get('content-type', ''):
            if r.json().get('errors'):
                logger.debug(f'[{ERROR}error{RESET}] {info_level[info]}')
                return r

        if r.status_code == 200:
            logger.debug(f'[{SUCCESS}success{RESET}] {info_level[info]}')
        elif r.status_code < 400:
            logger.debug(f'[{WARN}warning{RESET}] {info_level[info]}')
        else:
            logger.debug(f'[{ERROR}error{RESET}] {info_level[info]}')

        return r

    return wrapper


class Scraper:
    def __init__(self):
        self.session = Session()
        self.guest_token = self.get_guest_token()
        self.api = 'https://twitter.com/i/api/graphql'

    # @log(info=2)
    def _query(self, operation: tuple, key: int | str | list[int], **kwargs) -> Response:
        qid, op, k = operation
        headers = self.get_headers()
        params = {k: orjson.dumps(v).decode() for k, v in {
            'variables': {k: key} | kwargs | Operation.default_variables,
            'features': Operation.default_features,
        }.items()}
        r = self.session.get(f'{self.api}/{qid}/{op}', params=params, headers=headers)
        save_data(r.json(), op, key)
        if r.status_code == 429:
            raise Exception(f'rate limit exceeded: {r.url}')
        return r

    def _threaded_query(self, op: tuple, ids: list[str | int], **kwargs) -> list[dict]:
        res = []
        with tqdm(total=len(ids), desc=f'query {op[1]}') as pbar:
            with ThreadPoolExecutor(max_workers=kwargs.pop('max_workers', 32)) as e:
                for future in as_completed(e.submit(self._query, op, x, **kwargs) for x in ids):
                    res.append(future.result().json())
                    pbar.update(1)
        return res

    def _threaded_pagination(self, op: tuple, ids: list[str | int], limit: int, **kwargs) -> list[dict]:
        def fn(op: tuple, _id, **kwargs) -> list[dict]:
            r = self._query(op, _id, **kwargs)
            data = self.paginate(op, _id, r.json(), limit)
            data.extend(r.json())
            return data

        res = []
        with tqdm(total=len(ids), desc=f'(pagination) query {op[1]}') as pbar:
            with ThreadPoolExecutor(max_workers=kwargs.pop('max_workers', 32)) as e:
                for future in as_completed(e.submit(fn, op, x, **kwargs) for x in ids):
                    res.extend(future.result())
                    pbar.update(1)
        return res

    def profile_spotlight(self, screen_names: list[str], **kwargs) -> list:
        return self._threaded_query(Operation.ProfileSpotlightsQuery, screen_names, **kwargs)

    def users(self, screen_names: list[str], **kwargs) -> list:
        return self._threaded_query(Operation.UserByScreenName, screen_names, **kwargs)

    def users_by_id(self, user_ids: list[int], **kwargs) -> list[dict]:
        return self._threaded_query(Operation.UserByRestId, user_ids, **kwargs)

    def tweets_by_id(self, tweet_ids: list[int], **kwargs) -> list[dict]:
        return self._threaded_query(Operation.TweetResultByRestId, tweet_ids, **kwargs)

    def tweets_details(self, tweet_ids: list[int], limit=math.inf, **kwargs) -> list[dict]:
        return self._threaded_pagination(Operation.TweetDetail, tweet_ids, limit, **kwargs)

    def tweets(self, user_ids: list[int], limit=math.inf, **kwargs) -> list[dict]:
        return self._threaded_pagination(Operation.UserTweets, user_ids, limit, **kwargs)

    def tweets_and_replies(self, user_ids: list[int], limit=math.inf, **kwargs) -> list[dict]:
        return self._threaded_pagination(Operation.UserTweetsAndReplies, user_ids, limit, **kwargs)

    def media(self, user_ids: list[int], limit=math.inf, **kwargs) -> list[dict]:
        return self._threaded_pagination(Operation.UserMedia, user_ids, limit, **kwargs)

    # special case, batch query
    def users_by_ids(self, user_ids: list[int], **kwargs) -> dict:
        return self._query(Operation.UsersByRestIds, user_ids, **kwargs).json()

    def paginate(self, op: tuple, key: int | str | list[int], initial_result: dict, limit: int) -> list[dict]:
        res = []
        ids = set(find_key(initial_result, 'rest_id'))
        dups = 0
        DUP_LIMIT = 5

        cursor = get_cursor(initial_result)
        while dups < DUP_LIMIT:
            prev_len = len(ids)
            if prev_len >= limit:
                return res

            r = self._query(op, key, cursor=cursor)
            data = r.json()

            if r.status_code == 429:
                raise Exception(f'rate limit exceeded: {r.url}')

            cursor = get_cursor(data)
            ids |= set(find_key(data, 'rest_id'))

            if prev_len == len(ids):
                dups += 1

            res.append(data)
        return res

    def get_headers(self, **kwargs) -> dict:
        headers = kwargs | {
            'authority': 'twitter.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en;q=0.9',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'pragma': 'no-cache',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; Nokia G20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36',
            'x-guest-token': self.guest_token,
            'x-twitter-active-user': 'yes',
            'x-twitter-client-language': 'en-GB',
        }
        # lowercase and sorted sometimes matters (e.g. tiktok/aws)
        return dict(sorted({k.lower(): v for k, v in headers.items()}.items()))

    def get_guest_token(self) -> str:
        return Session().post('https://api.twitter.com/1.1/guest/activate.json', headers={
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; Nokia G20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36'
        }).json()['guest_token']
