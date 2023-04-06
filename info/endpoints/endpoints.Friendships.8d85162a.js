"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Friendships", "endpoints.Users"],
  {
    31149: (e, t, n) => {
      n.r(t), n.d(t, { default: () => l });
      var s = n(6899);
      const r = { users: [n(13239).Z] };
      var i = n(55371);
      const o = (e) => ({ ...i.getGlobalDefaults(e), cursor: -1 }),
        d = (e) => (0, s.Fv)(e, r),
        l = ({ apiClient: e, featureSwitches: t }) => ({
          fetchFollowersYouFollow: (n, s) =>
            e.get("friends/following/list", { ...o(t), ...n }, s || {}).then(d),
          fetchPendingFollowers(n, s) {
            const r = { ...o(t), ...n, stringify_ids: !0, count: 100 };
            return e.get("friendships/incoming", r, s || {}).then(d);
          },
          fetchFollowing(n, s) {
            const r = Array.isArray(n) ? void 0 : n;
            return e.get("friends/list", { ...o(t), ...r }, s || {}).then(d);
          },
          acceptPendingFollower: (n, s) =>
            e.post("friendships/accept", { ...o(t), ...n }, {}, s || {}),
          declinePendingFollower: (n, s) =>
            e.post("friendships/deny", { ...o(t), ...n }, {}, s || {}),
          updateFriendship: (n, s) =>
            e.post("friendships/update", { ...o(t), ...n }, {}, s || {}),
          createAllFriendships: (n, s) =>
            e.post("friendships/create_all", { ...o(t), ...n }, {}, s || {}),
          destroyAllFriendships: (n, s) =>
            e.post("friendships/destroy_all", { ...o(t), ...n }, {}, s || {}),
        });
    },
    55371: (e, t, n) => {
      n.r(t), n.d(t, { default: () => u, getGlobalDefaults: () => d });
      var s = n(6899),
        r = n(70151),
        i = n(13239),
        o = n(60348);
      const d = (e) => {
          const t = e.isTrue(
              "responsive_web_twitter_blue_verified_badge_is_enabled"
            ),
            n = e.isTrue("blue_business_consumption_api_enabled");
          return {
            include_profile_interstitial_type: 1,
            include_blocking: 1,
            include_blocked_by: 1,
            include_followed_by: 1,
            include_want_retweets: 1,
            include_mute_edge: 1,
            include_can_dm: 1,
            include_can_media_tag: 1,
            include_ext_has_nft_avatar: 1,
            ...(0, r.Z)(t ? { include_ext_is_blue_verified: 1 } : null),
            ...(0, r.Z)(n ? { include_ext_verified_type: 1 } : null),
            skip_status: 1,
          };
        },
        l = (e) => (0, s.Fv)(e, i.Z),
        c = (e) => (0, s.Fv)(e, [i.Z]),
        u = ({ apiClient: e, featureSwitches: t }) => ({
          fetchUsers: (n, s = {}) =>
            e.get("users/lookup", { ...d(t), ...n }, s).then(c),
          follow(n, s = {}) {
            const { id_str: r, promotedContent: i, ...c } = n,
              u = (0, o.cL)(i);
            return e
              .post(
                "friendships/create",
                { ...d(t), ...u, user_id: r, ...c },
                {},
                s
              )
              .then(l);
          },
          unfollow(n, s = {}) {
            const { id_str: r, promotedContent: i, ...c } = n,
              u = (0, o.cL)(i);
            return e
              .post(
                "friendships/destroy",
                { ...d(t), ...u, user_id: r, ...c },
                {},
                s
              )
              .then(l);
          },
          cancelPendingFollow(t, n = {}) {
            const { id_str: s, ...r } = t;
            return e
              .post("friendships/cancel", { ...r, user_id: s }, {}, n)
              .then(l);
          },
          block(t, n = {}) {
            const { id_str: s, promotedContent: r, ...i } = t,
              d = (0, o.cL)(r);
            return e
              .post("blocks/create", { ...d, user_id: s, ...i }, {}, n)
              .then(l);
          },
          unblock(t, n = {}) {
            const { id_str: s, promotedContent: r, ...i } = t,
              d = (0, o.cL)(r);
            return e
              .post("blocks/destroy", { ...d, user_id: s, ...i }, {}, n)
              .then(l);
          },
          mute(t, n = {}) {
            const { id_str: s, promotedContent: r, ...i } = t,
              d = (0, o.cL)(r);
            return e
              .post("mutes/users/create", { ...d, user_id: s, ...i }, {}, n)
              .then(l);
          },
          unmute(t, n = {}) {
            const { id_str: s, promotedContent: r, ...i } = t,
              d = (0, o.cL)(r);
            return e
              .post("mutes/users/destroy", { ...d, user_id: s, ...i }, {}, n)
              .then(l);
          },
          fetchProfileTranslation(t, n = {}) {
            const { profileUserId: s } = t;
            return e.get(
              `strato/column/None/profileUserId=${s},destinationLanguage=None,translationSource=Some(Google)/translation/service/translateProfile`,
              {},
              n,
              ""
            );
          },
        });
    },
    60348: (e, t, n) => {
      n.d(t, { cL: () => i, gQ: () => o });
      const s = Object.freeze({});
      function r(e) {
        const { conversational_card_details: t } = e;
        return t ? { conversational_card_details: t } : void 0;
      }
      function i(e) {
        if (!e) return s;
        const { disclosure_type: t, impression_id: n } = e,
          i = "earned" === d(e),
          o = JSON.stringify(r(e));
        if (!t || !n) return s;
        let l = { impression_id: n };
        return (
          o && (l = { ...l, engagement_metadata: o }),
          i && (l = { ...l, earned: 1 }),
          l
        );
      }
      function o(e) {
        if (!e) return;
        const { disclosure_type: t, impression_id: n } = e,
          s = "earned" === d(e),
          i = r(e);
        if (!t || !n) return;
        let o = { impression_id: n };
        return (
          i && (o = { ...o, engagement_metadata: i }),
          s && (o = { ...o, earned: !0 }),
          { engagement_request: { ...o } }
        );
      }
      function d(e) {
        const t = null == e ? void 0 : e.disclosure_type;
        return t && t.toLowerCase();
      }
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Friendships.8d85162a.js.map
