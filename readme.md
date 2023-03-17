*Work in Progress

Complete implementation of the undocumented Twitter API

- Includes twitter search, scraper, and automation library.


### Installation
```bash
pip install twitter-api-client
```

### Automation

```python
from twitter.main import *
from twitter.login import login

usr, pwd = ..., ...
session = login(usr, pwd)


create_poll('test poll', ['hello', 'world', 'foo', 'bar'], 10080, session)

# DM 1 user
dm('hello world', [123], session, filename='test.png')

# DM group of users
dm('foo bar', [123, 456, 789], session, filename='test.mp4')

# tweets
tweet('test 123', session)
tweet('test 123', session, media=['test.jpg', 'test.png'])
tweet('test 123', session, media=['test.mp4'])
tweet('test 123', session, media=[{'file': 'image.jpeg', 'tagged_users': [123234345456], 'alt': 'some image'}])
untweet(123, session)
retweet(1633609779745820675, session)
unretweet(1633609779745820675, session)
quote('test 123', 'elonmusk', 1633609779745820675, session)
comment('test 123', 1633609779745820675, session)
like(1633609779745820675, session)
unlike(1633609779745820675, session)
bookmark(1633609779745820675, session)
unbookmark(1633609779745820675, session)
pin(1635479755364651008, session)
unpin(1635479755364651008, session)

# users
follow(50393960, session)
unfollow(50393960, session)
mute(50393960, session)
unmute(50393960, session)
enable_notifications(50393960, session)
disable_notifications(50393960, session)
block(50393960, session)
unblock(50393960, session)

# other
stats(50393960, session)

# user profile
update_profile_image('profile.jpg', session)
update_profile_banner('banner.jpg', session)
update_profile_info(session, name='Foo Bar', description='Test 123', location='Victoria, BC')

# topics
follow_topic(session, 123)
unfollow_topic(session, 123)

# lists
create_list(session, 'My List', 'description of my list', private=False)
update_list(session, 456, 'My Updated List', 'some updated description', private=False)
update_list_banner(session, 456, 'test.jpg')
delete_list_banner(session, 456)
add_list_member(session, 456, 678)
remove_list_member(session, 456, 678)
delete_list(session, 456)
pin_list(session, 456)
unpin_list(session, 456)
# refresh all pinned lists in this order
update_pinned_lists(session, [456, 678, 789])
# unpin all lists
update_pinned_lists(session, [])


```

### Scraping
#### User/Tweet data

```python
from twitter.scrape import *
from twitter.login import login

usr, pwd = ..., ...
session = login(usr, pwd)

user_ids = [...]
usernames = [...]
tweet_ids = [...]

######### User Data ########
users = get_user_by_screen_name(usernames, session)
tweets = get_user_tweets(user_ids, session)
likes = get_likes(user_ids, session)
tweets_and_replies = get_tweets_and_replies(user_ids, session)
media = get_media(user_ids, session)
following = get_following(user_ids, session)
followers = get_followers(user_ids, session)

######### Tweet Data ########
tweet = get_tweet_by_rest_id(tweet_ids, session)
tweet_detail = get_tweets(tweet_ids, session)
retweeters = get_retweeters(tweet_ids, session)
favoriters = get_favoriters(tweet_ids, session)

######### Media (Images/Videos) ########
download_media(tweet_ids, session)
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
