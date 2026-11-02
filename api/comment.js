// Anonymous comments for articles. Comments go to a private Notion database (Status: New).
// Only comments the author marks "Approved" in Notion are shown publicly under the article.
// Env vars (Vercel): NOTION_TOKEN, NOTION_COMMENTS_DB. Optional rate limiting uses the same Redis as /api/views.
// GET  /api/comment?slug=<slug>  -> { configured:true, comments:[{text,date}] }   (503 { configured:false } until set up)
// POST /api/comment {slug,text,website,ms} -> { ok:true }
const crypto = require('crypto');
const TOKEN = process.env.NOTION_TOKEN, DB = process.env.NOTION_COMMENTS_DB;
const RURL = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL, RTOK = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN;
const H = { 'Authorization': 'Bearer ' + TOKEN, 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json' };

async function redis(cmd) {
  const r = await fetch(RURL, { method: 'POST', headers: { Authorization: 'Bearer ' + RTOK, 'Content-Type': 'application/json' }, body: JSON.stringify(cmd) });
  if (!r.ok) throw new Error('redis ' + r.status);
  return (await r.json()).result;
}
async function tooMany(req) {
  if (!RURL || !RTOK) return false;
  try {
    const ip = String((req.headers['x-forwarded-for'] || '').split(',')[0] || 'x').trim();
    const key = 'rl:comment:' + crypto.createHash('sha256').update(ip + 'medinn').digest('hex').slice(0, 24);
    const n = Number(await redis(['INCR', key])) || 0;
    if (n === 1) await redis(['EXPIRE', key, 3600]);
    return n > 3;
  } catch (e) { return false; }
}

module.exports = async (req, res) => {
  if (!TOKEN || !DB) { res.setHeader('Cache-Control', 'no-store'); return res.status(503).json({ configured: false }); }
  let b = req.body; if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } } b = b || {};
  const slug = String((req.method === 'POST' ? b.slug : (req.query && req.query.slug)) || '');
  if (!/^[a-z0-9-]{3,80}$/.test(slug)) return res.status(400).json({ error: 'bad_slug' });

  if (req.method === 'GET') {
    res.setHeader('Cache-Control', 'public, s-maxage=60, stale-while-revalidate=300');
    try {
      const r = await fetch('https://api.notion.com/v1/databases/' + DB + '/query', { method: 'POST', headers: H, body: JSON.stringify({
        filter: { and: [{ property: 'Status', select: { equals: 'Approved' } }, { property: 'Article', rich_text: { equals: slug } }] },
        sorts: [{ timestamp: 'created_time', direction: 'descending' }], page_size: 20 }) });
      if (!r.ok) return res.status(200).json({ configured: true, comments: [] }); // e.g. read access not enabled yet: the box still works, nothing is shown
      const j = await r.json();
      const comments = (j.results || []).map(p => ({ text: ((p.properties['Full comment'] || {}).rich_text || []).map(t => t.plain_text).join(''), date: p.created_time })).filter(c => c.text);
      return res.status(200).json({ configured: true, comments });
    } catch (e) { return res.status(200).json({ configured: true, comments: [] }); }
  }
  if (req.method !== 'POST') { res.setHeader('Allow', 'GET, POST'); return res.status(405).json({ error: 'method_not_allowed' }); }

  if (b.website) return res.status(200).json({ ok: true });                       // honeypot
  const text = String(b.text || '').replace(/\r/g, '').trim();
  if (text.length < 10) return res.status(400).json({ error: 'too_short' });
  if (text.length > 1000) return res.status(400).json({ error: 'too_long' });
  if ((text.match(/https?:\/\//gi) || []).length > 1) return res.status(400).json({ error: 'too_many_links' });
  if (Number(b.ms) < 3000) return res.status(400).json({ error: 'too_fast' });      // a human takes more than 3 seconds to write
  if (await tooMany(req)) return res.status(429).json({ error: 'slow_down' });

  try {
    const title = text.replace(/\s+/g, ' ').slice(0, 80) + (text.length > 80 ? '…' : '');
    const r = await fetch('https://api.notion.com/v1/pages', { method: 'POST', headers: H, body: JSON.stringify({ parent: { database_id: DB }, properties: {
      'Comment': { title: [{ type: 'text', text: { content: title } }] },
      'Full comment': { rich_text: [{ type: 'text', text: { content: text } }] },
      'Article': { rich_text: [{ type: 'text', text: { content: slug } }] },
      'Status': { select: { name: 'New' } } } }) });
    if (!r.ok) { console.error('notion_error', r.status, await r.text()); return res.status(502).json({ error: 'notion_error' }); }
    return res.status(200).json({ ok: true });
  } catch (e) { console.error('notion_exception', e); return res.status(502).json({ error: 'notion_error' }); }
};
