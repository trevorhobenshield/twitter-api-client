"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.ReportFlow"],
  {
    67151: (e, t, o) => {
      o.r(t), o.d(t, { default: () => n });
      const n = ({ apiClient: e, featureSwitches: t }) => ({
        task(t, o) {
          const { flow_name: n, test_country_code: s, ...r } = t;
          return e.post(
            "report/flow",
            r,
            { flow_name: n, test_country_code: s },
            { ...o, "content-type": "application/json" }
          );
        },
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.ReportFlow.c6789fea.js.map
