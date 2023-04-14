"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Recommendations"],
  {
    40886: (e, t, s) => {
      s.r(t), s.d(t, { default: () => c });
      var n = s(6899),
        r = s(13239);
      const i = new n.fK.Entity(
        "recommendations",
        { user: r.Z },
        {
          idAttribute: (e) => {
            var t;
            return null == (t = e.user) ? void 0 : t.id_str;
          },
        }
      );
      var u = s(6623),
        o = s(55371);
      const a = (e) => ({ ...o.getGlobalDefaults(e), excluded: [], pc: !0 }),
        c = ({ apiClient: e, featureSwitches: t }) => ({
          fetch(s, r = {}) {
            const o = { ...a(t), ...s, ...(0, u.Y)(t) };
            return e
              .get("users/recommendations", o, r)
              .then((e) => (0, n.Fv)(e, [i]));
          },
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Recommendations.e61abcea.js.map
