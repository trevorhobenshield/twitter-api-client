(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.RitoSuggestedActions"],
  {
    22276: (t) => {
      t.exports = {
        queryId: "2njnYoE69O2jdUM7KMEnDw",
        operationName: "ConvertRitoSuggestedActions",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    95885: (t, e, o) => {
      "use strict";
      o.r(e),
        o.d(e, {
          default: () => u,
          isFatalConvertRitoSuggestedActionsError: () => a,
        });
      var n = o(72599),
        s = o(17360),
        i = o(22276),
        r = o.n(i);
      const a = (t, e) => {
          const o = null == e ? void 0 : e.convert_rito_suggested_actions;
          return (
            o ||
              (0, n.ZP)(
                "GQL ConvertRitoSuggestedActions: Failed to query for Convert Rito Suggested Actions"
              ),
            !o && (0, s.jB)(t)
          );
        },
        u = ({ apiClient: t, featureSwitches: e }) => ({
          callConvertRitoSuggestedActions: (e) => t.graphQL(r(), { ...e }, a),
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.RitoSuggestedActions.9ec7c11a.js.map
