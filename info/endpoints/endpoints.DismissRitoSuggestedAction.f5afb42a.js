(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.DismissRitoSuggestedAction"],
  {
    5737: (e) => {
      e.exports = {
        queryId: "jYvwa61cv3NwNP24iUru6g",
        operationName: "DismissRitoSuggestedAction",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    4913: (e, t, s) => {
      "use strict";
      s.r(t),
        s.d(t, {
          default: () => a,
          isFatalDismissRitoSuggestedAction: () => u,
        });
      var i = s(72599),
        o = s(17360),
        n = s(5737),
        r = s.n(n);
      const u = (e, t) => {
          const s =
            "Done" ===
            (null == t ? void 0 : t.user_dismiss_rito_suggested_action);
          return (
            s ||
              (0, i.ZP)(
                "GQL DismissRitoSuggestedAction: Failed to remove flagged account"
              ),
            !s && (0, o.jB)(e)
          );
        },
        a = ({ apiClient: e, featureSwitches: t }) => ({
          dismissRitoSuggestedAction(t) {
            const { userId: s } = t;
            return e.graphQL(r(), { userId: s }, u);
          },
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.DismissRitoSuggestedAction.f5afb42a.js.map
