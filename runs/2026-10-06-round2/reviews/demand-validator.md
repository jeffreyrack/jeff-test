# Demand Validator — Round 2 (2026-10-06)

_Reviewer: demand-validator. Inputs: `operator-constraints.md`, `scoring-rubric.md`, `lessons-learned.md`, and the 13 round-2 briefs (G1–G3, C1–C3, I1–I3, M1–M3, U4). Day 0 is Tue 2026-10-06, and every "days to answer" figure counts from today. Testability is the first tie-breaker. It is not part of the composite._

## Summary

| ID | Idea | Testability | Test type | Pass threshold | Days to answer | Cost $ / human hrs |
|---|---|---|---|---|---|---|
| G1 | Keyword→Brief (Apify) | **7** | Live paid listing, Apify PPE (gated on DataForSEO resale OK) | ≥10 paid-plan users, ≥$15 billed, ≥3 paid users of the brief event, by Oct 25 | 19 | $50 float (~$5 consumed) / 1–1.5 h |
| G2 | LongForm Transcripts (Apify) | **8** | Live paid listing, Apify PPE | ≥8 paid-plan users, ≥2,000 paid minutes, ≥1 scheduled/RSS user, by Oct 24 | 18 | ~$7 / 0.5–1.25 h |
| G3 | AnswerShare API | **3** | $0 desk kill-check, then a paid listing on RapidAPI only | ≥3 paying accounts or ≥$30 paid usage by Nov 10 | 35 | ~$15 / 1–1.5 h |
| C1 | FunderFit | **4** | Partner commitment, then a $19 founding report sold through the partner's mention | ≥2 dated partner mentions by Nov 6; ≥5 paid reports from strangers within 14 days of the first mention (by Dec 4) | 31 (partners) / 45–59 (pay) | ~$17 / 2.5 h |
| C2 | Client Safety Kit | **5** if D2 is live (3 if not) | Paid subscription charged now ($29/mo founding), sold through partners plus D2's own outreach | ≥4 paying consultants by Nov 20 | 45 | ~$35 / 1.5–2 h |
| C3 | Interpreter Practice Lab | **3** | Partner commitment + scoring-calibration gate, then a $19 30-day pass | ≥2 partners by Nov 13; calibration ≥80%; ≥8 paid passes (or 1 school at $150) by Dec 18 | 38 (partners) / ~73 (pay) | ~$75 / 2.5–3 h |
| I1 | Zì Bot (Discord) | **5** | Real paid tier inside a free bot (no pre-order) | Distribution: ≥250 WAU or ≥8 servers. **And** ≥8 paid supporters from strangers, by Nov 20 | 45 | ~$17 / 2 h |
| I2 | Episode Study Packs | **7** | Concierge free sample, then a paid founding month ($29) | ≥3 paying creators by Nov 9 | 34 | ~$17 / 1 h |
| I3 | Role-Play Room | **3** | Paid founding class licence ($99, charged now, auto-refund) | ≥4 paid classes by Dec 15 | 70 | ~$17 / 1.5 h |
| M1 | ChatRelay for Jira | **4** | $0 competitor-velocity desk test, then a live paid Atlassian listing | Desk: Forge alternatives gain ≥25 installs in 14 days. Listing: ≥20 installs incl. ≥6 evals on >10-user sites within 21 days. Pay: ≥3 paid conversions by Jan 15 | 14 / ~45 / ~100 | $0–8 / 2–2.5 h |
| M2 | SpecView for Confluence | **3** | $0 desk test, then a listing with a **read-only** migration scan | ≥15 installs and ≥5 sites running the scan that find orphan macros, within 21 days; ≥2 paid by Jan 31 | ~45 / ~115 | $0 / 0–2 h |
| M3 | SheetSync (Apify) | **8** | Live paid listing, Apify PPE, **no free rows** | ≥25 users, ≥5 paid-plan users charged, ≥95% run success, by Oct 26 | 20 | $0 / 0.25–1 h |
| U4 | AI-matched job board | **2** | $9 one-time match report (the seeker pays). The employer side can't be tested now. | ≥10 paid from ≥400 unique visitors by Oct 29 | 23 | ~$17 / 1.5–2 h |

**Ranking by testability:** G2 = M3 (8) > G1 = I2 (7) > C2 (5 if D2 is live) = I1 (5) > C1 = M1 (4) > G3 = C3 = I3 = M2 (3) > U4 (2).

**This week (Oct 6–12), in this order:**
1. **M1/M2 desk tests:** start today. They cost $0 and need no sponsor time.
2. **M3 incumbent-failure audit:** today, about 1 operator-hour.
3. **Sponsor confirms the Apify account and payout:** 0.25 h if T2's account is reused.
4. **G2 and M3 builds:** publish by Oct 10–12.
5. **G1:** send the DataForSEO permission email today. Build only once the reply arrives.
6. **I2 concierge samples and C1 sample reports:** ready by Oct 9–12, so the first outreach goes out on Oct 12–14.

**Platform concentration:** G1, G2 and M3 all sit on Apify alongside T2. Their tests cost under $10 and finish by Oct 26, so the committee *may* run two of them at once as a shelf bake-off on one account. In that case it accepts the risk that a suspension during the test also hits T2. Keep at most one after the verdict. M1 and M2 share an Atlassian partner account, so test only one.

## Rules that apply to every test

1. **Only strangers count.** Every checkout carries a source tag (`?ref=` or an affiliate code). Purchases by the sponsor's acquaintances, partners' own staff and operator test accounts are logged but excluded from the pass count. On Apify, exclude any user ID linked to the operator.
2. **Automatic refunds.** Wherever delivery is deferred, the operator schedules a job: on the stated date, every undelivered order is refunded through the merchant-of-record API, with no customer action needed. Check that the refund endpoint works with a $1 test order before launch. If Lemon Squeezy is not accepting new stores (Stripe Managed Payments transition), use Gumroad or Stripe Managed Payments.
3. **"Founding price" must be real.** The higher price must actually apply to later buyers, and founding buyers keep their price. No countdown timers, no "only N left", no invented testimonials or user counts. Listings disclose AI-generated content wherever it is part of the product.
4. **External API costs on Apify free-plan users.** Apify pays developers only for paid-plan usage, but supplier bills (DataForSEO, Groq) are still incurred on free-plan runs. Apify permits free-plan limits if they are disclosed in the README and input schema. Use them in G1 and G2.
5. **Pre-commit the verdict.** The operator writes the thresholds into `runs/2026-10-06-round2/tests/<ID>.md` before launch and records the result on the verdict date. Moving the goalposts mid-test counts as a fail.

---

## G1 — Keyword→Brief (Apify Actor) · Testability 7

**What's wrong with the brief's test.** The $0.004 metrics-only listing tests the wrong product. It wins price shoppers on an event that nets only $0.003 per keyword, and break-even would need about 95k paid keywords a month. The margin is in the brief event, so the test has to include a version of it. Free-plan runs would also drain the $50 DataForSEO float without paying anything out.

- **Gate 0:** DataForSEO's written OK on resale through Apify. Don't publish without it. The email goes today.
- **Test type:** live paid listing (Apify Store search plus PPE billing).
- **Offer:** "Keyword Volume + SERP Brief API — failed rows never charged."
  - `keyword-metrics` at $0.006 per keyword: half the leader's price, not a third.
  - `serp-brief-lite` at $0.02 per keyword: top 10, PAA, AI Overview presence and cited URLs. No page fetching yet.
  - Free-plan runs are capped at 25 keywords, stated in the README.
- **Assets:** the Actor with both events, schemas, README and a nightly self-test. About 3 operator-days.
- **Traffic:** Apify Store keyword shelf (the top 3 Actors have about 1.4k users in 30 days). Expect 30–100 trial users in 14 days, mostly on free plans.
- **Thresholds (publish by Oct 11, verdict Oct 25):**
  - **Pass:** ≥10 paid-plan users, ≥$15 billed, and ≥3 paid-plan users of `serp-brief-lite`.
  - **Pivot:** 4–9 paid users, or metrics sell while the brief doesn't.
  - **Fail:** ≤3 paid users.
- **Cost:** a $50 float (about $5 consumed). Sponsor time is 1–1.5 h, or 0.5 h if T2's Apify account is reused.
- **Does NOT prove:** retention of scheduled pipelines, stability of DataForSEO's terms, whether the Store ranking holds once clones undercut the price, or any MCP/x402 agent demand.

## G2 — LongForm Transcripts (Apify Actor) · Testability 8

**What's wrong with the brief's test.** Its price story is wrong. `steadyfetch/media-transcriber` already charges $0.006/min, below our $0.009. Price is not the wedge. The wedge is RSS batches, large-file chunking and chapters, so test those from day 1. Groq bills on free-plan runs, so cap them.

- **Test type:** live paid listing (Apify PPE).
- **Offer:** "Podcast & webinar transcriber: RSS feed or file URL in, timestamped transcript and LLM-ready chunks out."
  - $0.009 per audio minute; `chapters-quotes` at $0.01 per episode.
  - Failed or silent files are never charged.
  - No YouTube, TikTok or Instagram fetching.
  - Free-plan runs are capped at 30 audio minutes, disclosed.
- **Assets:** fetch/ffmpeg/Groq pipeline, RSS input, chapters event, and a README with the AUP and rights-complaint policy. About 2.5 operator-days.
- **Traffic:** Apify Store searches for "transcribe", "podcast" and "whisper" (about 1,079 users in 30 days across the top results). Expect 30–80 trial users in 14 days.
- **Thresholds (publish Oct 10, verdict Oct 24):**
  - **Pass:** ≥8 paid-plan users, ≥2,000 paid minutes, and ≥1 paid user running on a schedule or RSS batch.
  - **Pivot:** 3–7 paid users or 500–1,999 minutes. Drop chapters and test $0.007.
  - **Fail:** <3 paid users or <500 paid minutes.
- **Cost:** $5 OpenAI credit plus about $2 of Groq. Sponsor time is 0.5 h (Groq card, Apify reused) to 1.25 h (new Apify account).
- **Does NOT prove:** copyright or takedown exposure at volume, survival against a $0.004 clone, or that the 49k minutes a month needed for break-even is reachable (2,000 minutes is about 4% of it).

## G3 — AnswerShare API · Testability 3

**What's wrong with the brief's test.**
- "100 calls from 10 keys" counts free RapidAPI keys, which are the weakest signal and trivially created.
- Payment is read only on day 40.
- The sponsor would complete three KYC setups (about 2.5 h) before any signal arrives.
- MentionsAPI already sells the same thing at $0.02 per cached check, with an MCP server.

**Step 0 (today, $0, about 1 operator-hour).** Record the visible 30-day users of every Apify GEO / "AI visibility" Actor (the brief reports 18–55 each, including free users) and the RapidAPI listings in the category. If no listing shows ≥50 monthly users, kill the idea: the paying pool is too small for an unknown newcomer.

- **Test type:** paid API listing on **RapidAPI only** (one KYC). MCPize and the free directories come only after a pass.
- **Offer:** "AI-search visibility check: is brand X mentioned or cited by ChatGPT-search (API), Perplexity and Gemini for this prompt? Raw cited URLs in JSON."
  - $0.10 per check, or $29/mo for 300 checks.
  - Free tier: 5 checks, not 25.
  - The listing states plainly that API answers differ from the consumer ChatGPT app.
- **Assets:** Worker + D1, three engine adapters, parser, listing and one sample report. About 4 operator-days.
- **Traffic:** RapidAPI search only. Expect 10–40 free keys in 4 weeks (unverified, zero reviews).
- **Thresholds (list by Oct 13, verdict Nov 10):**
  - **Pass:** ≥3 paying accounts or ≥$30 of paid usage.
  - **Pivot:** 1–2 payers. Add the MCPize listing.
  - **Fail:** 0 payers.
- **Cost:** $10 of credits plus about $5 of COGS on free checks. Sponsor time is 1–1.5 h.
- **Does NOT prove:** retention through the `watch` endpoint, or that agencies trust API answers as a stand-in for the consumer app.

## C1 — FunderFit · Testability 4

**What's wrong with the brief's test.**
- It parses 3 years of 990-PF data for 10 days before the first pitch, which delays the slowest step (partner replies).
- The free member perk confounds willingness to pay.
- "Agree to mention" isn't a commitment unless it has a date.

- **Test type:** partner commitment, then a paid founding report sold through the partner's mention.
- **Offer:** "25 foundations that actually funded organisations like your client: actual grants, amounts and years from IRS filings, white-labelled with your logo. Founding price $19 for your first report ($39 from Jan 1)."
  - Delivered within 24 h.
  - Automatic refund if fewer than 15 funders match.
  - **No free perk until the paid test reads.**
- **Assets:**
  - Parse the **latest filing year only** for the samples; extend to 3 years after a pass. About 2.5 operator-days.
  - 12 custom sample reports.
  - Lemon Squeezy checkout plus affiliates.
  - A one-page site.
  - A partner kit.
  - Together about 4 operator-days. Pitches go out Oct 12–14.
- **Traffic:** 12 one-to-one pitches sent by the sponsor. Expect 2 mentions reaching about 800–2,000 readers (Substacks of about 1–2k, academy communities) and 20–60 visits.
- **Thresholds:**
  - **Partner gate:** ≥2 written commitments with a mention date by Nov 6.
  - **Pass:** ≥5 paid reports from strangers within 14 days of the first mention, and by Dec 4 at the latest (the second half of December is dead).
  - **Pivot:** 2–4 paid reports.
  - **Fail:** <2 paid reports, or <2 partners. In either case, kill. Don't fall back to Gumroad, which has no grant-writer traffic.
- **Cost:** about $17. Sponsor time is about 2.5 h (KYC 1 h, emails 1 h, replies 0.5 h).
- **Does NOT prove:** uptake of the $99 plan, repeat purchases, whether partners mention it more than once, or data quality across 3 years.

## C2 — Client Safety Kit · Testability 5 (3 if D2 is not live)

**What's wrong with the brief's test.**
- "Billed when the first kit ships" adds nothing, because a kit can ship within 72 h. Charge now.
- Partner audience sizes are unverified.
- The cheapest channel is missing: D2's own personal-email outreach already reaches safety consultants. A one-line C2 offer in those emails costs $0 of extra traffic.
- The kit doesn't need D2's ingest for the test. The operator can pull last month's citations straight from the DOL enforcement API (about 1 day).

- **Test type:** paid subscription, charged now.
- **Offer:** "Your logo, your clients' crews: 4 bilingual toolbox talks plus a one-page 'OSHA cited your industry this month' brief, every month. $29/mo founding (up to 10 client kits; $49 later). First kit within 72 h. Cancel anytime."
- **Assets:**
  - A seed library of **3 trades × 8 talks**, not 150, with a native-Spanish spot check (about $20).
  - The brief generator.
  - 10 partner-branded sample kits.
  - A subscription checkout.
  - About 3 operator-days.
- **Traffic:**
  - 10–12 pitches: Primus, 6–8 Inogen firms, an ASSP lead.
  - The C2 line added to D2's consultant emails (assume 40–60 recipients).
- **Thresholds:**
  - **Partner gate:** ≥2 commitments or firm pilots by Nov 6.
  - **Pass:** ≥4 paying consultants by Nov 20.
  - **Pivot:** 2–3 paying consultants.
  - **Fail:** ≤1 paying consultant by Dec 4.
- **Cost:** about $35 ($15 LLM, $20 Spanish check). Sponsor time is 1.5–2 h.
- **Does NOT prove:** churn after the novelty fades, whether consultants actually forward kits to clients, or the content-liability exposure.

## C3 — Interpreter Practice Lab · Testability 3

**What's wrong with the brief's test.**
- A 10-dialogue demo built over 14 days is too slow. Five dialogues are enough to pitch.
- The calibration gate must pass *before* any student sees a score, not alongside the sale.
- A 10-session free perk can satisfy a candidate's whole pre-exam need, which suppresses paid conversion.

- **Test type:** partner commitment plus a quality gate, then a paid 30-day pass.
- **Offer:** "Scored practice for the medical-interpreter oral exam format: consecutive and sight translation, scored for omissions, additions and terminology. Original content; not affiliated with CCHI/NBCMI. 30-day pass $19 founding ($29 later)."
  - Free perk: 3 scored sessions.
  - Schools: a $150 first month for up to 40 students.
- **Assets:** 5 dialogues, the recorder, the scoring pipeline and a report. About 6 operator-days; the demo is ready by Oct 14 and pitches go out Oct 15–19.
- **Traffic:** InterpreMed, Bridging Words (about 3.1k subscribers) and self-paced schools. Expect 300–1,000 candidates to see the first promotion.
- **Thresholds:**
  - **Partner gate:** ≥2 commitments by Nov 13.
  - **Calibration:** ≥80% of 20 recordings within ±1 of the human rater by Nov 20. Otherwise kill.
  - **Pass:** ≥8 paid passes within 21 days of the first promotion, or 1 school paying, by Dec 18.
  - **Pivot:** 3–7 paid passes.
  - **Fail:** <3 paid passes.
- **Cost:** about $35 of build plus $40 for the rater. Sponsor time is 2.5–3 h.
- **Does NOT prove:** exam pass-rate impact, school renewals, or whether a small, tight-knit community stays positive after the first scoring error.

## I1 — Zì Bot (Discord) · Testability 5

**What's wrong with the brief's test.**
- Asking for a pre-order of an unseen AI feature, inside a bot whose users expect free, gives a low, noisy number. The sponsor already has the practice code, so ship a capped `/practice` and sell the real thing.
- The brief mixes the distribution signal (servers, WAU) with the payment signal. Gate them separately.
- Check that Discord's developer policy allows an external checkout link before the app is verified.

- **Test type:** real paid tier inside the free bot, delivered immediately.
- **Offer:** "Zì Supporter: level-locked AI writing practice at your HSK 3.0 band, plus personal SRS reviews in DMs. $3.99/mo, or $29 for the first year at the founding price."
  - Free users get 3 practice turns a week.
  - The paid tier is 18+.
- **Assets:** quiz, dictionary and leaderboard core (5 operator-days), a `/practice` port (2 days), checkout, and ToS/privacy pages.
- **Traffic:**
  - 5–6 server-admin requests from the sponsor (disclosed maker).
  - top.gg and discordbotlist listings.
  - One r/ChineseLanguage post within the subreddit's rules.
  - If 2 servers accept, expect 300–800 weekly active users.
- **Thresholds (verdict Nov 20):**
  - **Distribution gate:** ≥250 WAU or ≥8 servers. If it is missed, call it a distribution fail; the payment result means nothing without it.
  - **Pass:** ≥8 paid supporters from strangers.
  - **Pivot:** 3–7 paid. Test Server Pro instead.
  - **Fail:** <3 paid.
- **Cost:** about $17. Sponsor time is about 2 h.
- **Does NOT prove:** retention past month 1, conversion after Discord's 30% Premium Apps cut, or January peak behaviour.

## I2 — Episode Study Packs · Testability 7

**What's wrong with the brief's test.**
- A 7-day full pipeline before the first email is unnecessary. Produce the first packs concierge-style in about 2 days.
- Count a paying creator only if they publish ≥2 episodes a month (otherwise there is no subscription).
- Fix the verdict to 14 days after the last send, so that late contacts get a fair window.

- **Test type:** free sample on request, then a paid founding month, delivered immediately.
- **Offer:** "Send an episode link; within 24 h get a pack in your branding: hanzi/pinyin/English PDF, HSK 3.0 vocabulary, notes, and Anki + Pleco decks, as editable files you check before publishing. Founding month $29 for 4 episodes ($39 later)."
- **Assets:**
  - 3 public sample packs from Creative Commons audio.
  - A concierge production script.
  - A landing page and checkout.
  - About 2–3 operator-days; ready by Oct 10.
- **Traffic:** 40 named creators, each with a public business email, contacted 1:1 by the operator at ≤5 a day (Oct 12–23). Each email has a CAN-SPAM footer and at most one follow-up. Expect 10–14 replies and 6–10 sample requests.
- **Thresholds (verdict Nov 9):**
  - **Pass:** ≥3 paying creators.
  - **Pivot:** ≥6 sample requests but <3 paid. Test $12 per episode, pay-as-you-go.
  - **Fail:** <4 replies.
  - Stop immediately on any spam complaint.
- **Cost:** about $17. Sponsor time is about 1 h (KYC, approving the template).
- **Does NOT prove:** month-2 retention, whether creators tolerate pinyin errors under their brand, or a market larger than about 150 creators.

## I3 — Role-Play Room · Testability 3

**What's wrong with the brief's test.**
- "≥4 paid **or** ≥10 trials" lets free usage stand in for payment. Only payment passes.
- Instructors are mid-semester now, and the answer can't arrive before mid-December. A miss pushes the next read to July–August 2027.

- **Test type:** paid founding licence, charged now, with an automatic refund.
- **Offer:** "Spring 2027 founding class: level-locked AI role-play homework on this week's vocabulary, with transcripts and a class error report. $99 per class (list $149 from spring 2027), up to 30 students, 18+ only."
  - Refunded automatically if fewer than 5 students complete an assignment by Feb 15.
  - A free trial assignment comes first.
- **Assets:** a one-assignment demo, the dashboard, checkout and a data-practices page. About 5–6 operator-days; ready by Oct 16.
- **Traffic:** 60 named instructors on public faculty pages, emailed by the operator at ≤6 a day (Oct 19–30), plus emails to ACTFL presenters after Nov 22. Expect 9–12 replies and 4–6 trials.
- **Thresholds (verdict Dec 15):**
  - **Pass:** ≥4 paid classes.
  - **Pivot:** 1–3 paid, or ≥5 trials completed by ≥10 students each. Test the $12 student seat.
  - **Fail:** 0 paid and <3 trials.
- **Cost:** about $17. Sponsor time is about 1.5 h.
- **Does NOT prove:** semester-long student use, renewals, whether departments will buy without a DPA, or the size of the market beyond the first 60 instructors.

## M1 — ChatRelay for Jira · Testability 4

**What's wrong with the brief's test.**
- "20 installs" mostly counts free-tier installs (≤10 users).
- Willingness to pay appears only when 30–60-day evaluations end, around day 80–100.
- A $0 leading indicator is available today and the brief only uses it as an afterthought.

- **Step 0 (Oct 6–20, $0):** the operator snapshots daily install counts for all five Forge Google-Chat alternatives through the Marketplace API.
  - **Go** if they gain ≥25 installs combined in 14 days, which shows the banner is pushing admins to switch.
  - **No-go** if they gain <10. Build in parallel only if the sponsor is already doing the partner setup.
- **Test type:** live paid listing (Atlassian search, evaluations and billing).
- **Offer:** "Google Chat notifications for Jira, Forge-native: per-project/JQL routing, one thread per issue, a 5-minute migration from Google's app." Free for ≤10 users; $0.35 per user per month above that.
- **Assets:** Forge app, listing, migration guide and security self-assessment. About 7 operator-days; submit around Oct 16.
- **Traffic:** Marketplace and in-Jira search for "Google Chat" (about 11k orphaned sites). Expect 15–60 installs in 21 days.
- **Thresholds:**
  - **Listing gate (21 days after going live, around Nov 27):** ≥20 installs, including ≥6 evaluations on sites with >10 users.
  - **Pass (Jan 15):** ≥3 paid conversions.
  - **Pivot:** 1–2 paid conversions.
  - **Fail:** 0 paid conversions.
- **Cost:** $0–8. Sponsor time is 2–2.5 h.
- **Does NOT prove:** retention after the January deadline, or what happens if Google ships a Forge rewrite.

## M2 — SpecView for Confluence · Testability 3

**What's wrong with the brief's test.**
- It tests the viewer, a crowded shelf (one Forge bundle has 3,186 installs), while the differentiator (migration) is measured only by waitlist emails, the weakest signal.
- Ship a **read-only** dry-run scan in v1 instead. It writes nothing, so the risk is low, and running it is a behavioural signal.

- **Step 0 ($0):** 14 days of install-velocity snapshots for the Forge Swagger alternatives. Go if they gain ≥20 installs combined.
- **Test type:** live paid listing.
- **Offer:** "OpenAPI/Swagger macro for Confluence, plus a free scan that finds every page using an abandoned Swagger macro and shows the conversion plan." Free for ≤10 users; about $0.12 per user per month at 100 users.
- **Assets:** macro plus the CQL dry-run scan. About 7 operator-days.
- **Traffic:** Marketplace searches for "swagger" and "openapi" (about 5,500 orphan installs). Expect 10–40 installs in 21 days.
- **Thresholds:**
  - **Listing gate (21 days after going live):** ≥15 installs, and ≥5 sites where the scan finds ≥1 orphan macro.
  - **Pass (Jan 31):** ≥2 paid conversions.
  - **Fail:** <5 installs, or 0 scans that find orphan macros. Do not build the page writer.
- **Cost:** $0. Sponsor time is 0 h if M1's partner account exists, otherwise 2 h.
- **Does NOT prove:** that the page writer works safely at scale, or whether orphan vendors migrate late.

## M3 — SheetSync (Apify) · Testability 8

**What's wrong with the brief's test.**
- "The first 1,000 rows of each run free," with about 200 rows per run, makes almost every run free. The test would then measure nothing about willingness to pay. Charge from row 1.
- Check first whether the incumbent's 51% failure rate comes from the incumbent's own bugs or from users' auth mistakes. Read its issues tab (1 operator-hour) before building.

- **Test type:** live paid listing (Apify PPE).
- **Offer:** "Apify → Google Sheets that doesn't fail: append, replace or upsert-by-key, no duplicates, automatic tab rollover, no OAuth (share with our service account)." $0.005 per run plus $0.30 per 1,000 rows. No free rows; free-plan users pay their own credits.
- **Assets:** the Actor, an integration-ready payload, a switching guide and a canary self-test. About 4 operator-days; publish by Oct 12.
- **Traffic:** Apify Store search plus the Console integrations picker (the incumbent has 825 users in 30 days). Expect 20–80 trial users in 14 days.
- **Thresholds (verdict Oct 26):**
  - **Pass:** ≥25 distinct users, ≥5 paid-plan users charged, and ≥95% run success.
  - **Pivot:** 2–4 paid users.
  - **Fail:** ≤1 paid user, or <90% success.
- **Cost:** $0. Sponsor time is 0.25 h on the reused account, 1 h otherwise.
- **Does NOT prove:** survival if the Apify-staff incumbent is fixed, or Google Sheets quota limits at 45 or more paying users.

## U4 — AI-matched job board · Testability 2

**What's wrong with the user's plan.** It proposes free for job seekers now and employer posts later. Employer willingness to pay cannot be tested without an audience, which the operator doesn't have, so as proposed the idea is untestable. Test the seeker-pays alternative in one niche instead, through a channel the sponsor can use honestly.

- **Test type:** a paid one-time report, delivered within 24 h.
- **Offer:** "Upload your resume and get your 30 best-matched open roles from 3,000+ company career boards (Greenhouse, Lever, Ashby), each with why you match and what you're missing. $9 one-time."
  - Automatic refund if fewer than 10 matches.
  - Resumes are deleted after 7 days.
  - Not offered in the EU during the test (AI Act high-risk).
- **Assets:** public ATS-board ingest, embedding and LLM explanations, a landing page and checkout. About 4 operator-days.
- **Traffic:**
  - One Show HN post by the sponsor.
  - One post in a single niche community where the sponsor is a genuine member and the rules allow it.
  - Expect 200–2,000 visitors (high variance).
- **Thresholds (verdict Oct 29):**
  - **Pass:** ≥10 paid reports from ≥400 unique visitors.
  - **Pivot:** 3–9 paid reports.
  - **Fail:** <3 paid reports, or <200 visitors (a distribution fail).
- **Cost:** about $17. Sponsor time is 1.5–2 h.
- **Does NOT prove:** employer willingness to pay, subscription retention (seekers churn when they're hired), or a moat against the free Hiring Cafe.

---

**Sources checked (2026-10-06):**
- [Apify monetisation docs](https://docs.apify.com/actors/publishing/monetize): free-plan limits are allowed if disclosed, and profit counts paid-plan users only.
- [Lemon Squeezy / Stripe Managed Payments 2026 status](https://fungies.io/lemon-squeezy-stripe-acquisition-saas-founders-2026/).
- All other figures come from the round-2 briefs.
