"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.BonusFollows"],
  {
    49935: (e, t, s) => {
      s.r(t), s.d(t, { default: () => l });
      const o = { user_id: "", template_name: "bonus_follow" },
        l = ({ apiClient: e, featureSwitches: t }) => ({
          fetch: (t = o, s = {}) =>
            e.get("people_discovery/profile_follow", t, s),
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.BonusFollows.255992da.js.map
