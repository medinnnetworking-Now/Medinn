# Before I Leave Medical College: the Ledger design language

A separate identity from Medinn's other work (People of Healthcare, the Medinn site). It lives on medinn.in but looks like its own publication.

**Tone first:** read `bilmc/TONE.md` before writing or posting anything for this series. The premise: MBBS is the foundation of every doctor's career, and it feels undervalued.

## The colour code (this is the system)
| Colour | Means | Used for |
|---|---|---|
| **Red** `#E10600` (on black `#FF4A3D`) | A critique: what is broken, missing or unanswered | Critique text, the empty cell, dashed missing steps, the one red slide |
| **Black on white** `#0B0B0B` | An understanding: an insight, a proposal, a reframe | Body text, diagrams, insight posters |
| **Blue** `#0A47C2` (on black `#7FA6FF`) | Evidence | Sources, institutions, real events, links |
| White on black | Covers, closers and the one big reframe | Slides 1, 11, 12; question posters |

Rules: a red slide is for a critique and nothing else. Every slide and poster carries a tag in the header (Critique, Insight, Evidence, The question) so the code is always visible. Photos of past events are not used; every image is an original illustration or the author portrait.

## Type and layout
Fraunces (headlines, body), Inter (names), JetBrains Mono (running header, "Fig." captions, sources). 1080 x 1350. Running header on top, author footer at the bottom: `Dr. Sidharth Narayanan · House Surgeon, GMC Kozhikode`. No Medinn logo on slides.

## Files
- `system/ledger.css`: tokens and slide primitives. `fonts/`: self-hosted fonts.
- `bilmc/001/build_slides.py`: the 12-slide carousel (edit copy here). `takes.json` + `build_posters.py`: one poster per take.
- `bilmc/001/render.js`: exports PNGs, the PDF, posters, the thumbnail, and the figure plates for the article page into `/essays/img/`.
- Site: `/essays/ledger.css`, `/before-i-leave-medical-college/` (series home and articles). Short links: `/bilmc` and `/bilmc/<slug>`.

Render: `cd editorial/bilmc/001 && python3 build_slides.py && python3 build_posters.py && NODE_PATH=$(npm root -g) node render.js`

## Next article
Copy `bilmc/001` to `bilmc/002`, rewrite the slides and `takes.json`, add the page under `/before-i-leave-medical-college/`, and add its card to the series home.
