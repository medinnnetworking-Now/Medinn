// Vercel serverless function: receives a private reply to a "PoH Asks" card and writes it to the
// same Notion database as the nominations (Submitter type = "Ask reply"). Replies are never shown publicly.
// Uses the same env vars as nominate.js: NOTION_TOKEN and NOTION_NOMINATIONS_DB.

const clean = (v, max) => String(v == null ? '' : v).replace(/\r/g, '').trim().slice(0, max);
const text = (v) => ({ rich_text: v ? [{ type: 'text', text: { content: v } }] : [] });

module.exports = async (req, res) => {
  if (req.method === 'GET') {
    res.setHeader('Cache-Control', 'no-store');
    return res.status(200).json({ configured: !!(process.env.NOTION_TOKEN && process.env.NOTION_NOMINATIONS_DB) });
  }
  if (req.method !== 'POST') { res.setHeader('Allow', 'GET, POST'); return res.status(405).json({ error: 'method_not_allowed' }); }
  let b = req.body;
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  b = b || {};
  if (b.website) return res.status(200).json({ ok: true }); // honeypot

  const name = clean(b.name, 200), contact = clean(b.contact, 300), how = clean(b.how, 1900);
  const person = clean(b.person, 40), company = clean(b.company, 300);
  const asks = (Array.isArray(b.asks) ? b.asks : []).map((a) => clean(a, 10)).filter((a) => /^ASK-\d{1,3}$/.test(a)).slice(0, 12);
  if (!name || !contact || !how || !asks.length) return res.status(400).json({ error: 'missing_fields' });

  const token = process.env.NOTION_TOKEN, db = process.env.NOTION_NOMINATIONS_DB;
  if (!token || !db) return res.status(503).json({ error: 'not_configured' });

  const props = {
    'Nominee': { title: [{ type: 'text', text: { content: name } }] },
    'Role and organisation': text(company),
    'What they have built or lead': text('Offer: ' + how),
    'Why they belong among the 50': text('Reply to ' + (person || 'PoH Asks') + ': ' + asks.join(', ')),
    'Nominee contact': text(contact),
    'Submitted by': text(name),
    'Submitter contact': text(contact),
    'Submitter type': { select: { name: 'Ask reply' } },
    'Status': { select: { name: 'New' } }
  };
  try {
    const r = await fetch('https://api.notion.com/v1/pages', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer ' + token, 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json' },
      body: JSON.stringify({ parent: { database_id: db }, properties: props })
    });
    if (!r.ok) { console.error('notion_error', r.status, await r.text()); return res.status(502).json({ error: 'notion_error' }); }
    return res.status(200).json({ ok: true });
  } catch (e) {
    console.error('notion_exception', e);
    return res.status(502).json({ error: 'notion_error' });
  }
};
