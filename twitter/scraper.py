import asyncio
import logging.config
import math
import platform
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlsplit

import httpx
import orjson
from httpx import AsyncClient, Response
from tqdm import tqdm

from .constants import *
from .login import login
from .util import find_key, save_data, get_cursor, get_headers, set_qs, fmt_status

logging.config.dictConfig(log_config)
logger = logging.getLogger(__name__)

try:
    if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
        import nest_asyncio

        nest_asyncio.apply()
except:
    ...

if platform.system() != 'Windows':
    try:
        import uvloop

        uvloop.install()
    except ImportError as e:
        ...


class Scraper:
    def __init__(self, email: str, username: str, password: str, *, save=True, debug=False):
        self.session = login(email, username, password)
        self.api = 'https://twitter.com/i/api/graphql'
        self.save = save
        self.debug = debug

    def users(self, screen_names: list[str]) -> list:
        return self._run(screen_names, Operation.UserByScreenName)

    def tweets_by_id(self, tweet_ids: list[int]) -> list[dict]:
        return self._run(tweet_ids, Operation.TweetResultByRestId)

    def tweets_details(self, tweet_ids: list[int], limit=math.inf) -> list[dict]:
        return self._run(tweet_ids, Operation.TweetDetail, limit)

    def tweets(self, user_ids: list[int], limit=math.inf) -> list[dict]:
        return self._run(user_ids, Operation.UserTweets, limit)

    def tweets_and_replies(self, user_ids: list[int], limit=math.inf) -> list[dict]:
        return self._run(user_ids, Operation.UserTweetsAndReplies, limit)

    def media(self, user_ids: list[int], limit=math.inf) -> list[dict]:
        return self._run(user_ids, Operation.UserMedia, limit)

    def likes(self, user_ids: list[int], limit=math.inf) -> list[dict]:
        return self._run(user_ids, Operation.Likes, limit)

    def followers(self, user_ids: list[int], limit=math.inf) -> list[dict]:
        return self._run(user_ids, Operation.Followers, limit)

    # auth required
    def following(self, user_ids: list[int], limit=math.inf) -> list[dict]:
        return self._run(user_ids, Operation.Following, limit)

    # auth required
    def favoriters(self, tweet_ids: list[int], limit=math.inf) -> list[dict]:
        return self._run(tweet_ids, Operation.Favoriters, limit)

    # auth required
    def retweeters(self, tweet_ids: list[int], limit=math.inf) -> list[dict]:
        return self._run(tweet_ids, Operation.Retweeters, limit)

    def profile_spotlights(self, screen_names: list[str]) -> list:
        """
        This endpoint is included for completeness only. It returns very few data points.
        Use the batched query `users_by_ids` instead if you wish to pull user profile data.
        """
        return self._run(screen_names, Operation.ProfileSpotlightsQuery)

    def users_by_id(self, user_ids: list[int]) -> list[dict]:
        """
        This endpoint is included for completeness only.
        Use the batched query `users_by_ids` instead if you wish to pull user profile data.
        """
        return self._run(user_ids, Operation.UserByRestId)

    def tweet_stats(self, user_ids: list[int]) -> list[dict]:
        return self._run(user_ids, Operation.TweetStats)

    def recommended_users(self, user_id: int = None) -> dict:
        qid, op, key = Operation.ConnectTabTimeline
        context = {"contextualUserId": user_id} if user_id else {}
        params = {k: orjson.dumps(v).decode() for k, v in {
            'variables': Operation.default_variables | {key: orjson.dumps(context).decode()},
            'features': Operation.default_features,
        }.items()}
        r = self.session.get(f'{self.api}/{qid}/{op}', headers=get_headers(self.session), params=params)
        txt = r.text
        data = r.json()
        if self.debug:
            self.log(r, txt, data)
        if self.save:
            save_data(data, op, user_id)
        return data

    # special case, batch query
    def users_by_ids(self, user_ids: list[int]) -> dict:
        """
        Get user data in batches

        Batch-size limited to around 200-300 users
        """
        qid, op, key = Operation.UsersByRestIds
        params = {k: orjson.dumps(v).decode() for k, v in {
            'variables': Operation.default_variables | {key: user_ids},
            'features': Operation.default_features,
        }.items()}
        r = self.session.get(f'{self.api}/{qid}/{op}', headers=get_headers(self.session), params=params)
        txt = r.text
        data = r.json()
        if self.debug:
            self.log(r, txt, data)
        if self.save:
            save_data(data, op, user_ids[0])
        return data

    def _run(self, ids: list[int | str], operation: tuple, limit=None):
        return asyncio.run(self._process(ids, operation, limit))

    async def _process(self, ids: list[int | str], op: tuple, limit: int | None) -> list:
        async with AsyncClient(headers=get_headers(self.session)) as s:
            return await asyncio.gather(*(self._paginate(s, _id, op, limit) for _id in ids))

    async def _paginate(self, session: AsyncClient, _id: int | str | list[int], operation: tuple,
                        limit: int | None) -> list[dict]:

        r = await self._query(session, _id, operation)
        initial_data = r.json()
        res = [initial_data]
        ids = set(find_key(initial_data, 'rest_id'))
        dups = 0
        DUP_LIMIT = 3

        cursor = get_cursor(initial_data)
        while (dups < DUP_LIMIT) and cursor:
            prev_len = len(ids)
            if prev_len >= limit:
                return res

            r = await self._query(session, _id, operation, cursor=cursor)
            data = r.json()

            if len(find_key(data, 'entries')[0]) <= 2:
                # only top/bottom cursor in result
                return res

            cursor = get_cursor(data)
            ids |= set(find_key(data, 'rest_id'))

            if self.debug:
                logger.debug(f'cursor: {cursor}\tunique results: {len(ids)}')

            if prev_len == len(ids):
                dups += 1

            res.append(data)
        return res

    async def _query(self, session: AsyncClient, _id: int | str | list, operation: tuple, **kwargs) -> Response:
        qid, op, k = operation
        params = {k: orjson.dumps(v).decode() for k, v in {
            'variables': {k: _id} | Operation.default_variables | kwargs,
            'features': Operation.default_features,
        }.items()}
        r = await session.get(f'{self.api}/{qid}/{op}', params=params)
        txt = r.text
        data = r.json()
        if self.debug:
            self.log(r, txt, data)
        if self.save:
            save_data(data, op, _id[0] if isinstance(_id, list) else _id)
        return r

    def download_media(self, ids: list[int], photos: bool = True, videos: bool = True) -> None:
        tweets = self.tweets_by_id(ids)
        urls = []
        for tweet in tweets:
            tweet_id = find_key(tweet, 'id_str')[0]
            url = f'https://twitter.com/i/status/{tweet_id}'  # `i` evaluates to screen_name
            media = [y for x in find_key(tweet, 'media') for y in x]
            if photos:
                photo_urls = list({u for m in media if 'ext_tw_video_thumb' not in (u := m['media_url_https'])})
                [urls.append([url, photo]) for photo in photo_urls]
            if videos:
                video_urls = [x['variants'] for m in media if (x := m.get('video_info'))]
                hq_videos = {sorted(v, key=lambda d: d.get('bitrate', 0))[-1]['url'] for v in video_urls}
                [urls.append([url, video]) for video in hq_videos]

        with tqdm(total=len(urls), desc='downloading media') as pbar:
            with ThreadPoolExecutor(max_workers=32) as e:
                for future in as_completed(e.submit(self._download, x, y) for x, y in urls):
                    future.result()
                    pbar.update()

    def _download(self, post_url: str, cdn_url: str, path: str = 'media', chunk_size: int = 4096) -> None:
        Path(path).mkdir(parents=True, exist_ok=True)
        name = urlsplit(post_url).path.replace('/', '_')[1:]
        ext = urlsplit(cdn_url).path.split('/')[-1]
        try:
            with httpx.stream('GET', cdn_url) as r:
                with open(f'{path}/{name}_{ext}', 'wb') as f:
                    for chunk in r.iter_bytes(chunk_size=chunk_size):
                        f.write(chunk)
        except Exception as e:
            logger.debug(f'[{RED}error{RESET}] failed to download media: {post_url} {e}')

    def trends(self) -> dict:
        """Get trends for all UTC offsets"""

        def get_trends(offset: str, url: str, headers: dict):
            headers['x-twitter-utcoffset'] = offset
            r = self.session.get(url, headers=headers)
            trends = find_key(r.json(), 'item')
            return {t['content']['trend']['name']: t for t in trends}

        headers = get_headers(self.session)
        url = set_qs('https://twitter.com/i/api/2/guide.json', trending_params)
        offsets = [f"{str(i).zfill(3)}00" if i < 0 else f"+{str(i).zfill(2)}00" for i in range(-12, 15)]
        trends = {}
        with tqdm(total=len(offsets), desc='downloading trends') as pbar:
            with ThreadPoolExecutor(max_workers=32) as e:
                for future in as_completed(e.submit(get_trends, o, url, headers) for o in offsets):
                    trends |= future.result()
                    pbar.update()

        path = Path(f'data/raw/trends')
        path.mkdir(parents=True, exist_ok=True)
        (path / f'{time.time_ns()}.json').write_text(
            orjson.dumps(trends, option=orjson.OPT_INDENT_2).decode(),
            encoding='utf-8'
        )
        return trends

    def log(self, r: Response | Response, txt: str, data: dict):
        status = r.status_code

        def stat(r):
            if self.debug >= 1:
                logger.debug(f'{r.url}')
            if self.debug >= 2:
                logger.debug(f'{txt}')

            limits = {k: v for k, v in r.headers.items() if 'x-rate-limit' in k}
            current_time = int(time.time())
            wait = int(r.headers.get('x-rate-limit-reset', current_time)) - current_time
            logger.debug(
                f"remaining: {MAGENTA}{limits['x-rate-limit-remaining']}/{limits['x-rate-limit-limit']}{RESET} requests")
            logger.debug(f'reset:     {MAGENTA}{(wait / 60):.2f}{RESET} minutes')

        try:
            if 'json' in r.headers.get('content-type', ''):
                if data.get('errors'):
                    logger.debug(f'[{RED}error{RESET}] {status} {data}')
                else:
                    logger.debug(fmt_status(status))
                    stat(r)
            else:
                logger.debug(fmt_status(status))
                stat(r)
        except Exception as e:
            logger.debug(f'failed to log: {e}')
