"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Collections"],
  {
    53225: (e, t, s) => {
      s.r(t), s.d(t, { default: () => f });
      var n = s(6899),
        l = (s(85940), s(50445)),
        i = s(13239),
        c = s(46395);
      const o = /^[^-]+-/,
        a = new n.fK.Entity(
          "collections",
          {},
          { idAttribute: (e, t, s) => s.replace(o, ""), processStrategy: c.Z }
        ),
        r = {
          objects: {
            timelines: new n.fK.Values(a),
            tweets: new n.fK.Values(l.Z),
            users: new n.fK.Values(i.Z),
          },
        };
      var u = s(87233),
        w = s(55371);
      const f = ({ apiClient: e, featureSwitches: t }) => ({
        fetchCollection(s, l = {}) {
          const { id: i } = s;
          return e
            .get(
              "collections/entries",
              Object.assign(
                {},
                ((e) => ({
                  ...w.getGlobalDefaults(e),
                  ...u.getGlobalDefaults(e),
                  count: 5,
                }))(t),
                s,
                { id: `custom-${i}` }
              ),
              l
            )
            .then((e) => (0, n.Fv)(e, r));
        },
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Collections.070e358a.js.map
