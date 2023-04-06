(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.LegacyAndUnifiedCards"],
  {
    47546: (e) => {
      e.exports = {
        queryId: "VQDRJthjTcSKzwONpVGd3w",
        operationName: "CardPreviewByTweetText",
        operationType: "query",
        metadata: {
          featureSwitches: [
            "responsive_web_enhance_cards_enabled",
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_exclude_directive_enabled",
            "verified_phone_label_enabled",
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled",
            "responsive_web_graphql_timeline_navigation_enabled",
          ],
        },
      };
    },
    50269: (e, r, a) => {
      "use strict";
      a.r(r), a.d(r, { default: () => u });
      a(71372);
      var t = a(6899),
        i = a(69114),
        n = a(62707),
        d = a(46395),
        s = a(15804),
        _ = a(90650);
      const c = new t.fK.Entity(
        "legacyAndUnifiedCards",
        {},
        {
          processStrategy: (e, r, a) => {
            var t, i;
            const _ = {};
            if (
              ("HasCard" ===
                (null == (t = e.unified_card) ? void 0 : t.card_fetch_state) &&
                (_.unifiedCard = (0, d.Z)(e.unified_card, r, a)),
              null != (i = e.card) && i.legacy)
            ) {
              const t = (0, s.n)(e.card.legacy);
              _.legacyCard = (0, n.Z)(t, r, a);
            }
            return _;
          },
          idAttribute: "id",
        }
      );
      c.define({ users: new t.fK.Values(_.Z) });
      const o = c;
      var p = a(47546),
        l = a.n(p);
      function w(e, r, a, n) {
        const { url: d } = r,
          { retryDelay: s, retryMax: _ } = n;
        return a >= _
          ? Promise.reject(
              new Error(
                `retry limit of ${_} reached when fetching card preview for ${d} from graphql`
              )
            )
          : e
              .graphQL(l(), { tweetText: d })
              .then((_) =>
                _.card_preview
                  ? "Crawling" === _.card_preview.state
                    ? (0, i.Z)(s).then(() => w(e, r, a + 1, n))
                    : "CardNotFound" === _.card_preview.state
                    ? Promise.resolve({ result: !1 })
                    : _.card_preview.state
                    ? Promise.reject(
                        new Error(
                          `received state of ${_.card_preview.state} when fetching card preview for ${d}`
                        )
                      )
                    : (0, t.Fv)({ ..._.card_preview, id: d }, o)
                  : Promise.reject(
                      new Error(
                        `received undefined card_preview payload when fetching a card preview for ${d}`
                      )
                    )
              );
      }
      const u = ({ apiClient: e, featureSwitches: r }) => ({
        fetchCardPreview: (a, t) =>
          w(e, a, 0, {
            retryDelay: r.getNumberValue(
              "card_compose_preview_retry_after_ms",
              3e3
            ),
            retryMax: r.getNumberValue("card_compose_preview_retry_max", 5),
          }),
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.LegacyAndUnifiedCards.4e86581a.js.map
