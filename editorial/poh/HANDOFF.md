# People of Healthcare (PoH): handoff

Use this to start a fresh Claude Code session on PoH without losing anything. Also read the root `CLAUDE.md`.

## What PoH is
A Medinn initiative: **connecting with 50 MVPs of healthcare and MedTech in Kerala before 2026 ends** (hospital founders, CEOs, MedTech/device makers, KOLs, diagnostics leaders, researchers, investors). Aim: understand what they build and the gaps in Kerala's healthcare, publish profiles (with each person's approval), and use the relationships to funnel problems, mentors, pilots and future startups. Doctors are framed as potential builders, not just end users.
Tagline: "Connecting with the MVPs of healthcare and MedTech in Kerala." Owner's phone/WhatsApp: +91 94005 13128. Email: medinnnetworking@gmail.com.

## What is live (all on main)
- **/people-of-healthcare**: `people-of-healthcare.html` (cover, ecosystem, "where it comes from", questions, five lenses, who we speak to, why it matters, take part, discovery form, contact). Share image `people-of-healthcare-og.jpg`.
- **Homepage** (`index.html`): hero pill "Initiative: People of Healthcare", nav item first in the list, `#poh` section, "Discover People of Healthcare" button (replaced "Explore services" in the nav, hero, phone menu and universe panel), PoH card in the Blogs section. Sections run newest first.
- **/blogs** (`blogs/index.html`): PoH card.
- **/people-of-healthcare-questions** (`people-of-healthcare-questions.html`, public, noindex, not in nav): fill-in page for people who replied. Name, venture, one scale number, the 7 questions. They send by WhatsApp (+91 94005 13128) or email, or copy. No server storage; answers only live in their browser until sent. Link it only in messages.
- **/people-of-healthcare-share** (`people-of-healthcare-share.html`, public, noindex): second fill-in page with the 8-question set (biggest project; highlights you want the world to know; what are you building; immediate need; who to access; hospital ecosystem; what to build next in Kerala; who to speak to next). Same send options as the first page. Cards and copy blocks for this set are NOT built yet (pending owner OK).
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
- A planned `/people-of-healthcare-asks` page is not built yet.

## Pitfalls learned
- Phosphor icon font on the site only has a subset of icons (`story.css` / `index.html`). Check before using a new icon class.
- The homepage hero animation: first visit per browser session plays the universe burst and folds back; `sessionStorage` key `medinn-intro` (use a private tab to see it again).
- Vercel previews of branches need a Vercel login; test locally with `python3 -m http.server` plus Playwright instead.
