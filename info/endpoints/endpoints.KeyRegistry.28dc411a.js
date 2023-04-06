"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.KeyRegistry"],
  {
    98420: (e, t, s) => {
      s.r(t), s.d(t, { default: () => r });
      const r = ({ apiClient: e, featureSwitches: t }) => ({
        register: ({ device_id: s, ...r }) =>
          e.post(
            "keyregistry/register",
            r,
            {
              dm_secret_conversations_enabled: t.isTrue(
                "dm_secret_conversations_enabled"
              ),
              krs_registration_enabled: t.isTrue("krs_registration_enabled"),
            },
            { "X-Client-UUID": s, "content-type": "application/json" },
            ""
          ),
        extractPublicKeys: ({ device_id: s, user_id: r }) =>
          e.get(
            `keyregistry/extract_public_keys/${r}`,
            {
              dm_secret_conversations_enabled: t.isTrue(
                "dm_secret_conversations_enabled"
              ),
              krs_registration_enabled: t.isTrue("krs_registration_enabled"),
            },
            { "X-Client-UUID": s },
            ""
          ),
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.KeyRegistry.28dc411a.js.map
