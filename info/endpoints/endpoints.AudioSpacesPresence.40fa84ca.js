"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  [
    "endpoints.AudioSpacesPresence",
    "shared~loader.Typeahead~loader.AppModules~bundle.Birdwatch~bundle.Communities~bundle.Compose~bundle.Settings~",
  ],
  {
    18484: (e, s, t) => {
      t.r(s), t.d(s, { default: () => a });
      var n = t(49461),
        r = t(86928);
      const a = ({ apiClient: e, featureSwitches: s }) => ({
        fetchPresence: (s, t = {}) => {
          const { userIds: a } = s,
            c = { user_ids: a.join(","), only_spaces: !0 };
          return e
            .getUnversioned("/fleets/v1/avatar_content", c, t)
            .then((e) => {
              const { users: s, refresh_delay_secs: t = r.vj } = e,
                c = 0 === t ? r.vj : t,
                i = Date.now() + 1e3 * c,
                o = Object.fromEntries(
                  a.map((e) => [
                    e,
                    { expiry: i, spaces: void 0, refresh_delay_secs: c },
                  ])
                ),
                d =
                  s &&
                  (0, n.Z)(s, (e, s) => ({
                    ...e,
                    expiry: i,
                    refresh_delay_secs: c,
                  }));
              return (d || o) && { entities: { userPresence: { ...o, ...d } } };
            });
        },
      });
    },
    86928: (e, s, t) => {
      t.d(s, { ZP: () => _, cY: () => u, vj: () => c });
      t(6886), t(36728), t(2784), t(92028);
      var n = t(94668),
        r = t(29122),
        a = t(91191);
      const c = 30,
        i = (0, r.ZP)({
          namespace: "userPresence",
          entityIsComplete: (e) => e.expiry > Date.now(),
        }),
        o = (0, r.tb)(i, {
          context: "FETCH_USER_PRESENCE",
          endpoint: (e) => e.AudioSpacesPresence.fetchPresence,
          params: (e) => ({ userIds: e }),
        }),
        d = (0, r.Nr)(i, {
          context: "FETCH_USER_PRESENCE",
          endpoint: (e) => e.AudioSpacesPresence.fetchPresence,
          params: (e) => ({ userIds: e }),
        }),
        p = { ...i, ...o, ...d },
        u = (e, s) => {
          const t = p.select(e, s),
            r = t ? t.spaces : void 0;
          return (
            r && {
              presenceRingType: "space",
              link: {
                pathname: (0, n.e)(r.live_content.audiospace.broadcast_id),
                state: { origin: "audiospace_ring" },
              },
              spaceId: r.live_content.audiospace.broadcast_id,
            }
          );
        };
      const _ = a.Z.register(p);
    },
    94668: (e, s, t) => {
      function n(e) {
        return `/i/spaces/${e}/peek`;
      }
      t.d(s, { e: () => n });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.AudioSpacesPresence.40fa84ca.js.map
