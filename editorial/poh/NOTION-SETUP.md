# Turn on the People of Healthcare discovery form (Notion)

Everything is built and live. The form stays hidden until the site can talk to Notion. This takes about 5 minutes and needs no code.

The database already exists: **People of Healthcare: Nominations**
https://app.notion.com/p/5b140e8313a345de87158c76ec6b00a7

## Step 1: Create a Notion integration (the key)
1. Go to https://www.notion.so/profile/integrations
2. Click **New integration**.
3. Name: `Medinn website`. Workspace: your Medinn workspace. Type: **Internal**.
4. On the **Capabilities** tab: tick **Insert content** only. Untick Read and Update content.
5. Save, then click **Show** under *Internal Integration Secret* and copy it. It starts with `ntn_` or `secret_`. Treat it like a password.

## Step 2: Let the integration into the database
1. Open the Nominations database link above in Notion.
2. Click the **⋯** menu (top right) > **Connections** (or **Add connections**).
3. Search for `Medinn website` and confirm.

If you skip this, every submission fails and the form shows the email/WhatsApp fallback.

## Step 3: Give the key to the website (Vercel)
1. Open https://vercel.com, team **medinn**, project **medinn**.
2. **Settings** > **Environment Variables**.
3. Add two variables, both for **Production** and **Preview**:
   - Name `NOTION_TOKEN`: Value = the secret from Step 1.
   - Name `NOTION_NOMINATIONS_DB`: Value = `5b140e8313a345de87158c76ec6b00a7`
4. Click **Save**.

Paste the secret directly into Vercel, not into chat or email.

## Step 4: Redeploy so the website picks them up
1. **Deployments** tab > the top entry marked **Production** > **⋯** > **Redeploy**.
2. Wait about a minute for it to say Ready.

## Step 5: Check it
1. Open https://medinn.in/people-of-healthcare and refresh.
2. You should now see a **Fill the discovery form** button in the Take part section, a **Discovery form** section, and the hero "Nominate someone" link jumps to the form.
3. Tell me, and I will send a test entry through the live form, confirm it arrives in Notion as **New**, and delete it.

## What you'll see in Notion
Each submission is a row with: nominee, role and organisation, segment, what they built, why they belong among the 50, contact details, who submitted it, whether it is a nomination or a self-introduction, and a **Status** (New, Reviewing, Reached out, Scheduled, Done, Not now). Create a Board view grouped by Status to run the 50 like a pipeline.

## If something doesn't work
- Form still hidden after redeploy: the two variables are missing or misspelled, or the redeploy hasn't finished. Check names are exactly `NOTION_TOKEN` and `NOTION_NOMINATIONS_DB`.
- Form shows "That did not go through": Step 2 was skipped (the integration isn't connected to the database), or the token was pasted with extra spaces.
- To pause the form at any time, delete `NOTION_TOKEN` in Vercel and redeploy; the page falls back to email and WhatsApp automatically.
