# Investment Committee Report: run 2026-10-06

_Chair: investment-committee. Inputs: 15 idea briefs (`ideas/tech.md`, `writer.md`, `artist.md`, `data.md`, `scout.md`), 5 reviews (`reviews/sales-skeptic.md`, `market-analyst.md`, `autonomy-auditor.md`, `legal-risk-analyst.md`, `unit-economics-analyst.md`), and the reference files `operator-constraints.md`, `scoring-rubric.md` and `idea-brief.md`. Decision date: 2026-10-06._

---

## 1. Executive summary

1. I scored all 15 ideas with the rubric formula. Composites run from **4.90 to 6.20**, so there is no runaway winner, and no idea scored above 6 on sale plausibility.
2. **The hard gates reject one idea: T3 TipSplit for Clover** (sales-skeptic P50 = 185 days, over the 180-day gate). No idea breaks the upfront, legal or human-hours gates. A1 and A3 pass on upfront cost only under conditions.
3. **Pick 1: D2 InspectionWatch** (composite 6.20, ranked #1). Upfront $12. 7 subscribers at $49 reach $300/mo. Sponsor time is about 2 h of setup, then 0.5–0.75 h/week. Legal score 7 (Med). The weak spot is sales: P50 is 130 days. To address it, D2 changes in four ways: launch in 3–5 states, sell through the sponsor's personal emails plus editor data columns, keep company names off the public pages, and offer a founding price.
4. **Pick 2: T2 Accela/EnerGov Permit Actor on Apify** (5.95, #3). Upfront $0, the fastest P50 in the batch (50 days) and about 0.2 h/week of sponsor time. But revenue per user is thin: $300 needs about 20 steady paid users. Legal score 5. It runs as a hedge with a token cap and reuses D2's ingest code.
5. **T1 RainCheck (6.15, #2) is not picked now.** Its P50 is 170 days, it would launch in October into the off-season, and Jobber's review time and API are unverified. Revisit it in January 2027 for a spring launch.
6. **Both picks together:** $12 upfront, about 3–3.5 h of one-time sponsor setup and about 0.6–1.0 h/week ongoing. That fits the sponsor budget.
7. Kill checkpoints fall on days 21, 45 and 90 for D2, and days 30, 60 and 120 for T2 (Section 4).

---

## 2. Scoreboard (all 15 ideas, sorted by composite)

`composite = 0.30·Sale + 0.20·Market + 0.20·Autonomy + 0.15·UnitEcon + 0.15·Legal`. Scores are used exactly as each reviewer gave them; the committee changed none. Ties are broken by Sale plausibility, the heaviest-weighted dimension.

Worked example, D2: 0.30·4 + 0.20·6 + 0.20·7 + 0.15·9 + 0.15·7 = 1.20 + 1.20 + 1.40 + 1.35 + 1.05 = **6.20**.

Column sources:
- Upfront $ and sales/mo for $300: unit-economics-analyst's re-derived figures.
- P50/P90: sales-skeptic, counted from today with build and review time included. "never" means less than a 90% chance of any sale within 12 months.
- Human hours: autonomy-auditor.

| # | ID | Idea | Sale | Mkt | Auto | UnitEc | Legal | **Composite** | Upfront $ | P50 / P90 days | Human hrs setup / per wk | Sales/mo for $300 | Gate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | D2 | InspectionWatch (OSHA alerts) | 4 | 6 | 7 | 9 | 7 | **6.20** | 12 | 130 / never | 2 / 0.5–0.75 | 7 subs ($49) | Pass |
| 2 | T1 | RainCheck for Jobber | 3 | 7 | 8 | 7 | 8 | **6.15** | 12 (+20 if SMS) | 170 / never | 3.5–4 / 0.25–0.5 | 18 subs | Pass (P50 near the gate) |
| 3 | T2 | Accela/EnerGov Permit Actor (Apify) | 6 | 5 | 9 | 4 | 5 | **5.95** | 0 | 50 / 200 | 1–1.5 / 0.1–0.25 | ~107k paid permits ≈ 20 steady users | Pass |
| 4 | S2 | Bilingual Toolbox Talks | 4 | 4 | 8 | 7 | 7 | **5.70** | 33–47 | 110 / never | 3–3.5 / 0.25–0.5 | 21 orders (or 38 subs) | Pass |
| 5 | S3 | Custom Wedding Toasts & Eulogies | 6 | 3 | 4 | 8 | 8 | **5.60** | 29–43 | 45 / 160 | 3 / 1–1.5 (grows with orders) | 12 orders | Pass |
| 6 | A3 | "Looks Like Me" visual schedule cards | 5 | 5 | 7 | 3 | 8 | **5.55** | 69 (re-roll risk to ~105) | 90 / never | 3–4 / 0.25–0.5 (+0.5 with TPT) | 31 orders | Pass, conditional (see §3) |
| 7 | W2 | Florida HOA Board Letter Kit | 4 | 4 | 8 | 7 | 6 | **5.55** | 18–44 | 110 / never | 2.5–3 / 0.25–0.5 | 15 sales (≈9 kits) | Pass |
| 8 | D1 | LanguageBids tender alerts | 3 | 5 | 7 | 7 | 8 | **5.55** | 12 | 170 / never | 3 / 0.75 | 12 subs | Pass (P50 near the gate) |
| 9 | S1 | Done-For-You Airbnb Guidebook | 5 | 4 | 5 | 8 | 6 | **5.40** | 34–48 | 90 / never | 3 / 0.75–1.25 | 10 orders | Pass |
| 10 | D3 | LabelScout TTB COLA intel | 3 | 4 | 8 | 6 | 8 | **5.40** | 12 | 175 / never | 3 / 0.25–0.5 | 7 Pro subs | Pass (P50 near the gate) |
| 11 | A2 | Little Guests wedding activity book | 4 | 5 | 6 | 5 | 7 | **5.20** | 41–53 | 110 / never | 2.5–3 / 0.5–1 | 23 orders | Pass |
| 12 | T3 | TipSplit for Clover | 2 | 7 | 7 | 5 | 6 | **5.05** | 12 | **185** / never | 4–5 / 0.5–1 | 29 locations | **REJECT (P50 > 180)** |
| 13 | W3 | Grant Deadline Desk: [State] | 3 | 4 | 6 | 5 | 9 | **5.00** | 12 | 160 / never | 4–4.5 / 0.75–1 | 39 annual subs | Pass |
| 14 | W1 | Bid Brief: Facilities Services | 4 | 4 | 5 | 5 | 8 | **4.95** | 0–12 | 120 / never | 3–3.5 / 1–1.5 | 19 subs (≈23 at the real price mix) | Pass |
| 15 | A1 | "Closing Day" house portraits | 5 | 4 | 4 | 5 | 7 | **4.90** | 42–54 (digital only) | 70 / never | 3–3.5 / 1–2+ (Q4) | 18 orders | Pass, conditional (see §3) |

**Soft screen from `operator-constraints.md`:** a P50 over 90 days "needs a strong justification". Only five ideas have a P50 of 90 days or less: T2 (50), S3 (45), A1 (70), A3 (90) and S1 (90). Every other idea, including pick #1 (D2), needs that justification. D2's is in §4.

---

## 3. Rejected by hard gates

| Gate | Ideas rejected | Reason |
|---|---|---|
| P50 time to first sale > 180 days | **T3 TipSplit for Clover** | Sales-skeptic P50 = 185 days, P90 = never. The delays stack: about 15 days to build, then an unverified 2–4 week Clover approval, then a self-imposed 30-day trial. The first charge lands around day 75–100 at best, and cash arrives a month later because Clover pays out in arrears. The unit-economics analyst agrees: first cash in January and $300 not reached within 12 months. The legal analyst adds that the planned "credit-card-fee deduction" toggle is illegal in California (Lab. Code §351). |
| Upfront capital > $100 | None outright | **Two conditional passes:** (a) **A3** is budgeted at $69, but the unit-economics analyst shows that 2.5× image re-rolls push it to about $105. It passes only if launched with 3 avatars or a cheaper draft model. (b) **A1** is $42–54 for digital only. Adding the Printify samples needed to QC physical upsells makes it $95–114. It passes only if the physical products are deferred. |
| Legal safety ≤ 3 | None | The lowest legal score is T2 at 5. |
| > 3 human hours/week ongoing | None on paper | Near misses: **S3** reaches about 2–3 h/week at the stretch volume (about 35 orders/month) because of per-order sensitive-content review and anxious-buyer Etsy messages. **A1** runs 1–2+ h/week in the Q4 peak. Both would need re-checking if they scaled. |

---

## 4. Top picks

### Resolving reviewer conflicts (this drives the picks)

| Idea | Disagreement | Committee ruling |
|---|---|---|
| **S3** | Sales-skeptic **6** vs market-analyst **3** | **Each reviewer is right about a different horizon.** The skeptic is right about the *first* sale. An anxious best man or a grieving son searching Etsy by role is a real buyer with a deadline, and the $17/mo Wedding Speech AI app shows people pay for a *finished deliverable on a trusted marketplace*, not a generator. Most of the market analyst's competitors (My Wedding Toast, Speechcraft, ToastWiz, free generators) sit *off* Etsy. The market analyst is right about *sustained* volume. Etsy already has disclosed-AI speech listings at $7.35. Mandatory AI disclosure tells the buyer "this is ChatGPT". Shops with 4k+ reviews take the anxious buyer. So the unit-economics ramp to 9–14 orders/month by spring is optimistic. **Verdict:** S3 is a credible first-dollar idea with a low ceiling. Its autonomy score of 4 keeps it out of the picks: a human reviews about 10% of orders by design and the Etsy inbox needs a daily check. Runner-up. |
| **T2** | Autonomy **9** vs unit-economics **4** | **Both are right, and for the goal the unit-economics view binds.** Autonomy measures human time, and there really is almost none: Apify bills, self-serve publishing, no per-sale human. Unit economics measures whether the business pays for its own tokens, and on its own it probably doesn't. Revenue is $2.80 per 1k permits net. $300 needs about 20 steady paid users, not the ideator's 10. Maintenance tokens run about $120/mo. The market analyst's evidence backs the pessimism: the closest peer Actor has **38 total users and 6 monthly**. A zero-human business that never covers its tokens fails the brief. **Verdict:** T2 is picked as a **capped hedge**, not as the $300 engine. Scope shrinks to about 20 demand-verified jurisdictions, maintenance tokens are capped at $60/mo, and there is a freeze rule. It earns the slot because it is the fastest path to *any* stranger's dollar (P50 50, P90 200, the best P90 on the board) at $0 upfront and about 0.2 h/week. |
| **D2** | Unit-economics **9** / market **6** vs sales-skeptic **4** | The unit-economics analyst explicitly hands the willingness-to-pay question to the other reviewers. The skeptic's objection is about the **channel**, not the buyer: a solo consultant has budget authority and an obvious ROI, but the planned main channel (sponsor LinkedIn posts) is unlikely to produce paid trials. The market analyst confirms the gap is *packaging*: 4+ Apify OSHA Actors exist for technical buyers, and nobody sells a territory email to non-technical consultants. **Ruling:** the skeptic is right about the channel, so D2 is pivoted to channels with a direct line to the buyer (below). The buyer and the economics stand. |
| **T1** | Market **7** / autonomy **8** / legal **8** vs sales-skeptic **3** | Both are right. The market is real and uncontested inside the Jobber marketplace, but an October build plus an unverified Jobber review lands the listing in November–December, when lawn and exterior trades go dormant. Unit economics agrees ($300 only in M10). **Ruling:** a good business on the wrong calendar. Not picked now; it is runner-up #1 with a January restart. |
| **D1** | Unit-economics **7** / legal **8** vs sales-skeptic **3** | The skeptic's own fix (sell only the EU/TED and Canada feed) is **undercut by the market analyst**: Stotles already sends free alerts on CPV 79530000/79540000 for the UK and EU. The autonomy auditor adds that ATA listservs are members-only, with dues above the $100 cap. The only real gap is US state, court and county RFPs, which sit on portals whose terms ban scraping. **Ruling:** the skeptic's 3 stands, and the market analyst's evidence makes it worse. |
| **S1** | Unit-economics **8** vs market **4** | The market analyst wins. Touch Stay's AI generator and StayScan already build a guidebook from a listing URL in minutes, which removes the "done-for-you" gap the ideator thought existed. The unit-economics 8 depends on volume the market evidence does not support. |
| **A3** | Autonomy **7** vs unit-economics **3** | Unit economics wins. 31 orders/month fails the rubric's "< 30" test. Custom packs cost about $10 per order in generation. The upfront budget can overrun the cap. |
| **T3** | Market **7** vs sales-skeptic **2** | Moot, because the idea is gated. The skeptic was right that the 30-day trial was self-inflicted. |

### Combinations and pivots considered

- **The rejected idea's best element (T3):** platform-handled billing removes the checkout trust gap. T2 already has it through Apify billing. For T1 the lesson is to **drop long trials and charge from day 1** with a founding annual plan, as the skeptic also proposed. T3 itself cannot be rescued on this calendar.
- **D2 + T2 share infrastructure.** Both are scheduled public-records ingest → normalised schema → "new since last run" delta → nightly self-test. The operator builds one ingest and self-test library and uses it in both, which cuts build and maintenance tokens. This is part of why T2 is the second pick rather than T1.
- **D2 + S2 (later, not in the 30-day plan).** S2's best element is trade-specific bilingual talks with a dated meeting log. That could become a D2 upsell: a "client safety kit" keyed to the most-cited standards in each inspected client's NAICS code. Revisit at month 3 if D2 has 5 or more paying subscribers.
- **Explicit pivots adopted.**
  - **D2:** launch in 3–5 federal-OSHA states instead of 50 state pages. Use the sponsor's personal emails and editor data columns as the primary channel, and demote LinkedIn. Keep establishment names off public pages. Add a founding price.
  - **T2:** launch with about 20 demand-verified jurisdictions instead of "120+". Owner names are off by default. Drop the Upwork replies (the auditor notes they need an ID-verified Upwork account and count as bidding). Cap maintenance tokens.

---

### Pick 1: D2 InspectionWatch (daily OSHA inspection and citation alerts for safety consultants)

**Thesis.** Independent safety consultants and trainers win clients in the weeks after OSHA walks in. Today they find out late, from clunky free lookups or from Apify scrapers they can't use. A daily territory email of yesterday's inspections, with 5-year history and a plain-English "what to pitch" line, sells to a buyer who decides alone and gets payback from a single new client. It needs only **7 subscribers** to fund the operator, the best ratio in the batch.

**Key numbers**

| Metric | Value | Source |
|---|---|---|
| Upfront $ | **$12** (domain). DOL API key and free hosting tiers cost nothing. | ideator, confirmed by unit-economics |
| P50 / P90 days to first sale | **130 / never** (P(≤30d) 8%, P(≤90d) 30%). The unit-economics ramp is more optimistic, with the first subscriber in M2. | sales-skeptic |
| Sales/month for $300 | **7 subs at $49** ($45.81 net each). About 11 if every subscriber is on the $29 founding price. 3 subs cover tokens. | unit-economics |
| Human hours | **Setup about 2 h**: Lemon Squeezy KYC, domain, DOL key. **Weekly 0.5–0.75 h**: genuinely authored outreach and replies to editors. | autonomy-auditor |
| Legal risk | **7/10, Medium.** Top risk is defamation or false light from public pages naming establishments under "fatality" inspections. | legal-risk-analyst |
| Break-even timeline | Operating-positive in M4, payback in M6, $300/mo in M8 (if the ramp holds) | unit-economics |

**Why a P50 over 90 days is acceptable here** (the operator-constraints justification):
- The buyer has budget authority and a 100× ROI, so conversion is a reach problem, not a value problem.
- Only 7 sales are needed.
- At about $100/mo of tokens it is the cheapest data product to keep alive.
- The kill gates below cut the loss early if the pivoted channel fails.

**Launch configuration (pivoted):**
- **Pilot states:** 3–5 federal-OSHA states, e.g. TX, FL, GA, OH, PA. Their private-sector inspections come straight from federal OSHA with no state-plan reporting lag. State-plan states (CA, WA, MI, …) are added only after a timeliness check.
- **Pricing:** Territory $49/mo (1 state), Regional $99 (5 states). The **first 10 customers get a founding price of $29/mo**, locked for 12 months. A 7-day trial, card required, through Lemon Squeezy.
- **Public pages:** state aggregates only, with no establishment names. Names, history and the "what to pitch" line appear only in the paid feed. DOL fields are quoted verbatim with dates and source links, plus the line "an inspection is not a violation; citations are initial and may be contested". There is a correction/takedown form.
- **Positioning:** sold to consultants and trainers. The acceptable-use policy restricts attorney solicitation (ABA Rule 7.3).

**30-day launch plan**

*Week 1 (day by day)*

| Day | AI operator | Human sponsor |
|---|---|---|
| D1 (Wed Oct 7) | Scaffold Cloudflare Workers + D1. Pull DOL v4 inspection dataset samples and confirm which fields exist (open date, type, NAICS, scope, union) and how fresh they are for the pilot states. | Create the Lemon Squeezy store and pass KYC. Buy the domain. Register the DOL Open Data Portal key. (≈1.5 h) |
| D2 | Daily-delta ingest for inspections and violations. 5-year backfill for the pilot states only, keeping storage under the free tier. | — |
| D3 | Plain-English dictionary of standards ("1926.501 = fall protection, construction"). 5-year history join per establishment. Industry top-cited-standards table. | — |
| D4 | Paid daily email template and web dashboard behind the license key. Lemon Squeezy checkout with trial. Public state aggregate pages. Terms: no warranty, AUP, correction form. | — |
| D5 | Spot-check 50 random records against osha.gov. Build a sample "yesterday in Texas" email. From public directories and firm websites, compile 40–60 named independent safety consultants and trainers in the pilot states, plus 10 ASSP chapter newsletter editors. Draft a personal email for each. | Review and approve the terms and disclaimer wording. (≈0.25 h) |
| D6 | Go live: pages indexed, digest signup open. | Send the first 10 personal emails from the sponsor's own address, each offering 2 weeks of free access with an individual opt-out (not bulk). (≈0.3 h) |
| D7 (Tue Oct 13) | Send the editor pitches one-to-one from the operator inbox: a free monthly "OSHA activity in your region" data column. Start the metrics log: visits, signups, trials, replies. | Send 10 more personal emails. |

*Weeks 2–4*

| Week | AI operator | Human sponsor |
|---|---|---|
| Wk 2 (Oct 14–20) | Daily sends to trial users. Follow-up to non-openers. Deliver the first data column to any editor who accepts. Add 1–2 states if trial users ask. Watch for DOL v4 API breakage. | 20 more personal emails. One genuinely authored LinkedIn post using a real state statistic. (≈0.6 h) |
| Wk 3 (Oct 21–27) | Convert the first trials: a day-5 "here's what you'd have missed" recap and a founding-price reminder. Survey trial users who decline: price, freshness or territory? **Day-21 checkpoint.** | Reply to editors who want a human contact. Approve any refund. (≈0.5 h) |
| Wk 4 (Oct 28–Nov 5) | Publish a free "Q3 2026 most-cited OSHA standards by industry" report and pitch it to EHS Today, ISHN and Safety+Health. Decide on price or territory changes from the survey. Report at day 30: trials, paid, MRR, token spend. | Read the day-30 report and make the go/no-go call. (≈0.5 h) |

**Kill criteria**
- **Day 21:** fewer than **15 trial or free-sample signups** from 40 or more personal emails plus pages and columns, **or** fewer than 3 positive replies. The channel has failed, so test the skeptic's version: one state at $19/mo with a free weekly sample.
- **Day 45:** **0 paid subscribers** after 20 or more trials, or trial-to-paid under 10%. This is a value problem (free osha.gov is good enough). Pivot the buyer to safety-training providers, or kill.
- **Day 90:** fewer than **3 paid subscribers**, meaning it does not cover tokens. Kill.
- **At any time:** a DOL API outage over 7 days with no fallback means pause sales. Two or more defamation or takedown complaints in a month means review the public pages before continuing.

**Top 3 risks and mitigations**
1. **Free substitutes** (osha.gov shows inspections within 0–2 days; safetyrecord.org; Apify Actors at $3.50/1k) push willingness to pay down. *Mitigation:* sell the convenience none of them offer: the territory email, 5-year history and "what to pitch". Test the founding price. Measure with the day-21 survey.
2. **Distribution (the source of the sales score of 4).** *Mitigation:* personal sponsor emails and editor data columns are the primary channel, LinkedIn is secondary, and SEO is a bonus. The day-21 and day-45 kill gates cap the exposure.
3. **Defamation and "ambulance-chasing" reputation.** *Mitigation:* no names on public pages, verbatim DOL fields with dates, the "inspection ≠ violation" line, a correction form, consultants first, and an AUP for attorney subscribers. An LLC once revenue exists.

---

### Pick 2: T2 Accela & EnerGov Permit Extractor (Apify Store Actor, pay per result)

**Thesis.** Roofing, solar and HVAC lead-gen buyers on Apify can't get permits from the hundreds of counties that run Accela Citizen Access or Tyler EnerGov, because every existing permit Actor relies on Socrata, ArcGIS or CKAN open data. A maintained, nightly-verified Actor for those portals sells through Apify's own search and billing. That means no audience, no checkout and almost no human time, which makes it the fastest route in the batch to a stranger's dollar.

**Key numbers**

| Metric | Value | Source |
|---|---|---|
| Upfront $ | **$0** | ideator, confirmed by unit-economics |
| P50 / P90 days to first sale | **50 / 200** (P(≤30d) 30%, P(≤90d) 60%). This is the best P90 on the board. Expect the first "sale" to be cents to a few dollars. | sales-skeptic |
| Sales/month for $300 | **About 107k paid permits/month, roughly 20 steady paid "watch" users** at about $12–17/month each. Net is $2.80 per 1k permits after Apify's 20% and platform usage. Free-plan usage pays nothing. | unit-economics |
| Human hours | **Setup 1–1.5 h**: Apify account, payout KYC, tax form. **Weekly 0.1–0.25 h**: payout review and rare C&D handling. | autonomy-auditor |
| Legal risk | **5/10, Medium.** Portal terms (Accela's site terms are non-commercial), cease-and-desist letters and IP blocks, Apify takedown, and homeowner names being used for TCPA/DNC-violating outreach. | legal-risk-analyst |
| Break-even timeline | On the reviewer's ramp: operating-positive in M8, $300 not reached within 12 months. **This is why it is the hedge, not the engine.** | unit-economics |

**Operating rules for the hedge:**
- **Scope:** about 20 jurisdictions, picked from evidence of real demand (Apify issue requests, r/webscraping and Upwork asks, read-only). Not "120+".
- **Requests:** HTTP-only. Honour robots.txt and per-portal use notices. A **CAPTCHA or login means drop the jurisdiction, never solve it.** Drop any jurisdiction that objects.
- **Personal data:** the owner-name field is **off by default**. The README has a legality and acceptable-use section that forbids TCPA/DNC-violating outreach. The marketing never says "homeowner leads".
- **Tokens:** maintenance capped at **$60/mo** after the build. Ingest and self-test code is shared with D2.

**30-day launch plan** (runs alongside D2 and starts on day 2, after the sponsor's D2 setup)

*Week 1 (day by day)*

| Day | AI operator | Human sponsor |
|---|---|---|
| D1 (Wed Oct 7) | Desk research, read-only: list the Accela/EnerGov jurisdictions people have actually asked for. Check robots.txt, terms and CAPTCHA presence for each. Shortlist 25. | — |
| D2 | Accela ACA module (ASP.NET search postbacks, HTTP-only). Test on 5 shortlisted portals. | Create the Apify account. Complete payout KYC (photo ID) and the tax form. (≈1–1.5 h) |
| D3 | Extend Accela to the rest of the shortlist and record the failures. Normalised schema: permit #, type, description, status, issued date, address, parcel, valuation, contractor, source URL, plus owner (off by default). | — |
| D4 | EnerGov CSS module using its JSON search endpoints. Merge into the shared schema. | — |
| D5 | "Watch" mode that emits only permits that are new since the last run. Nightly self-test of every listed jurisdiction that auto-hides broken ones. | — |
| D6 | README: platforms named in the title ("Accela & EnerGov building permits"), a verified-jurisdiction table, the legality and AUP section, pay-per-event pricing ($4.00/1k permits + $0.02/run start), input schema, and one Clay or n8n "new roofing permits → CRM" recipe. | — |
| D7 (Tue Oct 13) | Publish to the Apify Store. Submit to Apify's Store newsletter and community showcase. | Confirm that payout settings show as complete. (≈0.1 h) |

*Weeks 2–4*

| Week | AI operator | Human sponsor |
|---|---|---|
| Wk 2 (Oct 14–20) | Watch Store analytics: searches, runs, paid vs free users. Fix failing jurisdictions. Answer Apify issue threads. Add a coverage-request form. | — |
| Wk 3 (Oct 21–27) | Add the jurisdictions users requested, after the robots and terms check. Publish a second listing or README section for "EnerGov Citizen Self Service scraper" to catch exact-match searches. Write a second integration recipe (Make or Zapier). | — |
| Wk 4 (Oct 28–Nov 5) | **Day-30 checkpoint:** distinct users, paid-plan users, events billed, token spend against the $60 cap. Recommend continue, freeze or kill. | Read the day-30 note. (≈0.1 h) |

**Kill criteria**
- **Day 30:** fewer than **10 distinct users** have run it, *or* more than 40% of the launch jurisdictions are dropped for CAPTCHA or blocking. Freeze: leave it listed, run only the nightly self-test and stop new development.
- **Day 60:** less than **$10 of paid events** earned. Freeze.
- **Day 120:** run-rate below **$75/month net**, which means it doesn't cover its capped tokens. Kill and unpublish.
- **Immediately:** any Apify takedown notice. Or more than 2 agency cease-and-desist letters in a quarter, which signals a pattern and calls for re-evaluating legal exposure.

**Top 3 risks and mitigations**
1. **Thin revenue and free-plan leakage.** The peer Actor has 6 monthly users, and free-plan runs earn $0. *Mitigation:* design for recurring "watch" users through the Clay and n8n recipes. The run-start fee sets a revenue floor. The token cap and freeze rule stop it from becoming a hobby that burns money.
2. **Legal and platform exposure** (score 5). *Mitigation:* no CAPTCHA solving or logins, robots.txt and polite rate limits, owner field off by default, AUP, drop any objecting jurisdiction within 24 h, and a fast response to Apify complaints.
3. **Maintenance load and copycats.** Heterogeneous ASP.NET portals break, other permit-Actor authors could add Accela within weeks, and Shovels.ai already covers many of these counties. *Mitigation:* keep coverage narrow and verified and publish an honest verified list. The nightly self-test auto-hides breakage. Accept that the moat is short-lived; this is a hedge.

**Both picks together:** $12 upfront. About 3–3.5 h of sponsor setup, within the 2–4 h budget. About 0.6–1.0 h/week of sponsor time, at the 1 h ideal. Operator tokens of about $160/mo at steady state ($100 for D2 plus a $60 cap for T2) after about $300 of build in October.

---

## 5. Runners-up

| Rank | Idea | What would need to be true for it to win |
|---|---|---|
| 1 | **T1 RainCheck for Jobber** (6.15) | Jobber confirms that app review takes 3 weeks or less **and** that the public API can edit visits. If both hold, start the build in January 2027 so the app is listed before the March lawn and exterior ramp, and charge from day 1 with a founding annual plan and no long trial. A snow-and-ice or southern-exterior v1 is the only way to sell this winter. |
| 2 | **S2 Bilingual Toolbox Talks** (5.70) | It needs at least 2 trades with **no** trade-specific bilingual Etsy listing (the reviewers already see near-identical AI packs appearing), a native-speaker check showing the Spanish holds up on a jobsite, and the subscription upsell moved off Etsy files to avoid the fee-avoidance risk. It could later fold into D2 as a consultant "client kit". |
| 3 | **S3 Custom Toasts & Eulogies** (5.60) | It has the fastest first sale (P50 45) and the best P90 after T2, but it would need disclosed-AI listings to convert at 1% or more against review-rich human writers, and sensitive-order review plus the Etsy inbox to stay under 1 h/week. Lead with eulogies and retirement toasts in October–December at $19 to collect 10 reviews before wedding season. |

---

## 6. Observations about the idea set as a whole

**Patterns**
- **The composite spread is narrow** (4.90–6.20), and the top three are within 0.25 of each other. The rubric did not find a clear winner, so the picks are judgment calls, made explicit in §4.
- **Market and sales scores pull in opposite directions.** Integration and data ideas (T1, T3, D2) score well on market and badly on sales because the buyer can't find them yet. Etsy ideas (A1, S1, S3) score the other way: the buyer is easy to reach, but the shelf is a red ocean. No idea has both a buyer channel that already exists and an uncrowded shelf. T2 comes closest.
- **Ideators underestimate time to first sale by roughly 3–5×.** Their estimates were 14–65 days; the skeptic's P50s are 45–185 days. Thirteen of 15 ideas have a P90 of "never". Ideators counted from launch rather than from today, assumed trials convert immediately, and left out marketplace review times.
- **Ideators ignored build-phase token burn** (about $80–250 in M1 per the unit-economics analyst) and **email-provider daily caps** (Resend's 100/day breaks T3's statements and D1's digest).
- **Seasonality was ignored at launch.** It is October. T1 (lawn and exterior), A2 and S3 (weddings) and W2 (HOA annual meetings, January–March) all launch into a trough.
- **Six of 15 ideas are "public government records → paid feed"** (W1, W3, T2, D1, D2, D3). The ideators converged on one pattern. Its strength is a real data moat; its shared weakness is the absence of a buyer channel.
- **Seven of 15 ideas run on one Etsy account** (W2, A1–A3, S1–S3). Etsy has no messaging API, so there is hidden daily human time. Etsy no longer returns buyer emails. Three designs (A1, S1, S2) include off-platform upsells that break Etsy's fee-avoidance policy. A single suspension would freeze them all.

**Blind spots in the ideators**
- **No idea validates willingness to pay before building.** None uses a pre-sale, a waitlist with deposits, or a $1 test listing. Both picks have kill gates for this reason.
- **Over-reliance on channels the operator can't use or that are slow:** "SEO in 3–6 months", "the sponsor posts in Facebook, LinkedIn or Reddit groups", "Pinterest auto-pinning" (banned by Pinterest's developer guidelines), "Substack discovery" (no API, plus AI filtering). Only T2 and T3 used marketplaces that also handle billing.
- **Few B2B buyers with real budgets were found through partners who already own them.** Examples would be course creators for W1, Clover resellers for T3 and ASSP editors for D2. The sales-skeptic's fixes (affiliate shares with niche creators, founding prices) were missing from the briefs.
- **Platform-policy homework was uneven.** It was good on Etsy AI disclosure. It missed the Etsy off-platform rule, the Etsy API's messaging and email gaps, Pinterest's "user chooses each Pin" rule, Substack's lack of an API, TPT's lack of an upload API, and A2P 10DLC for SMS.
- **The "why not ChatGPT" test was applied honestly to writing and art ideas but less so to data ideas.** COLA Cloud's MCP server (D3) and free Stotles alerts (D1) are close chatbot or free substitutes that the ideators did not find.
