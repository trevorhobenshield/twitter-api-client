"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.KeyRegistry"],
  {
    98420: (e, t, s) => {
      s.r(t), s.d(t, { default: () => i });
      s(6886), s(67694);
      const i = ({ apiClient: e, featureSwitches: t }) => ({
        register: ({ device_id: s, ...i }) =>
          e.post(
            "keyregistry/register",
            i,
            {
              dm_secret_conversations_enabled: t.isTrue(
                "dm_secret_conversations_enabled"
              ),
              krs_registration_enabled: t.isTrue("krs_registration_enabled"),
            },
            { "X-Client-UUID": s, "content-type": "application/json" },
            ""
          ),
        extractPublicKeys: (s = []) =>
          Promise.all(
            s.map((s) =>
              e
                .get(
                  `keyregistry/extract_public_keys/${s}`,
                  {
                    dm_secret_conversations_enabled: t.isTrue(
                      "dm_secret_conversations_enabled"
                    ),
                    krs_registration_enabled: t.isTrue(
                      "krs_registration_enabled"
                    ),
                  },
                  {},
                  ""
                )
                .then(({ public_keys: e = [] }) =>
                  e.map(({ identity_key: e, ...t }) => ({
                    user_id: s,
                    identity_key: e,
                    ...t,
                  }))
                )
            )
          ).then((e) => e.flat()),
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.KeyRegistry.c9073cea.js.map
