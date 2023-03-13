import asyncio
import logging.config
import math
import random
import re
import sys
import time
from enum import Enum, auto
from pathlib import Path
from urllib.parse import urlsplit

import ujson
from aiohttp import ClientSession, TCPConnector

from .config.operations import operations
from .config.log_config import log_config
from .login import Session
from .utils import find_key

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
logging.config.dictConfig(log_config)
logger = logging.getLogger(__name__)


def get_user_tweets(ids: list[int], session: Session, limit=math.inf):
    return run(Operation.UserTweets.name, 'userId', ids, session, limit)


def get_tweets_and_replies(ids: list[int], session: Session, limit=math.inf):
    return run(Operation.UserTweetsAndReplies.name, 'userId', ids, session, limit)


def get_likes(ids: list[int], session: Session, limit=math.inf):
    return run(Operation.Likes.name, 'userId', ids, session, limit)


def get_media(ids: list[int], session: Session, limit=math.inf):
    return run(Operation.UserMedia.name, 'userId', ids, session, limit)


def get_followers(ids: list[int], session: Session, limit=math.inf):
    return run(Operation.Followers.name, 'userId', ids, session, limit)


def get_following(ids: list[int], session: Session, limit=math.inf):
    return run(Operation.Following.name, 'userId', ids, session, limit)


def get_favoriters(ids: list[int], session: Session, limit=math.inf):
    return run(Operation.Favoriters.name, 'tweetId', ids, session, limit)


def get_retweeters(ids: list[int], session: Session, limit=math.inf):
    return run(Operation.Retweeters.name, 'tweetId', ids, session, limit)


def get_tweets(ids: list[int], session: Session, limit=math.inf):
    return run(Operation.TweetDetail.name, 'focalTweetId', ids, session, limit)


# no pagination needed
def get_tweet_by_rest_id(ids: list[int], session: Session):
    return graphql(ids, Operation.TweetResultByRestId.name, 'tweetId', session)


# no pagination needed
def get_user_by_screen_name(ids: list[str], session: Session):
    return graphql(ids, Operation.UserByScreenName.name, 'screen_name', session)


# no pagination needed
def get_user_by_rest_id(ids: list[int], session: Session):
    return graphql(ids, Operation.UserByRestId.name, 'userId', session)


# no pagination needed - special batch query
def get_users_by_rest_ids(ids: list[int], session: Session):
    operation = Operation.UsersByRestIds.name
    qid = operations[operation]['queryId']
    operations[operation]['variables']['userIds'] = ids
    query = build_query(operations[operation])
    url = f"https://api.twitter.com/graphql/{qid}/{operation}?{query}"
    headers = get_headers(session=session)
    users = session.get(url, headers=headers).json()
    return users


def run(operation: str, key: str, ids: list[str | int], session: Session, limit):
    res = graphql(ids, operation, key, session)
    return asyncio.run(pagination(operation, key, res, session, limit))


def graphql(ids: list[any], operation: any, key: str | int, session: Session) -> list:
    qid = operations[operation]['queryId']
    params = operations[operation]
    urls = []
    for _id in ids:
        params['variables'][key] = _id
        query = build_query(params)
        urls.append((_id, f"https://api.twitter.com/graphql/{qid}/{operation}?{query}"))
    res = asyncio.run(process(urls, get_headers(session=session), session))
    save_data(res, operation)
    return res


async def process(urls: list, headers: dict, session: Session) -> tuple:
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


async def pagination(operation: any, key: str, res: list, session: Session, limit) -> tuple:
    conn = TCPConnector(limit=len(res), ssl=False, ttl_dns_cache=69)
    async with ClientSession(headers=get_headers(session=session), connector=conn) as s:
        # add cookies from logged-in session
        s.cookie_jar.update_cookies(session.cookies)
        return await asyncio.gather(*(paginate(s, operation, key, data, limit) for data in res))


async def paginate(session: ClientSession, operation: any, key: str, data: dict, limit: int):
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

    DUP_LIMIT = 5
    qid = operations[operation]['queryId']
    params = operations[operation]

    ids = set()
    counts = []
    all_data = []

    params['variables'][key] = data[ID]
    cursor = get_cursor(data)

    while 1:
        params['variables']['cursor'] = cursor
        query = build_query(params)
        url = f"https://api.twitter.com/graphql/{qid}/{operation}?{query}"

        # update csrf header - must be an easier way
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


def build_query(params):
    return '&'.join(f'{k}={ujson.dumps(v)}' for k, v in {k: v for k, v in params.items() if k != 'queryId'}.items())


def save_data(data: list, operation: str = ''):
    for d in data:
        path = Path(f'data/raw/{d[ID]}')
        path.mkdir(parents=True, exist_ok=True)
        with open(path / f'{time.time_ns()}_{operation}.json', 'w') as fp:
            ujson.dump(d, fp, indent=4)


def get_headers(session=False, fname: str = '') -> dict:
    if fname:
        with open(fname) as fp:
            return {y.group(): z.group()
                    for x in fp.read().splitlines()
                    if (y := re.search('^[\w-]+(?=:\s)', x),
                        z := re.search(f'(?<={y.group()}:\s).*', x))}
    if session:
        return {
            "authorization": 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            "content-type": "application/json",
            "user-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
            "x-guest-token": session.tokens['guest_token'],
            "x-csrf-token": session.cookies.get("ct0"),
            "x-twitter-auth-type": "OAuth2Session" if session.cookies.get("auth_token") else '',
            "x-twitter-active-user": "yes",
            "x-twitter-client-language": 'en',
        }

    s = Session()
    headers = {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    r = s.post('https://api.twitter.com/1.1/guest/activate.json', headers=headers)
    headers['x-guest-token'] = r.json()['guest_token']
    return headers


def download(session: Session, post_url: str, cdn_url: str, path: str = 'media', chunk_size: int = 4096) -> None:
    """
    Download media

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


def download_media(ids: list[int], session: Session, photos: bool = True, videos: bool = True) -> None:
    res = get_tweet_by_rest_id(ids, session=session)
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
