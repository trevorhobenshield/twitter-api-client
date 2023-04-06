(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.BizProfiles"],
  {
    64256: (e) => {
      e.exports = {
        queryId: "6OFpJ3TH3p8JpwOSgfgyhg",
        operationName: "BizProfileFetchUser",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    48342: (e, s, r) => {
      "use strict";
      r.r(s), r.d(s, { default: () => u });
      var t = r(64256),
        i = r.n(t);
      const u = ({ apiClient: e, featureSwitches: s }) => ({
        fetchUserBizProfile: (s) =>
          e.graphQL(i(), { rest_id: s.rest_id }).then((e) => {
            var s, r, t, i;
            return {
              business:
                (null == (s = e.user_result_by_rest_id) ||
                null == (r = s.result)
                  ? void 0
                  : r.business) || void 0,
              professional:
                (null == (t = e.user_result_by_rest_id) ||
                null == (i = t.result)
                  ? void 0
                  : i.professional) || void 0,
            };
          }),
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.BizProfiles.1e307eda.js.map
