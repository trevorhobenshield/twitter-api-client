(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.RitoSuggestedActionsFacePile"],
  {
    75339: (e) => {
      e.exports = {
        queryId: "GnQKeEdL1LyeK3dTQCS1yw",
        operationName: "RitoSuggestedActionsFacePile",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    55104: (e, t, i) => {
      "use strict";
      i.r(t),
        i.d(t, {
          default: () => n,
          isFatalRitoSuggestedActionsFacePileError: () => l,
        });
      var s = i(72599),
        r = i(17360),
        u = i(75339),
        o = i.n(u);
      const l = (e, t) => {
          var i, u;
          const o =
            (null == t || null == (i = t.user.result)
              ? void 0
              : i.rito_suggested_actions_face_pile) &&
            (null == t || null == (u = t.user.result)
              ? void 0
              : u.rito_suggested_actions_face_pile);
          return (
            o ||
              (0, s.ZP)(
                "GQL RitoSuggestedActionsFacePile: Failed to query for Rito Suggested Actions facepile"
              ),
            !o && (0, r.jB)(e)
          );
        },
        n = ({ apiClient: e, featureSwitches: t }) => ({
          fetchRitoSuggestedActionsFacePile: (t) =>
            e.graphQL(o(), { ...t }, l).then((e) => {
              var t, i;
              return (
                (null == e || null == (t = e.user.result)
                  ? void 0
                  : t.rito_suggested_actions_face_pile) &&
                (null == e || null == (i = e.user.result)
                  ? void 0
                  : i.rito_suggested_actions_face_pile)
              );
            }),
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.RitoSuggestedActionsFacePile.84fb7e9a.js.map
