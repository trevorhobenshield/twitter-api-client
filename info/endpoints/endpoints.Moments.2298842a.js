"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Moments"],
  {
    61821: (e, t, n) => {
      n.r(t), n.d(t, { default: () => c });
      var o = n(6899),
        a = n(63752),
        s = n(93333),
        i = n(36364),
        r = n(6623);
      const c = ({ apiClient: e, featureSwitches: t }) => ({
        create: (t, n) =>
          e
            .post(
              "moments/create",
              t,
              {},
              {
                ...n,
                ...(0, r.c)(),
                ...(0, s.Z)(t.teamUserId),
                "content-type": "application/json",
              }
            )
            .then((e) => e && e.created_moment && e.created_moment.moment),
        updateMetadata: (t, n) =>
          e
            .post(
              `moments/update/${t.id}`,
              t,
              {},
              {
                ...n,
                ...(0, r.c)(),
                ...(0, s.Z)(t.teamUserId),
                "content-type": "application/json",
              }
            )
            .then((e) => e && e.updated_moment && e.updated_moment.moment),
        curateTimeline: (t, n) =>
          e
            .post(
              `moments/curate/${t.id}`,
              t,
              {},
              {
                ...n,
                ...(0, r.c)(),
                ...(0, s.Z)(t.teamUserId),
                "content-type": "application/json",
              }
            )
            .then((e) => e && e.updated_moment && e.updated_moment.moment),
        publish: (t, n) =>
          e
            .post(
              `moments/publish/${t.id}`,
              {},
              {},
              {
                ...n,
                ...(0, r.c)(),
                ...(0, s.Z)(t.teamUserId),
                "content-type": "application/json",
              }
            )
            .then((e) => e && e.updated_moment && e.updated_moment.moment),
        delete: (t, n) =>
          e.post(
            `moments/delete/${t.moment_id}`,
            {},
            {},
            {
              ...n,
              ...(0, r.c)(),
              ...(0, s.Z)(t.teamUserId),
              "content-type": "application/json",
            }
          ),
        curateTweetMetadata(t, n) {
          const o = { updates: [t.promotedMedia], use_staging_timeline: !0 };
          return e
            .post(
              `moments/curate_metadata/${t.id}`,
              o,
              {},
              {
                ...n,
                ...(0, r.c)(),
                ...(0, s.Z)(t.teamUserId),
                "content-type": "application/json",
              }
            )
            .then((e) => {
              var t;
              return null == e || null == (t = e.updated_moment)
                ? void 0
                : t.moment;
            });
        },
        fetchMoment(t, n) {
          const c = {
            bypass_cache: !0,
            cards_platform: a.i5,
            dedupe_pages: !0,
            get_annotations: !0,
            hydration_count: 100,
            include_cards: 1,
            staging: !0,
            tweet_mode: "extended",
            v: 1473704494,
          };
          return e
            .get(`moments/capsule/${t.id}`, c, {
              ...n,
              ...(0, r.c)(),
              ...(0, s.Z)(t.teamUserId),
              "content-type": "application/json",
            })
            .then((e) => {
              const t = { ...e.moment, pages: e.pages, tweets: e.tweets };
              return (0, o.Fv)(t, i.Z);
            });
        },
      });
    },
    6623: (e, t, n) => {
      n.d(t, { Y: () => i, c: () => s });
      n(6886);
      var o = n(53223),
        a = n(82436);
      const s = () => ({ "X-Twitter-UTCOffset": (0, a.Kc)() }),
        i = (e, t = []) => ({
          ext: (0, o.Z)([
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
    82436: (e, t, n) => {
      n.d(t, {
        BC: () => c,
        FI: () => i,
        Kc: () => r,
        gO: () => s,
        zk: () => a,
      });
      const o = () => new Date(Date.now());
      function a(e, t = o()) {
        return (
          t.getFullYear() === e.getFullYear() &&
          t.getMonth() === e.getMonth() &&
          t.getDate() === e.getDate()
        );
      }
      function s(e, t = o()) {
        const n = new Date(t);
        return n.setHours(n.getHours() - 24), a(e, n);
      }
      function i(e, t = o()) {
        const n = t - e;
        return n >= 0 && n <= 6048e5;
      }
      function r(e = o().toString()) {
        const t = e && e.match(/([-+][0-9]+)\s/);
        return t ? t[1] : "";
      }
      function c(e, t) {
        const n = new Date();
        return t < n || t < e ? 0 : Math.min(1, (n - e) / (t - e));
      }
    },
    93333: (e, t, n) => {
      function o(e) {
        return e ? { "x-act-as-user-id": e } : {};
      }
      n.d(t, { Z: () => o });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Moments.2298842a.js.map
