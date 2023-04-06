(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.GraphQLErrors"],
  {
    12657: (e) => {
      e.exports = {
        queryId: "2V2W3HIBuMW83vEMtfo_Rg",
        operationName: "GraphQLError",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    54143: (e, r, t) => {
      "use strict";
      t.r(r), t.d(r, { default: () => o });
      var a = t(12657),
        s = t.n(a);
      const o = ({ apiClient: e, featureSwitches: r }) => ({
        throwError: () => e.graphQL(s(), {}),
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.GraphQLErrors.ef2e58ea.js.map
