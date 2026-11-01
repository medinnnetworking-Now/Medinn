/* Reads counter. Shows the number only when the counter service is connected. Counts a visitor once a day,
   after 6 seconds on the page, never counts bots or the author (open any article with ?owner=1 once to exclude your own browser). */
(function () {
  var el = document.getElementById('views'); if (!el) return;
  var slug = el.getAttribute('data-slug'), ls = null;
  try { ls = window.localStorage; } catch (e) {}
  try { if (/[?&]owner=1/.test(location.search)) ls.setItem('medinn-owner', '1'); if (/[?&]owner=0/.test(location.search)) ls.removeItem('medinn-owner'); } catch (e) {}
  var owner = false, key = 'medinn-read:' + slug + ':' + new Date().toISOString().slice(0, 10), done = false;
  try { owner = ls.getItem('medinn-owner') === '1'; done = !!ls.getItem(key); } catch (e) {}
  function show(n) { if (typeof n !== 'number') return; el.textContent = ' · ' + n.toLocaleString('en-IN') + (n === 1 ? ' read' : ' reads'); el.hidden = false; }
  fetch('/api/views?slug=' + encodeURIComponent(slug)).then(function (r) { return r.ok ? r.json() : null; }).then(function (j) { if (j) show(j.views); }).catch(function () {});
  if (owner || done) return;
  setTimeout(function () {
    if (document.hidden) return;
    fetch('/api/views', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ slug: slug }) })
      .then(function (r) { return r.ok ? r.json() : null; }).then(function (j) { if (j) { show(j.views); try { ls.setItem(key, '1'); } catch (e) {} } }).catch(function () {});
  }, 6000);
})();
