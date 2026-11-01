/* Renders the subscribe buttons into every .sub-slot, only when the channel link is set in config.js. */
(function () {
  var c = (window.MEDINN_SUBSCRIBE || {}).whatsappChannel || '';
  var slots = document.querySelectorAll('.sub-slot');
  if (!/^https:\/\/(www\.)?whatsapp\.com\/channel\//.test(c)) { slots.forEach(function (s) { s.remove(); }); return; }
  var icon = '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.2 14.2c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.2-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.8s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.4.6-.3.3c-.1.2-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.1 1 2 1.3 2.3 1.4.3.2.5.1.6-.1l.8-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.8-.1 1.4z"/></svg>';
  slots.forEach(function (s) {
    var v = s.getAttribute('data-variant') || 'bar';
    var btn = '<a class="sub-btn" href="' + c + '" target="_blank" rel="noopener">' + icon + ' Get each article on WhatsApp</a>';
    s.innerHTML = v === 'box' ? btn : '<p><b>One article a week</b> on reforming medical education, from a house surgeon&rsquo;s lens.</p>' + btn;
  });
})();
