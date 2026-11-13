# People of Healthcare (PoH): handoff

Use this to start a fresh Claude Code session on PoH without losing anything. Also read the root `CLAUDE.md`.

## What PoH is
A Medinn initiative: **connecting with 50 MVPs of healthcare and MedTech in Kerala before 2026 ends** (hospital founders, CEOs, MedTech/device makers, KOLs, diagnostics leaders, researchers, investors). Aim: understand what they build and the gaps in Kerala's healthcare, publish profiles (with each person's approval), and use the relationships to funnel problems, mentors, pilots and future startups. Doctors are framed as potential builders, not just end users.
Tagline: "Connecting with the MVPs of healthcare and MedTech in Kerala." Owner's phone/WhatsApp: +91 94005 13128. Email: medinnnetworking@gmail.com.

## What is live (all on main)
- **/people-of-healthcare**: `people-of-healthcare.html` (cover, ecosystem, "where it comes from", questions, five lenses, who we speak to, why it matters, take part, discovery form, contact). Share image `people-of-healthcare-og.jpg`.
- **/people-of-healthcare now also has two sections right after the cover (4 Nov 2026)**: "Featured" (PoH | Karkinos card, links to the Moni article) and "PoH Asks" (PoH Person 01's four asks, links to /people-of-healthcare-asks). Existing sections renumbered 3 to 10. To add a new feature or Person 02, edit the `#featured` and `#asks` sections. Also fixed a broken `@media` line in that page's CSS (the mobile rules had never closed properly).
- **Homepage** (`index.html`): hero pill "Initiative: People of Healthcare", nav item first in the list, `#poh` section, "Discover People of Healthcare" button (replaced "Explore services" in the nav, hero, phone menu and universe panel), PoH card in the Blogs section. Sections run newest first.
- **/blogs** (`blogs/index.html`): PoH card.
- **/people-of-healthcare-questions** (`people-of-healthcare-questions.html`, public, noindex, not in nav): fill-in page for people who replied. Name, venture, one scale number, the 7 questions. They send by WhatsApp (+91 94005 13128) or email, or copy. No server storage; answers only live in their browser until sent. Link it only in messages.
- **/people-of-healthcare-mvp** (`people-of-healthcare-mvp.html`, public, noindex): fill-in page for MVPs/KOLs to be featured. Name, company, role, optional scale number, photo sent on WhatsApp, 11 questions (building, biggest project and highlights, bottlenecks, bridges, adoption and discovery, immediate need, access, future of healthcare, what needs to be done, who next, comments for Medinn and PoH). Same send options as the other fill-in pages. Text blocks (including audio-answer blocks) in `mvp-conversation.md`.
- **/people-of-healthcare-share** (`people-of-healthcare-share.html`, public, noindex): second fill-in page with the 8-question set (biggest project; highlights you want the world to know; what are you building; immediate need; who to access; hospital ecosystem; what to build next in Kerala; who to speak to next). Same send options as the first page. Cards and copy blocks for this set are NOT built yet (pending owner OK).
- **/poh-moni-abraham-kuriakose** (`poh-moni-abraham-kuriakose.html`, LIVE and indexable; cleared by Dr. Kuriakose 4 Nov 2026; own link-preview image `poh-moni-abraham-kuriakose-og.jpg` built from `editorial/poh/moni-og.html`): first MVP feature article, Dr. Moni Abraham Kuriakose, Karkinos Healthcare, with his photo `moni-abraham-kuriakose.jpg` (supplied by owner; confirm source/permission with him). No funding/investor ask in it. Header pattern for MVP features (owner decision, updated 4 Nov): tag "People of Healthcare · MVP", then a text lockup "PoH | Company" (no logos), then the title; the person's name sits with the photo below. Template for later MVP features. Poster: `editorial/poh/export/PoH-feature-Moni-Kuriakose-DRAFT.png` now has his photo.
- **/poh-maanas-jain** (`poh-maanas-jain.html`, live, noindex until Dr. Jain approves; og `poh-maanas-jain-og.jpg`; illustrations `essays/img/poh-quintubate-*.svg`): PoH feature on Dr. Maanas Jain, Founder and CTO, Quintubate (UVEAL). Source, carousel (13 slides, PNG/PDF in `export/`) and illustrations in `editorial/poh/features/maanas-jain/`. Old BILMC URLs `/before-i-leave-medical-college/some-doctors-dont-wait` and `/bilmc/...` redirect here. Card in PoH Featured section. Needs: Dr. Jain's approval and permission for his photo and video frames; CDSCO and scale claims are his.
- **/poh-hanan-kasim** (`poh-hanan-kasim.html`, LIVE and indexable from 13 Nov 2026 on the owner's instruction; owner to confirm Hanan's approval and the open items in `features/hanan-kasim-notes.md`; featured card on /people-of-healthcare): next MVP feature, "PoH | Elara Health AI" header, face crop `hanan-kasim-face.jpg` (full photo `hanan-kasim.jpg`), og image `poh-hanan-kasim-og.jpg`. Person 03 asks (ASK-09 to 12) are NOT on the Asks page yet.
- **Logo**: `poh-mark.png` (blue), `poh-mark-navy.png`. Built from Bricolage 800, "PoH." with a pale-blue dot.
- **Discovery form**: shown only when the server is configured. `api/nominate.js` writes to Notion. `GET /api/nominate` returns `{configured:true/false}`; the page reveals the form only if true. WhatsApp and email nomination buttons always work (prefilled messages).

## Notion (the nominations database)
- Database: "People of Healthcare: Nominations". URL https://app.notion.com/p/5b140e8313a345de87158c76ec6b00a7
- Database id `5b140e8313a345de87158c76ec6b00a7`; data source `collection://5ffaa309-8f55-4722-a001-9cdddb71abf0`
- Properties: Nominee (title), Role and organisation, Segment (select), What they have built or lead, Why they belong among the 50, Nominee contact, Submitted by, Submitter contact, Submitter type (select: Nominating someone else / Self-introduction), Status (New, Reviewing, Reached out, Scheduled, Done, Not now), Submitted (created time).
- Vercel (team `medinn`, project `medinn`) env vars, already set: `NOTION_TOKEN` (secret, never in the repo) and `NOTION_NOMINATIONS_DB`. The Notion connection is named "Medinn website" (API token type, insert access, connected to the database). End-to-end test passed (a test row arrived as "New", then was trashed).
- Setup instructions kept in `NOTION-SETUP.md`.

## Files in editorial/poh/
| File | What it makes |
|---|---|
| `build_poh.py` + `render.js` | 7-slide announcement carousel (PNGs + LinkedIn PDF) and the logo lockups |
| `poster-whatsapp.html` + `qr-form.png` + `render-poster.js` | One WhatsApp poster; QR opens medinn.in/people-of-healthcare#form |
| `build_docs.py` + `render-docs.js` | `PoH-Brief-for-MVPs.pdf` (2 pp, for invitees) and `PoH-Interview-Guide-and-Leverage-Playbook.pdf` (4 pp, internal) |
| `og.html` + `render-og.js` | Link-preview image source (output goes to `export/`; copy to `/people-of-healthcare-og.jpg` as a JPG) |
| `whatsapp-conversation.md` | One-day WhatsApp question kit for people who replied to the poster/link: intro, 8 core questions, close, segment add-ons, fit check. Has a facts-to-confirm list (first-generation doctor, last-month apparel revenue; KNYA vs "Kenya" is settled: it is KNYA) |
| `chat-cards.html` + `render-cards.js` | 4 WhatsApp conversation cards (1080x1350): intro, about-you prerequisite, the 7 questions, thank-you. Output `export/poh-chat-0N-*.png`. Questions text is in `whatsapp-conversation.md` |
| `question-cards.html` + `render-questions.js` | One card per question, `export/poh-q1.png` to `poh-q7.png`, to send one at a time |
| `asks-cards.html` + `render-asks.js` | PoH Asks cards (`export/poh-ask-02/01/03/04.png`). ASK-02 is the featured one. Tag "PoH Asks"; source line is only "From an engineering team working on a syringe pump system" (no names, company or patent number). Replies go privately to WhatsApp +91 94005 13128 quoting the ASK id, never public comments |
| `asks-campaign-poster.html` + `render-asks-poster.js` + `qr-asks.png` | Campaign poster `export/poh-asks-campaign-poster.png`: "Brave innovators reached out. They have asks." Two QRs: join (discovery form) and solve (asks page). Both QRs decode correctly |
| `discovery-message-template.md` | LinkedIn/DM discovery message template for cold or warm outreach (use "sir"), with the fact-check list and a log of who was sent it |
| `features/moni-captions.md` | LinkedIn and short social captions for the Dr. Moni / Karkinos feature, with alternative hooks. Post only after his approval |
| `features/` | Draft features for approval, one file per MVP. First: `moni-abraham-kuriakose-draft.md` (Karkinos Healthcare). Drafts are never published until the person approves, with their photo |
| `feature-moni-poster.html`, `asks02-named.html`, `asks02-anon.html`, `render-moni.js` | DRAFT posters for Dr. Moni Abraham Kuriakose: feature poster, and PoH Asks Person 02 (named and anonymous variants) in `export/*-DRAFT.png`. Photo placeholder until he sends one. The FEATURE (poster, article, draft) deliberately leaves out his asks (investor, funding) and presents the comprehensive cancer centre only as his vision; the asks live only in the separate PoH Asks material. NOT posted: waiting for his approval and his answer on named vs anonymous |
| `features/cancer-care-india-workup-draft.md` | Medinn workup "Cancer care in India: scattered, and still not reaching the community", with cited stats and a verify-before-publishing source list. Funding/investor points excluded per owner |
| `ig-carousel.html`, `ig-logo.html`, `render-ig.js`, `qr-mvp.png` | Instagram carousel (7 slides, `export/poh-ig-01..07.png`: cover, the initiative, this feature, why it matters, the model, bottleneck and bridges, the ask) and profile logo `export/poh-ig-profile-logo-1080.png` (text sized to survive the circular crop). Feature slides use the Moni/Karkinos content: do not post before his approval. "The ask" slide = call to nominate or share a story (not his personal asks) |
| `feature-hanan-poster.html`, `hanan-og.html`, `asks03-named.html`, `asks03-anon.html`, `render-hanan.js`, `render-asks03.js` | next MVP Hanan Kasim (Elara Health AI) feature poster, link-preview image and Person 03 ask posters (drafts). Notes, flags, follow-up message and caption in `features/hanan-kasim-notes.md`. Dr. Moopen intro request is PRIVATE, keep it off all public material |
| `hero-hanan.html`, `render-hero-hanan.js`, `qr-hanan.png` | Hero poster `export/poh-hero-Hanan-Kasim.png`: his photo, "Innovation alone isn't enough" (his words) plus four pillars (clinical trust, institutional access, regulatory awareness, real-world validation), QR to his feature |
| `announcement.md` | LinkedIn, Instagram and WhatsApp writeups, invitation message, bio |
| `package_kit.py` | Rebuilds the labelled zip into `editorial/dist/` (git-ignored) |
| `export/` | All rendered PNG/PDF outputs |
Rebuild everything: `cd editorial/poh && python3 build_poh.py && python3 build_docs.py && export NODE_PATH=$(npm root -g) && node render.js && node render-poster.js && node render-docs.js && python3 package_kit.py`

## Decisions already made (do not reopen without asking)
- Verb is "connecting with"; conversations are noun. "MVPs" is the owner's term.
- "Discovery" = the nomination page/form. It is the primary CTA site-wide for now (not "Explore services").
- Brief and guide say: profiles are sent for approval before publishing; Medinn is a consulting practice (stated openly); no fee to be featured; no promises of funding or outcomes.
- Outreach channels: Instagram DMs and WhatsApp. Messages and the ask ladder are in the guide and `announcement.md`.

## Open / next ideas
- KNYA Medical Apparel is the name (not Kenya). Owner to confirm the remaining unverified claims listed at the top of `whatsapp-conversation.md` before they are used in any message.
- Poster and discovery link are live; some people have shown interest. Next: run the WhatsApp conversations and log them in Notion.
- Add tracking fields to the Notion database: Date met, Key insight, Problems shared, Introductions offered, Offers (mentor / pilot / internship / funding intro), Profile status, Follow-up date.
- Build a public "People of Healthcare" profile page template (one per person, approved) and a directory page.
- Run the outreach and keep a real count (never publish a number that is not true).
- A one-pager PDF and a WhatsApp/email variant of the brief if asked.
- Optional: a reads/visit counter for PoH (the series has one wired to Upstash Redis; not yet connected).

## Conversation question set (owner decision, 2 Nov 2026)
- Do NOT ask "how could a doctor/house surgeon be useful to you". Instead ask: is access to a hospital ecosystem useful, what is your immediate need, who do you need access to, what should we build next in Kerala.
- Prerequisite asked first: name, venture name, one value metric (revenue, patients served, funding, team size, years: their choice, only what they are comfortable with and approve). Keep the tone light.

## PoH Asks (owner decision, 3 Nov 2026)
- Purpose: publish needs from featured people without losing leverage. Anonymous cards, private replies only, Medinn brokers every intro with both sides' consent. Never publish names, contacts, patent numbers or off-the-record material.
- 5 entries expected; entry 1 (a syringe pump engineering team) has cards built, wording still to be approved by that team before posting. Their raw answers are deliberately not stored in the repo.
- **LIVE on main (merged 3 Nov 2026)**: https://medinn.in/people-of-healthcare-asks (not yet linked from the nav; real reply submission still to be tested once and the test row trashed in Notion). `people-of-healthcare-asks.html` (noindex, not linked) plus `api/ask-reply.js`. Layout: "PoH Person 01" glowing masked silhouette, four numbered asks (device kept generic: no syringe pump, no patent, no company), a "Drop your reply" form (ask checkboxes, name, company, how they could help, contact) that writes privately to the Notion nominations DB with Submitter type "Ask reply" (same env vars as nominate.js), plus WhatsApp/email fallback buttons. Form shows only if `/api/ask-reply` GET says configured. To add Person 02: copy the `.pa-person` block, new ask ids (ASK-05...), add checkboxes. 
- **Person 02 (Karkinos cancer-care asks, ASK-05 to 08)** is built on branch `poh-asks-02` (page shows it anonymously, reply form supports both persons) and is NOT merged: merge only after Dr. Moni approves the wording and says named or anonymous. Draft article: `features/karkinos-healthcare-article-draft.md`.
- CSS gotcha: `story.css` already defines `.asks`/`.ask`; the Asks page uses `.pa*` classes instead.

## PoH Allies (owner wording, 3 Nov 2026)
- Solvers who answer asks are called **PoH Allies**. Campaign wording: "People of Healthcare have reached out. From our first submissions, a team of engineers has posted certain asks. Can you solve them?" Plus invitation to more people of healthcare to share challenges via the discovery form (purpose: understand challenges and the bridges to build for healthcare startups and the MedTech ecosystem in Kerala). CDSCO is emphasised in asks 2 and 3. Poster: `export/poh-asks-campaign-poster.png` (silhouette of PoH Person 01 plus the 4 asks plus two QRs).

## Pitfalls learned
- Phosphor icon font on the site only has a subset of icons (`story.css` / `index.html`). Check before using a new icon class.
- The homepage hero animation: first visit per browser session plays the universe burst and folds back; `sessionStorage` key `medinn-intro` (use a private tab to see it again).
- Vercel previews of branches need a Vercel login; test locally with `python3 -m http.server` plus Playwright instead.
