# Turn on the visit counter and the anonymous comment box

Both are built and live in the code. Each stays hidden until its service is connected, so nobody sees anything broken.

## A. Visit counter (needs the free Redis store)
1. Open https://vercel.com/medinn/medinn/stores (or the project's **Storage** tab).
2. **Create database** > **Upstash (Redis)** > free plan > connect it to the **medinn** project for all environments. Vercel adds the keys by itself.
3. Redeploy (https://vercel.com/medinn/medinn/deployments > top Production > ... > Redeploy).
4. Open the article. After a few seconds you should see "N visits" in the byline, and on the series page under the title.
- What counts: each new visit (a new browser session) after 6 seconds on the page. Reloading in the same tab does not add one. Bots and link-preview crawlers are ignored. The number refreshes every minute for people who stay on the page.
- Exclude yourself: open any page once with `?owner=1` on the end of the address (each browser or phone you use). `?owner=0` undoes it.

## B. Anonymous comment box (needs Notion)
The database already exists: **Article Comments (anonymous)**
https://app.notion.com/p/801b7e6b1fd34538903bdb0074f8cbf7
Database id `801b7e6b1fd34538903bdb0074f8cbf7` (data source `collection://acfc6d70-9b9d-43cc-8eda-ec712b49a943`).
1. In Notion, open that database > ... > **Connections** > add **Medinn website** (the same connection used for nominations).
2. In Vercel > Settings > Environment Variables, add `NOTION_COMMENTS_DB` = `801b7e6b1fd34538903bdb0074f8cbf7` (Production and Preview). Then redeploy.
3. The box appears under the article. Every comment arrives in Notion with Status **New**, private to you.
4. To show a comment publicly: change its Status to **Approved**. To keep it private or remove it: **Hidden**.
5. **To let approved comments show on the page**, the Notion connection also needs **Read content**: Notion > Settings > Connections > Medinn website > Capabilities > tick **Read content**. Without it the box still works and collects comments privately, but nothing is shown publicly.
- Protection: honeypot field, minimum writing time, 10 to 1000 characters, at most one link, and 3 comments per hour per person (the limit needs Redis from step A). Nothing about the writer (name, IP) is saved with the comment.
