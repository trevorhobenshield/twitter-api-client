import asyncio
import hashlib
import inspect
import logging.config
import mimetypes
import sys
import time
from copy import deepcopy
from enum import Enum, auto
from functools import wraps, partial
from pathlib import Path
from urllib.parse import urlencode
from uuid import uuid1, getnode

import ujson
from tqdm import tqdm

from .config.log_config import log_config
from .config.operations import operations
from .config.settings import *
from .login import Session, Response
from .utils import get_headers

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

logging.config.dictConfig(log_config)
logger = logging.getLogger(__name__)


class Operation(Enum):
    CreateTweet = auto()
    CreateScheduledTweet = auto()
    DeleteTweet = auto()
    UserTweets = auto()
    FavoriteTweet = auto()
    UnfavoriteTweet = auto()
    CreateRetweet = auto()
    DeleteRetweet = auto()
    CreateBookmark = auto()
    DeleteBookmark = auto()
    BookmarksAllDelete = auto()
    TweetStats = auto()
    # DM
    useSendMessageMutation = auto()


def log(fn=None, *, level: int = logging.DEBUG, info: list = None) -> callable:
    if fn is None:
        return partial(log, level=level, info=info)

    @wraps(fn)
    def wrapper(*args, **kwargs):
        args_info = " ".join(
            f'{k}={v}' for k, v in dict(zip(inspect.getfullargspec(fn)[0], args)).items()
            if '_id' in k or '_name' in k or 'Id' in k or 'Name' in k
        )
        r = fn(*args, **kwargs)

        limits = {k: v for k, v in r.headers.items() if 'x-rate-limit' in k}
        current_time = int(time.time())
        wait = int(r.headers.get('x-rate-limit-reset', current_time)) - current_time
        logger.log(level, f'{WARN}{wait // 60} minutes{RESET} until rate-limit reset. {limits = }')

        try:
            if 200 <= r.status_code < 300:
                message = f'[{SUCCESS}SUCCESS{RESET}] {r.status_code} ({BOLD}{fn.__name__}{RESET}) {args_info}'
                if info:
                    for k in info:
                        if callable(k):
                            logger.log(level, f'{message} {k(r)}')
                        else:
                            attr = getattr(r, k)
                            v = attr() if callable(attr) else attr
                            d = {f"{k}": v}
                            logger.log(level, f'{message} {d}')
                else:
                    logger.log(level, f'{message}')
            else:
                logger.log(level, f'[{WARN}ERROR{RESET}] ({fn.__name__}) {args_info} {r.status_code} {r.text}')
        except Exception as e:
            logger.log(level, f'[{WARN}FAILED{RESET}] ({fn.__name__}) {args_info} {r.status_code} {e}')
        return r

    return wrapper


def graphql_request(_id: int, operation: any, key: str | int, session: Session) -> Response:
    params = deepcopy(operations[operation])
    qid = params['queryId']
    if key: params['variables'][key] = _id
    url = f"https://api.twitter.com/graphql/{qid}/{operation}"
    r = session.post(url, headers=get_headers(session), json=params)
    return r


def api_request(settings: dict, path: str, session: Session) -> Response:
    headers = get_headers(session)
    headers['content-type'] = 'application/x-www-form-urlencoded'
    url = f'https://api.twitter.com/1.1/{path}'
    r = session.post(url, headers=headers, data=urlencode(settings))
    return r


def upload_media(filename: str, session: Session, is_dm: bool = False, is_profile=False) -> int:
    if is_profile:
        url = 'https://upload.twitter.com/i/media/upload.json'
    else:
        url = 'https://upload.twitter.com/1.1/media/upload.json'

    file = Path(filename)
    total_bytes = file.stat().st_size
    headers = get_headers(session)

    upload_type = 'dm' if is_dm else 'tweet'
    media_type = mimetypes.guess_type(file)[0]
    media_category = f'{upload_type}_{media_type.split("/")[0]}'

    if media_category in {'dm_image', 'tweet_image'} and total_bytes > MAX_IMAGE_SIZE:
        raise Exception(f'Image too large: max is {(MAX_IMAGE_SIZE / 1e6):.2f} MB')
    if media_category in {'dm_gif', 'tweet_gif'} and total_bytes > MAX_GIF_SIZE:
        raise Exception(f'GIF too large: max is {(MAX_GIF_SIZE / 1e6):.2f} MB')
    if media_category in {'dm_video', 'tweet_video'} and total_bytes > MAX_VIDEO_SIZE:
        raise Exception(f'Video too large: max is {(MAX_VIDEO_SIZE / 1e6):.2f} MB')

    data = {'command': 'INIT', 'media_type': media_type, 'total_bytes': total_bytes, 'media_category': media_category}
    r = session.post(url=url, headers=headers, data=data)
    media_id = r.json()['media_id']

    desc = f"uploading: {file.name}"
    with tqdm(total=total_bytes, desc=desc, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
        with open(file, 'rb') as f:
            i = 0
            while chunk := f.read(4 * 1024 * 1024):  # todo: arbitrary max size for now
                data = {'command': 'APPEND', 'media_id': media_id, 'segment_index': i}
                files = {'media': chunk}
                r = session.post(url=url, headers=headers, data=data, files=files)
                if r.status_code < 200 or r.status_code > 299:
                    logger.debug(f'{r.status_code} {r.text}')
                    raise Exception('Upload failed')
                i += 1
                pbar.update(f.tell() - pbar.n)

    data = {'command': 'FINALIZE', 'media_id': media_id, 'allow_async': 'true'}
    if is_dm:
        data |= {'original_md5': hashlib.md5(file.read_bytes()).hexdigest()}
    r = session.post(url=url, headers=headers, data=data)

    logger.debug(f'processing, please wait...')
    processing_info = r.json().get('processing_info')
    while processing_info:
        state = processing_info['state']
        if state == 'succeeded':
            break
        if state == 'failed':
            raise Exception('Media processing failed')
        check_after_secs = processing_info['check_after_secs']
        # logger.debug(f'{check_after_secs = }')
        time.sleep(check_after_secs)
        params = {'command': 'STATUS', 'media_id': media_id}
        r = session.get(url=url, headers=headers, params=params)
        processing_info = r.json().get('processing_info')
    logger.debug('processing complete')

    return media_id


@log(info=['text'])
def add_alt_text(text: str, media_id: int, session: Session) -> Response:
    params = {"media_id": media_id, "alt_text": {"text": text}}
    url = 'https://api.twitter.com/1.1/media/metadata/create.json'
    r = session.post(url, headers=get_headers(session), json=params)
    return r


@log(info=['json'])
def tweet(text: str, session: Session, media: list[dict | str] = None, **kwargs) -> Response:
    operation = Operation.CreateTweet.name
    params = deepcopy(operations[operation])
    qid = params['queryId']
    params['variables']['tweet_text'] = text
    if media:
        for m in media:
            if isinstance(m, dict):
                media_id = upload_media(m['file'], session)
                params['variables']['media']['media_entities'].append({
                    'media_id': media_id,
                    'tagged_users': m.get('tagged_users', [])
                })
                if alt := m.get('alt'):
                    add_alt_text(alt, media_id, session)
            # for convenience, so we can just pass list of strings
            elif isinstance(m, str):
                media_id = upload_media(m, session)
                params['variables']['media']['media_entities'].append({
                    'media_id': media_id,
                    'tagged_users': []
                })

    if reply_params := kwargs.get('reply_params', {}):
        params['variables'] |= reply_params
    if quote_params := kwargs.get('quote_params', {}):
        params['variables'] |= quote_params
    if poll_params := kwargs.get('poll_params', {}):
        params['variables'] |= poll_params

    url = f"https://api.twitter.com/graphql/{qid}/{operation}"
    r = session.post(url, headers=get_headers(session), json=params)
    return r


def comment(text: str, tweet_id: int, session: Session, media: list[dict | str] = None) -> Response:
    params = {"reply": {"in_reply_to_tweet_id": tweet_id, "exclude_reply_user_ids": []}}
    return tweet(text, session, media, reply_params=params)


def quote(text: str, screen_name: str, tweet_id: int, session: Session, media: list[dict | str] = None) -> Response:
    """ no unquote operation, just DeleteTweet"""
    params = {"attachment_url": f"https://twitter.com/{screen_name}/status/{tweet_id}"}
    return tweet(text, session, media, quote_params=params)


@log(info=['json'])
def untweet(tweet_id: int, session: Session) -> Response:
    return graphql_request(tweet_id, Operation.DeleteTweet.name, 'tweet_id', session)


@log(info=['json'])
def retweet(tweet_id: int, session: Session) -> Response:
    return graphql_request(tweet_id, Operation.CreateRetweet.name, 'tweet_id', session)


@log(info=['json'])
def unretweet(tweet_id: int, session: Session) -> Response:
    return graphql_request(tweet_id, Operation.DeleteRetweet.name, 'source_tweet_id', session)


@log(info=['json'])
def like(tweet_id: int, session: Session) -> Response:
    return graphql_request(tweet_id, Operation.FavoriteTweet.name, 'tweet_id', session)


@log(info=['json'])
def unlike(tweet_id: int, session: Session) -> Response:
    return graphql_request(tweet_id, Operation.UnfavoriteTweet.name, 'tweet_id', session)


@log(info=['json'])
def follow(user_id: int, session: Session) -> Response:
    settings = follow_settings.copy()
    settings |= {"user_id": user_id}
    return api_request(settings, 'friendships/create.json', session)


@log(info=['json'])
def unfollow(user_id: int, session: Session) -> Response:
    settings = follow_settings.copy()
    settings |= {"user_id": user_id}
    return api_request(settings, 'friendships/destroy.json', session)


@log(info=['json'])
def mute(user_id: int, session: Session) -> Response:
    settings = {'user_id': user_id}
    return api_request(settings, 'mutes/users/create.json', session)


@log(info=['json'])
def unmute(user_id: int, session: Session) -> Response:
    settings = {'user_id': user_id}
    return api_request(settings, 'mutes/users/destroy.json', session)


@log(info=['json'])
def enable_notifications(user_id: int, session: Session) -> Response:
    settings = notification_settings.copy()
    settings |= {'id': user_id, 'device': 'true'}
    return api_request(settings, 'friendships/update.json', session)


@log(info=['json'])
def disable_notifications(user_id: int, session: Session) -> Response:
    settings = notification_settings.copy()
    settings |= {'id': user_id, 'device': 'false'}
    return api_request(settings, 'friendships/update.json', session)


@log(info=['json'])
def block(user_id: int, session: Session) -> Response:
    settings = {'user_id': user_id}
    return api_request(settings, 'blocks/create.json', session)


@log(info=['json'])
def unblock(user_id: int, session: Session) -> Response:
    settings = {'user_id': user_id}
    return api_request(settings, 'blocks/destroy.json', session)


@log(info=['json'])
def bookmark(_id: int, session: Session) -> Response:
    return graphql_request(_id, Operation.CreateBookmark.name, 'tweet_id', session)


@log(info=['json'])
def unbookmark(_id: int, session: Session) -> Response:
    return graphql_request(_id, Operation.DeleteBookmark.name, 'tweet_id', session)


# @log(info=['json'])
# def unbookmark_all(session: Session) -> Response:
#     return graphql_request(0, Operation.BookmarksAllDelete.name, 0, session)


@log(info=['text'])
def update_search_settings(session: Session, **kwargs) -> Response:
    twid = int(session.cookies.get_dict()['twid'].split('=')[-1].strip('"'))
    headers = get_headers(session=session)
    r = session.post(
        url=f'https://api.twitter.com/1.1/strato/column/User/{twid}/search/searchSafety',
        headers=headers,
        json=kwargs,
    )
    return r


@log(info=['json'])
def update_content_settings(session: Session, **kwargs) -> Response:
    """
    Update content settings

    @param session: authenticated session
    @param kwargs: settings to enable/disable
    @return: updated settings
    """
    return api_request(kwargs, 'account/settings.json', session)


def build_query(params: dict) -> str:
    return '&'.join(f'{k}={ujson.dumps(v)}' for k, v in params.items())


@log(info=['json'])
def stats(rest_id: int, session: Session) -> Response:
    """private endpoint?"""
    operation = Operation.TweetStats.name
    params = deepcopy(operations[operation])
    qid = params['queryId']
    params['variables']['rest_id'] = rest_id
    query = build_query(params)
    url = f"https://api.twitter.com/graphql/{qid}/{operation}?{query}"
    r = session.get(url, headers=get_headers(session))
    return r


@log(info=['json'])
def dm(text: str, receivers: list[int], session: Session, filename: str = '') -> Response:
    operation = Operation.useSendMessageMutation.name
    params = deepcopy(operations[operation])
    qid = params['queryId']
    params['variables']['target'] = {"participant_ids": receivers}
    params['variables']['requestId'] = str(uuid1(getnode()))  # can be anything
    url = f"https://api.twitter.com/graphql/{qid}/{operation}"
    if filename:
        media_id = upload_media(filename, session, is_dm=True)
        params['variables']['message']['media'] = {'id': media_id, 'text': text}
    else:
        params['variables']['message']['text'] = {'text': text}
    r = session.post(url, headers=get_headers(session), json=params)
    return r


@log(info=['json'])
def update_profile_image(filename: str, session: Session) -> Response:
    media_id = upload_media(filename, session, is_profile=True)
    url = 'https://api.twitter.com/1.1/account/update_profile_image.json'
    headers = get_headers(session)
    params = {'media_id': media_id}
    r = session.post(url, headers=headers, params=params)
    return r


@log
def update_profile_banner(filename: str, session: Session) -> Response:
    media_id = upload_media(filename, session, is_profile=True)
    url = 'https://api.twitter.com/1.1/account/update_profile_banner.json'
    headers = get_headers(session)
    params = {'media_id': media_id}
    r = session.post(url, headers=headers, params=params)
    return r


@log
def update_profile_info(session: Session, **kwargs) -> Response:
    url = 'https://api.twitter.com/1.1/account/update_profile.json'
    headers = get_headers(session)
    r = session.post(url, headers=headers, params=kwargs)
    return r


@log(info=['json'])
def create_poll(text: str, choices: list[str], poll_duration: int, session: Session) -> Response:
    options = {
        "twitter:card": "poll4choice_text_only",
        "twitter:api:api:endpoint": "1",
        "twitter:long:duration_minutes": poll_duration  # max: 10080
    }
    for i, c in enumerate(choices):
        options[f"twitter:string:choice{i + 1}_label"] = c

    headers = get_headers(session)
    headers['content-type'] = 'application/x-www-form-urlencoded'
    url = 'https://caps.twitter.com/v2/cards/create.json'
    r = session.post(url, headers=headers, params={'card_data': ujson.dumps(options)})
    card_uri = r.json()['card_uri']
    r = tweet(text, session, poll_params={'card_uri': card_uri})
    return r


@log(info=['json'])
def pin(tweet_id: int, session: Session) -> Response:
    settings = {'tweet_mode': 'extended', 'id': tweet_id}
    return api_request(settings, 'account/pin_tweet.json', session)


@log(info=['json'])
def unpin(tweet_id: int, session: Session) -> Response:
    settings = {'tweet_mode': 'extended', 'id': tweet_id}
    return api_request(settings, 'account/unpin_tweet.json', session)
