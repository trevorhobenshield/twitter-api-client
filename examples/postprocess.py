import re
import pandas as pd
from twitter.util import find_key


def get_tweets(data: list | dict, cols: list[str] = None):
    """
    Convert raw GraphQL response to DataFrame

    @param data: tweets
    @param cols: option to only include certain columns
    @return: DataFrame of tweets
    """
    entries = [y for x in find_key(data, 'entries') for y in x]
    # filter out promoted tweets
    tweets = [x for x in entries if not x.get('entryId').startswith('promoted')]
    df = (
        pd.json_normalize(find_key(tweets, 'tweet_results'), max_level=1)
        ['result.legacy'].apply(pd.Series)
        .dropna(subset='user_id_str')
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
    cols = cols or [
        'id_str',
        'user_id_str',
        'created_at',
        'full_text',
        'favorite_count',
        'quote_count',
        'reply_count',
        'retweet_count',
        'lang',
    ]
    return df[cols]


def get_tweets_urls(data: dict | list, expr: str, cols: list[str] = None) -> pd.DataFrame:
    """
    Convert raw GraphQL response to DataFrame

    Search for tweets containing specific urls by regex

    @param data: tweets
    @param expr: regex to match urls
    @param cols: option to only include certain columns
    @return: DataFrame of tweets matching the expression
    """
    tweet_results = find_key(data, 'tweet_results')
    results = []
    for res in tweet_results:
        legacy = res.get('result', {}).get('legacy', {})
        urls = find_key(res, 'expanded_url')
        if any(re.search(expr, x) for x in urls):
            results.append({'urls': urls} | legacy)
    try:
        df = (
            pd.DataFrame(results)
            .assign(date=lambda x: pd.to_datetime(x['created_at'], format="%a %b %d %H:%M:%S %z %Y"))
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
        cols = cols or [
            'id_str',
            'user_id_str',
            'created_at',
            'urls',
            'full_text',
            'favorite_count',
            'quote_count',
            'reply_count',
            'retweet_count',
            'lang',
        ]
        return df[cols]
    except Exception as e:
        print(e)
