"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Devices"],
  {
    47876: (e, s, t) => {
      t.r(s), t.d(s, { default: () => n });
      const n = ({ apiClient: e, featureSwitches: s }) => ({
        fetchDevicePermissionsState(s) {
          const { deviceId: t, permissionName: n, userId: o, ...i } = s;
          return o
            ? e.get(
                `strato/column/None/${o},${encodeURIComponent(
                  t
                )},${n}/clients/permissionsState`,
                i,
                { "content-type": "application/json" },
                ""
              )
            : Promise.resolve(new Response());
        },
        fetchInfo: (s) => e.get("users/email_phone_info", s, {}),
        resendConfirmationEmail: () =>
          e.post("account/resend_confirmation_email", {}, {}, {}),
        removeDevice: (s) => e.post("device/unregister", s, {}, {}),
        updateDevicePermissionsState(s) {
          const { deviceId: t, permissionName: n, userId: o } = s;
          return o
            ? e.put(
                `strato/column/None/${o},${encodeURIComponent(
                  t
                )},${n}/clients/permissionsState`,
                s,
                { "content-type": "application/json" },
                ""
              )
            : Promise.resolve(new Response());
        },
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Devices.422f010a.js.map
