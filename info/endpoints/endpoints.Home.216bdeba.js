(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Home"],
  {
    56653: (e) => {
      e.exports = {
        queryId: "VyGvysk4GUAl_et492Gs1Q",
        operationName: "HomeLatestTimeline",
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
    58659: (e) => {
      e.exports = {
        queryId: "m4lVrL6Xa3S3DFWDarz2og",
        operationName: "HomeTimeline",
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
    27602: (e, t, n) => {
      "use strict";
      n.r(t), n.d(t, { default: () => m, isFatalHomeTimelineError: () => p });
      var i = n(72599),
        _ = n(51573),
        o = n(27479),
        r = n(17360),
        s = n(83175),
        a = n(56653),
        l = n.n(a),
        d = n(58659),
        c = n.n(d),
        u = n(82249);
      const p = (e, t) => {
          var n;
          const _ =
            null == t || null == (n = t.home) ? void 0 : n.home_timeline_urt;
          return (
            _ || (0, i.ZP)("GQL Home: Failed to query for Home timeline"),
            !_ && (0, r.jB)(e)
          );
        },
        m = ({ apiClient: e, featureSwitches: t }) => ({
          fetchHome: ({ count: n, cursor: i, requestContext: r, timeout: a }) =>
            (0, _.o)("homeTimeline", () => {
              const _ = o.m.get(),
                l = !!(_ && _.getTweets().length > 0),
                d = {
                  count: n,
                  cursor: i,
                  includePromotedContent: !0,
                  latestControlAvailable: !0,
                  requestContext: r,
                  withCommunity: t.isTrue("c9s_enabled"),
                  ...(0, s.d)(t),
                };
              return e
                .graphQL(
                  c(),
                  l ? { ...d, seenTweetIds: l ? _ && _.getTweets() : [] } : d,
                  p,
                  { forcePost: l, timeout: a }
                )
                .then((e) => {
                  var t;
                  l && _ && _.clearTweets();
                  return (
                    (null == e || null == (t = e.home)
                      ? void 0
                      : t.home_timeline_urt) || u.cY
                  );
                });
            }),
          fetchHomeLatest: ({
            count: n,
            cursor: i,
            requestContext: r,
            timeout: a,
          }) =>
            (0, _.o)("homeLatestTimeline", () => {
              const _ = o.m.getLatest(),
                d = !!(_ && _.getTweets().length > 0),
                c = {
                  count: n,
                  cursor: i,
                  includePromotedContent: !0,
                  latestControlAvailable: !0,
                  requestContext: r,
                  ...(0, s.d)(t),
                };
              return e
                .graphQL(
                  l(),
                  d ? { ...c, seenTweetIds: d ? _ && _.getTweets() : [] } : c,
                  p,
                  { forcePost: d, timeout: a }
                )
                .then((e) => {
                  var t;
                  d && _ && _.clearTweets();
                  return (
                    (null == e || null == (t = e.home)
                      ? void 0
                      : t.home_timeline_urt) || u.cY
                  );
                });
            }),
        });
    },
    83175: (e, t, n) => {
      "use strict";
      n.d(t, { S: () => r, d: () => o });
      var i = n(60917),
        _ = n.n(i);
      const o = (e) => {
          const t = e.isTrue("responsive_web_reactions_enabled");
          return {
            ...r(e),
            withDownvotePerspective: e.isTrue("rweb_reply_downvote_enabled"),
            withReactionsMetadata: t,
            withReactionsPerspective: t,
          };
        },
        r = (e) => _();
    },
    51573: (e, t, n) => {
      "use strict";
      n.d(t, { o: () => l });
      n(21515), n(6886);
      var i = n(72599);
      const _ = new (class {
          constructor() {
            this.promise = new Promise((e, t) => {
              (this.reject = t), (this.resolve = e);
            });
          }
        })(),
        o = _.promise;
      if ("undefined" != typeof document) {
        let e;
        document.addEventListener("DOMContentLoaded", () => {
          _.resolve(), null != e && clearTimeout(e);
        });
        const t = () => {
          "loading" !== document.readyState
            ? _.resolve()
            : (e = setTimeout(() => {
                t();
              }, 500));
        };
        t();
      }
      var r = n(86916),
        s = n(79150),
        a = n(25943);
      function l(e, t, n) {
        const _ =
          "undefined" != typeof window ? window.__PREFETCH_DATA__ : void 0;
        if (!_) return t();
        const l = Date.now(),
          d = _.timestamp || l;
        if (Math.max(0, l - d) >= 3e5)
          return delete window.__PREFETCH_DATA__, t();
        const c = _.items[e];
        if (!c) return t();
        return (n ? n(c.meta) : Promise.resolve(!0)).then(
          (n) =>
            n
              ? ((a.q.didPrefetch[e] = !0),
                Promise.race([c.promise, o])
                  .then(
                    (n) =>
                      n
                        ? r.i(n, s.AK)
                        : ((0, i.ZP)(
                            `DOM loaded but prefetch data was not present for ${e}`
                          ),
                          t()),
                    () => ((a.q.prefetchPromiseRejected[e] = !0), t())
                  )
                  .finally(() => {
                    delete _.items[e];
                  }))
              : t(),
          () => t()
        );
      }
    },
    25943: (e, t, n) => {
      "use strict";
      n.d(t, { q: () => i });
      const i = { didPrefetch: {}, prefetchPromiseRejected: {} };
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Home.216bdeba.js.map
