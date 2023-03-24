import asyncio
import logging.config
import math
import platform
import random
import time
from copy import deepcopy
from pathlib import Path
from urllib.parse import urlsplit

import ujson
from aiohttp import ClientSession, TCPConnector

from .config.log import log_config
from .config.operations import operations
from .constants import *
from .login import login
from .utils import find_key, build_query, get_headers

try:
    if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
        import nest_asyncio
        nest_asyncio.apply()
except:
    ...

if platform.system() != 'Windows':
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
else:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

ID = 'ID'
DUP_LIMIT = 5
logging.config.dictConfig(log_config)
logger = logging.getLogger(__name__)


class Scraper:
    GRAPHQL_URL = 'https://api.twitter.com/graphql'

    def __init__(self, username: str, password: str):
        self.session = login(username, password)

    def tweets(self, ids: list[int], limit=math.inf):
        return self.run(ids, Operation.Data.UserTweets, limit)

    def tweets_and_replies(self, ids: list[int], limit=math.inf):
        return self.run(ids, Operation.Data.UserTweetsAndReplies, limit)

    def likes(self, ids: list[int], limit=math.inf):
        return self.run(ids, Operation.Data.Likes, limit)

    def media(self, ids: list[int], limit=math.inf):
        return self.run(ids, Operation.Data.UserMedia, limit)

    def followers(self, ids: list[int], limit=math.inf):
        return self.run(ids, Operation.Data.Followers, limit)

    def following(self, ids: list[int], limit=math.inf):
        return self.run(ids, Operation.Data.Following, limit)

    def favoriters(self, ids: list[int], limit=math.inf):
        return self.run(ids, Operation.Data.Favoriters, limit)

    def retweeters(self, ids: list[int], limit=math.inf):
        return self.run(ids, Operation.Data.Retweeters, limit)

    def tweets_details(self, ids: list[int], limit=math.inf):
        return self.run(ids, Operation.Data.TweetDetail, limit)

    # no pagination needed
    def tweet_by_rest_id(self, ids: list[int]):
        return self.run(ids, Operation.Data.TweetResultByRestId)

    # no pagination needed
    def user_by_screen_name(self, ids: list[str]):
        return self.run(ids, Operation.Data.UserByScreenName)

    # no pagination needed
    def user_by_rest_id(self, ids: list[int]):
        return self.run(ids, Operation.Data.UserByRestId)

    # no pagination needed (special batch query)
    def users_by_rest_ids(self, ids: list[int]):
        name, key = Operation.Data.UsersByRestIds
        params = deepcopy(operations[name])
        qid = params['queryId']
        params['variables']['userIds'] = ids
        q = build_query(params)
        url = f"{self.GRAPHQL_URL}/{qid}/{name}?{q}"
        headers = get_headers(self.session)
        headers['content-type'] = "application/json"
        users = self.session.get(url, headers=headers).json()
        return users

    def run(self, ids: list, operation: tuple, limit=None):
        res = self.query(ids, operation)
        if limit is None:
            return res
        return asyncio.run(self.pagination(res, operation, limit))

    def query(self, ids: list[any], operation: tuple) -> list:
        name, key = operation
        params = deepcopy(operations[name])
        qid = params['queryId']
        urls = []
        for _id in ids:
            params['variables'][key] = _id
            q = build_query(params)
            urls.append((_id, f"{self.GRAPHQL_URL}/{qid}/{name}?{q}"))
        headers = get_headers(self.session)
        headers['content-type'] = "application/json"
        res = asyncio.run(self.process(urls, headers))
        self.save_data(res, name)
        return res

    async def process(self, urls: list, headers: dict) -> tuple:
        conn = TCPConnector(limit=0, ssl=False, ttl_dns_cache=69)
        async with ClientSession(headers=headers, connector=conn) as s:
            # add cookies from logged-in session
            s.cookie_jar.update_cookies(self.session.cookies)
            return await asyncio.gather(*(self.get(s, u) for u in urls))

    async def get(self, session: ClientSession, url: tuple) -> dict:
        identifier, api_url = url
        logger.debug(f'processing: {url}')
        try:
            r = await session.get(api_url)
            limits = {k: v for k, v in r.headers.items() if 'x-rate-limit' in k}
            logger.debug(f'{limits = }')
            if r.status == 429:
                logger.debug(f'rate limit exceeded: {url}')
                return {}
            data = await r.json()
            return {ID: identifier, **data}
        except Exception as e:
            logger.debug(f'failed to download {url}: {e}')

    async def pagination(self, res: list, operation: tuple, limit: int) -> tuple:
        conn = TCPConnector(limit=len(res), ssl=False, ttl_dns_cache=69)
        headers = get_headers(self.session)
        headers['content-type'] = "application/json"
        async with ClientSession(headers=headers, connector=conn) as s:
            # add cookies from logged-in session
            s.cookie_jar.update_cookies(self.session.cookies)
            return await asyncio.gather(*(self.paginate(s, data, operation, limit) for data in res))

    async def paginate(self, session: ClientSession, data: dict, operation: tuple, limit: int):
        def get_cursor(data):
            # inefficient, but need to deal with arbitrary schema
            entries = find_key(data, 'entries')
            if entries:
                for entry in entries.pop():
                    if entry.get('entryId', '').startswith('cursor-bottom'):
                        content = entry['content']
                        if itemContent := content.get('itemContent'):
                            return itemContent['value']  # v2 cursor
                        return content['value']  # v1 cursor

        all_data = []
        try:
            name, key = operation
            params = deepcopy(operations[name])
            qid = params['queryId']

            ids = set()
            counts = []

            params['variables'][key] = data[ID]
            cursor = get_cursor(data)

            while 1:
                params['variables']['cursor'] = cursor
                query = build_query(params)
                url = f"{self.GRAPHQL_URL}/{qid}/{name}?{query}"

                # code [353]: "This request requires a matching csrf cookie and header."
                r, _data = await self.backoff(lambda: session.get(url))
                if csrf := r.cookies.get("ct0"):
                    session.headers.update({"x-csrf-token": csrf.value})
                session.cookie_jar.update_cookies(r.cookies)

                tagged_data = _data | {ID: data[ID]}
                self.save_data([tagged_data], name)
                all_data.append(tagged_data)
                cursor = get_cursor(_data)
                logger.debug(f'{cursor = }')
                ids |= set(find_key(tagged_data, 'rest_id'))
                logger.debug(f'({data[ID]})\t{len(ids)} unique results')
                counts.append(len(ids))

                success_message = f'[{SUCCESS}SUCCESS{RESET}] done pagination'
                # followers/following have "0|"
                if not cursor or cursor.startswith('0|'):
                    logger.debug(f'{success_message}\tlast cursor: {cursor}')
                    break
                if len(ids) >= limit:
                    logger.debug(f'{success_message}\tsurpassed limit of {limit} results')
                    break
                # did last 5 requests return duplicate data?
                if len(counts) > DUP_LIMIT and len(set(counts[-1:-DUP_LIMIT:-1])) == 1:
                    logger.debug(f'{success_message}\tpast {DUP_LIMIT} requests returned duplicate data')
                    break
        except Exception as e:
            logger.debug(f'paginate falied: {e}')
        # save_data(all_data, name)
        return all_data

    async def backoff(self, fn, retries=12):
        for i in range(retries + 1):
            try:
                r = await fn()
                data = await r.json()
                return r, data
            except Exception as e:
                if i == retries:
                    logger.debug(f'{WARN}Max retries exceeded{RESET}\n{e}')
                    return
                t = 2 ** i + random.random()
                logger.debug(f'retrying in {f"{t:.2f}"} seconds\t\t{e}')
                time.sleep(t)

    def save_data(self, data: list, name: str = ''):
        try:
            for d in data:
                path = Path(f'data/raw/{d[ID]}')
                path.mkdir(parents=True, exist_ok=True)
                with open(path / f'{time.time_ns()}_{name}.json', 'w') as fp:
                    ujson.dump(d, fp, indent=4)
        except KeyError as e:
            logger.debug(f'failed to save data: {e}')

    def download(self, post_url: str, cdn_url: str, path: str = 'media', chunk_size: int = 4096) -> None:
        """
        Download file
    
        @param post_url: the actual post url
        @param cdn_url: the cdn url
        @param path: path to save media
        @param chunk_size: chunk size in bytes
        @return: None
        """
        Path(path).mkdir(parents=True, exist_ok=True)
        name = urlsplit(post_url).path.replace('/', '_')[1:]
        ext = urlsplit(cdn_url).path.split('/')[-1]
        try:
            with open(f'{path}/{name}_{ext}', 'wb') as fp:
                r = self.session.get(cdn_url, stream=True)
                for chunk in r.iter_content(chunk_size=chunk_size):
                    fp.write(chunk)
        except Exception as e:
            logger.debug(f'FAILED to download video: {post_url} {e}')

    def download_media(self, ids: list[int], photos: bool = True, videos: bool = True) -> None:
        res = self.tweet_by_rest_id(ids)
        for r in res:
            user_id = find_key(r, 'user_results')[0]['result']['rest_id']
            url = f'https://twitter.com/{user_id}/status/{r[ID]}'  # evaluates to username in browser
            media = [y for x in find_key(r, 'media') for y in x]  # in case of arbitrary schema
            if photos:
                photos = list({u for m in media if 'ext_tw_video_thumb' not in (u := m['media_url_https'])})
                logger.debug(f'{photos = }')
                if photos:
                    [self.download(url, photo) for photo in photos]
            if videos:
                videos = [x['variants'] for m in media if (x := m.get('video_info'))]
                hq_videos = {sorted(v, key=lambda d: d.get('bitrate', 0))[-1]['url'] for v in videos}
                logger.debug(f'{videos = }')
                logger.debug(f'{hq_videos = }')
                if hq_videos:
                    [self.download(url, video) for video in hq_videos]
