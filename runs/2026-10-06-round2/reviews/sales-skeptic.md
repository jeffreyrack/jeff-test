# Sales Skeptic review: round 2 (2026-10-06)

All day counts start from **today, Tue 2026-10-06**, and include build time, review queues and trials. "First sale" means the first time a stranger is charged: a billed pay-per-event (PPE) event from a paid-plan Apify user, an Atlassian evaluation converting to paid, or a Lemon Squeezy order (refundable pre-orders included). "First cash" means money landing in the sponsor's account. P90 is "never" when I put more than a 10% chance on no sale within about 180 days.

## Summary

| ID | Idea | Score | P(≤30d) | P(≤90d) | P50 days | P90 days | Kill shot |
|---|---|---|---|---|---|---|---|
| M3 | SheetSync (Apify → Google Sheets) | **7** | 0.55 | 0.85 | 20 | ~120 | The free incumbent is maintained by an Apify staffer; one fix removes the reason to switch. The launch promo also makes a typical run nearly free. |
| G1 | Keyword→Brief (Apify, PPE) | **6** | 0.40 | 0.75 | 32 | ~150 | It is a 1/3-price clone on a shelf of 20+ clones whose leader already shows 0 failures. Users skew to the free plan, so paid usage is tiny. |
| M1 | ChatRelay for Jira (Forge) | **5** | 0.03 | 0.40 | 105 | never | A free, actively maintained Forge app from an established vendor (Move Work Forward, updated 2026-10-02) absorbs the switchers. |
| G2 | LongForm Transcripts (Apify) | **4** | 0.25 | 0.55 | 70 | never | Not differentiated: steadyfetch already sells "podcast transcription, never charged on failure" at $0.006/min, cheaper than G2's $0.009. Excluding YouTube cuts the biggest input. |
| M2 | SpecView for Confluence (Forge) | **4** | 0.02 | 0.30 | 125 | never | The viewer alone is a commodity (free Narva plus a 3,186-install bundle). The converter, which is the only reason to choose it, is built after the deadline peak. |
| I2 | Episode Study Packs (Mandarin creators) | **4** | 0.10 | 0.45 | 100 | never | Small creators with small Patreon incomes won't pay $39/mo for a job they already do, or could do with ChatGPT. |
| C1 | FunderFit (grant-writer partners) | **3** | 0.03 | 0.25 | 130 | never | Partners don't say yes: they are Instrumentl affiliates or teach prospect research themselves. The first mention slips into the late-December dead zone. |
| C3 | Interpreter Practice Lab | **3** | 0.01 | 0.18 | 150 | never | The chain is too long: build, then a human calibration gate, then a partner yes, then a promotion, in a market of about 1,000 oral candidates a year. |
| I1 | Zì Bot (Discord) | **3** | 0.05 | 0.25 | 140 | never | Discord learners expect free bots. A pre-order for an unbuilt AI chat feature converts below 1%. |
| C2 | Client Safety Kit (white-label) | **2** | 0.01 | 0.12 | >180 (gate) | never | Consultants won't put their name and liability on AI-written bilingual safety talks from an unknown vendor. It also depends on D2 being built. |
| I3 | Role-Play Room (college classes) | **2** | 0.01 | 0.12 | ~300 (gate) | never | Instructors don't buy from unknown vendors mid-semester. If the spring window is missed, the next is August 2027. |
| G3 | AnswerShare GEO API | **2** | 0.02 | 0.12 | >180 (gate) | never | No buyer traffic on RapidAPI or MCPize for an unknown API, and MentionsAPI already sells the same thing for less. |
| U4a | Job board: free first, employers pay later | **1** | 0.00 | 0.02 | never (gate) | never | Employers don't pay to reach zero seekers, and the jobs are already aggregated for free from their own ATS feeds. |
| U4b | Job board: seekers pay from day 1 | **2** | 0.08 | 0.20 | >180 (gate) | never | Hiring Cafe does the same thing for free, and "pay to see jobs" from an anonymous site looks like a scam. |
| U4c | Job board: niche variant | **2** | 0.02 | 0.10 | >180 (gate) | never | A niche board still needs 6–12 months of traffic unless a partner who owns the niche audience supplies it. |

**Hard-gate flags (P50 > 180 days):** C2, I3, G3, and all three U4 variants.

## First sale vs first cash (payout thresholds)

| Idea | Payout rule | Earliest realistic cash | P50 cash |
|---|---|---|---|
| G1, G2, M3 (Apify) | Invoice on the 11th, paid on the 21st–25th of the following month. $20 minimum, rolls over (per G1; M3 marked it unverified). | Dec 21–25 (day ~77). October will not reach $20. | Jan 21–25 (day ~108). **M3 during its launch promo earns about $0.50 per user per month, so $20 could take until Feb–Mar.** |
| M1, M2 (Atlassian) | **$500 cumulative profit**, then paid within 30 days after the end of that month (verified on developer.atlassian.com today). | Apr 2027 (day ~180) | M1 about day 230 (late May 2027). M2 at about $15 per site needs about 33 site-months, so **late 2027 or never.** This is the largest gap between first sale and first cash in the round. |
| G3 | RapidAPI pays in the first week of month+2 (PayPal). MCPize pays by monthly Stripe payout. | A December sale arrives in early February. | never |
| C1, C2, C3, I1, I2, I3, U4 (Lemon Squeezy) | Short payout lag (weeks). Payout minimum not verified. **Lemon Squeezy is moving to Stripe Managed Payments, which has no affiliate tool**, so the C-ideas' 40% partner payouts may have to be paid by hand. | Sale + ~2–4 weeks | Close to the first-sale date |

## Spot checks I ran today (public APIs)
- `lukaskrivka/google-sheets`: 825 users in 30 days; 83,014 runs, 42,240 of them FAILED. **Confirmed.**
- `aitorsm/keyword-volume`: 717 users in 30 days; 7,061 runs, **0 failed**; PPE from $0.012 down to $0.008 per keyword on higher tiers. So G1's reliability pitch only works against the #2 Actor, not the leader.
- `steadyfetch/media-transcriber`: titled "Podcast Transcription Scraper"; **$0.006/min flat**; 0 failures in 883 runs; "never charged for a link we can't reach". `memo23` supports YouTube, TikTok, Instagram and RSS. G2 is neither the cheapest nor the only "no charge on failure" offer.
- Atlassian: "Google Chat for Jira Cloud" has 11,008 installs at 2.3★ (109 reviews). **Confirmed.** "Advanced Google Chat for Jira" (Move Work Forward) has 407 installs, is **free** (the pricing endpoint returns 404) and was **modified 2026-10-02**, so it is actively maintained.

## Cross-cutting observations
- **Apify:** G1, G2 and M3 all use Apify, plus T2 from last run. Pick at most one. M3 has the best odds of a fast first sale; G1 has the higher revenue per user.
- **Atlassian:** M1 and M2 share one partner account. Pick one.
- **Lemon Squeezy:** 6 of 13 ideas use it as merchant of record (7 if U4 does too). That is right at the "more than half" flag. Its pending migration to Stripe Managed Payments directly threatens the C-ideas' affiliate mechanics.
- **Partner-gated ideas (C1–C3)** all have P50 above 120 days. The gating event is a stranger saying yes to an email from the sponsor, through a pipe of 1 hour a week. The ideators' 10–25% agreement rates are optimistic for an unknown vendor with no track record. I used 5–10%.
- **The Mandarin trio (I1–I3)** shares demand risk. None of the three has a marketplace channel.

---

## M3: SheetSync, an integration Actor from Apify to Google Sheets
**First buyer:** a lead-gen freelancer on Apify Starter ($29/mo). Their scheduled Google Maps scraper's Sheets export failed again, and they search "Google Sheets" in the Store or the integration picker.

**Channels:**
- Apify Store search: *realistic*. 825 monthly users sit on a shelf with one failing incumbent.
- Integration picker: *realistic*, if integration-ready Actors really surface there. Verify this.
- Discord showcase: *optimistic*, small.
- GitHub/SEO docs: *optimistic*, 2+ months away.

**Why pay instead of:**
- (a) The free incumbent. It is maintained by Lukáš Křivka, an Apify staffer. 51% of runs failing ≠ 51% of users failing. Failures may cluster in a few heavy schedules, or come from user-side OAuth or permission errors that SheetSync would also hit.
- (b) n8n, Make or Zapier Sheets nodes, which many of these users already pay for.
- (c) Downloading a CSV by hand.
- (d) The 4.8★ incumbent.

**Trust gap:** small for billing, which runs through Apify. The real friction is that an agency must share a *client's* sheet with an anonymous service-account email. Bring-your-own service account helps.

**Conversion math:**
- Taking 10% of the incumbent's users gives about 80 users. If about 40% are on paid plans, that is about 30 paying users.
- **The launch promo breaks the revenue.** At about 200 rows per run, "first 1,000 rows free per run" leaves only the $0.005 start fee, about $0.50 per user per month. 30 users ≈ $12/mo.
- The shared service account is also limited to 60 requests/min across *all* customers, which recreates the incumbent's failure mode at scale.

**Timing:** not seasonal. No deduction.

**Steelman:** captive, recurring, verified demand with an obvious quality gap. A marketplace supplies both discovery and billing. This is the T2/Apify pattern that worked last run.

**Kill shot:** a single fix by the incumbent's maintainer, or a native Apify Sheets integration, ends switching demand overnight.

**Fix:** replace "first 1,000 rows free per run" with a one-time free allowance (for example, 5,000 rows per user). Before building, read the incumbent's issue tab to confirm the failures are fixable on the Actor side.

## G1: Keyword→Brief (Apify, PPE)
**First buyer:** an n8n freelancer on a paid Apify plan, building a client's "AI blog writer" flow, who searches "keyword search volume" in the Store.

**Channels:**
- Store search: *realistic*. New 2026 entrants reached 396–717 monthly users within weeks.
- Apify MCP / x402: *optimistic*. Unmeasured, and x402 volume is concentrated in the top 1% of wallets.
- n8n template: *optimistic*. Review queue, then weeks 4–8.
- Discord: *optimistic*, small.

**Why pay instead of:**
- (a) Free: free-plan users pay the developer nothing.
- (b) ChatGPT: it cannot produce real volumes. This is a genuine edge.
- (c) DataForSEO direct, which has its own MCP server.
- (d) The leader: 717 users, **0 failures**, $0.008–0.012. The only edge left is price, at 1/3.

**Trust:** a negligible gap. Apify bills, and the cost is a fraction of a cent per keyword.

**Conversion math:**
- The first sale needs just one paid-plan user to run it once, which is likely by day 20–40.
- The test bar of 15 paid users in 14 days implies about 40–50 total users in two weeks, which is leader-level and *optimistic*.
- $300/mo needs about 95k paid keywords or 10.7k briefs a month.

**Timing:** SEO tooling is not seasonal. No deduction. There is a risk of delay while waiting for DataForSEO's written resale confirmation (ToS §7.1).

**Steelman:** the shelf is proven to reward well-built newcomers within weeks, and pipelines that run on a schedule recur without repeat selling.

**First cash:** $20 needs about 6,700 paid keywords in one month at about $0.003 net each. P50 Jan 21–25.

**Kill shot:** a commodity clone on a crowded shelf. Users who switch on price are mostly free-plan users who earn nothing.

**Fix:** make `keyword-brief`, which no one on the shelf offers, the headline product at launch. Keep the metrics event as the cheap entry, not the whole test.

## M1: ChatRelay for Jira
**First buyer:** a Jira admin at a 40-person agency on Google Workspace. They see "may stop working after January 2027" on Google's app and search "Google Chat" in Explore apps.

**Channels:**
- Marketplace and in-Jira search: *realistic* for installs. But a new app with 0 installs and 0 reviews ranks below the free 407-install app.
- "Runs on Atlassian" badge: *optimistic*. Eligibility with external webhook egress is unverified.
- Troubleshooting SEO pages: *optimistic*, 3–8 weeks to index on a new domain.
- Sponsor's Community answers: *realistic*, small.

**Why pay instead of:**
- (a) **The free Move Work Forward app, actively maintained.** This is decisive.
- (b) Hand-rolled "Send web request" automation rules, which are free and widely documented.
- (c) Doing nothing. Google's app reportedly hasn't worked for years, so many of the 11k installs are probably dormant sites. **That base never paid anything.**
- (d) Canary's paid app, which has reviews.

**Trust:** a low gap, because billing goes through Atlassian on the Atlassian invoice.

**Conversion math:**
- Suppose 20% of truly active orphans move before February and we win 15% of them. That gives about 50–150 installs.
- Sites over 10 users that evaluate convert at maybe 20–30%. That gives 5–20 paying sites.
- So a first sale is plausible, but it waits on the approval queue (live day 17–31) plus 30–60-day evaluations, which puts it in mid-December to January.

**Timing:** the 31 Jan 2027 deadline is a tailwind. December change freezes hurt slightly. No deduction.

**Steelman:** a dated, quantified, platform-enforced push of 11k sites into one search box.

**First cash:** with a $500 threshold at about $25 per site, roughly day 230.

**Kill shot:** the free competitor captures the switchers.

**Fix:** a zero-cost check before building. Install the free app, list its gaps (threading, JQL routing, JSM SLA events, the migration guide), and kill the idea if there is no gap a buyer would pay for.

## G2: LongForm Transcripts
**First buyer:** a podcast agency's n8n builder on an Apify paid plan who needs show notes from RSS feeds.

**Channels:**
- Store search: *realistic* for discovery, but it is a shelf of more than 4 recent entrants.
- MCP / x402: *optimistic*.
- Templates: *optimistic*, weeks 4–8.

**Why pay instead of:**
- (a) **steadyfetch: $0.006/min, 0 failures, already titled "Podcast Transcription", already "never charged" on failure.** G2's headline price and promise are taken.
- (b) Groq or OpenAI directly at $0.0007–0.003/min, or ChatGPT uploads.
- (c) memo23, which handles YouTube, TikTok and IG. G2 deliberately excludes those, and they are likely the largest share of inputs on this shelf.

**Trust:** low gap. There is copyright and abuse exposure.

**Conversion math:**
- steadyfetch's 134 users ran only 883 runs in 30 days, so per-user volume is small.
- $300 needs about 49k paid minutes a month. That is far above what the whole shelf appears to bill.
- A first sale is still likely within 1–3 months.

**Timing:** many podcasts and webinars pause in late December. That is minor, so no deduction.

**Steelman:** the convenience moat is real, and buyers already pay $0.05/min to memo23.

**First cash:** $20 is about 3,300 paid minutes in one month. P50 Jan 21–25.

**Kill shot:** a me-too at a higher price than the cheapest rival.

**Fix:** ship chapters, quotes and RSS watch mode on day 1, priced at or below $0.006, or don't launch.

## M2: SpecView for Confluence
**First buyer:** a Confluence admin at a 300-user SaaS company with 150 API pages on "Open API (Swagger) Integration", who sees the banner.

**Channels:**
- Marketplace search for "swagger/openapi": *realistic* for installs. But a 0-review viewer sits below the 3,186-install bundle and the free Narva.
- Migration SEO pages: *optimistic*.
- Community answers: *realistic*, small.

**Why pay instead of:**
- (a) Narva, which is free.
- (b) The bundle these admins may already own.
- (c) The orphan vendor shipping its own Forge port. Atlassian says more than 95% of paid seats have already moved.
- (d) Re-pasting specs by hand on small sites.

**The demand test is miscalibrated.** It measures a commodity viewer and leaves out the converter, the only differentiator, so it can fail for the wrong reason.

**Trust:** low gap on billing. There is real liability if the converter breaks pages.

**Conversion math:** $300 needs 20 paying sites, about 1% of the paying orphan base. That sounds feasible, but at about $15 per site the $500 payout threshold pushes first cash to late 2027.

**Timing:** a deadline tailwind. No deduction.

**Steelman:** these customers already pay, and a converter is hard for an AI-farm clone to build.

**Kill shot:** the commodity viewer arrives first and the converter arrives after the January peak.

**Fix:** build the migration scan for the largest orphan (2,873 installs) first, and make the free dry-run scan the listing's hook. Before building, also check whether Toshihiro Sato has declared a Forge migration.

## I2: Episode Study Packs
**First buyer:** a Mandarin Corner-type creator who already gates PDFs behind a $10 donation and gets a 1:1 email offering a free pack for their latest episode.

**Channels:**
- 1:1 email by the operator: *realistic*. It is compliant B2B email and the creators' addresses are public.
- Sample library: *realistic* as proof, but it brings no traffic.
- Maker post: *optimistic*.

**Why pay instead of:**
- (a) Their current 2–3-hour manual workflow.
- (b) ChatGPT with a prompt. The ideator admits this can be rebuilt "in a weekend".
- (c) Simply publishing fewer PDFs.
- Native-speaker creators also distrust AI pinyin for 多音字 (polyphonic characters).

**Trust:** a $12–39 card payment is modest, but the email comes from an unknown "learner".

**Conversion math:**
- 40 contacts × 20% reply × 50% accepting a sample × 30% paying ≈ 1.2 paying creators.
- The pass bar of 3 is a coin flip at best, and the total pool is only 100–200 creators.

**Timing:** neutral, with a slight plus because creators prepare January content. No deduction.

**Steelman:** these buyers already sell exactly this artefact, so it is a proven product with a proven bottleneck.

**Kill shot:** most creators earn too little from Patreon to justify $39/mo for work they already do.

**Fix:** lead with $12 per episode and widen the list to all language-learning podcasters (Spanish, Japanese, Korean), which escapes the 200-creator ceiling.

## C1: FunderFit
**First buyer:** an FGWA graduate who freelances for 3 small nonprofits and hears a partner mention FunderFit.

**Channels:**
- Small Substacks: *optimistic*. Queen Israel's 1.9k subscribers × about 40% open × 2% click × 10% buy ≈ 1–2 buyers.
- Academy member perk: *optimistic to fantasy* within 60 days. Noble teaches funder research, and the roster partners earn Instrumentl affiliate income, so FunderFit competes with their own revenue.
- Podcast: *fantasy* within 90 days. Calendars run 4–10 weeks, plus a recording by the sponsor.

**Why pay instead of:**
- (a) grantmakers.io or ProPublica, which are free.
- (b) **Instrumentl's free trial.** A freelancer can research one client inside it.
- (c) Candid FDO, free at library partners.
- (d) ChatGPT deep research. It hallucinates, but it is "good enough" for many.

**Trust:** a freelancer is putting their name on an AI-built list whose data lags 12–24 months.

**Conversion math:** $300 needs about 15 affiliate-referred reports a month. With 0–1 partners at a realistic 5–10% yes rate from 12 pitches, that won't happen in Q4.

**Timing:** Q4 planning is favourable, but the realistic first mention lands around day 50–75, which runs into the dead second half of December. **−1.**

**Steelman:** a real data edge over chatbots, plus a white-label deliverable the freelancer can bill at $200–500.

**Kill shot:** the partners don't reply or say no.

**Fix:** make the partner the seller. Their brand, with them keeping 60%, turns the conflict into new income for them. Pitch the small Substacks first.

## C3: Interpreter Practice Lab
**First buyer:** a bilingual adult who finished MITS's $640 course, has a CCHI oral exam booked, and watches Bridging Words.

**Channels:**
- InterpreMed and Bridging Words: *optimistic*. A 3.1k-subscriber channel yields a few hundred views per video.
- Self-paced schools: *optimistic*. They already sell mock exams, so this cannibalises them.
- The CLP publisher: *fantasy* within 90 days, because it needs a contract.

**Why pay instead of:**
- (a) ChatGPT voice role-play, which is free.
- (b) Free peer Zoom practice.
- (c) The mock exams already included in their course.

**Trust:** AI scoring of consecutive interpreting, from accented Spanish speech recognition, is hard. One bad score spreads fast in a small community.

**The chain is long:** the build runs to day 16, the calibration gate needs a recruited instructor, then a partner must say yes, then the promotion must run. Each step slips.

**Conversion math:** $300 needs about 22 passes a month, against about 1,000 CoreCHI candidates a year.

**Timing:** first promotions land in mid-November to December (slow), and the January bump comes later. No deduction.

**Steelman:** about $485 in exam fees is at stake, so buyers are motivated and price-insensitive.

**Kill shot:** the build-plus-partner chain pushes the first promotion past day 60.

**Fix:** sell a 10-dialogue $9 pass through one creator before building 150 dialogues.

## I1: Zì Bot
**First buyer:** an HSK 3 learner active in the r/ChineseLanguage Discord who uses `/quiz` daily.

**Channels:**
- Admins of the large servers: *optimistic*. Admins are pitched bots constantly, and maybe 1–2 say yes by day 30.
- Bot directories: *optimistic*, a trickle.
- The sponsor's Reddit post: *realistic* as a single spike, if subreddit rules allow it.

**Why pay instead of:**
- (a) Free Kotoba-style norms.
- (b) ChatGPT free or Go.
- (c) HelloChinese, which they already pay for.
- (d) Nothing: the quiz part is free anyway.

**Trust:** a $29 pre-order for a feature that doesn't exist yet, through an external checkout from a bot, on a platform where many users are teenagers (the paid tier is 18+). Discord's payment-parity rules add policy risk.

**Conversion math:** 10 pre-orders at 1% needs about 1,000 engaged users within 30 days, which requires a big-server adoption.

**Timing:** a tailwind ahead of January and Chinese New Year (17 Feb), but the test runs before that peak. No deduction.

**Steelman:** there is no Kotoba equivalent for Mandarin, so it could become the default bot.

**Kill shot:** the free-bot expectation.

**Fix:** run the paid test in January with a working `/practice`, or sell Server Pro to teachers who run class servers.

## C2: Client Safety Kit
**First buyer:** a solo OSH consultant with 6 retainer clients in Texas who listens to Sheldon Primus.

**Channels:**
- Inogen member firms: *fantasy*. They are established EHS firms with their own content and procurement.
- Primus: *optimistic*. Audience size is unverified, and his calendar runs 4–8 weeks.
- D2 cross-sell: *fantasy* until D2 has subscribers.
- ASSP: 60–120 days.

**Why pay instead of:**
- (a) Free CPWR and NAWIC Spanish talks.
- (b) Free insurer loss-control material.
- (c) toolboxtalk-ai at $49.
- (d) ChatGPT.

**Trust:** the largest gap in the round. The consultant's professional reputation, and possibly their credential, goes on Spanish safety content they may not be able to read.

**Dependency:** it needs D2's ingest, which is not built yet.

**Timing:** northern trades slow down in December, and consultants are busy with year-end work. **−1.**

**Steelman:** recurring retainer deliverables are a real pain, and the OSHA-data hook is distinctive.

**Kill shot:** consultants refuse liability for AI safety content.

**Fix:** sell only the "OSHA cited your industry this month" brief, as a D2 add-on, once D2 has at least 10 paying users.

## I3: Role-Play Room
**First buyer:** a community-college instructor of first-year Chinese, planning spring.

**Channels:**
- 1:1 instructor emails: *realistic* to send, but replies are slow during end-of-semester and finals.
- Maker post: *optimistic*.
- ACTFL follow-ups: *optimistic*, landing late November to December.

**Why pay instead of:**
- (a) Free generic tutors.
- (b) Publisher drills that come with the textbook.
- (c) Nothing.
- Instructors rarely pay with a personal card, and department purchases bring FERPA, DPA and procurement requirements that the sponsor won't sign.

**Timing:** the spring adoption window is now, but trials can't prove anything before it closes. Finals take instructors' attention in December. **−1.** If the window is missed, the next is July–August 2027, so P50 ≈ day 300, which breaches the hard gate.

**Steelman:** assignable, checkable and level-locked practice is a real gap that ChatGPT doesn't fill.

**Kill shot:** the institutional buying cycle.

**Fix:** sell to individual private tutors (italki and Preply teachers) at $10/mo. They buy quickly, with their own card.

## G3: AnswerShare GEO API
**First buyer:** a growth engineer at an SEO agency who is building a client report.

**Channels:**
- RapidAPI search: *optimistic to fantasy* for a new API with no reviews.
- MCPize: *fantasy*. It publishes no buyer volume.
- Free MCP directories: they bring free keys, not payment.
- n8n template: weeks 4–8.

**Why pay instead of:**
- (a) MentionsAPI: from $0.02 per check, with MCP.
- (b) Otterly's API.
- (c) Apify GEO Actors.
- (d) DIY.

**Trust:** agencies won't put an anonymous API's numbers in front of clients, especially when the API's answers differ from the consumer ChatGPT app.

**Conversion math:** the free tier attracts testers. 24 subscribers at $29 is far out of reach.

**Timing:** neutral.

**Steelman:** "are we in ChatGPT?" is a hot question that clients pay to have answered.

**Kill shot:** no channel and a cheaper incumbent. P50 > 180, so it fails the hard gate.

**Fix:** kill it, or move it to Apify's GEO shelf only if no other idea uses the Apify slot.

## U4: AI-matched job board, three variants
| Variant | Score | P(≤30d) | P(≤90d) | P50 | P90 |
|---|---|---|---|---|---|
| a. Free for seekers; employers pay to post later (as proposed) | 1 | 0.00 | 0.02 | never | never |
| b. Seekers pay $9–19/mo from day 1 | 2 | 0.08 | 0.20 | >180 | never |
| c. Niche board (one profession or skill, e.g. Mandarin–English bilingual roles), with employer "featured" posts at $49–99 plus a seeker-paid digest | 2 | 0.02 | 0.10 | >180 | never |

**a. Free first, employers later.**
- First buyer: a startup hiring manager paying $199 to post on a board that has no seekers. Nobody does that.
- Traffic depends on programmatic SEO, which is *fantasy* inside 90 days. A new domain competes with Indeed, LinkedIn, Google for Jobs and Hiring Cafe, and Google demotes scaled, duplicative pages.
- The model also cannibalises itself: why would an employer pay to post a job you already aggregate for free from their ATS feed?
- It funds no tokens for months, which contradicts the goal.
- Hiring slows in Q4 and December: **−1.**

**b. Seekers pay from day 1.**
- First buyer: a laid-off engineer six weeks into their search.
- The only fast channel is a human Show HN or community post: *realistic* as a single spike of 1–5k visitors. At 0.2–0.5% paid conversion, that is 2–25 buyers if it lands, and zero if it doesn't. Job subreddits mostly ban self-promotion.
- **Hiring Cafe already does ATS-feed matching for free**, and Jobright has a free tier.
- "Pay to see jobs" from an anonymous site matches the job-scam pattern the FTC warns about. The trust gap is the largest of any variant.
- January is the job-search peak, so the timing is fine.
- This is the fastest variant, but still has about an 80% chance of no sale in 90 days.

**c. Niche board.**
- This is the only variant with a defensible angle: a niche the generalists serve badly, where employers already pay niche boards.
- It still needs months of traffic unless a partner who already owns the niche audience, such as a newsletter or association, hosts or promotes it in exchange for a share of employer posts.

**Verdict:** none of the three passes the P50 ≤ 180-day gate as stated. If the sponsor wants to pursue it, **c plus a named partner** is the only version with a credible channel, and b is the only one with a sub-90-day chance. Kill a.

**Legal notes:**
- Resumes are personal data under GDPR and CCPA.
- Recruitment AI is high-risk under the EU AI Act if it serves EU users. Geo-limit to the US at launch.
- Linking out to ATS postings, rather than reposting them, reduces terms-of-service exposure.
