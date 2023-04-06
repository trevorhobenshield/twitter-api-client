"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.AccountVerification"],
  {
    91976: (e, t, n) => {
      n.r(t), n.d(t, { default: () => i });
      const i = ({ apiClient: e, featureSwitches: t }) => ({
        fetchAccess: (t = {}, n = {}) =>
          e.getUnversioned("/verify/1.0/access", t, n),
        fetchAccountEligibility: (t = {}, n = {}) =>
          e.getUnversioned("/verify/1.0/account-eligibility", t, n),
        fetchAccountViolations: (t = {}, n = {}) =>
          e.getUnversioned("/verify/1.0/badge-violation/violations", t, n),
        fetchAuthenticationResult: (t = {}, n = {}) =>
          e.getUnversioned("/verify/1.0/id-document", t, n),
        fetchBadgeViolations: (t = {}, n = {}) =>
          e.getUnversioned("/verify/1.0/badge-violation", t, n),
        fetchDocumentFormats: (t = {}, n = {}) =>
          e.getUnversioned("/verify/1.0/document-formats", t, n),
        verifyAccount: (t, n = {}) =>
          e.postUnversioned("/verify/1.0/intake", t, {
            ...n,
            "content-type": "application/json",
          }),
        verifyIdDocument(t, n = {}) {
          const i = { ...n, "content-type": "multipart/form-data" },
            { backImage: o, country: c, frontImage: r, idType: a } = t,
            s = new FormData();
          return (
            a && s.append("id_type", a),
            c && s.append("country", c),
            o && s.append("back", o),
            r && s.append("front", r),
            e.postUnversioned("/verify/1.0/id-document", s, i)
          );
        },
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.AccountVerification.8eac276a.js.map
