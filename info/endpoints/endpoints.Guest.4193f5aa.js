"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Guest"],
  {
    61041: (e, t, s) => {
      s.r(t), s.d(t, { default: () => n });
      const n = ({ apiClient: e, featureSwitches: t }) => ({
        fetchGuestSegment(s, n = {}) {
          const r = t.getValueWithoutScribeImpression(
            "responsive_web_logged_out_gating_non_impressing_member_segments"
          );
          return Array.isArray(r) && r.length > 0
            ? e.get("rux/logged_out/segmentations", s, n).then(
                (e) => e.segmentation,
                (e) => {}
              )
            : Promise.resolve();
        },
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Guest.4193f5aa.js.map
