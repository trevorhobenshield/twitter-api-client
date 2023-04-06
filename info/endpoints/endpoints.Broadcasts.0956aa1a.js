"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Broadcasts"],
  {
    45205: (s, e, t) => {
      t.r(e), t.d(e, { default: () => i });
      var a = t(6899),
        r = t(88701),
        o = t(63174),
        n = t(63140);
      const c = { include_events: !0 },
        i = ({ apiClient: s, featureSwitches: e }) => ({
          fetchBroadcast: (e, t = {}) => {
            const i = { ...c, ...e, ids: e.ids.join(",") };
            return s.get("broadcasts/show", i, t).then((s) => {
              const { entities: c, result: i } = (0, a.Fv)(s, r.j);
              if (
                e.ids.every(
                  (s) =>
                    !(
                      c.broadcasts &&
                      c.broadcasts[s] &&
                      c.broadcasts[s].broadcast_id
                    )
                )
              )
                return Promise.reject(
                  new o.Z(
                    "fetchBroadcast URL",
                    404,
                    s.headers,
                    [{ code: n.ZP.GenericNotFound }],
                    t
                  )
                );
              const d = {
                result: { broadcasts: i.broadcasts },
                entities: { broadcasts: { ...c.broadcasts } },
              };
              if (
                (i.events &&
                  d.result.broadcasts.forEach((s) => {
                    const e = i.events && i.events[s],
                      t = d.entities.broadcasts[s];
                    if (e && t) {
                      const s = e.map((s) => c.liveEvents[s]);
                      t.liveEvents = s;
                    }
                  }),
                "object" == typeof e.broadcastVersionMap)
              )
                for (const s in e.broadcastVersionMap) {
                  var b;
                  const t = e.broadcastVersionMap[s];
                  (null == (b = d.entities.broadcasts[s])
                    ? void 0
                    : b.version) <= t &&
                    ((d.result.broadcasts = d.result.broadcasts.filter(
                      (e) => e !== s
                    )),
                    delete d.entities.broadcasts[s]);
                }
              return d;
            });
          },
        });
    },
    88701: (s, e, t) => {
      t.d(e, { j: () => l, u: () => v });
      var a = t(6899),
        r = t(50445),
        o = t(13239),
        n = t(46395);
      const c = new a.fK.Entity("broadcasts", {}, { processStrategy: n.Z }),
        i = new a.fK.Entity("audiospaces", {}, { processStrategy: n.Z }),
        d = new a.fK.Entity("liveEvents", {}, { processStrategy: n.Z }),
        b = new a.fK.Entity("slates", {}, { processStrategy: n.Z }),
        u = new a.fK.Values([d]),
        v = new a.fK.Object({
          twitter_objects: {
            audiospaces: [i],
            broadcasts: [c],
            live_events: [d],
            slates: [b],
            tweets: [r.Z],
            users: [o.Z],
          },
        }),
        l = new a.fK.Object({ broadcasts: [c], events: u });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Broadcasts.0956aa1a.js.map
