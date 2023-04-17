
```bash
pip install twitter-api-client
```

### Example
```python
from twitter.noauth.scraper import Scraper

scraper = Scraper()

users = scraper.user(['foo', 'bar', 'baz'])
users = scraper.user_by_id([123, 234, 345])
users = scraper.users_by_ids([123, 234, 345])  # special batch query

tweets = scraper.tweet_by_id([987, 876, 765])  # condensed
tweets = scraper.tweet_details([987, 876, 765])

user_tweets = scraper.tweets([123, 234, 345])
user_tweets_replies = scraper.tweets_and_replies([123, 234, 345])
user_media = scraper.media([123, 234, 345])
```

