from dataclasses import dataclass

MAX_IMAGE_SIZE = 5_242_880  # ~5 MB
MAX_GIF_SIZE = 15_728_640  # ~15 MB
MAX_VIDEO_SIZE = 536_870_912  # ~530 MB

UPLOAD_CHUNK_SIZE = 4 * 1024 * 1024
MEDIA_UPLOAD_SUCCEED = 'succeeded'
MEDIA_UPLOAD_FAIL = 'failed'

BLACK = '\x1b[30m'
RED = '\x1b[31m'
GREEN = '\x1b[32m'
YELLOW = '\x1b[33m'
BLUE = '\x1b[34m'
MAGENTA = '\x1b[35m'
CYAN = '\x1b[36m'
WHITE = '\x1b[37m'
BOLD = '\x1b[1m'
RESET = '\x1b[0m'

log_config = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(asctime)s.%(msecs)03d %(levelname)s: %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": "debug.log",
            "encoding": "utf8",
            "mode": "a"
        }
    },
    "loggers": {
        "myLogger": {
            "level": "DEBUG",
            "handlers": [
                "console"
            ],
            "propagate": "no"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "console",
            "file"
        ]
    }
}


@dataclass
class Operation:
    # Scraper Operations
    ProfileSpotlightsQuery = '9zwVLJ48lmVUk8u_Gh9DmA', 'ProfileSpotlightsQuery', 'screen_name'
    UserByScreenName = 'sLVLhk0bGj3MVFEKTdax1w', 'UserByScreenName', 'screen_name'
    UserByRestId = 'GazOglcBvgLigl3ywt6b3Q', 'UserByRestId', 'userId'
    UsersByRestIds = 'OJBgJQIrij6e3cjqQ3Zu1Q', 'UsersByRestIds', 'userIds'
    UserTweets = 'HuTx74BxAnezK1gWvYY7zg', 'UserTweets', 'userId'
    UserMedia = 'YqiE3JL1KNgf9nSljYdxaA', 'UserMedia', 'userId'
    UserTweetsAndReplies = 'RIWc55YCNyUJ-U3HHGYkdg', 'UserTweetsAndReplies', 'userId'
    TweetResultByRestId = 'D_jNhjWZeRZT5NURzfJZSQ', 'TweetResultByRestId', 'tweetId'
    TweetDetail = 'zXaXQgfyR4GxE21uwYQSyA', 'TweetDetail', 'focalTweetId'
    TweetStats = 'EvbTkPDT-xQCfupPu0rWMA', 'TweetStats', 'rest_id'

    # auth required
    Likes = 'nYrjBgnUWQFt_tRyCGatZA', 'Likes', 'userId'
    Followers = 'pd8Tt1qUz1YWrICegqZ8cw', 'Followers', 'userId'
    Following = 'wjvx62Hye2dGVvnvVco0xA', 'Following', 'userId'
    Retweeters = '0BoJlKAxoNPQUHRftlwZ2w', 'Retweeters', 'tweetId'
    Favoriters = 'XRRjv1-uj1HZn3o324etOQ', 'Favoriters', 'tweetId'
    ConnectTabTimeline = 'lq02A-gEzbLefqTgD_PFzQ', 'ConnectTabTimeline', 'context'

    # Account Operations
    useSendMessageMutation = 'MaxK2PKX1F9Z-9SwqwavTw', 'useSendMessageMutation'
    CreateTweet = '7TKRKCPuAGsmYde0CudbVg', 'CreateTweet'
    DeleteTweet = 'VaenaVgh5q5ih7kvyVjgtg', 'DeleteTweet'
    CreateScheduledTweet = 'LCVzRQGxOaGnOnYH01NQXg', 'CreateScheduledTweet'
    DeleteScheduledTweet = 'CTOVqej0JBXAZSwkp1US0g', 'DeleteScheduledTweet'
    CreateRetweet = 'ojPdsZsimiJrUGLR1sjUtA', 'CreateRetweet'
    DeleteRetweet = 'iQtK4dl5hBmXewYZuEOKVw', 'DeleteRetweet'
    FavoriteTweet = 'lI07N6Otwv1PhnEgXILM7A', 'FavoriteTweet'
    UnfavoriteTweet = 'ZYKSe-w7KEslx3JhSIk5LA', 'UnfavoriteTweet'
    CreateBookmark = 'aoDbu3RHznuiSkQ9aNM67Q', 'CreateBookmark'
    DeleteBookmark = 'Wlmlj2-xzyS1GN3a6cj-mQ', 'DeleteBookmark'
    CreateList = 'hQAsnViq2BrMLbPuQ9umDA', 'CreateList'
    UpdateList = '4dCEFWtxEbhnSLcJdJ6PNg', 'UpdateList'
    ListsPinMany = '2X4Vqu6XLneR-XZnGK5MAw', 'ListsPinMany'
    ListPinOne = '2pYlo-kjdXoNOZJoLzI6KA', 'ListPinOne'
    ListUnpinOne = 'c4ce-hzx6V4heV5IzdeBkA', 'ListUnpinOne'
    ListAddMember = 'P8tyfv2_0HzofrB5f6_ugw', 'ListAddMember'
    ListRemoveMember = 'DBZowzFN492FFkBPBptCwg', 'ListRemoveMember'
    DeleteList = 'UnN9Th1BDbeLjpgjGSpL3Q', 'DeleteList'
    EditListBanner = 'Uk0ZwKSMYng56aQdeJD1yw', 'EditListBanner'
    DeleteListBanner = '-bOKetDVCMl20qXn7YDXIA', 'DeleteListBanner'
    TopicFollow = 'ElqSLWFmsPL4NlZI5e1Grg', 'TopicFollow'
    TopicUnfollow = 'srwjU6JM_ZKTj_QMfUGNcw', 'TopicUnfollow'
    HomeLatestTimeline = 'zhX91JE87mWvfprhYE97xA', 'HomeLatestTimeline'
    HomeTimeline = 'HCosKfLNW1AcOo3la3mMgg', 'HomeTimeline'
    Bookmarks = 'tmd4ifV8RHltzn8ymGg1aw', 'Bookmarks'

    # misc/not implemented
    AdAccounts = 'a8KxGfFQAmm3WxqemuqSRA', 'AdAccounts'
    ArticleTimeline = 'o9FyvnC-xg8mVBXqL4g-rg', 'ArticleTimeline'
    ArticleTweetsTimeline = 'x4ywSpvg6BesoDszkfbFQg', 'ArticleTweetsTimeline'
    AudienceEstimate = '1LYVUabJBYkPlUAWRabB3g', 'AudienceEstimate'
    AudioSpaceById = 'QB5okPsUwVP3TefHBFItnw', 'AudioSpaceById'
    AudioSpaceSearch = 'NTq79TuSz6fHj8lQaferJw', 'AudioSpaceSearch'
    AuthenticatedUserTFLists = 'QjN8ZdavFDqxUjNn3r9cig', 'AuthenticatedUserTFLists'
    BirdwatchAliasSelect = '3ss48WFwGokBH_gj8t_8aQ', 'BirdwatchAliasSelect'
    BirdwatchCreateAppeal = 'TKdL0YFsX4DMOpMKeneLvA', 'BirdwatchCreateAppeal'
    BirdwatchCreateNote = '36EUZZyaciVmNrq4CRZcmw', 'BirdwatchCreateNote'
    BirdwatchCreateRating = 'bD3AEK9BMCSpRods_ng2fA', 'BirdwatchCreateRating'
    BirdwatchDeleteNote = 'IKS_qrShkDyor6Ri1ahd9g', 'BirdwatchDeleteNote'
    BirdwatchDeleteRating = 'OpvCOyOoQClUND66zDzrnA', 'BirdwatchDeleteRating'
    BirdwatchEditNotificationSettings = 'FLgLReVIssXjB_ui3wcrRQ', 'BirdwatchEditNotificationSettings'
    BirdwatchFetchAliasSelfSelectOptions = 'szoXMke8AZOErso908iglw', 'BirdwatchFetchAliasSelfSelectOptions'
    BirdwatchFetchAliasSelfSelectStatus = 'LUEdtkcpBlGktUtms4BvwA', 'BirdwatchFetchAliasSelfSelectStatus'
    BirdwatchFetchAuthenticatedUserProfile = 'pMbW6Y4LuS5MzlSOEqERJQ', 'BirdwatchFetchAuthenticatedUserProfile'
    BirdwatchFetchBirdwatchProfile = 'btgGtchypc3D491MJ7XXWA', 'BirdwatchFetchBirdwatchProfile'
    BirdwatchFetchContributorNotesSlice = 't6r3Wq7wripUW9gB3FQNBw', 'BirdwatchFetchContributorNotesSlice'
    BirdwatchFetchGlobalTimeline = 'L3LftPt6fhYqoQ5Vnxm7UQ', 'BirdwatchFetchGlobalTimeline'
    BirdwatchFetchNotes = 'ZGMhf1M7kPKMOhEk1nz0Yw', 'BirdwatchFetchNotes'
    BirdwatchFetchOneNote = 'GO8BR2MM2WZB63cdOoC7lw', 'BirdwatchFetchOneNote'
    BirdwatchFetchPublicData = '9bDdJ6AL26RLkcUShEcF-A', 'BirdwatchFetchPublicData'
    BirdwatchProfileAcknowledgeEarnOut = 'cED9wJy8Nd1kZCCYuIq9zQ', 'BirdwatchProfileAcknowledgeEarnOut'
    BizProfileFetchUser = '6OFpJ3TH3p8JpwOSgfgyhg', 'BizProfileFetchUser'
    BlockedAccountsAll = 'h52d1F7dumWGE1tJAhQBpg', 'BlockedAccountsAll'
    BlockedAccountsAutoBlock = '8w-D2OhT0jmGzXaNY--UQA', 'BlockedAccountsAutoBlock'
    BlockedAccountsImported = '8LDNeOEm0kA98uoDsqXvMg', 'BlockedAccountsImported'
    BookmarkFolderTimeline = '13H7EUATwethsj-XxX5ohw', 'BookmarkFolderTimeline'
    BookmarkFoldersSlice = 'i78YDd0Tza-dV4SYs58kRg', 'BookmarkFoldersSlice'
    BookmarksAllDelete = 'skiACZKC1GDYli-M8RzEPQ', 'BookmarksAllDelete'
    Budgets = 'mbK3oSQotwcJXyQIBE3uYw', 'Budgets'
    CardPreviewByTweetText = 'jnwTSDR-Eo_HWlSkXPcMGA', 'CardPreviewByTweetText'
    CheckTweetForNudge = 'C2dcvh7H69JALtomErxWlA', 'CheckTweetForNudge'
    CombinedLists = 'rIxum3avpCu7APi7mxTNjw', 'CombinedLists'
    CommunitiesMainDiscoveryModule = '8UB2fhB8TiYIW2M6vbBFXg', 'CommunitiesMainDiscoveryModule'
    CommunitiesMainPageTimeline = 'DzcxPzkGYVQk-BD0pqAcZw', 'CommunitiesMainPageTimeline'
    CommunitiesMembershipsSlice = 's8-oxdVsoJ3w2CFD0nFt9g', 'CommunitiesMembershipsSlice'
    CommunitiesMembershipsTimeline = 'QXo-eKTsvhpCyFotNz2u6g', 'CommunitiesMembershipsTimeline'
    CommunityAboutTimeline = 'plOgdpBzpVVQbTOEVuRc_A', 'CommunityAboutTimeline'
    CommunityByRestId = 'bCVwRBDPi15jrdJQ7NCENQ', 'CommunityByRestId'
    CommunityCreateRule = 'dShPoN6voXRusgxC1uvGog', 'CommunityCreateRule'
    CommunityDiscoveryTimeline = 'b3rceNUXWRyo5mSwVZF74Q', 'CommunityDiscoveryTimeline'
    CommunityEditBannerMedia = 'KVkZwp8Q6xy6iyhlQE5d7Q', 'CommunityEditBannerMedia'
    CommunityEditName = 'SKToKhvm3Z4Rir8ENCJ3YQ', 'CommunityEditName'
    CommunityEditPurpose = 'eMat-u2kx6KocreGTAt-hA', 'CommunityEditPurpose'
    CommunityEditRule = '9nEl5bNcdteuPGbGCdvEFA', 'CommunityEditRule'
    CommunityEditTheme = '4OhW6gWJwiu-JTAgBPsU1w', 'CommunityEditTheme'
    CommunityHashtagsTimeline = 'hril1TsnshopHbmnjdUmhQ', 'CommunityHashtagsTimeline'
    CommunityMemberRelationshipTypeahead = 'NEwac2-8ONgf0756ne8oXA', 'CommunityMemberRelationshipTypeahead'
    CommunityModerationKeepTweet = 'f_YqrHSCc1mPlG-aB7pFRw', 'CommunityModerationKeepTweet'
    CommunityModerationTweetCasesSlice = 'V-iC7tjWOlzBJ44SanqGzw', 'CommunityModerationTweetCasesSlice'
    CommunityRemoveBannerMedia = 'lSdK1v30qVhm37rDTgHq0Q', 'CommunityRemoveBannerMedia'
    CommunityRemoveRule = 'EI_g43Ss_Ixg0EC4K7nzlQ', 'CommunityRemoveRule'
    CommunityReorderRules = 'VwluNMGnl5uaNZ3LnlCQ_A', 'CommunityReorderRules'
    CommunityTweetsRankedTimeline = 'P38EspBBPhAfSKPP74-s2Q', 'CommunityTweetsRankedTimeline'
    CommunityTweetsTimeline = '2JgHOlqfeLusxAT0yGQJjg', 'CommunityTweetsTimeline'
    CommunityUpdateRole = '5eq76kkUqfdCzInCtcxQOA', 'CommunityUpdateRole'
    CommunityUserInvite = 'x8hUNaBCOV2tSalqB9cwWQ', 'CommunityUserInvite'
    CommunityUserRelationshipTypeahead = 'gi_UGcUurYp6N6p2BaLJqQ', 'CommunityUserRelationshipTypeahead'
    ConversationControlChange = 'hb1elGcj6769uT8qVYqtjw', 'ConversationControlChange'
    ConversationControlDelete = 'OoMO_aSZ1ZXjegeamF9QmA', 'ConversationControlDelete'
    ConvertRitoSuggestedActions = '2njnYoE69O2jdUM7KMEnDw', 'ConvertRitoSuggestedActions'
    Coupons = 'R1h43jnAl2bsDoUkgZb7NQ', 'Coupons'
    CreateCommunity = 'lRjZKTRcWuqwtYwCWGy9_w', 'CreateCommunity'
    CreateCustomerPortalSession = '2LHXrd1uYeaMWhciZgPZFw', 'CreateCustomerPortalSession'
    CreateDraftTweet = 'cH9HZWz_EW9gnswvA4ZRiQ', 'CreateDraftTweet'
    CreateNoteTweet = 'Pyx6nga4XtTVhfTh1gtX1A', 'CreateNoteTweet'
    CreateQuickPromotion = 'oDSoVgHhJxnd5IkckgPZdg', 'CreateQuickPromotion'
    CreateTrustedFriendsList = '2tP8XUYeLHKjq5RHvuvpZw', 'CreateTrustedFriendsList'
    CreateTweetDownvote = 'Eo65jl-gww30avDgrXvhUA', 'CreateTweetDownvote'
    CreateTweetReaction = 'D7M6X3h4-mJE8UB1Ap3_dQ', 'CreateTweetReaction'
    DataSaverMode = 'xF6sXnKJfS2AOylzxRjf6A', 'DataSaverMode'
    DeleteBookmarkFolder = '2UTTsO-6zs93XqlEUZPsSg', 'DeleteBookmarkFolder'
    DeleteDraftTweet = 'bkh9G3FGgTldS9iTKWWYYw', 'DeleteDraftTweet'
    DeletePaymentMethod = 'VaaLGwK5KNLoc7wsOmp4uw', 'DeletePaymentMethod'
    DeleteTweetDownvote = 'VNEvEGXaUAMfiExP8Tbezw', 'DeleteTweetDownvote'
    DeleteTweetReaction = 'GKwK0Rj4EdkfwdHQMZTpuw', 'DeleteTweetReaction'
    DisableUserAccountLabel = '_ckHEj05gan2VfNHG6thBA', 'DisableUserAccountLabel'
    DisableVerifiedPhoneLabel = 'g2m0pAOamawNtVIfjXNMJg', 'DisableVerifiedPhoneLabel'
    DismissRitoSuggestedAction = 'jYvwa61cv3NwNP24iUru6g', 'DismissRitoSuggestedAction'
    DmAllSearchSlice = '9qd2xqJkMURKSyXVJ33xBw', 'DmAllSearchSlice'
    DmGroupSearchSlice = '5zpY1dCR-8NyxQJS_CFJoQ', 'DmGroupSearchSlice'
    DmMutedTimeline = 'lrcWa13oyrQc7L33wRdLAQ', 'DmMutedTimeline'
    DmNsfwMediaFilterUpdate = 'of_N6O33zfyD4qsFJMYFxA', 'DmNsfwMediaFilterUpdate'
    DmPeopleSearchSlice = 'xYSm8m5kJnzm_gFCn5GH-w', 'DmPeopleSearchSlice'
    EditBookmarkFolder = 'a6kPp1cS1Dgbsjhapz1PNw', 'EditBookmarkFolder'
    EditDraftTweet = 'JIeXE-I6BZXHfxsgOkyHYQ', 'EditDraftTweet'
    EditScheduledTweet = '_mHkQ5LHpRRjSXKOcG6eZw', 'EditScheduledTweet'
    EnableLoggedOutWebNotifications = 'BqIHKmwZKtiUBPi07jKctg', 'EnableLoggedOutWebNotifications'
    EnableVerifiedPhoneLabel = 'C3RJFfMsb_KcEytpKmRRkw', 'EnableVerifiedPhoneLabel'
    EnrollCoupon = 'SOyGmNGaEXcvk15s5bqDrA', 'EnrollCoupon'
    ExplorePage = 'fkypGKlR9Xz9kLvUZDLoXw', 'ExplorePage'
    FeatureSettingsUpdate = '-btar_vkBwWA7s3YWfp_9g', 'FeatureSettingsUpdate'
    FetchDraftTweets = 'ZkqIq_xRhiUme0PBJNpRtg', 'FetchDraftTweets'
    FetchScheduledTweets = 'ITtjAzvlZni2wWXwf295Qg', 'FetchScheduledTweets'
    FollowersYouKnow = 'RvojYJJB90VwJ0rdVhbjMQ', 'FollowersYouKnow'
    ForYouExplore = 'wVEXnyTWzQlEsIuLq_D3tw', 'ForYouExplore'
    GenericTimelineById = 'LZfAdxTdNolKXw6ZkoY_kA', 'GenericTimelineById'
    GetSafetyModeSettings = 'AhxTX0lkbIos4WG53xwzSA', 'GetSafetyModeSettings'
    GetTweetReactionTimeline = 'ihIcULrtrtPGlCuprduRrA', 'GetTweetReactionTimeline'
    GetUserClaims = 'lFi3xnx0auUUnyG4YwpCNw', 'GetUserClaims'
    GraphQLError = '2V2W3HIBuMW83vEMtfo_Rg', 'GraphQLError'
    ImmersiveMedia = 'UGQD_VslAJBJ4XzigsBYAA', 'ImmersiveMedia'
    JoinCommunity = 'PXO-mA1KfmLqB9I6R-lOng', 'JoinCommunity'
    LeaveCommunity = 'AtiTdhEyRN8ruNFW069ewQ', 'LeaveCommunity'
    ListByRestId = 'wXzyA5vM_aVkBL9G8Vp3kw', 'ListByRestId'
    ListBySlug = '3-E3eSWorCv24kYkK3CCiQ', 'ListBySlug'
    ListCreationRecommendedUsers = 'Zf8ZwG57EKtss-rPlryIqg', 'ListCreationRecommendedUsers'
    ListEditRecommendedUsers = '-F4wsOirYNXjjg-ZjccQpQ', 'ListEditRecommendedUsers'
    ListLatestTweetsTimeline = '2TemLyqrMpTeAmysdbnVqw', 'ListLatestTweetsTimeline'
    ListMembers = 'vA952kfgGw6hh8KatWnbqw', 'ListMembers'
    ListMemberships = 'BlEXXdARdSeL_0KyKHHvvg', 'ListMemberships'
    ListOwnerships = 'wQcOSjSQ8NtgxIwvYl1lMg', 'ListOwnerships'
    ListPins = 'J0JOhmi8HSsle8LfSWv0cw', 'ListPins'
    ListProductSubscriptions = 'wwdBYgScze0_Jnan79jEUw', 'ListProductSubscriptions'
    ListRankedTweetsTimeline = '07lytXX9oG9uCld1RY4b0w', 'ListRankedTweetsTimeline'
    ListSubscribe = 'FjvrQI3k-97JIUbEE6Gxcw', 'ListSubscribe'
    ListSubscribers = 'e57wIELAAe0fYt4Hmqsk6g', 'ListSubscribers'
    ListUnsubscribe = 'bXyvW9HoS_Omy4ADhexj8A', 'ListUnsubscribe'
    ListsDiscovery = 'ehnzbxPHA69pyaV2EydN1g', 'ListsDiscovery'
    ListsManagementPageTimeline = 'nhYp4n09Hi5n2hQWseQztg', 'ListsManagementPageTimeline'
    LiveCommerceItemsSlice = '-lnNX56S2YrZYrLzbccFAQ', 'LiveCommerceItemsSlice'
    ModerateTweet = 'pjFnHGVqCjTcZol0xcBJjw', 'ModerateTweet'
    ModeratedTimeline = 'hnaqw2Vok5OETdBVa_uexw', 'ModeratedTimeline'
    MuteList = 'ZYyanJsskNUcltu9bliMLA', 'MuteList'
    MutedAccounts = '-G9eXTmseyiSenbqjrEG6w', 'MutedAccounts'
    NoteworthyAccountsPage = '3fOJzEwYMnVyzwgLTLIBkw', 'NoteworthyAccountsPage'
    PaymentMethods = 'mPF_G9okpbZuLcD6mN8K9g', 'PaymentMethods'
    PinReply = 'GA2_1uKP9b_GyR4MVAQXAw', 'PinReply'
    ProfileUserPhoneState = '5kUWP8C1hcd6omvg6HXXTQ', 'ProfileUserPhoneState'
    PutClientEducationFlag = 'IjQ-egg0uPkY11NyPMfRMQ', 'PutClientEducationFlag'
    QuickPromoteEligibility = 'LtpCXh66W-uXh7u7XSRA8Q', 'QuickPromoteEligibility'
    RemoveFollower = 'QpNfg0kpPRfjROQ_9eOLXA', 'RemoveFollower'
    RemoveTweetFromBookmarkFolder = '2Qbj9XZvtUvyJB4gFwWfaA', 'RemoveTweetFromBookmarkFolder'
    RequestToJoinCommunity = '6G66cW5zuxPXmHOeBOjF2w', 'RequestToJoinCommunity'
    RitoActionedTweetsTimeline = 'px9Zbs48D-YdQPEROK6-nA', 'RitoActionedTweetsTimeline'
    RitoFlaggedAccountsTimeline = 'lMzaBZHIbD6GuPqJJQubMg', 'RitoFlaggedAccountsTimeline'
    RitoFlaggedTweetsTimeline = 'iCuXMibh6yj9AelyjKXDeA', 'RitoFlaggedTweetsTimeline'
    RitoSuggestedActionsFacePile = 'GnQKeEdL1LyeK3dTQCS1yw', 'RitoSuggestedActionsFacePile'
    SearchTimeline = 'gkjsKepM6gl_HmFWoWKfgg', 'SearchTimeline'
    SetDefault = 'QEMLEzEMzoPNbeauKCCLbg', 'SetDefault'
    SetSafetyModeSettings = 'qSJIPIpf4gA7Wn21bT3D4w', 'SetSafetyModeSettings'
    SharingAudiospacesListeningDataWithFollowersUpdate = '5h0kNbk3ii97rmfY6CdgAA', 'SharingAudiospacesListeningDataWithFollowersUpdate'
    SubscribeToScheduledSpace = 'Sxn4YOlaAwEKjnjWV0h7Mw', 'SubscribeToScheduledSpace'
    SubscriptionCheckoutUrlWithEligibility = 'hKfOOObQr5JmfmxW0YtPvg', 'SubscriptionCheckoutUrlWithEligibility'
    SubscriptionProductDetails = 'f0dExZDmFWFSWMCPQSAemQ', 'SubscriptionProductDetails'
    SubscriptionProductFeaturesFetch = 'Me2CVcAXxvK2WMr-Nh_Qqg', 'SubscriptionProductFeaturesFetch'
    SuperFollowers = 'o0YtPFnd4Lk_pOQb9alCvA', 'SuperFollowers'
    TopicByRestId = '4OUZZOonV2h60I0wdlQb_w', 'TopicByRestId'
    TopicLandingPage = 'mAKQjs1kyTS75VLZzuIXXw', 'TopicLandingPage'
    TopicNotInterested = 'cPCFdDAaqRjlMRYInZzoDA', 'TopicNotInterested'
    TopicToFollowSidebar = 'RPWVYYupHVZkJOnokbt2cw', 'TopicToFollowSidebar'
    TopicUndoNotInterested = '4tVnt6FoSxaX8L-mDDJo4Q', 'TopicUndoNotInterested'
    TopicsManagementPage = 'Jvdjpe8qzsJD84BpK3qdkQ', 'TopicsManagementPage'
    TopicsPickerPage = 'UvG-XXtWNcJN1LzF0u3ByA', 'TopicsPickerPage'
    TopicsPickerPageById = 't6kH4v2c_VzWKljc2yNwHA', 'TopicsPickerPageById'
    TrustedFriendsTypeahead = 'RRnOwHttRGscWKC1zY9VRA', 'TrustedFriendsTypeahead'
    TweetEditHistory = '8eaWKjHszkS-G_hprUd9AA', 'TweetEditHistory'
    TwitterArticleByRestId = 'hwrvh-Qt24lcprL-BDfqRA', 'TwitterArticleByRestId'
    TwitterArticleCreate = 'aV-sm-IkvwplcxdYDoLZHQ', 'TwitterArticleCreate'
    TwitterArticleDelete = '6st-stMDc7KBqLT8KvWhHg', 'TwitterArticleDelete'
    TwitterArticleUpdateCoverImage = 'fpcVRSAsjvkwmCiN1HheqQ', 'TwitterArticleUpdateCoverImage'
    TwitterArticleUpdateData = 'XpBTYp_QXwyZ0XT0JXCBJw', 'TwitterArticleUpdateData'
    TwitterArticleUpdateMedia = '3ojmmegfBC_oHyrmPhxj-g', 'TwitterArticleUpdateMedia'
    TwitterArticleUpdateTitle = 'dvH6Ql989I4e5jWEV7HfaQ', 'TwitterArticleUpdateTitle'
    TwitterArticleUpdateVisibility = '8M35gHyfpcy3S4UXejUGfA', 'TwitterArticleUpdateVisibility'
    TwitterArticlesSlice = 'UUPSi_aS8_kHDFTWqSBPUA', 'TwitterArticlesSlice'
    UnmentionUserFromConversation = 'xVW9j3OqoBRY9d6_2OONEg', 'UnmentionUserFromConversation'
    UnmoderateTweet = 'pVSyu6PA57TLvIE4nN2tsA', 'UnmoderateTweet'
    UnmuteList = 'pMZrHRNsmEkXgbn3tOyr7Q', 'UnmuteList'
    UnpinReply = 'iRe6ig5OV1EzOtldNIuGDQ', 'UnpinReply'
    UnsubscribeFromScheduledSpace = 'Zevhh76Msw574ZSs2NQHGQ', 'UnsubscribeFromScheduledSpace'
    UrtFixtures = 'I_0j1mjMwv94SdS66S4pqw', 'UrtFixtures'
    UserAboutTimeline = 'dm7ReTFJoeU0qkiZCO1E1g', 'UserAboutTimeline'
    UserAccountLabel = 'rD5gLxVmMvtdtYU1UHWlFQ', 'UserAccountLabel'
    UserBusinessProfileTeamTimeline = 'dq1eUCn3N8v0BywlP4nT7A', 'UserBusinessProfileTeamTimeline'
    UserPromotableTweets = 'jF-OgMv-9vAym3JaCPUnhQ', 'UserPromotableTweets'
    UserSessionsList = 'vJ-XatpmQSG8bDch8-t9Jw', 'UserSessionsList'
    UserSuperFollowTweets = '1by3q8-AJWdNYhtltjlPTQ', 'UserSuperFollowTweets'
    Viewer = 'okNaf-6AQWu2DD2H_MAoVw', 'Viewer'
    ViewerEmailSettings = 'JpjlNgn4sLGvS6tgpTzYBg', 'ViewerEmailSettings'
    ViewerTeams = 'D8mVcJSVv66_3NcR7fOf6g', 'ViewerTeams'
    ViewingOtherUsersTopicsPage = 'tYXo6h_rpnHXbdLUFMatZA', 'ViewingOtherUsersTopicsPage'
    WriteDataSaverPreferences = 'H03etWvZGz41YASxAU2YPg', 'WriteDataSaverPreferences'
    WriteEmailNotificationSettings = '2qKKYFQift8p5-J1k6kqxQ', 'WriteEmailNotificationSettings'
    adFreeArticleDomains = 'zwTrX9CtnMvWlBXjsx95RQ', 'adFreeArticleDomains'
    articleNudgeDomains = '88Bu08U2ddaVVjKmmXjVYg', 'articleNudgeDomains'
    bookmarkTweetToFolder = '4KHZvvNbHNf07bsgnL9gWA', 'bookmarkTweetToFolder'
    createBookmarkFolder = '6Xxqpq8TM_CREYiuof_h5w', 'createBookmarkFolder'
    getAltTextPromptPreference = 'PFIxTk8owMoZgiMccP0r4g', 'getAltTextPromptPreference'
    getCaptionsAlwaysDisplayPreference = 'BwgMOGpOViDS0ri7VUgglg', 'getCaptionsAlwaysDisplayPreference'
    timelinesFeedback = 'vfVbgvTPTQ-dF_PQ5lD1WQ', 'timelinesFeedback'
    updateAltTextPromptPreference = 'aQKrduk_DA46XfOQDkcEng', 'updateAltTextPromptPreference'
    updateCaptionsAlwaysDisplayPreference = 'uCUQhvZ5sJ9qHinRp6CFlQ', 'updateCaptionsAlwaysDisplayPreference'

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
        'profile_foundations_tweet_stats_enabled': True,
        'profile_foundations_tweet_stats_tweet_frequency': True,
        'graphql_timeline_v2_bookmark_timeline': True,
    }


trending_params = {
    "include_profile_interstitial_type": "1",
    "include_blocking": "1",
    "include_blocked_by": "1",
    "include_followed_by": "1",
    "include_want_retweets": "1",
    "include_mute_edge": "1",
    "include_can_dm": "1",
    "include_can_media_tag": "1",
    "include_ext_has_nft_avatar": "1",
    "include_ext_is_blue_verified": "1",
    "include_ext_verified_type": "1",
    "skip_status": "1",
    "cards_platform": "Web-12",
    "include_cards": "1",
    "include_ext_alt_text": "true",
    "include_ext_limited_action_results": "false",
    "include_quote_count": "true",
    "include_reply_count": "1",
    "tweet_mode": "extended",
    "include_ext_views": "true",
    "include_entities": "true",
    "include_user_entities": "true",
    "include_ext_media_color": "true",
    "include_ext_media_availability": "true",
    "include_ext_sensitive_media_warning": "true",
    "include_ext_trusted_friends_metadata": "true",
    "send_error_codes": "true",
    "simple_quoted_tweet": "true",
    "count": 1000,
    "requestContext": "launch",
    "include_page_configuration": "true",
    "initial_tab_id": "trending",
    "entity_tokens": "false",
    "ext": "mediaStats,highlightedLabel,hasNftAvatar,voiceInfo,birdwatchPivot,enrichments,superFollowMetadata,unmentionInfo,editControl,vibe"
}

account_settings = {
    "address_book_live_sync_enabled": False,
    "allow_ads_personalization": False,
    "allow_authenticated_periscope_requests": True,
    "allow_dm_groups_from": "following",
    "allow_dms_from": "following",  # all
    "allow_location_history_personalization": False,
    "allow_logged_out_device_personalization": False,
    "allow_media_tagging": "none",  # all, following
    "allow_sharing_data_for_third_party_personalization": False,
    "alt_text_compose_enabled": None,
    "always_use_https": True,
    "autoplay_disabled": False,
    "country_code": "us",
    "discoverable_by_email": False,
    "discoverable_by_mobile_phone": False,
    "display_sensitive_media": True,
    "dm_quality_filter": "enabled",  # disabled
    "dm_receipt_setting": "all_disabled",  # all_enabled
    "geo_enabled": False,
    "include_alt_text_compose": True,
    "include_mention_filter": True,
    "include_nsfw_admin_flag": True,
    "include_nsfw_user_flag": True,
    "include_ranked_timeline": True,
    "language": "en",
    "mention_filter": "unfiltered",
    "nsfw_admin": False,
    "nsfw_user": False,
    "personalized_trends": True,
    "protected": False,
    "ranked_timeline_eligible": None,
    "ranked_timeline_setting": None,
    "require_password_login": False,
    "requires_login_verification": False,
    "settings_metadata": {},
    "sleep_time": {
        "enabled": False,
        "end_time": None,
        "start_time": None
    },
    "translator_type": "none",
    "universal_quality_filtering_enabled": "enabled",
    "use_cookie_personalization": False,
    ## todo: not yet implemented - requires additional steps
    # "allow_contributor_request": "all",
    # "protect_password_reset": False,
}
notification_settings = {
    "cursor": "-1",
    "include_profile_interstitial_type": "1",
    "include_blocking": "1",
    "include_blocked_by": "1",
    "include_followed_by": "1",
    "include_want_retweets": "1",
    "include_mute_edge": "1",
    "include_can_dm": "1",
    "include_can_media_tag": "1",
    "include_ext_has_nft_avatar": "1",
    "include_ext_is_blue_verified": "1",
    "include_ext_verified_type": "1",
    "skip_status": "1",
}

follow_settings = {
    "include_profile_interstitial_type": "1",
    "include_blocking": "1",
    "include_blocked_by": "1",
    "include_followed_by": "1",
    "include_want_retweets": "1",
    "include_mute_edge": "1",
    "include_can_dm": "1",
    "include_can_media_tag": "1",
    "include_ext_has_nft_avatar": "1",
    "include_ext_is_blue_verified": "1",
    "include_ext_verified_type": "1",
    "skip_status": "1",
}

account_search_settings = {
    "optInFiltering": True,  # filter out nsfw content
    "optInBlocking": True,  # filter out blocked accounts
}

profile_settings = {
    "birthdate_day": int,
    "birthdate_month": int,
    "birthdate_year": int,  # 1985
    "birthdate_visibility": str,  # "self",
    "birthdate_year_visibility": str,  # "self",
    "displayNameMaxLength": int,  # "50",
    "url": str,  # "https://example.com",
    "name": str,  # "foo",
    "description": str,  # "bar",
    "location": str,  # "world",
}

search_config = {
    "include_profile_interstitial_type": 1,
    "include_blocking": 1,
    "include_blocked_by": 1,
    "include_followed_by": 1,
    "include_want_retweets": 1,
    "include_mute_edge": 1,
    "include_can_dm": 1,
    "include_can_media_tag": 1,
    "include_ext_has_nft_avatar": 1,
    "include_ext_is_blue_verified": 1,
    "include_ext_verified_type": 1,
    "skip_status": 1,
    "cards_platform": "Web-12",
    "include_cards": 1,
    "include_ext_alt_text": "true",
    "include_ext_limited_action_results": "false",
    "include_quote_count": "true",
    "include_reply_count": 1,
    "tweet_mode": "extended",
    "include_ext_collab_control": "true",
    "include_ext_views": "true",
    "include_entities": "true",
    "include_user_entities": "true",
    "include_ext_media_color": "true",
    "include_ext_media_availability": "true",
    "include_ext_sensitive_media_warning": "true",
    "include_ext_trusted_friends_metadata": "true",
    "send_error_codes": "true",
    "simple_quoted_tweet": "true",
    "query_source": "typed_query",
    "count": 1000,
    "q": "",
    "requestContext": "launch",
    "pc": 1,
    "spelling_corrections": 1,
    "include_ext_edit_control": "true",
    "ext": "mediaStats,highlightedLabel,hasNftAvatar,voiceInfo,birdwatchPivot,enrichments,superFollowMetadata,unmentionInfo,editControl,collab_control,vibe"
}
