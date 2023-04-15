(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.TopArticles"],
  {
    39296: (e) => {
      e.exports = {
        queryId: "o9FyvnC-xg8mVBXqL4g-rg",
        operationName: "ArticleTimeline",
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
    33278: (e) => {
      e.exports = {
        queryId: "x4ywSpvg6BesoDszkfbFQg",
        operationName: "ArticleTweetsTimeline",
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
    15823: (e, i, _) => {
      "use strict";
      _.r(i),
        _.d(i, {
          default: () => w,
          isFatalArticleTimelineError: () => c,
          isFatalArticleTweetsTimelineError: () => b,
        });
      var t = _(72599),
        n = _(27024),
        l = _(17360),
        r = _(83175),
        a = _(39296),
        s = _.n(a),
        o = _(33278),
        d = _.n(o),
        p = _(82249);
      const b = (e, i) => {
          var _, n;
          const r =
            null == i ||
            null == (_ = i.article_by_rest_id) ||
            null == (n = _.tweets_timeline)
              ? void 0
              : n.timeline;
          return (
            r ||
              (0, t.ZP)(
                "GQL Top Articles: Failed query for article Tweets timeline"
              ),
            !r && (0, l.jB)(e)
          );
        },
        c = (e, i) => {
          var _;
          const n =
            null == i || null == (_ = i.article_timeline) ? void 0 : _.timeline;
          return (
            n ||
              (0, t.ZP)("GQL Top Articles: Failed query for article timeline"),
            !n && (0, l.jB)(e)
          );
        },
        w = ({ apiClient: e, featureSwitches: i }) => ({
          fetchArticleTweetsTimeline(_) {
            const t =
              _.articleListSeedType === n.v.FRIENDS_OF_FRIENDS
                ? "FriendsOfFriends"
                : "FollowingList";
            return e
              .graphQL(d(), { ..._, ...(0, r.d)(i), articleListSeedType: t }, b)
              .then((e) => {
                var i, _;
                return (
                  (null == e ||
                  null == (i = e.article_by_rest_id) ||
                  null == (_ = i.tweets_timeline)
                    ? void 0
                    : _.timeline) || p.cY
                );
              });
          },
          fetchArticleTimeline(_) {
            const t =
              _.articleListSeedType === n.v.FRIENDS_OF_FRIENDS
                ? "FriendsOfFriends"
                : "FollowingList";
            return e
              .graphQL(s(), { ..._, ...(0, r.d)(i), articleListSeedType: t }, c)
              .then((e) => {
                var i;
                return (
                  (null == e || null == (i = e.article_timeline)
                    ? void 0
                    : i.timeline) || p.cY
                );
              });
          },
        });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.TopArticles.8517a34a.js.map
