(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Drafts"],
  {
    12632: (e) => {
      e.exports = {
        queryId: "cH9HZWz_EW9gnswvA4ZRiQ",
        operationName: "CreateDraftTweet",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    71173: (e) => {
      e.exports = {
        queryId: "bkh9G3FGgTldS9iTKWWYYw",
        operationName: "DeleteDraftTweet",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    81539: (e) => {
      e.exports = {
        queryId: "JIeXE-I6BZXHfxsgOkyHYQ",
        operationName: "EditDraftTweet",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    66043: (e) => {
      e.exports = {
        queryId: "ZkqIq_xRhiUme0PBJNpRtg",
        operationName: "FetchDraftTweets",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    49498: (e, t, r) => {
      "use strict";
      r.r(t), r.d(t, { default: () => _ });
      var a = r(12632),
        i = r.n(a),
        s = r(71173),
        d = r.n(s),
        n = r(81539),
        o = r.n(n),
        u = r(66043),
        w = r.n(u),
        p = r(98671);
      const _ = ({ apiClient: e, featureSwitches: t }) => ({
        createDraftTweet: (t) =>
          e.graphQL(i(), { post_tweet_request: (0, p.y)(t) }).then((e) => {
            var t;
            return null == (t = e.tweet) ? void 0 : t.rest_id;
          }),
        deleteDraftTweet(t) {
          const { draftTweetId: r } = t;
          return e.graphQL(d(), { draft_tweet_id: r });
        },
        editDraftTweet(t) {
          const { draftTweetId: r, ...a } = t;
          return e
            .graphQL(o(), {
              draft_tweet_id: r,
              post_tweet_request: (0, p.y)(a),
            })
            .then(() => r);
        },
        fetchDraftTweets(t) {
          const r = {
            ascending: !1,
            limit: void 0,
            max_id: void 0,
            min_id: void 0,
          };
          return e.graphQL(w(), { ...r, ...t }, (0, p.F)("Draft")).then((e) => {
            var t, r;
            return (
              (null == (t = e.viewer) || null == (r = t.draft_list)
                ? void 0
                : r.response_data) || []
            );
          });
        },
      });
    },
    98671: (e, t, r) => {
      "use strict";
      r.d(t, { F: () => d, y: () => s });
      var a = r(72599),
        i = r(17360);
      function s({ exclude_reply_user_ids: e, media_ids: t, ...r }) {
        return {
          ...r,
          exclude_reply_user_ids: e ? e.split(",") : [],
          media_ids: t ? t.split(",") : [],
        };
      }
      const d = (e) => (t, r) => {
        const s =
            r &&
            r.viewer &&
            r.viewer.draft_list &&
            r.viewer.draft_list.response_data,
          d =
            r &&
            r.viewer &&
            !!r.viewer.scheduled_tweet_list &&
            r.viewer.scheduled_tweet_list;
        return (
          !s &&
          !d &&
          ((0, a.ZP)(`GQL: Failed to render ${e} Tweets List`), (0, i.jB)(t))
        );
      };
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Drafts.2aa71e7a.js.map
