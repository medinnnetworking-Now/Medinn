// Reads counter for articles. Stored in Upstash Redis (add it from Vercel: Storage > Create > Upstash Redis, connect to this project).
// GET  /api/views?slug=<slug>   -> { views }          (returns { configured:false } with 503 until Redis is connected)
// POST /api/views {slug}        -> { views }          (counts one read; bots are ignored)
const URL_ = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL;
const TOKEN = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN;
const BOT = /bot|crawl|spider|preview|facebookexternalhit|slurp|whatsapp|telegram|headless|lighthouse|monitor|curl|wget/i;

async function redis(cmd) {
  const r = await fetch(URL_, { method: 'POST', headers: { Authorization: 'Bearer ' + TOKEN, 'Content-Type': 'application/json' }, body: JSON.stringify(cmd) });
  if (!r.ok) throw new Error('redis ' + r.status);
  return (await r.json()).result;
}

module.exports = async (req, res) => {
  if (!URL_ || !TOKEN) { res.setHeader('Cache-Control', 'no-store'); return res.status(503).json({ configured: false }); }
  const slug = String((req.method === 'POST' ? (req.body && req.body.slug) : req.query && req.query.slug) || '');
  if (!/^[a-z0-9-]{3,80}$/.test(slug)) return res.status(400).json({ error: 'bad_slug' });
  const key = 'views:' + slug;
  try {
    if (req.method === 'POST') {
      const ua = String(req.headers['user-agent'] || '');
      const n = BOT.test(ua) || !ua ? Number(await redis(['GET', key])) || 0 : Number(await redis(['INCR', key])) || 0;
      res.setHeader('Cache-Control', 'no-store');
      return res.status(200).json({ views: n });
    }
    if (req.method === 'GET') {
      res.setHeader('Cache-Control', 'public, s-maxage=30, stale-while-revalidate=120');
      return res.status(200).json({ views: Number(await redis(['GET', key])) || 0 });
    }
    res.setHeader('Allow', 'GET, POST'); return res.status(405).json({ error: 'method_not_allowed' });
  } catch (e) { console.error('views_error', e); return res.status(502).json({ error: 'store_error' }); }
};
