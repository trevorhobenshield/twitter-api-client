"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Friendships"],
  {
    31149: (e, s, t) => {
      t.r(s), t.d(s, { default: () => d });
      var i = t(6899);
      const n = { users: [t(13239).Z] };
      var r = t(55371);
      const o = (e) => ({ ...r.getGlobalDefaults(e), cursor: -1 }),
        l = (e) => (0, i.Fv)(e, n),
        d = ({ apiClient: e, featureSwitches: s }) => ({
          fetchFollowersYouFollow: (t, i) =>
            e.get("friends/following/list", { ...o(s), ...t }, i || {}).then(l),
          fetchPendingFollowers(t, i) {
            const n = { ...o(s), ...t, stringify_ids: !0, count: 100 };
            return e.get("friendships/incoming", n, i || {}).then(l);
          },
          fetchFollowing(t, i) {
            const n = Array.isArray(t) ? void 0 : t;
            return e.get("friends/list", { ...o(s), ...n }, i || {}).then(l);
          },
          acceptPendingFollower: (t, i) =>
            e.post("friendships/accept", { ...o(s), ...t }, {}, i || {}),
          declinePendingFollower: (t, i) =>
            e.post("friendships/deny", { ...o(s), ...t }, {}, i || {}),
          updateFriendship: (t, i) =>
            e.post("friendships/update", { ...o(s), ...t }, {}, i || {}),
          createAllFriendships: (t, i) =>
            e.post("friendships/create_all", { ...o(s), ...t }, {}, i || {}),
          destroyAllFriendships: (t, i) =>
            e.post("friendships/destroy_all", { ...o(s), ...t }, {}, i || {}),
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Friendships.48d5d37a.js.map
