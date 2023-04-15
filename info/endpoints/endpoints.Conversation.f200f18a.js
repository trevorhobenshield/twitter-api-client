(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Conversation"],
  {
    77561: (e) => {
      e.exports = {
        queryId: "wNNG8DBB8EaXw1lq4vFWGA",
        operationName: "TweetDetail",
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
    33071: (e, t, i) => {
      "use strict";
      i.r(t),
        i.d(t, { default: () => c, isFatalTweetDetailTimelineError: () => d });
      var _ = i(72599),
        n = i(17360),
        r = i(83175),
        a = i(77561),
        o = i.n(a),
        s = i(63140),
        l = i(82249);
      const d = (e, t) => {
          const i =
            !(null == t || !t.threaded_conversation_with_injections) ||
            !(null == t || !t.threaded_conversation_with_injections_v2);
          if (!i) {
            (1 === e.length && e[0].code === s.ZP.StatusNotFound) ||
              (0, _.ZP)("GQL URT: Failed to render TweetDetail timeline");
          }
          return !i && (0, n.jB)(e);
        },
        c = ({ apiClient: e, featureSwitches: t }) => ({
          fetchTweetDetail: ({
            controller_data: i,
            cursor: _,
            focalTweetId: n,
            isReaderMode: a,
            referrer: s,
            rux_context: c,
            with_rux_injections: w,
          }) =>
            e
              .graphQL(
                o(),
                {
                  focalTweetId: n,
                  cursor: _,
                  referrer: s,
                  controller_data: i,
                  rux_context: c,
                  with_rux_injections: w,
                  includePromotedContent: !0,
                  withCommunity: t.isTrue("c9s_enabled"),
                  withQuickPromoteEligibilityTweetFields: !0,
                  withBirdwatchNotes: t.isTrue(
                    "responsive_web_birdwatch_consumption_enabled"
                  ),
                  ...(0, r.d)(t),
                  withVoice: t.isTrue("voice_consumption_enabled"),
                  withV2Timeline: t.isTrue(
                    "graphql_timeline_v2_query_threaded_conversation_with_injections"
                  ),
                  isReaderMode: a,
                },
                d
              )
              .then(
                (e) =>
                  e.threaded_conversation_with_injections ||
                  e.threaded_conversation_with_injections_v2 ||
                  l.cY
              ),
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Conversation.f200f18a.js.map
