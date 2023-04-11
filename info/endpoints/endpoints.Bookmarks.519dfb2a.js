(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Bookmarks"],
  {
    60992: (e) => {
      e.exports = {
        queryId: "MXadnowW4uG_ol0ZKrXICg",
        operationName: "BookmarkFolderTimeline",
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
    17305: (e) => {
      e.exports = {
        queryId: "i78YDd0Tza-dV4SYs58kRg",
        operationName: "BookmarkFoldersSlice",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    85419: (e) => {
      e.exports = {
        queryId: "4KHZvvNbHNf07bsgnL9gWA",
        operationName: "bookmarkTweetToFolder",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    2061: (e) => {
      e.exports = {
        queryId: "ThwoU-Q6_9oZHwxtWdpoPw",
        operationName: "Bookmarks",
        operationType: "query",
        metadata: {
          featureSwitches: [
            "graphql_timeline_v2_bookmark_timeline",
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
    5509: (e) => {
      e.exports = {
        queryId: "6Xxqpq8TM_CREYiuof_h5w",
        operationName: "createBookmarkFolder",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    1258: (e) => {
      e.exports = {
        queryId: "skiACZKC1GDYli-M8RzEPQ",
        operationName: "BookmarksAllDelete",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    86558: (e) => {
      e.exports = {
        queryId: "2UTTsO-6zs93XqlEUZPsSg",
        operationName: "DeleteBookmarkFolder",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    51792: (e) => {
      e.exports = {
        queryId: "a6kPp1cS1Dgbsjhapz1PNw",
        operationName: "EditBookmarkFolder",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    68831: (e) => {
      e.exports = {
        queryId: "2Qbj9XZvtUvyJB4gFwWfaA",
        operationName: "RemoveTweetFromBookmarkFolder",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    5929: (e, o, t) => {
      "use strict";
      t.r(o), t.d(o, { default: () => I, isFatalBookmarksAllDelete: () => Q });
      var r = t(6899),
        a = t(72599),
        n = t(17360),
        i = t(83175);
      const l = new r.fK.Entity("bookmarkFolders", {});
      var _ = t(17305),
        s = t.n(_),
        d = t(60992),
        m = t.n(d),
        p = t(2061),
        k = t.n(p),
        u = t(85419),
        b = t.n(u),
        c = t(5509),
        w = t.n(c),
        v = t(1258),
        h = t.n(v),
        f = t(86558),
        g = t.n(f),
        F = t(51792),
        y = t.n(F),
        B = t(68831),
        q = t.n(B),
        T = t(82249);
      const x = { result: [], entities: {}, slice_info: {} },
        Q = (e, o) => {
          const t = "Done" === (null == o ? void 0 : o.bookmark_all_delete);
          return (
            t || (0, a.ZP)("GQL Bookmarks: Failed to delete all bookmarks"),
            (0, n.jB)(e) || !t
          );
        },
        L = (e, o) => {
          var t, r, i;
          const l =
              null == o ||
              null == (t = o.viewer) ||
              null == (r = t.user_results)
                ? void 0
                : r.result,
            _ = "User" === (null == l ? void 0 : l.__typename) ? l : void 0,
            s =
              null == _ || null == (i = _.bookmark_collections_slice)
                ? void 0
                : i.items;
          return (
            s ||
              (0, a.ZP)(
                "GQL Bookmark Folders: Failed to render Bookmark Folders timeline"
              ),
            !s && (0, n.jB)(e)
          );
        },
        S = (e, o) => {
          var t;
          const r =
            null == o || null == (t = o.bookmark_collection_timeline)
              ? void 0
              : t.timeline;
          return (
            r ||
              (0, a.ZP)(
                "GQL Bookmark Folders: Failed to render Bookmark Folders timeline"
              ),
            !r && (0, n.jB)(e)
          );
        },
        I = ({ apiClient: e, featureSwitches: o }) => ({
          bookmarkTweetToFolder: (o) =>
            e.graphQL(
              b(),
              { ...o },
              (0, n.kj)(
                (e) => !e.bookmark_collection_tweet_put,
                "GQL Bookmark Folders: failed to Add Tweet to Bookmark Folder"
              )
            ),
          createBookmarkFolder: (o) =>
            e.graphQL(
              w(),
              { ...o },
              (0, n.kj)(
                (e) => !e.bookmark_collection_create,
                "GQL Bookmark Folders: failed to Create Bookmark Folder"
              )
            ),
          deleteAll: () => e.graphQL(h(), {}, Q).then((e) => e),
          deleteBookmarkFolder(o) {
            const { bookmarkFolderId: t } = o;
            return e.graphQL(g(), { bookmark_collection_id: t });
          },
          editBookmarkFolder(o) {
            const { bookmarkFolderId: t, name: r } = o;
            return e.graphQL(y(), { bookmark_collection_id: t, name: r });
          },
          removeTweetFromBookmarkFolder(o) {
            const { bookmarkFolderId: t, tweetId: r } = o;
            return e.graphQL(q(), { bookmark_collection_id: t, tweet_id: r });
          },
          fetchBookmarksTimeline: ({ count: t, cursor: r }) =>
            e
              .graphQL(
                k(),
                {
                  count: t,
                  cursor: r,
                  includePromotedContent: !0,
                  ...(0, i.d)(o),
                },
                (e, o) => {
                  var t, r;
                  return !(
                    (null != o &&
                      null != (t = o.bookmark_timeline) &&
                      t.timeline) ||
                    (null != o &&
                      null != (r = o.bookmark_timeline_v2) &&
                      r.timeline)
                  );
                }
              )
              .then((e) => {
                var o, t;
                return (
                  (null == e || null == (o = e.bookmark_timeline_v2)
                    ? void 0
                    : o.timeline) ||
                  (null == e || null == (t = e.bookmark_timeline)
                    ? void 0
                    : t.timeline) ||
                  T.cY
                );
              }),
          fetchBookmarkFolderTimeline: ({
            bookmark_collection_id: t,
            cursor: r,
          }) =>
            e
              .graphQL(
                m(),
                {
                  bookmark_collection_id: t,
                  cursor: r,
                  includePromotedContent: !0,
                  ...(0, i.d)(o),
                },
                S
              )
              .then((e) => {
                var o;
                return (
                  (null == e || null == (o = e.bookmark_collection_timeline)
                    ? void 0
                    : o.timeline) || T.cY
                );
              }),
          fetchBookmarkFoldersSlice: (o) =>
            o
              ? e.graphQL(s(), o, L).then((e) => {
                  var o, t;
                  const a =
                      null == e ||
                      null == (o = e.viewer) ||
                      null == (t = o.user_results)
                        ? void 0
                        : t.result,
                    n =
                      "User" === (null == a ? void 0 : a.__typename)
                        ? a
                        : void 0,
                    i = null == n ? void 0 : n.bookmark_collections_slice;
                  if (i) {
                    const { entities: e, result: o } = (0, r.Fv)(i.items, [l]);
                    return { entities: e, result: o, slice_info: i.slice_info };
                  }
                  return x;
                })
              : Promise.resolve(x),
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Bookmarks.519dfb2a.js.map
