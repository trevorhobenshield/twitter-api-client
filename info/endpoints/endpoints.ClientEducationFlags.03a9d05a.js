(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.ClientEducationFlags"],
  {
    27824: (t) => {
      t.exports = {
        queryId: "IjQ-egg0uPkY11NyPMfRMQ",
        operationName: "PutClientEducationFlag",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    68877: (t, e, a) => {
      "use strict";
      a.r(e), a.d(e, { default: () => s, isFatal: () => o });
      var i = a(72599),
        n = a(17360),
        l = a(27824),
        u = a.n(l);
      const o = (t, e) => {
          const a =
            "Done" === (null == e ? void 0 : e.add_client_education_flag_put);
          return (
            a || (0, i.ZP)("GQL Client Education Flag: Failed to add"),
            !a && (0, n.jB)(t)
          );
        },
        s = ({ apiClient: t, featureSwitches: e }) => ({
          putClientEducationFlag: ({ flag: e }) =>
            t.graphQL(u(), { flag: e }, o),
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.ClientEducationFlags.03a9d05a.js.map
