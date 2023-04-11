"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.PromotedContent"],
  {
    73842: (e, t, n) => {
      n.r(t), n.d(t, { default: () => i });
      var s = n(85586),
        o = n(63140);
      const r = [o.ZP.CurrentUserSuspended, o.ZP.AccessDeniedByBouncer];
      function c(e) {
        if (!(0, s.Z)(r, (t) => (0, o.VZ)(e, t))) throw e;
      }
      const i = ({ apiClient: e, featureSwitches: t }) => ({
        log: (t, n = {}) => e.post("promoted_content/log", t, {}, n).catch(c),
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.PromotedContent.5193e53a.js.map
