(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.PinnedReplies"],
  {
    27366: (e) => {
      e.exports = {
        queryId: "GA2_1uKP9b_GyR4MVAQXAw",
        operationName: "PinReply",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    93137: (e) => {
      e.exports = {
        queryId: "iRe6ig5OV1EzOtldNIuGDQ",
        operationName: "UnpinReply",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    45808: (e, t, n) => {
      "use strict";
      n.r(t), n.d(t, { default: () => u });
      var i = n(27366),
        s = n.n(i),
        a = n(93137),
        r = n.n(a);
      const u = ({ apiClient: e, featureSwitches: t }) => ({
        pin: (t) =>
          e.graphQL(s(), t).then((e) => {
            var t, n;
            return {
              success:
                null !=
                  (t =
                    null == e ||
                    null == (n = e.create_conversation_pinned_tweet)
                      ? void 0
                      : n.success) && t,
            };
          }),
        unpin: (t) =>
          e.graphQL(r(), t).then((e) => {
            var t, n;
            return {
              success:
                null !=
                  (t =
                    null == e ||
                    null == (n = e.delete_conversation_pinned_tweet)
                      ? void 0
                      : n.success) && t,
            };
          }),
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.PinnedReplies.37a1eb9a.js.map
