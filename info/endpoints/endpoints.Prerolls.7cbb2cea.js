"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Prerolls"],
  {
    50591: (e, t, r) => {
      r.r(t), r.d(t, { default: () => n });
      var i = r(48086);
      function s(e) {
        const t = { tweet_id: e.id_str },
          r = e.promoted_content && e.promoted_content.impression_id;
        return (
          r && (t.impression_id = r),
          e.card &&
            e.card.name === i.Z.CardNames.LIVE_EVENT &&
            (t.live_event_id = i.Z.getBindingValue(
              e.card.binding_values,
              "event_id"
            )),
          t
        );
      }
      const n = ({ apiClient: e, featureSwitches: t }) => ({
        fetch: (t) => {
          const r = { tweets: t.eligibleTweets.map(s) };
          t.trigger_preroll && (r.trigger_preroll = t.trigger_preroll),
            t.prerollDisplayLocation &&
              (r.display_location = t.prerollDisplayLocation);
          const i = { tweets: JSON.stringify(r) };
          return e.post("videoads/v2/prerolls", i, {}, {});
        },
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Prerolls.7cbb2cea.js.map
