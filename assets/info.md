
### Example Response (all resources)

`https://api.twitter.com/1.1/application/rate_limit_status.json`

Reference: https://developer.twitter.com/en/docs/twitter-api/v1/developer-utilities/rate-limit-status/api-reference/get-application-rate_limit_status

```python
resources = {
    'rate_limit_context': {
        'access_token': '786491-24zE39NUezJ8UTmOGOtLhgyLgCkPyY4dAcx6NA6sDKw',  # example token
    },
    'resources': {
        'profile_spotlight': {
            '/profile_spotlight/show': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'explore': {
            '/explore/tiles': {
                'limit': 30,
                'remaining': 30,
                'reset': 1678731831
            }
        },
        'lists': {
            '/lists/list': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/lists/:id/tweets&GET': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/lists/:id/followers&GET': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/lists/memberships': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/lists/:id&DELETE': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/lists/subscriptions': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/lists/members': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/lists/:id&GET': {
                'limit': 75,
                'remaining': 75,
                'reset': 1678731831
            },
            '/lists/subscribers/show': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/lists/:id&PUT': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/lists/show': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/lists/ownerships': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/lists/:id/members/:user_id&DELETE': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/lists/subscribers': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/lists/:id/members&POST': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/lists/:id/members&GET': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/lists/members/show': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/lists/statuses': {
                'limit': 1800,
                'remaining': 1800,
                'reset': 1678731831
            }
        },
        'application': {
            '/application/rate_limit_status': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'mutes': {
            '/mutes/keywords/create': {
                'limit': 30,
                'remaining': 30,
                'reset': 1678731831
            },
            '/mutes/advanced_filters': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            },
            '/mutes/keywords/destroy': {
                'limit': 30,
                'remaining': 30,
                'reset': 1678731831
            },
            '/mutes/keywords/discouraged': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/mutes/users/list': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/mutes/users/ids': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/mutes/keywords/list': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'business_profiles': {
            '/business_profiles/show': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/business_profiles/update': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'verify': {
            '/verify/:version/badge-violation': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/verify/:version/badge-violation/violations': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/verify/:version/intake': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/verify/:version/document-formats': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/verify/:version/id-document&GET': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            },
            '/verify/:version/id-document&POST': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/verify/:version/access': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/verify/:version/account-eligibility': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            }
        },
        'follow_search': {
            '/follow_search/show': {
                'limit': 60,
                'remaining': 60,
                'reset': 1678731831
            }
        },
        'keyregistry': {
            '/keyregistry/register&POST': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            },
            '/keyregistry/delete&DELETE': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/keyregistry/extract_prekey_bundle/:user_id&POST': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            },
            '/keyregistry/publish&POST': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            }
        },
        'tweetdeck': {
            '/tweetdeck/clients/blackbird': {
                'limit': 150,
                'remaining': 150,
                'reset': 1678731831
            },
            '/tweetdeck/columns': {
                'limit': 150,
                'remaining': 150,
                'reset': 1678731831
            },
            '/tweetdeck/clients/pro': {
                'limit': 150,
                'remaining': 150,
                'reset': 1678731831
            },
            '/tweetdeck/dataminr/authtoken': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/tweetdeck/clients': {
                'limit': 150,
                'remaining': 150,
                'reset': 1678731831
            },
            '/tweetdeck/clients/blackbird/all': {
                'limit': 150,
                'remaining': 150,
                'reset': 1678731831
            },
            '/tweetdeck/clients/pro/all': {
                'limit': 150,
                'remaining': 150,
                'reset': 1678731831
            },
            '/tweetdeck/feeds': {
                'limit': 150,
                'remaining': 150,
                'reset': 1678731831
            }
        },
        'admin_users': {
            '/admin_users': {
                'limit': 2000,
                'remaining': 2000,
                'reset': 1678731831
            }
        },
        'people_discovery': {
            '/people_discovery/module': {
                'limit': 30,
                'remaining': 30,
                'reset': 1678731831
            },
            '/people_discovery/modules': {
                'limit': 75,
                'remaining': 75,
                'reset': 1678731831
            }
        },
        'conversation': {
            '/conversation/unhide': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/conversation/show/:id': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/conversation/hide': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            }
        },
        'live_video_stream': {
            '/live_video_stream/status/:id': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            }
        },
        'users_derived.info': {
            '/users_derived.info': {
                'limit': 1,
                'remaining': 1,
                'reset': 1678731831
            }
        },
        'translations': {
            '/translations/show': {
                'limit': 90,
                'remaining': 90,
                'reset': 1678731831
            }
        },
        'friendships': {
            '/friendships/outgoing': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/friendships/create': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/friendships/list': {
                'limit': 200,
                'remaining': 200,
                'reset': 1678731831
            },
            '/friendships/no_retweets/ids': {
                'limit': 60,
                'remaining': 60,
                'reset': 1678731831
            },
            '/friendships/lookup': {
                'limit': 500,
                'remaining': 500,
                'reset': 1678731831
            },
            '/friendships/incoming': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/friendships/show': {
                'limit': 800,
                'remaining': 800,
                'reset': 1678731831
            }
        },
        'guide': {
            '/guide': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/guide/get_explore_locations': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            },
            '/guide/topic': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/guide/get_explore_settings': {
                'limit': 200,
                'remaining': 200,
                'reset': 1678731831
            },
            '/guide/explore_locations_with_autocomplete': {
                'limit': 800,
                'remaining': 800,
                'reset': 1678731831
            }
        },
        'auth': {
            '/auth/csrf_token': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            }
        },
        'compliance': {
            '/compliance/jobs&POST': {
                'limit': 150,
                'remaining': 150,
                'reset': 1678731831
            },
            '/compliance/jobs&GET': {
                'limit': 150,
                'remaining': 150,
                'reset': 1678731831
            },
            '/compliance/jobs/:job_id': {
                'limit': 150,
                'remaining': 150,
                'reset': 1678731831
            }
        },
        'paseto': {
            '/paseto/token': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            }
        },
        'badge_count': {
            '/badge_count/badge_count': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'blocks': {
            '/blocks/list': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/blocks/create&POST': {
                'limit': 400,
                'remaining': 400,
                'reset': 1678731831
            },
            '/blocks/exists': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/blocks/ids': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            }
        },
        'tfb': {
            '/tfb/v1/quick_promote/statuses/most_recently_active': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/tfb/v1/quick_promote/statuses/timeline': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'urls': {
            '/urls/expand': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/urls/click': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            }
        },
        'geo': {
            '/geo/similar_places': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/geo/place_page': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/geo/id/:place_id': {
                'limit': 75,
                'remaining': 75,
                'reset': 1678731831
            },
            '/geo/reverse_geocode': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/geo/search': {
                'limit': 60,
                'remaining': 60,
                'reset': 1678731831
            },
            '/geo/places': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/geo/reverse_geocode/from_ip': {
                'limit': 600000,
                'remaining': 600000,
                'reset': 1678731831
            }
        },
        'promoted_content': {
            '/promoted_content/log': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'users': {
            '/users/interests/timelines': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/users/wipe_addressbook': {
                'limit': 10,
                'remaining': 10,
                'reset': 1678731831
            },
            '/users/phone_number_available': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/users/': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/users/contributors': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/users/:id': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/users/contributees': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/users/:id/list_memberships&GET': {
                'limit': 75,
                'remaining': 75,
                'reset': 1678731831
            },
            '/users/:id/muting&POST': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/users/report_spam': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/users/:source_user_id/blocking/:target_user_id&DELETE': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/users/:id/pinned_lists/:list_id&DELETE': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/users/contributors/pending': {
                'limit': 2000,
                'remaining': 2000,
                'reset': 1678731831
            },
            '/users/send_invites_by_email': {
                'limit': 10,
                'remaining': 10,
                'reset': 1678731831
            },
            '/users/show/:id': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            },
            '/users/:source_user_id/following&POST': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/users/:id/tweets': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/users/:id/retweets/:source_tweet_id&DELETE': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/users/search': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/users/interests/topics': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/users/:id/likes&POST': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/users/suggestions/:slug': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/users/:id/retweets&POST': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/users/contributees/pending': {
                'limit': 200,
                'remaining': 200,
                'reset': 1678731831
            },
            '/users/recommendations': {
                'limit': 60,
                'remaining': 60,
                'reset': 1678731831
            },
            '/users/profile_banner': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/users/by/username/:source_username/following/:target_user_name&DELETE': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/users/by/username/:handle/tweets': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/users/derived_info': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/users/:id/blocking&POST': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/users/email_phone_info': {
                'limit': 30,
                'remaining': 30,
                'reset': 1678731831
            },
            '/users/by/username/:source_username/following&POST': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/users/:id/followers': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/users/suggestions/:slug/members': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/users/:id/pinned_lists&GET': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/users/:id/muting': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/users/:id/following': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/users/:id/mentions': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/users/:id/pinned_lists&POST': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/users/:id/owned_lists&GET': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/users/by/username/:username': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/users/:source_user_id/following/:target_user_id&DELETE': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/users/following_followers_of': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/users/:id/followed_lists&POST': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/users/lookup': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/users/by/username/:username/followers': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/users/:id/followed_lists/:list_id&DELETE': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/users/:id/likes/:tweet_id&DELETE': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/users/:id/blocking': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/users/suggestions': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/users/by/username/:username/following': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/users/by/username/:handle/mentions': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/users/extended_profile': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/users/by': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/users/:source_user_id/muting/:target_user_id&DELETE': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/users/reverse_lookup': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            },
            '/users/:id/followed_lists&GET': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/users/:id/liked_tweets': {
                'limit': 75,
                'remaining': 75,
                'reset': 1678731831
            }
        },
        'special_events': {
            '/special_events/world_cup_2014/settings': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            },
            '/special_events/world_cup_2014/countries/list': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            }
        },
        'device_following': {
            '/device_following/list': {
                'limit': 60,
                'remaining': 60,
                'reset': 1678731831
            },
            '/device_following/ids': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'prompts': {
            '/prompts/record_event': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/prompts/suggest': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'teams': {
            '/teams/authorize': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            }
        },
        'followers': {
            '/followers/ids': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            },
            '/followers/vit/ids': {
                'limit': 30,
                'remaining': 30,
                'reset': 1678731831
            },
            '/followers/vit/list': {
                'limit': 30,
                'remaining': 30,
                'reset': 1678731831
            },
            '/followers/list': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            }
        },
        'commerce': {
            '/commerce/payment_methods': {
                'limit': 30,
                'remaining': 30,
                'reset': 1678731831
            },
            '/commerce/addresses': {
                'limit': 30,
                'remaining': 30,
                'reset': 1678731831
            },
            '/commerce/products': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/commerce/profiles': {
                'limit': 30,
                'remaining': 30,
                'reset': 1678731831
            },
            '/commerce/user_profiles': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            }
        },
        'collections': {
            '/collections/list': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            },
            '/collections/entries': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            },
            '/collections/show': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            }
        },
        'bouncer': {
            '/bouncer/opt_in': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            }
        },
        'permissions': {
            '/permissions/user_permissions/admin_email_verification': {
                'limit': 3,
                'remaining': 3,
                'reset': 1678731831
            },
            '/permissions/user_permissions': {
                'limit': 3,
                'remaining': 3,
                'reset': 1678731831
            }
        },
        '{:Version}': {
            '/{:Version}/moments/set_cover/{moment_id:Long}': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'onboarding': {
            '/onboarding/begin_verification': {
                'limit': 5,
                'remaining': 5,
                'reset': 1678731831
            }
        },
        'tweets&POST': {
            '/tweets&POST': {
                'limit': 200,
                'remaining': 200,
                'reset': 1678731831
            }
        },
        'tv': {
            '/tv/telecasts/:id': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/tv/shows/:id': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'statuses': {
            '/statuses/retweeters/ids': {
                'limit': 75,
                'remaining': 75,
                'reset': 1678731831
            },
            '/statuses/favorited_by': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/statuses/retweets_of_me': {
                'limit': 75,
                'remaining': 75,
                'reset': 1678731831
            },
            '/statuses/show/:id': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            },
            '/statuses/home_timeline': {
                'limit': 600,
                'remaining': 600,
                'reset': 1678731831
            },
            '/statuses/user_timeline': {
                'limit': 1000000000,
                'remaining': 1000000000,
                'reset': 1678731831
            },
            '/statuses/friends': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/statuses/retweets/:id': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/statuses/:id/activity/summary': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/statuses/:id/activity': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/statuses/mentions_timeline': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/statuses/oembed': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/statuses/lookup': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/statuses/media_timeline': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            },
            '/statuses/following_timeline': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/statuses/retweeted_by': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/statuses/:id/activity_summary': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'stickerprovider': {
            '/stickerprovider/catalog': {
                'limit': 60,
                'remaining': 60,
                'reset': 1678731831
            },
            '/stickerprovider/stickers/:id': {
                'limit': 150,
                'remaining': 150,
                'reset': 1678731831
            }
        },
        'broadcasts': {
            '/broadcasts/show': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            }
        },
        'custom_profiles': {
            '/custom_profiles/list': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/custom_profiles/show': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'webhooks': {
            '/webhooks/subscriptions/direct_messages': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/webhooks': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            }
        },
        'contacts': {
            '/contacts/upload_and_match': {
                'limit': 20,
                'remaining': 20,
                'reset': 1678731831
            },
            '/contacts/uploaded_by': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/contacts/users': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/contacts/addressbook': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/contacts/users_and_uploaded_by': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/contacts/delete/status': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            }
        },
        'labs': {
            '/labs/2/platform_manipulation/reports': {
                'limit': 5,
                'remaining': 5,
                'reset': 1678731831
            },
            '/labs/:version/tweets/:id/hidden&PUT': {
                'limit': 10,
                'remaining': 10,
                'reset': 1678731831
            },
            '/labs/:version/tweets/stream/filter/': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/labs/:version/users/:id/tweets': {
                'limit': 225,
                'remaining': 225,
                'reset': 1678731831
            },
            '/labs/2/reports': {
                'limit': 5,
                'remaining': 5,
                'reset': 1678731831
            },
            '/labs/:version/tweets/stream/filter/rules&POST': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/labs/:version/tweets/stream/sample': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/labs/:version/users/by/username/:handle/tweets': {
                'limit': 225,
                'remaining': 225,
                'reset': 1678731831
            },
            '/labs/:version/tweets/metrics/private': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/labs/:version/tweets/stream/filter/rules/:instance_name': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/labs/:version/tweets/*': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/labs/:version/users/*': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/labs/:version/tweets/stream/filter/:instance_name': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/labs/:version/tweets/stream/filter/rules/': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/labs/:version/tweets/stream/compliance': {
                'limit': 500,
                'remaining': 500,
                'reset': 1678731831
            },
            '/labs/:version/tweets/search': {
                'limit': 225,
                'remaining': 225,
                'reset': 1678731831
            }
        },
        'i': {
            '/i/config': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/i/tfb/v1/smb/web/:account_id/payment/save': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            }
        },
        'tweet_prompts': {
            '/tweet_prompts/report_interaction': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/tweet_prompts/show': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'moments': {
            '/moments/feedback': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/moments/userlikes': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/moments/statuses/update': {
                'limit': 5,
                'remaining': 5,
                'reset': 1678731831
            },
            '/moments/annotate_timeline': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/moments/like': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/moments/list': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/moments/delete': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/moments/curate/:id': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/moments/get_recommended_tweets': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/moments/show/:id': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/moments/unsubscribe': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/moments/guide': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/moments/curate_metadata/:id': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/moments/publish': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/moments/list_user_moments': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/moments/categories/ttt_categories': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/moments/create': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/moments/pivot': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/moments/search': {
                'limit': 800,
                'remaining': 800,
                'reset': 1678731831
            },
            '/moments/categories': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/moments/modern_guide': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/moments/sports/scores': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/moments/upsert': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/moments/update/:id': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/moments/users': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/moments/permissions': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/moments/unlike': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/moments/list_categories': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/moments/capsule/momentID': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/moments/capsule/:id': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/moments/subscribe': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'limiter_scalding_report_creation': {
            '/limiter_scalding_report_creation': {
                'limit': 4500,
                'remaining': 4500,
                'reset': 1678731831
            }
        },
        'live_video': {
            '/live_video/1/:id/timeline': {
                'limit': 500,
                'remaining': 500,
                'reset': 1678731831
            }
        },
        'fleets': {
            '/fleets/:version/mutes/create': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            },
            '/fleets/:version/viewers': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            },
            '/fleets/:version/delete': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/fleets/:version/avatar_content': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            },
            '/fleets/:version/create': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/fleets/:version/user_fleets': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/fleets/:version/fleetline': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            },
            '/fleets/:version/track_events': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            },
            '/fleets/:version/update': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/fleets/:version/fleet_threads': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            },
            '/fleets/:version/mutes/list': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            },
            '/fleets/:version/mutes/destroy': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            },
            '/fleets/:version/home_timeline': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            },
            '/fleets/:version/feedback/create': {
                'limit': 500,
                'remaining': 500,
                'reset': 1678731831
            },
            '/fleets/:version/mark_read': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            }
        },
        'help': {
            '/help/tos': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/help/configuration': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/help/settings': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/help/privacy': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/help/languages': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/help/experiments': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            }
        },
        'feedback': {
            '/feedback/show/:id': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/feedback/events': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            }
        },
        'business_experience': {
            '/business_experience/twitter_pro_settings/update': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/business_experience/user_features': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/business_experience/dashboard_settings/destroy': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/business_experience/dashboard_features': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/business_experience/keywords': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/business_experience/inbox/interactions': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/business_experience/twitter_pro_settings/show': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/business_experience/twitter_pro_settings/destroy': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/business_experience/inbox/show': {
                'limit': 150,
                'remaining': 150,
                'reset': 1678731831
            },
            '/business_experience/analytics/account': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/business_experience/analytics/tweets': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/business_experience/dashboard_settings/show': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/business_experience/dashboard_settings/update': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            }
        },
        'ads': {
            '/ads/campaigns/account_permissions': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            }
        },
        'offers': {
            '/offers': {
                'limit': 60,
                'remaining': 60,
                'reset': 1678731831
            }
        },
        'graphql&POST': {
            '/graphql&POST': {
                'limit': 2500,
                'remaining': 2500,
                'reset': 1678731831
            }
        },
        'discover': {
            '/discover/universal': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/discover/nearby': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/discover/highlight': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/discover/home': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            }
        },
        'friends': {
            '/friends/vit/ids': {
                'limit': 30,
                'remaining': 30,
                'reset': 1678731831
            },
            '/friends/following/ids': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/friends/following/list': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/friends/list': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            },
            '/friends/vit/list': {
                'limit': 30,
                'remaining': 30,
                'reset': 1678731831
            },
            '/friends/ids': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            }
        },
        'streams': {
            '/streams/recommended_modules': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/streams/related_users': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/streams/recommended_videos': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/streams/stream': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/streams/categories': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'searchrecordings': {
            '/searchrecordings/list': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/searchrecordings/show': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'interests': {
            '/interests/suggestions': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'sandbox': {
            '/sandbox/account_activity/webhooks/:id/subscriptions': {
                'limit': 500,
                'remaining': 500,
                'reset': 1678731831
            }
        },
        'drafts': {
            '/drafts/statuses/update': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/drafts/statuses/destroy': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/drafts/statuses/ids': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/drafts/statuses/list': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/drafts/statuses/show': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/drafts/statuses/create': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            }
        },
        'content': {
            '/content/recommendations': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            }
        },
        'beta': {
            '/beta/timelines/custom/list': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/beta/timelines/custom/show': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/beta/timelines/custom/whitelisted': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/beta/timelines/timeline': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            }
        },
        'direct_messages': {
            '/direct_messages/sent': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/direct_messages/broadcasts/list': {
                'limit': 60,
                'remaining': 60,
                'reset': 1678731831
            },
            '/direct_messages/subscribers/lists/members/show': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            },
            '/direct_messages/mark_read': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            },
            '/direct_messages/subscribers/ids': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/direct_messages/sent_and_received': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/direct_messages/broadcasts/statuses/list': {
                'limit': 60,
                'remaining': 60,
                'reset': 1678731831
            },
            '/direct_messages': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/direct_messages/subscribers/lists/members/ids': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/direct_messages/subscribers/show': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/direct_messages/broadcasts/show': {
                'limit': 60,
                'remaining': 60,
                'reset': 1678731831
            },
            '/direct_messages/broadcasts/statuses/show': {
                'limit': 60,
                'remaining': 60,
                'reset': 1678731831
            },
            '/direct_messages/subscribers/lists/list': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/direct_messages/show': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/direct_messages/subscribers/lists/show': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/direct_messages/events/list': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/direct_messages/unread_count': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/direct_messages/events/show': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            }
        },
        'dm': {
            '/dm/destroy': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/dm/requests': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/dm/unread_count': {
                'limit': 60,
                'remaining': 60,
                'reset': 1678731831
            },
            '/dm/inbox_initial_state': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/dm/conversation/:id/metadata': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/dm/user_updates': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/dm/user_inbox': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/dm/inbox_timeline/:Id': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/dm/top_requests': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/dm/permissions/secret': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/dm/conversation/:id': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/dm/permissions': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            }
        },
        'stations': {
            '/stations/*': {
                'limit': 2000,
                'remaining': 2000,
                'reset': 1678731831
            }
        },
        'timeline': {
            '/timeline/retweeted_by': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/timeline/conversation/:id': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/timeline/home_latest': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/timeline/icymi': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/timeline/list_recommended_users': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/timeline/liked_by': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/timeline/media/:id': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/timeline/user/:id': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/timeline/favorites/:id': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/timeline/reactive': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/timeline/list': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/timeline/bookmark': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            },
            '/timeline/profile/:id': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/timeline/home': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'media': {
            '/media/upload': {
                'limit': 500,
                'remaining': 500,
                'reset': 1678731831
            }
        },
        'traffic': {
            '/traffic/map': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/traffic/beacon-list': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/traffic/recommendations': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            }
        },
        'strato': {
            '/strato/column/User/:id/notifications/': {
                'limit': 60,
                'remaining': 60,
                'reset': 1678731831
            },
            '/strato/column/User/:id/account-security/twoFactorAuthSettings': {
                'limit': 60,
                'remaining': 60,
                'reset': 1678731831
            },
            '/strato/column/None/:id/cms/*': {
                'limit': 150,
                'remaining': 150,
                'reset': 1678731831
            },
            '/strato/column/User/:id/account-security/twoFactorAuthSetting': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            },
            '/strato/column/User/:id/search/searchSafetyReadonly': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            }
        },
        'news': {
            '/news/details': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/news/rankings': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/news/top': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            }
        },
        'timelines': {
            '/timelines/hidden.json': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            }
        },
        'foundmedia': {
            '/foundmedia/search': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/foundmedia/categories/:category': {
                'limit': 150,
                'remaining': 150,
                'reset': 1678731831
            },
            '/foundmedia/categories': {
                'limit': 150,
                'remaining': 150,
                'reset': 1678731831
            }
        },
        'push_destinations': {
            '/push_destinations/device': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/push_destinations/list': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            }
        },
        'favorite_users': {
            '/favorite_users/ids': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/favorite_users/list': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'communities': {
            '/communities/1/community/:id/leave': {
                'limit': 5000,
                'remaining': 5000,
                'reset': 1678731831
            },
            '/communities/1/community/:id/members': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            },
            '/communities/1/communities/create': {
                'limit': 1000,
                'remaining': 1000,
                'reset': 1678731831
            },
            '/communities/1/community/:id/show': {
                'limit': 5000,
                'remaining': 5000,
                'reset': 1678731831
            },
            '/communities/1/community/:id/join': {
                'limit': 5000,
                'remaining': 5000,
                'reset': 1678731831
            },
            '/communities/1/communities/show': {
                'limit': 5000,
                'remaining': 5000,
                'reset': 1678731831
            },
            '/communities/1/community/:id/timeline': {
                'limit': 5000,
                'remaining': 5000,
                'reset': 1678731831
            }
        },
        'graph': {
            '/graph/app/optout/status': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'account_activity': {
            '/account_activity/all/webhooks': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/account_activity/all/:instance_name/subscriptions': {
                'limit': 500,
                'remaining': 500,
                'reset': 1678731831
            },
            '/account_activity/direct_messages/webhooks': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/account_activity/webhooks/:id/subscriptions/direct_messages/list': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/account_activity/webhooks/:id/subscriptions/all': {
                'limit': 500,
                'remaining': 500,
                'reset': 1678731831
            },
            '/account_activity/direct_messages/:instance_name/webhooks': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/account_activity/webhooks/:id/subscriptions/all/list': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/account_activity/webhooks/:id/subscriptions/direct_messages': {
                'limit': 500,
                'remaining': 500,
                'reset': 1678731831
            },
            '/account_activity/webhooks': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/account_activity/direct_messages/:instance_name/subscriptions': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/account_activity/webhooks/:id/subscriptions': {
                'limit': 500,
                'remaining': 500,
                'reset': 1678731831
            },
            '/account_activity/all/:instance_name/webhooks': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            }
        },
        'adaptive': {
            '/adaptive': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            }
        },
        'videos': {
            '/videos/suggestions': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/videos/:type/config/:id': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            }
        },
        'account': {
            '/account/multi/list': {
                'limit': 30,
                'remaining': 30,
                'reset': 1678731831
            },
            '/account/login_verification_enrollment': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/account/profile_banner': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/account/update_profile': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/account/personalization/partner_interests': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/account/multi/switch': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/account/verification': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/account/personalization/app_graph': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/account/authenticate_web_view': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/account/login_verification_request': {
                'limit': 120,
                'remaining': 120,
                'reset': 1678731831
            },
            '/account/personalization/download_advertiser_list': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/account/login_verification/remove_method': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/account/personalization/p13n_data': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/account/login_verification_enrollment_v2': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            },
            '/account/multi/add': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/account/beacon': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/account/verify_password': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/account/personalization/download_your_data': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/account/multi/logout_all': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/account/verify_credentials': {
                'limit': 2000,
                'remaining': 2000,
                'reset': 1678731831
            },
            '/account/personalization/appgraph/optout_status': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/account/backup_code': {
                'limit': 60,
                'remaining': 60,
                'reset': 1678731831
            },
            '/account/settings': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/account/change_password': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/account/personalization/p13n_preferences': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/account/personalization/set_optout_cookies': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/account/personalization/twitter_interests': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'safety': {
            '/safety/detection_feedback': {
                'limit': 450000,
                'remaining': 450000,
                'reset': 1678731831
            }
        },
        'alerts': {
            '/alerts/landing_page': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'mob_idsync_generate': {
            '/mob_idsync_generate': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            }
        },
        'favorites': {
            '/favorites/list': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'activity': {
            '/activity/by_friends': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/activity/ds': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/activity/about_me': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/activity/about_me/unread': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            }
        },
        'amplify': {
            '/amplify/marketplace/defaults': {
                'limit': 200,
                'remaining': 200,
                'reset': 1678731831
            },
            '/amplify/categories': {
                'limit': 75,
                'remaining': 75,
                'reset': 1678731831
            },
            '/amplify/marketplace/videos': {
                'limit': 200,
                'remaining': 200,
                'reset': 1678731831
            }
        },
        'bookmark': {
            '/bookmark/entries/add&POST': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/bookmark/entries/remove&POST': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'notifications': {
            '/notifications/:id': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/notifications/view/:id': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/notifications/settings/save': {
                'limit': 500,
                'remaining': 500,
                'reset': 1678731831
            },
            '/notifications/:id/unread_count': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/notifications/settings/logout': {
                'limit': 500,
                'remaining': 500,
                'reset': 1678731831
            },
            '/notifications/settings/login': {
                'limit': 500,
                'remaining': 500,
                'reset': 1678731831
            },
            '/notifications/:id/last_seen_cursor': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/notifications/settings/checkin': {
                'limit': 500,
                'remaining': 500,
                'reset': 1678731831
            }
        },
        'related_results': {
            '/related_results/show/:id': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            }
        },
        'live_event': {
            '/live_event/1/:id/timeline': {
                'limit': 500,
                'remaining': 500,
                'reset': 1678731831
            },
            '/live_event/timeline/:id': {
                'limit': 500,
                'remaining': 500,
                'reset': 1678731831
            }
        },
        'lists&POST': {
            '/lists&POST': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            }
        },
        'device': {
            '/device/install_referrer': {
                'limit': 18000,
                'remaining': 18000,
                'reset': 1678731831
            },
            '/device/register': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/device/operator_signup_info': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/device/sms_verify_begin': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/device/token': {
                'limit': 100,
                'remaining': 100,
                'reset': 1678731831
            }
        },
        'tweets': {
            '/tweets/search/all': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/tweets/search/stream/rules': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/tweets/search/recent': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/tweets/sample/stream': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/tweets/:id&DELETE': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/tweets/': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/tweets/counts/all': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/tweets/search/stream': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            },
            '/tweets/search/:product/:label': {
                'limit': 1800,
                'remaining': 1800,
                'reset': 1678731831
            },
            '/tweets/search/stream/rules/validation&POST': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/tweets/search/:product/:instance/counts': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/tweets/:id/retweeted_by': {
                'limit': 75,
                'remaining': 75,
                'reset': 1678731831
            },
            '/tweets/:tweet_id/liking_users': {
                'limit': 75,
                'remaining': 75,
                'reset': 1678731831
            },
            '/tweets/:id': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/tweets/search/stream/rules&DELETE': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/tweets/counts/recent': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/tweets/search/stream/rules&POST': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/tweets/:id/hidden&PUT': {
                'limit': 50,
                'remaining': 50,
                'reset': 1678731831
            }
        },
        'saved_searches': {
            '/saved_searches/destroy/:id': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/saved_searches/show/:id': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/saved_searches/list': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'oauth': {
            '/oauth/revoke': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            },
            '/oauth/authenticate_periscope': {
                'limit': 150,
                'remaining': 150,
                'reset': 1678731831
            },
            '/oauth/list': {
                'limit': 30,
                'remaining': 30,
                'reset': 1678731831
            },
            '/oauth/invalidate_token': {
                'limit': 450,
                'remaining': 450,
                'reset': 1678731831
            },
            '/oauth/revoke_html': {
                'limit': 15,
                'remaining': 15,
                'reset': 1678731831
            }
        },
        'storystream': {
            '/storystream/stories': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            }
        },
        'search': {
            '/search/integrated': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/search/tweets': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            },
            '/search/universal': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            },
            '/search/typeahead': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/search/adaptive': {
                'limit': 900,
                'remaining': 900,
                'reset': 1678731831
            }
        },
        'trends': {
            '/trends/personalized': {
                'limit': 60,
                'remaining': 60,
                'reset': 1678731831
            },
            '/trends/plus': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/trends/timeline': {
                'limit': 300,
                'remaining': 300,
                'reset': 1678731831
            },
            '/trends/closest': {
                'limit': 75,
                'remaining': 75,
                'reset': 1678731831
            },
            '/trends/available': {
                'limit': 75,
                'remaining': 75,
                'reset': 1678731831
            },
            '/trends/place': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'live_pipeline': {
            '/live_pipeline/events': {
                'limit': 180,
                'remaining': 180,
                'reset': 1678731831
            }
        },
        'graphql': {
            '/graphql': {
                'limit': 2500,
                'remaining': 2500,
                'reset': 1678731831
            }
        }
    }
}
```