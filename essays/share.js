/* Share a line: select any text in the article > "Share this line" > an image card (series style) to share or download.
   Also powers the "Share the idea you liked" gallery. Everything happens in the reader's browser. */
(function () {
  var prose = document.querySelector('.prose'); if (!prose) return;
  var canon = (document.querySelector('link[rel=canonical]') || {}).href || location.href.split('#')[0];
  var TITLE = 'Medical College Is More Than a Training Ground for Doctors';
  var RED = '#E10600', BLACK = '#0B0B0B', BLUE = '#0A47C2', GREY = '#6B6B6B';
  var SERIF = '"Fraunces",Georgia,serif', MONO = '"JetBrains Mono",ui-monospace,monospace', SANS = '"Inter",Helvetica,Arial,sans-serif';

  function clean(t) { return String(t).replace(/\[\d+\]/g, '').replace(/\s+/g, ' ').trim(); }
  function enc(s) { return encodeURIComponent(s).replace(/-/g, '%2D'); }
  function fragLink(t) {
    var w = t.split(' '); var f = w.length > 8 ? enc(w.slice(0, 4).join(' ')) + ',' + enc(w.slice(-4).join(' ')) : enc(t);
    return canon + '#:~:text=' + f;
  }
  function wrap(ctx, text, maxW) {
    var words = text.split(' '), lines = [], cur = '';
    words.forEach(function (w) { var t = cur ? cur + ' ' + w : w; if (ctx.measureText(t).width > maxW && cur) { lines.push(cur); cur = w; } else cur = t; });
    if (cur) lines.push(cur); return lines;
  }
  function mono(ctx, txt, x, y, size, color, align, weight) { ctx.font = (weight || 500) + ' ' + size + 'px ' + MONO; ctx.fillStyle = color; ctx.textAlign = align || 'left'; if ('letterSpacing' in ctx) ctx.letterSpacing = '1px'; ctx.fillText(txt, x, y); if ('letterSpacing' in ctx) ctx.letterSpacing = '0px'; }

  function renderCard(text, type) {
    return Promise.all([document.fonts.load('600 80px Fraunces'), document.fonts.load('500 22px "JetBrains Mono"'), document.fonts.load('700 22px Inter')]).catch(function () {}).then(function () {
      var W = 1080, H = 1350, c = document.createElement('canvas'); c.width = W; c.height = H; var x = c.getContext('2d');
      x.fillStyle = '#fff'; x.fillRect(0, 0, W, H);
      var col = type === 'critique' ? RED : BLACK, label = type === 'critique' ? 'CRITIQUE' : 'INSIGHT';
      mono(x, 'BEFORE I LEAVE MEDICAL COLLEGE · 001', 88, 80, 21, BLACK, 'left');
      x.font = '700 21px ' + MONO; var tw = x.measureText(label).width + 24; x.strokeStyle = col; x.lineWidth = 2.5; x.strokeRect(992 - tw, 52, tw, 38); mono(x, label, 992 - tw / 2, 79, 21, col, 'center', 700);
      x.fillStyle = BLACK; x.fillRect(88, 108, 904, 3);
      x.fillStyle = col; x.fillRect(88, 196, 120, 14);
      var size = 100, lines, lh;
      for (; size >= 38; size -= 2) { x.font = '600 ' + size + 'px ' + SERIF; lh = size * 1.08; lines = wrap(x, text, 904); if (lines.length * lh <= 800) break; }
      x.fillStyle = col; x.textAlign = 'left'; x.font = '600 ' + size + 'px ' + SERIF;
      lines.forEach(function (l, i) { x.fillText(l, 88, 290 + size * .8 + i * lh); });
      mono(x, 'FROM THE ARTICLE', 88, 1128, 20, BLUE, 'left', 700);
      var ts = 28; for (; ts > 18; ts--) { x.font = '500 ' + ts + 'px ' + SERIF; if (x.measureText(TITLE).width <= 904) break; } x.fillStyle = BLACK; x.fillText(TITLE, 88, 1170);
      mono(x, canon.replace(/^https?:\/\//, '').replace('before-i-leave-medical-college', 'bilmc').replace(/\/more-than-a-training-ground$/, '/more-than-a-training-ground'), 88, 1212, 22, BLUE, 'left', 700);
      x.fillStyle = BLACK; x.fillRect(88, 1262, 904, 3);
      x.font = '700 22px ' + SANS; x.textAlign = 'left'; x.fillStyle = BLACK; x.fillText('Dr. Sidharth Narayanan', 88, 1304);
      var nw = x.measureText('Dr. Sidharth Narayanan').width; x.font = '500 22px ' + SANS; x.fillStyle = GREY; x.fillText('  ·  House Surgeon, GMC Kozhikode', 88 + nw, 1304);
      return new Promise(function (res) { c.toBlob(function (b) { res(b); }, 'image/png'); });
    });
  }

  function download(blob, name) { var a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = name || 'before-i-leave-medical-college.png'; document.body.appendChild(a); a.click(); setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500); }
  function nativeShare(blob, text, url) {
    var file = new File([blob], 'before-i-leave-medical-college.png', { type: blob.type });
    if (navigator.canShare && navigator.canShare({ files: [file] })) {
      return navigator.share({ files: [file], title: TITLE, text: '“' + text + '”\n' + url }).catch(function (e) { if (e && e.name !== 'AbortError') download(blob); });
    }
    download(blob); return Promise.resolve();
  }

  /* modal */
  var modal = document.createElement('div'); modal.className = 'sc-modal'; modal.hidden = true; modal.setAttribute('role', 'dialog'); modal.setAttribute('aria-modal', 'true'); modal.setAttribute('aria-label', 'Share this line');
  modal.innerHTML = '<div class="sc-box"><button class="sc-x" type="button" aria-label="Close">&times;</button><img class="sc-img" alt="Preview of the share card"><div class="sc-acts"><button type="button" data-a="share">Share</button><button type="button" data-a="dl">Download image</button><a data-a="wa" target="_blank" rel="noopener">WhatsApp</a><a data-a="li" target="_blank" rel="noopener">LinkedIn</a><button type="button" data-a="copy">Copy link</button></div><p class="sc-note">Tip: on Instagram, share or download the image and post it as a story or post.</p></div>';
  document.body.appendChild(modal);
  var img = modal.querySelector('.sc-img'), cur = null;
  function closeModal() { modal.hidden = true; if (img.src) URL.revokeObjectURL(img.src); document.body.classList.remove('sc-open'); }
  modal.addEventListener('click', function (e) { if (e.target === modal || e.target.closest('.sc-x')) closeModal(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !modal.hidden) closeModal(); });
  if (!navigator.share) modal.querySelector('[data-a=share]').style.display = 'none';
  modal.querySelector('[data-a=share]').addEventListener('click', function () { cur && nativeShare(cur.blob, cur.text, cur.url); });
  modal.querySelector('[data-a=dl]').addEventListener('click', function () { cur && download(cur.blob); });
  modal.querySelector('[data-a=copy]').addEventListener('click', function (e) { var b = e.currentTarget; if (navigator.clipboard) navigator.clipboard.writeText(cur.url).then(function () { b.textContent = 'Link copied'; setTimeout(function () { b.textContent = 'Copy link'; }, 1800); }); });
  function openCard(text, type, url) {
    renderCard(text, type).then(function (blob) {
      cur = { blob: blob, text: text, url: url }; img.src = URL.createObjectURL(blob);
      modal.querySelector('[data-a=wa]').href = 'https://wa.me/?text=' + encodeURIComponent('“' + text + '”\n' + url);
      modal.querySelector('[data-a=li]').href = 'https://www.linkedin.com/sharing/share-offsite/?url=' + encodeURIComponent(url);
      modal.hidden = false; document.body.classList.add('sc-open');
    });
  }

  /* select a line, share it */
  var pop = document.createElement('button'); pop.type = 'button'; pop.className = 'sc-pop'; pop.hidden = true; pop.textContent = 'Share this line'; document.body.appendChild(pop);
  var pending = null, tm = null;
  function hidePop() { pop.hidden = true; pending = null; }
  function update() {
    var s = getSelection(); if (!s || s.isCollapsed || !s.rangeCount) return hidePop();
    var r = s.getRangeAt(0), a = r.commonAncestorContainer; a = a.nodeType === 1 ? a : a.parentElement;
    if (!a || !a.closest || !a.closest('.prose') || a.closest('figure')) return hidePop();
    var raw = s.toString(), t = clean(raw);
    if (t.length < 12) return hidePop();
    var rect = r.getBoundingClientRect(), too = t.length > 320;
    var crit = !!(a.closest('.crit') || (r.startContainer.parentElement && r.startContainer.parentElement.closest('.crit')));
    pending = { text: t, type: crit ? 'critique' : 'insight', url: (/\n/.test(raw.trim()) ? canon : fragLink(t)), too: too };
    pop.textContent = too ? 'Select a shorter line (max 320 characters)' : 'Share this line'; pop.disabled = too;
    pop.hidden = false;
    var pw = pop.offsetWidth, left = Math.min(Math.max(8, rect.left + rect.width / 2 - pw / 2), innerWidth - pw - 8);
    var top = rect.top - 52; if (top < 8) top = rect.bottom + 12;
    pop.style.left = left + 'px'; pop.style.top = top + 'px';
  }
  document.addEventListener('selectionchange', function () { clearTimeout(tm); tm = setTimeout(update, 200); });
  var raf = 0; function follow() { if (pop.hidden || raf) return; raf = requestAnimationFrame(function () { raf = 0; update(); }); }
  addEventListener('scroll', follow, { passive: true }); addEventListener('resize', follow);
  pop.addEventListener('pointerdown', function (e) { e.preventDefault(); });
  pop.addEventListener('click', function () { if (!pending || pending.too) return; var p = pending; hidePop(); getSelection().removeAllRanges(); openCard(p.text, p.type, p.url); });

  /* the gallery of ready-made cards */
  Array.prototype.forEach.call(document.querySelectorAll('.take'), function (f) {
    var src = f.getAttribute('data-src'), text = f.getAttribute('data-text');
    function blob() { return fetch(src).then(function (r) { return r.blob(); }); }
    f.querySelector('[data-t=share]').addEventListener('click', function () { blob().then(function (b) { return nativeShare(b, text, canon); }); });
    f.querySelector('[data-t=dl]').addEventListener('click', function () { blob().then(function (b) { download(b, f.getAttribute('data-id') + '.jpg'); }); });
    f.querySelector('[data-t=wa]').href = 'https://wa.me/?text=' + encodeURIComponent('“' + text + '”\n' + canon);
  });
})();
