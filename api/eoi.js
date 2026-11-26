// Vercel serverless function: receives the CMC Analytica Expression of Interest form and
// writes it to a private Notion database. Needs env vars: NOTION_TOKEN (already set) and NOTION_EOI_DB.
// Until NOTION_EOI_DB is set, GET returns { configured:false } and the page offers WhatsApp and email instead.
const STAGES = ['MBBS 1st year', 'MBBS 2nd year', 'MBBS 3rd year', 'Final year', 'Intern', 'Post-intern', 'Other'];
const WANTS = ['Learn the basics', 'Find a guide', 'Join a project', 'Prepare for PG or residency', 'Get ready for future research'];
const EXPS = ['None yet', 'A little', 'I have a project or paper'];
const clean = (v, max) => String(v == null ? '' : v).replace(/\r/g, '').trim().slice(0, max);
const text = (v) => ({ rich_text: v ? [{ type: 'text', text: { content: v } }] : [] });

module.exports = async (req, res) => {
  if (req.method === 'GET') {
    res.setHeader('Cache-Control', 'no-store');
    return res.status(200).json({ configured: !!(process.env.NOTION_TOKEN && process.env.NOTION_EOI_DB) });
  }
  if (req.method !== 'POST') { res.setHeader('Allow', 'GET, POST'); return res.status(405).json({ error: 'method_not_allowed' }); }
  let b = req.body;
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  b = b || {};
  if (b.website) return res.status(200).json({ ok: true }); // honeypot
  if (Number(b.ms) < 3000) return res.status(400).json({ error: 'too_fast' });

  const name = clean(b.name, 200), contact = clean(b.contact, 300);
  if (!name || !contact) return res.status(400).json({ error: 'missing_fields' });
  const token = process.env.NOTION_TOKEN, db = process.env.NOTION_EOI_DB;
  if (!token || !db) return res.status(503).json({ error: 'not_configured' });

  const props = {
    'Name': { title: [{ type: 'text', text: { content: name } }] },
    'Contact': text(contact),
    'College': text(clean(b.college, 300)),
    'Topics or domains of interest': text(clean(b.topics, 1900)),
    'Question or query': text(clean(b.question, 1900)),
    'Heard about us': text(clean(b.heard, 300)),
    'Status': { select: { name: 'New' } }
  };
  if (STAGES.includes(b.stage)) props['Stage'] = { select: { name: b.stage } };
  if (EXPS.includes(b.experience)) props['Experience'] = { select: { name: b.experience } };
  const wants = (Array.isArray(b.wants) ? b.wants : []).filter((w) => WANTS.includes(w));
  if (wants.length) props['Looking for'] = { multi_select: wants.map((name) => ({ name })) };

  try {
    const r = await fetch('https://api.notion.com/v1/pages', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer ' + token, 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json' },
      body: JSON.stringify({ parent: { database_id: db }, properties: props })
    });
    if (!r.ok) { console.error('notion_error', r.status, await r.text()); return res.status(502).json({ error: 'notion_error' }); }
    return res.status(200).json({ ok: true });
  } catch (e) { console.error('notion_exception', e); return res.status(502).json({ error: 'notion_error' }); }
};
