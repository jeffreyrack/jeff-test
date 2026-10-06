# Investment Committee Report: run 2026-10-06, round 3 (capital allowed)

_Chair: investment-committee. Decision date: Tue 2026-10-06._

_Inputs:_
- _`runs/2026-10-06-round3/PARAMS.md`, including the sponsor rulings;_
- _idea files `ideas/acquirer.md` (Q1–Q3), `media-buyer.md` (B1–B3), `physical-operator.md` (P1–P3) and `user.md` (U5);_
- _reviews from the sales-skeptic, market-analyst, autonomy-auditor, legal-risk-analyst, unit-economics-analyst and demand-validator;_
- _the reference files `operator-constraints.md`, `scoring-rubric.md` and `lessons-learned.md`;_
- _round 2's `REPORT.md` §7–8._

> **Orchestrator note:**
> - Sections 1–6 are the committee's report as returned. The committee scored against rulings 1–2.
> - **Sponsor ruling 3** (break-even after all costs replaces the $300/mo target) arrived while the committee was running. Its effect is applied in **§7** below.
> - Ruling 3 does not change the picks.

---

## 1. Executive summary

1. **No idea in round 3 clears the $300/mo net target at P50 with acceptable risk.** (See §7: under ruling 3 the target is break-even, and B1 meets it.) The committee scored 12 rows: 10 ideas, with U5 split into ×1/×2/×3. Composites run from 2.95 to 5.70. The best are **B3 (5.70)** and **B1 (5.55)**, and only those two pass the hard gates, and only as staged tests where capital is released after a pass.
2. **Nothing beats earlier picks on composite** (M3 6.70, M1 6.65, D2 6.20, T2 5.95). But every one of those is dead, dropped or never validated, and B2's review found live clones that also undercut D2.
3. **Sponsor rulings.**
   - Ruling 2 (operating basis) moves the sponsor-time gate for Q1 (to borderline), Q2 (to pass) and Q3 after close (to pass).
   - Ruling 1 (24-month payback) rescues no acquisition at a price the seller is likely to accept. It only makes Q3's run-rate payback pass, and Q3 still fails P10 and P50.
4. **Highest prices that pass the 24-month rule.** Basis: P50 cash net after recurring sponsor hours; one-time setup hours are charged to year-1 profit, not to payback.
   - **Q1: about $2.7k cash** (about $3.3k all-in), against a $13k ask.
   - **Q2: about $4.9k cash** if the $6,648 TTM is proceeds after store fees, which is the committee's reading; about $3.2k if it is gross. The ask is $11,111.
   - An earn-out paid only on revenue above the P50 baseline can sit on top.
   - If setup hours were also loaded into payback, Q1 has no passing price and Q2's ceiling falls to about $1–2k.
5. **Pick 1: B1, HSK 3.0 Speaking Mock.**
   - Gate 0 costs $0 and reports by Oct 8.
   - Then a $362 refundable pre-order test, with the verdict on Oct 30.
   - It ranks first by the testability tie-break (6 vs 5). Founder fit also favours it.
6. **Pick 2: B3, Heirloom Cookbook.**
   - An $820 test with ads live **by Oct 22 (hard seasonal deadline)** and a verdict on Nov 8.
   - It must run on Meta + Microsoft Ads, not Google, so it shares no ad or payment account with B1.
7. **Parallel $0 options (about 0.5 h of sponsor time):**
   - Q2 and Q1 price indications by Oct 13 at the ceilings above;
   - Q3 as an AI-only screen with a tighter buy-box.
8. **Rejected:** Q1, Q2, Q3, B2, P1, P2, P3, U5×1/×2/×3. All four physical ideas fail payback or P10 at 1–3 units.
9. **Total programme:** about $1.2k of capital at risk and about 8–9 sponsor hours (about $2.5k) over 30 days. If you fund only one, fund B1. Run B3 only if you can give it about 5 hours before Oct 22.

---

## 2. Scoreboard

`composite = 0.30·Sale + 0.20·Market + 0.20·Autonomy + 0.15·UnitEcon + 0.15·Legal`. Reviewer scores are used as given.

Worked example, B3: 0.30·6 + 0.20·6 + 0.20·6 + 0.15·4 + 0.15·6 = 1.80 + 1.20 + 1.20 + 0.60 + 0.90 = **5.70**.

Where each column comes from:

| Column | Source |
|---|---|
| Testability | demand-validator |
| Upfront $ | unit-economics analyst (total committed) and demand-validator (at risk before the go/no-go) |
| P50/P90 | sales-skeptic, counted from today |
| Sponsor hours | autonomy-auditor's realistic estimate; per week = per month ÷ 4.33 |

U5 was scored once by every reviewer except unit economics (which scored all three variants 1), so all U5 rows are identical.

| # | ID | Idea | Sale | Mkt | Auto | UE | Legal | **Composite** | Testability | Upfront $ total / at risk before verdict | P50 / P90 days | Sponsor h setup / per wk | Primary platform / account | Gate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | B3 | Heirloom recipe-card cookbook | 6 | 6 | 6 | 4 | 6 | **5.70** | 5 | 2,322 / ~820 | 26 / 75 | 6 / 0.14 (0.35 Nov–Jan) | Meta + Stripe + Lulu (Google moved to Microsoft Ads) | **PASS (staged test)** |
| 2 | B1 | HSK 3.0 speaking mock | 5 | 4 | 8 | 4 | 7 | **5.55** | 6 | 962 / 362 | 45 / never | 4 / 0.08 | Google Ads + Reddit Ads + Lemon Squeezy | **PASS (staged test)** |
| 3 | Q2 | Wheel of Life-class app | 4 | 6 | 5 | 3 | 6 | **4.75** | 6 | 8,316 at $7.5k / 0 | never (≈60–70 if accepted) / never | 13 / 0.23 | TrustMRR → App Store + Play + RevenueCat | REJECT |
| 4 | Q1 | UltraWideo-class extension | 3 | 6 | 6 | 2 | 6 | **4.50** | 7 | 8,709 at $8k / 0 | never (≈75 if accepted) / never | 12 (16–18 entity) / 0.17 | TrustMRR → CWS + AMO + Lemon Squeezy | REJECT |
| 5 | B2 | SubWatch (OSHA subs) | 3 | 4 | 6 | 2 | 6 | **4.10** | 4 | 912 / 512 | >180 / never | 5 / 0.17 | Google Ads + Lemon Squeezy | REJECT |
| 6 | P1 | Merchant-loaded ATMs | 3 | 4 | 4 | 3 | 5 | **3.70** | 4 | 6,660 (pilot 2,510) / 205 | 140 / never | 9 / 0.17 | ATM ISO/processor + Lob | REJECT |
| 7 | P2 | Power-bank stations | 4 | 4 | 3 | 2 | 4 | **3.50** | 5 | 3,220 (pilot 1,210) / 110–510 | 95 / never | 7 / 0.17–0.23 | OEM platform + Stripe + Lob | REJECT |
| 8 | Q3 | ≤$3k fire-sale buy order | 2 | 4 | 4 | 3 | 5 | **3.40** | 7 | 3,210 per deal / 0 | never / never | 9 per deal + 3 / 0.14 | TrustMRR/Microns/Flippa + Escrow.com | REJECT (kept as AI-only screen) |
| 9 | P3 | PlacementDesk | 2 | 4 | 2 | 2 | 6 | **3.00** | 5 | 575 / 180 | >180 / never | 6 / 0.58 | Lob + operator agreements | REJECT |
| 10 | U5×1 | Vending, 1 machine | 3 | 3 | 2 | 1 | 6 | **2.95** | 3 | 3,500 / 125 | 150 / never | 15 / 0.46 | Nayax/Cantaloupe + Lob | REJECT |
| 11 | U5×2 | Vending, 2 machines | 3 | 3 | 2 | 1 | 6 | **2.95** | 3 | 6,700 / 125 | 150 / never | 15 / 0.46 | same | REJECT |
| 12 | U5×3 | Vending, 3 machines | 3 | 3 | 2 | 1 | 6 | **2.95** | 3 | 9,900 (only $100 under the cap) / 125 | 150 / never | 15 / 0.46 | same | REJECT |

**Tie-breaks:**
- B3 vs B1 (gap 0.15): testability 5 vs 6, so **B1 ranks first** among the picks.
- Q2 vs Q1 (gap 0.25): testability 6 vs 7 would favour Q1, but both are gated. The Q2-first runner-up order rests on Q2's better economics (§4.5).

**Score sensitivity:**
- If Q2's revenue is proceeds (see §4.2), its UE score would plausibly rise to 4 and its composite to 4.90. That changes no rank and no gate.
- The acquisition UE scores were given under the 12-month framing. Even +1 on UE (+0.15 composite) leaves Q1 and Q2 below 5.

---

## 3. Rejected by hard gates

### 3.1 How the gates were re-applied under sponsor rulings 1–2

**Sponsor-time gate (ruling 2).**
- OP = operating profit before capital recovery and before the sponsor-hour charge: revenue − COGS − fees − contractors − tokens − maintenance.
- The gate passes if recurring sponsor h/mo ≤ OP ÷ $300. Equivalently, operating profit after the recurring sponsor charge must be ≥ $0.
- Recurring sponsor hours × $300 stay a cost for the profit target and for payback. Setup hours × $300 are charged to year-1 profit.

**Payback gate.**
- **Acquisitions with verified revenue (ruling 1):** purchase price + transaction costs ÷ P50 monthly cash net (after recurring sponsor hours) must be ≤ 24 months.
- **Other ideas above $1k:** ≤ 12 months.
- Setup hours go to year-1 profit, not payback. The ruling speaks of paying back "the purchase price", and loading setup hours into payback as well would double-count them, which is the same logic as ruling 2.

**Whose numbers were used.**
- Economics: the unit-economics analyst's, as the owner of that dimension, corrected for the Q2 proceeds finding (§4.2).
- Hours: the autonomy auditor's realistic hours, with the unit-economics hours shown where they differ.

| ID | Verdict before the rulings | Sponsor-time gate (ruling 2) | Payback gate | P10 ≤ ~50% | P50 ≤ 180 d | **Committee result** | Changed by the rulings? |
|---|---|---|---|---|---|---|---|
| Q1 | Auditor: FAIL all-cost, PASS operating. UE: FAIL (also at 24 mo) | OP ≈ $212 (UE) → 0.71 h allowed vs 0.25 (UE) – 0.75 (auditor) h → **borderline** | At $8k: 64 mo → **FAIL**. Passes only at ≤ ~$2.7k cash | At $8k: 77% → **FAIL**. At $2.7k: ~37% → pass | Never at a compliant price → **FAIL** | **REJECT** | Sponsor gate: FAIL → borderline. Overall: no change |
| Q2 | Auditor: FAIL all-cost, marginal PASS operating. UE: FAIL | OP ≈ $361 (proceeds reading) / $286 (gross reading) vs 0.4–1.0 h → **PASS** (marginal on gross reading at auditor hours) | At $7.5k: ~35 mo (proceeds) / 50 mo (gross) → **FAIL**. Passes at ≤ ~$4.9k / $3.2k | At $7.5k: ~60% / 67% → **FAIL**. At ≤$4.9k: ~41% over 12 mo → pass | Never at a compliant price (P(accept) ~10–20%) → **FAIL** | **REJECT at any price the seller is likely to accept**; re-admit if the seller accepts ≤ the ceiling | Sponsor gate: FAIL → PASS. Overall: no change |
| Q3 | Auditor: FAIL. UE: FAIL | Post-close OP ≈ $224 vs 0.6 h → **PASS**. The search phase is a capped test cost (≤ 0.5 h), not an ongoing hour | Run-rate 21.5 mo → **PASS** under ruling 1 (it failed 12) | 87% → **FAIL** (a tighter box only gets it to ~50–55%) | Never → **FAIL** | **REJECT** as a business. Keep the AI-only screen | Payback and sponsor gates flip to pass. Overall: no change |
| B1 | PASS (auditor, UE) | OP ≈ $80 avg / $155 peak (UE) vs 0.15–0.35 h → **PASS if recurring sponsor time ≤ 0.25 h/mo** | n/a (< $1k) | n/a (< $1k) | 45 d | **PASS (staged test)** | No |
| B2 | FAIL (auditor yr-1; UE) | OP ≈ $35 vs 0.25–0.75 h → **FAIL** | n/a | n/a | >180 d → **FAIL** | **REJECT** | No |
| B3 | Auditor: PASS (thin). UE: FAIL at P50 | If the test passes: OP ≈ $310 → pass. If it fails: ads stop, no ongoing hours. The failing "P50 limbo" (−$30/mo) is forbidden by the plan: scale or stop | First tranche $822 (< $1k); scale released only on a pass | 21% of committed / 59% of tranche 1 → pass under the tranche rule | 26 d | **PASS (staged test, no limbo)** | No |
| P1 | Auditor: PASS full build, FAIL pilot. UE: FAIL | 3 ATMs: OP ≈ $366 vs 0.75 h → pass. Pilot: OP ≈ $28 → **FAIL** | 31 mo run-rate / 49 mo from today vs 12 → **FAIL** | 84% of pilot → **FAIL** | 140 d | **REJECT** | No |
| P2 | FAIL (both) | Fleet: OP ≈ $153 vs 0.75–1 h self-shipped → **FAIL** (with a 3PL: OP $78 vs 0.4 h → FAIL). Pilot fails | Never / 99 mo → **FAIL** | 88% → **FAIL** | 95 d | **REJECT** | No |
| P3 | FAIL (both) | OP ≈ −$32 → **FAIL** | n/a (< $1k) | n/a | >180 d → **FAIL** | **REJECT** | No |
| U5×1/×2/×3 | FAIL (both) | OP ≈ −$80 / ~$2 / ~$85 vs 0.5–2.0 h → **FAIL** | Never → **FAIL** | 68–70% → **FAIL** | 150 d | **REJECT** | No |

**No idea breaks the $10k capital cap or the legal ≤ 3 gate.** The lowest legal score is P2 at 4. U5×3 sits $100 under the cap.

**Where the rulings changed results:**
- Ruling 2 flips the sponsor-time gate for Q1 (to borderline), Q2 (to pass) and Q3 after close (to pass).
- Ruling 1 flips Q3's payback to pass on run-rate.
- **Neither ruling changes any idea's overall verdict.**
- The ideators' own 19–26-month paybacks for Q1 and Q2 would have passed 24 months (Q2 at 19 mo), but only because they left out recurring sponsor hours, which the ruling keeps as a cost. They also used $60–70 of tokens and no legal fees.

### 3.2 Rejections in one line each

| ID | Reason |
|---|---|
| Q1 | Payback 64 mo at a realistic $8k; passes only at ~$2.7k, against a $13k ask. P10 77%. Lemon Squeezy subscriptions can't be ported. MRR down 21% in 30 days. |
| Q2 | Payback 35–50 mo at $7.5k; passes only at ≤ ~$4.9k, against an $11,111 ask, six weeks before the seller's January peak. |
| Q3 | P10 87%. Deal flow probably doesn't exist (all qualifying examples had already sold). |
| B2 | P50 > 180 d. Sponsor-time gate fails. SiteVetter already sells "SubWatch — Compliance Monitoring" at $79/mo with a free 5-sub tier. The free check gives away the unit (lessons-learned §12). |
| P1 | Payback 31–49 mo. P10 84%. Merchants with ≥ 150 withdrawals/mo are already served by ISOs. |
| P2 | Payback never. P10 88%. US small-venue utilisation unproven. Lithium liability. |
| P3 | P50 > 180 d. Sponsor-time negative: a phone-first partner channel (lessons-learned §14). |
| U5 (all) | Negative net at every size. Restocking labour is linear per machine. P10 68–70%. |

---

## 4. Top picks

### 4.1 Decision rules applied

- **Testability tie-break.** B3 (5.70, T5) vs B1 (5.55, T6) are inside the 0.3 band, so **B1 is Pick 1**. This is also the lower-exposure choice: $362 vs $820 at risk, about 3 vs about 5 sponsor hours, legal 7 vs 6, autonomy 8 vs 6.
- **Platform concentration.**
  - **Google Ads identity:** B1, B2 and B3 all ran on the sponsor's Google Ads advertiser verification. Google suspends related accounts by verifier and payment profile, so a second account does not isolate risk.
  - **Ruling:** **B3 drops Google Ads and uses Microsoft Ads for its search cell.** Meta remains its primary channel.
  - **Payments:** B1 uses Lemon Squeezy and B3 uses Stripe, so the two picks share no ad, payment or marketplace account.
  - **The sponsor's personal identity** is still behind every account. That can't be avoided; the mitigation is to keep each platform's footprint to one idea.
  - **Lemon Squeezy:** B1 (and Q1, if revived) use it. It is being folded into Stripe Managed Payments, which lacks the affiliate tooling. Before KYC, the AI must confirm that Lemon Squeezy still opens new stores; if not, B1 uses Stripe Managed Payments and handles affiliates manually.
- **Timing.**
  - **B3** must have ads live by about **Oct 22**, before BFCM CPM inflation. If it is not live by Oct 26, defer it to a Mother's Day 2027 test.
  - **Q2** needs a price answer by Oct 13 and DD by Nov 6 to close by Dec 1 and capture the January peak.
  - **B1** delivers by Nov 13, a month before the reported Dec 13 sitting. Its demand doesn't depend on that date; see §4.2.
  - **P1, P2:** Q4 is their good season, but they are gated.
  - **P3, U5:** Q4 is their off-season for host decisions.
- **Founder fit (noted, not scored).**
  - B1 matches the sponsor's Mandarin learning and the pending U3-W wedge.
  - B3 has no particular fit. It needs one hour of the sponsor's physical judgement of the sample books.

### 4.2 Reviewer conflicts resolved

1. **Is UltraWideo still listed?**
   - **The conflict:** the sales-skeptic's fetch on 2026-10-06 showed no for-sale flag or price. The market analyst read the page's `.md` endpoint the same day and found "$13,000, 2.5× revenue multiple" and partial October data ($123). The ideator also recorded the $13,000 ask.
   - **Ruling: probably still listed at $13k.** Two independent reads saw the ask, and the skeptic's fetch most likely missed content that renders client-side.
   - It doesn't affect the decision, because Q1 fails at any price near the ask. The sponsor confirms it on TrustMRR before sending the price indication.
   - **Related correction (unit economics):** UltraWideo's all-time revenue is only $6,877. The store listing is 5 years old; the revenue stream is about 12–18 months old.
2. **Wheel of Life: TTM $6,648 vs $8,285, and gross vs net of store fees.**
   - **Ruling: $6,648 is most likely net proceeds, and $8,285 is most likely the gross figure for the same period.**
     - $6,648 ÷ $8,285 = 0.80, which is what a 15% Small Business Program commission plus VAT/sales-tax deductions produces.
     - A shift in the TTM window would lower TTM, not raise it by $1.6k.
   - **Consequence:** the unit-economics model's 15% store-fee line double-counts about $75/mo. Q2's P50 cash net is about **$240/mo**, not $166. That raises the 24-month price ceiling from about $3.2k to about **$4.9k**.
   - **This must be confirmed** from App Store Connect "Proceeds" and Play earnings exports before any offer above $3.2k.
3. **HSK 3.0: live since 1 Jul, or first sitting 13 Dec?**
   - **Ruling: unresolved from desk evidence.**
   - **The question that matters is not the start date.** It is:
     - (a) whether the integrated speaking section is part of the L3–L6 sittings that English-speaking candidates take from Dec to Apr; and
     - (b) whether enough of them search for it.
   - Both are covered by B1's $0 Gate 0 (chinesetest.cn primary source plus the Keyword Planner forecast).
   - **How to plan:**
     - Assume steady monthly demand, not a December novelty spike.
     - If 1 Jul is confirmed, drop the "brand-new format" framing; the pre-order date still precedes the next sittings.
     - HanSpik's 0 ratings after 5 months are a negative signal on audience size.
4. **CAC disputes (B1, B3).**
   - B1: ideator $18; unit economics $22–30; sales-skeptic's 1–2% CVR implies about $35–70.
   - B3: ideator $42; unit economics $60; sales-skeptic $70–130.
   - **Ruling:** plan on the skeptical figures. Keep the ideators' pass bars ($22 and $47) as the go thresholds; the tests exist to settle this.
5. **B2's ad-policy risk.** The legal analyst is right: the 2026-10-05 change targets ads for *acquiring* government documents. The point is moot, because B2 is rejected.
6. **Sponsor hours.** The auditor's realistic hours are used, which are about 2× the ideators' figures.

### 4.3 Comparison with prior runs

| Run | Pick | Composite | Outcome |
|---|---|---|---|
| Round 1 | D2 OSHA inspection alerts | 6.20 | Deferred fallback, never tested. Its channel flaw (sales 4) is unfixed. B2's review found SiteVetter, 4+ Apify OSHA Actors, an OSHA MCP and a pay-per-call OSHA API, which is evidence against D2's data moat as well. |
| Round 1 | T2 Accela/EnerGov Actor | 5.95 | Shelved when M3 took the Apify slot. Never audited for clones. |
| Round 2 | M3 SheetSync | 6.70 | **No-go** after the day-0 audit: ~21 clones, and placement is at Apify's discretion. |
| Round 2 | M1 ChatRelay for Jira | 6.65 | **Dropped** by the sponsor: hard to test cheaply, cash ~Mar–May 2027. |
| Round 3 | B1 / B3 | 5.55 / 5.70 | Picks (staged tests). |

**Plain answer: nothing in round 3 beats the earlier top picks on composite.**

Two caveats:
- Round 3's composites are depressed by pricing sponsor time at $300/h, which lowered the autonomy and UE scores across the board.
- Every earlier pick is dead, dropped or unvalidated.

What round 3 adds is that, for the first time in three rounds, **capital buys the channel**. B1 and B3 answer "will a stranger pay?" within 3–4 weeks for a few hundred dollars. **D2 should not be revived** without the same day-0 clone audit that killed M3.

### 4.4 Combinations and pivots considered

| Combination | Verdict |
|---|---|
| Reddit + creator-slot fix → B1 | **Adopted** as the pivot branch of B1's Gate 0, for when keyword volume is 1,000–2,999 impressions/mo. |
| "Search intent first" → B3 | **Adopted**, but through Microsoft Ads exact match rather than Google, for concentration. Trade-off: less volume. If Microsoft can't spend $100 in the first week, move that budget to Meta rather than opening Google Ads. |
| Earn-out structure → Q1/Q2 | **Adopted** for the price indications. Cash at close stays at or below the 24-month ceiling, and the earn-out pays only on revenue above the P50 baseline. |
| Off-market approaches → Q3 | **Partially adopted.** The AI screens TrustMRR's verified-revenue startups that are not listed for sale, looking for abandonment signals. The sponsor sends notes only if the public screen fails by Dec 5, and at most 3 a month. |
| B2 → a $29 one-off "prequal pack" | Not now. It doesn't fix SiteVetter or the clone flood. Revisit in January only after a day-0 clone audit. |
| U5 → buy an existing mini-route, or a host-restocked variant | Rejected. Unit economics show < $300 below ~5 machines. ATM-portfolio comparables trade at ~3.5× cash flow, which implies the same for routes. |
| P3 as the location source for P1/U5 | Rejected: correlated risk, and P3 itself fails the sponsor-time gate. |
| Q2 + Apple Search Ads after close | An upside lever after purchase. It is not a reason to pay above the ceiling. |

### 4.5 Cheap-test options and acquisition price ceilings

Ranked by value per sponsor hour:

1. **B1 Gate 0.** $0 capital, about 0.6 h, answer by Oct 8. Then the $362 pre-order test.
2. **Q2 price indication.** $0 capital, about 0.25 h, answer by Oct 13.
   - Offer about **$4,500 cash at close**, subject to DD confirming that the $6,648 TTM is proceeds, plus **50% of monthly proceeds above $550 for 18 months**, capped below the $11,111 ask.
   - Hard ceiling: **$4.9k cash** (proceeds reading) or **$3.2k** (gross reading).
   - Even at the ceiling, Q2 is a ~$240/mo cash asset that nets about $0 until it has paid back at month ~24.
3. **Q1 price indication.** $0 capital, about 0.25 h.
   - Ceiling: **$2.7k cash**, plus 50% of gross above $390/mo for 18 months.
   - Expect "no": it is 79% below the ask.
   - Insist on asset purchase plus a merchant-of-record route confirmed in writing.
4. **Q3 screen.** $0 capital, about 0.25 h for Escrow.com KYC and buy-box pre-approval.
   - Use a tighter box: ≥ 18 months of history, ≤ 0.5× TTM, ≤ $2,750 all-in, nets ≥ $250/mo, marketplace-billed.
   - **Add billing portability:** App Store/Play, Shopify-billed apps or Freemius-billed plugins only; no Lemon Squeezy-locked subscriptions.
   - Verdict by Nov 5, with one extension to Dec 5.
5. **B3 test.** About $820 and about 5 h. Only if the sponsor commits by Oct 8.

**Highest cash prices that pass the 24-month rule:**

| Asset | P50 cash net used | Transaction costs | Ceiling (setup hours charged to year-1 profit) | Ceiling if setup hours are also loaded into payback | Ask |
|---|---|---|---|---|---|
| Q1 | ~$137–140/mo | ~$600 | **~$2.7k** (optimistic case: ~$4.5k) | None (negative) | $13,000 |
| Q2 | ~$240/mo (proceeds) / ~$166 (gross) | ~$816 | **~$4.9k / ~$3.2k** (optimistic case: ~$7k) | ~$1–2k / ~$0 | $11,111 |

### Pick 1: B1, HSK 3.0 Speaking Mock (paid search + Reddit; affiliates after a pass)

**Thesis.** English-speaking HSK L3–L6 candidates face a speaking section that the HSK 2.0 materials don't cover. They search for practice with clear intent, and a $29 timed mock with per-syllable tone scoring is an impulse-sized purchase. Paid search buys the channel that organic discovery can't, and the fast test settles whether the audience is big enough before anything beyond a demo is built.

**Key numbers**

| Item | Value |
|---|---|
| Upfront $ | **$962 committed**; **$362 at risk before the verdict** (ads $300, domain $12, native QA $50). After a pass: model-answer contractor ~$200 and a $400 scale tranche |
| Days to first sale | P50 **45** / P90 never. If Gate 0 passes, the first pre-order is plausible around Oct 18–25 |
| Sales/month for $300 net | **~33 every month** (at ~$14 blended net per sale after ads). P50 is ~15 in peak months |
| Expected net | P50 ~$35/mo average (Dec–Apr ~$110), P90 ~$500/mo |
| Sponsor hours | Setup ~4 h, of which ~3 h before the verdict. Ongoing ~0.35 h/mo; **cap it at 0.25 h/mo** |
| Legal risk | **Low** (7/10): FTC affiliate and testimonial disclosure, pre-order delivery promise, nominative "HSK" only, voice-data consent |

**30-day launch plan.** Day 0 = Tue Oct 6. Building beyond the landing page and one demo task starts only after the Oct 30 pass.

Week 1, day by day:

| Day | AI operator | Human sponsor |
|---|---|---|
| 0 (Oct 6) | Write `tests/B1.md` with the pre-committed thresholds. Start Gate 0 research. | none |
| 1 (Oct 7) | **Gate 0a:**<br>- chinesetest.cn/CTI primary sources for the L3–L6 speaking-task format and the 2026–27 sitting calendar;<br>- first-hand reports on r/ChineseLanguage and r/LearnChinese (read only);<br>- a price and rating table for the official mock, Mandarin Temple, HanSpik and hsktest.ai;<br>- the keyword list and negatives. | 0.5 h: create a Google Ads account (billing, no campaigns). Paste the keyword list into Keyword Planner and export the forecast CSV. |
| 2 (Oct 8) | **Gate 0 verdict:**<br>- **Pass:** format confirmed in the Dec–Apr sittings **and** ≥ 3,000 impressions/mo across English-speaking markets.<br>- **Pivot:** 1,000–2,999 impressions. Re-weight to Reddit $150 + one creator slot $150.<br>- **Kill:** < 1,000, or no speaking section.<br>Also confirm that Lemon Squeezy is accepting new stores. | 0.1 h: read the verdict. |
| 3 (Oct 9) | Build the landing page; one free read-aloud demo task (pronunciation-assessment API with no audio retention); the $29 refundable pre-order checkout (delivery by Nov 13); an automatic-refund job for Oct 31, tested with a $1 order. | 1.5 h: Lemon Squeezy KYC (or Stripe Managed Payments). Google Ads advertiser verification with an account-level cap of $200. Reddit Ads account with a $100 cap. |
| 4 (Oct 10) | Write the compliance copy: nominative "HSK", no "official", voice consent, 18+, EU withdrawal waiver, no score predictions. Draft the Upwork job post. | 0.5 h: hire a native-speaker QA (~2 h, ~$50). |
| 5 (Oct 11) | Apply the QA fixes. Set up email capture and a 4-email sequence keyed to the exam date (CAN-SPAM compliant). | none |
| 6 (Oct 12) | Build Google exact/phrase campaigns and Reddit community targeting. Add source tags so that only strangers count. Submit ads for review. | none |
| 7 (Oct 13) | Ads go live on approval (target Oct 13–16). Daily monitoring dashboard. | none |

Weeks 2–4:

| Week | AI operator | Human sponsor |
|---|---|---|
| 2 (Oct 14–20) | Daily bid and negative-keyword management. **Oct 20 checkpoint:** $150 spent with 0 pre-orders means stop paid. | 0 h |
| 3 (Oct 21–27) | Keep optimising. Prepare the L3 scoring skeleton only; no contractor spend. | 0 h |
| 4 (Oct 28–Nov 5) | **Oct 30 verdict:**<br>- **Pass** (≥ 12 stranger pre-orders, blended CAC ≤ $22, ≥ $250 spent): build L3/L4 for Nov 13 delivery, start one-to-one affiliate pitches to ~15 creators, schedule the $400 tranche.<br>- **Pivot** (6–11 pre-orders, or CAC $22–30): $150 more on the best ad group by Nov 6, then re-judge.<br>- **Fail:** automatic refunds on Oct 31; stop paid. | 0.5 h: approve the verdict and the model-answer contractor (after a pass only). |

**Kill criteria**

| When | Kill condition |
|---|---|
| Oct 8 (Gate 0) | Speaking is not part of the L3–L6 sittings candidates take from Dec to Apr, **or** Keyword Planner shows < 1,000 impressions/mo. Kill at $0. |
| Oct 16–30 | Less than $150 of budget can be spent. Stop paid. |
| Oct 20 | $150 spent with 0 pre-orders. Stop paid. |
| Oct 30 | ≤ 5 stranger pre-orders, or blended CAC > $30. Refund everything and kill. |
| After delivery | Refund rate > 15%. Stop ads until fixed. |
| Jan 31, 2027 | Dec–Jan contribution after ads is below tokens plus sponsor cost. Shut down; no limbo. |

**Top 3 risks and mitigations**

| # | Risk | Mitigation |
|---|---|---|
| 1 | **The audience is too small.** | Gate 0 keyword forecast; the Reddit + creator pivot; a $300 cap. |
| 2 | **Format or date uncertainty**, plus spec accuracy. | Check the primary source before any build; native QA; no "official" or score-prediction claims; refund on defect. |
| 3 | **Cheap incumbents and AI clones** (official mock ~$8, Mandarin Temple $19/mo, HanSpik), plus **Lemon Squeezy migration risk**. | Differentiate on the per-syllable tone report and the exam-date-keyed plan. CAC kill rule at $30. Stripe Managed Payments as the fallback. |

### Pick 2: B3, Heirloom Recipe-Card Cookbook (Q4 gift certificate; Meta + Microsoft Ads)

**Thesis.** Gift buyers pay $100+ for family-memory products (Storyworth proves the paid-social model). "Photograph Grandma's cards, get a facsimile-plus-typeset hardcover" removes the typing that stops people using Mixbook. Selling an instant certificate now, with the book made after upload, sidesteps the December print cutoff and catches the highest-intent gift shoppers of the year.

**Key numbers**

| Item | Value |
|---|---|
| Upfront $ | **$2,322 committed**; **~$820 at risk before the verdict** (samples ~$135–180, photographer $150, domain $12, permit ~$25, ads $500). The $1,500 scale tranche is released only on a pass |
| Days to first sale | P50 **26** / P90 **75**. Stripe pays out in about 2 days |
| Sales/month for $300 net | **~26 paid orders/mo at the $47 gate CAC**; **~73/mo at the P50 CAC of $60** |
| Expected net | Unconditional P50 −$30/mo. About $310/mo averaged if the test passes. P90 ~$560/mo |
| Sponsor hours | Setup ~6 h, of which ~5 h before the verdict. Ongoing ~0.6 h/mo average (1.5 h/mo Nov–Jan) |
| Legal risk | **Medium** (6/10): gift-certificate law, FTC Mail Order Rule, rights in uploaded clippings, publicity rights in ads, sales tax (Stripe is not a merchant of record) |

**30-day launch plan.** Every order taken is delivered whatever the verdict, so a minimal fulfilment pipeline is part of the test. Building beyond it waits for a pass.

Week 1, day by day:

| Day | AI operator | Human sponsor |
|---|---|---|
| 0 (Oct 6) | Write `tests/B3.md`. Source public-domain or CC0 handwritten-card scans and log their licences. Start the pipeline: upload → vision transcription with low-confidence flags → facing-page layout → PDF proof. Pull Lulu's 2026 holiday production calendar. | **Commit or skip B3 by Oct 8**: it needs ~5 h before Oct 22. |
| 1 (Oct 7) | Produce 3 sample-book PDFs (~100 pages). Integrate the Lulu Print API sandbox. | 0.5 h: create the Lulu account with a card. |
| 2 (Oct 8) | **Order the samples through the API with expedited shipping:** 2 to the photographer, 1 to the sponsor. Draft the terms:<br>- the certificate is for **"one heirloom cookbook"**, with no dollar value, no expiry, and a refund until upload;<br>- ToS with a rights warranty and an "untested recipes" disclaimer;<br>- uploads deleted after printing. | 1.25 h: Stripe KYC plus Stripe Tax. Apply for the home-state sales-tax permit. |
| 3 (Oct 9) | Build the landing page, checkout, instant certificate PDF, and the order → proof → approval → Lulu workflow. | 1 h: Meta Business Manager and business verification. |
| 4 (Oct 10) | Build the Microsoft Ads exact-match set and negatives. Set up a Meta manual sales campaign (not Advantage+), with pixel and Conversions API. | 0.5 h: open a Microsoft Ads account. **No Google Ads for B3.** |
| 5 (Oct 11) | Write the photographer brief and a shortlist. | 0.25 h: hire the photographer for Oct 19–20. |
| 6–7 (Oct 12–13) | Set platform caps (Meta $300, Microsoft $200). Dry-run the whole flow with a $1 order. Prepare 6 creative templates. Set the delivery-claim rule ("in time for Christmas" only for proofs approved by Lulu's cutoff less 5 business days). Automatic FTC delay notices. | none |

Weeks 2–4:

| Week | AI operator | Human sponsor |
|---|---|---|
| 2 (Oct 14–20) | Samples arrive (~Oct 15–19). Photo shoot Oct 19–20. Build the creatives from real photos only. | 1 h: inspect the sponsor's copy. Go/no-go. |
| 3 (Oct 21–27) | **Ads live by Oct 22.** Fulfil every order. **Checkpoint: 0 orders after $250 means stop.** | ~0.25 h: account or verification issues if any arise. |
| 4 (Oct 28–Nov 5) | Track the proof gate: ≥ 80% approved within 2 rounds. Prepare the Nov 8 verdict:<br>- **Pass** (≥ 10 stranger orders at CAC ≤ $47): $1,500 tranche from Nov 9 to Dec 20, with per-ad-set CAC stops; hold spend in BFCM week unless CAC ≤ $47; stop on Dec 23.<br>- **Pivot** (6–9 orders): change one creative or the offer and spend $250 by Nov 16.<br>- **Fail:** stop ads and fulfil existing orders. | ~0.25 h/week: chargeback approvals; the sales-tax return when due. |

**Kill criteria**

| When | Kill condition |
|---|---|
| Oct 19 | The samples show print defects that Lulu won't remedy, or transcription is below 95% character accuracy. Don't launch (~$300 lost). |
| Oct 26 | Ads not yet live. Skip Christmas and re-plan as a Mother's Day 2027 test. |
| Any time | 0 orders after $250 spent. |
| Nov 8 | ≤ 5 stranger orders, or CAC > $70 at $500. |
| Any time | Proof approval < 80%, or misprints > 10% of the first 10 books. Stop ads. |
| Any time | Meta ad account restricted for > 72 h. Go Microsoft-only; if that is also blocked, stop. |
| Jan 15, 2027 | Season contribution after ads and tokens is negative. No Mother's Day run. |

**Top 3 risks and mitigations**

| # | Risk | Mitigation |
|---|---|---|
| 1 | **CAC well above $47.** | Test before BFCM. Microsoft exact match for intent. A manual Meta campaign judged on cost per purchase. Hard platform caps. |
| 2 | **Fulfilment and quality.** | Low-confidence words flagged for the family. Mandatory proof approval. Conservative delivery claims with a buffer. Automatic delay and refund notices. 5% reprint reserve. |
| 3 | **Compliance.** | A "one cookbook" certificate with no stated value and no expiry. Stripe Tax plus the home-state permit, with a resale certificate to Lulu. Exclude printed or branded cards. Written releases before any customer content appears in ads. |

---

## 5. Runners-up

1. **Q2, Wheel of Life-class app (4.75; gated).** To win, two things must be true:
   - the seller accepts **≤ ~$4.9k cash** plus an earn-out above the baseline by Oct 13;
   - DD confirms by Nov 6 that the $6,648 TTM is proceeds, lifetime purchases are < 40% of TTM, and there are ≥ 110 active subscriptions.
2. **Q1, UltraWideo-class extension (4.50; gated).** To win, all of these must be true:
   - the seller accepts **≤ ~$2.7k cash**;
   - a merchant-of-record route is confirmed in writing;
   - MRR stops falling and Chrome Web Store users hold.
3. **B2 / D2 lineage, OSHA data for contractors (4.10; gated).** Revisit in January only after a day-0 clone audit, a Keyword Planner check, and a paid one-off "prequal pack" test.

**Standing background option:** Q3, as the AI-only screen with the billing-portability filter. It costs nothing while nothing qualifies.

---

## 6. Observations about the idea set

1. **Capital did not unlock profit; it unlocked tests.**
   - At under $10k, cash-flowing assets are priced at 1.7–2.8× revenue, or rest on utilisation that industry incumbents already skip (ATMs below 250 tx/mo, vending sites grossing $300–700, US power-bank habits).
   - Capital's best use in this run was **buying a fast, capped answer** (B1, B3), not buying an income stream.
2. **Sponsor time at $300/h is now the binding constraint.**
   - Tokens plus even 0.25–0.5 h/mo of sponsor time form a ~$150–300/mo fixed floor.
   - Anything grossing under ~$600/mo can't clear $300 net.
3. **Systematic ideator biases:**
   - setup hours under-counted about 2×;
   - cold-traffic CVR 2–3× optimistic for review-less brands;
   - recurring sponsor cost left out of net;
   - heavy reliance on seller-biased sources.
4. **Physical ideas are correlated, not diversified.**
   - P1, P2, P3 and U5 all hinge on signing a location by mail, and all hit Q4 host inertia.
   - **The sponsor's one identity sits behind every ad and payment account.**
5. **Blind spots in the ideators:**
   - billing portability was never a buy-box criterion;
   - **no idea used the sponsor's own audience, credentials or network**;
   - no one considered buying distribution instead of product (e.g. a niche newsletter or a YouTube channel);
   - deal structure (earn-outs) came from reviewers, not ideators;
   - the seasonal calendar beyond Q4 was ignored.

---

## 7. Addendum: sponsor ruling 3 (break-even target), applied by the orchestrator

**Ruling 3** (PARAMS.md): the target is **P50 net ≥ $0 after all costs**, not $300/mo. Those costs are:
- operator tokens;
- every sponsor hour at $300/h;
- capital recovery within the payback window.

| ID | P50 net after all costs (unit-economics, committee-adjusted) | Under $300/mo target | Under break-even (ruling 3) | Other gates | Net change |
|---|---|---|---|---|---|
| **B1** | ~+$35/mo avg (Dec–Apr ~+$110) | Fail | **Pass** | < $1k; staged test | **Now a full pass**, not just a staged test |
| **B3** | ~−$30/mo unconditional; ~+$310 if the test passes | Fail | **Pass if the test passes**; ≈ break-even unconditional | First tranche < $1k | Unchanged: still a staged test |
| Q2 | ~+$240/mo cash before capital recovery (proceeds reading) | Fail | Profit OK | **Payback fails** at any likely price (ceiling ~$4.9k) | None |
| Q1 | ~+$137/mo cash before capital recovery | Fail | Profit OK | **Payback fails** (ceiling ~$2.7k) | None |
| P1 | ~+$142/mo after depreciation | Fail | Profit OK | **Payback 31–49 mo** vs 12; P10 84% | None |
| Q3 | ~+$60/mo (conditional on a deal) | Fail | Profit OK | **P10 87%**; deal flow probably absent | None |
| B2, P2, P3, U5 | Negative | Fail | **Fail** | | None |

**Conclusion: the picks are unchanged (B1, then B3).**
- B1 now meets the target in its own right, rather than only as a test.
- For every other idea, the binding constraint is **capital payback and downside**, not the profit target. Acquisitions only work at the price ceilings in §4.5.
- At break-even the capital earns ~0% against ~4% in T-bills. That is context only.
