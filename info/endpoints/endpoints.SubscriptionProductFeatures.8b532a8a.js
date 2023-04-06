(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.SubscriptionProductFeatures"],
  {
    1819: (e) => {
      e.exports = {
        queryId: "-btar_vkBwWA7s3YWfp_9g",
        operationName: "FeatureSettingsUpdate",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    73402: (e) => {
      e.exports = {
        queryId: "Me2CVcAXxvK2WMr-Nh_Qqg",
        operationName: "SubscriptionProductFeaturesFetch",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    25465: (e, t, r) => {
      "use strict";
      r.r(t), r.d(t, { default: () => o });
      const i = (e) => {
        var t;
        return (
          (null == e || null == (t = e.viewer)
            ? void 0
            : t.subscription_product_features_for_client) || []
        ).reduce(
          (e, t) => (
            t[t.rest_id]
              ? (e[t.rest_id] = {
                  rest_id: t.rest_id,
                  ...t.config,
                  settings: t[t.rest_id],
                })
              : (e[t.rest_id] = { rest_id: t.rest_id, ...t.config }),
            e
          ),
          {}
        );
      };
      var s = r(1819),
        a = r.n(s),
        u = r(73402),
        n = r.n(u);
      const o = ({ apiClient: e, featureSwitches: t }) => ({
        fetchSubscriptionProductFeatures: () => e.graphQL(n(), {}).then(i),
        updateFeatureSettings: (t) => e.graphQL(a(), t),
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.SubscriptionProductFeatures.8b532a8a.js.map
