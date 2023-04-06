(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Settings", "endpoints.Users"],
  {
    69685: (e) => {
      e.exports = {
        queryId: "g2m0pAOamawNtVIfjXNMJg",
        operationName: "DisableVerifiedPhoneLabel",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    62152: (e) => {
      e.exports = {
        queryId: "C3RJFfMsb_KcEytpKmRRkw",
        operationName: "EnableVerifiedPhoneLabel",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    20784: (e) => {
      e.exports = {
        queryId: "5kUWP8C1hcd6omvg6HXXTQ",
        operationName: "ProfileUserPhoneState",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    27141: (e) => {
      e.exports = {
        queryId: "vJ-XatpmQSG8bDch8-t9Jw",
        operationName: "UserSessionsList",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    98084: (e, t, n) => {
      "use strict";
      n.r(t), n.d(t, { default: () => g });
      var o = n(6899),
        s = n(69685),
        r = n.n(s),
        i = n(62152),
        a = n.n(i),
        c = n(20784),
        l = n.n(c),
        u = n(27141),
        d = n.n(u);
      const _ = new o.fK.Entity("applications", {}, { idAttribute: "token" });
      var p = n(13239),
        f = n(55371);
      const h = {
          include_mention_filter: !0,
          include_nsfw_user_flag: !0,
          include_nsfw_admin_flag: !0,
          include_ranked_timeline: !0,
          include_alt_text_compose: !0,
        },
        g = ({ apiClient: e, featureSwitches: t }) => ({
          fetch(n, o) {
            const s = t.isTrue(
                "voice_rooms_sharing_listening_data_with_followers_setting_enabled"
              )
                ? {
                    include_ext_sharing_audiospaces_listening_data_with_followers:
                      !0,
                  }
                : {},
              r = t.isTrue("toxic_reply_filter_inline_callout_enabled")
                ? { include_ext_reply_filter_setting: !0 }
                : {},
              i = {
                ext: "ssoConnections",
                include_country_code: !0,
                include_ext_dm_nsfw_media_filter: !0,
              },
              a = Object.assign({}, h, i, s, r, n);
            return e.get("account/settings", a, o);
          },
          fetchRateLimits: (t, n) =>
            e.get("application/rate_limit_status", t, n || {}),
          fetchHashflags: () => e.get("hashflags", {}, {}),
          update(t, n) {
            const o = Object.assign({}, h, t);
            return e.post("account/settings", o, {}, n);
          },
          deleteSSOConnection(t, n) {
            const { ssoProvider: o } = t;
            return e.post(
              "sso/delete_connection",
              { sso_provider: o },
              {},
              n,
              ""
            );
          },
          deleteLocationData: (t, n) =>
            e.post("geo/delete_location_data", t, {}, n),
          deleteContacts: (t, n) => e.post("contacts/destroy/all", t, {}, n),
          fetchNotificationFilters: (t, n) =>
            e.get("mutes/advanced_filters", t, n || {}),
          updateNotificationFilters: (t, n) =>
            e.post("mutes/advanced_filters", t, {}, n || {}),
          updateProfile: (t, n) =>
            e
              .post("account/update_profile", t, {}, n)
              .then((e) => (0, o.Fv)(e, p.Z)),
          removeProfileBanner(n, o) {
            const s = Object.assign(
              {},
              f.getGlobalDefaults(t),
              { return_user: !0 },
              n
            );
            return e.post("account/remove_profile_banner", s, {}, o);
          },
          updateProfileAvatar(n, o) {
            const s = Object.assign(
              {},
              f.getGlobalDefaults(t),
              { return_user: !0 },
              n
            );
            return e.post("account/update_profile_image", s, {}, o);
          },
          updateProfileBanner(n, o) {
            const s = Object.assign(
              {},
              f.getGlobalDefaults(t),
              { return_user: !0 },
              n
            );
            return e.post("account/update_profile_banner", s, {}, o);
          },
          fetchPlaceTrendSettings: (t, n) =>
            e.getURT("guide/get_explore_settings", t, n || {}),
          updatePlaceTrendSettings: (t, n) =>
            e.postURT("guide/set_explore_settings", { ...t }, {}, n || {}),
          usernameAvailable: (t, n) =>
            e.dispatch({
              path: "/i/users/username_available.json",
              method: "GET",
              params: t,
              headers: n || {},
            }),
          fetchApplications: (t, n) =>
            e
              .get("oauth/list", t, n)
              .then((e) => (0, o.Fv)(e, { applications: [_] })),
          revokeApplication: (t, n) => e.post("oauth/revoke", t, {}, n),
          revokeOauth2Token: (t, n) =>
            e.postUnversioned("/2/oauth2/revoke_token_hash", t, n),
          changePassword: (t, n) =>
            e.postI("account/change_password", t, n || {}),
          deactivate(t, n) {
            const { deactivation_timespan: o, password: s } = t;
            return e.post(
              "account/deactivate",
              { current_password: s, deactivation_timespan: o },
              {},
              n
            );
          },
          fetchWoeTrendsLocations: (t, n) =>
            e.get("trends/available", t, n || {}),
          fetchPlaceTrendsLocations: (t, n) =>
            e.getURT("guide/explore_locations_with_auto_complete", t, n || {}),
          fetchLoginVerificationSettings(t, n) {
            const { userId: o, ...s } = t;
            return o
              ? e.get(
                  `strato/column/User/${o}/account-security/twoFactorAuthSettings2`,
                  s,
                  n || {},
                  ""
                )
              : Promise.resolve(new Response());
          },
          fetchBackupCode: (t, n) => e.get("account/backup_code", t, n || {}),
          fetchNewBackupCode: (t, n) =>
            e.post("account/backup_code", t, {}, n || {}),
          fetchTemporaryPassword: (t, n) =>
            e.post(
              "account/login_verification/temporary_password",
              t,
              {},
              n || {}
            ),
          fetchSessions: (t, n) => e.graphQL(d(), {}),
          enableVerifiedPhoneLabel: () =>
            t.isTrue("verified_phone_label_enabled")
              ? e.graphQL(a(), {})
              : Promise.resolve(),
          disableVerifiedPhoneLabel: (n, o) =>
            t.isTrue("verified_phone_label_enabled")
              ? e.graphQL(r(), {})
              : Promise.resolve(),
          fetchUserProfilePhoneState: (t, n) => e.graphQL(l(), {}),
          revokeSession: (t, n) =>
            e.postUnversioned("/account/sessions/revoke", t, n),
          revokeAllSessions: (t, n) =>
            e.postUnversioned("/account/sessions/revoke_all", t, n),
          enrollIn2FA: (t, n) => e.post("bouncer/opt_in", t, {}, n || {}),
          disable2FA: (t, n) =>
            e.delete("account/login_verification_enrollment", t, n || {}),
          disable2FAMethod: (t, n) =>
            e.post("account/login_verification/remove_method", t, {}, n || {}),
          rename2FASecurityKey: (t, n) =>
            e.post(
              "account/login_verification/rename_security_key_method",
              t,
              {},
              n
            ),
          verifyPassword(t, n) {
            const { password: o } = t;
            return e.post("account/verify_password", { password: o }, {}, n);
          },
        });
    },
    55371: (e, t, n) => {
      "use strict";
      n.r(t), n.d(t, { default: () => u, getGlobalDefaults: () => a });
      var o = n(6899),
        s = n(70151),
        r = n(13239),
        i = n(60348);
      const a = (e) => {
          const t = e.isTrue(
              "responsive_web_twitter_blue_verified_badge_is_enabled"
            ),
            n = e.isTrue("blue_business_consumption_api_enabled");
          return {
            include_profile_interstitial_type: 1,
            include_blocking: 1,
            include_blocked_by: 1,
            include_followed_by: 1,
            include_want_retweets: 1,
            include_mute_edge: 1,
            include_can_dm: 1,
            include_can_media_tag: 1,
            include_ext_has_nft_avatar: 1,
            ...(0, s.Z)(t ? { include_ext_is_blue_verified: 1 } : null),
            ...(0, s.Z)(n ? { include_ext_verified_type: 1 } : null),
            skip_status: 1,
          };
        },
        c = (e) => (0, o.Fv)(e, r.Z),
        l = (e) => (0, o.Fv)(e, [r.Z]),
        u = ({ apiClient: e, featureSwitches: t }) => ({
          fetchUsers: (n, o = {}) =>
            e.get("users/lookup", { ...a(t), ...n }, o).then(l),
          follow(n, o = {}) {
            const { id_str: s, promotedContent: r, ...l } = n,
              u = (0, i.cL)(r);
            return e
              .post(
                "friendships/create",
                { ...a(t), ...u, user_id: s, ...l },
                {},
                o
              )
              .then(c);
          },
          unfollow(n, o = {}) {
            const { id_str: s, promotedContent: r, ...l } = n,
              u = (0, i.cL)(r);
            return e
              .post(
                "friendships/destroy",
                { ...a(t), ...u, user_id: s, ...l },
                {},
                o
              )
              .then(c);
          },
          cancelPendingFollow(t, n = {}) {
            const { id_str: o, ...s } = t;
            return e
              .post("friendships/cancel", { ...s, user_id: o }, {}, n)
              .then(c);
          },
          block(t, n = {}) {
            const { id_str: o, promotedContent: s, ...r } = t,
              a = (0, i.cL)(s);
            return e
              .post("blocks/create", { ...a, user_id: o, ...r }, {}, n)
              .then(c);
          },
          unblock(t, n = {}) {
            const { id_str: o, promotedContent: s, ...r } = t,
              a = (0, i.cL)(s);
            return e
              .post("blocks/destroy", { ...a, user_id: o, ...r }, {}, n)
              .then(c);
          },
          mute(t, n = {}) {
            const { id_str: o, promotedContent: s, ...r } = t,
              a = (0, i.cL)(s);
            return e
              .post("mutes/users/create", { ...a, user_id: o, ...r }, {}, n)
              .then(c);
          },
          unmute(t, n = {}) {
            const { id_str: o, promotedContent: s, ...r } = t,
              a = (0, i.cL)(s);
            return e
              .post("mutes/users/destroy", { ...a, user_id: o, ...r }, {}, n)
              .then(c);
          },
          fetchProfileTranslation(t, n = {}) {
            const { profileUserId: o } = t;
            return e.get(
              `strato/column/None/profileUserId=${o},destinationLanguage=None,translationSource=Some(Google)/translation/service/translateProfile`,
              {},
              n,
              ""
            );
          },
        });
    },
    60348: (e, t, n) => {
      "use strict";
      n.d(t, { cL: () => r, gQ: () => i });
      const o = Object.freeze({});
      function s(e) {
        const { conversational_card_details: t } = e;
        return t ? { conversational_card_details: t } : void 0;
      }
      function r(e) {
        if (!e) return o;
        const { disclosure_type: t, impression_id: n } = e,
          r = "earned" === a(e),
          i = JSON.stringify(s(e));
        if (!t || !n) return o;
        let c = { impression_id: n };
        return (
          i && (c = { ...c, engagement_metadata: i }),
          r && (c = { ...c, earned: 1 }),
          c
        );
      }
      function i(e) {
        if (!e) return;
        const { disclosure_type: t, impression_id: n } = e,
          o = "earned" === a(e),
          r = s(e);
        if (!t || !n) return;
        let i = { impression_id: n };
        return (
          r && (i = { ...i, engagement_metadata: r }),
          o && (i = { ...i, earned: !0 }),
          { engagement_request: { ...i } }
        );
      }
      function a(e) {
        const t = null == e ? void 0 : e.disclosure_type;
        return t && t.toLowerCase();
      }
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Settings.0a7f4c4a.js.map
