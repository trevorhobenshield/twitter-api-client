(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Typeahead"],
  {
    17883: (e) => {
      e.exports = {
        queryId: "NEwac2-8ONgf0756ne8oXA",
        operationName: "CommunityMemberRelationshipTypeahead",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    56667: (e) => {
      e.exports = {
        queryId: "gi_UGcUurYp6N6p2BaLJqQ",
        operationName: "CommunityUserRelationshipTypeahead",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    29337: (e) => {
      e.exports = {
        queryId: "RRnOwHttRGscWKC1zY9VRA",
        operationName: "TrustedFriendsTypeahead",
        operationType: "query",
        metadata: {
          featureSwitches: [
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_timeline_navigation_enabled",
          ],
        },
      };
    },
    43524: (e, t, r) => {
      "use strict";
      r.r(t), r.d(t, { default: () => b });
      var i = r(6899),
        s = r(70151),
        n = r(90968),
        _ = r(95212),
        a = r(45611);
      function u(e) {
        const {
          community_results: { rest_id: t },
          role: r,
          user_results: { result: i },
        } = e;
        if (!i || "User" !== i.__typename || !e) return;
        const { id: s, legacy: n, rest_id: _ } = i,
          a = null == n ? void 0 : n.screen_name;
        return a
          ? { id_str: `${t}_${_}`, role: r, user: { id: s, screen_name: a } }
          : void 0;
      }
      const l = new i.fK.Entity(a.L, {}, { idAttribute: "id_str" });
      var o = r(12006),
        d = r(17883),
        m = r.n(d),
        p = r(56667),
        c = r.n(p),
        y = r(29337),
        f = r.n(y);
      const h = (e) =>
          e
            .map((e) => {
              const { result: t } = e.user_results;
              if ("User" === (null == t ? void 0 : t.__typename) && t.legacy) {
                const e = t.legacy;
                return {
                  id_str: t.rest_id,
                  is_blue_verified: t.is_blue_verified,
                  profile_image_url_https: e.profile_image_url_https || "",
                  can_dm: e.can_dm || !1,
                  can_media_tag: e.can_media_tag || !1,
                  protected: e.protected || !1,
                  verified: e.verified || !1,
                  name: e.name || "",
                  screen_name: e.screen_name || "",
                };
              }
            })
            .filter(Boolean),
        b = ({ apiClient: e, featureSwitches: t }) => ({
          fetch(r, i = {}) {
            const n = t.isTrue(
                "responsive_web_twitter_blue_verified_badge_is_enabled"
              ),
              _ = t.isTrue("blue_business_consumption_api_enabled"),
              a = t.isTrue("blue_business_profile_image_shape_enabled"),
              u = {
                ...(0, s.Z)(n ? { include_ext_is_blue_verified: 1 } : null),
                ...(0, s.Z)(_ ? { include_ext_verified_type: 1 } : null),
                ...(0, s.Z)(a ? { include_ext_profile_image_shape: 1 } : null),
                ...r,
              };
            return e.get("search/typeahead", u, i);
          },
          fetchTrustedFriendsSuggestions: (t) =>
            e
              .graphQL(f(), {
                trustedFriendsId: t.trustedFriendsId,
                prefix: t.prefix,
              })
              .then((e) => ({
                events: [],
                ordered_sections: [],
                topics: [],
                users:
                  e.trusted_friends_list_by_rest_id.recommended_members_typeahead_results
                    .map((e) => {
                      const { result: t } = e;
                      if (
                        "User" === (null == t ? void 0 : t.__typename) &&
                        t.legacy
                      ) {
                        var r, i, s;
                        const e = t.legacy;
                        return {
                          id_str: t.rest_id,
                          is_trusted_friends_list_member:
                            t.is_trusted_friends_list_member,
                          profile_image_url_https:
                            e.profile_image_url_https || "",
                          can_dm: e.can_dm || !1,
                          can_media_tag: e.can_media_tag || !1,
                          protected: e.protected || !1,
                          verified: e.verified || !1,
                          is_blue_verified:
                            null != (r = t.is_blue_verified) && r,
                          verified_type:
                            null != (i = t.legacy.verified_type) ? i : void 0,
                          name: e.name || "",
                          screen_name: e.screen_name || "",
                          highlightedLabel: (0, o.H)(
                            null ==
                              (s = t.identity_profile_labels_highlighted_label)
                              ? void 0
                              : s.label
                          ),
                          profile_image_shape: t.profile_image_shape,
                        };
                      }
                    })
                    .filter(Boolean),
              })),
          fetchCommunityInviteUsers: (t) =>
            e
              .graphQL(c(), { communityId: t.communityId, prefix: t.prefix })
              .then((e) => {
                var t;
                const r =
                  "Community" ===
                    (null == (t = e.communityResults.result)
                      ? void 0
                      : t.__typename) && e.communityResults.result;
                if (!r)
                  return {
                    events: [],
                    ordered_sections: [],
                    topics: [],
                    users: [],
                    invite_action_results: { result: [] },
                  };
                const s = r.user_relationship_typeahead,
                  n = h(s),
                  a = s.map(_.W).filter(Boolean);
                return {
                  events: [],
                  ordered_sections: [],
                  topics: [],
                  users: n,
                  invite_action_results: (0, i.Fv)(a, [_.Z]),
                };
              }),
          fetchCommunityMembers: (t) =>
            e
              .graphQL(m(), { communityId: t.communityId, prefix: t.prefix })
              .then((e) => {
                var t;
                const r =
                  "Community" ===
                    (null == (t = e.communityResults.result)
                      ? void 0
                      : t.__typename) && e.communityResults.result;
                if (!r)
                  return {
                    events: [],
                    ordered_sections: [],
                    topics: [],
                    users: [],
                    user_community_relationships: { result: [] },
                  };
                const s = r.member_relationship_typeahead.filter(
                    (e) => e.role !== n.WW.NonMember
                  ),
                  _ = h(s).filter((e) => !!e.screen_name),
                  a = s.map(u).filter(Boolean);
                return {
                  events: [],
                  ordered_sections: [],
                  topics: [],
                  users: _,
                  user_community_relationships: (0, i.Fv)(a, [l]),
                };
              }),
          prefetchUsers(r, i = {}) {
            const n = t.isTrue(
                "responsive_web_twitter_blue_verified_badge_is_enabled"
              ),
              _ = t.isTrue("blue_business_consumption_api_enabled"),
              a = t.isTrue("blue_business_profile_image_shape_enabled"),
              u = {
                prefetch: !0,
                media_tagging_in_prefetch: !0,
                result_type: "users",
                ...(0, s.Z)(n ? { include_ext_is_blue_verified: 1 } : null),
                ...(0, s.Z)(_ ? { include_ext_verified_type: 1 } : null),
                ...(0, s.Z)(a ? { include_ext_profile_image_shape: 1 } : null),
                ...r,
              };
            return e.get("search/typeahead", u, i);
          },
        });
    },
    12006: (e, t, r) => {
      "use strict";
      r.d(t, { H: () => s });
      var i = r(3760);
      function s(e) {
        if (!e) return;
        const {
          badge: t,
          description: r,
          url: s,
          userLabelDisplayType: n,
          userLabelType: _,
        } = e;
        return {
          badge: t,
          description: r,
          userLabelType: _,
          userLabelDisplayType: n,
          url: s && (0, i.Z)(s),
        };
      }
    },
    45611: (e, t, r) => {
      "use strict";
      r.d(t, { L: () => l, Z: () => p });
      r(6886);
      var i = r(15729),
        s = r(90968),
        n = r(36325),
        _ = r(23006),
        a = r(29122),
        u = r(91191);
      const l = "userCommunityRoleRelationship",
        o = (0, a.ZP)({ namespace: l }),
        d = {
          markUserAsRemovedFromCommunity: (0, a.Tx)(
            o,
            "markUserAsRemovedFromCommunity",
            {
              getMeta: (e) => {
                const [t, r] = e.split("_");
                return { communityId: t, entityId: e, userId: r };
              },
              reducer: (e, t) => {
                const { entityId: r } = t.meta;
                return r
                  ? (0, i.ZP)(e, (e) => {
                      e.entities[r] && (e.entities[r].role = s.WW.NonMember);
                    })
                  : e;
              },
              relayStoreUpdater: (e, t) => {
                var r;
                const { communityId: i, userId: s } = t,
                  a = e.get((0, n.WG)("Community", i)),
                  u = (0, _.h)(a),
                  l =
                    null == u ||
                    null == (r = u.getLinkedRecords("items_results"))
                      ? void 0
                      : r.filter((e) => {
                          var t;
                          return (
                            (null == e ||
                            null == (t = e.getLinkedRecord("result"))
                              ? void 0
                              : t.getValue("rest_id")) !== s
                          );
                        });
                l && (null == u || u.setLinkedRecords(l, "items_results"));
              },
              context: "MARK_USER_AS_REMOVED_FROM_COMMUNITY",
            }
          ),
        },
        m = { ...o, ...d },
        p = u.Z.register(m);
    },
    23006: (e, t, r) => {
      "use strict";
      r.d(t, { h: () => s });
      var i = r(23555);
      const s = (e) =>
        e && (0, i.$R)(e, "CommunityMembers_Query_members_slice");
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Typeahead.4d55e8da.js.map
