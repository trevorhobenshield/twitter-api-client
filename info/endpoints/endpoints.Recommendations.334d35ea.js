"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Recommendations"],
  {
    40886: (e, t, s) => {
      s.r(t), s.d(t, { default: () => a });
      var n = s(6899),
        r = s(13239);
      const i = new n.fK.Entity(
        "recommendations",
        { user: r.Z },
        { idAttribute: (e) => e.user.id_str }
      );
      var c = s(6623),
        o = s(55371);
      const u = (e) => ({ ...o.getGlobalDefaults(e), excluded: [], pc: !0 }),
        a = ({ apiClient: e, featureSwitches: t }) => ({
          fetch(s, r = {}) {
            const o = { ...u(t), ...s, ...(0, c.Y)(t) };
            return e
              .get("users/recommendations", o, r)
              .then((e) => (0, n.Fv)(e, [i]));
          },
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Recommendations.334d35ea.js.map
