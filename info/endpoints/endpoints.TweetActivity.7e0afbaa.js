(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.TweetActivity"],
  {
    64728: (e) => {
      e.exports = {
        queryId: "4UCAqbA6K7LRYlwSiuImIw",
        operationName: "Favoriters",
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
    12505: (e) => {
      e.exports = {
        queryId: "yTkZT3ynT87umyc8KzYYxQ",
        operationName: "Retweeters",
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
    79115: (e) => {
      e.exports = {
        queryId: "8eaWKjHszkS-G_hprUd9AA",
        operationName: "TweetEditHistory",
        operationType: "query",
        metadata: {
          featureSwitches: [
            "freedom_of_speech_not_reach_fetch_enabled",
            "standardized_nudges_misinfo",
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled",
            "tweetypie_unmention_optimization_enabled",
            "vibe_api_enabled",
            "responsive_web_edit_tweet_api_enabled",
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled",
            "view_counts_everywhere_api_enabled",
            "longform_notetweets_consumption_enabled",
            "tweet_awards_web_tipping_enabled",
            "interactive_text_enabled",
            "responsive_web_text_conversations_enabled",
            "longform_notetweets_rich_text_read_enabled",
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_exclude_directive_enabled",
            "verified_phone_label_enabled",
            "responsive_web_graphql_timeline_navigation_enabled",
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled",
            "responsive_web_enhance_cards_enabled",
          ],
        },
      };
    },
    4972: (e, _, t) => {
      "use strict";
      t.r(_), t.d(_, { default: () => b });
      var i = t(83175),
        n = t(64728),
        r = t.n(n),
        a = t(12505),
        l = t.n(a),
        s = t(79115),
        o = t.n(s),
        d = t(82249);
      const b = ({ apiClient: e, featureSwitches: _ }) => ({
        fetchLikedBy: ({ count: t, cursor: n, tweetId: a }) =>
          e
            .graphQL(
              r(),
              {
                tweetId: a,
                count: t,
                cursor: n,
                includePromotedContent: !0,
                ...(0, i.d)(_),
              },
              (e, _) => {
                var t;
                return !(
                  null != _ &&
                  null != (t = _.favoriters_timeline) &&
                  t.timeline
                );
              }
            )
            .then((e) => {
              var _;
              return (
                (null == e || null == (_ = e.favoriters_timeline)
                  ? void 0
                  : _.timeline) || d.cY
              );
            }),
        fetchRetweetedBy: ({ count: t, cursor: n, tweetId: r }) =>
          e
            .graphQL(
              l(),
              {
                tweetId: r,
                count: t,
                cursor: n,
                includePromotedContent: !0,
                ...(0, i.d)(_),
              },
              (e, _) => {
                var t;
                return !(
                  null != _ &&
                  null != (t = _.retweeters_timeline) &&
                  t.timeline
                );
              }
            )
            .then((e) => {
              var _;
              return (
                (null == e || null == (_ = e.retweeters_timeline)
                  ? void 0
                  : _.timeline) || d.cY
              );
            }),
        fetchEditHistory: ({ tweetId: t }) =>
          e
            .graphQL(
              o(),
              {
                tweetId: t,
                ...(0, i.d)(_),
                withQuickPromoteEligibilityTweetFields: !0,
              },
              (e, _) => {
                var t;
                return !(
                  null != _ &&
                  null != (t = _.tweet_result_by_rest_id) &&
                  t.result
                );
              }
            )
            .then((e) => {
              var _, t;
              return (
                ((null == e || null == (_ = e.tweet_result_by_rest_id)
                  ? void 0
                  : _.result) &&
                  e.tweet_result_by_rest_id.result.edit_history_timeline &&
                  (null ==
                  (t = e.tweet_result_by_rest_id.result.edit_history_timeline)
                    ? void 0
                    : t.timeline)) ||
                d.cY
              );
            }),
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.TweetActivity.7e0afbaa.js.map
