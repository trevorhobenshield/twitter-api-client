(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Commerce"],
  {
    99313: (e) => {
      e.exports = {
        queryId: "-lnNX56S2YrZYrLzbccFAQ",
        operationName: "LiveCommerceItemsSlice",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    54556: (e, t, i) => {
      "use strict";
      i.r(t), i.d(t, { default: () => m, isFatal: () => _ });
      var r = i(6899),
        s = i(72599),
        c = i(17360);
      const n = new r.fK.Entity(
        "commerceItems",
        {},
        {
          idAttribute: (e) => {
            var t, i;
            return null !=
              (t =
                null == (i = e.product_core_data)
                  ? void 0
                  : i.product_metadata.product_key)
              ? t
              : "";
          },
        }
      );
      var o = i(99313),
        l = i.n(o);
      const _ = (e, t) => {
          var i;
          const r =
            null == t || null == (i = t.live_event_by_rest_id)
              ? void 0
              : i.shop_grid_commerce_item_slice;
          return (
            r ||
              (0, s.ZP)(
                "GQL Live Commerce: Failed to fetch Live Commerce Slice"
              ),
            !r && (0, c.jB)(e)
          );
        },
        a = { result: [], entities: {}, slice_info: {} },
        m = ({ apiClient: e, featureSwitches: t }) => ({
          fetchLiveCommerceItemsSlice: (t) =>
            t
              ? e.graphQL(l(), t, _).then((e) => {
                  var t;
                  const i =
                    null == e || null == (t = e.live_event_by_rest_id)
                      ? void 0
                      : t.shop_grid_commerce_item_slice;
                  if (i) {
                    const { entities: e, result: t } = (0, r.Fv)(i.items, [n]);
                    return { result: t, entities: e, slice_info: i.slice_info };
                  }
                  return a;
                })
              : Promise.resolve(a),
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Commerce.a4648afa.js.map
