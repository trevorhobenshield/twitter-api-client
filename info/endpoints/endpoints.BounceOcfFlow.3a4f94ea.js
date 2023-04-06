"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.BounceOcfFlow"],
  {
    25449: (e, t, n) => {
      n.r(t), n.d(t, { default: () => o });
      const o = ({ apiClient: e, featureSwitches: t }) => ({
        task(t, n) {
          const { flow_name: o, test_country_code: s, ...c } = t;
          return e.post(
            "onboarding/bounce",
            c,
            { flow_name: o, test_country_code: s },
            { ...n, "content-type": "application/json" }
          );
        },
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.BounceOcfFlow.3a4f94ea.js.map
