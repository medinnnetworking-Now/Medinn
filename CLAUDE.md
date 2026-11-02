# Medinn repo: read me first (for Claude Code sessions)

Static site for medinn.in (Vercel) plus serverless functions in `api/`, and the content workshop in `editorial/`.
Owner: Dr. Sidharth Narayanan (house surgeon, GMC Kozhikode; founder of Medinn). GitHub: medinnnetworking-Now/Medinn.

## Two separate workstreams. Work on ONE per session.
| Workstream | Start here |
|---|---|
| **People of Healthcare (PoH)**: connecting with 50 healthcare/MedTech leaders in Kerala. Medinn blue look. | `editorial/poh/HANDOFF.md` |
| **Before I Leave Medical College (the article series)**: medical education, red/black/white/blue look. | `editorial/bilmc/HANDOFF.md` |

Do not mix their identities or wording. PoH and the series live on the same site but are different products.

## Ground rules
- `main` deploys to https://medinn.in in about a minute (Vercel). Prefer a branch for risky changes, then merge. After any deploy, verify the live URL with curl.
- A stop hook requires a clean tree: commit and push everything before finishing a turn.
- Never commit secrets. Keys live only in Vercel env vars (names are in the handoff files).
- `.vercelignore` keeps `internal/`, `editorial/` and this file off the public site. Everything else in the repo root is public.
- Verify with the real browser (Playwright is installed: `NODE_PATH=$(npm root -g) node script.js`) before saying something works. Look at screenshots; check text fits and QR codes decode (`cv2.QRCodeDetector`).
- Never publish invented statistics, quotes or claims. Facts about the owner come from `internal/PROFILE.md` and `content.js`.
- Site visual language for PoH/Medinn pages: `story.css` (dark, Bricolage + Geist). Series pages: `essays/ledger.css` (white/black/red/blue, Fraunces).

## Owner's wording preferences
- Say "MBBS" (not "the MBBS"). Premise: "MBBS is the foundation of every doctor's career. Right now, it feels undervalued."
- PoH verb is "connecting with" the 50 MVPs (not "meeting" or "finding").
- Name: "Dr. Sidharth Narayanan". Role line: "House Surgeon, GMC Kozhikode".
