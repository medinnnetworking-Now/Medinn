// Usage: node render.js   (run from editorial/001). Exports PNGs + LinkedIn PDF.
const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const dir = __dirname; const out = path.join(dir, 'export');
  fs.mkdirSync(out, { recursive: true });
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + path.join(dir, 'slides.html')); await p.evaluate(() => document.fonts.ready);
  for (let i = 1; i <= 12; i++) {
    const id = 's' + String(i).padStart(2, '0');
    await (await p.$('#' + id)).screenshot({ path: path.join(out, `medinn-001-slide-${String(i).padStart(2, '0')}.png`) });
  }
  await p.pdf({ path: path.join(out, 'medinn-001-carousel.pdf'), width: '1080px', height: '1350px', printBackground: true });
  const t = await b.newPage({ viewport: { width: 1200, height: 630 } });
  await t.goto('file://' + path.join(dir, 'thumbnail.html')); await t.evaluate(() => document.fonts.ready);
  await t.screenshot({ path: path.join(out, 'medinn-001-thumbnail-1200x630.png') });
  await b.close();
})();
