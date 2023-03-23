import asyncio
import hashlib
import inspect
import logging.config
import mimetypes
import platform
import random
import time
from copy import deepcopy
from datetime import datetime
from functools import wraps, partial
from pathlib import Path
from urllib.parse import urlencode
from uuid import uuid1, getnode

import ujson
from requests import Response
from tqdm import tqdm

from .config.log import log_config
from .config.operations import operations
from .config.settings import *
from .constants import *
from .login import login
from .utils import get_headers, build_query

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

logging.config.dictConfig(log_config)
logger = logging.getLogger(__name__)


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
        logger.log(level, f'{wait // 60} minutes until rate-limit reset. {limits = }')

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


class Account:
    V1_URL = 'https://api.twitter.com/1.1'
    V2_URL = 'https://api.twitter.com/2'  # /search
    GRAPHQL_URL = 'https://api.twitter.com/graphql'

    def __init__(self, username: str, password: str):
        self.session = login(username, password)

    def gql(self, operation: tuple, variables: dict) -> Response:
        name, _ = operation
        payload = deepcopy(operations[name])
        qid = payload['queryId']
        payload['variables'] |= variables
        url = f"{self.GRAPHQL_URL}/{qid}/{name}"
        r = self.session.post(url, headers=get_headers(self.session), json=payload)
        return r

    def api(self, path: str, settings: dict) -> Response:
        headers = get_headers(self.session)
        headers['content-type'] = 'application/x-www-form-urlencoded'
        url = f'{self.V1_URL}/{path}'
        r = self.session.post(url, headers=headers, data=urlencode(settings))
        return r

    @log(info=['json'])
    def dm(self, receivers: list[int], text: str, filename: str = '') -> Response:
        name, _ = Operation.Account.useSendMessageMutation
        params = deepcopy(operations[name])
        qid = params['queryId']
        params['variables']['target'] = {"participant_ids": receivers}
        params['variables']['requestId'] = str(uuid1(getnode()))  # can be anything
        url = f"{self.GRAPHQL_URL}/{qid}/{name}"
        if filename:
            media_id = self.upload_media(filename, is_dm=True)
            params['variables']['message']['media'] = {'id': media_id, 'text': text}
        else:
            params['variables']['message']['text'] = {'text': text}
        r = self.session.post(url, headers=get_headers(self.session), json=params)
        return r

    @log(info=['json'])
    def tweet(self, text: str, media: list = None, **kwargs) -> Response:
        name, _ = Operation.Account.CreateTweet
        params = deepcopy(operations[name])
        qid = params['queryId']
        params['variables']['tweet_text'] = text
        if media:
            for m in media:
                if isinstance(m, dict):
                    media_id = self.upload_media(m['file'])
                    params['variables']['media']['media_entities'].append({
                        'media_id': media_id,
                        'tagged_users': m.get('tagged_users', [])
                    })
                    if alt := m.get('alt'):
                        self.add_alt_text(media_id, alt)
                # for convenience, so we can just pass list of strings
                elif isinstance(m, str):
                    media_id = self.upload_media(m)
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

        url = f"{self.GRAPHQL_URL}/{qid}/{name}"
        r = self.session.post(url, headers=get_headers(self.session), json=params)
        return r

    @log(info=['json'])
    def schedule_tweet(self, text: str, execute_at: any, *, reply_to: int = None,
                       media: list = None) -> Response:
        name, _ = Operation.Account.CreateScheduledTweet
        params = deepcopy(operations[name])
        qid = params['queryId']
        params['variables']['post_tweet_request']['status'] = text
        params['variables']['execute_at'] = (
            datetime.strptime(execute_at, "%Y-%m-%d %H:%M").timestamp()
            if isinstance(execute_at, str)
            else execute_at
        )
        if reply_to:
            params['variables']['post_tweet_request']['in_reply_to_status_id'] = reply_to
        if media:
            for m in media:
                if isinstance(m, dict):
                    media_id = self.upload_media(m['file'])
                    params['variables']['post_tweet_request']['media_ids'].append(media_id)
                    if alt := m.get('alt'):
                        self.add_alt_text(self.session, media_id, alt)
                # for convenience, so we can just pass list of strings
                elif isinstance(m, str):
                    media_id = self.upload_media(m)
                    params['variables']['post_tweet_request']['media_ids'].append(media_id)
        url = f"{self.GRAPHQL_URL}/{qid}/{name}"
        r = self.session.post(url, headers=get_headers(self.session), json=params)
        return r

    @log(info=['json'])
    def create_poll(self, text: str, choices: list[str], poll_duration: int) -> Response:
        options = {
            "twitter:card": "poll4choice_text_only",
            "twitter:api:api:endpoint": "1",
            "twitter:long:duration_minutes": poll_duration  # max: 10080
        }
        for i, c in enumerate(choices):
            options[f"twitter:string:choice{i + 1}_label"] = c

        headers = get_headers(self.session)
        headers['content-type'] = 'application/x-www-form-urlencoded'
        url = 'https://caps.twitter.com/v2/cards/create.json'
        r = self.session.post(url, headers=headers, params={'card_data': ujson.dumps(options)})
        card_uri = r.json()['card_uri']
        r = self.tweet(text, poll_params={'card_uri': card_uri})
        return r

    def check_media(self, category: str, total_bytes: int) -> None:
        def check(media):
            name, size = media
            fmt = lambda x: f'{(x / 1e6):.2f} MB'
            if name in category and total_bytes > size:
                raise Exception(f'cannot upload {fmt(total_bytes)} {name}: max {name} size is {fmt(size)}')

        tuple(map(check, (Media.Type.image, Media.Type.gif, Media.Type.video)))

    def upload_media(self, filename: str, is_dm: bool = False, is_profile=False) -> int:
        if is_profile:
            url = 'https://upload.twitter.com/i/media/upload.json'
        else:
            url = 'https://upload.twitter.com/1.1/media/upload.json'

        file = Path(filename)
        total_bytes = file.stat().st_size
        headers = get_headers(self.session)

        upload_type = 'dm' if is_dm else 'tweet'
        media_type = mimetypes.guess_type(file)[0]
        media_category = f'{upload_type}_{media_type.split("/")[0]}'

        self.check_media(media_category, total_bytes)

        data = {'command': 'INIT', 'media_type': media_type, 'total_bytes': total_bytes,
                'media_category': media_category}
        r = self.session.post(url=url, headers=headers, data=data)
        media_id = r.json()['media_id']

        desc = f"uploading: {file.name}"
        with tqdm(total=total_bytes, desc=desc, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
            with open(file, 'rb') as f:
                i = 0
                while chunk := f.read(UPLOAD_CHUNK_SIZE):  # todo: arbitrary max size for now
                    data = {'command': 'APPEND', 'media_id': media_id, 'segment_index': i}
                    files = {'media': chunk}
                    r = self.session.post(url=url, headers=headers, data=data, files=files)
                    if r.status_code < 200 or r.status_code > 299:
                        logger.debug(f'{r.status_code} {r.text}')
                        raise Exception('Upload failed')
                    i += 1
                    pbar.update(f.tell() - pbar.n)

        data = {'command': 'FINALIZE', 'media_id': media_id, 'allow_async': 'true'}
        if is_dm:
            data |= {'original_md5': hashlib.md5(file.read_bytes()).hexdigest()}
        r = self.session.post(url=url, headers=headers, data=data)

        logger.debug(f'processing, please wait...')
        processing_info = r.json().get('processing_info')
        while processing_info:
            state = processing_info['state']
            logger.debug(f'{processing_info = }')
            if state == MEDIA_UPLOAD_SUCCEED:
                break
            if state == MEDIA_UPLOAD_FAIL:
                raise Exception('Media processing failed')
            check_after_secs = processing_info.get('check_after_secs', random.randint(1, 5))
            time.sleep(check_after_secs)
            params = {'command': 'STATUS', 'media_id': media_id}
            r = self.session.get(url=url, headers=headers, params=params)
            processing_info = r.json().get('processing_info')
        logger.debug('processing complete')

        return media_id

    @log(info=['text'])
    def add_alt_text(self, media_id: int, text: str) -> Response:
        params = {"media_id": media_id, "alt_text": {"text": text}}
        url = f'{self.V1_URL}/media/metadata/create.json'
        r = self.session.post(url, headers=get_headers(self.session), json=params)
        return r

    def reply(self, tweet_id: int, text: str, media: list = None) -> Response:
        """ an un-reply operation is just DeleteTweet"""
        params = {"reply": {"in_reply_to_tweet_id": tweet_id, "exclude_reply_user_ids": []}}
        return self.tweet(text, media, reply_params=params)

    def quote(self, tweet_id: int, screen_name: str, text: str, media: list = None) -> Response:
        """ an un-quote operation is just DeleteTweet"""
        params = {"attachment_url": f"https://twitter.com/{screen_name}/status/{tweet_id}"}
        return self.tweet(text, media, quote_params=params)

    @log(info=['json'])
    def unschedule_tweet(self, tweet_id: int) -> Response:
        return self.gql(Operation.Account.DeleteScheduledTweet, {'scheduled_tweet_id': tweet_id})

    @log(info=['json'])
    def untweet(self, tweet_id: int) -> Response:
        return self.gql(Operation.Account.DeleteTweet, {'tweet_id': tweet_id})

    @log(info=['json'])
    def retweet(self, tweet_id: int) -> Response:
        return self.gql(Operation.Account.CreateRetweet, {'tweet_id': tweet_id})

    @log(info=['json'])
    def unretweet(self, tweet_id: int) -> Response:
        return self.gql(Operation.Account.DeleteRetweet, {'source_tweet_id': tweet_id})

    @log(info=['json'])
    def like(self, tweet_id: int) -> Response:
        return self.gql(Operation.Account.FavoriteTweet, {'tweet_id': tweet_id})

    @log(info=['json'])
    def unlike(self, tweet_id: int) -> Response:
        return self.gql(Operation.Account.UnfavoriteTweet, {'tweet_id': tweet_id})

    @log(info=['json'])
    def bookmark(self, tweet_id: int) -> Response:
        return self.gql(Operation.Account.CreateBookmark, {'tweet_id': tweet_id})

    @log(info=['json'])
    def unbookmark(self, tweet_id: int) -> Response:
        return self.gql(Operation.Account.DeleteBookmark, {'tweet_id': tweet_id})

    @log(info=['json'])
    def create_list(self, name: str, description: str, private: bool) -> Response:
        variables = {
            "isPrivate": private,
            "name": name,
            "description": description,
        }
        return self.gql(Operation.Account.CreateList, variables)

    @log(info=['json'])
    def update_list(self, list_id: int, name: str, description: str, private: bool) -> Response:
        variables = {
            "listId": list_id,
            "isPrivate": private,
            "name": name,
            "description": description,
        }
        return self.gql(Operation.Account.UpdateList, variables)

    @log(info=['json'])
    def update_pinned_lists(self, list_ids: list[int]) -> Response:
        """
        Update pinned lists

        Reset all pinned lists and pin all specified lists in the order they are provided.

        @param list_ids: list of list ids to pin
        @return: response
        """
        return self.gql(Operation.Account.ListsPinMany, {'listIds': list_ids})

    @log(info=['json'])
    def pin_list(self, list_id: int) -> Response:
        return self.gql(Operation.Account.ListPinOne, {'listId': list_id})

    @log(info=['json'])
    def unpin_list(self, list_id: int) -> Response:
        return self.gql(Operation.Account.ListUnpinOne, {'listId': list_id})

    @log(info=['json'])
    def add_list_member(self, list_id: int, user_id: int) -> Response:
        return self.gql(Operation.Account.ListAddMember, {'listId': list_id, "userId": user_id})

    @log(info=['json'])
    def remove_list_member(self, list_id: int, user_id: int) -> Response:
        return self.gql(Operation.Account.ListRemoveMember, {'listId': list_id, "userId": user_id})

    @log(info=['json'])
    def delete_list(self, list_id: int) -> Response:
        return self.gql(Operation.Account.DeleteList, {'listId': list_id})

    @log(info=['json'])
    def update_list_banner(self, list_id: int, filename: str) -> Response:
        media_id = self.upload_media(filename)
        return self.gql(Operation.Account.EditListBanner, {'listId': list_id, 'mediaId': media_id})

    @log(info=['json'])
    def delete_list_banner(self, list_id: int) -> Response:
        return self.gql(Operation.Account.DeleteListBanner, {'listId': list_id})

    @log(info=['json'])
    def unfollow_topic(self, topic_id: int) -> Response:
        return self.gql(Operation.Account.TopicUnfollow, {'topicId': str(topic_id)})

    @log(info=['json'])
    def follow_topic(self, topic_id: int) -> Response:
        return self.gql(Operation.Account.TopicFollow, {'topicId': str(topic_id)})

    @log(info=['json'])
    def follow(self, user_id: int) -> Response:
        settings = follow_settings.copy()
        settings |= {"user_id": user_id}
        return self.api('friendships/create.json', settings)

    @log(info=['json'])
    def unfollow(self, user_id: int) -> Response:
        settings = follow_settings.copy()
        settings |= {"user_id": user_id}
        return self.api('friendships/destroy.json', settings)

    @log(info=['json'])
    def mute(self, user_id: int) -> Response:
        settings = {'user_id': user_id}
        return self.api('mutes/users/create.json', settings)

    @log(info=['json'])
    def unmute(self, user_id: int) -> Response:
        settings = {'user_id': user_id}
        return self.api('mutes/users/destroy.json', settings)

    @log(info=['json'])
    def enable_notifications(self, user_id: int) -> Response:
        settings = notification_settings.copy()
        settings |= {'id': user_id, 'device': 'true'}
        return self.api('friendships/update.json', settings)

    @log(info=['json'])
    def disable_notifications(self, user_id: int) -> Response:
        settings = notification_settings.copy()
        settings |= {'id': user_id, 'device': 'false'}
        return self.api('friendships/update.json', settings)

    @log(info=['json'])
    def block(self, user_id: int) -> Response:
        settings = {'user_id': user_id}
        return self.api('blocks/create.json', settings)

    @log(info=['json'])
    def unblock(self, user_id: int) -> Response:
        settings = {'user_id': user_id}
        return self.api('blocks/destroy.json', settings)

    @log(info=['json'])
    def pin(self, tweet_id: int) -> Response:
        settings = {'tweet_mode': 'extended', 'id': tweet_id}
        return self.api('account/pin_tweet.json', settings)

    @log(info=['json'])
    def unpin(self, tweet_id: int) -> Response:
        settings = {'tweet_mode': 'extended', 'id': tweet_id}
        return self.api('account/unpin_tweet.json', settings)

    @log(info=['json'])
    def stats(self, rest_id: int) -> Response:
        """private endpoint?"""
        name, _ = Operation.Account.TweetStats
        params = deepcopy(operations[name])
        qid = params['queryId']
        params['variables']['rest_id'] = rest_id
        query = build_query(params)
        url = f"{self.GRAPHQL_URL}/{qid}/{name}?{query}"
        r = self.session.get(url, headers=get_headers(self.session))
        return r

    @log(info=['json'])
    def remove_interests(self, *args):
        url = f'{self.V1_URL}/account/personalization/twitter_interests.json'
        r = self.session.get(url, headers=get_headers(self.session))
        current_interests = r.json()['interested_in']
        if args == 'all':
            disabled_interests = [x['id'] for x in current_interests]
        else:
            disabled_interests = [x['id'] for x in current_interests if x['display_name'] in args]
        payload = {
            "preferences": {
                "interest_preferences": {
                    "disabled_interests": disabled_interests,
                    "disabled_partner_interests": []
                }
            }
        }
        url = f'{self.V1_URL}/account/personalization/p13n_preferences.json'
        r = self.session.post(url, headers=get_headers(self.session), json=payload)
        return r

    @log(info=['json'])
    def update_profile_image(self, filename: str) -> Response:
        media_id = self.upload_media(filename, is_profile=True)
        url = f'{self.V1_URL}/account/update_profile_image.json'
        headers = get_headers(self.session)
        params = {'media_id': media_id}
        r = self.session.post(url, headers=headers, params=params)
        return r

    @log
    def update_profile_banner(self, filename: str) -> Response:
        media_id = self.upload_media(filename, is_profile=True)
        url = f'{self.V1_URL}/account/update_profile_banner.json'
        headers = get_headers(self.session)
        params = {'media_id': media_id}
        r = self.session.post(url, headers=headers, params=params)
        return r

    @log
    def update_profile_info(self, **kwargs) -> Response:
        url = f'{self.V1_URL}/account/update_profile.json'
        headers = get_headers(self.session)
        r = self.session.post(url, headers=headers, params=kwargs)
        return r

    @log(info=['text'])
    def update_search_settings(self, settings: dict) -> Response:
        """
        Update account search settings

        @param settings: search filtering settings to enable/disable
        @return: authenticated session
        """
        twid = int(self.session.cookies.get_dict()['twid'].split('=')[-1].strip('"'))
        headers = get_headers(self.session)
        r = self.session.post(
            url=f'{self.V1_URL}/strato/column/User/{twid}/search/searchSafety',
            headers=headers,
            json=settings,
        )
        return r

    @log(info=['json'])
    def update_settings(self, settings: dict) -> Response:
        """
        Update account settings
    
        @param settings: settings to enable/disable
        @return: authenticated session
        """
        return self.api('account/settings.json', settings)

    @log(info=['json'])
    def change_password(self, old: str, new: str) -> Response:
        settings = {
            'current_password': old,
            'password': new,
            'password_confirmation': new
        }
        headers = get_headers(self.session)
        headers['content-type'] = 'application/x-www-form-urlencoded'
        url = 'https://twitter.com/i/api/i/account/change_password.json'
        r = self.session.post(url, headers=headers, data=urlencode(settings))
        return r

    @log(info=['json'])
    def logout_all_sessions(self) -> Response:
        headers = get_headers(self.session)
        url = 'https://twitter.com/i/api/account/self.sessions/revoke_all'
        r = self.session.post(url, headers=headers)
        return r
