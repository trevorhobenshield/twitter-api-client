from enum import Enum, member


class Value:
    def __init__(self, value: any = None):
        self.value = value


class Operation(Enum):
    """
    Enum with repeated values for GraphQL operations
    """

    def __getattr__(self, item):
        if item != "_value_":
            attr = getattr(self.value, item)
            return attr.name, attr.value.value
        raise AttributeError

    @member
    class Data(Enum):
        # tweet
        Favoriters = Value('tweetId')
        Retweeters = Value('tweetId')
        TweetDetail = Value('focalTweetId')
        TweetResultByRestId = Value('tweetId')
        # user
        UserTweets = Value('userId')
        UserTweetsAndReplies = Value('userId')
        Likes = Value('userId')
        UserMedia = Value('userId')
        Followers = Value('userId')
        Following = Value('userId')
        UserByScreenName = Value('screen_name')
        UserByRestId = Value('userId')
        # batch-user
        UsersByRestIds = Value('userIds')

    @member
    class Account(Enum):
        # tweet
        CreateTweet = Value()
        CreateScheduledTweet = Value()
        DeleteTweet = Value()
        FavoriteTweet = Value()
        UnfavoriteTweet = Value()
        CreateRetweet = Value()
        DeleteRetweet = Value()
        # bookmark
        CreateBookmark = Value()
        DeleteBookmark = Value()
        BookmarksAllDelete = Value()
        # topic
        TopicFollow = Value()
        TopicUnfollow = Value()
        # list
        ListsManagementPageTimeline = Value()
        CreateList = Value()
        DeleteList = Value()
        EditListBanner = Value()
        DeleteListBanner = Value()
        ListAddMember = Value()
        ListRemoveMember = Value()
        ListsPinMany = Value()
        ListPinOne = Value()
        ListUnpinOne = Value()
        UpdateList = Value()
        # DM
        useSendMessageMutation = Value()
        # other
        TweetStats = Value()
