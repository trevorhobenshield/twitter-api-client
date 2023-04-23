from textwrap import dedent

from setuptools import find_packages, setup

install_requires = [
    "nest_asyncio",
    "aiohttp",
    "httpx",
    "tqdm",
    "orjson",
    'uvloop; platform_system != "Windows"',
]

setup(
    name="twitter-api-client",
    version="0.7.6",
    python_requires=">=3.11.0",
    description="Twitter API",
    long_description=dedent('''
    Implementation of Twitter's v1, v2, and GraphQL APIs
    
    Includes tools to **scrape**, **automate**, and **search**.

    ### Automation
    
    ```python
    from twitter.account import Account
    
    email, username, password = ..., ..., ...
    account = Account(email, username, password, debug=2, save=True)
    
    account.tweet('test 123')
    account.untweet(123456)
    account.retweet(123456)
    account.unretweet(123456)
    account.reply('foo', tweet_id=123456)
    account.quote('bar', tweet_id=123456)
    account.schedule_tweet('schedule foo', 1681851240)
    account.unschedule_tweet(123456)
    
    account.tweet('hello world', media=[
        {'media': 'test.jpg', 'alt': 'some alt text', 'tagged_users': [123]},
        {'media': 'test.jpeg', 'alt': 'some alt text', 'tagged_users': [123]},
        {'media': 'test.png', 'alt': 'some alt text', 'tagged_users': [123]},
        {'media': 'test.jfif', 'alt': 'some alt text', 'tagged_users': [123]},
    ])
    
    account.schedule_tweet('foo bar', '2023-04-18 15:42', media=[
        {'media': 'test.gif', 'alt': 'some alt text'},
    ])
    
    account.schedule_reply('hello world', '2023-04-19 15:42', tweet_id=123456, media=[
        {'media': 'test.gif', 'alt': 'some alt text'},
    ])
    
    account.dm('my message', [1234], media='test.jpg')
    
    account.create_poll('test poll 123', ['hello', 'world', 'foo', 'bar'], 10080)
    
    # tweets
    account.like(123456)
    account.unlike(123456)
    account.bookmark(123456)
    account.unbookmark(123456)
    account.pin(123456)
    account.unpin(123456)
    
    # users
    account.follow(1234)
    account.unfollow(1234)
    account.mute(1234)
    account.unmute(1234)
    account.enable_notifications(1234)
    account.disable_notifications(1234)
    account.block(1234)
    account.unblock(1234)
    
    # user profile
    account.update_profile_image('test.jpg')
    account.update_profile_banner('test.png')
    account.update_profile_info(name='Foo Bar', description='test 123', location='Victoria, BC')
    
    #  topics
    account.follow_topic(111)
    account.unfollow_topic(111)
    
    # lists
    account.create_list('My List', 'description of my list', private=False)
    account.update_list(222, 'My Updated List', 'some updated description', private=False)
    account.update_list_banner(222, 'test.png')
    account.delete_list_banner(222)
    account.add_list_member(222, 1234)
    account.remove_list_member(222, 1234)
    account.delete_list(222)
    account.pin_list(222)
    account.unpin_list(222)
    
    # refresh all pinned lists in this order
    account.update_pinned_lists([222, 111, 333])
    
    # unpin all lists
    account.update_pinned_lists([])
    
    # get timelines
    timeline = account.home_timeline()
    latest_timeline = account.home_latest_timeline(limit=500)
    
    # get bookmarks
    bookmarks = account.bookmarks()
    
    # example configuration
    account.update_settings({
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
        "display_sensitive_media": False,
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
    account.update_search_settings({
        "optInFiltering": True,  # filter nsfw content
        "optInBlocking": True,  # filter blocked accounts
    })
    
    ## change_password('old pwd','new pwd)
    
    ```
    
    ### Scraping
    
    #### Get all user/tweet data
    
    ```python
    from twitter.scraper import Scraper
    
    email, username, password = ..., ..., ...
    scraper = Scraper(email, username, password, debug=1, save=True)
    
    # user data
    users = scraper.users(['foo', 'bar', 'hello', 'world'])
    users = scraper.users_by_ids([123, 234, 345])  # batch-request
    tweets = scraper.tweets([123, 234, 345])
    likes = scraper.likes([123, 234, 345])
    tweets_and_replies = scraper.tweets_and_replies([123, 234, 345])
    media = scraper.media([123, 234, 345])
    following = scraper.following([123, 234, 345])
    followers = scraper.followers([123, 234, 345])
    scraper.tweet_stats([111111, 222222, 333333])
    
    # get recommended users based on user
    scraper.recommended_users()
    scraper.recommended_users(123)
    
    # tweet data
    tweets_by_ids = scraper.tweets_by_id([987, 876, 754])
    tweets_details = scraper.tweets_details([987, 876, 754])
    retweeters = scraper.retweeters([987, 876, 754])
    favoriters = scraper.favoriters([987, 876, 754])
    
    scraper.download_media([
        111111,
        222222,
        333333,
        444444,
    ])
    

    
    # trends
    scraper.trends()
    ```
    
    #### Search
    
    ```python   
    from twitter.search import Search
    
    email, username, password = ..., ..., ...
    search = Search(email, username, password)
    
    res = search.run(
        '(#dogs OR #cats) min_retweets:500',
        'min_faves:10000 @elonmusk until:2023-02-16 since:2023-02-01',
        'brasil portugal -argentina',
        'paperswithcode -tensorflow -tf',
        'skateboarding baseball guitar',
        'cheese bread butter',
        'ios android',
        limit=100,
    )
    ```
    '''),
    long_description_content_type='text/markdown',
    author="Trevor Hobenshield",
    author_email="trevorhobenshield@gmail.com",
    url="https://github.com/trevorhobenshield/twitter-api-client",
    install_requires=install_requires,
    keywords="twitter api client async search automation bot scrape",
    packages=find_packages(),
    include_package_data=True,
)
