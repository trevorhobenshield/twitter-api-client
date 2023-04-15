(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.AudioSpaces"],
  {
    78111: (e) => {
      e.exports = {
        queryId: "QB5okPsUwVP3TefHBFItnw",
        operationName: "AudioSpaceById",
        operationType: "query",
        metadata: {
          featureSwitches: [
            "spaces_2022_h2_clipping",
            "spaces_2022_h2_spaces_communities",
            "blue_business_profile_image_shape_enabled",
            "responsive_web_graphql_exclude_directive_enabled",
            "verified_phone_label_enabled",
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
            "responsive_web_graphql_timeline_navigation_enabled",
            "interactive_text_enabled",
            "responsive_web_text_conversations_enabled",
            "longform_notetweets_rich_text_read_enabled",
            "responsive_web_enhance_cards_enabled",
          ],
        },
      };
    },
    52546: (e) => {
      e.exports = {
        queryId: "NTq79TuSz6fHj8lQaferJw",
        operationName: "AudioSpaceSearch",
        operationType: "query",
        metadata: { featureSwitches: [] },
      };
    },
    28119: (e) => {
      e.exports = {
        queryId: "Sxn4YOlaAwEKjnjWV0h7Mw",
        operationName: "SubscribeToScheduledSpace",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    88997: (e) => {
      e.exports = {
        queryId: "Zevhh76Msw574ZSs2NQHGQ",
        operationName: "UnsubscribeFromScheduledSpace",
        operationType: "mutation",
        metadata: { featureSwitches: [] },
      };
    },
    27260: (e, t, r) => {
      "use strict";
      r.r(t), r.d(t, { default: () => I });
      r(71372), r(6886);
      var s = r(72599),
        i = r(83175),
        n = (r(36728), r(14983)),
        a = r.n(n),
        o = r(59124),
        l = r(90968),
        u = r(36002),
        _ = r(38269),
        c = r(26178),
        d = r(12006);
      function p(e) {
        var t, r, s, i;
        a()(e, "audioSpace is required");
        const { metadata: n, participants: l, sharings: d, ...p } = e;
        a()(n, "metadata is required");
        const { rest_id: f, state: b } = n;
        a()(f, "rest_id is required"), a()(b, "state is required");
        const y = (function (e) {
            if (e && e.result && "Community" === e.result.__typename) {
              const { __typename: t, rest_id: r, ...s } = e.result,
                { custom_theme: i, default_theme: n, name: a } = s,
                l = o.Z.getCommunityTheme(i || n),
                u = o.Z.getCommunityBackgroundColor(l),
                c = (0, _.Wb)(s),
                d = (0, _.TB)(s),
                p = c || d;
              return {
                rest_id: r,
                color: u,
                name: a,
                image_url: null == p ? void 0 : p.url,
              };
            }
          })(n.community_results),
          v = (function (e, t) {
            const r = null == e ? void 0 : e.total,
              s = h(null == e ? void 0 : e.admins, t),
              i = h(null == e ? void 0 : e.speakers, t),
              n = h(null == e ? void 0 : e.listeners, t);
            return { total: r, admins: s, speakers: i, listeners: n };
          })(l, y),
          w = (function (e) {
            if (!e) return [];
            return e.items
              .map((e) => {
                var t;
                const r = m(null == (t = e.user_results) ? void 0 : t.result),
                  s = e.shared_item;
                if ("AudioSpaceSharedTweet" === s.__typename) {
                  var i, n;
                  if (
                    "Tweet" ===
                    (null == (i = s.tweet_results) || null == (n = i.result)
                      ? void 0
                      : n.__typename)
                  ) {
                    var a;
                    const { __typename: t, ...i } =
                        (null == (a = s.tweet_results) ? void 0 : a.result) ||
                        {},
                      n = (0, c.y9)(i);
                    if (n) {
                      const { cards: t, tweets: s, users: i } = n.entities,
                        a = (0, u.F)(s, t, i, n.result);
                      if (a) return { id: e.sharing_id, user: r, tweet: a };
                    }
                  }
                  return null;
                }
                return null;
              })
              .filter(Boolean);
          })(d),
          g = m(null == (t = n.creator_results) ? void 0 : t.result),
          S = null == g ? void 0 : g.screen_name,
          q =
            null == g || null == (r = g.profile_image_extensions_media_color)
              ? void 0
              : r.palette,
          { cohosts: T, host: I } = (function (e, t) {
            let r;
            const s = [];
            t
              ? e.admins.forEach((e) => {
                  e.twitter_screen_name === t ? (r = e) : s.push(e);
                })
              : (r = e.admins[0]);
            return { host: r, cohosts: s };
          })(v, S);
        return (
          a()(I, "host is required"),
          {
            ...p,
            ...n,
            rest_id: f,
            state: b,
            host: I,
            hostPalette: q,
            cohosts: T,
            participants: v,
            sharings: w,
            ended_at: n.ended_at ? parseInt(n.ended_at, 10) : void 0,
            total_live_listeners: null != (s = n.total_live_listeners) ? s : 0,
            total_replay_watched: null != (i = n.total_replay_watched) ? i : 0,
            community: y,
          }
        );
      }
      function h(e, t) {
        return e
          ? e.map(({ user_results: e, ...r }) => {
              const s = {
                ...r,
                user_id: null == e ? void 0 : e.rest_id,
                community: void 0,
                has_nft_avatar: void 0,
                is_blue_verified: void 0,
                verified_type: void 0,
                highlightedLabel: void 0,
              };
              if (t) {
                const e = t.color,
                  i = Boolean(
                    r.community_role && r.community_role !== l.WW.NonMember
                  );
                s.community = { color: e, isMember: i };
              }
              var i, n;
              null != e &&
                e.result &&
                "User" === e.result.__typename &&
                ((s.is_blue_verified = e.result.is_blue_verified),
                (s.has_nft_avatar = e.result.has_nft_avatar),
                (s.is_blue_verified = e.result.is_blue_verified),
                (s.verified_type =
                  null == (i = e.result.legacy) ? void 0 : i.verified_type),
                (s.highlightedLabel = (0, d.H)(
                  null ==
                    (n = e.result.identity_profile_labels_highlighted_label)
                    ? void 0
                    : n.label
                )));
              return s;
            })
          : [];
      }
      function m(e) {
        if (e && "User" === e.__typename) {
          const { __typename: t, ...r } = e,
            s = (0, c.Hy)(r);
          if (s) return s.entities.users[s.result];
        }
        return null;
      }
      var f = r(78111),
        b = r.n(f),
        y = r(52546),
        v = r.n(y),
        w = r(28119),
        g = r.n(w),
        S = r(88997),
        q = r.n(S),
        T = r(67560);
      const I = ({ apiClient: e, featureSwitches: t }) => ({
          spacebar: () =>
            e.getUnversioned("/fleets/v1/fleetline", { only_spaces: !0 }, {}),
          byId(r, s = {}) {
            const n = "byId",
              a = s.isMetatagsQuery || !1;
            return e
              .graphQL(
                b(),
                {
                  id: r,
                  isMetatagsQuery: a,
                  ...(0, i.d)(t),
                  withReplays: t.isTrue("voice_rooms_replay_consumption"),
                },
                Q(n, r, () => !0)
              )
              .catch((e) => {
                if (
                  !(function (e) {
                    if (!e) return !1;
                    const [t] = e.errors || [];
                    return (
                      (null == t ? void 0 : t.code) === T.Z.DuplicateRequest
                    );
                  })(e)
                )
                  throw e;
              })
              .then((e) => {
                if (e)
                  try {
                    return p(null == e ? void 0 : e.audioSpace);
                  } catch (e) {
                    throw new Error(L(n, e.message));
                  }
              });
          },
          subscribeToScheduledSpaceById(t) {
            const r = "subscribeToScheduledSpaceById";
            return e.graphQL(g(), { id: t }, Q(r, t)).catch(x(r)).then(A(r));
          },
          unsubscribeFromScheduledSpaceById(t) {
            const r = "unsubscribeFromScheduledSpaceById";
            return e.graphQL(q(), { id: t }, Q(r, t)).catch(x(r)).then(A(r));
          },
          search(t, r) {
            const s = "spacesSearch";
            return e
              .graphQL(v(), { query: t, filter: r }, Q(s, t))
              .catch(x(s))
              .then((e) => {
                var t, r;
                return null != e &&
                  null != (t = e.search_by_raw_query) &&
                  t.audio_spaces_grouped_by_section
                  ? (function (e) {
                      if (!Array.isArray(e.sections)) return { sections: [] };
                      const t = { sections: [] };
                      return (
                        e.sections.forEach((e) => {
                          const { destination: r, name: s } = e;
                          if (Array.isArray(e.items)) {
                            const i = [];
                            e.items.forEach((e) => {
                              var t;
                              null != e &&
                                null != (t = e.space) &&
                                t.rest_id &&
                                i.push(e.space.rest_id);
                            }),
                              s &&
                                r &&
                                t.sections.push({
                                  name: s,
                                  destination: r,
                                  items: i,
                                });
                          }
                        }),
                        t
                      );
                    })(
                      null == e || null == (r = e.search_by_raw_query)
                        ? void 0
                        : r.audio_spaces_grouped_by_section
                    )
                  : { sections: [] };
              });
          },
        }),
        L = (e, t) => `GQL: AudioSpaces.${e} [${t}]`;
      function x(e) {
        return (t) => {
          if (t) throw new Error(L(e, t.message));
        };
      }
      function A(e) {
        return (t) => {
          if (t) return t;
          throw new Error(L(e, "404"));
        };
      }
      const B = (e, t) => !1;
      function Q(e, t, r = B) {
        return function (i, n) {
          let a = !1;
          if (i.length) {
            const [r] = i,
              { code: n, message: o, path: l } = r;
            let u;
            const _ = C.find(({ matches: e }) => e(o));
            if (null != _ && _.message) u = L(e, _.message);
            else if (Array.isArray(l)) {
              const t = l.map(k).join(".");
              u = L(e, t);
            } else u = L(e, o || "isFatalError");
            (0, s.ZP)(u, { extra: { code: n, id: t, message: o, path: l } }),
              (a = !0);
          }
          return !r(i, n) && a;
        };
      }
      function k(e) {
        return "number" == typeof e ? "#" : e;
      }
      const C = ["Overcapacity: Unspecified", "Timeout: Unspecified"].map(
        (e) => ({
          matches: (t) => t && e.toLowerCase() === t.toLowerCase(),
          message: e,
        })
      );
    },
    12006: (e, t, r) => {
      "use strict";
      r.d(t, { H: () => i });
      var s = r(3760);
      function i(e) {
        if (!e) return;
        const {
          badge: t,
          description: r,
          url: i,
          userLabelDisplayType: n,
          userLabelType: a,
        } = e;
        return {
          badge: t,
          description: r,
          userLabelType: a,
          userLabelDisplayType: n,
          url: i && (0, s.Z)(i),
        };
      }
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.AudioSpaces.4551fcfa.js.map
