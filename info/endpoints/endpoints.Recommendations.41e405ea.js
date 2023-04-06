"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Recommendations", "endpoints.Users"],
  {
    40886: (e, t, n) => {
      n.r(t), n.d(t, { default: () => c });
      var r = n(6899),
        s = n(13239);
      const i = new r.fK.Entity(
        "recommendations",
        { user: s.Z },
        { idAttribute: (e) => e.user.id_str }
      );
      var o = n(6623),
        a = n(55371);
      const u = (e) => ({ ...a.getGlobalDefaults(e), excluded: [], pc: !0 }),
        c = ({ apiClient: e, featureSwitches: t }) => ({
          fetch(n, s = {}) {
            const a = { ...u(t), ...n, ...(0, o.Y)(t) };
            return e
              .get("users/recommendations", a, s)
              .then((e) => (0, r.Fv)(e, [i]));
          },
        });
    },
    55371: (e, t, n) => {
      n.r(t), n.d(t, { default: () => _, getGlobalDefaults: () => a });
      var r = n(6899),
        s = n(70151),
        i = n(13239),
        o = n(60348);
      const a = (e) => {
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
            ...(0, s.Z)(t ? { include_ext_is_blue_verified: 1 } : null),
            ...(0, s.Z)(n ? { include_ext_verified_type: 1 } : null),
            skip_status: 1,
          };
        },
        u = (e) => (0, r.Fv)(e, i.Z),
        c = (e) => (0, r.Fv)(e, [i.Z]),
        _ = ({ apiClient: e, featureSwitches: t }) => ({
          fetchUsers: (n, r = {}) =>
            e.get("users/lookup", { ...a(t), ...n }, r).then(c),
          follow(n, r = {}) {
            const { id_str: s, promotedContent: i, ...c } = n,
              _ = (0, o.cL)(i);
            return e
              .post(
                "friendships/create",
                { ...a(t), ..._, user_id: s, ...c },
                {},
                r
              )
              .then(u);
          },
          unfollow(n, r = {}) {
            const { id_str: s, promotedContent: i, ...c } = n,
              _ = (0, o.cL)(i);
            return e
              .post(
                "friendships/destroy",
                { ...a(t), ..._, user_id: s, ...c },
                {},
                r
              )
              .then(u);
          },
          cancelPendingFollow(t, n = {}) {
            const { id_str: r, ...s } = t;
            return e
              .post("friendships/cancel", { ...s, user_id: r }, {}, n)
              .then(u);
          },
          block(t, n = {}) {
            const { id_str: r, promotedContent: s, ...i } = t,
              a = (0, o.cL)(s);
            return e
              .post("blocks/create", { ...a, user_id: r, ...i }, {}, n)
              .then(u);
          },
          unblock(t, n = {}) {
            const { id_str: r, promotedContent: s, ...i } = t,
              a = (0, o.cL)(s);
            return e
              .post("blocks/destroy", { ...a, user_id: r, ...i }, {}, n)
              .then(u);
          },
          mute(t, n = {}) {
            const { id_str: r, promotedContent: s, ...i } = t,
              a = (0, o.cL)(s);
            return e
              .post("mutes/users/create", { ...a, user_id: r, ...i }, {}, n)
              .then(u);
          },
          unmute(t, n = {}) {
            const { id_str: r, promotedContent: s, ...i } = t,
              a = (0, o.cL)(s);
            return e
              .post("mutes/users/destroy", { ...a, user_id: r, ...i }, {}, n)
              .then(u);
          },
          fetchProfileTranslation(t, n = {}) {
            const { profileUserId: r } = t;
            return e.get(
              `strato/column/None/profileUserId=${r},destinationLanguage=None,translationSource=Some(Google)/translation/service/translateProfile`,
              {},
              n,
              ""
            );
          },
        });
    },
    6623: (e, t, n) => {
      n.d(t, { Y: () => o, c: () => i });
      n(6886);
      var r = n(53223),
        s = n(82436);
      const i = () => ({ "X-Twitter-UTCOffset": (0, s.Kc)() }),
        o = (e, t = []) => ({
          ext: (0, r.Z)([
            ...t,
            "mediaStats",
            "highlightedLabel",
            "hasNftAvatar",
            e.isTrue("responsive_web_reactions_enabled") &&
              "signalsReactionMetadata",
            e.isTrue("responsive_web_reactions_enabled") &&
              "signalsReactionPerspective",
            e.isTrue("rweb_reply_downvote_enabled") &&
              "replyvotingDownvotePerspective",
            e.isTrue("voice_consumption_enabled") && "voiceInfo",
            !0 ===
              e.getValueWithoutScribeImpression(
                "responsive_web_birdwatch_pivots_enabled"
              ) && "birdwatchPivot",
            (e.isTrue("interactive_text_enabled") ||
              e.isTrue("responsive_web_text_conversations_enabled")) &&
              "enrichments",
            "superFollowMetadata",
            e.isTrue("dont_mention_me_view_api_enabled") && "unmentionInfo",
            e.isTrue("responsive_web_edit_tweet_api_enabled") && "editControl",
            e.isTrue("vibe_api_enabled") && "vibe",
          ]).join(","),
        });
    },
    60348: (e, t, n) => {
      n.d(t, { cL: () => i, gQ: () => o });
      const r = Object.freeze({});
      function s(e) {
        const { conversational_card_details: t } = e;
        return t ? { conversational_card_details: t } : void 0;
      }
      function i(e) {
        if (!e) return r;
        const { disclosure_type: t, impression_id: n } = e,
          i = "earned" === a(e),
          o = JSON.stringify(s(e));
        if (!t || !n) return r;
        let u = { impression_id: n };
        return (
          o && (u = { ...u, engagement_metadata: o }),
          i && (u = { ...u, earned: 1 }),
          u
        );
      }
      function o(e) {
        if (!e) return;
        const { disclosure_type: t, impression_id: n } = e,
          r = "earned" === a(e),
          i = s(e);
        if (!t || !n) return;
        let o = { impression_id: n };
        return (
          i && (o = { ...o, engagement_metadata: i }),
          r && (o = { ...o, earned: !0 }),
          { engagement_request: { ...o } }
        );
      }
      function a(e) {
        const t = null == e ? void 0 : e.disclosure_type;
        return t && t.toLowerCase();
      }
    },
    82436: (e, t, n) => {
      n.d(t, {
        BC: () => u,
        FI: () => o,
        Kc: () => a,
        gO: () => i,
        zk: () => s,
      });
      const r = () => new Date(Date.now());
      function s(e, t = r()) {
        return (
          t.getFullYear() === e.getFullYear() &&
          t.getMonth() === e.getMonth() &&
          t.getDate() === e.getDate()
        );
      }
      function i(e, t = r()) {
        const n = new Date(t);
        return n.setHours(n.getHours() - 24), s(e, n);
      }
      function o(e, t = r()) {
        const n = t - e;
        return n >= 0 && n <= 6048e5;
      }
      function a(e = r().toString()) {
        const t = e && e.match(/([-+][0-9]+)\s/);
        return t ? t[1] : "";
      }
      function u(e, t) {
        const n = new Date();
        return t < n || t < e ? 0 : Math.min(1, (n - e) / (t - e));
      }
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Recommendations.41e405ea.js.map
