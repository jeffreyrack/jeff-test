# Agent-economy ideas — The Agent Economist

_Run 2026-10-06, round 2. Persona: The Agent Economist. All day counts start from **today, Tue 2026-10-06**. Applies `operator-constraints.md`, `idea-brief.md` and `lessons-learned.md` (binding)._

## Research notes (evidence shared by all three ideas)

**How the demand numbers were gathered.** I pulled them from Apify's public Store API (`api.apify.com/v2/store?search=…` and `/v2/acts/<id>`) on 2026-10-06. "u30" means distinct users in the last 30 days and "runs30" means runs in the last 30 days. Both count free-plan users. Apify pays developers **only for paid-plan users**, so treat every user count below as an upper bound on paying demand.

**Five findings set the direction of this brief:**

1. **Only one agent-tool channel has proven discovery and billing: Apify.**
   - The Store lists 82,023 Actors. Pay-per-event (PPE) payout = 0.8 × revenue − platform costs. Invoices are issued on the 11th and paid out on the 21st–25th of the following month. The payout minimum is $20 via PayPal or Wise. KYC is required.
   - Apify's MCP server (mcp.apify.com) lets agents search for and run Actors. Apify also accepts **x402 USDC agentic payments** for PPE Actors, so a single listing reaches humans, n8n/Make users and autonomous agents.
   - The other monetised channels are thinner:
     - **MCPize:** 80% revenue share, Stripe payouts, x402 option, 900–1,050 servers, 450 publishers, **no published buyer volume**.
     - **RapidAPI ("Rapid", owned by Nokia):** 25% flat fee since 15 Nov 2025, payouts by PayPal only, paid in the first week of month+2.
     - **x402 in general:** about $19M adjusted volume to April 2026. The top 1% of wallets make about 90% of the volume. One provider owns 52% of the agentic.market catalogue, and about 17% of probed endpoints are dead or traps.
     - **Paid skill marketplaces:** fragmented, with a long tail that "monetises poorly".
     - **GitHub Marketplace paid apps:** need 100 installs and a verified-publisher organisation.
2. **Apify is flooded with Actors built by other AI operators.** Niche public-records shelves are priced at around $0.002 per item and have 1–50 monthly users.
   - The XRechnung validator I first considered has **1 total user**.
   - FMCSA, NPI, Federal Register and liquor-licence shelves each have fewer than 30 monthly users.
   - A niche shelf cannot reach $300 a month. **Only high-demand shelves can.**
3. **High-demand shelves still reward a new, well-built entrant within weeks.**
   - `aitorsm/keyword-volume` was created 2026-07-07. It now has 717 users in 30 days and 7,061 runs in 30 days, at $0.012 per keyword.
   - `khadinakbar/dataforseo-keyword-research` was created 2026-08-10. It has 396 users in 30 days **despite a 25% failure rate**.
   - `memo23/video-audio-transcriber` was created 2026-07-23. It has 158 users in 30 days at **$0.05 per minute**.
   - `steadyfetch/media-transcriber` was created 2026-08-27. It has 134 users in 30 days.
4. **Lesson 4 (platform concentration).** G1 and G2 both use Apify, and so does last run's pick T2. **The committee should pick at most one of G1/G2**, and should not run it on the same Apify account as T2 unless T2 is frozen. G3 deliberately avoids Apify, as a hedge for diversification.
5. **Lesson 9 (public records → feed).** None of the three ideas follows that pattern. Each one sells to a buyer through a channel where that buyer already searches and already pays per use.

---

## G1 — Keyword→Brief: one-call SEO research for AI content agents (Apify Actor, pay per event)

- **Persona:** The Agent Economist
- **One-liner:** An Apify Actor for AI blog-writing agents and SEO automations (n8n, Make, Claude/ChatGPT via Apify MCP). It returns live keyword metrics, plus an optional "brief" per keyword: SERP top 10, People-Also-Ask, AI Overview presence and cited URLs, and the headings outline of the ranking pages. One pay-per-event call replaces four API integrations.
- **Discovery surface:**
  - Apify Store search for "keyword search volume", "keyword research", "SEO content brief" and "people also ask", plus the SEO Tools category. The shelf leader has 717 users in 30 days and the next has 396 with a 25% failure rate.
  - The Apify MCP server, through agent-side `search-actors` queries such as "keyword volume" and "SERP brief".
  - Apify x402 agentic payments.
  - A free n8n template on n8n.io/workflows ("AI blog writer with live keyword data"), which uses n8n's built-in Apify node.
- **Demand test:**
  - **Offer:** publish the thin "Keyword Metrics" event first, at $0.004 per keyword: one-third of the shelf leader's price, with 0 failed runs as the target. It takes about 1 day to build.
  - **Pass:** at least **15 distinct paid-plan users and at least $10 of billed events within 14 days** of publishing.
  - **Pivot zone:** 5–14 users. Re-title and re-price, then test for 7 more days.
  - **Fail:** fewer than 5 users. Kill before building the Brief event.
- **Customer:**
  - Builders of automated content pipelines: SEO agencies, affiliate-site operators, solo "AI blog" builders, and n8n/Make freelancers who build these flows for clients.
  - They hang out in the Apify Store, n8n's template library and forum, and Make's community.
  - They already pay for Apify credits, DataForSEO, Ahrefs/Semrush seats, and the Apify scrapers of Ahrefs and Semrush. Those scrapers have 998 and 563 users in 30 days, which shows they want this data cheaply and per call.
- **Problem / desire:**
  - "My n8n blog agent writes from vibes. I need real volume, CPC and what's ranking, without a $129/mo Semrush seat or a $50 DataForSEO deposit and four separate API calls."
  - "The Actor I use fails 1 run in 4." The second-largest DataForSEO-backed Actor has a 25% failure rate, and santhej's Labs Actor has 27%.
- **Offering:**
  - An Apify Actor with pay-per-event pricing and agent-readable input and output schemas, with two events:
    - `keyword-metrics`: Google Ads volume, CPC, competition and a 12-month trend. $0.004 per keyword, with lower prices on higher Apify tiers.
    - `keyword-brief`: top-10 organic results, PAA questions, AI Overview text and cited URLs, search-intent label, word counts and H2/H3 outline of the top 5 pages, and entity list. $0.04 per keyword.
  - Failed or empty results are never charged.
  - The source is the DataForSEO Keywords Data and SERP APIs plus the operator's own polite HTTP fetch of the ranking pages, honouring robots.txt.
- **Price & revenue model:**
  - Per use, through Apify PPE.
  - **Net per brief:** 0.8 × $0.04 − (SERP about $0.002 + keyword data about $0.0001 + compute about $0.002) ≈ **$0.028**.
  - **Net per keyword-metrics call:** about $0.0031.
  - **$300 net a month ≈ 10,700 briefs**, or about 95k metric keywords, or a mix. That is roughly 40 paying users spending about $9.50 a month. For comparison, the shelf leader runs about 7k runs a month at 3× my metric price.
- **Physical items required?** No

### Upfront capital
| Item | Cost |
|---|---|
| DataForSEO minimum account balance (prepaid usage, consumed as COGS) | $50 |
| Apify account, publishing, hosting (the Actor runs on Apify) | $0 |
| Domain | $0 (not needed) |
| **Total** | **$50** |

### Monthly running costs (excluding operator tokens)
- **Apify:** 20% of revenue. The developer also pays platform compute. The Actor is HTTP-only at 256–512 MB, so compute is about $0.0005–0.002 per run.
- **DataForSEO:**
  - Google Ads search volume costs about $0.06 per 1,000 keywords at the standard queue, after the July 2026 increase of about 20%.
  - SERP costs $0.0006 (standard) to $0.002 (live) per page.
  - Usage scales with revenue at roughly 5–8% of the brief price. **At $300 net, about $25–40 a month.**
- **Fixed costs:** $0. PayPal payout fees are about 2%.

### Customer acquisition plan
1. Rank inside the Apify Store. The title, SEO description and README all lead with the exact search phrases ("Keyword Search Volume API", "SEO content brief", "People Also Ask"). Use PPE pricing, which Apify gives "priority store placement". Aim for a 0% failure badge. The demand evidence shows a new entrant can reach hundreds of monthly users in 4–8 weeks on this shelf.
2. Make the Actor agent-native, so the Apify MCP server's actor search surfaces it to Claude, ChatGPT and Cursor agents. The input schema descriptions use natural-language parameter names, and the output is a flat JSON brief.
3. Publish 2–3 free n8n and Make templates that use the Actor: "AI blog post from keyword with live SERP brief" and "weekly keyword trend digest". Template pages bring in-app and organic discovery to the automation builders who are the buyers.
4. Retention: a tier-discounted price, plus a stable output contract (versioned fields) so that people's pipelines don't break. Pipelines that run on a schedule create recurring usage with no repeat selling.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Apify Store search** — the listing goes live on day 5. It works with zero audience because buyers already search this shelf: the top 3 keyword Actors have about 1.4k users in 30 days between them. Expected speed: first runs within 2–7 days of publishing.
2. **Apify MCP and x402 agent discovery** — no extra work beyond good schema metadata. It works because agents query the Store at runtime. Expected speed: 1–3 weeks, and the size is unknown.
3. **n8n template library** — 2 free templates submitted in week 2. n8n reviews them before publishing (timing unverified, assume 1–3 weeks). The template pages draw search traffic from people who build exactly this flow. Expected speed: 3–5 weeks.
4. **Apify Discord #showcase and an "Actor of the week" submission** — a one-time post by the operator under the Actor's account, where community rules allow it. Expected speed: 1–2 weeks, small.

### Path to first sale
- **Days 0–2 (Oct 6–8):** the sponsor creates the Apify account (or confirms which one to use, see the concentration note), completes KYC and PayPal payout, and opens a DataForSEO account with the $50 deposit. The operator emails DataForSEO support asking for written confirmation that serving per-keyword results to Apify users is allowed. DataForSEO markets itself to "750+ software companies built on its endpoints", but its ToS neither permits nor forbids resale.
- **Days 2–4:** build the `keyword-metrics` event, a self-test suite and the README.
- **Day 5 (Oct 11):** publish. The 14-day demand test starts.
- **Days 12–21:** first paid-plan event expected.
- **Day 19 (Oct 25):** test verdict. On a pass, build `keyword-brief` on days 19–24 and publish the n8n templates.
- **Cash:**
  - October earnings below $20 roll over.
  - November earnings are invoiced Dec 11 and paid **Dec 21–25 (about day 77–80)**.
- **My estimate: about 21 days to the first paid event and about 78 days to first cash.** Per lesson 2, the skeptic should stretch this. The comparable 2026 entrants suggest the first paid user arrives within 2 weeks of a listing on this shelf.

### Who does what
- **AI operator:**
  - Build, test and publish the Actor.
  - Run a nightly self-test that checks Google Ads data freshness and SERP parse integrity.
  - Write the README and templates, and answer Apify issue threads (the platform has an API for these).
  - Adjust prices, watch DataForSEO balance and cost per event, and write a weekly metrics log.
- **Human sponsor:**
  - One-time: about 1–1.5 h for Apify KYC and PayPal, DataForSEO signup and deposit, and reading the DataForSEO reply.
  - Recurring: about 0.1 h/week to glance at the monthly invoice (it auto-approves on the 14th) and top up the DataForSEO balance from earnings.

### Moat — why not just ask ChatGPT?
- **What a chatbot can't do:** it cannot produce real Google Ads search volumes or today's SERP, PAA and AI Overview; it estimates or hallucinates them. A web-search-enabled agent can see results, but not volumes, CPC or trends.
- **The real substitute is DataForSEO itself, which has an official MCP server.** A developer with their own DataForSEO account doesn't need us.
- **Why buyers pay us anyway:**
  - No $50 deposit or separate account.
  - One Apify bill alongside their other Actors.
  - A single call that returns a writer-ready brief instead of orchestrating SERP, keywords and page fetches.
  - Reliability: the competing DataForSEO wrappers fail 10–27% of runs.
- **This moat is thin and operational.** The shelf will see price competition, so the plan is to win on reliability and the brief format, not on exclusive data.

### Biggest risks (ideator's own view)
- **Supplier terms.** DataForSEO could object to resale through a marketplace. ToS §7.1 says SERP data must not be used "to compete with or adversely affect" search engines. Mitigation: get written confirmation before building. Fallback: a BYO-key mode that charges only for the brief assembly.
- **Price war and free-plan leakage.** At least 5 AI-built competitors already sit on this shelf, and free-plan users earn the developer nothing. If net per paid user stays under $3, reaching $300 needs more than 100 paid users.
- **Platform concentration with T2 and G2 on Apify.** One account suspension or a change to PPE rules hits everything. Apify retired the rental model on 2026-10-01, which shows the terms do change.

---

## G2 — LongForm Transcripts: podcast, webinar and meeting audio → agent-ready transcript with chapters and quotes (Apify Actor, pay per minute)

- **Persona:** The Agent Economist
- **One-liner:** An Apify Actor that takes a podcast episode or RSS feed, a direct audio/video file URL, or a Drive/Dropbox/S3 link. It returns a timestamped transcript plus chapters, pull-quotes and an LLM-ready chunked JSON, for $0.009 per audio minute. That is far below the $0.05/min shelf leader. It **deliberately excludes YouTube, TikTok and Instagram downloading** to stay legally clean.
- **Discovery surface:**
  - Apify Store search for "podcast transcription", "speech to text", "audio transcriber", "whisper" and "transcribe".
  - The demand comes from new entrants:
    - `memo23/video-audio-transcriber`: 158 users in 30 days at $0.05/min.
    - `steadyfetch/media-transcriber` (created Aug 27): 134 users in 30 days at $0.006/min.
    - `kaz_kakyo/audio-transcriber`: 72 users at $0.01/min.
    - `amanatools/whisper-transcriber`: 68 users.
  - The Apify MCP server, for agents that need "transcribe this episode".
  - Apify x402 payments.
- **Demand test:**
  - **Offer:** publish the transcript-only event (no chapters yet) at $0.009/min, with failed or silent files never charged. It takes about 1.5 days to build.
  - **Pass:** at least **10 distinct paid-plan users and at least 2,000 billed audio minutes within 14 days.**
  - **Pivot zone:** 3–9 users or 500–2,000 minutes. Test the price at $0.006 and add Spanish and Portuguese examples.
  - **Fail:** fewer than 3 users or fewer than 500 minutes.
- **Customer:**
  - Builders of content-repurposing and research pipelines: podcast agencies turning episodes into show notes and blog posts, B2B marketers mining webinars, analysts tracking earnings-call and industry podcasts, and n8n/Make builders whose cloud flows can't run Whisper locally.
  - They already pay Apify, Descript and Riverside, plus per-minute fees to Apify transcribers.
- **Problem / desire:**
  - "n8n Cloud can't run Whisper, OpenAI's endpoint chokes on files over 25 MB and on RSS links, and the Apify one I use costs $3 an hour."
  - "I need chapters and quotable lines, not a wall of text."
- **Offering:**
  - An Apify Actor with PPE pricing. Input is a URL, an RSS feed plus episode filter, or a cloud-storage link.
  - Processing:
    - fetch the file and split it into chunks with ffmpeg in the Actor container;
    - transcribe with Groq `whisper-large-v3-turbo` at $0.04 per audio hour;
    - fall back to OpenAI `gpt-4o-mini-transcribe` if Groq fails.
  - Output: JSON segments, SRT/VTT, markdown, 1,500-token RAG chunks with timestamps, and an optional `chapters+quotes` event generated by a small Groq-hosted LLM.
  - **Audio is deleted when the run ends.** Nothing is kept beyond the user's own Apify dataset.
- **Price & revenue model:**
  - Per use, through Apify PPE:
    - `audio-minute` $0.009, with tier discounts down to $0.007;
    - `chapters-quotes` $0.01 per episode;
    - `actor-start` $0.0001.
  - **Net per minute** ≈ 0.8 × $0.009 − $0.00067 (Groq) − about $0.0004 (compute and bandwidth) ≈ **$0.0061**.
  - **$300 net ≈ 49k audio minutes a month** (about 820 hours), for example 35 paying users at about 23 hours each. That is ambitious but within the volume the shelf already has: `invideoiq/video-transcriber` alone logs 31,306 runs in 30 days.
- **Physical items required?** No

### Upfront capital
| Item | Cost |
|---|---|
| Groq API account (postpaid; card on file, no prepayment) | $0 |
| OpenAI fallback credit (minimum top-up) | $5 |
| Apify account and hosting | $0 |
| **Total** | **$5** |

### Monthly running costs (excluding operator tokens)
- **Groq transcription:** $0.04 per audio hour, so about $33 a month at 820 hours.
- **OpenAI fallback:** $0.18 per hour, used only on Groq failures. Assume 5% of volume, about $7 a month at target.
- **Apify:** compute for download and ffmpeg (1 GB memory for about 20–40 seconds per audio hour) is about $0.002–0.005 per hour, plus 20% of revenue.
- **Fixed costs:** $0. PayPal payout fees are about 2%.

### Customer acquisition plan
1. Win the Apify "transcribe / podcast / speech to text" searches on price, at 1/5 of the leader and below the $0.01 incumbents. Also win on the Store's failure-rate badge and on features the cheap incumbents lack (RSS batch, chapters and quotes, RAG chunks).
2. Make it agent-callable. Use MCP-friendly input such as `{"url": "…"}` and return a short summary first, so agents using the Apify MCP server choose it.
3. Publish free n8n and Make templates: "New podcast episode → transcript → show notes → WordPress draft" and "Webinar recording in Drive → chapters → LinkedIn post drafts". The human sponsor posts those drafts; nothing is auto-posted.
4. Retention comes from RSS watch mode, scheduled on Apify: new episodes are transcribed automatically, which gives recurring minutes with no repeat selling.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Apify Store search** — live on day 4. Buyers already search this shelf: about 1,079 users in 30 days across the top results for "transcribe". Expected speed: first runs within 3–7 days of publishing.
2. **Apify MCP and x402 agent discovery** — free with a good schema. Expected speed: 1–3 weeks.
3. **n8n and Make templates** — submitted in week 2. Expected speed: 3–5 weeks, after template review.
4. **README cross-links from the operator's other Actors** (G1, if both ever run) — slow, small.

### Path to first sale
- **Days 0–1 (Oct 6–7):** the sponsor sets up the Apify account and KYC (shared with G1 or T2, see the concentration note), adds a card to Groq, and adds $5 to OpenAI.
- **Days 1–3:** the operator builds the fetch, chunk and transcribe pipeline, self-tests on 20 public-domain and Creative Commons podcast episodes, and writes the AUP and README.
- **Day 4 (Oct 10):** publish. The 14-day test starts.
- **Days 10–20:** first paid-plan minutes expected.
- **Day 18 (Oct 24):** verdict. On a pass, add `chapters-quotes` and RSS watch mode on days 18–22.
- **Cash:** November earnings are paid Dec 21–25 (about day 78). October earnings are paid Nov 21–25 only if at least $20.
- **My estimate: about 24 days to the first paid event and about 78 days to first cash.**

### Who does what
- **AI operator:** build and maintain the Actor; nightly self-test against 5 reference files (checking WER drift and Groq availability); write the README, templates and pricing; answer Apify issue threads; handle takedown and abuse emails using a written policy that blocks a URL or user on any rights complaint.
- **Human sponsor:**
  - One-time: about 0.75–1.25 h, or 0.25 h if the Apify account already exists.
  - Recurring: about 0.1–0.2 h/week to glance at invoices and approve any rights-complaint response the operator drafts. These should be rare.

### Moat — why not just ask ChatGPT?
- **The free or cheaper substitute is real.**
  - A developer with an OpenAI key can call `gpt-4o-mini-transcribe` at $0.003/min, or Groq directly at $0.00067/min.
  - ChatGPT itself will transcribe an uploaded file by hand.
- **Why Apify buyers pay anyway** (the same reason they pay memo23 $0.05/min today):
  - URL, RSS and cloud-link fetching.
  - Chunking of large files.
  - No API key.
  - One Apify bill.
  - Agent-ready chapters and chunks.
  - Scheduled watch mode.
- **This is a convenience moat, not a data moat.** It survives while the operator keeps a clear price and reliability lead. Frontier models will not erode it next quarter, because the buyer already has free ASR and still chooses the marketplace.

### Biggest risks (ideator's own view)
- **Price compression.** The shelf already runs from $0.004 to $0.05 per minute. At $0.006 the net falls to about $0.004/min, and $300 then needs about 75k minutes a month.
- **Copyright and privacy.** Users may submit content they have no right to transcribe, or meeting recordings containing personal data. Mitigations:
  - process only and keep no copies;
  - an AUP;
  - a rights-complaint block list;
  - no platform downloaders (YouTube, TikTok, IG), which keeps clear of those platforms' terms.
  - The legal analyst should still check DMCA safe-harbour applicability (a designated agent costs $6 at the US Copyright Office).
- **Apify concentration.** This is the same platform as G1 and T2, so pick at most one of G1 and G2.

---

## G3 — AnswerShare API: pay-per-check AI-search visibility for agency agents (MCPize + RapidAPI; off-Apify by design)

- **Persona:** The Agent Economist
- **One-liner:** An MCP server and REST API for SEO/PR agencies' own agents and dashboards. It answers "for these prompts, is brand X mentioned or cited by ChatGPT-search, Perplexity and Gemini, at what position, and which URLs did each engine cite?" It keeps 12 months of trend history and is sold per check through MCPize (80%, Stripe or x402) and RapidAPI (75%, PayPal). There is no Apify dependency.
- **Discovery surface:**
  - MCPize marketplace (Marketing/SEO category), searching "AI visibility", "GEO", "LLM brand mentions" and "AI rank tracker".
  - RapidAPI Hub search for the same terms (200k+ monthly active subscribers, per Rapid).
  - Free listings with no billing that point to the paid endpoints: the official MCP Registry, glama.ai, PulseMCP and mcp.so.
  - One free n8n template: "weekly AI-visibility report to Google Sheets".
- **Demand test:**
  - **Offer:** a free tier (25 checks a month on RapidAPI, and MCPize's free quota), with a $29/mo plan (300 checks) and $0.12 per pay-per-call check. It is listed in all 6 directories by day 7.
  - **Pass:** at least **100 calls from at least 10 distinct keys within 14 days of listing, and at least 1 paid plan or $5 of paid calls by day 40.**
  - **Pivot zone:** usage passes but nobody pays. Cut to Perplexity plus Gemini only at $0.05 a check.
  - **Fail:** fewer than 30 calls or fewer than 5 keys in 14 days. Kill. Do not port it to Apify while G1 or G2 is running there.
- **Customer:**
  - SEO and PR agencies and in-house growth engineers who are building client reporting or GEO agents.
  - They hang out on RapidAPI, MCP directories and the n8n forum.
  - They already pay Otterly ($29+/mo), Peec ($95+), Profound ($99+), Semrush's AI toolkit ($99/domain), Ahrefs Brand Radar ($199+), or pay-per-check Apify Actors ($0.05–0.30 a check, with 18–55 users in 30 days each).
- **Problem / desire:**
  - "Clients ask 'are we showing up in ChatGPT?' every week. The SaaS dashboards charge per seat and per domain and won't let my agent pull raw citations into my own report."
  - "I need an API I can call per prompt from my pipeline."
- **Offering:**
  - Hosted on Cloudflare Workers with a D1 database for history. Endpoints:
    - `check` (prompt × engines → mention, rank, sentiment, cited URLs);
    - `watch` (scheduled weekly re-checks with a webhook);
    - `history` (trend);
    - `citations` (the domains cited most for a prompt set, for outreach targets).
  - Engines:
    - OpenAI Responses with web search, labelled honestly as "ChatGPT-search via API, not the logged-in consumer app";
    - Perplexity Sonar;
    - Gemini with Google Search grounding.
  - Google AI Overviews can be added only if G1's DataForSEO account exists.
- **Price & revenue model:**
  - Prices: $0.12 per 3-engine check pay-per-call; $29/mo for 300 checks; $99/mo for 1,200 checks with history and webhooks. Overage is $0.10.
  - **Cost per 3-engine check** ≈ OpenAI web search about $0.025–0.03 + Perplexity about $0.006 + Gemini about $0 within the free grounded-request quota, about $0.035 above it. That is **about $0.035–0.07**.
  - **Net per check** ≈ $0.02–0.06, depending on channel and engine mix.
  - **$300 net ≈ 24 subscribers on the $29 plan**, or about 8 on the $99 plan, or about 6–10k pay-per-call checks.
- **Physical items required?** No

### Upfront capital
| Item | Cost |
|---|---|
| OpenAI API minimum credit | $5 |
| Perplexity API minimum credit | $5 |
| Google AI Studio / Gemini API (free tier, then billed) | $0 |
| Cloudflare Workers + D1 (free tier), workers.dev subdomain | $0 |
| MCPize and RapidAPI listings | $0 |
| **Total** | **$10** |

### Monthly running costs (excluding operator tokens)
- **Engine API costs:** variable, about $0.035–0.07 per check, roughly 30–55% of revenue.
- **Cloudflare:** $0 on the free tier (100k requests a day, D1 5 GB). It moves to $5/mo Workers Paid only if cron and CPU limits are reached.
- **Channel fees:** RapidAPI 25% of RapidAPI sales plus PayPal fees; MCPize 20% of its sales. There is no fixed cost.

### Customer acquisition plan
1. List on two billed marketplaces (MCPize and RapidAPI) and four free MCP directories, with the exact category terms buyers search ("AI visibility API", "GEO tracker", "ChatGPT brand mentions API").
2. Make the free tier immediately useful: one call returns a shareable JSON and markdown "AI visibility snapshot" that an agency can paste into a client email.
3. Convert through the `watch` endpoint. Once a weekly schedule is set, usage recurs, and the 300-check plan is the natural upgrade.
4. Publish an n8n template plus a public sample report on GitHub Pages: "How 50 SaaS brands show up across ChatGPT-search, Perplexity and Gemini, Oct 2026". It is a data asset that directory listings can link to. No social posting by the operator.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **RapidAPI Hub search** — live on day 5. The buyer base browses by keyword, but discovery for a new API with no reviews is unproven. Expected speed: 1–3 weeks to the first free keys.
2. **MCPize marketplace and the free MCP directories** (official MCP Registry, glama, PulseMCP, mcp.so) — submitted on days 5–7. MCPize's review time is unknown. Agents' users browse these directories for tools. Expected speed: 2–4 weeks.
3. **n8n template and the public sample-report page** — week 3. These are slower and depend on indexing and template review. Expected speed: 4–8 weeks.

### Path to first sale
- **Days 0–3:** the sponsor creates the RapidAPI provider account and PayPal payout, the MCPize account with Stripe Connect KYC, and OpenAI, Perplexity and Google AI Studio billing ($10).
- **Days 1–5:** the operator builds the Worker and D1, the three engine adapters, and a parser for mentions and citations, and validates on 50 prompts.
- **Days 5–7:** list everywhere. The free-tier test runs from day 7 to day 21.
- **First paid plan or pay-per-call:** expected around **days 45–60**.
- **Cash:**
  - MCPize pays by monthly Stripe payout.
  - RapidAPI pays in the first week of month+2. A November sale arrives in early January (about day 90).
- **My estimate: about 55 days to first sale and about 90 days to first cash.** P90 may be "never": this is the weakest-channel idea, included as the off-Apify hedge.

### Who does what
- **AI operator:** build and run the API; nightly self-test per engine for API changes and parse drift; manage the listings and README; build the sample-report page; adjust prices; answer support email through the API-connected inbox; keep the cost-per-check dashboard.
- **Human sponsor:**
  - One-time: about 2–2.5 h across three KYC and payout setups and three AI-provider billing accounts.
  - Recurring: about 0.25 h/week to glance at payouts and approve any refund.

### Moat — why not just ask ChatGPT?
- **What a single chatbot can't do:** it cannot report what *other* engines say, cannot run 50 prompts × 3 engines on a schedule, and cannot keep a trend history.
- **The real substitutes are paid tools and free DIY:**
  - **MentionsAPI:** pay-as-you-go from $0.02 per cached check, with an MCP server, live since June 2026.
  - **Otterly:** API and MCP on its Standard plan.
  - **Apify GEO Actors.**
  - **Open-source DIY trackers.**
- **Our only edges:** per-check pricing with no seats or domains, raw citation-URL output for outreach, and stored history. Those are modest. **This is a crowded market reached through an unproven channel.**

### Biggest risks (ideator's own view)
- **Competition.** MentionsAPI already sells exactly this model with an MCP server and lower cached prices. If the test shows usage but no payment, the market is saturated for an unknown seller.
- **Thin margins and engine-cost changes.** OpenAI web search at about $25 per 1k calls dominates COGS. A price rise or a Gemini free-quota cut pushes net per check toward $0.02. Also, API answers differ from the consumer ChatGPT app, so buyers may distrust the numbers. Mitigation: disclose this clearly.
- **Two thin channels.** RapidAPI takes 25% and pays slowly. MCPize publishes no buyer volume. Days to first sale could exceed 90.

---

## Sources checked (2026-10-06)

**Apify Store demand data:** pulled from the public Store API, `https://api.apify.com/v2/store?search=<term>` and `https://api.apify.com/v2/acts/<user>~<actor>`.
- Keyword and SEO shelf: [aitorsm/keyword-volume](https://apify.com/aitorsm/keyword-volume), [khadinakbar/dataforseo-keyword-research](https://apify.com/khadinakbar/dataforseo-keyword-research).
- Transcription shelf: [memo23/video-audio-transcriber](https://apify.com/memo23/video-audio-transcriber), [steadyfetch/media-transcriber](https://apify.com/steadyfetch/media-transcriber), [kaz_kakyo/audio-transcriber](https://apify.com/kaz_kakyo/audio-transcriber).
- The e-invoice shelf I rejected (1 total user): [kamerozkan/xrechnung-xml-batch-validator-api](https://apify.com/kamerozkan/xrechnung-xml-batch-validator-api).

**Apify terms:**
- Payouts: [monthly payouts](https://docs.apify.com/actors/publishing/monetize/monthly-payouts.md).
- PPE: 80% share, developer pays platform costs, free-plan users excluded ([pricing and costs](https://docs.apify.com/actors/publishing/monetize/pricing-and-costs.md)).
- x402: [Apify x402 agentic payments](https://docs.apify.com/platform/integrations/x402).

**Other channels:**
- MCPize: [developers page](https://mcpize.com/developers) (80% share, Stripe payouts, x402).
- RapidAPI: [payouts](https://docs.rapidapi.com/docs/payouts-and-finance) (25% fee, PayPal only).
- x402 market: [The Defiant, adjusted x402 volume](https://thedefiant.io/news/infrastructure/visa-s-sheffield-pegs-adjusted-x402-volume-at-19m), [dev.to probe of 20,338 x402 endpoints](https://dev.to/afx/we-probed-20338-x402-endpoints-161-are-agent-honeypots-4c3n).
- GitHub Marketplace: [paid-app requirements](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app).
- Skills marketplaces: [Agensi comparison](https://www.agensi.io/learn/ai-agent-skills-marketplace-comparison-2026).
- Smithery: [smithery.ai](https://smithery.ai) usage counts.

**Suppliers and substitutes:**
- DataForSEO: [ToS](https://dataforseo.com/terms-of-service), [MCP server launch](https://dataforseo.com/update/dataforseo-mcp-server-launch), [pricing update July 2026](https://dataforseo.com/update/pricing-update-in-dataforseo-apis).
- Groq Whisper at $0.04/hr: [eesel Groq pricing](https://eesel.ai/blog/groq-pricing).
- OpenAI web search at $25 per 1k: [costbench comparison](https://www.costbench.com/compare/perplexity-api-vs-openai/).
- GEO competitors: [MentionsAPI MCP (glama)](https://glama.ai/mcp/servers/fugd8fsh8u), [AI visibility tool pricing 2026](https://ainora.lt/blog/best-ai-visibility-tracking-tools-2026).
