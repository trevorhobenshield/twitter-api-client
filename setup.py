import sys
from textwrap import dedent
from setuptools import find_packages, setup

install_requires = [
    "tqdm",
    "ujson",
    "nest_asyncio",
    "aiohttp",
    "requests",
]
if sys.platform != 'win32':
    install_requires.append('uvloop')

setup(
    name="twitter-api-client",
    version="0.3.5",
    description="Twitter API",
    long_description=dedent('''
    Complete implementation of the undocumented Twitter API
    
    Includes tools to **scrape**, **automate**, and **search** twitter
    
    ### Installation
    
    ```bash
    pip install twitter-api-client
    ```
    
    ### Automation
    
    ```python
    from twitter import account
    from twitter.login import login
    
    username,password = ...,...
    s = login(username, password)  # session
    
    account.create_poll(s, 'test poll', ['hello', 'world', 'foo', 'bar'], 10080)
    
    # DM 1 user
    account.dm(s, [111], 'hello world', filename='test.png')
    
    # DM group of users
    account.dm(s, [111, 222, 333], 'foo bar', filename='test.mp4')
    
    # tweets
    account.tweet(s, 'test 123')
    account.tweet(s, 'test 123', media=['test.mp4'])
    account.tweet(s, 'test 123', media=['test.jpg', 'test.png', 'test.jpeg', 'test.jfif'])
    account.tweet(s, 'test 123', media=[{'file': 'test.jpeg', 'tagged_users': [123234345456], 'alt': 'some image'}])
    account.untweet(s, 123)
    account.retweet(s, 1633609779745820675)
    account.unretweet(s, 1633609779745820675)
    account.quote(s, 1633609779745820675, 'elonmusk', 'test 123')
    account.comment(s, 1633609779745820675, 'test 123')
    account.like(s, 1633609779745820675)
    account.unlike(s, 1633609779745820675)
    account.bookmark(s, 1633609779745820675)
    account.unbookmark(s, 1633609779745820675)
    account.pin(s, 1635479755364651008)
    account.unpin(s, 1635479755364651008)
    
    # users
    account.follow(s, 50393960)
    account.unfollow(s, 50393960)
    account.mute(s, 50393960)
    account.unmute(s, 50393960)
    account.enable_notifications(s, 50393960)
    account.disable_notifications(s, 50393960)
    account.block(s, 50393960)
    account.unblock(s, 50393960)
    
    # other
    account.stats(s, 50393960)
    
    # user profile
    account.update_profile_image(s, 'test.jpg')
    account.update_profile_banner(s, 'test.png')
    account.update_profile_info(s, name='Foo Bar', description='Test 123', location='Victoria, BC')
    
    # topics
    account.follow_topic(s, 808713037230157824)
    account.unfollow_topic(s, 808713037230157824)
    
    # lists
    account.create_list(s, 'My List', 'description of my list', private=False)
    account.update_list(s, 123456, 'My Updated List', 'some updated description', private=False)
    account.update_list_banner(s, 123456, 'test.png')
    account.delete_list_banner(s, 123456)
    account.add_list_member(s, 123456, 50393960)
    account.remove_list_member(s, 123456, 50393960)
    account.delete_list(s, 123456)
    account.pin_list(s, 123456)
    account.unpin_list(s, 123456)
    # refresh all pinned lists in this order
    account.update_pinned_lists(s, [123, 234, 345, 456])
    
    # unpin all lists
    account.update_pinned_lists(s, [])
    
    # example configuration
    account.update_settings(s, {
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
    account.update_search_settings(s, {
        "optInFiltering": True,  # filter out nsfw content
        "optInBlocking": True,  # filter out blocked accounts
    })
    
    
    ```
    
    ### Scraping
    
    #### Get all user/tweet data
    
    ```python
    from twitter import scraper
    from twitter.login import login
    
    username,password = ...,...
    s = login(username, password)  # session
    
    ####### User Data ########
    users = scraper.get_user_by_screen_name(s, ['bob123', 'jim456', 'stanley789'])
    tweets = scraper.get_user_tweets(s, [123, 234, 345])
    likes = scraper.get_likes(s, [123, 234, 345])
    tweets_and_replies = scraper.get_tweets_and_replies(s, [123, 234, 345])
    media = scraper.get_media(s, [123, 234, 345])
    following = scraper.get_following(s, [123, 234, 345])
    followers = scraper.get_followers(s, [123, 234, 345])
    
    ######## Tweet Data ########
    tweet = scraper.get_tweets_by_rest_id(s, [456, 567, 678])
    tweet_detail = scraper.get_tweets(s, [456, 567, 678])
    retweeters = scraper.get_retweeters(s, [456, 567, 678])
    favoriters = scraper.get_favoriters(s, [456, 567, 678])
    
    scraper.download_media(s, [456, 567, 678])
    ```
    
    #### Most recent ~100 results of user/tweet data
    
    ```python
    from twitter.login import login
    from twitter.constants import Operation
    from twitter import scraper
    from functools import partial
    
    username, password = ..., ...
    session = login(username, password)
    
    user_ids = [123, 234, 345, 456]
    user_query = partial(scraper.query, session, user_ids)
    
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
    '''),
    long_description_content_type='text/markdown',
    author="Trevor Hobenshield",
    author_email="trevorhobenshield@gmail.com",
    url="https://github.com/trevorhobenshield/twitter-api",
    install_requires=install_requires,
    keywords="twitter api client async search automation bot scrape",
    packages=find_packages(),
    include_package_data=True,
)
