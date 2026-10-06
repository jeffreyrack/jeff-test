# Investment Committee Report: run 2026-10-06, round 2

_Chair: investment-committee. Inputs:_
- _13 idea briefs: `ideas/agent-economist.md` (G1–G3), `channel-partner.md` (C1–C3), `insider.md` (I1–I3), `marketplace-native.md` (M1–M3) and `user.md` (U4)._
- _6 reviews: sales-skeptic, market-analyst, autonomy-auditor, legal-risk-analyst, unit-economics-analyst and demand-validator._
- _The reference files `operator-constraints.md`, `scoring-rubric.md` (including the additional decision rules) and `lessons-learned.md`._
- _Round 1's `runs/2026-10-06/REPORT.md` and `runs/2026-10-06-eval-user-ideas/VERDICT.md`._

_Decision date: Tue 2026-10-06. No round-1 build has started._

---

## 1. Executive summary

1. I scored 15 rows: 12 ideas plus three variants of the user's job board (U4a/b/c). Composites run from **2.20 to 6.70**. This run's top two, **M3 SheetSync (6.70)** and **M1 ChatRelay for Jira (6.65)**, both score above round 1's picks, D2 (6.20) and T2 (5.95). M3's sale-plausibility score of 7 is the first above 6 in any run.
2. **Hard gates reject C2, I3, G3, U4a, U4b and U4c**, all on sales-skeptic P50 > 180 days. U4a also risks the > 3 h/week gate. No idea breaks the upfront-cost or legal gates; the lowest legal scores are 4, for G3 and U4.
3. **Pick 1: M3 SheetSync**, a reliable Apify-to-Google-Sheets integration Actor. It targets the 825 monthly users of an incumbent whose runs fail 51% of the time. Upfront $0, P50/P90 of 20/~120 days, about 0.1 h/week. M3 and M1 are only 0.05 apart, so testability broke the tie (8 vs 4). Two must-fix items come before launch:
   - Replace the shared-service-account design with per-sheet ownership proof or bring-your-own credentials.
   - Drop the "free rows" promo.
4. **Pick 2: M1 ChatRelay for Jira**, a Forge-native replacement for Google's broken Connect app (11,008 installs, 2.3★). It starts with a $0 two-week install-velocity desk test plus a gap audit of the free competitor. Nothing gets built before the Oct 20 verdict. P50 is 105 days; first cash is around day 170–230 because of Atlassian's $500 payout threshold.
5. **Round 1 vs round 2:** M3 beats T2 on every dimension or ties, so it **replaces T2** in the single Apify slot. T2 is shelved and not co-located. M1 beats D2 on every dimension or ties, so it **takes slot #2**. D2 is deferred and is the named fallback if M1's desk test fails on Oct 20.
6. **Apify concentration:** one Apify Actor in production at a time. The fallback order is G1 (only with DataForSEO's written resale OK), then T2.
7. **U4 (user's job board):** do not build it as proposed. If the user wants to pursue it, the only acceptable experiment is a US-only, seeker-paid $9 match report in one niche (§3.1).
8. **Both picks together:** $0–8 upfront, about 4–5.5 h of one-time sponsor setup (slightly over budget; the Atlassian part is reusable for M2), about 0.2–0.35 h/week, and about $110/mo of operator tokens at steady state. Neither pick needs a Lemon Squeezy account.

---

## 2. Scoreboard

`composite = 0.30·Sale + 0.20·Market + 0.20·Autonomy + 0.15·UnitEcon + 0.15·Legal`. Reviewer scores are used exactly as given.

Worked example, M3: 0.30·7 + 0.20·5 + 0.20·9 + 0.15·6 + 0.15·6 = 2.10 + 1.00 + 1.80 + 0.90 + 0.90 = **6.70**.

Column sources:
- Testability: demand-validator.
- Upfront $: unit-economics.
- P50/P90: sales-skeptic, counted from today.
- Human hours: autonomy-auditor.

| # | ID | Idea | Sale | Mkt | Auto | UE | Legal | **Composite** | Testability | Upfront $ | P50 / P90 days | Human hrs setup / per wk | Primary platform / account | Gate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | M3 | SheetSync (Apify → Sheets) | 7 | 5 | 9 | 6 | 6 | **6.70** | 8 | 0 | 20 / ~120 | 0.5–1.25 / ~0.1 | Apify (+ Google Cloud project) | Pass |
| 2 | M1 | ChatRelay for Jira | 5 | 6 | 7 | 9 | 8 | **6.65** | 4 | 0–8 | 105 / never | 3–4 + ~3 wk wait / 0.1–0.25 | Atlassian Marketplace partner | Pass |
| 3 | G1 | Keyword→Brief | 6 | 4 | 8 | 6 | 6 | **6.00** | 7 | 50 | 32 / ~150 | 1.5–2 / 0.1–0.25 | Apify + DataForSEO | Pass |
| 4 | I2 | Episode Study Packs | 4 | 3 | 7 | 7 | 8 | **5.45** | 7 | 12 | 100 / never | 2–2.5 / 0.5–0.75, then 0.25–0.5 | Lemon Squeezy + real mailbox | Pass |
| 5 | M2 | SpecView for Confluence | 4 | 4 | 6 | 8 | 7 | **5.45** | 3 | 0 | 125 / never | 3–4 (0.25 if M1 is done) / 0.25–0.5 | Atlassian (same account as M1) | Pass |
| 6 | C1 | FunderFit | 3 | 5 | 6 | 7 | 8 | **5.35** | 4 | 17 | 130 / never | 3–4 / 1–1.5, then 0.25–0.5 | Lemon Squeezy + affiliates | Pass |
| 7 | G2 | LongForm Transcripts | 4 | 3 | 8 | 5 | 6 | **5.05** | 8 | 5 | 70 / never | 1–1.5 / 0.1–0.25 | Apify + Groq | Pass |
| 8 | I1 | Zì Bot (Discord) | 3 | 4 | 6 | 3 | 6 | **4.25** | 5 | 12 | 140 / never | 3.5–4.5 / 0.5–1, then 0.25 | Discord + Lemon Squeezy | Pass |
| 9 | C3 | Interpreter Practice Lab | 3 | 3 | 5 | 4 | 7 | **4.15** | 3 | 28–74 | 150 / never | 4–6 / 1–1.5, then 0.5 | Lemon Squeezy | Pass |
| 10 | C2 | Client Safety Kit | 2 | 4 | 5 | 6 | 5 | **4.05** | 5 (3 without D2) | 15–27 | >180 / never | 2.5–3.5 / 1–1.5, then 0.5 | Lemon Squeezy (+ depends on D2) | **REJECT** |
| 11 | I3 | Role-Play Room | 2 | 3 | 5 | 4 | 6 | **3.70** | 3 | 12 | ~300 / never | 2.5–3 / 0.5–1 + per institution | Lemon Squeezy | **REJECT** |
| 12 | G3 | AnswerShare GEO API | 2 | 2 | 7 | 2 | 4 | **3.30** | 3 | 10 | >180 / never | 2.5–3.5 / 0.25–0.5 | RapidAPI + MCPize | **REJECT** |
| 13 | U4b | Job board, seeker pays | 2 | 2 | 5–6* | 4 | 4 | **3.20** (3.40 at Auto 6) | 2 | 12 | >180 / never | 2.5–3.5 / 0.5–1 | Lemon Squeezy | **REJECT** |
| 14 | U4c | Job board, niche | 2 | 2 | 3* | n/s | 4 | **~2.5–2.8** (UE imputed at 2–4) | 2 | 12 | >180 / never | 2.5–3.5 / 2–4+ | Lemon Squeezy + employer invoicing | **REJECT** |
| 15 | U4a | Job board, free then employers | 1 | 2 | 3 | 2 | 4 | **2.20** | 2 | 12 | never / never | 2.5–3.5 / 2–4+ | Lemon Squeezy + employer invoicing | **REJECT** |

**Missing or variant scores (U4).**
- The sales-skeptic scored all three variants.
- The unit-economics analyst scored only U4a and U4b, so **U4c has no unit-economics score**.
- The autonomy auditor gave one score (3, or "5–6 if seeker-pays") and the market and legal analysts gave one score each (2 and 4) for U4 as a whole. I applied those to every variant.
- The legal analyst says a US-only, seeker-only, link-out v1 would score about 6. At legal 6 and autonomy 6, U4b would reach 3.70. That is still gated.

**Round-1 reference rows** (not part of this run's ranking): D2 InspectionWatch 6.20 (4/6/7/9/7) and T2 Accela/EnerGov Actor 5.95 (6/5/9/4/5). Round 1 had no testability scores.

**Tie-break applications (the 0.3 rule).**
- M3 vs M1 (gap 0.05): testability 8 vs 4, so **M3 ranks #1**.
- I2 vs M2 vs C1 (5.45/5.45/5.35): testability 7, 3 and 4, so I2 ranks ahead of C1 and C1 ahead of M2 for runner-up purposes.
- G1 is 0.65 below M1, outside the tie band.

---

## 3. Rejected by hard gates

| Gate | Ideas rejected | Reason |
|---|---|---|
| P50 > 180 days | **C2 Client Safety Kit** | P50 > 180, P90 never. Consultants won't put their name and liability on AI-written bilingual safety talks from an unknown vendor. It also depends on D2's ingest, which doesn't exist. **Salvage:** sell only the "OSHA cited your industry this month" brief as a D2 add-on once D2 has 10 or more paying users. |
| P50 > 180 days | **I3 Role-Play Room** | P50 about 300 days. The institutional buying cycle runs through the spring window now, and if that is missed the next window is July–August 2027. The free tool Mizou already covers the use case. Legal 6 also carries FERPA and procurement paperwork that only the sponsor can sign. **Salvage:** sell to private tutors (italki/Preply), or fold it into I1's Server Pro for teacher-run class servers. |
| P50 > 180 days | **G3 AnswerShare GEO API** | P50 > 180. Neither RapidAPI nor MCPize shows buyer traffic, and MentionsAPI already sells the same check at $0.02. It is also the weakest legal score: 4, High. **Legal blocker:** the Gemini API grounding terms forbid caching, reselling or analysing Grounded Results, which is the product's core. Perplexity's output licence is non-sublicensable. Unit economics are 2, because the free tier costs more than realistic revenue. |
| P50 > 180 days (U4a also nears the > 3 h/week gate) | **U4a, U4b, U4c job board** | See §3.1. |
| Upfront > $100 | None | Highest is C3 at $74, including the paid calibration rater. |
| Legal ≤ 3 | None | Lowest are G3 and U4 at 4. |
| > 3 human h/week | None outright | U4a and U4c reach 2–4+ h/week once employer selling and moderation start (autonomy-auditor). |

### 3.1 Recommendation on the user's idea, U4 (AI-matched job board)

**Verdict: no-go as proposed. Park it.** Spend no build tokens on it this month.

- **The incumbent already gives away the core feature.** HiringCafe has 2M MAU and 5.7M listings pulled from company ATS feeds. On **2026-09-28** it launched a **free** AI agent that parses resumes, matches roles and monitors continuously (market-analyst, verified). Jobright and Teal charge $29–40/mo with known brands.
- **"Free first, employers later" (U4a) can't be tested and burns cash.** Unit economics model it at **−$2,065 cumulative by March**, and the more free users it attracts, the faster it burns. Employers won't pay to reach zero seekers, and the model cannibalises itself: why pay to post a job you already aggregate for free from their ATS?
- **Seeker-pays (U4b) is the only variant with any sub-90-day chance**, and that chance is 20%. "Pay to see jobs" from an anonymous site matches the FTC's job-scam pattern.
- **Legal:**
  - Resumes are sensitive personal data.
  - Any employer-side ranking brings NYC LL144, Colorado's AI law (1 Jan 2027) and EU AI Act high-risk rules (now Dec 2027).
  - FCRA and Title VII "employment agency" exposure follow if ranked candidates are sold to employers.
- **If the user still wants to try it**, run only the demand-validator's test: a **$9 one-time "30 best-matched roles" report**.
  - Scope: US-only, in one niche where the sponsor is a genuine community member.
  - Data: public Greenhouse/Lever/Ashby boards only, link-out snippets, no full descriptions.
  - Privacy: resume PDFs deleted within 7 days; no employer product.
  - Traffic: one Show HN post plus one niche-community post by the sponsor.
  - Threshold: **pass at ≥ 10 paid from ≥ 400 visitors by Oct 29.**
  - Cost: about $17 and 1.5–2 h.
  - Treat it as an experiment outside the token budget, not a pick.
- **The only long-run shape with a channel is U4c plus a named partner** who already owns a niche audience (a newsletter or association) and shares employer-post revenue. Even then, $300/mo is 6–12 months out.

---

## 4. Top picks

### 4.1 Round 2 vs round 1, and how to handle Apify

| Dimension | T2 (r1 #2) | **M3** | D2 (r1 #1) | **M1** |
|---|---|---|---|---|
| Sale / Mkt / Auto / UE / Legal | 6 / 5 / 9 / 4 / 5 | **7 / 5 / 9 / 6 / 6** (legal 8 once auth is fixed) | 4 / 6 / 7 / 9 / 7 | **5 / 6 / 7 / 9 / 8** |
| Composite | 5.95 | **6.70** | 6.20 | **6.65** |
| P50 / P90 | 50 / 200 | **20 / ~120** | 130 / never | **105 / never** |
| Demand evidence | Closest peer Actor has 6 MAU | Incumbent has **825 MAU**, 51% failed runs (verified by 3 reviewers) | No paid feed for consultants found | **11,008 installs** on a 2.3★ broken app; Forge alternatives about 690 |
| Channel | Apify Store | Apify Store + Console integration picker | Sponsor's personal emails + editors | Atlassian Marketplace + in-Jira search, with Atlassian billing and tax |
| Sponsor h/week | 0.1–0.25 | ~0.1 | 0.5–0.75 | 0.1–0.25 |
| Cash timing | Apify monthly, $20 minimum | Same | Lemon Squeezy, fast | **Slow: $500 threshold, about day 170–230** |

**Ruling: yes, round 2 beats round 1.**
- **M3 dominates T2.** It scores higher or equal on all five dimensions, has a faster P50 and better P90, and has two orders of magnitude more verified demand.
- **M1 dominates D2** on every dimension or ties. It uses a marketplace with built-in discovery and billing, which is lesson 1's winning pattern, instead of the sponsor's email time. Its one inferior feature is cash timing.
- **Caveat:** the scores come from different reviewer passes, and round 1 had no testability scores. The substantive evidence (channel, verified demand, legal profile) points the same way as the scores, so the conclusion does not rest on calibration.

**How to handle Apify concentration:**
1. **One Apify Actor in production at a time, on one account. M3 takes the slot, and T2 is shelved (not built).** Running T2 next to M3 would be worse than ordinary concentration. T2's main legal risk is county-portal terms, cease-and-desist letters and Apify takedown (legal 5). Under Apify's Store Publishing Terms, Apify can unpublish without notice, **withhold all outstanding payouts** and impose a penalty up to the unpaid balance. A T2 incident would therefore put M3's earnings at risk. Separate Apify accounts don't fix this: KYC ties both to the same sponsor identity, and multi-account rules are unverified.
2. **Order of fallback for the Apify slot:**
   - If M3 fails its Oct 26 verdict, the slot goes to **G1**, provided DataForSEO's written resale permission has arrived. The operator may send that permission request today at $0. Launch G1 with the demand-validator's version: `serp-brief-lite` included, and free-plan runs capped.
   - **T2** comes only after G1.
   - I reject the demand-validator's optional two-Actor "bake-off". It doubles exposure for little information gain, because M3's test reads in 20 days anyway.
3. **No other Apify idea (G1, G2) runs while M3 is live.** G2 is out regardless: it is undifferentiated against steadyfetch at $0.006/min (market 3).

**D2's status:** deferred, not killed. It is the **fallback for slot #2** if M1's desk test is a no-go on Oct 20. Under the new rules, D2's round-1 plan must first be restarted with a demand test: a founding-price paid trial from 40 personal emails, passing at **≥ 3 paid by day 45**.

### 4.2 Resolving reviewer conflicts

| Idea | Disagreement | Committee ruling |
|---|---|---|
| **M3** | Skeptic **7** / autonomy **9** vs market **5** / legal **6** / unit economics **6** | **Each reviewer is right about something, and every objection can be tested for $0 within 20 days.** The market analyst's strongest point is that two "reliable" Sheets clones already exist and have 1–2 users, so Store search alone won't deliver switchers. The mitigation is placement in the Console integration picker plus README templates, and the operator verifies that the picker surfaces integration-ready Actors **before** building. The skeptic's point (51% of runs failing ≠ 51% of users; failures may be user-side auth) becomes a mandatory pre-build audit of the incumbent's issues. The legal 6 and the unit-economics 6 are both **self-inflicted design bugs** (the shared-service-account confused deputy and the free-rows promo). Both are fixed before launch, so the composite understates the fixed product. |
| **M1** | Market **6** / unit economics **9** / legal **8** vs skeptic **5** (P90 never) | **The skeptic is right about the competitor and the market analyst about the trigger.** Move Work Forward's free 5.0★ app was updated 2026-10-02, and it is the decisive threat. The market analyst found that Connect apps do *not* stop working on Jan 31; Atlassian says customers "won't lose access". Urgency therefore comes from the app being **already broken** (recent 1★ reviews), not from a cliff. That cuts both ways: less of a January spike, but demand that doesn't vanish on Feb 1. **Ruling:** both $0 checks gate the build. The skeptic's gap audit (install the free app and list gaps a >10-user site would pay for) and the validator's install-velocity test must pass before any building. |
| **G1** | Skeptic **6** vs market **4** | **The market analyst wins.** Eight or more keyword Actors priced at or below $0.004 have 0–10 users each, so price is a proven non-wedge. The "brief" shelf's best Actor has 1 user. The skeptic's 6 rests on shelf dynamics that favour incumbents with history. G1 is the Apify fallback, not a pick. |
| **I2** | Unit economics **7** / legal **8** vs market **3** / skeptic **4** | **The market analyst wins on the ceiling.** There are 100–200 creators, and every example already makes its PDFs in-house. I2 is still cheap to test (testability 7), so it is runner-up #2. |
| **C1** | Unit economics **7** / legal **8** / market **5** vs skeptic **3** | **The skeptic wins.** The gating event is a stranger saying yes, and several named partners earn Instrumentl affiliate income or teach prospect research themselves. The skeptic's realistic 5–10% yes-rate from 12 pitches gives 0–1 partners. |
| **C1–C3** generally | Ideators' 10–25% partner agreement vs skeptic's 5–10% and autonomy's hidden 1–1.5 h/week | **The skeptic and the auditor win.** Partner channels are not marketplaces: there is no built-in discovery or billing, and every yes costs human time. All three have P50 ≥ 130 days. |
| **I1** | Ideator's Lemon Squeezy pre-order vs legal | **Legal wins.** Discord's payment-parity rule makes off-Discord selling of in-bot features a delisting risk on the idea's only channel. |
| **M3 auth** | Autonomy (the shared service account means no OAuth, so less friction) vs legal (confused deputy) | **Legal wins. This must be fixed before launch** (§4.3). |

### 4.3 Must-fix legal blockers (before launch)

| Idea | Blocker | Required fix |
|---|---|---|
| **M3** (pick) | **The shared Google service account is a confused deputy.** Every customer shares their sheet with the same identity, so any Apify user who enters another customer's sheet URL can append to it or *replace* it. The sponsor is liable as provider, and Apify may pull the Actor. | Fix all of the following before launch:<br>- **Ownership proof per sheet before any write**: a one-time token, bound to the user's Apify user ID, placed in a named range. Or bring-your-own service-account credentials (recommended for teams and heavy volume, which also avoids the shared 60 req/min quota).<br>- **No "replace" mode on the shared identity without proof.**<br>- No row data in logs.<br>- GDPR processor terms in the Actor's end-user terms.<br>- Comparative claims stated factually ("51% failed runs, Apify public stats, 2026-10-06"), with no disparagement of the Apify-staff incumbent. |
| **M1** (pick) | A false "Runs on Atlassian" or "data stays in Atlassian" claim | Claim the badge only after Atlassian confirms eligibility with the declared Google Chat egress. Use "Google Chat" nominatively, with no Google logos. The privacy policy must disclose email matching for @mentions and the egress to Google. Offer a mentions-off mode. Store webhook URLs encrypted and never log them. |
| G3 (gated) | **Gemini grounding terms** ban caching, reselling and analysing Grounded Results. Perplexity's output licence is non-sublicensable. | Drop Gemini. Get Perplexity's written OK, or return only derived metrics. Keep "ChatGPT" out of all names. Check tax handling, because MCPize is probably not a merchant of record. |
| G1 (fallback) | DataForSEO's ToS is silent on resale, and §7.2 makes us indemnify DataForSEO | Get written resale permission before building. Gate free-plan users before calling DataForSEO. Truncate any AI Overview text. |
| G2 | The claim "audio is deleted when the run ends" is false, because the speech-to-text providers keep inputs | Correct the claim. No live capture and no diarization (In re Otter.AI). Register a DMCA agent. Sign DPAs with the providers. |
| I1 | Discord payment parity | Don't sell in-bot features through Lemon Squeezy before Premium Apps. Sell the paid tier as a separate web product instead. Comply with CC-CEDICT's share-alike licence. |
| C1 | ProPublica's API is CC BY-NC-ND | Use only IRS bulk XML. Exclude grants to individuals. Partners must make FTC affiliate disclosures. |
| C2 (gated) | Injury and negligence exposure from mistranslated safety talks | Native-speaker review of every talk. Never call the content "OSHA-compliant" or "training". Form an LLC. |
| I3 (gated) | The "18+ only" claim is false for dual-enrolment students; FERPA | Drop the claim. Publish FERPA school-official terms. Build to WCAG 2.1 AA. |
| C3 | Exam-content and trademark exposure | Never solicit exam content. Use marks nominatively only. Make no pass-rate claims. |
| U4 | Resume data; employer-side ranking | US-only, seeker-only, link-out. Delete PDFs. No employer ranking without counsel. |

---

### Pick 1: M3 SheetSync, a reliable Apify → Google Sheets integration Actor

**Thesis.** 825 Apify users a month pipe scheduled scraper output into Google Sheets through a free Actor whose runs fail 51% of the time, and whose maintainer typically takes 22 days to respond. A reliable, integration-ready replacement with upsert, de-duplication and tab rollover sells inside the Apify Console at the moment the export fails. Apify supplies discovery and billing, and the sponsor does almost nothing.

**Key numbers**

| Metric | Value | Source |
|---|---|---|
| Upfront $ | **$0** | unit-economics |
| P50 / P90 to first sale | **20 / ~120 days**. P(≤30d) 0.55, P(≤90d) 0.85. | sales-skeptic |
| First cash | Earliest Dec 21–25 (about day 77) if November reaches the $20 minimum; P50 Jan 21–25 (about day 108) | sales-skeptic |
| Sales/month for $300 | **About 45 paying users** at $6.73 net, or **about 60** at a realistic $5. At the validator's test price ($0.005 per run + $0.30 per 1k rows, about 100 runs of 200 rows), net is about $5.1/user, so plan on about 60. | unit-economics, re-priced by committee |
| Human hours | **Setup 1–1.5 h**: Apify account, KYC and payout; Google Cloud project and service account; Sheets quota-increase request. **Weekly about 0.1 h.** | autonomy-auditor |
| Legal | **6/10, Medium as briefed; 8 once the auth fix ships**, which is mandatory | legal-risk |
| Tokens | $100 build, then about $50/mo (the lightest in the round) | unit-economics |
| Break-even | Accrued month 2–3; cumulative about month 3; $300 net about month 9–12 | unit-economics |
| Timing | Not seasonal; no deduction | sales-skeptic |
| Founder fit | Good. A pure developer-integration product that suits a builder of multi-agent Claude Code pipelines. No domain dogfooding needed. | committee note |

**Launch configuration (pivots adopted)**
- **Pricing for the test:** PPE at $0.005 per run start plus $0.30 per 1,000 rows. **No free rows.** The brief's "first 1,000 rows of each run free" made a typical 200-row run nearly free, at about $0.40 net per user per month.
- **Auth:** the shared service account with mandatory per-sheet ownership token, plus a bring-your-own service-account option. Replace mode is never allowed on the shared identity without proof.
- **Distribution:** integration-ready Actor, the Console picker, an exact-match title ("Google Sheets export / import"), a field-by-field switching guide from the incumbent, and README templates for the top scrapers.

**30-day launch plan. It starts with the demand test (demand-validator, testability 8).**
- The demand test is a **live paid listing with no free rows**.
- **Pass (Oct 26, day 20):** ≥ 25 distinct users, ≥ 5 paid-plan users charged, and ≥ 95% run success.
- **Pivot:** 2–4 paid-plan users.
- **Fail:** ≤ 1 paid-plan user, or < 90% success.
- Only strangers count; operator-linked Apify IDs are excluded.
- The test build is the minimum reliable Actor. Phase-2 work (top-10 templates, status tab, docs site) starts only after a pass.

*Week 1, day by day*

| Day | AI operator | Human sponsor |
|---|---|---|
| D0 Tue Oct 6 | **Gate 0, the incumbent-failure audit (about 1 h):** read `lukaskrivka/google-sheets` issues and classify failures as Actor-side (fixable by us) or user-side (auth or permissions we would also hit). Verify that integration-ready Actors appear in the Console integration picker. Write `runs/2026-10-06-round2/tests/M3.md` with the pre-committed thresholds. **Stop if the failures are mainly user-side.** Optionally email DataForSEO for G1's resale permission, to keep the fallback warm. | — |
| D1 Wed Oct 7 | Scaffold the Node Actor and the Sheets client with batched `values.append`, exponential backoff and quota pacing. | Create the Apify account and complete KYC and payout (PayPal/Wise). Create the Google Cloud project, enable the Sheets API and create the service account. (≈1–1.25 h) |
| D2 Thu Oct 8 | Build append, replace and upsert-by-key modes, a per-run idempotency key, automatic tab rollover before 10M cells, and the **ownership-token check** plus the bring-your-own-credentials path. | Submit the Sheets quota-increase request; the operator drafts it. (≈0.15 h) |
| D3 Fri Oct 9 | Load tests at 1k, 100k and 2M rows, plus quota-exhaustion tests. Handle the integration-ready payload (`defaultDatasetId`). Set up a daily canary sheet. **Security test:** a write to an unproven sheet must be refused. | — |
| D4 Sat Oct 10 | README: switching guide, factual comparison, data-handling note, GDPR processor terms, AUP, PPE pricing, and the input schema. | — |
| D5 Sun Oct 11 | End-to-end runs attached to 3 popular Store scrapers (e.g. Google Maps). Fix any edge cases. | — |
| D6 Mon Oct 12 | **Publish.** Start the daily metrics log: users, paid-plan users, runs, success rate, events billed. | Accept the publishing and monetisation terms if prompted. (≈0.1 h) |
| D7 Tue Oct 13 | Monitor, answer issue threads, hot-fix failures. | — |

*Weeks 2–4*

| Week | AI operator | Human sponsor |
|---|---|---|
| Wk 2 (Oct 14–20) | Keep the success rate at or above 95%. Answer issues within 24 h. Add 3 README templates for top scrapers. Track the incumbent's user count and success rate weekly. | Optional: one disclosed post in the Apify Discord showcase. (≈0.1 h) |
| Wk 3 (Oct 21–27) | **Oct 26 verdict, against the pre-committed thresholds.** Pass: start phase 2 (templates for the top 10 scrapers, status tab, GitHub Pages docs page). Pivot: change price or positioning and test for 7 more days. Fail: freeze or unpublish and hand the Apify slot to G1. | Read the verdict. (≈0.1 h) |
| Wk 4 (Oct 28–Nov 4) | Phase 2 if passed. **Day-30 report:** paid-plan users, $ billed, token spend against the $100 build cap and $50/mo run cap. | Read the day-30 report. (≈0.1 h) |

**Kill criteria**
- **Day 0:** the audit shows the incumbent's failures are mostly user-side. Don't build.
- **Day 20 (Oct 26):** ≤ 1 paid-plan user, or < 90% run success. Freeze, and give the Apify slot to G1.
- **Day 45 (Nov 20):** fewer than 15 paid-plan users, or less than $40 billed in the trailing 30 days. Freeze.
- **Day 90 (Jan 4):** net run-rate below $50/month, so it doesn't cover its own tokens. Kill and unpublish.
- **At any time:**
  - Any cross-customer write incident: pause immediately.
  - Any Apify policy notice: pause.
  - The incumbent drops below 10% failures **and** our paid users are flat for 2 weeks: freeze.
  - Apify ships a native Sheets append integration: freeze.

**Top 3 risks and mitigations**
1. **The incumbent is fixed, or Apify ships a native integration.** It is maintained by Apify staff. *Mitigation:* differentiate beyond reliability (upsert by key, de-duplication, tab rollover, status tab, templates). Keep token spend capped and use the freeze rule. Never disparage the incumbent.
2. **Discovery.** "Reliable" clones already sit at 1–2 users. *Mitigation:* placement in the integration picker (verified on D0), an exact-match title, the switching guide and scraper templates. The Oct 26 test measures this directly.
3. **Security and quota.** There is the confused deputy, and a shared service account is limited to 60 requests/min across all customers, which could recreate the incumbent's failure mode. *Mitigation:* the ownership token, bring-your-own credentials for heavy users, batching, the quota increase, and no spreading of load across projects.

---

### Pick 2: M1 ChatRelay for Jira, Forge-native Google Chat notifications

**Thesis.** About 11,000 Jira Cloud sites installed Google's own Google Chat app. It is broken (2.3★, recent 1★ reviews, last release 2021), and only about 6% of that base has moved to Forge alternatives. A Forge-native app sits in the one search box those admins use, with per-JQL routing, one thread per issue and a 5-minute migration guide. It is billed on the Atlassian invoice with 0% revenue share, so 15 paying sites fund the operator.

**Key numbers**

| Metric | Value | Source |
|---|---|---|
| Upfront $ | **$0–8** (a Google Workspace test month only if the sponsor has no Workspace) | unit-economics |
| P50 / P90 to first sale | **105 / never**. P(≤30d) 0.03, P(≤90d) 0.40. | sales-skeptic |
| First cash | **About day 170** (late March, unit-economics) to **about day 230** (skeptic), because nothing is paid out until $500 cumulative. The sponsor fronts about $470 of tokens until then. | unit-economics, sales-skeptic |
| Sales/month for $300 | **15 paying sites** at about $20 (18 to also cover tokens). 8 sites cover tokens only. | unit-economics |
| Human hours | **Setup 3–4 h plus about 3 weeks of partner-verification wait**: Atlassian ID, the ECOHELP identity form, W-9/W-8BEN, bank details, Partner Agreement, security questionnaire, Workspace test space. **Weekly 0.1–0.25 h.** | autonomy-auditor |
| Legal | **8/10, Low** | legal-risk |
| Tokens | About $30 for the desk test, $150 build plus $80 listing and review, then about $60/mo | unit-economics |
| Timing | The deadline is a soft tailwind; December change freezes are a mild drag; no deduction. The listing must be live by about Nov 20 to catch pre-deadline clean-ups. | sales-skeptic, market-analyst |
| Founder fit | Neutral to good: developer tooling the operator can build and maintain alone | committee note |

**30-day launch plan. It starts with the demand test (demand-validator Step 0, plus the skeptic's gap audit).**
- **Step 0 (Oct 6–20, $0):** daily snapshots of installs for the 5 Forge Google-Chat alternatives.
  - **Go** if they gain ≥ 25 installs combined in 14 days.
  - **Grey zone (10–24):** go only if the gap audit finds ≥ 2 gaps a >10-user site would pay for.
  - **No-go** if they gain < 10. Slot #2 then goes to D2.
- **Later gates** (beyond day 30):
  - **Listing gate, 21 days after going live (~Dec 10):** ≥ 20 installs, including ≥ 6 evaluations on sites with more than 10 users.
  - **Pay gate (Jan 15):** ≥ 3 paid conversions.
- **No Forge code is written before the Oct 20 go.**

*Week 1, day by day*

| Day | AI operator | Human sponsor |
|---|---|---|
| D0 Tue Oct 6 | Start daily Marketplace API snapshots of installs for all 5 Forge alternatives and for Google's orphan. Write `tests/M1.md` with the pre-committed thresholds. | — |
| D1 Wed Oct 7 | Mine the orphan's and the alternatives' reviews and the Atlassian Community threads for unmet needs. Draft the gap hypothesis list (JQL routing, threading, JSM SLA events, digest, migration). | Create an Atlassian ID, the developer console and a free Jira Cloud developer site. (≈0.5 h) |
| D2 Thu Oct 8 | **Gap audit:** install Move Work Forward's free app (and Canary's trial) on the dev site and test each gap hypothesis against a real Chat space. | Provide a Google Workspace test space (existing, or a trial). (≈0.5 h) |
| D3 Fri Oct 9 | Write up the gap audit: which gaps exist, and whether a >10-user site would pay. Ask Atlassian developer support in writing whether declared Google Chat webhook egress keeps "Runs on Atlassian" eligibility. | — |
| D4–D6 Oct 10–12 | Continue snapshots. Draft the listing copy, privacy policy and migration-guide outline. Docs only, no code. | — |
| D7 Tue Oct 13 | **7-day interim read.** If the alternatives gained ≥ 8 installs combined (on pace) **or** the gap audit found clear payable gaps, recommend starting partner verification now to save about a week on the 3-week wait. | **If the interim read is positive:** submit the ECOHELP identity form, W-9/W-8BEN and bank details, and accept the Partner Agreement. This is about 1–1.5 h at risk, accepted by the committee because of the deadline; it is reusable for M2. |

*Weeks 2–4*

| Week | AI operator | Human sponsor |
|---|---|---|
| Wk 2 (Oct 14–20) | Continue snapshots. **Oct 20 verdict.** Go: start the build. No-go: stop, and activate D2 as slot #2. | Read the verdict. If it is a go and verification wasn't submitted on D7, submit it now. (≈0.1–1.5 h) |
| Wk 3 (Oct 21–27) | **Build:** Forge event triggers, admin UI (project and JQL → space), `threadKey` = issue key, card messages, quiet hours and digest, the "Send to Google Chat" automation action, and @-mention mapping with a mentions-off mode. Test on the dev site. | — |
| Wk 4 (Oct 28–Nov 4) | Listing (exact-match "Google Chat"), the 5-minute migration guide, troubleshooting pages on GitHub Pages titled with the orphan's error strings, and the security self-assessment. **Submit for approval** as soon as verification clears (expected about Nov 2–4). The approval queue is 10–15 business days, so the listing goes live about Nov 16–24. | Attest the security questionnaire and answer reviewer questions. (≈0.5 h) |

**Kill criteria**
- **Oct 20 (day 14):** < 10 combined installs on the alternatives, **or** 10–24 with no payable gap. No-go; slot #2 goes to D2.
- **Nov 20 (day 45):** partner verification still not complete, or the listing not submitted. Stop, because the pre-deadline window is lost.
- **Dec 1:** listing not live. Leave it as maintenance-only and give no further feature tokens.
- **21 days after going live:** < 20 installs, or < 6 evaluations on >10-user sites. Maintenance-only.
- **Jan 15:** 0 paid conversions. Kill (maintenance-only or unpublish). 1–2 conversions: pivot on pricing, or add M2's read-only scan to the same account.
- **Mar 31:** fewer than 8 paying sites, so it doesn't cover tokens. Maintenance-only.
- **At any time:** Google ships a Forge rewrite, or Atlassian adds a native Google Chat automation action. Stop feature work.

**Top 3 risks and mitigations**
1. **The free Move Work Forward app absorbs the switchers.** *Mitigation:* the gap audit before building. Keep sites with 10 or fewer users free. Win >10-user sites on JQL routing, threading, JSM SLA events and the migration guide. Make the first 20 reviews the asset.
2. **Slow cash.** The $500 threshold means first cash around day 170–230. *Mitigation:* cap tokens at $60/mo after the build. M3's earlier Apify cash offsets the gap. If M1 passes, add M2 later on the same account, which pools toward the threshold.
3. **Onboarding and approval delays, or an Atlassian/Google native fix.** Verification takes about 3 weeks and approval 10–15 business days. *Mitigation:* start verification on the D7 interim signal, and use the dated stop rules (Nov 20, Dec 1) so the idea doesn't drift past the window.

**Both picks together**
- **Upfront:** $0–8.
- **Sponsor setup:** about 4–5.5 h (M3 1–1.5 h, M1 3–4 h). That is slightly over the 2–4 h budget, but it is spread over 3 weeks, and about 1.5 h of the M1 part is reusable for M2.
- **Weekly:** about 0.2–0.35 h, well under the 1 h ideal.
- **Tokens:** about $130 in October (M3 build plus M1 desk test), about $280 in November (M1 build plus M3 run), then about $110/mo. That is cheaper than round 1's D2+T2 plan ($300 build plus $160/mo).
- **No shared seller account:** Apify and Atlassian. No Lemon Squeezy KYC is needed.

### 4.4 Combinations and pivots considered
- **M1 + M2 on one Atlassian account (adopted as phase 2).** M2's best element is the **read-only migration scan**. It becomes M1's second listing only after M1 passes its listing gate. Pooling counts toward the $500 payout threshold, so cash arrives earlier. This doesn't violate the concentration rule because it is one pick's account.
- **Rejected G1's best idea (agent-native schemas) is folded into M3.** M3 gets flat, documented output and natural-language input descriptions so the Apify MCP server can surface it to agents.
- **C2's best element** (the NAICS-and-state citation brief) belongs to D2 as an add-on if D2 is ever activated, as round 1 also concluded.
- **I3's best element** (level-locked, assignable role-play) moves to I1's Server Pro for teacher-run class servers, or to private tutors.
- **U4c's only viable shape** borrows the C-series channel: a niche partner who owns the audience and shares employer-post revenue.
- **Pivots adopted explicitly:**
  - M3: no free rows, plus ownership-token or bring-your-own auth.
  - M1: build gated on the gap audit and install velocity.
  - G1, if activated: launch with `serp-brief-lite` and free-plan caps, not the $0.004 metrics-only listing.

---

## 5. Runners-up

| Rank | Idea | What would need to be true for it to win |
|---|---|---|
| 1 | **G1 Keyword→Brief** (6.00, testability 7) | DataForSEO grants written resale permission. **And** M3 fails its Oct 26 verdict, which frees the single Apify slot. **And** the `serp-brief-lite` event sells to at least 3 paid-plan users in 14 days, proving a non-price wedge on a shelf where clones at $0.004 or less get 0–10 users. |
| 2 | **I2 Episode Study Packs** (5.45, testability 7) | At least 3 paying creators from 40 one-to-one emails by Nov 9. The list is widened to Spanish, Japanese and Korean learning podcasters (skeptic's fix) to escape the ceiling of 100–200 creators. Outreach goes through a real mailbox, not a transactional ESP. It has the strongest founder fit in the run (Mandarin learner who dogfoods it) and doesn't share an account with either pick. It is the right personal-interest project if the sponsor wants one, but it is not in the default token budget. |
| 3 | **M2 SpecView for Confluence** (5.45, testability 3) | Only as M1's phase 2. It needs M1's listing gate to pass, Forge Swagger alternatives to gain at least 20 installs in a $0 14-day velocity check, and the read-only scan to find orphan macros on at least 5 sites before any page writer is built. |

**Round-1 picks, for the record:**
- **D2** is deferred and is the slot #2 fallback (activated on an M1 no-go on Oct 20, restarted with a paid demand test).
- **T2** is shelved. M3 holds the Apify slot, and T2 is third in the Apify fallback order after M3 and G1.

---

## 6. Observations about the idea set

**Patterns**
- **The lessons worked, partially.** Every idea now has a demand test and a named channel. The best composite rose from 6.20 to 6.70. The first sale score above 6 (M3, 7) came from the persona told to read marketplaces for **stranded paying users**, not for "few listings". The marketplace-native persona produced the top two ideas and the M-series had the smallest gaps between ideator and skeptic estimates. For example, M3 was 14 vs 20 days and M1 was 70 vs 105.
- **Partner-first channels underperformed.** All three C-ideas have P50 ≥ 130 days, and C2 is gated. The gating event is a stranger's yes, with a realistic hit rate of 5–10% and hidden sponsor time of 1–1.5 h/week. **A partner is not a marketplace:** there is no built-in discovery or billing.
- **First sale ≠ first cash is the new blind spot.** Atlassian's $500 threshold, Apify's $20 minimum with rollover, and RapidAPI's month+2 payouts were missed or under-weighted by ideators. M1's sale-to-cash gap is about 2–4 months.
- **Launch promos and price anchors broke the economics:**
  - M3's per-run free rows;
  - C2's "founding price for life";
  - C3's flat school licence with no usage cap;
  - G1/G2's supplier costs on free-plan users (Apify pays nothing for free-plan usage, but DataForSEO and Groq still bill us).
- **AI-built clone floods are now the default.** "Cheaper" clones (G1, G2) and "reliable" clones (M3's precedent) both sit at 0–2 users. The winners have ranking history or placement in the workflow (the integration picker, in-Jira search). Ideas need a placement advantage, not only a product advantage.
- **Ideators missed supplier and platform terms:**
  - DataForSEO resale (G1);
  - Gemini grounding (G3);
  - ProPublica's NC licence (C1);
  - Discord payment parity (I1);
  - transactional ESPs banning cold outreach (I2, I3, U4);
  - a false privacy claim (G2);
  - a multi-tenant security hole (M3).

  Legal and autonomy reviewers caught all of them. They should become ideator checklist items.

**Platform concentration (rubric flag)**
- **Lemon Squeezy is the merchant of record for 6 of 13 briefs** (C1–C3, I1–I3), and **7 of 13 (54%) counting U4**. That is over the "more than half" flag. Its pending move to Stripe Managed Payments, which has no affiliate tool, directly threatens the C-series' 40% partner mechanics. Neither pick uses Lemon Squeezy.
- **Apify:** 3 of 13 (G1, G2, M3), plus round 1's T2. This is handled by the one-Actor rule in §4.1.
- **Atlassian:** 2 of 13 (M1, M2), handled as one pick plus a phase 2.
- **Market correlation:** all of I1–I3 sell into Mandarin learning. The Insider flagged this honestly; the three share demand risk.

**Blind spots in the ideators**
- **Seasonality was mostly handled.** Remaining misses: I3 (finals and the spring window), C1 (dead late December) and U4 (Q4 hiring slowdown).
- **Free incumbents launched days ago were not found.** Examples: HiringCafe's free AI agent (Sept 28) and Move Work Forward's app update (Oct 2). Ideators should check the incumbent's last-modified date and changelog as a standard step.
- **No idea combined founder fit with a marketplace channel.** The Insider's Mandarin ideas use Discord, cold email and institutions, never a billing marketplace. A Mandarin-learning product on a marketplace with built-in billing would be worth one ideator slot next round, for example a paid Anki/AnkiWeb-adjacent or Gumroad Discover HSK 3.0 pack, the pending U3-W wedge.
- **Suggested additions to `lessons-learned.md`:**
  - Model first *cash* as well as first sale, including payout thresholds.
  - Never give away the unit you charge for in a launch promo.
  - Multi-tenant designs need per-customer authorization.
  - Partner yes-rates for an unknown vendor are 5–10%.
  - Check supplier ToS for resale before building.
  - One production listing per marketplace account across all runs.

---

## 7. Sponsor decision (2026-10-06)

The sponsor chose to **focus on M3 SheetSync only**.

- **M1 ChatRelay is dropped.** Atlassian partner verification and app review make it hard to test cheaply, and cash wouldn't arrive until around March–May 2027. No Atlassian account will be created.
- **Slot #2 is left empty** for now. D2 and G1 remain documented fallbacks but are not active.
- **Next step:** M3's day-0 gate, an incumbent-failure audit plus a check of placement in Apify's integration picker. Its findings go in `tests/M3.md`, and building starts only if the audit passes.

## 8. Outcome of M3 day-0 gate (2026-10-06)

The audit is in `tests/M3.md`. Its verdict was **pivot (placement first)**, and the sponsor concluded **no-go**.

- **The failure audit passed.** About 55% of the incumbent's failures are fixable bugs in the Actor itself.
- **Placement failed.**
  - About 21 Actors making the same pitch launched in Jul–Sep 2026, and together they have about 25 users.
  - The incumbent is maintained by Apify.
  - The only placement that would give an edge ("Generic integrations" or "Suggested for this Actor") is granted at Apify's discretion.

**No active picks remain from round 2.**
