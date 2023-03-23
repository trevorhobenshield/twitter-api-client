from enum import Enum  # todo:add back in python 3.13 , member

BOLD = '\u001b[1m'
SUCCESS = '\u001b[32m'
WARN = '\u001b[31m'
RESET = '\u001b[0m'

UPLOAD_CHUNK_SIZE = 4 * 1024 * 1024
MEDIA_UPLOAD_SUCCEED = 'succeeded'
MEDIA_UPLOAD_FAIL = 'failed'


class Value:
    __slots__ = 'value'

    def __init__(self, value: any = None):
        self.value = value


class CustomEnum(Enum):
    def __getattr__(self, item):
        if item != "_value_":
            attr = getattr(self.value, item)
            return attr.name, attr.value.value
        raise AttributeError


class Media(CustomEnum):
    #@member
    class Type(Enum):
        image = Value(5_242_880)  # ~5 MB
        gif = Value(15_728_640)  # ~15 MB
        video = Value(536_870_912)  # ~530 MB


class Operation(CustomEnum):
    #@member
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

    #@member
    class Account(Enum):
        # tweet
        CreateTweet = Value()
        CreateScheduledTweet = Value()
        DeleteScheduledTweet = Value()
        FetchScheduledTweets = Value()
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
