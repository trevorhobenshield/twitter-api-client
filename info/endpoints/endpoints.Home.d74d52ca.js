(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Home"],
  {
    85302: (e) => {
      e.exports = {
        queryId: "ggk_aL0AFGWZcJs8HmEUcw",
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
    74612: (e) => {
      e.exports = {
        queryId: "BntFPEOxs3GYdPaS6CjUcg",
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
      n.r(t), n.d(t, { default: () => p, isFatalHomeTimelineError: () => m });
      var _ = n(72599),
        i = n(51573),
        o = n(27479),
        r = n(17360),
        s = n(83175),
        a = n(85302),
        l = n.n(a),
        d = n(74612),
        c = n.n(d),
        u = n(82249);
      const m = (e, t) => {
          var n;
          const i =
            null == t || null == (n = t.home) ? void 0 : n.home_timeline_urt;
          return (
            i || (0, _.ZP)("GQL Home: Failed to query for Home timeline"),
            !i && (0, r.jB)(e)
          );
        },
        p = ({ apiClient: e, featureSwitches: t }) => ({
          fetchHome: ({ count: n, cursor: _, requestContext: r, timeout: a }) =>
            (0, i.o)("homeTimeline", () => {
              const i = o.m.get(),
                l = !!(i && i.getTweets().length > 0),
                d = {
                  count: n,
                  cursor: _,
                  includePromotedContent: !0,
                  latestControlAvailable: !0,
                  requestContext: r,
                  withCommunity: t.isTrue("c9s_enabled"),
                  ...(0, s.d)(t),
                };
              return e
                .graphQL(
                  c(),
                  l ? { ...d, seenTweetIds: l ? i && i.getTweets() : [] } : d,
                  m,
                  { forcePost: l, timeout: a }
                )
                .then((e) => {
                  var t;
                  l && i && i.clearTweets();
                  return (
                    (null == e || null == (t = e.home)
                      ? void 0
                      : t.home_timeline_urt) || u.cY
                  );
                });
            }),
          fetchHomeLatest: ({
            count: n,
            cursor: _,
            requestContext: r,
            timeout: a,
          }) =>
            (0, i.o)("homeLatestTimeline", () => {
              const i = o.m.getLatest(),
                d = !!(i && i.getTweets().length > 0),
                c = {
                  count: n,
                  cursor: _,
                  includePromotedContent: !0,
                  latestControlAvailable: !0,
                  requestContext: r,
                  ...(0, s.d)(t),
                };
              return e
                .graphQL(
                  l(),
                  d ? { ...c, seenTweetIds: d ? i && i.getTweets() : [] } : c,
                  m,
                  { forcePost: d, timeout: a }
                )
                .then((e) => {
                  var t;
                  d && i && i.clearTweets();
                  return (
                    (null == e || null == (t = e.home)
                      ? void 0
                      : t.home_timeline_urt) || u.cY
                  );
                });
            }),
        });
    },
    51573: (e, t, n) => {
      "use strict";
      n.d(t, { o: () => l });
      n(21515), n(6886);
      var _ = n(72599);
      const i = new (class {
          constructor() {
            this.promise = new Promise((e, t) => {
              (this.reject = t), (this.resolve = e);
            });
          }
        })(),
        o = i.promise;
      if ("undefined" != typeof document) {
        let e;
        document.addEventListener("DOMContentLoaded", () => {
          i.resolve(), null != e && clearTimeout(e);
        });
        const t = () => {
          "loading" !== document.readyState
            ? i.resolve()
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
        const i =
          "undefined" != typeof window ? window.__PREFETCH_DATA__ : void 0;
        if (!i) return t();
        const l = Date.now(),
          d = i.timestamp || l;
        if (Math.max(0, l - d) >= 3e5)
          return delete window.__PREFETCH_DATA__, t();
        const c = i.items[e];
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
                        : ((0, _.ZP)(
                            `DOM loaded but prefetch data was not present for ${e}`
                          ),
                          t()),
                    () => ((a.q.prefetchPromiseRejected[e] = !0), t())
                  )
                  .finally(() => {
                    delete i.items[e];
                  }))
              : t(),
          () => t()
        );
      }
    },
    25943: (e, t, n) => {
      "use strict";
      n.d(t, { q: () => _ });
      const _ = { didPrefetch: {}, prefetchPromiseRejected: {} };
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Home.d74d52ca.js.map
