# Before I Leave Medical College (the article series): handoff

Use this to start a fresh Claude Code session on the series without losing anything. Also read the root `CLAUDE.md` and `TONE.md` (same folder).

## What it is
The owner's personal series on medical education from a house surgeon's lens, published under medinn.in but with its own identity (white, black, red, blue). Premise: **MBBS is the foundation of every doctor's career. Right now, it feels undervalued.** Aim: bring value back to undergraduate medical education: first strengthen what we teach, then, for students who want it, expand what it can enable. Clinical training stays the core. Colour code: **red = critique, black on white = insight, blue = evidence**. Read `TONE.md` before writing anything.

## What is live (all on main)
- **Series home** `/before-i-leave-medical-college` (short link `/bilmc`): `before-i-leave-medical-college/index.html`.
- **Article 001** `/before-i-leave-medical-college/more-than-a-training-ground` (short `/bilmc/more-than-a-training-ground`): the owner's text verbatim, critique paragraphs in red, 7 illustrations, numbered sources in blue, MedX Talks photo header, "Share the idea you liked" gallery, reads counter slot, subscribe buttons.
  - One deliberate text change: "APJ Abdul Kalam Technological University (KTU)" instead of "Kerala Technological University". Revert if the owner prefers.
- Styles `essays/ledger.css`, fonts `essays/fonts/`, figure plates `essays/img/`, cards `essays/img/cards/`.
- **Share cards** (`essays/share.js`): select a line > "Share this line" > image card (red if critique, black if insight) with a text-fragment link. Gallery of 9... see `takes.json` (the page's gallery has the 8 article takes).
- **Reads counter** (`essays/views.js` + `api/views.js`): hidden until Upstash Redis is connected in Vercel (Storage > create Upstash Redis > connect to project > redeploy). Counts once a day after 6s, skips bots; `?owner=1` excludes the owner's browser.
- **Subscribe**: WhatsApp channel https://whatsapp.com/channel/0029VapjEz12975AjbhVk32V is set in `essays/config.js`; buttons render under the series title, after the photos and at the end of each article.
- Homepage: hero pill "Series: Before I Leave Medical College" (red), series card first in the Blogs section and on /blogs. The series is NOT in the menu and has no homepage section (owner's decision).

## Files in editorial/bilmc/001/
| File | What it makes |
|---|---|
| `build_slides.py` + `render.js` | 13-slide carousel (PNG, LinkedIn PDF), thumbnail, hook image, launch posters, and the article figure plates in `/essays/img` |
| `takes.json` + `build_posters.py` | One poster per take (critique red, insight black, question dark). Add takes here each week |
| `hook.html`, `launch-poster.html`, `launch-poster-photo.html`, `qr-article.png` | LinkedIn hook, launch posters (plain and with the MedX photo) |
| `POST-KIT.md`, `captions.md` | All copy: LinkedIn, Instagram, WhatsApp, first comment, daily poster captions, launch posts |
| `package_posts.py` | Rebuilds the labelled zip into `editorial/dist/` (git-ignored) |
Rebuild: `cd editorial/bilmc/001 && python3 build_slides.py && python3 build_posters.py && NODE_PATH=$(npm root -g) node render.js && python3 package_posts.py`
Assets: author portrait `editorial/assets/author-portrait.jpg`, MedX crops `editorial/assets/medx-*.jpg`; the original MedX photos are saved as `/bilmc-001-medx.jpg` and `/bilmc-001-medx-slide.jpg`.

## Decisions already made
- Say "MBBS", not "the MBBS". Never colour "MBBS", "clinical practice", "training doctors" or "learn medicine" red.
- Red slides/posters are for critique only. No photos of the owner's past events except the MedX Talks photos (25 October 2026, IMA MSN All Kerala, GMC Kozhikode, topic: the pressure to have it all figured out as an MBBS student).
- 13-slide carousel starts with the premise slide. WhatsApp channel (not email) is the subscribe route for now.

## Open / next
- **Article title/subtitle**: title "Medical College Is More Than a Training Ground for Doctors" leads with "more than". Recommended: keep the title and change the page subtitle (deck) to carry the premise. Awaiting the owner's choice. If chosen, update the page, share image, slides and posters.
- **"290+ days into internship"** is a fixed number on the article byline, series page, closing slide and posts. Update on each publish.
- Reads counter needs Redis connected (see above).
- Article 002: copy `bilmc/001` to `bilmc/002`, rewrite `build_slides.py` and `takes.json`, add the page under `/before-i-leave-medical-college/`, add its card to the series home and `index.html`/`blogs/index.html` card text if needed. Weekly cycle: article > carousel > one poster a day with a question > replies become next week's takes.
- Verify the sources [1] to [7] links open (KTU and Kerala Startup Mission link to homepages only).

## Pitfalls learned
- `html{scroll-behavior:smooth}` in `ledger.css` can break scripted scroll-then-measure in tests; use `behavior:'instant'`.
- Instagram does not link captions: point people to the bio link.
- The carousel numbering is automatic (`@@N@@` placeholder in `build_slides.py`); article figure plates are exported by slide id (`s03..s10`), so keep those ids stable.
