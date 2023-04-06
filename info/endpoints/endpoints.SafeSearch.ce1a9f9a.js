"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.SafeSearch"],
  {
    98178: (e, t, s) => {
      s.r(t), s.d(t, { default: () => a });
      var r = s(60917),
        n = s.n(r);
      const a = ({ apiClient: e, featureSwitches: t }) => ({
        fetch(t, s = {}) {
          const { userId: r } = t;
          return e.get(
            `strato/column/User/${r}/search/searchSafetyReadonly`,
            n(),
            s,
            ""
          );
        },
        set(t, s = {}) {
          const { userId: r, ...a } = t;
          return e.post(
            `strato/column/User/${r}/search/searchSafety`,
            a,
            n(),
            { ...s, "content-type": "application/json" },
            ""
          );
        },
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.SafeSearch.ce1a9f9a.js.map
