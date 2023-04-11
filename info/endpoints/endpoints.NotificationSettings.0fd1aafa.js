"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.NotificationSettings"],
  {
    93886: (t, e, n) => {
      n.r(e), n.d(e, { default: () => l });
      n(6886);
      var i = n(60917),
        o = n.n(i),
        s = n(58314),
        c = n(59975);
      const a = { "content-type": "application/json" },
        p = () => {
          const { clientAppId: t } = (0, s.Z)();
          return { client_application_id: parseInt(t, 10) };
        },
        r = ({
          locale: t,
          subscription: e,
          templateChecksum: n,
          transport: i,
        }) => {
          const o = {
            ...(0, c.lX)(),
            checksum: n,
            env: 3,
            locale: t,
            protocol_version: 1,
          };
          return (
            e &&
              ((o.token = e.endpoint),
              e.keys &&
                ((o.encryption_key1 = e.keys.p256dh),
                (o.encryption_key2 = e.keys.auth))),
            o
          );
        },
        f = (t) => ({
          [`${t.transport}_device_info`]: r(t),
          ...(window.apkInterface ? p() : o()),
        }),
        l = ({ apiClient: t, featureSwitches: e }) => ({
          getNotificationSettingsLogin: (e, n) =>
            t.post("notifications/settings/login", f(e), {}, { ...a, ...n }),
          getNotificationSettings: (e, n) =>
            t.post("notifications/settings/checkin", f(e), {}, { ...a, ...n }),
          updateNotificationSettings(e, n) {
            const { settings: i, transport: o, ...s } = e,
              c = f({ transport: o, ...s });
            return t.post(
              "notifications/settings/save",
              {
                ...c,
                [`${o}_device_info`]: { ...c[`${o}_device_info`], settings: i },
              },
              {},
              { ...a, ...n }
            );
          },
          removePushDevices: (e, n) =>
            t.post(
              "notifications/settings/logout",
              { ...r(e), ...(window.apkInterface ? p() : o()) },
              {},
              { ...a, ...n }
            ),
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.NotificationSettings.0fd1aafa.js.map
