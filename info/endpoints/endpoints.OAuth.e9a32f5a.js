"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.OAuth"],
  {
    96814: (e, t, s) => {
      s.r(t), s.d(t, { default: () => i });
      const i = ({ apiClient: e, featureSwitches: t }) => ({
        fetch: (t, s = {}) => e.getUnversioned("/2/oauth2/authorize", t, s),
        post: (t) => e.postUnversioned("/2/oauth2/authorize", t, {}),
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.OAuth.e9a32f5a.js.map
