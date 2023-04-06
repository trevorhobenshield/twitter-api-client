(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.RitoFlaggedAccounts"],
  {
    81396: (e) => {
      e.exports = {
        queryId: "3S01rv24qThg6f4F-4AXOQ",
        operationName: "RitoFlaggedAccountsTimeline",
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
            "longform_notetweets_richtext_consumption_enabled",
            "responsive_web_enhance_cards_enabled",
          ],
        },
      };
    },
    88466: (e, _, t) => {
      "use strict";
      t.r(_),
        t.d(_, {
          default: () => d,
          isFatalRitoFlaggedAccountsTimelineError: () => s,
        });
      var i = t(72599),
        n = t(17360),
        a = t(83175),
        l = t(81396),
        r = t.n(l),
        o = t(82249);
      const s = (e, _) => {
          var t, a;
          const l =
            null == _ ||
            null == (t = _.viewer_v2) ||
            null == (a = t.rito_flagged_accounts_timeline)
              ? void 0
              : a.timeline;
          return (
            l ||
              (0, i.ZP)(
                "GQL RitoFlaggedAccounts: Failed to query for Rito Flagged Accounts timeline"
              ),
            !l && (0, n.jB)(e)
          );
        },
        d = ({ apiClient: e, featureSwitches: _ }) => ({
          fetchRitoFlaggedAccounts: ({ cursor: t }) =>
            e
              .graphQL(
                r(),
                {
                  cursor: t,
                  ...(0, a.d)(_),
                  withSafetyModeUserFields: _.isTrue(
                    "rito_safety_mode_blocked_profile_enabled"
                  ),
                },
                s
              )
              .then((e) => {
                var _, t;
                return (
                  (null == e ||
                  null == (_ = e.viewer_v2) ||
                  null == (t = _.rito_flagged_accounts_timeline)
                    ? void 0
                    : t.timeline) || o.cY
                );
              }),
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.RitoFlaggedAccounts.c2a23d4a.js.map
