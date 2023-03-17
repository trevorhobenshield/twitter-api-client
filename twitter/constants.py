from enum import Enum, auto, member


class Operation(Enum):
    def __getattr__(self, item):
        if item != '_value_':
            return getattr(self.value, item).name
        raise AttributeError

    @member
    class Account(Enum):
        # tweet
        CreateTweet = auto()
        CreateScheduledTweet = auto()
        DeleteTweet = auto()
        FavoriteTweet = auto()
        UnfavoriteTweet = auto()
        CreateRetweet = auto()
        DeleteRetweet = auto()
        # bookmark
        CreateBookmark = auto()
        DeleteBookmark = auto()
        BookmarksAllDelete = auto()
        # topic
        TopicFollow = auto()
        TopicUnfollow = auto()
        # list
        ListsManagementPageTimeline = auto()
        CreateList = auto()
        DeleteList = auto()
        EditListBanner = auto()
        DeleteListBanner = auto()
        ListAddMember = auto()
        ListRemoveMember = auto()
        ListsPinMany = auto()
        ListPinOne = auto()
        ListUnpinOne = auto()
        UpdateList = auto()
        # DM
        useSendMessageMutation = auto()
        # other
        TweetStats = auto()

    @member
    class Data(Enum):
        # tweet operations
        TweetDetail = auto()
        TweetResultByRestId = auto()
        Favoriters = auto()
        Retweeters = auto()

        # user operations
        Following = auto()
        UserTweets = auto()
        Followers = auto()
        UserTweetsAndReplies = auto()
        UserMedia = auto()
        Likes = auto()
        UserByScreenName = auto()
        UserByRestId = auto()

        # batch user operations
        UsersByRestIds = auto()
