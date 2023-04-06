(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.DirectMessagesGraphQL"],
  {
    23221: (e) => {
      e.exports = {
        queryId: "2NpGQJPxEmFk36AV6XHFkw",
        operationName: "DmAllSearchSlice",
        operationType: "query",
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
    52864: (e) => {
      e.exports = {
        queryId: "5zpY1dCR-8NyxQJS_CFJoQ",
        operationName: "DmGroupSearchSlice",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    74907: (e) => {
      e.exports = {
        queryId: "EA6DU_EGuonAVLSHduSlLw",
        operationName: "DmMutedTimeline",
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
    10776: (e) => {
      e.exports = {
        queryId: "xYSm8m5kJnzm_gFCn5GH-w",
        operationName: "DmPeopleSearchSlice",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    30310: (e, i, t) => {
      "use strict";
      t.r(i), t.d(i, { default: () => f, isFatalDMSearchError: () => h });
      var n = t(6899),
        l = t(17360),
        r = t(83175),
        a = t(5189),
        _ = t(23221),
        s = t.n(_),
        o = t(52864),
        d = t.n(o),
        u = t(74907),
        c = t.n(u),
        m = t(10776),
        v = t.n(m),
        g = t(82249);
      const h = (e, i) => {
          let t = !1;
          var n, r;
          if (null != i && i.dmPeopleSearchSlice)
            t = !(
              null == i ||
              null == (n = i.dmPeopleSearchSlice) ||
              null == (r = n.items) ||
              !r.length
            );
          else if (null != i && i.dmGroupSearchSlice) {
            var a, _;
            t = !(
              null == i ||
              null == (a = i.dmGroupSearchSlice) ||
              null == (_ = a.items) ||
              !_.length
            );
          } else if (null != i && i.dmMessageSearchSlice) {
            if (
              "DMMessageSlice" !==
              (null == i ? void 0 : i.dmMessageSearchSlice.__typename)
            )
              return !0;
            var s, o;
            t = !(
              null == i ||
              null == (s = i.dmMessageSearchSlice) ||
              null == (o = s.items) ||
              !o.length
            );
          }
          return !t && (0, l.jB)(e);
        },
        p = (e) => {
          var i;
          const t =
            null == (i = e.items)
              ? void 0
              : i.map((e) => (null == e ? void 0 : e.dm_convo_search));
          return (0, n.Fv)(t, [a.ZP]);
        },
        f = ({ apiClient: e, featureSwitches: i }) => ({
          fetchDMAllSearch: (t) =>
            t
              ? e
                  .graphQL(
                    s(),
                    {
                      count: null == t ? void 0 : t.count,
                      query: t.query,
                      withAttachments:
                        i.isTrue(
                          "dm_inbox_search_message_attachment_previews_enabled"
                        ) &&
                        i.isTrue("dm_inbox_search_message_results_enabled") &&
                        i.isTrue("direct_messages_incremental_holdback_2022h1"),
                      withConversationQueryHighlights:
                        i.isTrue(
                          "dm_inbox_search_query_highlighting_conversation_results_enabled"
                        ) &&
                        i.isTrue("direct_messages_incremental_holdback_2022h1"),
                      withMessageQueryHighlights:
                        i.isTrue(
                          "dm_inbox_search_query_highlighting_message_results_enabled"
                        ) &&
                        i.isTrue("dm_inbox_search_message_results_enabled") &&
                        i.isTrue("direct_messages_incremental_holdback_2022h1"),
                      withMessages:
                        i.isTrue("dm_inbox_search_message_results_enabled") &&
                        i.isTrue("direct_messages_incremental_holdback_2022h1"),
                      withSafetyModeUserFields: i.isTrue(
                        "rito_safety_mode_blocked_profile_enabled"
                      ),
                    },
                    h
                  )
                  .then((e) => {
                    const i = null == e ? void 0 : e.dmGroupSearchSlice,
                      t = null == e ? void 0 : e.dmMessageSearchSlice,
                      l = null == e ? void 0 : e.dmPeopleSearchSlice;
                    let r = g.d;
                    if (i) {
                      var _, s, o;
                      const { entities: e, result: t } = p(i),
                        n =
                          (null == (_ = i.items)
                            ? void 0
                            : _.find((e) => {
                                var i;
                                return null == e || null == (i = e.highlighting)
                                  ? void 0
                                  : i.query_tokens;
                              })) &&
                          (null == (s = i.items)
                            ? void 0
                            : s.map((e) => {
                                var i;
                                return null == e || null == (i = e.highlighting)
                                  ? void 0
                                  : i.query_tokens;
                              }));
                      r = {
                        result:
                          null == (o = r)
                            ? void 0
                            : o.result.concat({
                                groupData: { result: t, highlightingTokens: n },
                              }),
                        entities: e,
                      };
                    }
                    if (l) {
                      var d, u, c, m;
                      const { entities: e, result: i } = p(l),
                        t =
                          (null == (d = l.items)
                            ? void 0
                            : d.find((e) => {
                                var i;
                                return null == e || null == (i = e.highlighting)
                                  ? void 0
                                  : i.query_tokens;
                              })) &&
                          (null == (u = l.items)
                            ? void 0
                            : u.map((e) => {
                                var i;
                                return null == e || null == (i = e.highlighting)
                                  ? void 0
                                  : i.query_tokens;
                              }));
                      r = {
                        ...r,
                        result:
                          null == (c = r)
                            ? void 0
                            : c.result.concat({
                                peopleData: {
                                  result: i,
                                  highlightingTokens: t,
                                },
                              }),
                        entities: {
                          ...(null == (m = r) ? void 0 : m.entities),
                          ...e,
                        },
                      };
                    }
                    if (
                      t &&
                      "DMMessageSlice" === (null == t ? void 0 : t.__typename)
                    ) {
                      var v, h, f, b;
                      const e = null == t ? void 0 : t.items,
                        i = (0, n.Fv)(e, [a.JJ]),
                        l =
                          null == e
                            ? void 0
                            : e.map((e) => {
                                var i, t;
                                return null == e ||
                                  null == (i = e.dm_event) ||
                                  null == (t = i.legacy)
                                  ? void 0
                                  : t.conversation;
                              }),
                        _ =
                          (null == e
                            ? void 0
                            : e.find((e) => {
                                var i;
                                return null == e || null == (i = e.highlighting)
                                  ? void 0
                                  : i.query_tokens;
                              })) &&
                          (null == e
                            ? void 0
                            : e.map((e) => {
                                var i;
                                return null == e || null == (i = e.highlighting)
                                  ? void 0
                                  : i.query_tokens;
                              })),
                        { entities: s, result: o } = (0, n.Fv)(l, [a.ZP]);
                      r = {
                        ...r,
                        result:
                          null == (v = r) || null == (h = v.result)
                            ? void 0
                            : h.concat({
                                messageData: {
                                  conversationIds: o,
                                  entryIds: null == i ? void 0 : i.result,
                                  highlightingTokens: _,
                                },
                              }),
                        entities: {
                          ...(null == i ? void 0 : i.entities),
                          conversations: {
                            ...(null == (f = r) || null == (b = f.entities)
                              ? void 0
                              : b.conversations),
                            ...(null == s ? void 0 : s.conversations),
                          },
                        },
                      };
                    }
                    return r;
                  })
              : Promise.resolve(g.d),
          fetchDMGroupSearch: (t) =>
            t
              ? e
                  .graphQL(
                    d(),
                    {
                      ...t,
                      withConversationQueryHighlights:
                        i.isTrue(
                          "dm_inbox_search_query_highlighting_conversation_results_enabled"
                        ) &&
                        i.isTrue("direct_messages_incremental_holdback_2022h1"),
                    },
                    h
                  )
                  .then((e) => {
                    const i = null == e ? void 0 : e.dmGroupSearchSlice;
                    if (i) {
                      const { entities: e, result: t } = p(i);
                      return {
                        result: t,
                        entities: e,
                        slice_info: i.sliceInfo,
                      };
                    }
                    return g.d;
                  })
              : Promise.resolve(g.d),
          fetchDMPeopleSearch: (t) =>
            t
              ? e
                  .graphQL(
                    v(),
                    {
                      ...t,
                      withConversationQueryHighlights:
                        i.isTrue(
                          "dm_inbox_search_query_highlighting_conversation_results_enabled"
                        ) &&
                        i.isTrue("direct_messages_incremental_holdback_2022h1"),
                    },
                    h
                  )
                  .then((e) => {
                    const i = null == e ? void 0 : e.dmPeopleSearchSlice;
                    if (i) {
                      const { entities: e, result: t } = p(i);
                      return {
                        result: t,
                        entities: e,
                        slice_info: i.sliceInfo,
                      };
                    }
                    return g.d;
                  })
              : Promise.resolve(g.d),
          fetchDMMutedUsers: ({ count: t, cursor: n }) =>
            e
              .graphQL(
                c(),
                {
                  count: t,
                  cursor: n,
                  includePromotedContent: !1,
                  ...(0, r.d)(i),
                },
                (0, l.kj)((e) => {
                  var i, t;
                  return !(
                    null != e &&
                    null != (i = e.viewer) &&
                    null != (t = i.dm_muting_timeline) &&
                    t.timeline
                  );
                }, "GQL URT: Failed to render DM Muting timeline")
              )
              .then((e) => {
                var i, t;
                return (
                  (null == (i = e.viewer) || null == (t = i.dm_muting_timeline)
                    ? void 0
                    : t.timeline) || g.cY
                );
              }),
        });
    },
    5189: (e, i, t) => {
      "use strict";
      t.d(i, { JJ: () => u, ZP: () => m });
      t(6886), t(36728);
      var n = t(6899),
        l = t(29086),
        r = t(22167),
        a = t(46395),
        _ = t(15804),
        s = t(85364);
      const o = Object.freeze({
          GROUP: "GroupDm",
          ONE_TO_ONE: "OneToOneDm",
          UNKNOWN: "Unknown",
        }),
        d = Object.freeze({
          MessageCreate: r.Cr.MESSAGE,
          ParticipantsJoin: r.Cr.PARTICIPANTS_JOIN,
          ParticipantsLeave: r.Cr.PARTICIPANTS_LEAVE,
          ConversationNameUpdate: r.Cr.CONVERSATION_NAME_UPDATE,
          JoinConversation: r.Cr.JOIN_CONVERSATION,
        }),
        u = new n.fK.Entity(
          "entries",
          {
            message_data: { attachment: { card: _.Z, tweet: { status: s.Z } } },
          },
          {
            processStrategy: (e, i, t) => {
              var n, r, _, s, o, u, c;
              const { legacy: m, rest_id: v } =
                  (null == e ? void 0 : e.dm_event) || {},
                g = null == m ? void 0 : m.event_type,
                { affects_sort: h, request_id: p } = m || {};
              let f,
                b,
                S = "Unknown";
              g in d && (S = d[g]);
              const y =
                  null == m || null == (n = m.conversation)
                    ? void 0
                    : n.rest_id,
                E = null == m || null == (r = m.event_detail) ? void 0 : r.dm,
                A = null == m ? void 0 : m.created_at_millis,
                {
                  card: T,
                  media: N,
                  tweet_results: O,
                  urls_entity: w,
                } = (null == E || null == (_ = E.attachments)
                  ? void 0
                  : _[0]) || {};
              if (
                (null != T && T.legacy && (f = { card: T }),
                null != w &&
                  w.length &&
                  E.text &&
                  w.forEach((e) => {
                    null != e &&
                      e.indices[0] &&
                      (b = E.text
                        .slice(0, null == e ? void 0 : e.indices[0])
                        .concat(E.text.slice(e.indices[1])));
                  }),
                "Tweet" ===
                  (null == O || null == (s = O.result) ? void 0 : s.__typename))
              ) {
                var I, D, x, M, C, R, P, k, q;
                const e =
                  null == O || null == (I = O.result) || null == (D = I.legacy)
                    ? void 0
                    : D.entities;
                let i;
                null != e && null != (x = e.media) && x.length
                  ? (i = null == e ? void 0 : e.media[0])
                  : null != e &&
                    null != (M = e.urls) &&
                    M.length &&
                    (i = null == e ? void 0 : e.urls[0]);
                const {
                    display_url: t,
                    expanded_url: n,
                    id_str: l,
                    indices: r,
                    url: a,
                  } = i || {},
                  { extended_entities: _ } =
                    (null == O || null == (C = O.result) ? void 0 : C.legacy) ||
                    {},
                  s =
                    null == _ || null == (R = _.media)
                      ? void 0
                      : R.map((e) => {
                          if (null != e && e.video_info) {
                            var i;
                            const t =
                              null == e || null == (i = e.video_info)
                                ? void 0
                                : i.variants;
                            return {
                              ...e,
                              video_info: {
                                ...(null == e ? void 0 : e.video_info),
                                variants: t,
                              },
                            };
                          }
                          return e;
                        }),
                  o = {
                    ...(null == O ||
                    null == (P = O.result) ||
                    null == (k = P.legacy)
                      ? void 0
                      : k.extended_entities),
                    media: s,
                  };
                f = {
                  tweet: {
                    status: {
                      ...(null == O ? void 0 : O.result),
                      legacy: {
                        ...(null == O || null == (q = O.result)
                          ? void 0
                          : q.legacy),
                        extended_entities: o,
                      },
                    },
                    display_url: t,
                    expanded_url: n,
                    indices: r,
                    url: a,
                    id: l,
                  },
                };
              }
              const G = N ? (0, l.m)(N) : null;
              G &&
                G.type &&
                ("photo" === G.type
                  ? (f = { photo: G })
                  : "video" === G.type
                  ? (f = { video: G })
                  : "animated_gif" === G.type && (f = { animated_gif: G }));
              const L = {
                affects_sort: h,
                request_id: p,
                time: A,
                type: S,
                conversation_id: y,
                message_data: {
                  id: v,
                  text: b || (null == E ? void 0 : E.text),
                  entities: null == E ? void 0 : E.entities,
                  recipient_id:
                    null == E ||
                    null == (o = E.recipient_results) ||
                    null == (u = o.result)
                      ? void 0
                      : u.rest_id,
                  sender_id:
                    null == E || null == (c = E.sender_results)
                      ? void 0
                      : c.result.rest_id,
                  attachment: f,
                },
                id: v,
              };
              return (0, a.Z)(L, i, t);
            },
            idAttribute: (e) => {
              var i;
              return null == e || null == (i = e.dm_event) ? void 0 : i.rest_id;
            },
          }
        ),
        c = new n.fK.Entity(
          "conversations",
          {},
          {
            processStrategy: (e, i, t) => {
              var n, l, _;
              const {
                  id: s,
                  labels: d,
                  legacy: u,
                  perspectival_conversation_metadata: c,
                  rest_id: m,
                } = e || {},
                v = {},
                g = [];
              for (const e of (null == u ? void 0 : u.participants_metadata) ||
                []) {
                var h;
                const i =
                  null == e || null == (h = e.user_results) ? void 0 : h.result;
                if (!i || !i.legacy) continue;
                const t = {
                  description: i.legacy.description,
                  id_str: i.legacy.id_str,
                  name: i.legacy.name,
                  profile_image_url_https:
                    i.legacy.profile_image_url_https || "",
                  screen_name: i.legacy.screen_name,
                };
                (v[i.rest_id] = t), g.push({ user: t, user_id: i.rest_id });
              }
              let p = null == u || null == (n = u.metadata) ? void 0 : n.avatar;
              const f = null == (l = p) ? void 0 : l.media_info,
                b = null == e ? void 0 : e.last_readable_event_id;
              if (f) {
                const {
                  original_img_height: e,
                  original_img_url: i,
                  original_img_width: t,
                } = f || {};
                p = {
                  image: { original_info: { height: e, width: t, url: i } },
                };
              }
              const S =
                  (null == u || null == (_ = u.metadata)
                    ? void 0
                    : _.conversation_type) === o.GROUP
                    ? r.eD.GROUP
                    : r.eD.ONE_TO_ONE,
                y = {
                  ...(null == u
                    ? void 0
                    : u.perspectival_conversation_metadata),
                  ...(null == u ? void 0 : u.metadata),
                  ...c,
                  id: s,
                  conversation_id: m,
                  avatar: p,
                  labels: d,
                  last_readable_event_id: b,
                  type: S,
                  participants: g,
                  users: v,
                };
              return (0, a.Z)(y, i, t);
            },
            idAttribute: (e) => {
              var i;
              return null == e || null == (i = e.legacy)
                ? void 0
                : i.conversation_id;
            },
          }
        );
      c.define({ entities: u });
      const m = c;
    },
    29086: (e, i, t) => {
      "use strict";
      t.d(i, { m: () => n });
      const n = (e) => {
          const i = null == e ? void 0 : e.media_info;
          if ("ApiImage" === (null == i ? void 0 : i.__typename)) {
            var t;
            return {
              altText: i.alt_text,
              display_url: i.original_img_url,
              expanded_url: i.original_img_url,
              ext_alt_text: i.alt_text,
              ...((null == (t = i.color_info) ? void 0 : t.palette) && {
                ext_media_color: { palette: i.color_info.palette },
              }),
              id: r(e.media_id),
              id_str: e.media_id || "",
              media_key: e.media_key,
              media_url: i.original_img_url,
              media_url_https: i.original_img_url,
              original_info: {
                height: i.original_img_height,
                width: i.original_img_width,
              },
              sizes: {
                original: {
                  h: i.original_img_height,
                  resize: "fit",
                  w: i.original_img_width,
                },
              },
              type: "photo",
            };
          }
          if ("ApiVideo" === (null == i ? void 0 : i.__typename)) {
            const { __typename: t, ...n } = i;
            return l(n, e.media_id, null == i ? void 0 : i.__typename);
          }
          if ("ApiGif" === (null == i ? void 0 : i.__typename)) {
            const { __typename: t, ...n } = i;
            return l(n, e.media_id, null == i ? void 0 : i.__typename);
          }
        },
        l = (e, i, t) => {
          var n;
          const l = "ApiGif" === t ? "animated_gif" : "video",
            a = e.preview_image;
          return {
            type: l,
            id: r(i),
            id_str: i || "",
            ext_alt_text: null == a ? void 0 : a.alt_text,
            ext_media_color: {
              palette:
                (null == a || null == (n = a.color_info)
                  ? void 0
                  : n.palette) || [],
            },
            media_url: (null == a ? void 0 : a.original_img_url) || "",
            media_url_https: (null == a ? void 0 : a.original_img_url) || "",
            url: (null == a ? void 0 : a.original_img_url) || "",
            display_url: (null == a ? void 0 : a.original_img_url) || "",
            expanded_url: (null == a ? void 0 : a.original_img_url) || "",
            original_info: {
              height: (null == a ? void 0 : a.original_img_height) || 0,
              width: (null == a ? void 0 : a.original_img_width) || 0,
            },
            sizes: {
              original: {
                h: (null == a ? void 0 : a.original_img_height) || 0,
                resize: "fit",
                w: (null == a ? void 0 : a.original_img_width) || 0,
              },
            },
            video_info: {
              aspect_ratio: [
                e.aspect_ratio.numerator,
                e.aspect_ratio.denominator,
              ],
              ...(e.duration_millis && { duration_millis: e.duration_millis }),
              variants: e.variants.map((e) => ({
                bitrate: e.bit_rate,
                content_type: e.content_type,
                url: e.url,
              })),
            },
          };
        },
        r = (e) => {
          const i = parseInt(e, 10);
          return Number.isNaN(i) ? 0 : i;
        };
    },
    22167: (e, i, t) => {
      "use strict";
      t.d(i, { Cr: () => r, To: () => l, UN: () => a, eD: () => n });
      const n = Object.freeze({ ONE_TO_ONE: "ONE_TO_ONE", GROUP: "GROUP_DM" }),
        l = Object.freeze({ AT_END: "AT_END", HAS_MORE: "HAS_MORE" }),
        r = Object.freeze({
          CONVERSATION_AVATAR_UPDATE: "conversation_avatar_update",
          CONVERSATION_NAME_UPDATE: "conversation_name_update",
          CONVERSATION_PROFILE_INFO_HEADER: "conversation_profile_info_header",
          CONVERSATION_READ: "conversation_read",
          CONVO_METADATA_UPDATE: "convo_metadata_update",
          DELEGATE_ALERT_BANNER: "delegate_alert_banner",
          DISABLE_NOTIFICATIONS: "disable_notifications",
          ENABLE_NOTIFICATIONS: "enable_notifications",
          JOIN_CONVERSATION: "join_conversation",
          LOADING_INDICATOR: "loading_indicator",
          MARK_ALL_AS_READ: "mark_all_as_read",
          MENTION_NOTIFICATIONS_UPDATE: "mention_notifications_setting_update",
          MESSAGE: "message",
          MESSAGE_DELETE: "message_delete",
          MESSAGE_MARK_AS_NOT_SPAM: "message_unmark_as_spam",
          MESSAGE_MARK_AS_SPAM: "message_mark_as_spam",
          NEW_MESSAGES_DIVIDER: "new_messages_divider",
          PARTICIPANTS_JOIN: "participants_join",
          PARTICIPANTS_LEAVE: "participants_leave",
          REACTION_CREATE: "reaction_create",
          REACTION_DELETE: "reaction_delete",
          READ_ONLY_INDICATOR: "read_only_indicator",
          REMOVE_CONVERSATION: "remove_conversation",
          TRUST_CONVERSATION: "trust_conversation",
          TYPING_INDICATOR: "typing_indicator",
          WELCOME_MESSAGE: "welcome_message_create",
        }),
        a = Object.freeze({ MUTUAL_FRIENDS: "mutual_friends" });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.DirectMessagesGraphQL.76aaa8fa.js.map
