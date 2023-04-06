(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.TweetActivity"],
  {
    64728: (e) => {
      e.exports = {
        queryId: "6dAXygU9-nJz_0WNC_erqw",
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
            "longform_notetweets_richtext_consumption_enabled",
            "responsive_web_enhance_cards_enabled",
          ],
        },
      };
    },
    12505: (e) => {
      e.exports = {
        queryId: "JSi_B43J6JJXdIq7cw1ATg",
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
            "longform_notetweets_richtext_consumption_enabled",
            "responsive_web_enhance_cards_enabled",
          ],
        },
      };
    },
    79115: (e) => {
      e.exports = {
        queryId: "2uxygY22_lVtmcoamo6_9w",
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
            "longform_notetweets_richtext_consumption_enabled",
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
    64849: (e) => {
      e.exports = {
        queryId: "4taQiSNC8Es5Ms9jiIo_qQ",
        operationName: "GetTweetReactionTimeline",
        operationType: "query",
        metadata: {
          featureSwitches: [
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_exclude_directive_enabled",
            "verified_phone_label_enabled",
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled",
            "responsive_web_graphql_timeline_navigation_enabled",
          ],
        },
      };
    },
    89112: (e, t, _) => {
      "use strict";
      _.r(t), _.d(t, { default: () => v });
      var i = _(83175),
        n = _(6899),
        r = _(45265),
        a = _(90650);
      const s = (e) => {
        switch (e) {
          case "Like":
          case "Haha":
          case "Hmm":
          case "Sad":
          case "Cheer":
            return e;
          default:
            return r.k.Like;
        }
      };
      var l = _(64728),
        o = _.n(l),
        d = _(12505),
        p = _.n(d),
        u = _(79115),
        b = _.n(u),
        c = _(64849),
        w = _.n(c),
        m = _(82249);
      const v = ({ apiClient: e, featureSwitches: t }) => ({
        fetchReactedBy: ({ tweetId: t }) =>
          e
            .graphQL(w(), { tweetId: t }, (e, t) => {
              var _, i;
              return (
                null == t ||
                null == (_ = t.tweet_result_by_rest_id) ||
                null == (i = _.result) ||
                !i.reaction_timeline
              );
            })
            .then((e) =>
              ((e) => {
                var t;
                const _ =
                  null == (t = e.tweet_result_by_rest_id) ? void 0 : t.result;
                if (_ && _.reaction_timeline) {
                  var i, r;
                  const e = {};
                  return {
                    reactionTimeline:
                      null == (i = _.reaction_timeline)
                        ? void 0
                        : i.tweet_reaction_timeline_entries
                            .map((t) => {
                              if (t.user_results.result) {
                                const _ = (0, n.Fv)(t.user_results.result, a.Z);
                                return (
                                  (e[_.result] = _.entities.users[_.result]),
                                  {
                                    user: _.result,
                                    reactionType: s(t.reaction_type),
                                  }
                                );
                              }
                            })
                            .filter(Boolean),
                    reactionCounts:
                      null == (r = _.reaction_timeline)
                        ? void 0
                        : r.reactionTypeMap.map((e) => ({
                            count: e.count,
                            type: s(e.type),
                          })),
                    userEntities: e,
                  };
                }
              })(e)
            ),
        fetchLikedBy: ({ count: _, cursor: n, tweetId: r }) =>
          e
            .graphQL(
              o(),
              {
                tweetId: r,
                count: _,
                cursor: n,
                includePromotedContent: !0,
                ...(0, i.d)(t),
              },
              (e, t) => {
                var _;
                return !(
                  null != t &&
                  null != (_ = t.favoriters_timeline) &&
                  _.timeline
                );
              }
            )
            .then((e) => {
              var t;
              return (
                (null == e || null == (t = e.favoriters_timeline)
                  ? void 0
                  : t.timeline) || m.cY
              );
            }),
        fetchRetweetedBy: ({ count: _, cursor: n, tweetId: r }) =>
          e
            .graphQL(
              p(),
              {
                tweetId: r,
                count: _,
                cursor: n,
                includePromotedContent: !0,
                ...(0, i.d)(t),
              },
              (e, t) => {
                var _;
                return !(
                  null != t &&
                  null != (_ = t.retweeters_timeline) &&
                  _.timeline
                );
              }
            )
            .then((e) => {
              var t;
              return (
                (null == e || null == (t = e.retweeters_timeline)
                  ? void 0
                  : t.timeline) || m.cY
              );
            }),
        fetchEditHistory: ({ tweetId: _ }) =>
          e
            .graphQL(
              b(),
              {
                tweetId: _,
                ...(0, i.d)(t),
                withQuickPromoteEligibilityTweetFields: !0,
              },
              (e, t) => {
                var _;
                return !(
                  null != t &&
                  null != (_ = t.tweet_result_by_rest_id) &&
                  _.result
                );
              }
            )
            .then((e) => {
              var t, _;
              return (
                ((null == e || null == (t = e.tweet_result_by_rest_id)
                  ? void 0
                  : t.result) &&
                  e.tweet_result_by_rest_id.result.edit_history_timeline &&
                  (null ==
                  (_ = e.tweet_result_by_rest_id.result.edit_history_timeline)
                    ? void 0
                    : _.timeline)) ||
                m.cY
              );
            }),
      });
    },
    45265: (e, t, _) => {
      "use strict";
      _.d(t, { k: () => i });
      const i = Object.freeze({
        Hmm: "Hmm",
        Sad: "Sad",
        Haha: "Haha",
        Cheer: "Cheer",
        Like: "Like",
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.TweetActivity.eb4d783a.js.map
