from textwrap import dedent

from setuptools import find_packages, setup

install_requires = [
    "tqdm",
    "ujson",
    "nest_asyncio",
    "aiohttp",
    "requests",
    'uvloop; platform_system != "Windows"'
]

setup(
    name="twitter-api-client",
    version="0.5.0",
    python_requires=">=3.9.7",
    description="Twitter API",
    long_description=dedent('''
    Complete implementation of the undocumented Twitter API
    
    Includes tools to **scrape**, **automate**, and **search** twitter
    
    ### Installation
    
   ```python
    from twitter.account import Account
    
    username, password = ..., ...
    account = Account(username, password)
    
    account.create_poll('test poll 123', ['hello', 'world', 'foo', 'bar'], 10080)
    
    # DM 1 user
    account.dm([123], 'hello world', filename='test.png')
    
    # DM group of users
    account.dm([123, 234, 345], 'foo bar', filename='test.mp4')
    
    # schedule a tweet (date str or timestamp)
    account.schedule_tweet('scheduled hello', 1679912795, media=['test.jpg'])
    
    # schedule a reply tweet (date str or timestamp)
    account.schedule_tweet('scheduled world', '2023-03-25 19:11', media=['test.jpg'], reply_to=645)
    
    account.unschedule_tweet(321)
    
    # tweets
    account.tweet('test 123')
    account.tweet('test 234', media=['test.mp4'])
    account.tweet('test 345', media=['test.jpg', 'test.png', 'test.jpeg', 'test.jfif'])
    account.tweet('test 456', media=[{'file': 'test.jpeg', 'tagged_users': [123234345456], 'alt': 'some image'}])
    account.untweet(123)
    account.retweet(1633609779745820675)
    account.unretweet(1633609779745820675)
    account.quote(1633609779745820675, 'elonmusk', 'test 123')
    account.reply(1633609779745820675, 'test 123')
    account.like(1633609779745820675)
    account.unlike(1633609779745820675)
    account.bookmark(1633609779745820675)
    account.unbookmark(1633609779745820675)
    account.pin(1635479755364651008)
    account.unpin(1635479755364651008)
    
    # users
    account.follow(50393960)
    account.unfollow(50393960)
    account.mute(50393960)
    account.unmute(50393960)
    account.enable_notifications(50393960)
    account.disable_notifications(50393960)
    account.block(50393960)
    account.unblock(50393960)
    
    # other
    account.stats(50393960)
    
    # user profile
    account.update_profile_image('test.jpg')
    account.update_profile_banner('test.png')
    account.update_profile_info(name='Foo Bar', description='test 123', location='Victoria, BC')
    
    # topics
    account.follow_topic(808713037230157824)
    account.unfollow_topic(808713037230157824)
    
    # lists
    account.create_list('My List', 'description of my list', private=False)
    account.update_list(543, 'My Updated List', 'some updated description', private=False)
    account.update_list_banner(543, 'test.png')
    account.delete_list_banner(543)
    account.add_list_member(543, 50393960)
    account.remove_list_member(543, 50393960)
    account.delete_list(543)
    account.pin_list(543)
    account.unpin_list(543)
    
    # refresh all pinned lists in this order
    account.update_pinned_lists([543, 432, 321])
    
    # unpin all lists
    account.update_pinned_lists([])
    
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
        "optInFiltering": True,  # filter out nsfw content
        "optInBlocking": True,  # filter out blocked accounts
    })
    
    ## account.change_password('old password', 'new password')
    ## account.logout_all_sessions()
    
    ```
    
    
    ### Scraping
    
    #### Get all user/tweet data
    
    ```python
    from twitter.scraper import Scraper
    
    username, password = ..., ...
    scraper = Scraper(username, password)  # session
    
    ####### User Data ########
    users = scraper.user_by_screen_name(['bob123', 'jim456', 'stanley789'])
    tweets = scraper.tweets([123, 234, 345])
    likes = scraper.likes([123, 234, 345])
    tweets_and_replies = scraper.tweets_and_replies([123, 234, 345])
    media = scraper.media([123, 234, 345])
    following = scraper.following([123, 234, 345])
    followers = scraper.followers([123, 234, 345])
    
    ######## Tweet Data ########
    tweets_by_ids = scraper.tweet_by_rest_id([456, 567, 678])
    tweets_details = scraper.tweets_details([456, 567, 678])
    retweeters = scraper.retweeters([456, 567, 678])
    favoriters = scraper.favoriters([456, 567, 678])
    
    scraper.download_media([456, 567, 678])
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
