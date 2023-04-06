(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.ArticleDomains"],
  {
    79676: (e) => {
      e.exports = {
        queryId: "88Bu08U2ddaVVjKmmXjVYg",
        operationName: "articleNudgeDomains",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    65660: (e, t, r) => {
      "use strict";
      r.r(t), r.d(t, { default: () => n });
      var a = r(79676),
        i = r.n(a);
      const n = ({ apiClient: e, featureSwitches: t }) => ({
        fetchArticleDomainsGraphQL: () =>
          e.graphQL(i(), {}).then((e) => {
            var t;
            return null == (t = e.viewer) ? void 0 : t.article_nudge_domains;
          }),
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.ArticleDomains.3b7fc81a.js.map
