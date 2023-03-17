import asyncio
import logging.config
import math
import random
import re
import sys
import time
from copy import deepcopy
from enum import Enum, auto
from pathlib import Path
from urllib.parse import urlsplit

import ujson
from aiohttp import ClientSession, TCPConnector

from .config.operations import operations
from .config.log_config import log_config
from .login import Session
from .utils import find_key, build_query, get_headers

try:
    if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
        import nest_asyncio

        nest_asyncio.apply()
except:
    ...

if sys.platform != 'win32':
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
else:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class Operation(Enum):
    # tweet operations
    TweetDetail = auto()
    TweetResultByRestId = auto()
    Favoriters = auto()
    Retweeters = auto()

    # user operations
    Following = auto()
    UserTweets = auto()
    Followers = auto()
    UserTweetsAndReplies = auto()
    UserMedia = auto()
    Likes = auto()
    UserByScreenName = auto()
    UserByRestId = auto()

    # batch user operations
    UsersByRestIds = auto()


ID = 'ID'
DUP_LIMIT = 5
logging.config.dictConfig(log_config)
logger = logging.getLogger(__name__)


def get_user_tweets(session: Session, ids: list[int], limit=math.inf):
    return run(session, ids, Operation.UserTweets.name, 'userId', limit)


def get_tweets_and_replies(session: Session, ids: list[int], limit=math.inf):
    return run(session, ids, Operation.UserTweetsAndReplies.name, 'userId', limit)


def get_likes(session: Session, ids: list[int], limit=math.inf):
    return run(session, ids, Operation.Likes.name, 'userId', limit)


def get_media(session: Session, ids: list[int], limit=math.inf):
    return run(session, ids, Operation.UserMedia.name, 'userId', limit)


def get_followers(session: Session, ids: list[int], limit=math.inf):
    return run(session, ids, Operation.Followers.name, 'userId', limit)


def get_following(session: Session, ids: list[int], limit=math.inf):
    return run(session, ids, Operation.Following.name, 'userId', limit)


def get_favoriters(session: Session, ids: list[int], limit=math.inf):
    return run(session, ids, Operation.Favoriters.name, 'tweetId', limit)


def get_retweeters(session: Session, ids: list[int], limit=math.inf):
    return run(session, ids, Operation.Retweeters.name, 'tweetId', limit)


def get_tweets(session: Session, ids: list[int], limit=math.inf):
    return run(session, ids, Operation.TweetDetail.name, 'focalTweetId', limit)


# no pagination needed
def get_tweet_by_rest_id(session: Session, ids: list[int]):
    return run(session, ids, Operation.TweetResultByRestId.name, 'tweetId')


# no pagination needed
def get_user_by_screen_name(session: Session, ids: list[str]):
    return run(session, ids, Operation.UserByScreenName.name, 'screen_name')


# no pagination needed
def get_user_by_rest_id(session: Session, ids: list[int]):
    return run(session, ids, Operation.UserByRestId.name, 'userId')


# no pagination needed (special batch query)
def users_by_rest_ids(session: Session, ids: list[int]):
    operation = Operation.UsersByRestIds.name
    qid = operations[operation]['queryId']
    params = deepcopy(operations[operation])
    params['variables']['userIds'] = ids
    query = build_query(params)
    url = f"https://api.twitter.com/graphql/{qid}/{operation}?{query}"
    headers = get_headers(session)
    headers['content-type'] = "application/json"
    users = session.get(url, headers=headers).json()
    return users


def run(session: Session, ids: list[str | int], operation: str, key: str, limit=None):
    res = graphql(session, ids, operation, key)
    if limit is None:
        return res
    return asyncio.run(pagination(session, res, operation, key, limit))


def graphql(session: Session, ids: list[any], operation: any, key: str | int) -> list:
    qid = operations[operation]['queryId']
    params = deepcopy(operations[operation])
    urls = []
    for _id in ids:
        params['variables'][key] = _id
        query = build_query(params)
        urls.append((_id, f"https://api.twitter.com/graphql/{qid}/{operation}?{query}"))
    headers = get_headers(session)
    headers['content-type'] = "application/json"
    res = asyncio.run(process(session, urls, headers))
    save_data(res, operation)
    return res


async def process(session: Session, urls: list, headers: dict) -> tuple:
    conn = TCPConnector(limit=0, ssl=False, ttl_dns_cache=69)
    async with ClientSession(headers=headers, connector=conn) as s:
        # add cookies from logged-in session
        s.cookie_jar.update_cookies(session.cookies)
        return await asyncio.gather(*(get(s, u) for u in urls))


async def get(session: ClientSession, url: tuple) -> dict:
    identifier, api_url = url
    logger.debug(f'processing: {url}')
    try:
        r = await session.get(api_url)
        data = await r.json()
        return {ID: identifier, **data}
    except Exception as e:
        logger.debug(e)


async def pagination(session: Session, res: list, operation: any, key: str, limit) -> tuple:
    conn = TCPConnector(limit=len(res), ssl=False, ttl_dns_cache=69)
    headers = get_headers(session)
    headers['content-type'] = "application/json"
    async with ClientSession(headers=headers, connector=conn) as s:
        # add cookies from logged-in session
        s.cookie_jar.update_cookies(session.cookies)
        return await asyncio.gather(*(paginate(s, data, operation, key, limit) for data in res))


async def paginate(session: ClientSession, data: dict, operation: any, key: str, limit: int):
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

    qid = operations[operation]['queryId']
    params = deepcopy(operations[operation])

    ids = set()
    counts = []
    all_data = []

    params['variables'][key] = data[ID]
    cursor = get_cursor(data)

    while 1:
        params['variables']['cursor'] = cursor
        query = build_query(params)
        url = f"https://api.twitter.com/graphql/{qid}/{operation}?{query}"

        # update csrf header - must be an easier way without importing yarl
        if k := session.cookie_jar.__dict__['_cookies'].get('twitter.com'):
            if cookie := re.search('(?<=ct0\=)\w+(?=;)', str(k)):
                session.headers.update({"x-csrf-token": cookie.group()})

        _data = await backoff(lambda: session.get(url))
        tagged_data = _data | {ID: data[ID]}
        save_data([tagged_data], operation)
        all_data.append(tagged_data)
        cursor = get_cursor(_data)
        logger.debug(f'{cursor = }')
        ids |= set(find_key(tagged_data, 'rest_id'))
        logger.debug(f'({data[ID]})\t{len(ids)} unique results')
        counts.append(len(ids))

        # followers/following have "0|"
        if not cursor or cursor.startswith('0|'):
            logger.debug(f'[SUCCESS] done pagination\tlast cursor: {cursor}')
            break
        if len(ids) >= limit:
            logger.debug(f'[SUCCESS] done pagination\tsurpassed limit of {limit} results')
            break
        # did last 5 requests return duplicate data?
        if len(counts) > DUP_LIMIT and len(set(counts[-1:-DUP_LIMIT:-1])) == 1:
            logger.debug(f'[SUCCESS] done pagination\tpast {DUP_LIMIT} requests returned duplicate data')
            break

    save_data(all_data, operation)
    return all_data


async def backoff(fn, retries=12):
    for i in range(retries + 1):
        try:
            r = await fn()
            data = await r.json()
            return data
        except Exception as e:
            if i == retries:
                logger.debug(f'Max retries exceeded\n{e}')
                return
            t = 2 ** i + random.random()
            logger.debug(f'retrying in {f"{t:.2f}"} seconds\t\t{e}')
            time.sleep(t)


def save_data(data: list, operation: str = ''):
    for d in data:
        path = Path(f'data/raw/{d[ID]}')
        path.mkdir(parents=True, exist_ok=True)
        with open(path / f'{time.time_ns()}_{operation}.json', 'w') as fp:
            ujson.dump(d, fp, indent=4)


def download(session: Session, post_url: str, cdn_url: str, path: str = 'media', chunk_size: int = 4096) -> None:
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
            r = session.get(cdn_url, stream=True)
            for chunk in r.iter_content(chunk_size=chunk_size):
                fp.write(chunk)
    except Exception as e:
        logger.debug(f'FAILED to download video: {post_url} {e}')


def download_media(session: Session, ids: list[int], photos: bool = True, videos: bool = True) -> None:
    res = get_tweet_by_rest_id(session, ids)
    for r in res:
        user_id = find_key(r, 'user_results')[0]['result']['rest_id']
        url = f'https://twitter.com/{user_id}/status/{r[ID]}'  # evaluates to username in browser
        media = [y for x in find_key(r, 'media') for y in x]  # in case of arbitrary schema
        if photos:
            photos = list({u for m in media if 'ext_tw_video_thumb' not in (u := m['media_url_https'])})
            logger.debug(f'{photos = }')
            if photos:
                [download(session, url, photo) for photo in photos]
        if videos:
            videos = [x['variants'] for m in media if (x := m.get('video_info'))]
            hq_videos = {sorted(v, key=lambda d: d.get('bitrate', 0))[-1]['url'] for v in videos}
            logger.debug(f'{videos = }')
            logger.debug(f'{hq_videos = }')
            if hq_videos:
                [download(session, url, video) for video in hq_videos]
