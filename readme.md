**(Work in Progress)**

Complete implementation of the undocumented Twitter API

- Frantically written in a day, crude, needs refactoring/redesign, code is repetitive.
- Includes twitter search, scraper, and automation library.


### Installation
```bash
pip install twitter-api-client
```

### Automation
```python
from src.main import *
from src.login import login

usr, pwd = ..., ...
session = login(usr, pwd)

# create tweet with images, videos, gifs, and tagged users
r = create_tweet('test 123', session, media=[{'file': 'image.jpeg', 'tagged_users': [123234345456], 'alt': 'some image'}])
r = create_tweet('test 123', session, media=['test.jpg', 'test.png'])
r = create_tweet('test 123', session, media=['test.mp4'])
r = create_tweet('test 123', session)

r = delete_tweet(123, session)

# delete all tweets in account
r = delete_all_tweets(456, session)

r = retweet(1633609779745820675, session)
r = unretweet(1633609779745820675, session)

r = quote('test 123', 'elonmusk', 1633609779745820675, session)
r = comment('test 123', 1633609779745820675, session)

r = unlike_tweet(1633609779745820675, session)
r = like_tweet(1633609779745820675, session)

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

```

### Scraping
#### User/Tweet data
```python
from src.scrape import *
from src.login import login

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
from src.search import search
from src.config.search_config import search_config

search(
    '(#dogs OR #cats) min_retweets:500',
    'min_faves:10000 @elonmusk until:2023-02-16 since:2023-02-01',
    'brasil portugal -argentina',
    'paperswithcode -tensorflow -tf',
    'skateboarding baseball guitar',
    'cheese bread butter',
    'ios android',
    config=search_config
)
```