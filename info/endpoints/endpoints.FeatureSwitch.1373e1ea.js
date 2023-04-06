"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.FeatureSwitch"],
  {
    36162: (e, t, s) => {
      s.r(t),
        s.d(t, { REQUEST_FEATURE_SWITCHES_PATH: () => i, default: () => a });
      const i = "help/settings",
        n = { include_zero_rate: !0 },
        a = ({ apiClient: e, featureSwitches: t }) => ({
          fetch: (t, s = {}) => e.get(i, { ...n, ...t }, s),
          fetchLanguages: (t, s = {}) =>
            e.get("help/languages", { ...n, ...t }, s),
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.FeatureSwitch.1373e1ea.js.map
