**(Work in Progress)** Complete implementation of the undocumented Twitter API

- Written very quickly, crude, needs refactoring/redesign


```bash
pip install twitter-api-client
```

### Usage
```python
from src.main import *

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

