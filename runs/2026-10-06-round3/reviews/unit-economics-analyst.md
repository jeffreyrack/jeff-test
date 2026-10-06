# Unit Economics Analyst review: round 3 (capital allowed)

_Date: 2026-10-06. Scope: all 10 round-3 ideas (Q1–Q3, B1–B3, P1–P3, U5). Binding rules: `../PARAMS.md`. I re-derived every ideator number; where I disagree, the section says why._

## Method and conventions (applied to every idea)
- **Clock.** m1 = Oct 2026. Every ramp is counted from today, not from launch (lesson §2).
- **Net after all costs** = revenue − COGS − payment/store fees − contractors − AI operator tokens − **ongoing sponsor hours × $300** − depreciation or amortisation.
  - **Depreciation and amortisation:** ATMs and vending machines over 5 years down to salvage; power banks over 3 years; acquired digital assets over 36 months straight-line.
  - **Cash net** is the same figure before depreciation. Payback uses cash net.
- **Payback from today:** the first month in which cumulative cash turns ≥ 0. Cumulative cash includes capital, one-time sponsor setup hours × $300 (PARAMS charges them to year 1) and operating cash along a realistic ramp.
  - **Run-rate payback** = capital ÷ steady-state P50 cash net.
  - **Gate basis:** the 12-month gate is judged on payback from today.
- **P10 capital loss** = (capital deployed in the P10 path − operating cash recovered − salvage) ÷ that capital. One-time sponsor hours are excluded.
  - **Tranche rule (staged ideas):** if the first tranche is above $1k, the gate is judged on that tranche. If it is under $1k, the gate is judged on committed capital.
- **Sponsor-hour gate:** ongoing hours ≤ (net *before* sponsor cost) ÷ $300.
- **Return on capital:** two figures.
  - **Year 1:** includes setup hours, ramp, and terminal book value at m12.
  - **Steady state:** 12 × P50 net after all costs ÷ capital.
  - Both are compared with 4% T-bills.
- **Capital** excludes "operating reserves". They are unspent cash, not a cost.

## Summary table

| ID | Idea | UE score | Total capital | Net $/mo after all costs, P10 / P50 / P90 | P50 payback: from today / run-rate | P10 capital loss | Return on capital, P50 (yr-1 / steady) vs 4% | PARAMS gates | Sensitivity: 24-mo payback for verified-revenue acquisitions |
|---|---|---|---|---|---|---|---|---|---|
| Q1 | UltraWideo-class extension | 2 | $8,709 (at $8.0k price; $7,685 at $7k) | −$239 / −$105 / +$131 (cash: $3 / $137 / $373) | 90 mo / 64 mo | 77% | −52% / −15% (cash yield 19%) | **FAIL** (payback, P10) | **FAIL.** Needs all-in ≤ $3.3k (price ≈ $2.7k) |
| Q2 | Wheel of Life-class app | 3 | $8,316 (at $7.5k price) | −$208 / −$65 / +$191 (cash: $23 / $166 / $422) | 70 mo / 50 mo | 67% | −44% / −9% (cash yield 24%) | **FAIL** (payback, P10) | **FAIL.** Needs all-in ≤ $4.0k (price ≈ $3.2k) |
| Q3 | ≤$3k fire-sale buy order | 3 | $3,210 per deal | −$102 / +$60 / +$240, conditional on a deal (cash: −$13 / $149 / $329) | 50 mo / 21.5 mo (34 mo from close incl. setup) | 87% | −91% / +22% (cash yield 56%) | **FAIL** (payback, P10) | **FAIL** on a consistent basis. Passes only on run-rate (21.5 mo) if search time and $1.8k of setup hours are ignored |
| B1 | HSK 3.0 speaking mock (paid search) | 4 | $962 committed ($712 deployed at P50) | Killed at test (−$562 one-off) / ~$35 avg ($110 peak) / ~$500 | 39 mo (16 ex-setup) / 28 mo | 58% committed (100% of deployed) | yr-1 −$1,110 / +44% | **PASS** (<$1k; sponsor-hour OK). Misses the $300 target | N/A (<$1k) |
| B2 | SubWatch (OSHA subs, Google Ads) | 2 | $912 ($712 deployed at P50) | Killed (−$512) / −$40 (likely killed ~m3) / +$765 by m12 | never / never | 56% committed (100% of deployed) | yr-1 −$2,172 / negative | **FAIL** (sponsor-hour gate at P50) | N/A |
| B3 | Heirloom recipe cookbook (Meta, Q4) | 4 | $2,322 committed ($822 tranche 1) | −$40 (killed; −$487 one-off) / −$30 / +$560 avg | never / never (P90: ~m3) | 59% of the $822 tranche = 21% of committed → **PASS** | yr-1 −$2,391 / −16% | **FAIL** (payback at P50; sponsor-hour) | N/A. Restructured as an $822 test plus a separate scale decision, it drops under $1k |
| P1 | Merchant-loaded ATMs (3) | 3 | $6,660 (pilot $2,510) | Pilot killed at −$278 / +$142 (cash $216) / +$1,121 | 49 mo / 31 mo | 84% of pilot tranche | −26% / +26% (cash yield 39%) | **FAIL** (payback, P10) | N/A (also fails 24: 31 mo) |
| P2 | Power-bank stations (8) | 2 | $3,220 (pilot $1,210) | Pilot killed at −$250 / −$43 (cash $33) / +$1,358 | never / 99 mo | 88% of pilot tranche | −63% / −16% | **FAIL** (payback, P10) | N/A |
| P3 | PlacementDesk (location sourcing) | 2 | $575 | −$695 (killed m3) / −$482 / +$505 | never / never | 100% (N/A, <$1k) | deeply negative | **FAIL** (sponsor-hour gate) | N/A |
| U5 ×1 | Vending, 1 used combo machine, outsourced restock | 1 | $3,500 | −$345 / −$263 / −$198 | never / never | 70% | −106% / −90% | **FAIL** | N/A |
| U5 ×2 | Vending, 2 machines | 1 | $6,700 | −$425 / −$243 / −$60 | never / never | 69% | −56% / −43% | **FAIL** | N/A |
| U5 ×3 | Vending, 3 machines | 1 | $9,900 (zero headroom under the $10k cap) | −$505 / −$223 / +$78 | never / never (P90 run-rate 57 mo) | 68% | −38% / −27% | **FAIL** | N/A |

**Bottom line.**
- **No idea above $1k passes.** Only B1 passes the PARAMS gates, and its P50 (~$35/mo) is far below the $300 target.
- **Relaxing payback to 24 months does not rescue any acquisition at today's prices.** It would only matter at purchase prices of roughly $2.7k (Q1), $3.2k (Q2), or Q3's buy-box with sponsor setup time ignored.

### Agent-standard table
| ID | Idea | Score | Upfront $ | Monthly fixed $ (incl. tokens + ongoing sponsor h) | Net $/sale | Sales/mo for $300 after all costs | Est. operator tokens $/mo | Months to break-even (from today, P50) |
|---|---|---|---|---|---|---|---|---|
| Q1 | UltraWideo-class | 2 | 8,709 | 186 (+242 amortisation) | $2.29 per paying sub-month | ~318 paying subs (now 130) | 90 | 90 |
| Q2 | Wheel of Life-class | 3 | 8,316 | 258 (+231 amortisation) | 85% of gross | ~$930/mo gross (1.9× P50) | 100 | 70 |
| Q3 | Fire-sale buy order | 3 | 3,210 | 175 (+89 amortisation) | 90% of gross | ~$630/mo gross (vs $360 P50) | 40 before the deal / 60 after | 50 |
| B1 | HSK speaking mock | 4 | 962 | ~165 | ~$14 blended ($28 organic, $18 affiliate, ~$6 paid) | ~33/mo every month (P50 ~15) | ~100 (80–150) | 39 |
| B2 | SubWatch | 2 | 912 | ~215 + ads | $88.75 per account-month (CAC ~$1,000) | ~13 active accounts plus ~$600/mo ads (P50: 2–3) | 120–150 | never |
| B3 | Heirloom cookbook | 4 | 2,322 | ~210 in season / ~110 off-season | $67 before CAC; ~$7 after P50 CAC $60 | ~73 paid orders/mo, or 8 organic | 50–150 (~90 avg) | never (P90 ~3) |
| P1 | ATMs ×3 | 3 | 6,660 | 545 (+74 depreciation) | $1.95 per withdrawal | ~470 withdrawals/mo (157/ATM; P50 130) | 100 | 49 |
| P2 | Power banks ×8 | 2 | 3,220 | 322 (+75 depreciation) | ~$2.95 per rental | ~236 rentals/mo (30/station; P50 15) | 80 | never |
| P3 | PlacementDesk | 2 | 575 | 695 | $250 per install | ~4 installs/mo (P50 0.7) | 150 | never |
| U5 | Vending ×1 / ×2 / ×3 | 1 | 3,500 / 6,700 / 9,900 | 375 / 468 / 560 (+33/65/98 depreciation) | ~$0.65 per vend before restock | ×3: ~$1,050 gross per machine per month (2.3× P50); ×1: ~$2,400 | 70 / 80 / 90 | never |

## Cross-cutting findings
1. **The $300/h price on sponsor time and $60–150 of tokens are a fixed ~$150–300/mo floor on every idea.** Any asset grossing under ~$600/mo struggles to clear it. The ideators mostly left recurring sponsor hours out of "net" (Q1, Q2, Q3, B1) or understated them (P3).
2. **The acquisitions fail on price, not quality.** Q1 and Q2 are real businesses, but they throw off $137–166/mo of cash after costs, and that cannot repay $8k+ inside 24 months. The ideators' 19–26-month paybacks rested on three things:
   - $60–70 of tokens;
   - no ongoing sponsor cost;
   - no legal fees, a lower purchase price and (Q1) a lower fee rate.
3. **Physical ideas fail on overhead per unit at 1–3 units.**
   - P1, P2 and U5 each have a P50 below their *own* scale gate (ATM 130 vs 150 tx; stations 15 vs 20 rentals).
   - So the realistic P50 path is "pilot, then kill", with an 84–88% loss on the pilot tranche.
4. **Ad-funded ideas (B1, B3) have the best risk shape.**
   - Every order carries positive contribution, so a failed test loses at most the test budget.
   - The tests are cheap: $562 and $822 deployed.
   - Neither shows a P50 near $300. Each is a live option that the test resolves.

---

## Q1 — UltraWideo-class aged browser extension
**Verified:** TrustMRR shows $440 for the last 30 days, $346 MRR and 130 subs. All-time revenue is only **$6,877**, although the product was founded in 2021, so meaningful monetisation is ~12–18 months old. The "5-year" history belongs to the store listing, not to the revenue.

| Item | Ideator | Mine |
|---|---|---|
| Price | $7,000 | $8,000 (P50 negotiated, against a $13k ask) |
| Escrow / legal / dev accounts | $230 / $0 / $35 | $192 (Escrow.com 2.4%) / **$500 APA review** / $17 |
| LS fees | 12% | 14% (the derived mix is 85 annual + 45 monthly subs, at 5% + $0.50, plus ~1.5% international) |
| Gross run-rate | $390 | $375 (TTM avg, −15% migration loss on LS→Stripe, +10% from operator work) |
| Tokens / ongoing sponsor | $60 / not charged | $90 / 0.25 h = $75 |
| **Cash net** | ~$290 | **$137** |

- **Payback:** 64 months at run-rate. From today it is 90 months: close ~m2, plus 10 h of setup = $3,000.
- **P10:** gross $220 → $3/mo cash; resale ~$2,000 → **77% loss**.
- **P90:** gross $650 → $373 cash.
- **Return:** the cash yield is 19%, but after 36-month amortisation it is **−15%/yr**, below T-bills. Even 60-month amortisation gives about −2%.
- **24-month sensitivity:** fails. Passing needs all-in ≤ $3.3k (price ≈ $2.7k, about 0.6× TTM).

## Q2 — Wheel of Life-class subscription app
- **Data discrepancy:** TrustMRR currently shows **TTM $8,285**, while the ideator has $6,648. Gross vs proceeds is also still ambiguous. DD must reconcile both before an offer.
- **Revenue mix:** with MRR at only $181, about 60% of revenue is new annual or lifetime purchases. Revenue therefore rides on the store's install flow, not on the subscriber base.

| Item | Ideator | Mine |
|---|---|---|
| Price | $6,500 | $7,500 |
| One-off extras | escrow $210, dev fees $124, domain $12 | escrow $180, **legal $500**, dev fees $124, domain $12 |
| Gross | $554 | $499 (TTM × 0.9 decay; seasonal profile kept: Dec $747, Jan $957) |
| Store fee | 15% | 15% (Small Business Program) |
| Fixed | $88 + tokens $70 | dev $8 + backend $10 + **macOS CI $20** + tokens $100 + **sponsor 0.4 h = $120** (Apple 2FA and agreements) |
| **Cash net** | $370 | **$166** |

- **Payback:** 50 months at run-rate; 70 from today (10 h of setup = $3,000; first Apple cash ~Jan 2027).
- **P10:** gross $330 → $23 cash; resale ~$2,500 → **67% loss**.
- **P90:** $422 cash.
- **Return:** steady state −9% after amortisation (cash yield 24%).
- **Verdict:** this is the strongest acquisition, but it fails both gates, and it fails 24 months unless the price is ≤ ~$3.2k (12 months needs ≤ ~$1.2k).
- **Timing:** missing the Dec–Jan peak costs ~25% of annual revenue.

## Q3 — Standing ≤$3k fire-sale buy order
- **Per-deal capital:** $2,800 price + $100 escrow + $250 legal template + ~$60 dev accounts = **$3,210**.
- **Post-close P50:** gross $360 (the $450 buy-box floor less 20% decay) × 90% after fees, less $40 hosting, $60 tokens and $75 sponsor = **$149 cash**, or **+$60 after amortisation**.
- **What the ideator omitted:**
  - **Search costs:** at ≥3 desk-passing candidates a month, memo reading is ~0.5 h/mo = $150/mo, plus ~$40 tokens.
  - **A failed due diligence:** ~2 h = $600.
  - **The ideator's own odds:** a ~35% chance of a deal within 90 days puts the **P50 close around month 5**, not day 60–90.
- **Payback:** 21.5 months at run-rate, 34 months from close including 6 setup hours ($1,800), and **50 months from today**.
- **P10 (conditional on buying):** decay of −60% gives gross $180 → −$13/mo; resale ~$500 → **87% loss**. The P10 with no deal loses no capital but burns about $1–2k of sponsor time.
- **Return:** +22% steady state, the only acquisition above T-bills, but year 1 is −91%.
- **24-month sensitivity:** fails on the same basis as the other ideas. It passes only on run-rate.

## B1 — HSK 3.0 speaking mock (paid search plus affiliates)
- **Per sale:** $33 average less Lemon Squeezy (5% + $0.50 + 1.5% international) ≈ $2.65 and ~$2.50 inference = **$28 net**.
- **The ideator's P50 CAC of $18 is optimistic for a new brand.** I use a CPC of ~$0.75–0.90 and a CVR of ~3%, giving a CAC of **$22–30**.
  - That leaves only ~$6 of margin per paid sale.
  - The test sits on the kill rule's $22–30 boundary.
  - Affiliates net ~$18 and organic sales net ~$28.
- **P50 mix:** ~15 sales a month in peak months; English-speaking L3–6 candidates are a small pool.
  - Contribution is ~$214, against ~$165 fixed: tokens ~$100, hosting $5, native-contractor upkeep $15, sponsor 0.15 h = $45.
  - That gives **~$35/mo averaged** (Dec–Apr ~$110, summer −$20).
  - Reaching $300 needs ~33 sales every month.
- **Payback:** 16 months from today excluding setup, **39 months** including 3 h of setup ($900).
- **P10:** the test fails; $562 is lost (58% of the committed $962).
- **P90:** CAC ~$12 with ~50 sales → ~$500/mo.
- **Gates:** passes (under $1k, sponsor-hour gate met), but it is a long-dated option, not a $300/mo business.
- **Biggest swing factor:** whether the speaking section really runs from the 13 Dec sittings. If it doesn't, P50 is ~0.

## B2 — SubWatch (OSHA history for GCs' subcontractors)
- **Per account:** margin is $88.75/mo. Using 5%/mo SMB churn, capped at 18 months, LTV ≈ $1,300–1,600.
- **The ideator's 8% free→paid rate is the weak link.** A "check 5 subs" report solves the one-off prequalification need, so buyers leave. My P50 inputs:
  - CPC: $4.50 (construction $5.87–6.45);
  - landing page → lead: 10%;
  - lead → paid: 4%;
  - **CAC ≈ $1,100, LTV:CAC ≈ 1.2**, against the ideator's 3.7.
- **P50 path:**
  - the $500 test produces about 11 leads and 1 trial;
  - a partial pass leads to the $200 retest;
  - paid acquisition stops, leaving 1–2 customers against $215/mo of fixed cost (tokens $120 standalone, $20 hosting and email, sponsor $75).
  - That is **−$40/mo**, so it is likely killed around m3. Year 1 is −$2.2k including setup.
- **P90:** CAC ~$300 → ~18 accounts by m12 → +$765/mo.
- **P10:** ads are disapproved under the 2026-10-05 Google government-documents policy, or the test returns 0 trials → $512 lost.
- **Gates:** under $1k, so the payback and P10 gates don't apply. It **fails the sponsor-hour gate** at P50: net before sponsor is ~$35, which allows 0.12 h, against 0.25 h needed.

## B3 — Heirloom recipe-card cookbook (Meta + Google, Q4 gift certificate)
**Contribution per order:** **$67**, against the ideator's $71. The build-up:
- Lulu 100-page colour hardcover ≈ $32.50, fulfilment $1.75 and ground shipping ~$8, so **$42**;
- Stripe plus Stripe Tax $4.35;
- tokens $3;
- reprint reserve raised to 5% ($6), because transcription errors in heirloom content are likely;
- extra-copy attach +$3.

**CAC:**
- The ideator's $42 assumes a 2.5% cold CVR for a new, review-less brand selling a $119 gift during Q4 CPM inflation.
- My P50 is **CAC ~$60** (CPC ~$1.30, CVR ~2–2.2%).
- That misses the ≤$47 pass bar, so no scale tranche is released. Orders still contribute about +$7 each.

**Outcomes:**
- **P50:** the season runs at test-level spend: 8 test orders, ~12 Nov–Dec orders and ~5 organic, plus relatives' copies and a small Mother's Day run.
  - About **−$30/mo** steady state and **−$2.4k in year 1** including 5 h of setup ($1,500) and 0.4 h/mo of sponsor time for sales-tax filing and chargebacks.
- **P10:** CAC ≥$90 → 5 orders → $487 lost of the $822 first tranche (21% of committed). **Passes** P10 under the tranche rule.
- **P90:** CAC $35 → about $7.6k of season contribution → ~$560/mo average, with payback by ~m3.

**Gates:** fails at P50 (payback and sponsor-hour). The risk shape is the best in the run. It is decided by the $500 test before Nov 8; any launch later than ~Oct 22 loses the season.

## P1 — Merchant-loaded ATMs
**Per withdrawal:** the 60% owner share of $3.25 plus ~$0.10 interchange, less a ~$0.10 per-transaction processing fee = **$1.95**.

**Per-ATM fixed costs: $85/mo.** The ideator's $80 omitted the per-transaction processing fee.
- processing $25;
- cellular $15;
- repair reserve $35;
- paper $5;
- bank fees $5.

**Business-level costs:**
- tokens $100;
- sponsor 0.5 h = $150, for processor, merchant disputes and 1099s (ideator: 0.3 h);
- insurance $40.

**Volume:** "Gated" locations evidenced by popular-times data and a till photo are weak evidence. My P50 is **130 tx** (the beancount guide says 100–200 is typical).

**Capital:**
- per ATM $1,975: refurbished unit $1,450, freight $200, install $200, **key loading $75**, signage $50;
- pilot: $2,510;
- full build: **$6,660**.

| P50 path | Cash/mo |
|---|---|
| Pilot only. At 130 tx it misses the ideator's own ≥150 scale gate | **−$122** |
| 3 ATMs (units 2–3 live in Apr, m7, after the 2-month gate; the ideator had m2–m4) | **+$216** (+$142 after depreciation) |

- **Payback (3-ATM path):** 31 months at run-rate, **49 months from today** including 6 setup hours ($1,800).
- **Break-even volume:** reaching $300 net needs ~157 tx per ATM.
- **P10:** 50 tx, relocation $300, resale ~$700 net → **84% loss on the $2.5k pilot**.
- **P90:** 300 tx × 3 ATMs → +$1,121/mo.
- **Return:** +26% steady state (beats T-bills), −26% in year 1.
- **Gates:** fails payback and P10.

## P2 — Countertop power-bank stations
**Capital, re-itemised:**
- Tariffs are taken at ~40% rather than 32%, because Section 301 on Chinese Li-ion stacks with other China duties.
- Additions the ideator left out: the express sample station (~$200), lithium-safe ground shipping to venues (~$30 each), and product-liability insurance (~$150/quarter rather than $100).
- **Pilot: $1,210**, which is above $1k. **Full fleet of 8: $3,220.**

**Utilisation:** Brick's ~1 rental/day "typical" figure is for a branded European network. A no-name station in small US bars at P50 does **~15 rentals/month at $5**.

**Per station:**
- gross $75;
- venue share −$15;
- Stripe −$6.70 (the $0.30 fixed fee is 6% of a $5 rental);
- SaaS and SIM −$9;
- battery wear −$3;
- lost banks and chargebacks −$6;
- **net $35**.

**Business-level fixed:** tokens $80, sponsor 0.4 h = $120, insurance $50.

| Path | Cash/mo |
|---|---|
| Fleet of 8 | **+$33** (−$43 after 3-year depreciation) |
| Pilot only (P50 misses the ≥20/station scale gate) | **−$179** |

- **Break-even volume:** $300 net needs ~30 rentals per station.
- **P10:** 4 rentals → pilot killed; resale ~$150 → **88% loss** of the pilot.
- **P90:** 60 rentals per station → ~$1,358.
- **Gates:** fails payback and P10.

## P3 — PlacementDesk (paid-per-install location sourcing)
- **Capital:** $575 (Lob $245, Workspace and domain $55, Places $25, lawyer template $250).
- **Fixed costs:**
  - overheads $95/mo (Workspace, Places, Lob 100/mo);
  - tokens **$150**, for heavy research and writing;
  - ongoing sponsor time **1.5 h/mo ($450)**: operators are phone-first, hosts want calls, and attribution disputes need a human. Lesson §14 warns of 1–1.5 h *per week* for partner channels, so 1.5 h/mo is generous. The ideator had 0.5 h.
- **P50 volume:**
  - a 5–10% operator yes-rate, Q4 host inertia and a first install around Jan 2027;
  - then ~0.7 installs/month at $250, with residuals haircut to ~$6/mo each because collection depends on the operator's statements.
- **Result:** **−$482/mo at m12**. The ideator's $345 by month 4 assumed 2 installs/month and no sponsor cost. Even with 0.5 h of sponsor time, P50 is about −$180.
- **Break-even volume:** $300 net needs ~4 installs a month.
- **P10:** no installs; killed by m3; $575 lost plus $1,200 of setup time.
- **P90:** 3 installs/month at $300 → ~$505.
- **Gates:** fails the sponsor-hour gate. The capital is trivial; the business model is sponsor-time-negative.

## U5 — Vending machines, AI-managed, restocking outsourced (1, 2 and 3 machines)
**Capital per machine: $3,200.**
- refurbished combo with a Nayax/Cantaloupe reader: $2,250;
- liftgate delivery and install: $400;
- initial stock: $300;
- locator fee or outreach: $250.

**Business one-time costs: $300** (sales-tax and vending permits, first-quarter insurance).

**Per-machine P50: $450/mo gross.** That is a 30–60-staff site, the kind an independent can win.
- COGS 45% (Sam's Club buying, plus spoilage);
- commission 5%;
- card fees 5%;
- **sales tax 5%** (snacks and soda are taxable in most states; the ideator omitted it);
- telemetry $15;
- repairs $30;
- refunds $5;
- **leaves $130/machine before restocking.**

**Outsourced restocking at local rates:**
- a helper at ~$30/h all-in plus mileage, at 1.5 rounds a month;
- one round costs $60 for the first machine plus $25 for each additional site (shopping trip, drive and service);
- at TaskRabbit rates (~$50/h) every row below gets worse by $30–60.

**Business-level fixed:** insurance $50, tokens $60 + $10 per machine, sponsor (0.4 + 0.1 per machine) h × $300.

| Machines | Capital | Restock $/mo | P10 net ($150 gross/machine) | **P50 net** ($450) | P90 net ($1,000, 10% commission, 3 rounds) | Payback (P50) | P10 loss |
|---|---|---|---|---|---|---|---|
| 1 | $3,500 | $90 | −$345 | **−$263** | −$198 | never | 70% |
| 2 | $6,700 | $128 | −$425 | **−$243** | −$60 | never | 69% |
| 3 | $9,900 | $165 | −$505 | **−$223** | +$78 | never (P90 run-rate 57 mo) | 68% |

Nets are after $33 per machine per month of depreciation. P10 loss assumes resale at ~$1,050 net per machine.

- **What it would take:** a 12-month payback at 3 machines needs ≥ ~$1,800/mo gross *per machine*. Those are top-decile sites that incumbent route operators already hold.
- **Route-operator revenue share instead:** the sponsor's ~17% of gross at $450 × 3 machines ≈ $230, less tokens and sponsor time, is ~$60/mo against $6.75k → ~110-month payback.
- **Cap headroom:** 3 machines sit at $9,900, so any overrun breaches the $10k cap.
- **Verdict:** fails every capital-related gate at 1, 2 and 3 machines.
- **Only adjacent fix worth testing:** a "host-restocked" variant, in which the host's staff load delivered stock for a higher commission, mirroring P1's merchant-load. Even then, P50 stays under $300 below ~5 machines.

## Sources (accessed 2026-10-06)
- TrustMRR listings: [UltraWideo](https://trustmrr.com/startup/ultrawideo), [Wheel of Life](https://trustmrr.com/startup/wheel-of-life)
- Escrow.com fees, 2.4% (minimum $130) for $5k–50k: [escrow.com/domains](https://www.escrow.com/domains), [onlinedomain.com fee change](https://onlinedomain.com/2024/05/31/domain-name-news/escrow-com-fees-change-domain-sales-above-10k-take-a-big-hit/)
- Lulu print and fulfilment costs: [podvector Lulu pricing](https://podvector.ai/articles/print-on-demand/costs-and-suppliers/lulu-print-on-demand-pricing), [Lulu Print API fees](https://help.api.lulu.com/en/support/solutions/articles/64000254631-are-there-fees-to-use-lulu-s-print-api-)
- Vending revenue ranges (seller-biased; discounted): [vmfsusa: how much a vending machine makes](https://vmfsusa.com/blogs/business/how-much-can-a-vending-machine-make), [vmfsusa: realistic earnings](https://vmfsusa.com/blogs/starting-your-vending-business/how-much-can-a-vending-machine-really-make)
- Restocking labour and visit costs: [vmfsusa restock scheduling](https://vmfsusa.com/blogs/business/vending-machine-restock-scheduling-and-routes), [restocking cost overview](https://new.risingsunartscentre.org/news/cost-of-restocking-a-vending-machine-2026.html)
- Card-reader fees (Nayax ~5.95%): [carwashforum](https://carwashforum.com/threads/disgusting-fees-for-vending-machine.12417), [vmfsusa card readers](https://vmfsusa.com/blogs/business/best-card-readers-for-vending-machines)
- Power-bank utilisation: [Brick bar case study](https://articles.brick.tech/case-study-placing-a-powerbank-station-in-a-bar/), [Brick revenue FAQ](https://help.brick.tech/en/articles/6579962-what-will-my-revenue-look-like-month-to-month-with-brick)
- ATM volumes and fees: the ideator's beancount and ATM Marketplace sources, as cited in `physical-operator.md`
