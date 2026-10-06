# Unit Economics Review — 2026-10-06

_Reviewer: unit-economics-analyst. I re-derived every number; ideator figures were not taken on trust. Fees were checked by web search on 2026-10-06 (sources at the bottom)._

## Summary

| ID | Idea | Score | Upfront $ | Monthly fixed $ | Net $/sale | Sales/mo for $300 | Est. operator tokens $/mo | Months to break-even |
|---|---|---|---|---|---|---|---|---|
| D2 | InspectionWatch (OSHA alerts) | 9 | 12 | 5 | 45.81 ($49 plan) | 7 subs | 100 (M1 build 150) | Op M4 · payback M6 · $300 M8 |
| S3 | Custom wedding toasts / eulogies (Etsy) | 8 | 29–43 | 1.5 | ~26 (blended) | 12 orders | 90 (M1 build 80) | Op M5 · payback M7 · $300 M8 |
| S1 | Done-for-you Airbnb guidebook (Etsy) | 8 | 34–48 | 2 (+15 ads M1–2) | ~32 ($39 std) | 10 orders | 90 (M1 build 120) | Op M4 · payback M7 · $300 not in 12 mo (peaks ~$255) |
| D1 | LanguageBids (language-services tenders) | 7 | 12 | 1 (→5–20 at scale) | 26.90 ($29 Solo) | 12 subs | 140 (M1 build 180) | Op M5 · payback M10 · $300 M10 |
| W2 | Florida HOA letter kit (Etsy + LS) | 7 | 18–44 | 2.5 | 21.30 (blend; 34.85 kit) | 15 sales (≈9 kits) | 50 (M1 build 80) | Op M3 · payback M5 · $300 not in 12 mo |
| S2 | Bilingual toolbox talks (packs + $9/mo) | 7 | 33–47 | 2.5 | 14.48 (Etsy blend); 8.00/sub | 21 orders (or 38 subs) | 90 (M1 build 220) | Op M3 · payback M7 · $300 ~M13 |
| T1 | RainCheck for Jobber | 7 | 12 (+20 if SMS) | 1 (+3–11 with SMS) | 17.46 ($19 plan) | 18 subs | 80 (M1–2 build 150/100) | Op M6 · payback M10 · $300 M10 |
| D3 | LabelScout (TTB COLA feed) | 6 | 12 | 1 | 45.81 (Pro); 141 per report | 7 Pro subs | 180 (M1 build 200) | Op M4 (lumpy) · payback M8 · $300 sustained ~M12 |
| W3 | Grant Deadline Desk (one state) | 5 | 12 | 1 | 93.05/yr = 7.75/mo (annual) | 39 annual subs | 200 (M1 build 250) | Cash: payback M5 · MRR basis: op M7, payback M12, $300 M9 |
| W1 | Bid Brief: federal janitorial bids (Substack) | 5 | 0–12 | 4 | 16.12 ($19); 10.07 founding | 19 subs (≈23 at real mix) | 180 (M1 build 200) | Op M9 · payback not in 12 mo |
| T3 | TipSplit for Clover | 5 | 12 | 1 (+20 if email cap hit) | 10.49 | 29 locations | 90 (M1–2 build 150/120) | Op M8 · payback not in 12 mo |
| A1 | Closing Day house portraits (Etsy) | 5 | 42–54 (digital only) | 32 Q4, then 17 (ads) | 18.40 | 18 orders | 90 (M1 build 120) | Op M3 (seasonal only) · payback not in 12 mo |
| A2 | Little Guests wedding activity book | 5 | 41–53 | 32 (incl. ads) | ~15 (blend) | 23 orders | 100 (M1 build 120) | Op M6 · payback ~M13 |
| T2 | Accela/EnerGov permit Actor (Apify) | 4 | 0 | 0 (risk 29) | ~2.80 per 1k permits | ~107k permits (≈20 steady users) | 120 (M1 build 150) | Op M8 · payback not in 12 mo |
| A3 | "Looks Like Me" visual schedule cards | 3 | 69 (overrun risk to ~105) | 32 (incl. ads) | ~10.86 (blend) | 31 orders | 120 (M1 build 180) | Op M10 · payback not in 12 mo |

**Definitions.** M1 = October 2026 (partial). *Net $/sale* = price minus payment/marketplace fees, listing renewal and per-order generation/LLM cost. *Sales/mo for $300* = sales needed for $300 net after the business's own fixed costs (operator tokens are what the $300 is meant to pay for). *Op* = first month the business covers its fixed costs **and** my operator-token estimate. *Payback* = first month cumulative cash (including upfront capital and build-phase token burn) turns positive. *$300* = first month net revenue minus fixed costs reaches $300.

## Method and shared assumptions

**Operator token burn.** I price a routine operator session (monitoring, support replies, listing tweaks, one content piece) at about **$4**, and a heavy build or research session at about **$12–15**. Mid-tier model with prompt caching; frontier-model sessions would cost roughly 2–3x. Each idea's **M1 includes the build-phase burn**, which ideators ignored. That burn is real cash even though it does not count against the $100 upfront cap. Per-order LLM and image costs are in *net $/sale*, not in the operator line.

**Verified fees (2026-10-06):**
- **Lemon Squeezy:** 5% + $0.50, **+0.5% on subscription payments**, +1.5% on international or PayPal payments. Ideators left out the subscription and international surcharges.
- **Etsy:** $0.20 listing (renewed on each sale), 6.5% transaction fee, 3% + $0.25 processing (US), 15% Offsite Ads on attributed sales, and a $15–$29 one-time setup fee (I use $29 as the worst case).
- **Substack:** 10% + Stripe 2.9% + $0.30 + 0.7% recurring billing.
- **Gumroad:** 10% + $0.50 + card processing on direct sales; 30% flat via Discover.
- **Apify pay-per-event:** profit = 0.8 × revenue − platform usage; only users on paid plans count. Free plan $5/mo credit; Starter $29.
- **Clover App Market:** 70% of net subscription revenue to the developer.
- **TPT:** Basic tier 55% payout + $0.30 per resource; Premium $59.95/yr for 80%.
- **Twilio A2P 10DLC:** about $4.50 brand + $15 campaign vetting one-time, plus $1.50–$10/mo per campaign.
- **Resend free tier:** 3,000/mo **and 100 emails/day**. The daily cap is the trap for daily-alert and bulk-statement products; Pro is $20/mo.
- **Image APIs:** about $0.01–$0.04 per image at medium quality, about $0.13 at high quality (GPT-image-1.5 tier).
- **Jobber App Marketplace:** I could not find any published revenue share or billing rule. This is an open risk for T1.

**Payout lags.** Apify (T2) and Clover (T3) pay monthly in arrears, so their projections shift cash one month later.

---

## T1 — RainCheck for Jobber

**Upfront:** $12 (domain). The ideator missed the cost of the $39 tier's SMS: A2P 10DLC registration (~$20 one-time) plus $1.50–$10/mo per campaign and ~$1.15/mo per number. Launch email-only and add SMS later.
**Fixed:** ~$1/mo; Cloudflare, NWS and Resend free tiers suffice (one digest per customer per day stays under 100/day until ~90 customers).
**Per sale:** $19 − (5.5% + $0.50) = **$17.46**; Canadian buyers lose another ~$0.29. The $39 tier nets ~$35 before SMS. Jobber may impose a revenue share or its own billing; that is unverified.
**Tokens:** about $150 to build in M1 and $100 in M2 (review change requests), then ~$80/mo (≈20 light sessions).
**Needed:** 18 subs for $300; 6 subs to cover tokens.

The ideator's day-45 first sale lands in **late November**, when lawn and exterior trades go dormant. My ramp is 1→5 subs through March, then the spring surge.

| Month | Net revenue $ | Fixed $ | Op. tokens $ | Monthly net $ | Cumulative $ |
|---|---|---|---|---|---|
| M0 (upfront) | – | – | – | -12 | -12 |
| M1 | 0 | 1 | 150 | -151 | -163 |
| M2 | 0 | 1 | 100 | -101 | -264 |
| M3 | 17 | 1 | 80 | -64 | -328 |
| M4 | 35 | 1 | 80 | -46 | -374 |
| M5 | 52 | 1 | 80 | -29 | -402 |
| M6 | 87 | 1 | 80 | 6 | -396 |

Months 7–12 (Apr–Sep 2027) reach 8→21 subs: operating break-even in **M6**, payback in **M10**, $300 in **M10**. The economics are clean (≈92% margin), but the timing works against it: almost a full winter of token burn (~$400 cumulative) comes before the spring revenue. **Score 7.**

## T2 — Accela & EnerGov Permit Extractor (Apify)

**Upfront:** $0, which is correct.
**Fixed:** $0 while self-tests fit in the $5 free credit. If Accela portals force headless browsers or residential proxies, the developer's own test runs push it onto the **$29 Starter plan**.
**Per unit:** $4.00 per 1k permits × 0.8 = $3.20, minus platform usage. With HTTP-only crawling and a detail-page fetch per permit, platform usage is ~$0.10–$0.80 per 1k, so I use **≈$2.80 per 1k** (+$0.016 per run start). Free-plan users pay nothing out.
**Volume reality:** A "watch" user covering 3 mid-size counties pulls ~4–6k new permits/month, worth ~$12–17 net. **$300 therefore needs ~107k paid permits/month, about 20 steady paid users.** The ideator's figure was 10. One-off backfills give spikes, not a run rate.
**Tokens:** about $120/mo. This is maintenance-heavy: two portal families, 100+ jurisdictions, nightly breakage triage and coverage requests. M1 build costs about $150.

| Month | Net revenue $ | Fixed $ | Op. tokens $ | Monthly net $ | Cumulative $ |
|---|---|---|---|---|---|
| M0 (upfront) | – | – | – | 0 | 0 |
| M1 | 0 | 0 | 150 | -150 | -150 |
| M2 | 0 | 0 | 120 | -120 | -270 |
| M3 | 10 | 0 | 120 | -110 | -380 |
| M4 | 30 | 0 | 120 | -90 | -470 |
| M5 | 50 | 0 | 120 | -70 | -540 |
| M6 | 75 | 0 | 120 | -45 | -585 |

Typical Apify Store Actors earn tens of dollars a month. My ramp reaches ~$240/mo earned by M12 and **turns operating-positive in M8**. Payback falls outside 12 months (−$335 at M12), and $300 is not reached. Per-unit revenue is too thin for the maintenance load. **Score 4.**

## T3 — TipSplit for Clover

**Upfront:** $12. **Per location:** $14.99 × 70% = **$10.49**, with no other processing fee. Clover pays out monthly in arrears.
**Fixed:** about $1. There is a hidden trap in the **Resend 100/day cap**. Sunday statements for 7+ cafés × 15 staff go over 100 emails in one day, so the operator must stagger sends or pay $20/mo for Pro (that would raise the $300 requirement to 31 locations).
**Tokens:** about $150 to build in M1 and $120 in M2 for Clover review changes, then ~$90/mo. Wage-dispute-adjacent support is not "light".
**Needed:** 29 paying locations for $300 and ~9 to cover tokens.

Approval around mid-November plus a 30-day trial gives first billing around mid-December and **first cash in January**.

| Month | Net revenue $ | Fixed $ | Op. tokens $ | Monthly net $ | Cumulative $ |
|---|---|---|---|---|---|
| M0 (upfront) | – | – | – | -12 | -12 |
| M1 | 0 | 1 | 150 | -151 | -163 |
| M2 | 0 | 1 | 120 | -121 | -284 |
| M3 | 0 | 1 | 90 | -91 | -375 |
| M4 | 10 | 1 | 90 | -81 | -456 |
| M5 | 31 | 1 | 90 | -60 | -515 |
| M6 | 52 | 1 | 90 | -39 | -554 |

Months 7–12 grow to 21 locations. Operating break-even comes in **M8**, cumulative cash is still −$281 at M12, and **$300 is not reached within 12 months**. The margin is fine, but $10.49 per unit, a 30-day trial and a 2–4 week approval stack three delays on top of each other. A 14-day trial helps by about one month. **Score 5.**

## W1 — Bid Brief: Facilities Services

**Upfront:** $0–$12. Substack works on a subdomain.
**Per sub:** on $19 the ideator forgot Stripe's 0.7% recurring-billing fee, so $19 − 10% − (2.9% + $0.30) − 0.7% = **$16.12**. The **$12 founding rate nets $10.07** and annual $149 nets $10.70/mo. A realistic mix with ~10 locked-in founders averages ~$13, so **≈23 subs for $300**, not 20.
**Fixed:** ~$4 (OCR fallback).
**Tokens:** this is content-heavy. It produces 9 issues/mo, each extracting SOWs from ~40–80 notices with 40-page PDFs: ~$30–50/mo of extraction API, ~$70 of QA sessions and ~$60 for state pages, support and outreach. That comes to **~$180/mo**, plus a $200 M1 build and backfill.

| Month | Net revenue $ | Fixed $ | Op. tokens $ | Monthly net $ | Cumulative $ |
|---|---|---|---|---|---|
| M0 (upfront) | – | – | – | -12 | -12 |
| M1 | 0 | 4 | 200 | -204 | -216 |
| M2 | 20 | 4 | 180 | -164 | -380 |
| M3 | 40 | 4 | 180 | -144 | -524 |
| M4 | 60 | 4 | 180 | -124 | -647 |
| M5 | 91 | 4 | 180 | -93 | -741 |
| M6 | 115 | 4 | 180 | -69 | -809 |

At 13–21 subs over months 7–12 it turns **operating-positive in M9**. Cumulative cash is still about **−$657 at M12**. The token load is fixed while revenue per subscriber is low and churn after "no win" is likely. Cutting to one issue a week (~$110/mo of tokens) would pull break-even to ~M6. **Score 5.**

## W2 — Florida HOA Board Letter & Notice Kit

**Upfront:** Etsy setup $15–29 + 10 listings $2 + preview images ~$1 + optional domain $12 = **$18–44**. The attorney review ($250–$400) has to come from revenue.
**Per sale (Etsy):** $39 kit nets **$34.85**; $14 mini-pack nets **$12.22**. Lemon Squeezy direct sales net $36.55. Each Offsite Ads sale loses another 15%. At a 40/60 kit/mini mix the blend is **$21.30**.
**Fixed:** ~$2.50 (renewals and domain).
**Tokens:** ~$50/mo. The product is static: weekly tag tuning, message drafts and a July law-change refresh (~$100 in that month). The M1 build is ~$80.
**Needed:** 15 mixed sales (≈9 full kits) for $300, and 3 sales to cover tokens.

Demand is small and seasonal, peaking Jan–Mar around annual meetings. My ramp is 1→8 sales/mo, peaking in February, then 4–5/mo.

| Month | Net revenue $ | Fixed $ | Op. tokens $ | Monthly net $ | Cumulative $ |
|---|---|---|---|---|---|
| M0 (upfront) | – | – | – | -44 | -44 |
| M1 | 21 | 2 | 80 | -61 | -105 |
| M2 | 43 | 2 | 50 | -10 | -115 |
| M3 | 64 | 2 | 50 | 11 | -104 |
| M4 | 128 | 2 | 50 | 75 | -28 |
| M5 | 170 | 2 | 50 | 118 | 90 |
| M6 | 149 | 2 | 50 | 97 | 186 |

This is the cheapest idea to keep alive. It is **operating-positive in M3 and pays back in M5**, but it peaks at ~$170/mo net in February and **does not reach $300 in 12 months** without the Texas or other-state expansion. The fee math is fine; the ceiling is the market, not the margin. **Score 7.**

## W3 — Grant Deadline Desk: [State]

**Upfront:** $12. **Per sale:** annual $99 nets $93.05 (Lemon Squeezy 5.5% + $0.50), i.e. **$7.75/mo**. The $79 launch rate nets $74.15. Monthly $15 nets $13.68. The $199 consultant licence nets $187.55.
**Needed:** **39 active annual subs** for $300 (the ideator said 35), or 26 just to cover tokens.
**Tokens:** heavy. It requires a monthly crawl and verification of 200–400 funder pages plus extraction, one-line eligibility summaries, monthly email, SEO pages and gap fixes. That is **~$200/mo**, with a $250 M1 build for the funder universe from 990-PF data.

Cash projection (annual prepay front-loads cash; ~4 new annual sales/mo plus a slowly growing monthly base):

| Month | Net revenue $ | Fixed $ | Op. tokens $ | Monthly net $ | Cumulative $ |
|---|---|---|---|---|---|
| M0 (upfront) | – | – | – | -12 | -12 |
| M1 | 0 | 1 | 250 | -251 | -263 |
| M2 | 148 | 1 | 200 | -53 | -316 |
| M3 | 236 | 1 | 200 | 35 | -281 |
| M4 | 437 | 1 | 200 | 236 | -44 |
| M5 | 451 | 1 | 200 | 250 | 206 |
| M6 | 465 | 1 | 200 | 264 | 470 |

**Do not be fooled by the cash curve.** It pays back in M5 only because 12 months of revenue arrive upfront. The renewal cliff hits at M14, and churned nonprofits leave a gap. On an MRR-equivalent basis the business is **operating-positive in M7, reaches $300 in M9 and pays back in M12**. The low per-month value of an annual nonprofit sub combined with a content-heavy crawl is the core weakness. **Score 5.**

## D1 — LanguageBids

**Upfront:** $12. **Per sub:** Solo $29 nets **$26.90** (Lemon Squeezy 5.5% + $0.50). Canadian and EU buyers (a real share of this market) pay another 1.5%, giving ~$26.47. Agency $79 nets ~$73. I use **$30 blended**.
**Fixed:** ~$1 at launch. Send the free weekly digest via beehiiv's free tier, not Resend: 500 recipients in one day breaks the 100/day cap. Expect $5–20/mo once paid alerts pass ~100/day.
**Tokens:** ~$140/mo. That covers four ingesters (SAM, TED, CanadaBuys, USAspending), daily classification and summaries of 20–80 notices (~$30 API), the quarterly market report and pitch drafting. The M1 build and 12-month backfill cost ~$180.
**Needed:** 12 Solo subs (≈10 blended) for $300; 5 to cover tokens.

| Month | Net revenue $ | Fixed $ | Op. tokens $ | Monthly net $ | Cumulative $ |
|---|---|---|---|---|---|
| M0 (upfront) | – | – | – | -12 | -12 |
| M1 | 0 | 1 | 180 | -181 | -193 |
| M2 | 30 | 1 | 140 | -111 | -304 |
| M3 | 60 | 1 | 140 | -81 | -385 |
| M4 | 90 | 1 | 140 | -51 | -436 |
| M5 | 150 | 1 | 140 | 9 | -427 |
| M6 | 180 | 1 | 140 | 39 | -388 |

At 8→13 subs over months 7–12: operating-positive in **M5**, payback in **M10**, $300 in **M10**. The margin is high and few sales are needed. The risk is market size (a few thousand LSPs), not the unit economics. **Score 7.**

## D2 — InspectionWatch

**Upfront:** $12. **Per sub:** $49 Territory nets **$45.81**, $99 nets $93.06 and $199 nets $187.56 (Lemon Squeezy 5.5% + $0.50). I use $48 blended.
**Fixed:** ~$5. Workers Paid covers the D1 limits; 5 years of inspections and violations is hundreds of thousands of rows, not "millions", so a $25 Postgres plan is unnecessary. Email stays within free tiers at this scale.
**Tokens:** ~$100/mo. The daily ingest is mechanical, and the operator writes state pages, quarterly reports and editor pitches. Watch for breakage from the DOL v4 API migration. The M1 build and 5-year backfill cost ~$150.
**Needed:** **7 subs for $300; 3 to cover tokens.** This is the best ratio in the batch.

| Month | Net revenue $ | Fixed $ | Op. tokens $ | Monthly net $ | Cumulative $ |
|---|---|---|---|---|---|
| M0 (upfront) | – | – | – | -12 | -12 |
| M1 | 0 | 1 | 150 | -151 | -163 |
| M2 | 48 | 5 | 100 | -57 | -220 |
| M3 | 96 | 5 | 100 | -9 | -229 |
| M4 | 144 | 5 | 100 | 39 | -190 |
| M5 | 192 | 5 | 100 | 87 | -103 |
| M6 | 240 | 5 | 100 | 135 | 32 |

Ramp 6→10 subs over months 7–12 (with churn). It is operating-positive in **M4**, pays back in **M6** and reaches $300 in **M8**. The unit economics are excellent. Whether 7–10 consultants pay instead of using free osha.gov lookups or Apify actors is a question for the sales and market reviewers, not this one. **Score 9.**

## D3 — LabelScout

**Upfront:** $12. **Per sale:** Pro $49 nets **$45.81**, Team $129 nets $121.40, and a $149 quarterly report nets $141.05. Affiliate income is ~$0 for months. It needs a human applicant and age-gating, and spirits programmes pay a few % on low volume.
**Fixed:** ~$1; link to TTB images instead of mirroring them.
**Tokens:** content-heavy, at **~$180/mo**. It runs a daily COLA crawl and classification of ~4k filings/week (~$20–35 API with a small model on form fields; label-image OCR would double it), two digest editions, consumer SEO pages, scoop pitches and a quarterly report. The M1 build plus 12-month backfill costs ~$200.
**Needed:** 7 Pro subs for $300; 4 to cover tokens.

The B2B buyer (label printers) is slow and unproven. I assume the first Pro sub in M3 and 2 report sales each quarter.

| Month | Net revenue $ | Fixed $ | Op. tokens $ | Monthly net $ | Cumulative $ |
|---|---|---|---|---|---|
| M0 (upfront) | – | – | – | -12 | -12 |
| M1 | 0 | 1 | 200 | -201 | -213 |
| M2 | 0 | 1 | 180 | -181 | -394 |
| M3 | 46 | 1 | 180 | -135 | -529 |
| M4 | 374 | 1 | 180 | 193 | -336 |
| M5 | 137 | 1 | 180 | -44 | -380 |
| M6 | 183 | 1 | 180 | 2 | -378 |

The M4 jump is the Q4 report spike, not a run rate. Subscription revenue alone covers tokens around M7–M8. Payback comes in **M8**, and **sustained $300 (7 Pro subs) only around M12**. The margins are good, but $180/mo of content burn against an uncertain B2B conversion. **Score 6.**

## A1 — "Closing Day" house portraits

**Upfront:** Etsy setup $29 + 25 listings $5 + ~150 images $8 + optional domain = **$42–54 for digital only**. Missed: **Printify samples**. Selling framed prints and ornaments without inspecting a sample is a QC gamble, and 2–3 samples (~$40–60 shipped) push the total to ~$95–114, at or over the cap. Defer physical products until revenue pays for the samples.
**Per sale:** $22 digital → Etsy 6.5% + 3% + $0.25 + $0.20 renewal = $19.46. Print-ready output realistically needs high-quality edits plus a 16×20" upscale (~$0.50) and vision-QA tokens (~$0.20), and some sales carry Offsite Ads. That gives **≈$18.40**. Ornament upsell: $24 − ~$12 base − ~$5 shipping − Etsy fees leaves **only ~$4–5**.
**Fixed:** Etsy Ads $30/mo in Q4, then $15, plus renewals: **$32 → $17**.
**Tokens:** ~$90/mo (listing tuning, message drafts, revisions); M1 $120.
**Needed:** 18 orders for $300.

| Month | Net revenue $ | Fixed $ | Op. tokens $ | Monthly net $ | Cumulative $ |
|---|---|---|---|---|---|
| M0 (upfront) | – | – | – | -54 | -54 |
| M1 | 37 | 32 | 120 | -115 | -169 |
| M2 | 92 | 32 | 90 | -30 | -198 |
| M3 | 147 | 32 | 90 | 26 | -172 |
| M4 | 55 | 16 | 90 | -51 | -224 |
| M5 | 74 | 16 | 90 | -33 | -257 |
| M6 | 92 | 16 | 90 | -14 | -271 |

Q4 gift demand makes **M3 (December) briefly operating-positive**. January collapses, and a 0-review shop in a saturated $10–20 AI-portrait niche plateaus at ~6–7 orders/mo. **Payback is not reached in 12 months** (−$211 at M12). **Score 5.**

## A2 — Little Guests wedding activity book

**Upfront:** $29 setup + $4 listings + $8 images = **$41** ($53 with a domain).
**Per sale:** $19 base nets $16.25 after Etsy fees and ~$0.50 of generation and QA. $32 nets ~$28.00, and the $6 review-bait pack nets **$4.98**. The ideator's "$20 average net" ignores the $6 pack and the base-tier skew. My blend is **~$15**.
**Fixed:** $30 ads + renewals = **$32**.
**Tokens:** ~$100/mo. Each order needs likeness and printability QA and revisions are common; M1 build of the puzzle and layout engine costs ~$120.
**Needed:** 23 orders for $300; ~9 to cover tokens.

October launch is off-season; the birthday edition carries Q4, and engagement-season planning lifts M4–M6.

| Month | Net revenue $ | Fixed $ | Op. tokens $ | Monthly net $ | Cumulative $ |
|---|---|---|---|---|---|
| M0 (upfront) | – | – | – | -41 | -41 |
| M1 | 15 | 32 | 120 | -136 | -178 |
| M2 | 45 | 32 | 100 | -86 | -264 |
| M3 | 60 | 32 | 100 | -72 | -336 |
| M4 | 90 | 32 | 100 | -42 | -377 |
| M5 | 120 | 32 | 100 | -12 | -388 |
| M6 | 150 | 32 | 100 | 18 | -370 |

Over months 7–12 (spring wedding planning) it reaches 12–14 orders/mo. It is **operating-positive in M6**, ends at **−$34 cumulative at M12** (payback ~M13), and **never reaches $300**. The ads line ($360/yr) is more than a third of all net revenue in the first six months ($180 of $480). Test turning it off once reviews exist. **Score 5.**

## A3 — "Looks Like Me" visual schedule cards

**Upfront:** $29 + $4 + **$36 base library = $69**. The ideator's own risk note says rerolls can exceed 3×. At 2.5× the library costs ~$90 and the total goes to **~$105, over the hard cap**. Mitigation: build 3 launch avatars, not 6, or use a cheaper model (~$0.011/image tier) for drafts.
**Per sale:** $9 pack nets **$7.70**; $16 nets $14.03; $24 classroom nets $21.27. A $29 custom pack nets $25.80 after Etsy fees, but ~150 images × 1.5 rerolls × $0.04 = $9 plus ~$1 of vision QA leaves **~$15.80**, about half the ideator's implied margin. The free sample loses $0.20 each. My blend is **~$10.86**.
**Fixed:** $32 (ads + renewals), plus TPT Premium $59.95 once TPT opens (M5).
**Tokens:** ~$120/mo (custom orders need heavy QA; library expansion); M1 $180 for 900-image QA.
**Needed:** **31 orders/mo**, which fails the rubric's <30 test.

| Month | Net revenue $ | Fixed $ | Op. tokens $ | Monthly net $ | Cumulative $ |
|---|---|---|---|---|---|
| M0 (upfront) | – | – | – | -69 | -69 |
| M1 | 22 | 32 | 180 | -190 | -259 |
| M2 | 54 | 32 | 120 | -97 | -356 |
| M3 | 87 | 32 | 120 | -65 | -421 |
| M4 | 130 | 32 | 120 | -21 | -442 |
| M5 | 141 | 92 | 120 | -70 | -512 |
| M6 | 141 | 32 | 120 | -10 | -522 |

The January "new routine" bump helps, but at 11–16 orders/mo the business only reaches operating break-even in **M10**. It sits at about −$560 cumulative at M12. Low ticket size, high per-order generation on custom packs and a sensitive QA bar make it the weakest unit economics in the batch. **Score 3.**

## S1 — Done-For-You Airbnb Guidebook

**Upfront:** $15–29 setup + $2 listings + $12 domain + ~$5 images = **$34–48**.
**Per sale:** $39 → Etsy fees $3.96 + renewal $0.20. The ideator missed **per-order research**: 15–25 places verified by web search plus generation, about **$2 of tokens and search fees**, plus ~$0.25 of images. Some sales carry Offsite Ads. That gives **≈$32 net**. Premium $69 nets ~$59 and the $29/yr refresh ~$25.
**Fixed:** ~$2 (+$15/mo ads in M1–M2).
**Tokens:** ~$90/mo routine (listings, revision forms, message drafts); M1 $120 to build the generator and demos.
**Needed:** **10 orders for $300; 3 to cover tokens.**

| Month | Net revenue $ | Fixed $ | Op. tokens $ | Monthly net $ | Cumulative $ |
|---|---|---|---|---|---|
| M0 (upfront) | – | – | – | -48 | -48 |
| M1 | 32 | 17 | 120 | -105 | -153 |
| M2 | 64 | 17 | 90 | -43 | -196 |
| M3 | 64 | 2 | 90 | -28 | -224 |
| M4 | 128 | 2 | 90 | 36 | -188 |
| M5 | 160 | 2 | 90 | 68 | -120 |
| M6 | 192 | 2 | 90 | 100 | -20 |

At 6→8 orders/mo over months 7–12 it is operating-positive in **M4** and pays back in **M7**, but it plateaus at ~$225–255/mo net. **$300 needs ~10 orders**, which needs Premium or bundle mix or refresh renewals. Upsell attach is the lever. Good per-order margin, and the high ticket makes the target reachable. **Score 8.**

## S2 — Bilingual Toolbox Talks

**Upfront:** $15–29 setup + ~30 listings $6 + $12 domain = **$33–47**.
**Per sale:** $24 pack nets **$21.27** on Etsy, $4 single nets **$3.17** (the fixed fees eat 21%), and $49 bundle nets $43.90. On Gumroad direct, a $24 pack nets ~$20.10 after card fees. The **$9/mo subscription nets $8.00** on Lemon Squeezy, where the $0.50 fixed fee costs 11%; $79/yr nets $6.18/mo. Etsy blend (50% singles / 40% packs / 10% bundles) is **$14.48**.
**Fixed:** ~$2.50. Resend Pro ($20) is needed once the Sunday send passes 100 subscribers.
**Tokens:** the **M1 build is ~$220**: 312 bilingual talks, an OSHA cross-check and a second-pass Spanish review. The ideator ignored this. After that, ~$90/mo.
**Needed:** 21 Etsy orders or 38 subs for $300.

| Month | Net revenue $ | Fixed $ | Op. tokens $ | Monthly net $ | Cumulative $ |
|---|---|---|---|---|---|
| M0 (upfront) | – | – | – | -47 | -47 |
| M1 | 14 | 2 | 220 | -208 | -255 |
| M2 | 58 | 2 | 90 | -35 | -290 |
| M3 | 95 | 2 | 90 | 2 | -287 |
| M4 | 117 | 2 | 90 | 25 | -262 |
| M5 | 162 | 2 | 90 | 70 | -193 |
| M6 | 207 | 2 | 90 | 115 | -78 |

Over months 7–12 it reaches 12–14 orders plus 8–15 subs (~$250–300/mo). It is **operating-positive in M3**, pays back in **M7** and **hits $300 around M13** as spring construction peaks. Drop the $4 singles or raise them to $5–6. **Score 7.**

## S3 — Custom wedding toasts and eulogies

**Upfront:** $15–29 setup + $2.40 listings + $12 domain = **$29–43**.
**Per sale:** $29 standard → Etsy $3.21 + ~$0.80 of tokens per order (questionnaire synthesis, self-critique, revision) and some Offsite Ads = **≈$24.50**. $49 nets ~$42 and $39 eulogy ~$33.60. Blend **≈$26**.
**Fixed:** ~$1.50.
**Tokens:** ~$90/mo; M1 build ~$80 (simple pipeline).
**Needed:** **12 orders for $300; 4 to cover tokens.**

The October launch is off-season; eulogies and retirement toasts carry Nov–Feb, and wedding-speech demand climbs from March for May–September weddings.

| Month | Net revenue $ | Fixed $ | Op. tokens $ | Monthly net $ | Cumulative $ |
|---|---|---|---|---|---|
| M0 (upfront) | – | – | – | -43 | -43 |
| M1 | 26 | 2 | 80 | -56 | -98 |
| M2 | 52 | 2 | 90 | -40 | -138 |
| M3 | 78 | 2 | 90 | -14 | -152 |
| M4 | 78 | 2 | 90 | -14 | -165 |
| M5 | 104 | 2 | 90 | 12 | -152 |
| M6 | 156 | 2 | 90 | 64 | -88 |

Months 7–12 reach 9–14 orders/mo (spring/summer weddings). It is operating-positive in **M5**, pays back in **M7** and reaches $300 in **M8**, then drifts down in autumn. This is the lowest build cost in the batch with a high per-order margin. The risk is conversion, given AI disclosure and a weak moat, not the arithmetic. **Score 8.**

---

### Sources (fees checked 2026-10-06)
- Lemon Squeezy fees and surcharges: https://www.swell.is/content/lemon-squeezy-pricing , https://resources.rework.com/tools/billing-revenue/paddle-vs-lemon-squeezy
- Etsy 2026 fees and setup fee: https://checkoutpage.com/blog/etsy-fees , https://www.thecraftmap.com/blog/etsy-shop-setup-fees
- Apify pay-per-event profit formula: https://docs.apify.com/platform/actors/publishing/monetize/pay-per-event ; Apify plans: https://automationatlas.io/answers/apify-pricing-explained-2026/
- Clover developer share: https://clover.com/developers
- Substack + Stripe fees: https://schoolmaker.com/blog/substack-pricing
- Gumroad fees: https://checkoutpage.com/blog/gumroad-fees
- Resend free-tier limits: https://automationatlas.io/answers/resend-free-tier-explained-2026/
- Twilio A2P 10DLC fees: https://www.ghlscaleup.com/blog/a2p-10dlc-fees-explained
- TPT seller fees: https://www.tpt.it.com/fees/
- Image API pricing: https://pricepertoken.com/gpt-image-pricing , https://pricepertoken.com/image
- Jobber App Marketplace revenue share: not publicly documented (searched; developer.getjobber.com)
