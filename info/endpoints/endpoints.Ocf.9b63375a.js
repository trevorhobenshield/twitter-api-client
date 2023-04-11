"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Ocf"],
  {
    66660: (t, n, o) => {
      o.r(n), o.d(n, { default: () => a });
      o(6886), o(14121), o(60523);
      var e = o(56642);
      const a = ({ apiClient: t, featureSwitches: n }) => ({
        task(n = {}, o = {}) {
          const { flow_name: e, test_country_code: a, ...s } = n;
          return t.post(
            "onboarding/task",
            s,
            { flow_name: e, test_country_code: a },
            { ...o, "content-type": "application/json" }
          );
        },
        syncContacts(n) {
          const { callback_url: o, ...e } = n;
          return t.post(
            "onboarding/contacts_authorize",
            { callback_url: o, import_params: e },
            {},
            { "content-type": "application/json" }
          );
        },
        getContactsImportStatus: (n) =>
          t.get(
            "onboarding/contacts_import_status",
            { options: n },
            { "content-type": "application/json" }
          ),
        getVerificationStatus: (n) =>
          t.get("onboarding/verification_status", n, {
            "content-type": "application/json",
          }),
        callInteractiveSpinnerPath: (n) =>
          t.get(`${n}`, {}, { "content-type": "application/json" }, ""),
        callOnboardingPath(n, o) {
          const a = new URL(n, "https://twitter.com"),
            s = a.pathname.substring(1),
            i = e.parse(a.searchParams.toString());
          return t.post(
            `onboarding/${s}`,
            { ...i, ...o },
            {},
            { "content-type": "application/json" },
            ""
          );
        },
        referer: (n) =>
          t.post(
            "onboarding/referrer",
            n,
            {},
            { "content-type": "application/json" }
          ),
        removeContacts: (n) => t.post("contacts/destroy/all", n, {}, {}),
        setUserPwaLaunched(n) {
          const { userId: o } = n;
          return t.put(
            `strato/column/User/${o}/onboarding/hasLaunchedPWA`,
            "true",
            { "content-type": "application/json" },
            ""
          );
        },
        verifyUserIdentifier: (n) =>
          t.post(
            "onboarding/begin_verification",
            n,
            {},
            { "content-type": "application/json" }
          ),
        verificationLink: (n = {}) =>
          t.post(
            "onboarding/verify",
            n,
            {},
            { "content-type": "application/json" }
          ),
        getBrowsableNuxRecommendations: (n) =>
          t.post(
            "onboarding/fetch_user_recommendations",
            n,
            {},
            { "content-type": "application/json" }
          ),
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Ocf.9b63375a.js.map
