(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.RitoFlaggedAccounts"],
  {
    75169: (e) => {
      e.exports = {
        queryId: "D2IQV0IXewm6AgwP8NcFKA",
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
    88466: (e, t, i) => {
      "use strict";
      i.r(t),
        i.d(t, {
          default: () => d,
          isFatalRitoFlaggedAccountsTimelineError: () => l,
        });
      var _ = i(72599),
        n = i(17360),
        a = i(83175),
        s = i(75169),
        r = i.n(s),
        o = i(82249);
      const l = (e, t) => {
          var i, a;
          const s =
            null == t ||
            null == (i = t.viewer_v2) ||
            null == (a = i.rito_flagged_accounts_timeline)
              ? void 0
              : a.timeline;
          return (
            s ||
              (0, _.ZP)(
                "GQL RitoFlaggedAccounts: Failed to query for Rito Flagged Accounts timeline"
              ),
            !s && (0, n.jB)(e)
          );
        },
        d = ({ apiClient: e, featureSwitches: t }) => ({
          fetchRitoFlaggedAccounts: ({ cursor: i }) =>
            e
              .graphQL(
                r(),
                {
                  cursor: i,
                  ...(0, a.d)(t),
                  withSafetyModeUserFields: t.isTrue(
                    "rito_safety_mode_blocked_profile_enabled"
                  ),
                },
                l
              )
              .then((e) => {
                var t, i;
                return (
                  (null == e ||
                  null == (t = e.viewer_v2) ||
                  null == (i = t.rito_flagged_accounts_timeline)
                    ? void 0
                    : i.timeline) || o.cY
                );
              }),
        });
    },
    83175: (e, t, i) => {
      "use strict";
      i.d(t, { S: () => s, d: () => a });
      var _ = i(60917),
        n = i.n(_);
      const a = (e) => {
          const t = e.isTrue("responsive_web_reactions_enabled");
          return {
            ...s(e),
            withDownvotePerspective: e.isTrue("rweb_reply_downvote_enabled"),
            withReactionsMetadata: t,
            withReactionsPerspective: t,
          };
        },
        s = (e) => n();
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.RitoFlaggedAccounts.cef8072a.js.map
