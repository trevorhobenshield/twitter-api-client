"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Validity"],
  {
    10134: (e, a, s) => {
      s.r(a), s.d(a, { default: () => u });
      var i = s(6899),
        t = s(73228),
        l = s.n(t);
      const r = l().d5568440,
        n = l().d0511fe6,
        d = l().cd24fe60,
        o = new i.fK.Entity(
          "emailValidity",
          {},
          {
            processStrategy: (e) => ({
              valid: e.valid,
              errorMessage: e.valid ? "" : e.msg,
            }),
          }
        ),
        p = new i.fK.Entity(
          "passwordValidity",
          {},
          {
            processStrategy: (e) => ({
              valid: e.pass,
              errorMessage: e.pass ? "" : r,
            }),
          }
        ),
        v = new i.fK.Entity(
          "phoneNumberValidity",
          {},
          {
            processStrategy: (e) => ({
              valid: e.valid && e.available,
              errorMessage: e.valid ? (e.available ? "" : n) : d,
            }),
          }
        ),
        u = ({ apiClient: e, featureSwitches: a }) => ({
          fetchPasswordStrength: (a, s) =>
            e
              .post("account/password_strength", a, {}, null != s ? s : {})
              .then((e) => ((e) => (0, i.Fv)(e, p))({ ...e, id: a.password })),
          isPhoneNumberAvailable: (a, s) =>
            e
              .get("users/phone_number_available", a, null != s ? s : {})
              .then((e) =>
                ((e) => (0, i.Fv)(e, v))({ ...e, id: a.raw_phone_number })
              ),
          isEmailAvailable: (a, s) =>
            e
              .getI("users/email_available", a, null != s ? s : {})
              .then((e) => ((e) => (0, i.Fv)(e, o))({ ...e, id: a.email })),
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Validity.82b4706a.js.map
