(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Subscription"],
  {
    61827: (e) => {
      e.exports = {
        queryId: "lFi3xnx0auUUnyG4YwpCNw",
        operationName: "GetUserClaims",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    14424: (e, t, r) => {
      "use strict";
      r.r(t), r.d(t, { default: () => n });
      r(53985);
      const s = (e) => {
        var t, r, s;
        return {
          userClaims: (null !=
          (t =
            null == e || null == (r = e.viewer_v2) || null == (s = r.claims)
              ? void 0
              : s.flatMap(({ resources: e }) => (null != e ? e : [])))
            ? t
            : []
          )
            .map(({ rest_id: e }) => {
              if (e) return { rest_id: e };
            })
            .filter(Boolean),
        };
      };
      var i = r(61827),
        a = r.n(i);
      const n = ({ apiClient: e, featureSwitches: t }) => ({
        fetchUserClaims: () => e.graphQL(a(), {}).then(s),
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Subscription.00cc311a.js.map
