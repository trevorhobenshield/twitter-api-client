"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.MuteKeywordSettings"],
  {
    64477: (e, t, s) => {
      s.r(t), s.d(t, { default: () => d });
      const d = ({ apiClient: e, featureSwitches: t }) => ({
        fetchMutedKeywords: (t, s) => e.get("mutes/keywords/list", t, s),
        fetchDiscouragedKeywords: (t, s) =>
          e.get("mutes/keywords/discouraged", t, s),
        addMutedKeyword: (t, s) => e.post("mutes/keywords/create", t, {}, s),
        deleteMutedKeyword: (t, s) =>
          e.post("mutes/keywords/destroy", t, {}, s),
        updateMutedKeyword: (t, s) => e.post("mutes/keywords/update", t, {}, s),
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.MuteKeywordSettings.8b3eee2a.js.map
