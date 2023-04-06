(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Settings"],
  {
    22001: (e) => {
      e.exports = {
        queryId: "g2m0pAOamawNtVIfjXNMJg",
        operationName: "DisableVerifiedPhoneLabel",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    67065: (e) => {
      e.exports = {
        queryId: "C3RJFfMsb_KcEytpKmRRkw",
        operationName: "EnableVerifiedPhoneLabel",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    19874: (e) => {
      e.exports = {
        queryId: "5kUWP8C1hcd6omvg6HXXTQ",
        operationName: "ProfileUserPhoneState",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    58043: (e) => {
      e.exports = {
        queryId: "vJ-XatpmQSG8bDch8-t9Jw",
        operationName: "UserSessionsList",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    98084: (e, t, o) => {
      "use strict";
      o.r(t), o.d(t, { default: () => g });
      var a = o(6899),
        s = o(22001),
        n = o.n(s),
        i = o(67065),
        r = o.n(i),
        c = o(19874),
        l = o.n(c),
        u = o(58043),
        p = o.n(u);
      const _ = new a.fK.Entity("applications", {}, { idAttribute: "token" });
      var d = o(13239),
        f = o(55371);
      const h = {
          include_mention_filter: !0,
          include_nsfw_user_flag: !0,
          include_nsfw_admin_flag: !0,
          include_ranked_timeline: !0,
          include_alt_text_compose: !0,
        },
        g = ({ apiClient: e, featureSwitches: t }) => ({
          fetch(o, a) {
            const s = t.isTrue(
                "voice_rooms_sharing_listening_data_with_followers_setting_enabled"
              )
                ? {
                    include_ext_sharing_audiospaces_listening_data_with_followers:
                      !0,
                  }
                : {},
              n = t.isTrue("toxic_reply_filter_inline_callout_enabled")
                ? { include_ext_reply_filter_setting: !0 }
                : {},
              i = {
                ext: "ssoConnections",
                include_country_code: !0,
                include_ext_dm_nsfw_media_filter: !0,
              },
              r = Object.assign({}, h, i, s, n, o);
            return e.get("account/settings", r, a);
          },
          fetchRateLimits: (t, o) =>
            e.get("application/rate_limit_status", t, o || {}),
          fetchHashflags: () => e.get("hashflags", {}, {}),
          update(t, o) {
            const a = Object.assign({}, h, t);
            return e.post("account/settings", a, {}, o);
          },
          deleteSSOConnection(t, o) {
            const { ssoProvider: a } = t;
            return e.post(
              "sso/delete_connection",
              { sso_provider: a },
              {},
              o,
              ""
            );
          },
          deleteLocationData: (t, o) =>
            e.post("geo/delete_location_data", t, {}, o),
          deleteContacts: (t, o) => e.post("contacts/destroy/all", t, {}, o),
          fetchNotificationFilters: (t, o) =>
            e.get("mutes/advanced_filters", t, o || {}),
          updateNotificationFilters: (t, o) =>
            e.post("mutes/advanced_filters", t, {}, o || {}),
          updateProfile: (t, o) =>
            e
              .post("account/update_profile", t, {}, o)
              .then((e) => (0, a.Fv)(e, d.Z)),
          removeProfileBanner(o, a) {
            const s = Object.assign(
              {},
              f.getGlobalDefaults(t),
              { return_user: !0 },
              o
            );
            return e.post("account/remove_profile_banner", s, {}, a);
          },
          updateProfileAvatar(o, a) {
            const s = Object.assign(
              {},
              f.getGlobalDefaults(t),
              { return_user: !0 },
              o
            );
            return e.post("account/update_profile_image", s, {}, a);
          },
          updateProfileBanner(o, a) {
            const s = Object.assign(
              {},
              f.getGlobalDefaults(t),
              { return_user: !0 },
              o
            );
            return e.post("account/update_profile_banner", s, {}, a);
          },
          fetchPlaceTrendSettings: (t, o) =>
            e.getURT("guide/get_explore_settings", t, o || {}),
          updatePlaceTrendSettings: (t, o) =>
            e.postURT("guide/set_explore_settings", { ...t }, {}, o || {}),
          usernameAvailable: (t, o) =>
            e.dispatch({
              path: "/i/users/username_available.json",
              method: "GET",
              params: t,
              headers: o || {},
            }),
          fetchApplications: (t, o) =>
            e
              .get("oauth/list", t, o)
              .then((e) => (0, a.Fv)(e, { applications: [_] })),
          revokeApplication: (t, o) => e.post("oauth/revoke", t, {}, o),
          revokeOauth2Token: (t, o) =>
            e.postUnversioned("/2/oauth2/revoke_token_hash", t, o),
          changePassword: (t, o) =>
            e.postI("account/change_password", t, o || {}),
          deactivate(t, o) {
            const { deactivation_timespan: a, password: s } = t;
            return e.post(
              "account/deactivate",
              { current_password: s, deactivation_timespan: a },
              {},
              o
            );
          },
          fetchWoeTrendsLocations: (t, o) =>
            e.get("trends/available", t, o || {}),
          fetchPlaceTrendsLocations: (t, o) =>
            e.getURT("guide/explore_locations_with_auto_complete", t, o || {}),
          fetchLoginVerificationSettings(t, o) {
            const { userId: a, ...s } = t;
            return a
              ? e.get(
                  `strato/column/User/${a}/account-security/twoFactorAuthSettings2`,
                  s,
                  o || {},
                  ""
                )
              : Promise.resolve(new Response());
          },
          fetchBackupCode: (t, o) => e.get("account/backup_code", t, o || {}),
          fetchNewBackupCode: (t, o) =>
            e.post("account/backup_code", t, {}, o || {}),
          fetchTemporaryPassword: (t, o) =>
            e.post(
              "account/login_verification/temporary_password",
              t,
              {},
              o || {}
            ),
          fetchSessions: (t, o) => e.graphQL(p(), {}),
          enableVerifiedPhoneLabel: () =>
            t.isTrue("verified_phone_label_enabled")
              ? e.graphQL(r(), {})
              : Promise.resolve(),
          disableVerifiedPhoneLabel: (o, a) =>
            t.isTrue("verified_phone_label_enabled")
              ? e.graphQL(n(), {})
              : Promise.resolve(),
          fetchUserProfilePhoneState: (t, o) => e.graphQL(l(), {}),
          revokeSession: (t, o) =>
            e.postUnversioned("/account/sessions/revoke", t, o),
          revokeAllSessions: (t, o) =>
            e.postUnversioned("/account/sessions/revoke_all", t, o),
          enrollIn2FA: (t, o) => e.post("bouncer/opt_in", t, {}, o || {}),
          disable2FA: (t, o) =>
            e.delete("account/login_verification_enrollment", t, o || {}),
          disable2FAMethod: (t, o) =>
            e.post("account/login_verification/remove_method", t, {}, o || {}),
          rename2FASecurityKey: (t, o) =>
            e.post(
              "account/login_verification/rename_security_key_method",
              t,
              {},
              o
            ),
          verifyPassword(t, o) {
            const { password: a } = t;
            return e.post("account/verify_password", { password: a }, {}, o);
          },
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Settings.266bdcaa.js.map
