# Updating the Medinn site

Every change committed to the `main` branch goes live on https://medinn-sandy.vercel.app in about a minute. Vercel builds it automatically.

## Where things live

| File | What it controls |
|---|---|
| `content.js` | All the words and lists: gallery, services, timeline, selected work, the universe and the logo wall |
| `index.html` | The cinematic homepage (layout, styles, animation) |
| `classic.html` | The previous homepage, at `/classic` |
| Image and video files | Sit in the root of the repository, next to `index.html` |

Most updates only touch `content.js` plus an uploaded file.

## Add a photo or video to the gallery

1. On GitHub, open the repository, tap **Add file → Upload files**, and upload the photo or video. Use a short name with no spaces, such as `repair-cafe-2026.jpg`.
2. Open `content.js`, tap the pencil icon to edit, and add a line inside `GALLERY`:

   ```js
   { "type": "image", "src": "repair-cafe-2026.jpg", "caption": "Repair Café, GMC Kozhikode" },
   ```

   For a video, add a cover image too (a screenshot from the video works):

   ```js
   { "type": "video", "src": "handover-highlights.mp4", "poster": "handover-cover.jpg", "caption": "The Handover highlights" },
   ```

   For an Instagram reel or YouTube video, link to it instead of uploading:

   ```js
   { "type": "link", "src": "reel-cover.jpg", "url": "https://www.instagram.com/reel/...", "caption": "Watch the reel" },
   ```

3. Tap **Commit changes**. The site updates in about a minute.

Every line ends with a comma, and the text sits inside straight double quotes. If the page ever comes up blank after an edit, a missing comma or quote in `content.js` is the usual cause.

## Add a timeline entry

In `content.js`, find `"events"`, pick the year, and add an item to its `"items"` list:

```js
{ "when": "November 2026", "title": "Event name", "role": "What you did", "img": "photo.jpg", "imgMax": "440px", "url": "", "linkLabel": "" },
```

Leave `"img"` as `""` if there is no photo. Put a LinkedIn or Instagram link in `"url"` and a label such as `"LinkedIn post"` in `"linkLabel"` to show a link.

## Photo and video tips

- Photos: JPG, around 1200 to 1600 px on the longest side. Any shape works; nothing is cropped.
- Videos: MP4, under 20 MB, ideally 10 to 30 seconds. GitHub's web upload accepts files up to 25 MB. For longer videos, post them to Instagram or YouTube and use a `link` entry.
- Logos: PNG with a transparent or white background, named `logo-something.png` so the site shows them on a white tile.

## Seeing your change

After committing, wait a minute, then open the site in a Private tab in Safari, or pull down to refresh. Safari keeps old copies for a while.
