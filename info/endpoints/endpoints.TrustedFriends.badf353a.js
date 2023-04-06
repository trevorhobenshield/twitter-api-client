(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.TrustedFriends"],
  {
    30474: (e) => {
      e.exports = {
        queryId: "QjN8ZdavFDqxUjNn3r9cig",
        operationName: "AuthenticatedUserTFLists",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    21037: (e) => {
      e.exports = {
        queryId: "2tP8XUYeLHKjq5RHvuvpZw",
        operationName: "CreateTrustedFriendsList",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    75323: (e, t, s) => {
      "use strict";
      s.r(t), s.d(t, { default: () => u });
      var r = s(17360),
        i = s(30474),
        a = s.n(i),
        n = s(21037),
        d = s.n(n);
      const u = ({ apiClient: e, featureSwitches: t }) => ({
        fetchAuthenticatedUserTFLists: () =>
          e
            .graphQL(
              a(),
              {},
              (0, r.kj)(
                (e) =>
                  !(null != e && e.authenticated_user_trusted_friends_lists),
                "GQL Trusted Friends: Failed to fetch trusted friends lists"
              )
            )
            .then((e) => e),
        createTrustedFriendsList: () =>
          e
            .graphQL(
              d(),
              {},
              (0, r.kj)(
                (e) => !(null != e && e.trusted_friends_list_create),
                "GQL Trusted Friends: Failed to create trusted friends list"
              )
            )
            .then((e) => e),
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.TrustedFriends.badf353a.js.map
