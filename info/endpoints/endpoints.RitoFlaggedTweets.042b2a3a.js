(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.RitoFlaggedTweets"],
  {
    4149: (e) => {
      e.exports = {
        queryId: "CMPDkW0aEs4ra-fXkd_X9Q",
        operationName: "RitoFlaggedTweetsTimeline",
        operationType: "query",
        metadata: {
          featureSwitches: [
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_exclude_directive_enabled",
            "verified_phone_label_enabled",
            "responsive_web_graphql_timeline_navigation_enabled",
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled",
            "tweetypie_unmention_optimization_enabled",
            "vibe_api_enabled",
            "responsive_web_edit_tweet_api_enabled",
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled",
            "view_counts_everywhere_api_enabled",
            "longform_notetweets_consumption_enabled",
            "tweet_awards_web_tipping_enabled",
            "freedom_of_speech_not_reach_fetch_enabled",
            "standardized_nudges_misinfo",
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled",
            "interactive_text_enabled",
            "responsive_web_text_conversations_enabled",
            "longform_notetweets_rich_text_read_enabled",
            "responsive_web_enhance_cards_enabled",
          ],
        },
      };
    },
    89910: (e, _, t) => {
      "use strict";
      t.r(_),
        t.d(_, {
          default: () => d,
          isFatalRitoFlaggedTweetsTimelineError: () => o,
        });
      var i = t(72599),
        n = t(17360),
        a = t(83175),
        r = t(4149),
        s = t.n(r),
        l = t(82249);
      const o = (e, _) => {
          var t;
          const a =
            null == _ || null == (t = _.user_result_by_rest_id)
              ? void 0
              : t.result;
          return (
            a ||
              (0, i.ZP)(
                "GQL RitoFlaggedTweets: Failed to query for Rito Flagged Tweets timeline"
              ),
            !a && (0, n.jB)(e)
          );
        },
        d = ({ apiClient: e, featureSwitches: _ }) => ({
          fetchRitoFlaggedTweets: ({ cursor: t, userId: i }) =>
            e
              .graphQL(
                s(),
                {
                  cursor: t,
                  rest_id: i,
                  ...(0, a.d)(_),
                  withSafetyModeUserFields: _.isTrue(
                    "rito_safety_mode_blocked_profile_enabled"
                  ),
                },
                o
              )
              .then((e) => {
                var _;
                const t =
                  null == e || null == (_ = e.user_result_by_rest_id)
                    ? void 0
                    : _.result;
                let i = l.cY;
                var n;
                "User" === (null == t ? void 0 : t.__typename) &&
                  (i =
                    null == (n = t.rito_flagged_tweets_timeline)
                      ? void 0
                      : n.timeline);
                return i || l.cY;
              }),
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.RitoFlaggedTweets.042b2a3a.js.map
