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

# DM one user
dm('hello world', [123], session)

# DM group of users
dm('foo bar', [123, 456, 789], session)

# create tweet with images, videos, gifs, and tagged users
r = tweet('test 123', session, media=[{'file': 'image.jpeg', 'tagged_users': [123234345456], 'alt': 'some image'}])
r = tweet('test 123', session, media=['test.jpg', 'test.png'])
r = tweet('test 123', session, media=['test.mp4'])
r = tweet('test 123', session)

# delete tweet
r = untweet(123, session)

r = retweet(1633609779745820675, session)
r = unretweet(1633609779745820675, session)

r = quote('test 123', 'elonmusk', 1633609779745820675, session)
r = comment('test 123', 1633609779745820675, session)

r = unlike(1633609779745820675, session)
r = like(1633609779745820675, session)

r = follow(50393960, session)
r = unfollow(50393960, session)

r = mute(50393960, session)
r = unmute(50393960, session)

r = enable_notifications(50393960, session)
r = disable_notifications(50393960, session)

r = block(50393960, session)
r = unblock(50393960, session)

# some hidden user attribute?
r = stats(50393960, session)

r = bookmark(1633609779745820675, session)
r = unbookmark(1633609779745820675, session)
r = unbookmark_all(1633609779745820675, session)

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
users = get_user_by_screen_name(usernames, session=session)
tweets = get_user_tweets(user_ids, session=session)
likes = get_likes(user_ids, session=session)
tweets_and_replies = get_tweets_and_replies(user_ids, session=session)
media = get_media(user_ids, session=session)
following = get_following(user_ids, session=session)
followers = get_followers(user_ids, session=session)

######### Tweet Data ########
tweet = get_tweet_by_rest_id(tweet_ids, session=session)
tweet_detail = get_tweets(tweet_ids, session=session)
retweeters = get_retweeters(tweet_ids, session=session)
favoriters = get_favoriters(tweet_ids, session=session)

######### Media (Images/Videos) ########
download_media(tweet_ids, session=session)
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