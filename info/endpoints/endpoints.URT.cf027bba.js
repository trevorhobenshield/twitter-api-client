(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.URT"],
  {
    58274: (e) => {
      e.exports = {
        queryId: "lq02A-gEzbLefqTgD_PFzQ",
        operationName: "ConnectTabTimeline",
        operationType: "query",
        metadata: {
          featureSwitches: [
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_exclude_directive_enabled",
            "verified_phone_label_enabled",
            "responsive_web_graphql_timeline_navigation_enabled",
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled",
            "tweetypie_unmention_optimization_enabled",
            "vibe_api_enabled",
            "responsive_web_edit_tweet_api_enabled",
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled",
            "view_counts_everywhere_api_enabled",
            "longform_notetweets_consumption_enabled",
            "tweet_awards_web_tipping_enabled",
            "freedom_of_speech_not_reach_fetch_enabled",
            "standardized_nudges_misinfo",
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled",
            "interactive_text_enabled",
            "responsive_web_text_conversations_enabled",
            "longform_notetweets_rich_text_read_enabled",
            "responsive_web_enhance_cards_enabled",
          ],
        },
      };
    },
    34758: (e) => {
      e.exports = {
        queryId: "fkypGKlR9Xz9kLvUZDLoXw",
        operationName: "ExplorePage",
        operationType: "query",
        metadata: {
          featureSwitches: [
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_exclude_directive_enabled",
            "verified_phone_label_enabled",
            "responsive_web_graphql_timeline_navigation_enabled",
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled",
            "tweetypie_unmention_optimization_enabled",
            "vibe_api_enabled",
            "responsive_web_edit_tweet_api_enabled",
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled",
            "view_counts_everywhere_api_enabled",
            "longform_notetweets_consumption_enabled",
            "tweet_awards_web_tipping_enabled",
            "freedom_of_speech_not_reach_fetch_enabled",
            "standardized_nudges_misinfo",
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled",
            "interactive_text_enabled",
            "responsive_web_text_conversations_enabled",
            "longform_notetweets_rich_text_read_enabled",
            "responsive_web_enhance_cards_enabled",
          ],
        },
      };
    },
    43847: (e) => {
      e.exports = {
        queryId: "gkjsKepM6gl_HmFWoWKfgg",
        operationName: "SearchTimeline",
        operationType: "query",
        metadata: {
          featureSwitches: [
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_exclude_directive_enabled",
            "verified_phone_label_enabled",
            "responsive_web_graphql_timeline_navigation_enabled",
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled",
            "tweetypie_unmention_optimization_enabled",
            "vibe_api_enabled",
            "responsive_web_edit_tweet_api_enabled",
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled",
            "view_counts_everywhere_api_enabled",
            "longform_notetweets_consumption_enabled",
            "tweet_awards_web_tipping_enabled",
            "freedom_of_speech_not_reach_fetch_enabled",
            "standardized_nudges_misinfo",
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled",
            "interactive_text_enabled",
            "responsive_web_text_conversations_enabled",
            "longform_notetweets_rich_text_read_enabled",
            "responsive_web_enhance_cards_enabled",
          ],
        },
      };
    },
    31063: (e) => {
      e.exports = {
        queryId: "vfVbgvTPTQ-dF_PQ5lD1WQ",
        operationName: "timelinesFeedback",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    83230: (e) => {
      e.exports = {
        queryId: "I_0j1mjMwv94SdS66S4pqw",
        operationName: "UrtFixtures",
        operationType: "query",
        metadata: {
          featureSwitches: [
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_exclude_directive_enabled",
            "verified_phone_label_enabled",
            "responsive_web_graphql_timeline_navigation_enabled",
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled",
            "tweetypie_unmention_optimization_enabled",
            "vibe_api_enabled",
            "responsive_web_edit_tweet_api_enabled",
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled",
            "view_counts_everywhere_api_enabled",
            "longform_notetweets_consumption_enabled",
            "tweet_awards_web_tipping_enabled",
            "freedom_of_speech_not_reach_fetch_enabled",
            "standardized_nudges_misinfo",
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled",
            "interactive_text_enabled",
            "responsive_web_text_conversations_enabled",
            "longform_notetweets_rich_text_read_enabled",
            "responsive_web_enhance_cards_enabled",
          ],
        },
      };
    },
    7276: (e, t, n) => {
      "use strict";
      n.r(t), n.d(t, { default: () => T, getDefaults: () => x });
      var _ = n(98209),
        i = n(93333),
        a = n(17360),
        r = n(83175),
        s = n(58274),
        o = n.n(s),
        l = n(34758),
        d = n.n(l),
        c = n(43847),
        p = n.n(c),
        b = n(31063),
        u = n.n(b),
        m = n(83230),
        h = n.n(m),
        w = n(6623),
        g = n(82249),
        v = n(87233),
        f = n(55371);
      const x = (e) => ({
          ...f.getGlobalDefaults(e),
          ...v.getGlobalDefaults(e),
          include_entities: !0,
          include_user_entities: !0,
          include_ext_media_color: !0,
          include_ext_media_availability: !0,
          include_ext_sensitive_media_warning: !0,
          include_ext_trusted_friends_metadata: !0,
          send_error_codes: !0,
          simple_quoted_tweet: !0,
        }),
        y = { pc: 1, spelling_corrections: 1 },
        T = ({ apiClient: e, featureSwitches: t }) => ({
          fetchNotifications(n, _ = {}) {
            const { type: i, ...a } = n;
            return e.getURT(
              `notifications/${i}`,
              Object.assign({}, x(t), a, (0, w.Y)(t)),
              _
            );
          },
          fetchNotificationsUnreadCount(t, n = {}) {
            const { type: _, ...i } = t;
            return e.getURT(
              `notifications/${_}/unread_count`,
              { ...i, include_tweet_replies: !0 },
              n
            );
          },
          updateNotificationsLastSeenCursor(t, n = {}) {
            const { type: _, ...i } = t;
            return e.postURT(`notifications/${_}/last_seen_cursor`, i, {}, n);
          },
          fetchSearch: (n, i = {}) =>
            e.getURT(
              "search/adaptive",
              Object.assign(
                {},
                x(t),
                n,
                y,
                {
                  include_ext_edit_control: t.isTrue(
                    "responsive_web_edit_tweet_api_enabled"
                  ),
                },
                (0, w.Y)(t),
                ((e) =>
                  _.Z.shouldDisablePromotedContentFromRequests(e)
                    ? { pc: "0" }
                    : {})(t),
                {}
              ),
              i
            ),
          fetchSearchGraphQL: ({
            count: n,
            cursor: _,
            product: i,
            querySource: s,
            rawQuery: o,
          }) =>
            e
              .graphQL(
                p(),
                {
                  rawQuery: o || "",
                  count: n,
                  cursor: _,
                  querySource: s,
                  product: i,
                  ...(0, r.d)(t),
                },
                (0, a.kj)((e) => {
                  var t, n;
                  return !(
                    null != e &&
                    null != (t = e.search_by_raw_query) &&
                    null != (n = t.search_timeline) &&
                    n.timeline
                  );
                }, "GQL URT: Failed to render SearchTimeline")
              )
              .then((e) => {
                var t, n;
                return (
                  (null == (t = e.search_by_raw_query) ||
                  null == (n = t.search_timeline)
                    ? void 0
                    : n.timeline) || g.cY
                );
              }),
          fetchGeneric(n, _ = {}) {
            const { endpointUrl: i, ...a } = n;
            return e.getUnversioned(
              i,
              Object.assign({}, x(t), a, (0, w.Y)(t)),
              { ..._, ...(0, w.c)() }
            );
          },
          fetchReactiveInstructions(n, _ = {}) {
            const { timeout: i, ...a } = n;
            return e.getURT(
              "timeline/reactive",
              Object.assign({}, x(t), a, (0, w.Y)(t)),
              _,
              ".json",
              i
            );
          },
          fetchTestFixtures: (n, _) =>
            e.getURT("timeline/fixture", Object.assign({}, x(t), n), {
              ..._,
              ...(0, w.c)(),
            }),
          fetchTestGraphqlFixtures: (n, _) =>
            e
              .graphQL(
                h(),
                { includePromotedContent: !0, ...(0, r.d)(t) },
                (e, t) => {
                  var n, _;
                  return !(
                    null != t &&
                    null != (n = t.viewer) &&
                    null != (_ = n.urt_fixture) &&
                    _.timeline
                  );
                }
              )
              .then((e) => {
                var t, n;
                return null == e ||
                  null == (t = e.viewer) ||
                  null == (n = t.urt_fixture)
                  ? void 0
                  : n.timeline;
              }),
          fetchExplore: (n, _) =>
            e.getURT("guide", Object.assign({}, x(t), n, (0, w.Y)(t)), {
              ..._,
              ...(0, w.c)(),
            }),
          fetchExploreGraphQL: ({ context: n, cursor: _ }) =>
            e
              .graphQL(
                d(),
                { cursor: _ ? _.toString() : "", context: n, ...(0, r.d)(t) },
                (0, a.kj)(
                  (e) => !(null != e && e.explore_page),
                  "GQL URT: Failed to render Explore GraphQL"
                )
              )
              .then((e) => e.explore_page || g.ln),
          fetchUserMoments(n, _) {
            const a = {
                ..._,
                ...(0, i.Z)(n.activeTeamId),
                ...(0, w.c)(),
                "content-type": "application/json",
              },
              { includeCapsuleContents: r, ...s } = n;
            return e.getURT(
              "moments/list_user_moments",
              Object.assign({}, x(t), s, { include_capsule_contents: r }),
              a
            );
          },
          postCustomEndpoint(t, n = {}) {
            const { endpoint: _, ...i } = t;
            return e.postUnversioned(_, i, n);
          },
          fetchLiveEventTimeline(n, _) {
            const { eventId: i, ...a } = n;
            return e.getURT(
              `live_event/timeline/${i}`,
              Object.assign({}, x(t), a, (0, w.Y)(t), {
                urt: !0,
                get_annotations: t.isTrue("moment_annotations_enabled"),
              }),
              { ..._, ...(0, w.c)() }
            );
          },
          fetchExploreTopic: (n, _ = {}) =>
            e.getURT("guide/topic", Object.assign({}, x(t), n, (0, w.Y)(t)), _),
          fetchNewsLandingTimeline: (n, _ = {}) =>
            e.getURT("rux", Object.assign({}, x(t), n, (0, w.Y)(t)), _),
          fetchRichConnectTimeline: (n, _ = {}) =>
            e.getURT(
              "people_discovery/modules_urt",
              Object.assign({}, x(t), n, (0, w.Y)(t)),
              _
            ),
          fetchRichSuggestedTimeline: (n, _ = {}) =>
            e.getURT(
              "people_discovery/modules_urt",
              Object.assign({}, x(t), n, (0, w.Y)(t)),
              _
            ),
          fetchNUXUserRecommendations: (n, _ = {}) =>
            e.getURT(
              "onboarding/fetch_user_recommendations_urt",
              Object.assign({}, x(t), n, (0, w.Y)(t)),
              _
            ),
          submitTimelinesFeedback: (t) => e.graphQL(u(), { ...t }),
          fetchRichConnectTimelineGraphql: ({
            context: n,
            count: _,
            cursor: i,
          }) =>
            e
              .graphQL(
                o(),
                { count: _, cursor: i, context: n, ...(0, r.d)(t) },
                (0, a.kj)((e) => {
                  var t;
                  return !(
                    null != e &&
                    null != (t = e.connect_tab_timeline) &&
                    t.timeline
                  );
                }, "GQL URT: Failed to render ConnectTabTimeline")
              )
              .then((e) => {
                var t;
                return (
                  (null == (t = e.connect_tab_timeline)
                    ? void 0
                    : t.timeline) || g.cY
                );
              }),
        });
    },
    98209: (e, t, n) => {
      "use strict";
      n.d(t, { Z: () => _ });
      const _ = (() => {
        let e = !1;
        return {
          recordAdBlockerPresence: () => {
            e = !0;
          },
          shouldHidePromotedTweets: (t) =>
            e && t.isTrue("responsive_web_extension_compatibility_hide"),
          shouldDisablePromotedContentFromRequests: (t) =>
            e &&
            t.isTrue("responsive_web_extension_compatibility_override_param"),
        };
      })();
    },
    93333: (e, t, n) => {
      "use strict";
      function _(e) {
        return e ? { "x-act-as-user-id": e } : {};
      }
      n.d(t, { Z: () => _ });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.URT.cf027bba.js.map
