(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Explore"],
  {
    52055: (e) => {
      e.exports = {
        queryId: "UGQD_VslAJBJ4XzigsBYAA",
        operationName: "ImmersiveMedia",
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
    93490: (e, _, i) => {
      "use strict";
      i.r(_),
        i.d(_, { default: () => o, isImmersiveMediaTimelineError: () => d });
      var n = i(72599),
        t = i(17360),
        a = i(83175),
        r = i(52055),
        s = i.n(r),
        l = i(82249);
      const d = (e, _) => {
          var i;
          const a =
            null == _ || null == (i = _.immersiveMedia) ? void 0 : i.timeline;
          return (
            a || (0, n.ZP)("GQL failed to query for Immersive Media timeline"),
            !a && (0, t.jB)(e)
          );
        },
        o = ({ apiClient: e, featureSwitches: _ }) => ({
          fetchImmersiveMedia: (i) =>
            e
              .graphQL(
                s(),
                {
                  pinned_tweet_id: null == i ? void 0 : i.pinned_tweet_id,
                  page_name: null == i ? void 0 : i.page_name,
                  ...(0, a.d)(_),
                },
                d
              )
              .then((e) => {
                var _;
                return (
                  (null == e || null == (_ = e.immersiveMedia)
                    ? void 0
                    : _.timeline) || l.cY
                );
              }),
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Explore.9b2e28ea.js.map
