from dataclasses import dataclass


@dataclass
class Operation:
    ProfileSpotlightsQuery = '9zwVLJ48lmVUk8u_Gh9DmA', 'ProfileSpotlightsQuery', 'screen_name'
    UserByScreenName = 'sLVLhk0bGj3MVFEKTdax1w', 'UserByScreenName', 'screen_name'
    UserByRestId = 'GazOglcBvgLigl3ywt6b3Q', 'UserByRestId', 'userId'
    UsersByRestIds = 'OJBgJQIrij6e3cjqQ3Zu1Q', 'UsersByRestIds', 'userIds'
    UserTweets = 'HuTx74BxAnezK1gWvYY7zg', 'UserTweets', 'userId'
    UserMedia = 'YqiE3JL1KNgf9nSljYdxaA', 'UserMedia', 'userId'
    UserTweetsAndReplies = 'RIWc55YCNyUJ-U3HHGYkdg', 'UserTweetsAndReplies', 'userId'
    TweetResultByRestId = 'D_jNhjWZeRZT5NURzfJZSQ', 'TweetResultByRestId', 'tweetId'
    TweetDetail = 'zXaXQgfyR4GxE21uwYQSyA', 'TweetDetail', 'focalTweetId'

    default_variables = {
        "count": 1000,
        "withSafetyModeUserFields": True,
        "includePromotedContent": True,
        "withQuickPromoteEligibilityTweetFields": True,
        "withVoice": True,
        "withV2Timeline": True,
        "withDownvotePerspective": False,
        "withBirdwatchNotes": True,
        "withCommunity": True,
        "withSuperFollowsUserFields": True,
        "withReactionsMetadata": False,
        "withReactionsPerspective": False,
        "withSuperFollowsTweetFields": True
    }

    default_features = {
        'blue_business_profile_image_shape_enabled': True,
        'responsive_web_graphql_exclude_directive_enabled': True,
        'verified_phone_label_enabled': False,
        'responsive_web_graphql_skip_user_profile_image_extensions_enabled': False,
        'responsive_web_graphql_timeline_navigation_enabled': True,
        'tweetypie_unmention_optimization_enabled': True, 'vibe_api_enabled': True,
        'responsive_web_edit_tweet_api_enabled': True,
        'graphql_is_translatable_rweb_tweet_is_translatable_enabled': True,
        'view_counts_everywhere_api_enabled': True,
        'longform_notetweets_consumption_enabled': True,
        'tweet_awards_web_tipping_enabled': False,
        'freedom_of_speech_not_reach_fetch_enabled': False,
        'standardized_nudges_misinfo': True,
        'tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled': False,
        'interactive_text_enabled': True, 'responsive_web_text_conversations_enabled': False,
        'longform_notetweets_rich_text_read_enabled': True,
        'responsive_web_enhance_cards_enabled': False,
        'responsive_web_twitter_blue_verified_badge_is_enabled': True,
        'longform_notetweets_richtext_consumption_enabled': True,
    }
