// Vercel serverless function: receives the People of Healthcare discovery form and
// writes it to the Notion "People of Healthcare: Nominations" database.
// Needs two environment variables in Vercel: NOTION_TOKEN and NOTION_NOMINATIONS_DB.

const SEGMENTS = ['Hospital group or leader', 'Medical devices and manufacturing', 'Diagnostics', 'Biotech and research',
  'Digital health and technology', 'Healthcare entrepreneur or founder', 'Investor', 'Clinician-builder', 'Other'];
const TYPES = ['Nominating someone else', 'Self-introduction'];

const clean = (v, max) => String(v == null ? '' : v).replace(/\r/g, '').trim().slice(0, max);
const text = (v) => ({ rich_text: v ? [{ type: 'text', text: { content: v } }] : [] });

module.exports = async (req, res) => {
  if (req.method === 'GET') { // the page asks this to decide whether to show the form
    res.setHeader('Cache-Control', 'no-store');
    return res.status(200).json({ configured: !!(process.env.NOTION_TOKEN && process.env.NOTION_NOMINATIONS_DB) });
  }
  if (req.method !== 'POST') { res.setHeader('Allow', 'GET, POST'); return res.status(405).json({ error: 'method_not_allowed' }); }
  let b = req.body;
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  b = b || {};

  if (b.website) return res.status(200).json({ ok: true }); // honeypot: bots fill this, people never see it

  const nominee = clean(b.nominee, 200), by = clean(b.by, 200), byContact = clean(b.byContact, 300);
  if (!nominee || !by || !byContact) return res.status(400).json({ error: 'missing_fields' });

  const token = process.env.NOTION_TOKEN, db = process.env.NOTION_NOMINATIONS_DB;
  if (!token || !db) return res.status(503).json({ error: 'not_configured' });

  const props = {
    'Nominee': { title: [{ type: 'text', text: { content: nominee } }] },
    'Role and organisation': text(clean(b.role, 500)),
    'What they have built or lead': text(clean(b.built, 1900)),
    'Why they belong among the 50': text(clean(b.why, 1900)),
    'Nominee contact': text(clean(b.nomineeContact, 300)),
    'Submitted by': text(by),
    'Submitter contact': text(byContact),
    'Status': { select: { name: 'New' } }
  };
  if (SEGMENTS.includes(b.segment)) props['Segment'] = { select: { name: b.segment } };
  if (TYPES.includes(b.type)) props['Submitter type'] = { select: { name: b.type } };

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
