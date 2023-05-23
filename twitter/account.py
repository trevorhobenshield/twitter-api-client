import hashlib
import logging.config
import math
import mimetypes
import random
import time
from copy import deepcopy
from datetime import datetime
from logging import Logger
from pathlib import Path
from urllib.parse import urlencode
from uuid import uuid1, getnode

import orjson
from httpx import Response
from tqdm import tqdm

from .constants import *
from .login import login
from .util import find_key, get_headers, fmt_status, get_cursor, save_data


class Account:

    def __init__(self, email: str, username: str, password: str, **kwargs):
        self.session = login(email, username, password, **kwargs)
        self.gql_url = 'https://twitter.com/i/api/graphql'
        self.v1_url = 'https://api.twitter.com/1.1'
        self.save = kwargs.get('save', True)
        self.debug = kwargs.get('debug', 0)
        self.logger = self.init_logger(kwargs.get('log_config', False))

    @staticmethod
    def init_logger(cfg: dict) -> Logger:
        logging.config.dictConfig(cfg or log_config)
        return logging.getLogger(__name__)

    def gql(self, method: str, operation: tuple, variables: dict, features: dict = Operation.default_features) -> dict:
        qid, op = operation
        params = {
            'queryId': qid,
            'features': features,
            'variables': Operation.default_variables | variables
        }
        if method == 'POST':
            data = {'json': params}
        else:
            data = {'params': {k: orjson.dumps(v).decode() for k, v in params.items()}}
        r = self.session.request(
            method=method,
            url=f'{self.gql_url}/{qid}/{op}',
            headers=get_headers(self.session),
            **data
        )
        if self.debug:
            self.log(r)
        if self.save:
            save_data(r.json(), op, self.session.cookies.get('username', '_'))
        return r.json()

    def v1(self, path: str, params: dict) -> dict:
        headers = get_headers(self.session)
        headers['content-type'] = 'application/x-www-form-urlencoded'
        r = self.session.post(f'{self.v1_url}/{path}', headers=headers, data=urlencode(params))
        if self.debug:
            self.log(r)
        if self.save:
            save_data(r.json(), '_', self.session.cookies.get('username', '_'))
        return r.json()

    def create_poll(self, text: str, choices: list[str], poll_duration: int) -> dict:
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
        r = self.session.post(url, headers=headers, params={'card_data': orjson.dumps(options).decode()})
        card_uri = r.json()['card_uri']
        r = self.tweet(text, poll_params={'card_uri': card_uri})
        return r

    def dm(self, text: str, receivers: list[int], media: str = '') -> dict:
        variables = {
            "message": {},
            "requestId": str(uuid1(getnode())),
            "target": {"participant_ids": receivers},
        }
        if media:
            media_id = self._upload_media(media, is_dm=True)
            variables['message']['media'] = {'id': media_id, 'text': text}
        else:
            variables['message']['text'] = {'text': text}
        return self.gql('POST', Operation.useSendMessageMutation, variables)

    def tweet(self, text: str, *, media: any = None, **kwargs) -> dict:
        variables = {
            'tweet_text': text,
            'dark_request': False,
            'media': {
                'media_entities': [],
                'possibly_sensitive': False,
            },
            'semantic_annotation_ids': [],
        }
        if media:
            for m in media:
                media_id = self._upload_media(m['media'])
                variables['media']['media_entities'].append({
                    'media_id': media_id,
                    'tagged_users': m.get('tagged_users', [])
                })
                if alt := m.get('alt'):
                    self._add_alt_text(media_id, alt)
        if reply_params := kwargs.get('reply_params', {}):
            variables |= reply_params
        if quote_params := kwargs.get('quote_params', {}):
            variables |= quote_params
        if poll_params := kwargs.get('poll_params', {}):
            variables |= poll_params
        return self.gql('POST', Operation.CreateTweet, variables)

    def schedule_tweet(self, text: str, date: int | str, *, media: list = None) -> dict:
        variables = {
            'post_tweet_request': {
                'auto_populate_reply_metadata': False,
                'status': text,
                'exclude_reply_user_ids': [],
                'media_ids': [],
            },
            'execute_at': (
                datetime.strptime(date, "%Y-%m-%d %H:%M").timestamp()
                if isinstance(date, str)
                else date
            ),
        }
        if media:
            for m in media:
                media_id = self._upload_media(m['media'])
                variables['post_tweet_request']['media_ids'].append(media_id)
                if alt := m.get('alt'):
                    self._add_alt_text(media_id, alt)
        return self.gql('POST', Operation.CreateScheduledTweet, variables)

    def schedule_reply(self, text: str, date: int | str, tweet_id: int, *, media: list = None) -> dict:
        variables = {
            'post_tweet_request': {
                'auto_populate_reply_metadata': True,
                'in_reply_to_status_id': tweet_id,
                'status': text,
                'exclude_reply_user_ids': [],
                'media_ids': [],
            },
            'execute_at': (
                datetime.strptime(date, "%Y-%m-%d %H:%M").timestamp()
                if isinstance(date, str)
                else date
            ),
        }
        if media:
            for m in media:
                media_id = self._upload_media(m['media'])
                variables['post_tweet_request']['media_ids'].append(media_id)
                if alt := m.get('alt'):
                    self._add_alt_text(media_id, alt)
        return self.gql('POST', Operation.CreateScheduledTweet, variables)

    def unschedule_tweet(self, tweet_id: int) -> dict:
        variables = {
            'scheduled_tweet_id': tweet_id,
        }
        return self.gql('POST', Operation.DeleteScheduledTweet, variables)

    def untweet(self, tweet_id: int) -> dict:
        variables = {
            'tweet_id': tweet_id,
            'dark_request': False,
        }
        return self.gql('POST', Operation.DeleteTweet, variables)

    def reply(self, text: str, tweet_id: int) -> dict:
        variables = {
            'tweet_text': text,
            'reply': {
                'in_reply_to_tweet_id': tweet_id,
                'exclude_reply_user_ids': [],
            },
            'batch_compose': 'BatchSubsequent',
            'dark_request': False,
            'media': {
                'media_entities': [],
                'possibly_sensitive': False,
            },
            'semantic_annotation_ids': [],
        }
        return self.gql('POST', Operation.CreateTweet, variables)

    def quote(self, text: str, tweet_id: int) -> dict:
        variables = {
            'tweet_text': text,
            # can use `i` as it resolves to screen_name
            'attachment_url': f'https://twitter.com/i/status/{tweet_id}',
            'dark_request': False,
            'media': {
                'media_entities': [],
                'possibly_sensitive': False,
            },
            'semantic_annotation_ids': [],
        }
        return self.gql('POST', Operation.CreateTweet, variables)

    def retweet(self, tweet_id: int) -> dict:
        variables = {
            "tweet_id": tweet_id,
            "dark_request": False
        }
        return self.gql('POST', Operation.CreateRetweet, variables)

    def unretweet(self, tweet_id: int) -> dict:
        variables = {
            "source_tweet_id": tweet_id,
            "dark_request": False
        }
        return self.gql('POST', Operation.DeleteRetweet, variables)

    def like(self, tweet_id: int) -> dict:
        variables = {'tweet_id': tweet_id}
        return self.gql('POST', Operation.FavoriteTweet, variables)

    def unlike(self, tweet_id: int) -> dict:
        variables = {'tweet_id': tweet_id}
        return self.gql('POST', Operation.UnfavoriteTweet, variables)

    def bookmark(self, tweet_id: int) -> dict:
        variables = {'tweet_id': tweet_id}
        return self.gql('POST', Operation.CreateBookmark, variables)

    def unbookmark(self, tweet_id: int) -> dict:
        variables = {'tweet_id': tweet_id}
        return self.gql('POST', Operation.DeleteBookmark, variables)

    def create_list(self, name: str, description: str, private: bool) -> dict:
        variables = {
            "isPrivate": private,
            "name": name,
            "description": description,
        }
        return self.gql('POST', Operation.CreateList, variables)

    def update_list(self, list_id: int, name: str, description: str, private: bool) -> dict:
        variables = {
            "listId": list_id,
            "isPrivate": private,
            "name": name,
            "description": description,
        }
        return self.gql('POST', Operation.UpdateList, variables)

    def update_pinned_lists(self, list_ids: list[int]) -> dict:
        """
        Update pinned lists.
        Reset all pinned lists and pin all specified lists in the order they are provided.

        @param list_ids: list of list ids to pin
        @return: response
        """
        return self.gql('POST', Operation.ListsPinMany, {'listIds': list_ids})

    def pin_list(self, list_id: int) -> dict:
        return self.gql('POST', Operation.ListPinOne, {'listId': list_id})

    def unpin_list(self, list_id: int) -> dict:
        return self.gql('POST', Operation.ListUnpinOne, {'listId': list_id})

    def add_list_member(self, list_id: int, user_id: int) -> dict:
        return self.gql('POST', Operation.ListAddMember, {'listId': list_id, "userId": user_id})

    def remove_list_member(self, list_id: int, user_id: int) -> dict:
        return self.gql('POST', Operation.ListRemoveMember, {'listId': list_id, "userId": user_id})

    def delete_list(self, list_id: int) -> dict:
        return self.gql('POST', Operation.DeleteList, {'listId': list_id})

    def update_list_banner(self, list_id: int, media: str) -> dict:
        media_id = self._upload_media(media)
        variables = {'listId': list_id, 'mediaId': media_id}
        return self.gql('POST', Operation.EditListBanner, variables)

    def delete_list_banner(self, list_id: int) -> dict:
        return self.gql('POST', Operation.DeleteListBanner, {'listId': list_id})

    def follow_topic(self, topic_id: int) -> dict:
        variables = {'topicId': str(topic_id)}
        return self.gql('POST', Operation.TopicFollow, variables)

    def unfollow_topic(self, topic_id: int) -> dict:
        variables = {'topicId': str(topic_id)}
        return self.gql('POST', Operation.TopicUnfollow, variables)

    def pin(self, tweet_id: int) -> dict:
        params = {'tweet_mode': 'extended', 'id': tweet_id}
        return self.v1('account/pin_tweet.json', params)

    def unpin(self, tweet_id: int) -> dict:
        params = {'tweet_mode': 'extended', 'id': tweet_id}
        return self.v1('account/unpin_tweet.json', params)

    def follow(self, user_id: int) -> dict:
        settings = deepcopy(follow_settings)
        settings |= {"user_id": user_id}
        return self.v1('friendships/create.json', settings)

    def unfollow(self, user_id: int) -> dict:
        settings = deepcopy(follow_settings)
        settings |= {"user_id": user_id}
        return self.v1('friendships/destroy.json', settings)

    def mute(self, user_id: int) -> dict:
        params = {'user_id': user_id}
        return self.v1('mutes/users/create.json', params)

    def unmute(self, user_id: int) -> dict:
        params = {'user_id': user_id}
        return self.v1('mutes/users/destroy.json', params)

    def enable_notifications(self, user_id: int) -> dict:
        settings = deepcopy(notification_settings)
        settings |= {'id': user_id, 'device': 'true'}
        return self.v1('friendships/update.json', settings)

    def disable_notifications(self, user_id: int) -> dict:
        settings = deepcopy(notification_settings)
        settings |= {'id': user_id, 'device': 'false'}
        return self.v1('friendships/update.json', settings)

    def block(self, user_id: int) -> dict:
        params = {'user_id': user_id}
        return self.v1('blocks/create.json', params)

    def unblock(self, user_id: int) -> dict:
        params = {'user_id': user_id}
        return self.v1('blocks/destroy.json', params)

    def update_profile_image(self, media: str) -> Response:
        media_id = self._upload_media(media, is_profile=True)
        url = f'{self.v1_url}/account/update_profile_image.json'
        headers = get_headers(self.session)
        params = {'media_id': media_id}
        r = self.session.post(url, headers=headers, params=params)
        return r

    def update_profile_banner(self, media: str) -> Response:
        media_id = self._upload_media(media, is_profile=True)
        url = f'{self.v1_url}/account/update_profile_banner.json'
        headers = get_headers(self.session)
        params = {'media_id': media_id}
        r = self.session.post(url, headers=headers, params=params)
        return r

    def update_profile_info(self, **kwargs) -> Response:
        url = f'{self.v1_url}/account/update_profile.json'
        headers = get_headers(self.session)
        r = self.session.post(url, headers=headers, params=kwargs)
        return r

    def update_search_settings(self, settings: dict) -> Response:
        twid = int(self.session.cookies.get('twid').split('=')[-1].strip('"'))
        headers = get_headers(self.session)
        r = self.session.post(
            url=f'{self.v1_url}/strato/column/User/{twid}/search/searchSafety',
            headers=headers,
            json=settings,
        )
        self.logger.debug(r)
        return r

    def update_settings(self, settings: dict) -> dict:
        return self.v1('account/settings.json', settings)

    def change_password(self, old: str, new: str) -> dict:
        params = {
            'current_password': old,
            'password': new,
            'password_confirmation': new
        }
        headers = get_headers(self.session)
        headers['content-type'] = 'application/x-www-form-urlencoded'
        url = 'https://twitter.com/i/api/i/account/change_password.json'
        r = self.session.post(url, headers=headers, data=urlencode(params))
        return r.json()

    def remove_interests(self, *args):
        """
        Pass 'all' to remove all interests
        """
        r = self.session.get(
            f'{self.v1_url}/account/personalization/twitter_interests.json',
            headers=get_headers(self.session)
        )
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
        r = self.session.post(
            f'{self.v1_url}/account/personalization/p13n_preferences.json',
            headers=get_headers(self.session),
            json=payload
        )
        return r

    def home_timeline(self, limit=math.inf) -> list[dict]:
        return self._paginate('POST', Operation.HomeTimeline, Operation.default_variables, limit)

    def home_latest_timeline(self, limit=math.inf) -> list[dict]:
        return self._paginate('POST', Operation.HomeLatestTimeline, Operation.default_variables, limit)

    def bookmarks(self, limit=math.inf) -> list[dict]:
        return self._paginate('GET', Operation.Bookmarks, {}, limit)

    def _paginate(self, method: str, operation: tuple, variables: dict, limit: int) -> list[dict]:
        initial_data = self.gql(method, operation, variables)
        res = [initial_data]
        ids = set(find_key(initial_data, 'rest_id'))
        dups = 0
        DUP_LIMIT = 3

        cursor = get_cursor(initial_data)
        while (dups < DUP_LIMIT) and cursor:
            prev_len = len(ids)
            if prev_len >= limit:
                return res

            variables['cursor'] = cursor
            data = self.gql(method, operation, variables)

            cursor = get_cursor(data)
            ids |= set(find_key(data, 'rest_id'))

            if self.debug:
                self.logger.debug(f'cursor: {cursor}\tunique results: {len(ids)}')

            if prev_len == len(ids):
                dups += 1

            res.append(data)
        return res

    def _upload_media(self, filename: str, is_dm: bool = False, is_profile=False) -> int | None:

        def check_media(category: str, size: int) -> None:
            fmt = lambda x: f'{(x / 1e6):.2f} MB'
            msg = lambda x: f'cannot upload {fmt(size)} {category}, max size is {fmt(x)}'
            if category == 'image' and size > MAX_IMAGE_SIZE:
                raise Exception(msg(MAX_IMAGE_SIZE))
            if category == 'gif' and size > MAX_GIF_SIZE:
                raise Exception(msg(MAX_GIF_SIZE))
            if category == 'video' and size > MAX_VIDEO_SIZE:
                raise Exception(msg(MAX_VIDEO_SIZE))

        if is_profile:
            url = 'https://upload.twitter.com/i/media/upload.json'
        else:
            url = 'https://upload.twitter.com/1.1/media/upload.json'

        file = Path(filename)
        total_bytes = file.stat().st_size
        headers = get_headers(self.session)

        upload_type = 'dm' if is_dm else 'tweet'
        media_type = mimetypes.guess_type(file)[0]
        media_category = f'{upload_type}_gif' if 'gif' in media_type else f'{upload_type}_{media_type.split("/")[0]}'

        check_media(media_category, total_bytes)

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
                        self.logger.debug(f'{r.status_code} {r.text}')
                        raise Exception(f'[{RED}error{RESET}] upload failed')
                    i += 1
                    pbar.update(f.tell() - pbar.n)

        data = {'command': 'FINALIZE', 'media_id': media_id, 'allow_async': 'true'}
        if is_dm:
            data |= {'original_md5': hashlib.md5(file.read_bytes()).hexdigest()}
        r = self.session.post(url=url, headers=headers, data=data)

        # self.logger.debug(f'processing, please wait...')
        processing_info = r.json().get('processing_info')
        while processing_info:
            state = processing_info['state']
            if error := processing_info.get("error"):
                raise Exception(f'media upload failed: {error}')
            if state == MEDIA_UPLOAD_SUCCEED:
                break
            if state == MEDIA_UPLOAD_FAIL:
                raise Exception(f'[{RED}error{RESET}] media processing failed')
            check_after_secs = processing_info.get('check_after_secs', random.randint(1, 5))
            time.sleep(check_after_secs)
            params = {'command': 'STATUS', 'media_id': media_id}
            r = self.session.get(url=url, headers=headers, params=params)
            processing_info = r.json().get('processing_info')
        # self.logger.debug('processing complete')
        return media_id

    def _add_alt_text(self, media_id: int, text: str) -> Response:
        params = {"media_id": media_id, "alt_text": {"text": text}}
        url = f'{self.v1_url}/media/metadata/create.json'
        r = self.session.post(url, headers=get_headers(self.session), json=params)
        return r

    def log(self, response: Response):
        status = fmt_status(response.status_code)
        if 'json' in response.headers.get('content-type', ''):
            if response.json().get('errors'):
                self.logger.debug(f'[{RED}twitter error{RESET}]')
                self.logger.debug(f'{response.url}')
                self.logger.debug(f'{response.text}')
                return
        self.logger.debug(status)
        if self.debug >= 1:
            self.logger.debug(f'{response.url}')
        if self.debug >= 2:
            self.logger.debug(f'{response.text}')
        if self.debug >= 3:
            self.logger.debug(f'{response.headers}')
        if self.debug >= 4:
            self.logger.debug(f'{response.cookies}')
