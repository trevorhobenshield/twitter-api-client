Complete implementation of the undocumented Twitter API

Includes tools to **scrape**, **automate**, and **search** twitter

### Installation

```bash
pip install twitter-api-client
```

### Automation

```python
from twitter.main import *
from twitter.login import login

usr, pwd = ..., ...
s = login(usr, pwd)  # session

create_poll(s, 'test poll', ['hello', 'world', 'foo', 'bar'], 10080)

# DM 1 user
dm(s, [111], 'hello world', filename='test.png')

# DM group of users
dm(s, [111, 222, 333], 'foo bar', filename='test.mp4')

# tweets
tweet(s, 'test 123')
tweet(s, 'test 123', media=['test.mp4'])
tweet(s, 'test 123', media=['test.jpg', 'test.png', 'test.jpeg', 'test.jfif'])
tweet(s, 'test 123', media=[{'file': 'test.jpeg', 'tagged_users': [123234345456], 'alt': 'some image'}])
untweet(s, 123)
retweet(s, 1633609779745820675)
unretweet(s, 1633609779745820675)
quote(s, 1633609779745820675, 'elonmusk', 'test 123')
comment(s, 1633609779745820675, 'test 123')
like(s, 1633609779745820675)
unlike(s, 1633609779745820675)
bookmark(s, 1633609779745820675)
unbookmark(s, 1633609779745820675)
pin(s, 1635479755364651008)
unpin(s, 1635479755364651008)

# users
follow(s, 50393960)
unfollow(s, 50393960)
mute(s, 50393960)
unmute(s, 50393960)
enable_notifications(s, 50393960)
disable_notifications(s, 50393960)
block(s, 50393960)
unblock(s, 50393960)

# other
stats(s, 50393960)

# user profile
update_profile_image(s, 'test.jpg')
update_profile_banner(s, 'test.png')
update_profile_info(s, name='Foo Bar', description='Test 123', location='Victoria, BC')

# topics
follow_topic(s, 808713037230157824)
unfollow_topic(s, 808713037230157824)

# lists
create_list(s, 'My List', 'description of my list', private=False)
update_list(s, 123456, 'My Updated List', 'some updated description', private=False)
update_list_banner(s, 123456, 'test.png')
delete_list_banner(s, 123456)
add_list_member(s, 123456, 50393960)
remove_list_member(s, 123456, 50393960)
delete_list(s, 123456)
pin_list(s, 123456)
unpin_list(s, 123456)

# refresh all pinned lists in this order
update_pinned_lists(s, [123, 234, 345, 456])

# unpin all lists
update_pinned_lists(s, [])

# example configuration
update_account_settings(s, {
    "address_book_live_sync_enabled": False,
    "allow_ads_personalization": False,
    "allow_authenticated_periscope_requests": True,
    "allow_dm_groups_from": "following",
    "allow_dms_from": "following",
    "allow_location_history_personalization": False,
    "allow_logged_out_device_personalization": False,
    "allow_media_tagging": "none",
    "allow_sharing_data_for_third_party_personalization": False,
    "alt_text_compose_enabled": None,
    "always_use_https": True,
    "autoplay_disabled": False,
    "country_code": "us",
    "discoverable_by_email": False,
    "discoverable_by_mobile_phone": False,
    "display_sensitive_media": True,
    "dm_quality_filter": "enabled",
    "dm_receipt_setting": "all_disabled",
    "geo_enabled": False,
    "include_alt_text_compose": True,
    "include_mention_filter": True,
    "include_nsfw_admin_flag": True,
    "include_nsfw_user_flag": True,
    "include_ranked_timeline": True,
    "language": "en",
    "mention_filter": "unfiltered",
    "nsfw_admin": False,
    "nsfw_user": False,
    "personalized_trends": True,
    "protected": False,
    "ranked_timeline_eligible": None,
    "ranked_timeline_setting": None,
    "require_password_login": False,
    "requires_login_verification": False,
    "sleep_time": {
        "enabled": False,
        "end_time": None,
        "start_time": None
    },
    "translator_type": "none",
    "universal_quality_filtering_enabled": "enabled",
    "use_cookie_personalization": False,
})

# example configuration
update_search_settings(s, {
    "optInFiltering": True,  # filter out nsfw content
    "optInBlocking": True,  # filter out blocked accounts
})


```

### Scraping

#### Get all user/tweet data

```python
from twitter.scrape import *
from twitter.login import login

usr, pwd = ..., ...
s = login(usr, pwd)  # session

user_ids = [...]
usernames = [...]
tweet_ids = [...]

####### User Data ########
users = get_user_by_screen_name(s, usernames)
tweets = get_user_tweets(s, user_ids)
likes = get_likes(s, user_ids)
tweets_and_replies = get_tweets_and_replies(s, user_ids)
media = get_media(s, user_ids)
following = get_following(s, user_ids)
followers = get_followers(s, user_ids)

######## Tweet Data ########
tweet = get_tweet_by_rest_id(s, tweet_ids)
tweet_detail = get_tweets(s, tweet_ids)
retweeters = get_retweeters(s, tweet_ids)
favoriters = get_favoriters(s, tweet_ids)

download_media(s, tweet_ids)
```

#### Most recent ~100 results of user/tweet data

```python
from twitter.login import login
from twitter.scrape import query
from twitter.constants import Operation

from functools import partial

username, password = ..., ...
session = login(username, password)

user_ids = [123, 234, 345, 456]
user_query = partial(query, session, user_ids)

tweets = user_query(Operation.Data.UserTweets)
likes = user_query(Operation.Data.Likes)
followers = user_query(Operation.Data.Followers)

```

#### Search

```python   
from twitter.search import search

search(
    '(#dogs OR #cats) min_retweets:500',
    'min_faves:10000 @elonmusk until:2023-02-16 since:2023-02-01',
    'brasil portugal -argentina',
    'paperswithcode -tensorflow -tf',
    'skateboarding baseball guitar',
    'cheese bread butter',
    'ios android',
)
```

![](assets/example-search.gif)

- search results are output to `~/data/raw`
- ~400 search results rate limiting occurs

**Search Operators Reference**

https://developer.twitter.com/en/docs/twitter-api/v1/rules-and-filtering/search-operators

https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query
