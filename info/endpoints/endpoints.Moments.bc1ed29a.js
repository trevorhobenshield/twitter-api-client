"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Moments"],
  {
    61821: (e, t, n) => {
      n.r(t), n.d(t, { default: () => p });
      var a = n(6899),
        o = n(63752),
        s = n(93333),
        m = n(36364),
        d = n(6623);
      const p = ({ apiClient: e, featureSwitches: t }) => ({
        create: (t, n) =>
          e
            .post(
              "moments/create",
              t,
              {},
              {
                ...n,
                ...(0, d.c)(),
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
                ...(0, d.c)(),
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
                ...(0, d.c)(),
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
                ...(0, d.c)(),
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
              ...(0, d.c)(),
              ...(0, s.Z)(t.teamUserId),
              "content-type": "application/json",
            }
          ),
        curateTweetMetadata(t, n) {
          const a = { updates: [t.promotedMedia], use_staging_timeline: !0 };
          return e
            .post(
              `moments/curate_metadata/${t.id}`,
              a,
              {},
              {
                ...n,
                ...(0, d.c)(),
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
          const p = {
            bypass_cache: !0,
            cards_platform: o.i5,
            dedupe_pages: !0,
            get_annotations: !0,
            hydration_count: 100,
            include_cards: 1,
            staging: !0,
            tweet_mode: "extended",
            v: 1473704494,
          };
          return e
            .get(`moments/capsule/${t.id}`, p, {
              ...n,
              ...(0, d.c)(),
              ...(0, s.Z)(t.teamUserId),
              "content-type": "application/json",
            })
            .then((e) => {
              const t = { ...e.moment, pages: e.pages, tweets: e.tweets };
              return (0, a.Fv)(t, m.Z);
            });
        },
      });
    },
    93333: (e, t, n) => {
      function a(e) {
        return e ? { "x-act-as-user-id": e } : {};
      }
      n.d(t, { Z: () => a });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Moments.bc1ed29a.js.map
