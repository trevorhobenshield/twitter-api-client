MAX_IMAGE_SIZE = 5_242_880  # ~5 MB
MAX_GIF_SIZE = 15_728_640  # ~15 MB
MAX_VIDEO_SIZE = 536_870_912  # ~530 MB
CHUNK_SIZE = 8192

BOLD = '\u001b[1m'
SUCCESS = '\u001b[32m'
WARN = '\u001b[31m'
RESET = '\u001b[0m'

content_settings = {
    'include_mention_filter': True,
    'include_nsfw_user_flag': True,
    'include_nsfw_admin_flag': True,
    'include_ranked_timeline': True,
    'include_alt_text_compose': True,
    'display_sensitive_media': True,
    'protected': False,
    'discoverable_by_email': False,
    'discoverable_by_mobile_phone': False,
    'allow_dms_from': 'following',  ## {'all'}
    'dm_quality_filter': 'enabled',  ## {'disabled'}
    'dm_receipt_setting': 'all_disabled',  ## {'all_enabled'}
    'allow_media_tagging': 'none',  ## {'all', 'following'}
    'nsfw_user': False,
    'geo_enabled': False,  ## add location information to your tweets
    'allow_ads_personalization': False,
    'allow_logged_out_device_personalization': False,
    'allow_sharing_data_for_third_party_personalization': False,
    'allow_location_history_personalization': False,
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
