/* Visit counter. Every new visit (a new browser session) adds one, after 6 seconds on the page, so quick bounces and bots don't count.
   Reloading the page in the same tab does not add another. The number updates live while a reader stays on the page.
   Hidden until the counter service (Upstash Redis) is connected. Open any page once with ?owner=1 to exclude your own browser (?owner=0 undoes it). */
(function () {
  var el = document.getElementById('views'); if (!el) return;
  var slug = el.getAttribute('data-slug'), prefix = el.hasAttribute('data-prefix') ? el.getAttribute('data-prefix') : ' · ', ss = null, ls = null;
  try { ss = window.sessionStorage; ls = window.localStorage; } catch (e) {}
  try { if (/[?&]owner=1/.test(location.search)) ls.setItem('medinn-owner', '1'); if (/[?&]owner=0/.test(location.search)) ls.removeItem('medinn-owner'); } catch (e) {}
  var owner = false, key = 'medinn-visit:' + slug, counted = false;
  try { owner = ls.getItem('medinn-owner') === '1'; counted = !!ss.getItem(key); } catch (e) {}
  function show(n) { if (typeof n !== 'number') return; el.textContent = prefix + n.toLocaleString('en-IN') + (n === 1 ? ' visit' : ' visits'); el.hidden = false; }
  function read() { fetch('/api/views?slug=' + encodeURIComponent(slug), { cache: 'no-store' }).then(function (r) { return r.ok ? r.json() : null; }).then(function (j) { if (j) show(j.views); }).catch(function () {}); }
  read();
  setInterval(function () { if (!document.hidden) read(); }, 60000);   /* live: pick up other visitors while this page is open */
  if (owner || counted) return;
  setTimeout(function () {
    if (document.hidden) return;
    fetch('/api/views', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ slug: slug }) })
      .then(function (r) { return r.ok ? r.json() : null; }).then(function (j) { if (j) { show(j.views); try { ss.setItem(key, '1'); } catch (e) {} } }).catch(function () {});
  }, 6000);
})();
