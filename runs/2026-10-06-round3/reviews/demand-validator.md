# Demand Validator: Round 3 (2026-10-06, capital allowed)

_Reviewer: demand-validator. Inputs: `../PARAMS.md` (which overrides the defaults), `operator-constraints.md`, `scoring-rubric.md`, `lessons-learned.md`, and the 10 briefs (Q1–Q3, B1–B3, P1–P3, U5)._

**Conventions**
- Day 0 is Tue 2026-10-06. Every "days to answer" figure counts from today.
- Sponsor time is priced at **$300/h**.
- **"Capital at risk"** means cash spent or committed **before the go/no-go decision**. Capital that is released only after a pass is listed separately.
- Testability is the first tie-breaker. It is not part of the composite.

## Summary

| ID | Idea | Testability | Test type | Pass threshold | Days to answer | Cost $ / human hrs (capital at risk before go/no-go / sponsor h at $300) |
|---|---|---|---|---|---|---|
| Q1 | UltraWideo-class extension acquisition | **7** | Non-binding price indication first, then DD on read-only data. No money moves before go | Seller engages at **≤ $3,300 cash at close** (plus an optional earn-out paid only on gross above $390/mo) by Oct 13. Then all 9 DD gates pass by Oct 30 | 7 (price) / 24 (DD) | **$0** / 1.25 h (**$375**) |
| Q2 | Wheel of Life-class app acquisition | **6** | Same as Q1, with a hard Dec 1 close date | Seller engages at **≤ $4,100 cash** by Oct 13. By Nov 6: recurring proceeds ≥ $380/mo and lifetime purchases < 40% of TTM, both verified from App Store Connect and Play exports | 7 / 31 | **$0** / 1.5 h (**$450**) |
| Q3 | Standing ≤ $3k fire-sale buy order | **7** | Free deal-flow screen, then DD gates on each deal | By Nov 5: ≥ 2 listings pass every desk gate **and** ≥ 1 seller grants read-only revenue access. One extension to Dec 5 | 30 (60 max) | **$0** / 0.5 h (**$150**). Each deal pursued adds 5 h ($1,500) |
| B1 | HSK 3.0 speaking mock | **6** | Refundable $29 pre-order. Capped Google Search + Reddit test | ≥ 12 stranger pre-orders at blended CAC ≤ $22 with ≥ $250 spent, by Oct 30 | 24 | **$362** / 2.5 h (**$750**) |
| B2 | SubWatch (GC sub OSHA monitoring) | **4** | Free instant check, then card-on-file trial. Capped Google Search | CPL ≤ $50 on ≥ 10 business-domain free checks by Oct 28; ≥ 2 card-on-file trials by Nov 13; ≥ 1 paid by Nov 20 | 45 | **$512** / 2 h (**$600**) |
| B3 | Heirloom recipe-card cookbook | **5** | Real $119 orders, delivered whatever the verdict. Capped Meta + Google test | ≥ 10 stranger orders at CAC ≤ $47 by Nov 8 | 33 | **~$820** / 4 h (**$1,200**) |
| P1 | Merchant-loaded ATMs | **4** | Signed conditional placement plus verified withdrawal volume, then a 1-ATM pilot with kill rules | By Nov 20: ≥ 3 signed conditional placements, ≥ 1 of them verified at ≥ 150 withdrawals/mo. Pilot: ≥ 150/mo in months 2 and 3 | 45 (buy) / ~120 (pilot) | **$205** / 0.75 h (**$225**). Pilot adds ~$2.4k; max pilot loss ~$1.3–1.6k |
| P2 | Power-bank rental stations | **5** | Signed venues plus a staff tally, then the sample station doubles as pilot #1 | By Oct 30: ≥ 4 signed venues and ≥ 2 tallying ≥ 3 charge requests/night. Sample station: ≥ 25 paid stranger rentals in its first 30 days (~Dec 6) | 24 / ~61 | **$110** / 0.5 h (**$150**) before any hardware. **$510** / 2.5 h (**$750**) before the pilot order |
| P3 | PlacementDesk (location sourcing) | **5** | Host intake first, then written lead acceptance by operators, then a paid install | ≥ 4 qualified host intakes by Nov 10; ≥ 2 leads accepted in writing by Nov 20; ≥ 1 install by Dec 20; first invoice paid by ~Jan 4 | 45 / 90 | **$180** / 1 h (**$300**) |
| U5 | Owned vending, outsourced restocking | **3** | Signed conditional placement plus verified gross plus a written restock quote, then 1 used machine | By Nov 20: a location with verified gross ≥ $1,300/mo and a restock quote ≤ $35/visit. Pilot: ≥ $1,100/mo gross in months 2–3 | 45 / ~150 | **$125** / 0.5 h (**$150**). Pilot adds ~$3.4k; max pilot loss ~$2k (fails P10) |

**Ranking by testability:** Q1 = Q3 (7) > Q2 = B1 (6) > B3 = P2 = P3 (5) > B2 = P1 (4) > U5 (3).

**What it costs to run everything.**
- Running all ten tests to their first go/no-go would put about **$2.7k of capital** at risk.
- It would also take about **16.5 sponsor hours (~$4,950)**.
- So in this run, **sponsor time, not capital, is the bigger pre-commitment cost.** Run the tests in sequence, not all at once.

### This week (Oct 6–12), in this order
1. **Today, $0, AI only.**
   - Start the Q3 deal screen.
   - Q1 desk checks: 12-month weekly-user history for UltraWideo from public extension-stats sites, and a 90-day clone audit.
   - Q2 clone audit.
2. **Q1 + Q2 price indications (sponsor 0.5 h).** The AI drafts both; the sponsor sends them through TrustMRR.
   - The multiple is the binding constraint, so price goes first.
   - Expect "no" from both sellers within a week. That answer costs $150 instead of ~$2k of DD time.
3. **B1 and B3: seasonal, so start now or wait a year.**
   - B1: Gate 0 (specs and keyword forecast) by Oct 8.
   - B3: Lulu samples ordered by Oct 10.
4. **P1 and P2: Q4 is their good season.** Build the scored lists and send Lob wave 1 by Oct 13.
5. **Defer B2, P3 and U5 to January.**
   - B2: the test is underpowered and not seasonal.
   - P3 and U5: Q4 is the slow season for host decisions (P3's own brief says so).
   - If one of them must run now, run **P3's host wave as U5's location test**. They target the same workplaces, so running both burns the same list twice.

### Platform and channel concentration
- **Google Ads advertiser verification:** B1, B2 and B3 all run on the sponsor's verification. B2 having its own account does not isolate it, because a verification-level suspension follows the person. Run at most two of the three.
- **Lemon Squeezy:** B1, B2 and possibly Q1 sit on it. Confirm it still accepts new stores during the Stripe Managed Payments transition. If not, use Stripe Managed Payments.
- **Lob:** P1, P2, P3 and U5 share one account. Give each idea a separate prospect segment so that no business receives two of our offers:

  | Idea | Segment |
  |---|---|
  | P1 | Salons, barbers, cash-only shops |
  | P2 | Bars, breweries, bowling alleys |
  | U5 / P3 | Workplaces with 50+ staff |

## Rules that apply to every test
1. **Only strangers count.**
   - Every checkout and intake form carries a source tag.
   - Purchases or sign-ups from the sponsor's contacts, partners' staff and operator test accounts are logged but not counted.
   - For physical ideas, "stranger" means a business with no prior relationship to the sponsor.
2. **Automatic refunds.** Where delivery is deferred, a scheduled job refunds every undelivered order on the stated date through the payment API, with no customer action needed. Test it with a $1 order before launch.
3. **No fake scarcity and no invented proof.** No countdowns, no "only N left", no invented reviews or counts. Ad creatives show real products only (B3: real sample books).
4. **Spend caps are enforced by the platform, not by the AI's discipline** (the Project Vend lesson).
   - Set account-level budget limits on Google Ads and Meta.
   - Physical purchases above $200 need the sponsor's approval.
   - Each scale tranche is released only after the sponsor reads the verdict file.
5. **Pre-commit the verdict.**
   - The operator writes the thresholds into `runs/2026-10-06-round3/tests/<ID>.md` before launch.
   - It records the result on the verdict date.
   - Moving the goalposts counts as a fail.
6. **No money moves on an acquisition before every DD gate passes.**
   - All revenue claims must be checked against data pulled by the buyer: read-only access, or an export sent straight from the platform. Seller screenshots don't count.
   - Each close includes an escrow holdback with stated release conditions.

---

## Q1: UltraWideo-class aged extension · Testability 7

**What's wrong with the brief's test.**
- The DD gates are good, but they are tested in the wrong order. Q1 fails PARAMS on **price**, not on revenue. Yet the brief spends ~6 sponsor hours of DD before learning whether the seller will move from $13k toward a gate-compliant number.
- The "trailing 6-month gross ≥ $400" gate is flattered by the May–Jun spike ($700–764). It also uses gross revenue, which mixes annual-plan lumps with recurring revenue.
- The brief also takes the billing-transfer answer from the seller. The only acceptable source is Lemon Squeezy itself, which publishes multi-store docs but no documented store-ownership transfer.

**The test**
- **Step 1, price indication (by Oct 13).** The AI drafts a non-binding indication and the sponsor sends it:
  - **≤ $3,300 cash at close.** This is 12 × $290 P50 net, less escrow and domain fees. If one-time sponsor hours count against payback, the figure is ≤ ~$1,500.
  - **Optional earn-out:** 50% of monthly gross **above $390** for 18 months, capped at the ask. It pays the seller only if their May–Jun story repeats, so it doesn't hurt P50 payback.
  - **Pivot:** the seller counters at $3.3–6.5k. That only passes if the committee relaxes payback to 24 months.
  - **Fail:** a counter above $6.5k. Walk away.
- **Step 2, DD gates (by Oct 30). Every gate must pass.**
  1. Read-only Lemon Squeezy API data reconciles to TrustMRR within 5%.
  2. MRR is ≥ $320 at LOI.
  3. Monthly subscription churn is ≤ 8% over 6 months, and annual renewals are ≥ 40%.
  4. Jul–Sep gross averages ≥ $400/mo. It is ~$474 today, so this passes.
  5. Chrome Web Store weekly users are ≥ 65k and within ±10% over 12 months.
  6. The billing route is confirmed **in writing by Lemon Squeezy or Stripe**. If the only route is re-subscribing customers on Stripe, cut the price by 25%.
  7. The CWS transfer form is accepted, with no policy strikes in the last 24 months.
  8. A clean CI build passes a smoke test on Netflix, YouTube and Prime.
  9. Fewer than 5 same-pitch clones launched in the last 90 days have more than 1k users each.
- **Close terms:** 20% of the price is held in escrow for 45 days. It is released if active subscriptions are ≥ 110 and both store listings have transferred.
- **Post-close kill rule:** if MRR is below $220 at month 3, list the asset for resale.
- **Capital at risk before go:** $0. **Sponsor time:** 1.25 h ($375). The lawyer's APA review (~$300–500, assumed) comes only after go.
- **Does NOT prove:** churn after the billing migration; whether the summer spike repeats; MV3 or permissions policy risk; whether the AI's conversion work lifts revenue.

## Q2: Wheel of Life-class mobile app · Testability 6

**What's wrong with the brief's test.**
- The listing's numbers show that most revenue is **not recurring**:
  - MRR is **$181**, but the last 30 days brought in **$552**, and the January spike is ~$1,000/mo.
  - That points to annual and lifetime purchases. The brief's "lifetime < 40% of TTM" gate will probably bind, and it should be checked first, not last.
- The TrustMRR page is ambiguous on whether figures are gross or proceeds. Only App Store Connect "Proceeds" and Play earnings reports settle that.
- Starting D-U-N-S and developer enrolment on day 0 spends sponsor hours before price is known.

**The test**
- **Step 1, price indication (by Oct 13).**
  - **≤ $4,100 cash at close.** This is 12 × $370, less fees, or ≤ ~$1,700 if sponsor setup hours count.
  - **Optional earn-out:** 50% of gross above $550/mo for 18 months.
  - **Pivot:** a counter of $4.1–8k, which only works if the committee relaxes the gate.
  - **Fail:** a counter above $8k.
- **Step 2, DD gates (by Nov 6, so that the deal can close by Dec 1 and capture the New Year peak).**
  - Trailing 6-month **proceeds** are ≥ $380/mo.
  - Lifetime purchases are < 40% of TTM.
  - At least 40% of the Jan-2025 annual cohort renewed in Jan 2026.
  - Active subscriptions are ≥ 110.
  - A fresh Android build passes on Linux CI, and an iOS archive builds on a macOS CI runner.
  - Both stores confirm the app is eligible to transfer. Check Apple's caveats for Sign in with Apple, iCloud containers and App Groups.
  - The RevenueCat project can be transferred.
- **Close terms:** 15% holdback through Jan 31, released if active subscriptions are ≥ 110.
- **Sequencing:** developer accounts start **only after** the price gate passes. Individual Apple enrolment avoids the D-U-N-S wait.
- **Capital at risk before go:** $0. **Sponsor time:** 1.5 h ($450).
- **Does NOT prove:** that the January peak repeats; ratings after the first update under new ownership; that the buyer can keep up with Apple's recurring 2FA and agreement prompts.

## Q3: Standing fire-sale buy order · Testability 7

**What's wrong with the brief's test.**
- "≥ 3 candidates/month pass a desk screen" is too easy to pass, because desk screens read seller-reported numbers.
- The brief admits its P10 is −63%, yet it leaves the buy-box loose.
- It also names a 48-hour sponsor response window but doesn't prepare for it.

**The test**
- **Week 0 (sponsor 0.25 h):**
  - Complete Escrow.com KYC.
  - Pre-approve the buy-box and a template LOI, so that a qualifying offer can go out within 24 h on a 0.1 h approval.
- **Tightened buy-box, to bring P10 under 50%:**
  - ≥ 18 months of API-verified history;
  - LLM/API COGS ≤ 10% of revenue;
  - the asset is a marketplace placement (CWS, AMO, App Store/Play, WP.org);
  - 6-month MRR slope no worse than −10%;
  - all-in price ≤ $2,750 and ≤ 0.5× TTM revenue;
  - 20% holdback for 30 days;
  - the asset nets ≥ $250/mo, so year 1 covers the $1,500 of per-deal sponsor time.
- **Sources:** daily reads of public listing pages on TrustMRR `/acquire`, Microns and Flippa, within each site's terms. Use the platforms' own email alerts where they offer them.
- **Thresholds:**

  | Result | Condition |
  |---|---|
  | Pass (by Nov 5) | ≥ 2 listings pass every desk gate **and** ≥ 1 seller grants read-only revenue access |
  | Pivot | Exactly 1 desk-qualified listing. Extend once, to Dec 5 |
  | Fail | 0 by Dec 5. Shelve the idea and keep the capital in T-bills |

- **Capital at risk:** $0. **Sponsor time:** 0.5 h ($150) to the verdict. Each deal pursued costs about 5 h ($1,500).
- **Does NOT prove:** the quality of any individual asset; seller honesty beyond the API data; whether an AI screen beats faster human buyers to the same fire-sales.

## B1: HSK 3.0 Speaking Mock · Testability 6

**What's wrong with the brief's test.**
- The pass rule is internally inconsistent. "≥ 8 pre-orders at CAC ≤ $22" uses only $176 of a $300 budget, so it doesn't say what happens to the rest.
- It spends $250 on the native contractor **before** the verdict.
- It never checks whether the keywords carry enough volume to spend the budget. The P50 needs ~470 paid clicks/mo, which is roughly 6–7k impressions.
- The first official HSK 3.0 sitting is reported as **13 Dec 2026** (hsklord), but other sources say July. Verify it on chinesetest.cn.

**Gate 0 (by Oct 8, $0)**
- The official L3–L6 speaking-task format is published.
- The Keyword Planner forecast for the keyword set in the target countries is **≥ 3,000 impressions/mo**.
- If either fails, kill B1 at $0, or keep it affiliates-only.

**The test**
- **Offer:** "HSK 3.0 Speaking Mock, Level 3 or 4: 5 timed mocks in the official task order, per-syllable tone report." $29.
  - Refundable pre-order, delivery by Nov 13 (a month before the Dec 13 sitting).
  - Automatic refund on Oct 31 if the test fails.
- **Assets:** landing page, one free demo task (native QA ~2 h, $50), checkout. About 2 operator-days.
- **Traffic:**
  - Google exact and phrase match: $200.
  - Reddit community-targeted ads: $100.
  - Expect ~350–450 clicks from Oct 16 to Oct 30.
- **Thresholds (Oct 30):**

  | Result | Condition |
  |---|---|
  | Pass | ≥ 12 stranger pre-orders, blended CAC ≤ $22, ≥ $250 spent |
  | Pivot | 6–11 pre-orders, or CAC $22–30. Run $150 more on the best ad group only |
  | Fail | ≤ 5 pre-orders, CAC > $30, or less than $150 of the budget could be spent (no volume) |

- **Capital at risk:** $362 (ads $300, domain $12, QA $50). **Sponsor time:** 2.5 h ($750).
- **Does NOT prove:** off-peak demand; second-level repeat purchases; affiliate yield; whether the grading is good enough to avoid refunds.

## B2: SubWatch · Testability 4

**What's wrong with the brief's test.**
- **It is underpowered.**
  - $500 at the brief's P50 ($3.50 CPC, 10% to free check, 8% to paid) buys about **143 clicks, 14 free checks and 1.1 paying customers**.
  - The "≥ 3 trials by day 21" pass needs a 21% free-to-trial rate, about 2.6× the brief's own P50.
  - One paid conversion can't separate P50 from P10.
- **The policy risk is overstated.** The 2026-10-05 update targets ads for *acquiring* government documents, and requires authorised-provider status for those. It doesn't clearly cover information services. Keep the $0 pre-check anyway.
- **It depends on D2's ingest being built.** If it isn't, the build doubles.

**Gate 0 ($0, Oct 7–9)**
- Ads are approved in review.
- The keyword forecast is ≥ 2,000 impressions/mo after negatives. Many "OSHA violations by company" searchers are workers, not GCs.

**The test**
- **Offer:** a free "check 5 subs" instant report, email-gated. Then a 14-day trial of "Monitor your list" at $79/mo, card on file.
- **Traffic:** Google Search, $500, Oct 14 to Nov 13. Import the campaign to Bing at no extra budget.
- **Thresholds:**

  | Result | Condition |
  |---|---|
  | Pass | CPL ≤ $50 on ≥ 10 free checks from business email domains by Oct 28, **and** ≥ 2 card-on-file trials by Nov 13, **and** ≥ 1 paid by Nov 20 |
  | Pivot | CPL passes but 0–1 trials. Add a one-off $49 "prequal pack" PDF and re-test with $200 |
  | Fail | CPL > $80 at $250 spent, or fewer than 5 free checks at $500 |

- **Capital at risk:** $512. **Sponsor time:** 2 h ($600).
- **Does NOT prove:** the 4% churn assumption; the LTV of $1,598; that the CAC holds above ~$600/mo of spend. Sample size is the big caveat: **passing still leaves a wide CAC range.**

## B3: Heirloom Recipe-Card Cookbook · Testability 5

**What's wrong with the brief's test.**
- **"Fail and refund-on-request" breaks the rules.** A buyer who has already given the certificate as a gift can't sensibly be refunded. The fix: **every order taken is delivered**, so the pipeline and proof flow must work before ads go live. A kill stops ad spend, not fulfilment.
- **The Meta setup can't learn.** $300 on a new pixel can't take Advantage+ out of its learning phase. Use a manual sales campaign and judge it on cost per purchase anyway.
- **The Christmas promise is unverified.** Check the "upload by Nov 20, book under the tree" date against Lulu's 2026 holiday production calendar before it goes in any ad.

**The test**
- **Offer:** "Grandma's recipe cards, turned into a hardcover heirloom cookbook." $119, with US shipping included.
  - Shown with photos of real printed samples.
  - Delivery dates stated: books in time for Christmas if cards are uploaded by Nov 20 (once Lulu's calendar confirms it); otherwise about 3 weeks after upload.
- **Assets:**
  - the upload, transcription, proof and Lulu API pipeline (~4 operator-days);
  - 3 sample books, ordered by Oct 10;
  - a photographer shoot around Oct 21.
- **Traffic:** Meta $300 and Google $200, Oct 22 to Nov 8. That is about 410 clicks.
- **Thresholds (Nov 8):**

  | Result | Condition |
  |---|---|
  | Pass | ≥ 10 stranger orders at CAC ≤ $47. Release the $1,500 tranche |
  | Pivot | 6–9 orders. Change one creative or the offer, spend $250 more by Nov 16 (before BFCM), and re-judge |
  | Fail | ≤ 5 orders, or 0 orders after $250 |

  There is also a quality gate: ≥ 80% of the first proofs are approved within 2 revision rounds.
- **Capital at risk:** ~$820 (samples $135, photographer $150, domain $12, permit ~$25, ads $500). **Sponsor time:** 4 h ($1,200).
- **Does NOT prove:** CAC at BFCM CPMs; certificate redemption; Mother's Day repeat orders; copy orders from relatives.

## P1: Merchant-loaded ATMs · Testability 4

**What's wrong with the brief's test.**
- **"≥ 80 customers/day" from Google popular times plus a till photo is not withdrawal volume.**
- **A free, cancel-anytime signature costs the merchant nothing,** so it is a weak commitment.
- **The processor and state registration are bought before any merchant has said yes,** which wastes ~2.5 sponsor hours if nobody signs.

**The test**
- **Step 1, outreach and verification (by Nov 20).**
  - Lob postcards go to 300 scored salons, barbers and cash-only businesses: $185.
  - The offer: "Free ATM. You keep 40% of each surcharge."
  - **Conditional placement agreement:** subject to processor approval and equipment, with no obligation on our side. The merchant commits to:
    - vault cash ≥ $2,000;
    - a 24-month term;
    - a $300 removal fee if it cancels in year 1.
  - **Volume must be verified** by either:
    1. processor statements from an ATM removed within the last 12 months; or
    2. a 14-day staff tally on a QR form of cash requests and customers who leave to get cash, averaging **≥ 6/day**.
- **Step 1 thresholds:**

  | Result | Condition |
  |---|---|
  | Pass | ≥ 3 signed and ≥ 1 verified at ≥ 150 withdrawals/mo. Then the sponsor does the processor application, insurance and state check (2.5 h) and buys 1 refurbished unit |
  | Pivot | Signed, but verified only at 100–149/mo. Tally a second location |
  | Fail | < 2 signed by Nov 13, or nothing verified at ≥ 100/mo by Nov 20 |

- **Step 2, pilot kill rules:**
  - < 75 withdrawals in month 2: relocate once (~$300).
  - < 75 after the relocation: sell the unit.
  - Buy unit 2 only after ≥ 150/mo in two consecutive months.
- **Capital at risk before buying:** ~$205. **Sponsor time:** 0.75 h ($225).
  - The pilot adds ~$2.4k. Its maximum loss is ~$1.3–1.6k, which is at the PARAMS 50% edge.
- **Does NOT prove:** that tallies convert to paid withdrawals at $3.25; merchants' reliability at loading cash; the long-run decline in cash use.

## P2: Power-bank rental stations · Testability 5

**What's wrong with the brief's test.**
- **It waits for a production order (around day 45) before measuring the one unknown:** rentals per station at small US venues.
- **The express sample station is bought anyway, but it is used only for a bench test.**
- **The pass bar is too low to hit target.** At 20 rentals/mo the full fleet nets ~$250/mo after depreciation, below the $300 target. The bar needs to be ≥ 25.

**The test**
- **Gate 0 ($0):**
  - The OEM's FCC and UL certificates and its platform terms are checked.
  - Payments settle in the sponsor's Stripe account.
- **Stage A, venues (by Oct 30).**
  - Lob and email go to 150 bars, breweries and bowling alleys ($92).
  - Signed venues get a free, cancel-anytime placement.
  - Staff at each signed venue tally "can you charge my phone?" requests for 7 nights on a QR form.
  - **Pass:** ≥ 4 signed venues, ≥ 2 of them tallying ≥ 3 requests/night.
  - **Fail:** < 2 signed. Kill at ~$110.
- **Stage B, sample station as pilot #1.**
  - The sample goes into the best-tallying venue by about Nov 6. Before that, the sponsor sets up Stripe and the OEM account, insurance and the sales-tax permit (2 h).
  - **Thresholds (30 days live, ~Dec 6):**

    | Result | Condition |
    |---|---|
    | Pass | ≥ 25 paid stranger rentals. Order 2 more stations |
    | Pivot | 10–24 rentals. Relocate once by mail and re-run 30 days |
    | Fail | < 10 after the relocation. Stop; the loss is ~$450 |

  - Keep the brief's rule of 2 consecutive months at ≥ 20 rentals before buying the full fleet.
- **Capital at risk:** ~$110 and 0.5 h ($150) before any hardware; ~$510 and 2.5 h ($750) before the pilot order.
- **Does NOT prove:** non-return and chargeback rates at scale; summer seasonality; how long venues keep the stations.

## P3: PlacementDesk · Testability 5

**What's wrong with the brief's test.**
- **Operators first means pitching an abstract offer cold.** Lesson 14 sets the yes-rate at 5–10%, so "≥ 2 of 25" is a coin flip, and it costs 1.5 sponsor call-hours before any lead exists.
- **Paying for a lawyer and calls up front inverts the risk.**

**The test**
- **Step 0 ($0).** The AI lists operators and ATM ISOs in the metro that **publish** referral or locator payouts in writing. Those are buyers who have already committed, and need no call.
  - The legal analyst also clears the FTC Business Opportunity Rule and the real-estate-licence questions before any agreement.
- **Step 1, host wave (by Nov 10).** 200 Lob postcards go to workplaces with 50+ staff, laundromats and gyms ($122).
  - **Pass:** ≥ 4 qualified host intakes.
  - **Fail:** < 2. Kill at ~$180.
- **Step 2, operator acceptance (by Nov 20).** The sponsor calls operators **with the leads in hand** (1 h).
  - **Pass:** ≥ 2 leads accepted in writing on pay-on-install terms ($150–400).
- **Step 3, cash.** ≥ 1 install by Dec 20, and the first invoice paid by about Jan 4.
  - **Pivot:** hosts are interested but operators don't act. Switch to the published-programme categories.
- **Capital at risk:** ~$180. **Sponsor time:** 1 h ($300).
- **Does NOT prove:** that installs are paid without circumvention; whether residuals arrive; whether supply holds beyond the first few hosts. Q4 is slow for host decisions, so expect the verdict to slip into January.

## U5: Owned vending, outsourced restocking · Testability 3

**What's wrong with the brief's test.**
- **There is no volume gate and no restocking quote,** and those decide the outcome.
- **Break-even arithmetic (assumed: COGS 45%, commission 10%, card fees ~5%, telemetry $25, weekly restock $35, insurance and repairs $40):**
  - net ≈ 0.37 × gross − $217;
  - a 12-month payback on ~$3.4k needs **gross ≥ ~$1,300/mo**;
  - 2026 route averages are cited at $400–700 per machine, so **expect most locations to fail.** That is the point of testing before buying.

**The test**
- **Path A, a new placement.**
  - Send 200 Lob postcards to workplaces with 100+ staff on site ($122).
  - Pass to buy requires all of:
    - a signed conditional placement: commission ≤ 10%, 12-month term, we can exit on 30 days' notice;
    - **verified gross ≥ $1,300/mo**, from 3 months of the host's commission statements from its current operator (a commission cheque implies gross);
    - a written restocking quote of ≤ $35 per weekly visit, from a contractor or a route operator;
    - a cleared licence and health-permit check.
- **Path B, buy a machine already in place.** Requires read-only telemetry access (Nayax or Cantaloupe) showing ≥ 3 months at ≥ $1,300/mo, plus the host's written consent to the assignment.
- **Thresholds:**

  | Result | Condition |
  |---|---|
  | Pass | Either path qualifies by Nov 20 |
  | Pivot | Verified gross $1,000–1,299/mo. Proceed only if the machine costs ≤ $1,800 used |
  | Fail | Nothing qualifies by Dec 20 |

- **Pilot kill rules:** gross < $700 in month 2 means relocate once; < $700 after that means sell. Scale only after 2 consecutive months at ≥ $1,100.
- **Capital at risk:** ~$125. **Sponsor time:** 0.5 h ($150).
  - The pilot adds ~$3.4k. Its maximum loss is ~$2k (~59%), which **exceeds the P10 limit** unless the machine is bought at ≤ $1,800.
- **Does NOT prove:** that the restocker turns up reliably; theft and spoilage; that the AI's pricing avoids Project Vend-style losses.

---

## Sources (accessed 2026-10-06)
- [hsklord: HSK 3.0 test dates 2026](https://hsklord.com/blog/hsk-3-0-test-dates-2026) (first official sitting reported as 13 Dec 2026)
- [studycli: The new HSK](https://studycli.org/learn-chinese/the-new-hsk) (speaking integrated from Level 3)
- [University of Glasgow Confucius Institute: HSK 3.0 trial exam](https://www.gla.ac.uk/explore/confucius/whatson/headline_1284976_en.html)
- [TrustMRR: UltraWideo](https://trustmrr.com/startup/ultrawideo) and [TrustMRR: Wheel of Life](https://trustmrr.com/startup/wheel-of-life)
- [Lemon Squeezy docs: multiple stores](https://docs.lemonsqueezy.com/help/your-account/multiple-stores) (no documented store-ownership transfer found)
- [Fungies: Lemon Squeezy, Stripe Managed Payments migration](https://fungies.io/lemon-squeezy-stripe-acquisition-saas-founders-2026/)
- [Chrome Web Store: register your developer account](https://developer.chrome.com/docs/webstore/register) (item transfer form)
- [Google Ads: government documents and services policy](https://support.google.com/adspolicy/answer/13156083) and [TechWyse: Oct 2026 update](https://www.techwyse.com/news/platform-updates/google-ads-government-documents-services-policy-update-october-2026)
- [Lulu Jr: holiday production delays](https://blog.lulujr.com/holiday-shopping-production-delays/) (allow at least 2 weeks)
- [FTC Mail Order Rule and the Fashion Nova settlement (Manatt)](https://www.manatt.com/insights/newsletters/advertising-law/ftc-reaches-9-3-million-settlement-with-fashion-no)
- [vmfsusa: vending revenue per machine](https://vmfsusa.com/blogs/starting-your-vending-business/how-much-can-a-vending-machine-really-make) and [Gitnux: vending profit statistics 2026](https://gitnux.org/vending-machine-profit-statistics/) (route averages of $400–700 per machine; seller-biased sources)
