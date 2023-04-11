"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.BadgeCount"],
  {
    21918: (e, t, n) => {
      n.r(t), n.d(t, { default: () => i });
      const s = { supports_ntab_urt: 1 },
        u = { "x-twitter-polling": "true" },
        i = ({ apiClient: e, featureSwitches: t }) => ({
          fetchBadgeCount: (t, n) =>
            e.getURT("badge_count/badge_count", { ...s, ...t }, { ...u, ...n }),
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.BadgeCount.bb77295a.js.map
