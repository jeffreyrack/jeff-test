# Marketplace-native ideas — The Marketplace Native

_Run 2026-10-06, round 2. Persona: The Marketplace Native. All counts were pulled live on 2026-10-06 from public marketplace APIs: the Apify Store API (`api.apify.com/v2/store`, `/v2/acts/<id>`), the Atlassian Marketplace REST API (`marketplace.atlassian.com/rest/2/addons…`, including `/versions/latest` and `/pricing/cloud/live`), the public Atlassian issue tracker (`jira.atlassian.com/rest/api/2/search`), the WordPress.org plugin API, and Wix App Market search pages._

## Research notes (read before the ideas)

1. **"Few listings" no longer signals a gap, because AI-built listings now flood the long tail of every marketplace I checked.** The evidence:
   - **Apify:** I scanned about 230 search terms. Almost every term with any demand returns 20–30 matching Actors. "Google Trends" alone has **about 40 Actors**, including two that already offer the "more than 5 keywords, anchor-normalised" feature I had planned as a differentiator. Most of these have 0–20 monthly users. The same few publishers (automation-lab, khadinakbar, memo23, johnvc and others) appear on every shelf. Prediction markets show the same pattern: 15+ Kalshi/Polymarket Actors.
   - **Chrome Web Store:** a search for "kalshi" returns 9 extensions, all with 0 ratings.
   - **Wix App Market:** a search for "waitlist" returns 7 appointment-waitlist apps, 5 of them with 0 reviews.
   - **Atlassian:** one vendor ("appsplus") has published "Figma+", "Miro+", "Zeplin+" and "Replit+" Forge clones within the last week.
   - **WordPress.org:** none of the 14 terms I searched has a stale incumbent with 10k+ installs.
2. **The gaps that remain are deadline-driven or quality-driven,** meaning paying users stranded by a platform change or by a broken incumbent. I looked for three things:
   - (a) many installs or runs sitting on a listing that is **abandoned, failing or about to be cut off**;
   - (b) proof that buyers **already pay** in that category;
   - (c) a replacement that needs **more than a shallow clone**. Examples are migration tooling or reliability engineering, which a one-shot AI clone usually skips.
3. **The biggest event of this kind in any billing marketplace right now is Atlassian's Connect end of support.**
   - Atlassian moved the cut-off to **31 January 2027**.
   - Since July–September 2026, customers of non-migrated apps see "This app may stop working after January 2027" banners in the app UI and in admin. Partners on Atlassian's developer forum say the banner "kills all potential new trials" of affected apps.
   - My scan of the 1,500 most popular cloud apps found:
     - **239 Connect apps whose last release predates 17 Sep 2025**, with about 198k installs between them;
     - **88 of those are paid via Atlassian** (about 32k installs), so the buyers already pay.
   - Since 1 Jan 2026, Atlassian takes **0% revenue share on the first $1M of lifetime Forge revenue**. M1 and M2 target this shock.
4. **Platform concentration (lesson 4).**
   - **M1 and M2 share one Atlassian partner account.** I accept this deliberately, because Atlassian is the only marketplace where I found a quantified, deadline-driven, already-paying gap. Atlassian acts on listings one app at a time and has no Etsy-style messaging trap. Still, **the committee should pick at most one of M1/M2** and treat the other as a phase-2 listing.
   - **M3 is on Apify,** as are last run's T2 and this round's G1/G2 (agent-economist). M3 should be read as an *alternative* Apify slot, not an addition.

---

## M1 — ChatRelay for Jira: Forge-native Google Chat notifications that replace Google's abandoned "Google Chat for Jira Cloud"

- **Persona:** The Marketplace Native
- **One-liner:** A Forge app on the Atlassian Marketplace. It posts Jira work-item events into Google Chat spaces with per-project and per-JQL routing and one thread per issue. It is aimed at the roughly 11,000 Jira Cloud sites that installed Google's own Connect app. That app is broken, was last updated in 2021, and will show a "may stop working after January 2027" banner.
- **Marketplace & gap evidence:**
  - **The orphan.** "Google Chat for Jira Cloud" (vendor Google LLC, key `linovi-hangoutschat-bot`) has **11,008 installs** and a **2.3★ rating from 109 reviews**. It is a **Connect app last released 2021-11-11**. Its recent reviews are almost all 1★, for example:
    - "Doesn't work. Impossible to set up" (2026-08-14);
    - "The app is very old… notifications… does not work" (2026-02-25);
    - "Error in last step" (2025-04 to 2025-06, repeated).
  - **The replacements so far.** Every Forge alternative together has about **680 installs**:
    - Advanced Google Chat for Jira: 407 installs, free;
    - Jigo, a Google Workspace suite: 137 installs;
    - "Google Chat for Jira": 123 installs, paid;
    - ChatBridge: 16 installs.
    - "Google Chat Automation Actions for Jira" also exists; I could not get its install count.
    - So **about 94% of the orphan base has not moved yet.**
  - **Willingness to pay is proven.**
    - The paid Forge competitor charges **$5/mo for up to 10 users and $1.20/user/mo at 100 users**, which is $120/mo for a 100-user site.
    - The comparable Slack connector (WISOFT, paid via Atlassian) has 1,160 installs.
  - **Deadline and pressure.**
    - Atlassian moved Connect end of support to 31 Jan 2027.
    - Admin and in-app banners ("This app may stop working after January 2027…") have been rolling out since Jul–Sep 2026.
    - A Figma-for-Jira customer reported the "Legacy" flag in Atlassian admin on the Figma forum, 22 Sep 2026.
  - **Substitutes.**
    - Jira Automation has no native "Send Google Chat message" action. Admins can hand-roll "Send web request" calls to Google Chat webhooks.
    - Zapier and Pabbly have Jira→Google Chat zaps, but they cost a separate subscription.
- **Demand test:**
  - Publish v1 (event → space routing and issue threads) as a paid-via-Atlassian listing with a free tier for 10 users or fewer.
  - **Pass:** 20 or more installs, of which 6 or more are evaluations on sites with more than 10 users, within 21 days of the listing going live.
  - **Fail:** stop feature work, leave the app listed as maintenance-only, and redirect operator time to M2/M3.
  - A pre-check costs nothing: the Atlassian Marketplace API shows the competitors' install counts. If "Advanced Google Chat for Jira" gains more than 1,000 installs before our listing is live, re-assess.
- **Customer:**
  - **Who:** Jira Cloud admins at companies that run Google Workspace instead of Slack or Teams. Typically 20–500 Jira users: agencies, SaaS startups, schools and universities, LatAm and EU firms. One reviewer is "a company based in Colombia".
  - **Where they are:** they find apps inside Atlassian admin ("Find new apps") and on marketplace.atlassian.com, and they read Atlassian Community threads.
  - **What they already pay for:** Jira Standard/Premium seats, Google Workspace, and often other paid-via-Atlassian apps billed on the same Atlassian invoice.
- **Problem / desire:**
  - Their words, from the reviews: "It does not work. Integration fails with no indication on why or how to fix it." "I would only like to look at notifications wherever I'm tagged, watching, assigned… or all updates of a certain team."
  - The new pressure is a red banner in their own Jira saying the app may stop working after January 2027.
- **Offering:** A Forge app (Jira) with the following features.
  - **Admin page:** map projects or JQL filters to Google Chat space webhooks, and pick events (created, transitioned, assigned, commented, resolved, SLA breached for JSM).
  - **Threading:** one Chat thread per issue, using `threadKey` = issue key.
  - **Messages:** card-formatted messages with status, assignee and priority, and an "open in Jira" button.
  - **Mentions:** @-mention mapping by matching Atlassian and Google emails.
  - **Quiet hours** and a **daily digest** mode.
  - **Jira Automation action:** "Send to Google Chat", added as a Forge automation action.
  - **"Migrate from Google Chat for Jira Cloud" guide:** a step-by-step checklist that recreates the old per-project subscriptions in 5 minutes.
  - **Data handling:** webhook URLs are kept in Forge encrypted storage, and no customer data leaves Atlassian except the message sent to Google.
- **Price & revenue model:**
  - Paid via Atlassian, as a monthly or annual subscription by Jira user tier.
  - **Free for 10 users or fewer.** About $0.35/user/mo for 11–100 users, $0.25 for 101–250, and $0.15 above that. That is about 70% below the $1.20/user incumbent price.
  - Example bills: a 40-user site pays about $14/mo, a 150-user site about $45/mo, and the blended average is about $25 per paying site.
  - **$300/mo ≈ 12 paying sites.** Atlassian's revenue share is 0% on the first $1M of lifetime Forge revenue (from 1 Jan 2026), and Atlassian handles tax.
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Atlassian developer account, Forge CLI, free developer sites (Jira/Confluence) | $0 |
| Atlassian Marketplace partner profile and paid-via-Atlassian listing | $0 |
| Google Workspace space for testing webhooks: the sponsor's existing Workspace, a 14-day trial, or 1 month of Business Starter if neither is available | $0–8 |
| Privacy policy, docs and support page on GitHub Pages | $0 |
| **Total** | **$0–8** |

### Monthly running costs (excluding operator tokens)
- **Forge platform:** $0 expected. The 2026 free allowance includes 200,000 GB-seconds of functions, and posting a webhook takes milliseconds. Usage above the allowance is metered.
- **Atlassian revenue share:** 0% up to $1M lifetime Forge revenue. Payment processing and tax are included.
- **Google Chat incoming webhooks:** free.
- **Domain:** optional ($1/mo if bought).
- **Total:** about $0/mo.

### Customer acquisition plan
1. **Atlassian Marketplace search is the channel.**
   - The listing title and summary target the exact strings orphaned admins type: "Google Chat", "Hangouts Chat", "Google Chat for Jira Cloud replacement", "Connect migration".
   - The category is Communication/Notifications, and the listing qualifies for the "Runs on Atlassian" badge (no external backend).
2. **In-product discovery.**
   - Jira admins land in "Explore apps" inside Jira, and search there runs on the same index.
   - The banner on the orphan pushes them to search right now, before 31 Jan 2027.
3. **Conversion on the listing page.**
   - The listing page carries a "Switch in 5 minutes" migration guide, screenshots that mirror the old app's settings screen, and a comparison table against the free and paid alternatives.
   - Atlassian's 30-day evaluation then converts to paid automatically, using Atlassian's own billing.
4. **Retention.** Monthly changelog updates, and fast support through the Atlassian listing's support link, which routes to an API-connected inbox the operator answers.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Atlassian Marketplace and in-Jira search**
   - **Tactic:** exact-match listing copy for "Google Chat".
   - **Why it works with no audience:** there are only 5 Forge listings for that query and 11k sites are being pushed to look.
   - **Expected speed:** first installs within 1 week of listing approval.
2. **"Runs on Atlassian" and Forge-migration filters**
   - **Tactic:** qualify for the badge (no egress except the Google Chat webhook domain, which must be declared, so confirm eligibility rules at build time).
   - **Why it works:** security-conscious admins filter by the badge during Connect clean-ups.
   - **Expected speed:** the same as #1.
3. **Long-tail search pages on GitHub Pages**
   - **Tactic:** troubleshooting pages titled with the orphan's literal error strings ("There was an error processing your request. Go back to Google Chat and initiate the configuration again") and "Google Chat for Jira Cloud stopped working".
   - **Why it works:** these queries have near-zero competition and the searchers have urgent intent.
   - **Expected speed:** 3–8 weeks to index.
4. **Optional, human only:** the sponsor answers 2–3 existing Atlassian Community threads about the broken Google app, as a disclosed vendor and genuine participant. No bot posting. Expected speed: 1–3 weeks.

### Path to first sale
| When (from today, 6 Oct) | Step |
|---|---|
| Days 0–2 | The sponsor creates the Atlassian ID, developer console and Marketplace partner profile; enters bank and tax details and accepts the Marketplace Partner Agreement (about 2 h); and provides a Google Workspace test space. |
| Days 2–10 | The operator builds the Forge app (event triggers, admin UI, Chat card renderer, JQL routing, automation action), tests it on a free developer site, and writes the listing, docs, privacy policy and security self-assessment. |
| Day ~10 | Submit for Marketplace approval. Atlassian says 5–10 business days, with 2026 reports of 3+ weeks, so the listing goes live around day 17–31 (23 Oct – 6 Nov). |
| Days 18–35 | First evaluation installs. The demand test runs here. |
| ~Day 50–100 | Evaluations last 30 days and **co-terminate with the customer's monthly billing cycle (30–60 days in practice)**, so the first paid conversion lands between late November and mid-January. A few customers click "Buy now" without trialling. |
| Cash | Atlassian remits **only after $500 of cumulative profit**, within 30 days of month-end. At 12–15 paying sites this is about 1–2 months of revenue, so the first cash is likely March–April 2027. |

**Ideator estimate: first sale about day 70 (≈ 15 Dec 2026). Range 50–100 days. First cash about day 150–190.**

### Who does what
- **AI operator:**
  - Builds, tests and deploys with the Forge CLI.
  - Writes the listing, docs and troubleshooting pages.
  - Answers support email.
  - Monitors install and evaluation counts through the Marketplace reporting API.
  - Ships monthly updates and tracks the competitor listings' install counts weekly.
- **Human sponsor:**
  - **One-time (about 2–2.5 h):** Atlassian partner signup, bank and tax forms, legal acceptance of the Marketplace Partner Agreement, and the Workspace test space.
  - **Recurring (about 0.25 h/week):** glance at the payout and approval emails, and approve any pricing change, which needs the partner admin login.

### Moat — why not just ask ChatGPT?
- **The chatbot is irrelevant here.** This is a running integration, not content. The real substitutes are:
  - an admin hand-rolling "Send web request" automation rules for each project;
  - Zapier, which is a separate subscription and sends data outside Atlassian;
  - the free competitor.
- **Our edge:**
  - (1) We are present in the one search box every orphaned admin uses, during a hard deadline.
  - (2) Forge-native, with no external backend: data stays in Atlassian. This is the reason admins are being told to switch.
  - (3) A migration guide built around the old app's exact settings.
  - (4) It sits on the Atlassian invoice, so there is no new vendor to onboard.
- **The moat is thin.** Distribution timing plus reviews. The first 20 reviews on the listing are the real defensive asset.

### Biggest risks (ideator's own view)
- **Google ships a Forge rewrite before the deadline,** or Atlassian adds a native Google Chat automation action. Either would remove most demand. Google has not updated the app since 2021, which suggests neither is likely before January.
- **The free competitor ("Advanced Google Chat for Jira", 407 installs, free) caps the price,** and AI-farm clones may appear within weeks. Our pricing must rely on the free tier for 10 users or fewer, plus better routing and threading.
- **Cash is slow:**
  - the review queue (up to 3+ weeks);
  - 30–60-day evaluations;
  - Atlassian's $500 payout threshold.
  - So the first dollar *banked* is about 5 months out, even though the first *sale* is about 2 months out.

---

## M2 — SpecView for Confluence: Forge OpenAPI/Swagger docs macro with one-click migration from orphaned Connect macros

- **Persona:** The Marketplace Native
- **One-liner:** A Forge Confluence macro that renders OpenAPI 3.x, Swagger 2.0 and AsyncAPI specs from page attachments or inline text. Its distinctive feature is an admin "migration scan" that finds every page using one of four abandoned Connect Swagger macros and rewrites those pages to SpecView with the spec preserved. The scan includes a preview and a one-click rollback.
- **Marketplace & gap evidence:**
  - **Four paid-via-Atlassian Connect apps in this one category have no release since before the Sept 2025 Connect freeze:**

    | App | Vendor | Installs | Rating | Last release |
    |---|---|---|---|---|
    | Open API (Swagger) Integration | Toshihiro Sato | 2,873 | 4.4★/31 | 2024-09-19 |
    | Visualize OpenAPI (Swagger) documentation | Dutch Beginners | 1,218 | 4.3★/21 | 2024-11-16 |
    | Swagger UI for Confluence | Tech Labs | 657 | 4.5★/8 | 2025-04-24 |
    | Open API (Swagger) Editor for Confluence | EliteSoft | 601 | 4.6★/9 | 2024-09-25 |

    - SwaggerHub Integration for Confluence (153 installs, 2022) is also stale.
    - **Total: about 5,500 installs of apps that customers already pay for.** The two largest charge $1/mo for 10 users and about $0.10/user/mo at 100 users.
  - **The same solo vendor (Toshihiro Sato) also has three more stale paid Connect diagram macros,** which make a phase-2 migration target:
    - Mermaid Integration: 582 installs;
    - Flowchart & PlantUML: 542 installs;
    - Figma Viewer: 410 installs.
  - **Forge alternatives already listed:**
    - one multi-macro bundle, "PlantUML, Swagger, drawio.xml, Mermaid…", with 3,186 installs at $0.25/user;
    - smaller ones: Narva (387 installs, free), appsplus "Swagger UI+" (201 installs, launched in 2026), AsyncAPI & OpenAPI (124 installs) and RapiDoc (74 installs).
    - **None of them advertises converting existing pages.** That matters because a team with 150 API pages cannot re-paste 150 specs by hand.
  - **Pressure:** the in-app "may stop working after January 2027" banners described in M1, which Atlassian is showing on every Connect app that has not declared it is migrating.
- **Demand test:**
  - List the viewer first, with a free tier for 10 users or fewer. The migration scan ships second, and only if the test passes.
  - **Pass:** 15 or more installs and 5 or more "migration-scan waitlist" sign-ups within 21 days of listing. The listing's "Migrate my Swagger macros" button collects admin emails in Forge storage.
  - **Fail:** do not build the converter. Leave a maintenance-only viewer listed.
- **Customer:**
  - **Who:** Confluence Cloud admins and API platform or tech-writing leads at software companies with 50–2,000 Confluence users who keep internal API docs in Confluence.
  - **Where they are:** they find apps through Confluence's app search and marketplace.atlassian.com.
  - **What they already pay for:** one of the orphaned apps above, plus Confluence Standard/Premium.
- **Problem / desire:**
  - "Our Swagger macro shows 'This app may stop working after January 2027'. The vendor hasn't answered. We have hundreds of pages embedding specs. What do we switch to, and how do we move the pages without redoing them?"
- **Offering:** A Forge Confluence app with two parts.
  - **(1) The macro.** It renders specs with Swagger UI or Redoc (the user picks) from:
    - an attachment;
    - pasted YAML or JSON;
    - another page's attachment.
    - It has try-it-out disabled by default and a version selector.
    - Everything is bundled inside Forge (Custom UI), with no external calls, so it qualifies for "Runs on Atlassian".
  - **(2) The admin "Migration scan".** This is a CQL search for pages containing the orphaned apps' macro keys.
    - It builds a dry-run report: pages found, specs found, and the conversion plan.
    - It rewrites the page storage format to SpecView macros, keeping attachments, and saves the original page version ID so each page can be rolled back.
  - Phase 2 adds Mermaid and PlantUML conversion for the Toshihiro Sato orphans.
- **Price & revenue model:**
  - Paid via Atlassian by Confluence user tier.
  - Free for 10 users or fewer. About $0.12/user/mo at 100 users (≈ $12/mo), close to the orphans' price so switching costs nothing extra, and volume tiers down to about $0.05/user.
  - The migration scan is included and is the reason to choose us.
  - Blended about $15 per paying site, so **$300/mo ≈ 20 paying sites,** about 1% of the paying orphan base.
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Atlassian developer account, Forge, free Confluence developer site | $0 |
| Evaluation installs of the orphaned Connect apps on the dev site, to capture their macro storage format (Marketplace 30-day evaluations) | $0 |
| Partner profile (shared with M1 if both are run) | $0 |
| **Total** | **$0** |

### Monthly running costs (excluding operator tokens)
- **Forge:** $0 expected. Rendering is client-side, and the scan uses Confluence REST calls inside the function free allowance.
- **Atlassian revenue share:** 0% to $1M.
- **Total:** about $0/mo.

### Customer acquisition plan
1. **Atlassian Marketplace and Confluence app search.**
   - Target terms: "OpenAPI", "Swagger", "API documentation", "Swagger UI", plus each orphan's exact product name in the description ("replacement for Open API (Swagger) Integration", worded to stay inside Atlassian listing rules).
   - "Runs on Atlassian" badge.
2. **The migration scan is the conversion hook** for admins who already know they must switch: "Find every Swagger macro in your site in 60 seconds, free on the trial."
3. **Atlassian's evaluation-to-paid flow and billing,** on the same invoice as Confluence.
4. **Phase-2 listings** for Mermaid and PlantUML conversion inside the same app (a feature, not a new app), which enlarges the searchable surface.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Marketplace search for "swagger"/"openapi"**
   - **Why it works with no audience:** there are 15 cloud results, 6 of them stale Connect apps that will show warning banners. Our listing is one of the few Forge results and the only one offering migration.
   - **Expected speed:** first installs within 1 week of approval.
2. **Admins' active switching searches** ("swagger confluence forge", "connect end of support swagger")
   - **Tactic:** a docs page on GitHub Pages titled for each orphan ("Migrating from Open API (Swagger) Integration to Forge").
   - **Expected speed:** 3–6 weeks to index, with high intent.
3. **Atlassian Community answers by the sponsor (optional, disclosed)**, in threads where customers ask the silent vendors about migration.
   - **Expected speed:** 1–3 weeks. Human only.

### Path to first sale
| When (from today, 6 Oct) | Step |
|---|---|
| Days 0–2 | Partner setup, as in M1. If M1 already ran, there is no extra sponsor time. |
| Days 2–8 | Build the viewer macro and the listing; submit around day 8. |
| Days 8–14 | While the app is in review: install the orphans' evaluations on the dev site, record their macro storage formats, and build the dry-run scan. |
| Days 15–30 | Listing approved, five to ten business days or longer (≈ 21 Oct – 5 Nov). The demand test starts. |
| ~Day 35 | The converter ships if the test passes. |
| ~Day 55–105 | First paid conversion, after the 30–60-day evaluation. |
| Cash | After the $500 threshold, the first payout is likely April 2027. |

**Ideator estimate: first sale about day 80 (≈ 25 Dec 2026). Range 55–110 days.**

### Who does what
- **AI operator:**
  - Builds the macro and converter.
  - Keeps a regression suite of real-world specs (public OpenAPI files) and test pages for every orphan macro format.
  - Writes the listing and docs, answers support, and runs the weekly competitor and install check.
- **Human sponsor:**
  - **One-time:** the shared Atlassian partner setup (0 h if M1 is done, otherwise about 2 h).
  - **Recurring:** about 0.25 h/week, including approving any customer request to run the converter on more than 500 pages (as a safety gate).

### Moat — why not just ask ChatGPT?
- **The chatbot cannot do the job.** It can explain how to embed Swagger, but it cannot rewrite hundreds of Confluence pages safely inside a customer's site.
- **The real substitute is a free or cheap Forge viewer plus manual re-pasting.** The converter is the differentiator a shallow AI-farm clone is least likely to build, because it needs each orphan's storage format, dry-run, rollback and edge cases.
- **Secondary moats:** "Runs on Atlassian" and being on the Atlassian invoice.

### Biggest risks (ideator's own view)
- **The orphan vendors migrate late** (Atlassian says over 95% of *paid seats* have already moved), or the 3,186-install Forge bundle adds a converter. Either shrinks the pool.
- **Converter mistakes break customer pages.** This needs strict dry-run, per-page rollback and a page-count gate. It is a reputational and legal (liability) risk carried by the sponsor.
- **Low revenue per site (about $10–15)** plus Atlassian's $500 payout threshold means slow cash. It also shares M1's partner account (concentration).

---

## M3 — SheetSync: a reliable "send my Apify dataset to Google Sheets" integration Actor (fixing the 51%-failure incumbent)

- **Persona:** The Marketplace Native
- **One-liner:** An integration-ready Apify Actor that appends or upserts any Apify dataset into a Google Sheet after every run of another Actor. It authenticates with a shared service account, so there is no OAuth dance. It handles chunking, retries, the 10M-cell limit and de-duplication by key. It is aimed at the 825 monthly users of the incumbent Sheets Actor, which fails about half its runs.
- **Marketplace & gap evidence:**
  - **The incumbent.** `lukaskrivka/google-sheets` ("Google Sheets Import & Export") has:
    - **825 users in the last 30 days** (625 in the last 7) and 4,891 all-time;
    - **83,014 runs in 30 days, of which 42,240 FAILED (51%)**;
    - a 4.8★ rating from 7 reviews, no PPE pricing (free), a typical maintainer response time of **22 days** on its issues tab, and a last modification on 2026-07-29.
  - **Next-best supply is negligible.** The next Sheets-export Actors have 2–7 monthly users. Apify's search finds only one other Sheets *write* Actor (srd836, 2 users). By contrast, "send email" and "Airtable" each have an Apify-maintained utility that works (86% and 95% success).
  - **Demand is captive and recurring.** These are existing Apify users wiring Sheets as the destination of scheduled scrapers, about 100 runs per user per month.
  - **Discovery is native to the platform.** Apify's console lets users attach an "integration-ready" Actor to any Actor or task run. It reads `payload.resource.defaultDatasetId` automatically.
- **Demand test:**
  - Publish with PPE pricing and a free first 1,000 rows per run.
  - **Pass:** 30 or more distinct users, 1,000 or more successful runs, and 5 or more paid-plan users charged within 14 days of publishing.
  - **Fail:** keep it free as a portfolio credibility asset and stop work. At most 5 operator-days are spent.
- **Customer:**
  - **Who:** Apify users who are growth marketers, lead-gen freelancers, e-commerce analysts and no-code builders. They schedule scrapers (Google Maps, Instagram, Amazon…) and want results in a shared Sheet their team or client already uses.
  - **What they already pay for:** Apify Starter or Scale plans ($29–$199), and often Make or Zapier too.
  - **Where they are:** the Apify Console and Store, and the Apify Discord.
- **Problem / desire:**
  - "My scheduled run finishes, but the Sheets export fails half the time and I find out days later when the client's sheet is stale."
  - They want: "append new rows, don't duplicate yesterday's, don't blow the cell limit".
- **Offering:** A public, integration-ready Apify Actor (Node).
  - **Inputs:** spreadsheet URL, tab name, mode (append / replace / upsert-by-key), column mapping and transforms, and dataset source (automatic from the integration payload, or a dataset ID).
  - **Authentication:**
    - **The default is a shared service account.** The user shares the sheet with our service-account email, and no OAuth app verification is needed.
    - **An option for teams:** bring your own service-account JSON.
  - **Reliability:**
    - batched `values.append` calls with exponential backoff and quota-aware pacing;
    - automatic tab rollover before the 10M-cell limit;
    - an idempotency key per run, so retries never double-write;
    - a clear failure summary written to the run log and an optional "status" tab.
  - **Template integrations** for the 10 most-used Store Actors, so new users can attach SheetSync without configuring it.
- **Price & revenue model:**
  - Apify pay-per-event: **$0.005 per run start + $0.40 per 1,000 rows written.** The first 1,000 rows of each run are free during launch to win switchers.
  - At the observed about 100 runs per user per month and about 200 rows per run, that is about $8.50 per user per month gross, or about $6.80 net after Apify's 20%.
  - **$300/mo net ≈ 45 paid-plan users,** about 5–6% of the incumbent's monthly users.
  - Free-plan usage is not paid out.
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Apify account (free plan covers development runs) | $0 |
| Google Cloud project, Sheets API and service account | $0 |
| **Total** | **$0** |

### Monthly running costs (excluding operator tokens)
- **Apify:** a 20% commission, plus platform compute deducted from revenue under PPE. An HTTP-only 256 MB Actor costs about $0.0003–0.001 per run, which at 5k runs/mo is about $2–5.
- **Google Sheets API:** free, within per-minute quotas.
- **Total:** under $5/mo at the target volume.

### Customer acquisition plan
1. **Apify Store search** for "Google Sheets", "export to Google Sheets" and "Sheets integration". There are 694 matches, but only one working-at-scale Sheets *writer* exists.
   - The listing leads with reliability numbers: "99%+ success rate, last 30 days". Apify displays the run success rate publicly.
2. **The Apify Console integrations picker:** users attaching an integration to a scraper run see integration-ready Actors.
3. **Switching hook:** a "Moving from Google Sheets Import & Export" section with the input mapped field by field. Same sheet, and only one "share with" step.
4. **Template integrations** published in the README for the top Store scrapers, for example "Google Maps Scraper → Sheet, de-duplicated by placeId".

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Apify Store search, live on publish day**
   - **Why it works with no audience:** there are 825 monthly users on a shelf with one failing incumbent.
   - **Expected speed:** first runs in 1–5 days.
2. **Integration picker visibility**
   - **Tactic:** mark the Actor integration-ready and document the payload.
   - **Why it works:** users find it at the moment of need, inside the Console.
   - **Expected speed:** 1–2 weeks.
3. **Apify Discord and Apify's monthly Store newsletter/showcase submission**
   - **Tactic:** one disclosed post by the account owner where the community rules allow it.
   - **Expected speed:** 1–3 weeks, small.
4. **A GitHub README and a short docs page** ("Apify to Google Sheets without failures") for organic search.
   - **Expected speed:** 4–8 weeks.

### Path to first sale
| When (from today, 6 Oct) | Step |
|---|---|
| Day 0 | The sponsor confirms which Apify account to use, ideally the existing T2 account (see the concentration note) or a new one with KYC and payout (about 1 h). The sponsor also creates the Google Cloud project and service account (about 0.25 h; the operator can do it if given a Google login). |
| Days 1–5 | The operator builds the Actor, tests it on 1k / 100k / 2M-row datasets and on quota-exhaustion scenarios, and writes the README, templates and switching guide. |
| Day ~6 | Publish with PPE pricing. |
| Days 7–20 | First runs; the demand test runs. The first paid-plan user is charged when their scheduled runs fire. |
| Cash | Apify pays out monthly for the prior month. A minimum payout threshold may apply (unverified), so the first payout is likely mid-December. |

**Ideator estimate: first sale about day 14 (≈ 20 Oct 2026). Range 8–30 days. First cash about day 70.**

### Who does what
- **AI operator:**
  - Builds and maintains the Actor.
  - Runs a daily self-test that writes to a canary sheet and alerts on failure.
  - Answers Apify issue threads and support, which is possible through Apify's API.
  - Publishes integration templates and watches the incumbent's success rate and user count weekly.
- **Human sponsor:**
  - **One-time:** about 1–1.25 h (Apify KYC and payout if a new account; Google Cloud project).
  - **Recurring:** about 0.1 h/week (payout review).

### Moat — why not just ask ChatGPT?
- **The chatbot is not the competition.** The real alternatives are:
  - the free incumbent;
  - Make or Zapier (another subscription and another integration to keep running);
  - writing your own Sheets API code.
- **Our edge:**
  - reliability engineering that the incumbent has not delivered (51% failure, 22-day response);
  - native placement in the Apify Console where the need arises;
  - the switching guide.
- **Honest weakness:** the moat is execution and reviews only. A fixed incumbent or a clone erodes it.

### Biggest risks (ideator's own view)
- **The incumbent is free and maintained by an Apify staff member.** A fix there, or Apify shipping a native "Google Sheets" integration, could remove most switching demand overnight.
- **Google Sheets API quotas.** The per-project limit is 300 requests/min and the per-user limit is 60 requests/min, and the shared service account counts as one user. Mitigations: heavy batching, a bring-your-own-credentials option, and an early quota-increase request. Unmitigated, peak-hour throttling would recreate the incumbent's failure mode.
- **Thin and leaky revenue.** Free-plan users pay nothing out, $300/mo needs about 45 paying users, and it adds Apify concentration on top of T2, G1 and G2. The committee should pick at most one Apify slot across the round.

---

## Sources checked (2026-10-06)

**Apify (Store API):**
- Search across about 230 terms, including Google Trends (about 40 Actors), Kalshi/Polymarket, Google Sheets, Airtable and "send email".
- Actor detail for `lukaskrivka/google-sheets`, with 30-day run stats.
- [Integration-ready Actors docs](https://docs.apify.com/platform/integrations/actors/integration-ready-actors).
- [PPE monetization docs](https://docs.apify.com/platform/actors/publishing/monetize): 80% share, free-plan usage not paid out, rentals retired 1 Oct 2026.

**Atlassian Marketplace REST API:**
- The top 1,500 cloud apps by popularity, with the `deployment.connect` flag and last release date from `/versions/latest`.
- Keyword checks for "google chat", "openapi swagger", "mermaid", "markdown", "figma", "miro", "restore deleted issues" and others.
- Pricing and reviews endpoints for the Google Chat and Swagger apps.

**Atlassian announcements and documentation:**
- [Connect EoS timeline](https://www.atlassian.com/blog/developer/announcing-connect-end-of-support-timeline-and-next-steps).
- [Connect EoS extended to 31 Jan 2027](https://community.developer.atlassian.com/t/connect-end-of-support-extended-to-january-31-2027/102002).
- ["This app might stop working soon" banner thread](https://community.developer.atlassian.com/t/new-this-app-might-stop-working-soon-banner-in-all-our-uis/100817).
- [Exalate customer-facing banner text](https://community.exalate.com/t/jira-cloud-this-app-may-stop-working-after-december-january-2027-warning-atlassian-connect-deprecation/8353).
- [Figma forum: "Legacy" flag on Figma for Jira](https://forum.figma.com/report-a-problem-6/figma-for-jira-v1-0-16-ac-legacy-platform-no-update-available-january-2027-deadline-57719).
- [Revenue share 2026: 0% on first $1M Forge](https://www.atlassian.com/blog/developer/updates-to-marketplace-revenue-share-2026).
- [Forge pricing 2026 free allowances](https://www.atlassian.com/blog/developer/updates-to-forge-pricing-effective-january-2026).
- [Payouts: $500 threshold, net 30 after month-end](https://developer.atlassian.com/platform/marketplace/pricing-payment-and-billing/).
- Cloud evaluations of 30 days, co-terminating with billing (Atlassian developer docs and the Easy Agile help pages).
- [Approval in 5–10 business days](https://developer.atlassian.com/platform/marketplace/onboarding-hub/launch/submit-for-review/), with 2026 forum reports of waits of 3+ weeks.

**Atlassian issue tracker (JQL `type = Suggestion ORDER BY votes`):**
- I checked the top-voted 2023–2026 cloud suggestions, for example JSDCLOUD-12765 (1,154 votes) and CONFCLOUD-77328 (756 votes).
- Most cannot be built as apps (they need native UI or missing APIs), so I did not use them.

**Saturation checks that led me to reject channels:**
- Chrome Web Store search "kalshi": 9 extensions, all with 0 ratings.
- Wix App Market searches for "etsy" (39 results, including Etsy EasySync at 4.9★/102), "waitlist" (7 appointment-waitlist apps, mostly with 0 reviews) and "checkout custom fields" (48 results).
- WordPress.org plugin API: 14 terms, no stale incumbent with 10k+ installs.
- [RapidAPI](https://docs.rapidapi.com/docs/payouts-and-finance): 25% fee, PayPal-only payouts.
- [ChatGPT app directory](https://www.moburst.com/blog/chatgpt-app-directory-explained-what-brands-need-to-know/): no digital-goods checkout.
- Shopify Stocky sunset (31 Aug 2026), already contested by Sumtracker, Prediko and others.
- Google Custom Search JSON API retiring 1 Jan 2027: an Apify drop-in already exists with 2 users, and the buyers do not search Apify.

**Not verified:**
- Whether ChatRelay's Google Chat webhook egress keeps "Runs on Atlassian" eligibility.
- The install count of "Google Chat Automation Actions for Jira".
- Apify's payout minimum.
- The exact storage format of each orphaned Swagger macro. This gets captured on the dev site during the build.
