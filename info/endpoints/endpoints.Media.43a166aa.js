"use strict";
(self.webpackChunk_twitter_responsive_web =
  self.webpackChunk_twitter_responsive_web || []).push([
  ["endpoints.Media"],
  {
    73114: (e, t, a) => {
      a.r(t), a.d(t, { default: () => i });
      const i = ({ apiClient: e, featureSwitches: t }) => ({
        metadataCreate: (t, a) =>
          e.post(
            "media/metadata/create",
            t,
            {},
            { ...a, "content-type": "application/json" }
          ),
        attachSubtitles: (t, a) =>
          e.post(
            "media/subtitles/create",
            {
              media_id: t.videoMediaUploadId,
              media_category: t.videoMediaCategory,
              subtitle_info: {
                subtitles: [
                  {
                    media_id: t.subtitlesMediaUploadId,
                    language_code: t.subtitlesLang,
                    display_name: t.subtitlesDisplayName,
                  },
                ],
              },
            },
            {},
            { ...a, "content-type": "application/json" }
          ),
      });
    },
  },
]);
//# sourceMappingURL=https://ton.local.twitter.com/responsive-web-internal/sourcemaps/client-web/endpoints.Media.43a166aa.js.map
