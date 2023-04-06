(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.URT"],
  {
    58274: (e) => {
      e.exports = {
        queryId: "cA9Gp-VIehDryHSNLlAzGw",
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
            "longform_notetweets_richtext_consumption_enabled",
            "responsive_web_enhance_cards_enabled",
          ],
        },
      };
    },
    34758: (e) => {
      e.exports = {
        queryId: "7VMeU_woptIODfaBCwbUnA",
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
            "longform_notetweets_richtext_consumption_enabled",
            "responsive_web_enhance_cards_enabled",
          ],
        },
      };
    },
    43847: (e) => {
      e.exports = {
        queryId: "onvt6Vb9JZcoK-MyPreHGg",
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
            "longform_notetweets_richtext_consumption_enabled",
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
        queryId: "i4SU_TyEjcOBrlQ9fEQx8g",
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
            "longform_notetweets_richtext_consumption_enabled",
            "responsive_web_enhance_cards_enabled",
          ],
        },
      };
    },
    7276: (e, t, n) => {
      "use strict";
      n.r(t), n.d(t, { default: () => T, getDefaults: () => x });
      var i = n(98209),
        _ = n(93333),
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
          fetchNotifications(n, i = {}) {
            const { type: _, ...a } = n;
            return e.getURT(
              `notifications/${_}`,
              Object.assign({}, x(t), a, (0, w.Y)(t)),
              i
            );
          },
          fetchNotificationsUnreadCount(t, n = {}) {
            const { type: i, ..._ } = t;
            return e.getURT(
              `notifications/${i}/unread_count`,
              { ..._, include_tweet_replies: !0 },
              n
            );
          },
          updateNotificationsLastSeenCursor(t, n = {}) {
            const { type: i, ..._ } = t;
            return e.postURT(`notifications/${i}/last_seen_cursor`, _, {}, n);
          },
          fetchSearch: (n, _ = {}) =>
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
                  i.Z.shouldDisablePromotedContentFromRequests(e)
                    ? { pc: "0" }
                    : {})(t),
                {}
              ),
              _
            ),
          fetchSearchGraphQL: ({
            count: n,
            cursor: i,
            product: _,
            querySource: s,
            rawQuery: o,
          }) =>
            e
              .graphQL(
                p(),
                {
                  rawQuery: o || "",
                  count: n,
                  cursor: i,
                  querySource: s,
                  product: _,
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
          fetchGeneric(n, i = {}) {
            const { endpointUrl: _, ...a } = n;
            return e.getUnversioned(
              _,
              Object.assign({}, x(t), a, (0, w.Y)(t)),
              { ...i, ...(0, w.c)() }
            );
          },
          fetchReactiveInstructions(n, i = {}) {
            const { timeout: _, ...a } = n;
            return e.getURT(
              "timeline/reactive",
              Object.assign({}, x(t), a, (0, w.Y)(t)),
              i,
              ".json",
              _
            );
          },
          fetchTestFixtures: (n, i) =>
            e.getURT("timeline/fixture", Object.assign({}, x(t), n), {
              ...i,
              ...(0, w.c)(),
            }),
          fetchTestGraphqlFixtures: (n, i) =>
            e
              .graphQL(
                h(),
                { includePromotedContent: !0, ...(0, r.d)(t) },
                (e, t) => {
                  var n, i;
                  return !(
                    null != t &&
                    null != (n = t.viewer) &&
                    null != (i = n.urt_fixture) &&
                    i.timeline
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
          fetchExplore: (n, i) =>
            e.getURT("guide", Object.assign({}, x(t), n, (0, w.Y)(t)), {
              ...i,
              ...(0, w.c)(),
            }),
          fetchExploreGraphQL: ({ context: n, cursor: i }) =>
            e
              .graphQL(
                d(),
                { cursor: i ? i.toString() : "", context: n, ...(0, r.d)(t) },
                (0, a.kj)(
                  (e) => !(null != e && e.explore_page),
                  "GQL URT: Failed to render Explore GraphQL"
                )
              )
              .then((e) => e.explore_page || g.ln),
          fetchUserMoments(n, i) {
            const a = {
                ...i,
                ...(0, _.Z)(n.activeTeamId),
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
            const { endpoint: i, ..._ } = t;
            return e.postUnversioned(i, _, n);
          },
          fetchLiveEventTimeline(n, i) {
            const { eventId: _, ...a } = n;
            return e.getURT(
              `live_event/timeline/${_}`,
              Object.assign({}, x(t), a, (0, w.Y)(t), {
                urt: !0,
                get_annotations: t.isTrue("moment_annotations_enabled"),
              }),
              { ...i, ...(0, w.c)() }
            );
          },
          fetchExploreTopic: (n, i = {}) =>
            e.getURT("guide/topic", Object.assign({}, x(t), n, (0, w.Y)(t)), i),
          fetchNewsLandingTimeline: (n, i = {}) =>
            e.getURT("rux", Object.assign({}, x(t), n, (0, w.Y)(t)), i),
          fetchRichConnectTimeline: (n, i = {}) =>
            e.getURT(
              "people_discovery/modules_urt",
              Object.assign({}, x(t), n, (0, w.Y)(t)),
              i
            ),
          fetchRichSuggestedTimeline: (n, i = {}) =>
            e.getURT(
              "people_discovery/modules_urt",
              Object.assign({}, x(t), n, (0, w.Y)(t)),
              i
            ),
          fetchNUXUserRecommendations: (n, i = {}) =>
            e.getURT(
              "onboarding/fetch_user_recommendations_urt",
              Object.assign({}, x(t), n, (0, w.Y)(t)),
              i
            ),
          submitTimelinesFeedback: (t) => e.graphQL(u(), { ...t }),
          fetchRichConnectTimelineGraphql: ({
            context: n,
            count: i,
            cursor: _,
          }) =>
            e
              .graphQL(
                o(),
                { count: i, cursor: _, context: n, ...(0, r.d)(t) },
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
      n.d(t, { Z: () => i });
      const i = (() => {
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
      function i(e) {
        return e ? { "x-act-as-user-id": e } : {};
      }
      n.d(t, { Z: () => i });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.URT.0c56715a.js.map
