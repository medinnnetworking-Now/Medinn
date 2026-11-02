/* Anonymous comment box. Appears only when the server is connected to Notion (GET /api/comment says configured).
   Comments are private to the author until he marks them Approved in Notion; approved ones are listed here. */
(function () {
  var sec = document.getElementById('comments'); if (!sec) return;
  var slug = sec.getAttribute('data-slug'), t0 = Date.now();
  var list = sec.querySelector('.cm-list'), form = sec.querySelector('form'), msg = sec.querySelector('.cm-msg'), ta = form.querySelector('textarea'), cnt = sec.querySelector('.cm-count'), btn = form.querySelector('button');
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  fetch('/api/comment?slug=' + encodeURIComponent(slug)).then(function (r) { return r.ok ? r.json() : null; }).then(function (j) {
    if (!j || !j.configured) return;
    sec.hidden = false;
    if (j.comments && j.comments.length) {
      list.innerHTML = '<h3>What readers said</h3>' + j.comments.map(function (c) { return '<blockquote>' + esc(c.text).replace(/\n/g, '<br>') + '</blockquote>'; }).join('');
    }
  }).catch(function () {});
  ta.addEventListener('input', function () { cnt.textContent = ta.value.length + ' / 1000'; });
  form.addEventListener('submit', function (e) {
    e.preventDefault(); msg.className = 'cm-msg'; msg.textContent = '';
    var text = ta.value.trim();
    if (text.length < 10) { msg.className = 'cm-msg err'; msg.textContent = 'Please write a little more (at least 10 characters).'; return; }
    btn.disabled = true;
    fetch('/api/comment', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ slug: slug, text: text, website: form.website.value, ms: Date.now() - t0 }) })
      .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
      .then(function (x) {
        if (x.ok && x.j.ok) { ta.value = ''; cnt.textContent = '0 / 1000'; msg.className = 'cm-msg ok'; msg.textContent = 'Thank you. It has reached Dr. Sidharth privately. Some comments may be shown here after he reads them.'; }
        else if (x.j && x.j.error === 'slow_down') { msg.className = 'cm-msg err'; msg.textContent = 'You have sent a few already. Please try again in a while.'; }
        else if (x.j && x.j.error === 'too_many_links') { msg.className = 'cm-msg err'; msg.textContent = 'Please keep it to one link or none.'; }
        else if (x.j && x.j.error === 'too_fast') { msg.className = 'cm-msg err'; msg.textContent = 'Take a moment to write it, then send.'; }
        else throw 0;
      }).catch(function () { msg.className = 'cm-msg err'; msg.textContent = 'That did not go through. Please try again in a moment.'; })
      .then(function () { btn.disabled = false; });
  });
})();
