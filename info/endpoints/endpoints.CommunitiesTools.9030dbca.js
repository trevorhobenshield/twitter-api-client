(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.CommunitiesTools"],
  {
    61054: (e) => {
      e.exports = {
        queryId: "grMra5CiyVe9qUp2Ckv_gA",
        operationName: "CommunityCreateRule",
        operationType: "mutation",
        metadata: {
          featureSwitches: [
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_exclude_directive_enabled",
            "verified_phone_label_enabled",
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled",
            "responsive_web_graphql_timeline_navigation_enabled",
          ],
        },
      };
    },
    12235: (e) => {
      e.exports = {
        queryId: "PqF9tmZFUuIUQJBa1Yp6dA",
        operationName: "CommunityEditBannerMedia",
        operationType: "mutation",
        metadata: {
          featureSwitches: [
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_exclude_directive_enabled",
            "verified_phone_label_enabled",
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled",
            "responsive_web_graphql_timeline_navigation_enabled",
          ],
        },
      };
    },
    12773: (e) => {
      e.exports = {
        queryId: "vjJo0T_--jYPFIDmUJpywQ",
        operationName: "CommunityEditName",
        operationType: "mutation",
        metadata: {
          featureSwitches: [
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_exclude_directive_enabled",
            "verified_phone_label_enabled",
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled",
            "responsive_web_graphql_timeline_navigation_enabled",
          ],
        },
      };
    },
    3211: (e) => {
      e.exports = {
        queryId: "W3KRuCm_asI3kpnfGb-Yow",
        operationName: "CommunityEditPurpose",
        operationType: "mutation",
        metadata: {
          featureSwitches: [
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_exclude_directive_enabled",
            "verified_phone_label_enabled",
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled",
            "responsive_web_graphql_timeline_navigation_enabled",
          ],
        },
      };
    },
    11382: (e) => {
      e.exports = {
        queryId: "jZ0iF8Ej4iT9REu_5Bhbog",
        operationName: "CommunityEditRule",
        operationType: "mutation",
        metadata: {
          featureSwitches: [
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_exclude_directive_enabled",
            "verified_phone_label_enabled",
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled",
            "responsive_web_graphql_timeline_navigation_enabled",
          ],
        },
      };
    },
    4389: (e) => {
      e.exports = {
        queryId: "F9E0Gfuz47z9cHosrzp0Xg",
        operationName: "CommunityEditTheme",
        operationType: "mutation",
        metadata: {
          featureSwitches: [
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_exclude_directive_enabled",
            "verified_phone_label_enabled",
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled",
            "responsive_web_graphql_timeline_navigation_enabled",
          ],
        },
      };
    },
    36058: (e) => {
      e.exports = {
        queryId: "vhKogY1hNfXm7BHHN7lbWA",
        operationName: "CommunityRemoveBannerMedia",
        operationType: "mutation",
        metadata: {
          featureSwitches: [
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_exclude_directive_enabled",
            "verified_phone_label_enabled",
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled",
            "responsive_web_graphql_timeline_navigation_enabled",
          ],
        },
      };
    },
    44565: (e) => {
      e.exports = {
        queryId: "0SSCibJ7ZdA-UPBgTXg1Kw",
        operationName: "CommunityRemoveRule",
        operationType: "mutation",
        metadata: {
          featureSwitches: [
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_exclude_directive_enabled",
            "verified_phone_label_enabled",
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled",
            "responsive_web_graphql_timeline_navigation_enabled",
          ],
        },
      };
    },
    16786: (e) => {
      e.exports = {
        queryId: "y_e8QBHYvU6sGy_K0TFGoQ",
        operationName: "CommunityReorderRules",
        operationType: "mutation",
        metadata: {
          featureSwitches: [
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_exclude_directive_enabled",
            "verified_phone_label_enabled",
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled",
            "responsive_web_graphql_timeline_navigation_enabled",
          ],
        },
      };
    },
    40873: (e, i, n) => {
      "use strict";
      n.r(i), n.d(i, { default: () => x });
      var _ = n(6899),
        t = n(17360),
        a = n(83175),
        o = n(38269),
        r = n(61054),
        m = n.n(r),
        s = n(12235),
        u = n.n(s),
        l = n(12773),
        p = n.n(l),
        d = n(3211),
        b = n.n(d),
        c = n(11382),
        h = n.n(c),
        v = n(4389),
        y = n.n(v),
        g = n(36058),
        w = n.n(g),
        f = n(44565),
        q = n.n(f),
        I = n(16786),
        C = n.n(I);
      const x = ({ apiClient: e, featureSwitches: i }) => ({
        editCommunityName: (n) =>
          e
            .graphQL(
              p(),
              { communityId: n.communityId, name: n.name, ...(0, a.S)(i) },
              (0, t.kj)((e) => {
                var i;
                return !(null != (i = e.community_name_put) && i.name);
              }, "GQL Communities: Failed to edit community name")
            )
            .then((e) => (0, _.Fv)(e.community_name_put, o.ZP)),
        editCommunityPurpose: (n) =>
          e
            .graphQL(
              b(),
              {
                communityId: n.communityId,
                description: n.purpose,
                ...(0, a.S)(i),
              },
              (0, t.kj)((e) => {
                var i;
                return !(
                  null != (i = e.community_description_put) && i.description
                );
              }, "GQL Communities: Failed to edit community purpose")
            )
            .then((e) => (0, _.Fv)(e.community_description_put, o.ZP)),
        editCommunityTheme: (n) =>
          e
            .graphQL(
              y(),
              { communityId: n.communityId, theme: n.theme, ...(0, a.S)(i) },
              (0, t.kj)((e) => {
                var i;
                return !(
                  null != (i = e.community_custom_theme_put) && i.custom_theme
                );
              }, "GQL Communities: Failed to edit community theme")
            )
            .then((e) => (0, _.Fv)(e.community_custom_theme_put, o.ZP)),
        editCommunityRule: (n) =>
          e
            .graphQL(
              h(),
              {
                communityId: n.communityId,
                ruleId: n.ruleId,
                name: n.name,
                description: n.description,
                ...(0, a.S)(i),
              },
              (0, t.kj)(
                (e) => !(null != e && e.community_rule_update),
                "GQL Communities: Failed to edit community rule"
              )
            )
            .then((e) => (0, _.Fv)(e.community_rule_update, o.ZP)),
        createCommunityRule: (n) =>
          e
            .graphQL(
              m(),
              {
                communityId: n.communityId,
                name: n.name,
                description: n.description,
                ...(0, a.S)(i),
              },
              (0, t.kj)(
                (e) => !(null != e && e.community_rule_create),
                "GQL Communities: Failed to create community rule"
              )
            )
            .then((e) => (0, _.Fv)(e.community_rule_create, o.ZP)),
        removeCommunityRule: (n) =>
          e
            .graphQL(
              q(),
              { communityId: n.communityId, ruleId: n.ruleId, ...(0, a.S)(i) },
              (0, t.kj)(
                (e) => !(null != e && e.community_rule_remove),
                "GQL Communities: Failed to remove community rule"
              )
            )
            .then((e) => (0, _.Fv)(e.community_rule_remove, o.ZP)),
        reorderCommunityRules: (n) =>
          e
            .graphQL(
              C(),
              {
                communityId: n.communityId,
                ruleIds: n.ruleIds,
                ...(0, a.S)(i),
              },
              (0, t.kj)(
                (e) => !(null != e && e.community_rules_reorder),
                "GQL Communities: Failed to reorder community rules"
              )
            )
            .then((e) => (0, _.Fv)(e.community_rules_reorder, o.ZP)),
        editCommunityBannerMedia: (n) =>
          e
            .graphQL(
              u(),
              {
                communityId: n.communityId,
                mediaId: n.mediaId,
                ...(0, a.S)(i),
              },
              (0, t.kj)((e) => {
                var i;
                return !(
                  null != (i = e.community_custom_banner_media_put) &&
                  i.custom_banner_media
                );
              }, "GQL Communities: Failed to edit community banner media")
            )
            .then((e) => (0, _.Fv)(e.community_custom_banner_media_put, o.ZP)),
        removeCommunityBannerMedia: (n) =>
          e
            .graphQL(
              w(),
              { communityId: n.communityId, ...(0, a.S)(i) },
              (0, t.kj)(
                (e) => !e.community_custom_banner_media_delete,
                "GQL Communities: Failed to remove community banner media"
              )
            )
            .then((e) =>
              (0, _.Fv)(e.community_custom_banner_media_delete, o.ZP)
            ),
      });
    },
    83175: (e, i, n) => {
      "use strict";
      n.d(i, { S: () => o, d: () => a });
      var _ = n(60917),
        t = n.n(_);
      const a = (e) => {
          const i = e.isTrue("responsive_web_reactions_enabled");
          return {
            ...o(e),
            withDownvotePerspective: e.isTrue("rweb_reply_downvote_enabled"),
            withReactionsMetadata: i,
            withReactionsPerspective: i,
          };
        },
        o = (e) => t();
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.CommunitiesTools.9030dbca.js.map
