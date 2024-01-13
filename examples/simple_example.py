import pandas as pd
from twitter.util import find_key
from twitter.scraper import Scraper


def parse_tweets(data: list | dict) -> pd.DataFrame:
    """
    Parse small subset of relevant features into a DataFrame.

    Note: structure of GraphQL response is not consistent, this example may not work in all cases.

    @param data: tweets (raw GraphQL response data)
    @return: DataFrame of tweets
    """
    df = (
        pd.json_normalize((
            x.get('result', {}).get('tweet', {}).get('legacy') for x in find_key(data, 'tweet_results')),
            max_level=1
        )
        .assign(created_at=lambda x: pd.to_datetime(x['created_at'], format="%a %b %d %H:%M:%S %z %Y"))
        .sort_values('created_at', ascending=False)
        .reset_index(drop=True)
    )
    numeric = [
        'user_id_str',
        'id_str',
        'favorite_count',
        'quote_count',
        'reply_count',
        'retweet_count',
    ]
    df[numeric] = df[numeric].apply(pd.to_numeric, errors='coerce')
    df = df[[
        'id_str',
        'user_id_str',
        'created_at',
        'full_text',
        'favorite_count',
        'quote_count',
        'reply_count',
        'retweet_count',
        'lang',
    ]]
    return df


if __name__ == '__main__':
    ## sign-in with credentials
    email, username, password = ..., ..., ...
    scraper = Scraper(email, username, password)

    ## or, resume session using cookies
    # scraper = Scraper(cookies={"ct0": ..., "auth_token": ...})

    tweets = scraper.tweets([
        ...,  # tweet ids
    ])

    df = parse_tweets(tweets)

    df.to_csv('tweets.csv')
    # df.to_parquet('tweets.parquet', engine='pyarrow')
