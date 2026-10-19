/* Shared by the story pages (/bmh, /repair-cafe, /incubator) and the homepage.
   Share buttons: <button data-share="/repair-cafe" data-title="...">. On phones this opens the
   native share sheet; elsewhere it copies the link and shows a short confirmation. */
(() => {
  const toast = (msg) => {
    let t = document.querySelector('.toast');
    if (!t) { t = document.createElement('div'); t.className = 'toast'; t.setAttribute('role', 'status'); document.body.appendChild(t); }
    t.innerHTML = '<i class="ph ph-check" aria-hidden="true"></i> ' + msg;
    t.classList.add('on'); clearTimeout(t._h); t._h = setTimeout(() => t.classList.remove('on'), 2400);
  };
  const copy = async (url) => {
    try { await navigator.clipboard.writeText(url); toast('Link copied'); }
    catch (e) { window.prompt('Copy this link', url); }
  };
  document.addEventListener('click', async (e) => {
    const b = e.target.closest('[data-share]'); if (!b) return;
    e.preventDefault();
    const url = new URL(b.dataset.share || location.pathname, location.origin).href;
    const title = b.dataset.title || document.title;
    const touch = matchMedia('(hover: none)').matches;
    if (navigator.share && touch) { try { await navigator.share({ title, url }); return; } catch (err) { if (err && err.name === 'AbortError') return; } }
    copy(url);
  });

  /* reveals on the story pages: items already on screen show at once */
  if (!document.body.hasAttribute('data-story') || !document.documentElement.classList.contains('js')) return;
  const els = [...document.querySelectorAll('.rv')];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!els.length) return;
  if (reduce || !('IntersectionObserver' in window)) { els.forEach(e => e.classList.add('in')); return; }
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -6% 0px' });
  els.forEach(e => { if (e.getBoundingClientRect().top < innerHeight) e.classList.add('in'); else io.observe(e); });
  addEventListener('beforeprint', () => els.forEach(e => e.classList.add('in')));
})();
