"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.LiveEvent"],
  {
    98930: (e, t, s) => {
      s.r(t), s.d(t, { default: () => v });
      var n = s(6899),
        a = s(93333),
        r = s(88701),
        i = s(6623),
        c = s(87233),
        o = s(55371);
      const u = (e) => ({
          ...o.getGlobalDefaults(e),
          ...c.getGlobalDefaults(e),
        }),
        v = ({ apiClient: e, featureSwitches: t }) => ({
          fetchLiveEventMetadata(s, c) {
            const { eventId: o, teamUserId: v } = s,
              l = Object.assign({}, c, (0, i.c)(), (0, a.Z)(v));
            return e
              .get(
                `live_event/1/${o}/timeline`,
                { ...u(t), count: 0, urt: !0, ext: "mediaColor" },
                l
              )
              .then((e) => (0, n.Fv)(e, r.u));
          },
          updateRemindMeSubscription(t, s) {
            const { eventId: n, params: a } = t;
            return e.post(`live_event/1/${n}/subscription`, {}, a, s);
          },
        });
    },
    88701: (e, t, s) => {
      s.d(t, { j: () => p, u: () => d });
      var n = s(6899),
        a = s(50445),
        r = s(13239),
        i = s(46395);
      const c = new n.fK.Entity("broadcasts", {}, { processStrategy: i.Z }),
        o = new n.fK.Entity("audiospaces", {}, { processStrategy: i.Z }),
        u = new n.fK.Entity("liveEvents", {}, { processStrategy: i.Z }),
        v = new n.fK.Entity("slates", {}, { processStrategy: i.Z }),
        l = new n.fK.Values([u]),
        d = new n.fK.Object({
          twitter_objects: {
            audiospaces: [o],
            broadcasts: [c],
            live_events: [u],
            slates: [v],
            tweets: [a.Z],
            users: [r.Z],
          },
        }),
        p = new n.fK.Object({ broadcasts: [c], events: l });
    },
    93333: (e, t, s) => {
      function n(e) {
        return e ? { "x-act-as-user-id": e } : {};
      }
      s.d(t, { Z: () => n });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.LiveEvent.6258c53a.js.map
