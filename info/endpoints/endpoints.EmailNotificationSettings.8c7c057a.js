(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.EmailNotificationSettings"],
  {
    61537: (e) => {
      e.exports = {
        queryId: "2qKKYFQift8p5-J1k6kqxQ",
        operationName: "WriteEmailNotificationSettings",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    29544: (e) => {
      e.exports = {
        queryId: "JpjlNgn4sLGvS6tgpTzYBg",
        operationName: "ViewerEmailSettings",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    6382: (e, t, i) => {
      "use strict";
      i.r(t), i.d(t, { default: () => u });
      var n = i(72599),
        r = i(61537),
        s = i.n(r),
        a = i(29544),
        o = i.n(a);
      const u = ({ apiClient: e, featureSwitches: t }) => ({
        fetch: () =>
          e.graphQL(o(), {}).then((e) => {
            let t;
            if (e.viewer) {
              var i;
              const { user_results: n } = e.viewer;
              "User" ===
                (null == n || null == (i = n.result) ? void 0 : i.__typename) &&
                (t = n.result.notifications_email_notifications);
            }
            return (
              t ||
                (0, n.ZP)(
                  "GraphQL email notification settings query returned no settings object."
                ),
              t || {}
            );
          }),
        update(t) {
          const { settings: i, userId: n } = t;
          return e.graphQL(s(), { userId: n, settings: i });
        },
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.EmailNotificationSettings.8c7c057a.js.map
