# Before I Leave Medical College: series design system ("The Atlas")

A personal editorial series by Dr. Sidharth Narayanan. It lives on medinn.in but is deliberately **not** the Medinn brand look: no Medinn logo or blue on the slides. Medinn's MedTech work keeps its own design language.

| Element | Standard |
|---|---|
| Palette | Paper `#F3EDE2`, paper-deep `#E8DFCE`, ink `#17140F`, signal red `#D3401F` (light `#F2714F` on dark) |
| Type | Fraunces (headlines, body in articles), Inter (names, labels), JetBrains Mono (running header, "Fig." captions) |
| Running header | `BEFORE I LEAVE MEDICAL COLLEGE · 00N` left, section or `FIG. n` right, ink rule beneath |
| Footer | `Dr. Sidharth Narayanan · House Surgeon, GMC Kozhikode` left, `03 / 12` right |
| Illustration | Inked line plates: ink strokes, diagonal hatching, one red annotation per figure, numbered "Fig." caption. Diagrams over decoration |
| Slide rhythm | Mostly paper; ink for the hard question; one red slide for the pivotal statement |
| Author | Portrait on the cover and the closing slide only |
| Link-out | Last slide points to the article on medinn.in |

## Files
- `system/atlas.css`: tokens and slide primitives. `fonts/`: self-hosted fonts.
- `001/slides.html`: the 12 slides (editable source). `001/thumbnail.html`: link preview.
- `001/render.js`: exports PNGs, the LinkedIn PDF and the thumbnail into `001/export/`.
- `001/figs.js`: exports the figure plates used inside the article page into `/essays/img/`.
- `/essays/essay.css`: long-form article styles. `/blogs/<slug>.html`: the article.

Render with `cd editorial/001 && NODE_PATH=$(npm root -g) node render.js && node figs.js`.

## Next article
Copy `001/` to `002/`, swap the copy and diagrams, keep the header, footer and palette. Run `figs.js` only if the article reuses plates.
