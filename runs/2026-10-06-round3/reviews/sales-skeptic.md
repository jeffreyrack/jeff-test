# Sales Skeptic review: round 3 (2026-10-06)

Rules applied: `../PARAMS.md` ($10k cap, preferably under $1k; sponsor time at $300/h; physical labour outsourced), the operator constraints, the scoring rubric and lessons-learned §1–19. Today is **Tue 2026-10-06**, and every day count runs from today.

How "first sale" is defined for each idea type:
- **Q\* (acquisitions):** a deal that closes at or under the ideator's walk-away price, plus the first revenue after close.
- **B\* (paid ads):** the first paid order from the paid channel. A refundable pre-order counts.
- **P\* and U5 (physical):** the first revenue from a placed unit, or for P3, the first invoice paid.

| ID | Idea | Score | P(≤30d) | P(≤90d) | P50 days | P90 days | Kill shot |
|---|---|---|---|---|---|---|---|
| Q1 | UltraWideo-class extension acquisition | 3 | 2% | 22% | Never at ≤$8.5k (≈75 if the seller accepts) | Never | The seller won't take 35–46% off a $13k ask on verified revenue. Lemon Squeezy subscriptions can't move, so a Stripe migration loses 30–50% of monthly subscribers. |
| Q2 | Wheel of Life-class app acquisition | 4 | 2% | 30% | Never at ≤$8k (≈60 if the seller accepts) | Never | The seller won't sell at ~1× gross six weeks before the Dec–Jan peak, which is ~28% of annual revenue. |
| Q3 | Standing fire-sale buy order (≤$3k) | 2 | 1% | 10% | Never | Never | No qualifying deal shows up, or it clears within hours to faster buyers. |
| B1 | HSK 3.0 speaking mock, paid search | 5 | 30% | 60% | ≈45 | Never | Too few English searches for the new terms. Google marks the keywords "low search volume", the $200 can't buy enough clicks, and the ~$8 official mock caps price. |
| B2 | SubWatch, OSHA monitoring for general contractors | 3 | 2% | 22% | >180 | Never | The free 5-sub check meets the one-time pre-award need. Almost nobody puts a card down for monitoring, so $500 buys ~0.4 expected customers. |
| B3 | Heirloom recipe-card cookbook, Q4 gift | 6 | 50% | 80% | ≈26 | ≈75 (never if the Meta ad account is restricted) | Cold conversion for a $119 brand with no reviews is ~1%, so CAC is ~$100 against a $47 gate. The first sale probably happens; scale is killed on Nov 8. |
| P1 | Merchant-loaded ATMs | 3 | 1% | 22% | ≈140 | Never | A merchant with ≥150 withdrawals a month already has an ATM. The ones answering postcards are the ones the ISOs dropped for low volume. |
| P2 | Power-bank stations in bars | 4 | 3% | 45% | ≈95 | Never | Bar owners ignore the mail, and US rentals at small venues run 2–8 a month, not 20. |
| P3 | PlacementDesk, location sourcing for operators | 2 | 1% | 10% | >180 | Never | Two-sided cold start with no phone. Hosts don't answer postcards, and operators circumvent the fee or install in Feb–Mar. |
| U5 | Owned vending machines, outsourced restocking | 3 | 1% | 20% | ≈150 | Never | Signing the host needs a site visit and a person they trust. The weekly restocker is the unreliable link and eats most of the margin at 1–3 machines. |

**Bottom line:**
- **B3 is the only idea where a stranger is likely to pay within 30 days**, because it uses a proven paid gift channel in peak season. Even so, the cash it makes per order probably won't cover the ads.
- **The acquisitions (Q1, Q2) have the best revenue after close** of anything seen in three rounds. Their binding risk is **price acceptance, not demand.**
- **All four physical ideas (P1–P3, U5) have P50s beyond 90 days.** In every case the cause is signing the location, not the end customer.

---

## Q1: UltraWideo-class aged subscription extension

**First buyer:** UltraWideo's founder (Devilos LLC). He must accept $7,000–8,500 against a $13,000 ask. After close, the buyers are existing Pro subscribers, plus a 34" ultrawide owner who searches "black bars" in the Chrome Web Store.

**Is a deal findable and closable?**
- **Fantasy at the target price, optimistic at walk-away.**
  - Revenue is API-verified and sellers on TrustMRR anchor hard. The ideator's own Bulk File Downloader example shows a seller re-anchoring *upward* after a listing failed.
  - My fetch of the TrustMRR startup page on 2026-10-06 showed no for-sale flag or asking price. **Confirm the listing is still live before spending any sponsor time.**
- The likely P(seller accepts ≤$8.5k) is about 25–30%. Raise it with an earn-out (below).

**Does revenue hold after transfer?** This is the hidden kill shot.
- Lemon Squeezy is a merchant of record. Its docs list multiple stores per account but no ownership-transfer route that I found. Merchants of record generally don't export card tokens to Stripe.
- So option (b), "migrate to Stripe", means every monthly subscriber re-enters a card. Expect a 30–50% loss of monthly subscribers, not 15–30%. Annual subscribers survive only until renewal.
- Option (a), buying the entity, is the only clean path. It adds lawyer time and liability review, which pushes close from day 45 to about day 60–75.

**Revenue trend:** MRR is −21% over 30 days, and the last 4 months fell from $764 to $358. That is decay, not seasonality, until shown otherwise.

**Steelman:** 70k installs and 591 reviews are the one thing an AI clone can't copy. In-product conversion work on 86k users is real leverage.

**Timing:** neutral.

**Score: 3.**
- **Kill shot:** the price gap plus subscriber loss in a billing migration.
- **Fix:** offer **$5,000 cash plus a 12-month earn-out of 30% of gross, capped at $4,000**, structured as an entity purchase. This puts the seller near $9k, protects against decay, and avoids migrating subscriptions.

## Q2: Wheel of Life-class subscription app

**First buyer:** the Wheel of Life founder. The listing is confirmed live on TrustMRR today. After close, the buyers are the ~1,800 organic installs a month from App Store and Play search.

**Is a deal findable and closable?**
- **Optimistic.** The offer is $6,500 against $11,111, which is 41% below ask.
- TrustMRR's own copy says "~74% margin after store fees", so the $6,648 TTM is **gross**. Net is about $4.9k a year, which makes $6,500 roughly 1.3× net. That is a defensible number, but timing works against it.
  - Closing by Dec 1 is needed to capture the New Year spike, and the seller can see the same chart. Dec + Jan last year were $1,893, about 28% of TTM.
  - A rational seller either waits for January to re-list on a fresh peak or prices that peak in.
- P(accept ≤$8k by Dec 1) is about 30%.

**Does revenue hold after transfer?** Much better than Q1.
- Apple and Google app transfers carry subscriptions, and RevenueCat projects transfer.
- **Hidden risk:** MRR is $181 against $552 in the last 30 days. That means about two-thirds of monthly cash comes from new annual and lifetime purchases, not renewals. That's fine if the install flow holds, but the "lifetime <40% of TTM" gate may fail.

**Day count:**
- Apple organisation enrolment with D-U-N-S takes 2–3 weeks.
- Then the LOI, APA, escrow and transfer.
- Realistic close is **day 55–70**, landing around Dec 1–15. That is borderline for the peak.

**Steelman:** placement in two stores, 4.7–4.8★, and verified revenue whose peak arrives right after a close in late November.

**Score: 4.**
- **Kill shot:** the seller refuses ~1× gross right before the peak.
- **Fix:** offer a **price that rises with January revenue**: $6,000 at close plus 50% of Jan 2027 net revenue above $700. The seller gets paid for the peak, and the buyer is covered if it doesn't come.

## Q3: Standing fire-sale buy order (≤$3,000, ≥$450/mo verified, ≥12 months of history)

**First buyer:** a serial builder dumping an asset. The ideator's own evidence is that every qualifying example had **already sold**.

**Deal flow:**
- **Fantasy at P50.** The buy-box (≤0.55× annual revenue, verified, 12+ months, no LLM COGS, slope no worse than −10%) is stricter than any live listing found today.
- Microns and TrustMRR fire-sales clear in hours to days, against buyers with alerts and their own agents.
- A sponsor who must "act within 48 h" loses those races. Each fire drill also costs $75–150 of sponsor time.
- I put P(qualifying deal in 90 days) at **10–15%**, not 35%.

**Adverse selection:** the ideator already concedes that the P10 fails. Anything priced at 0.3–0.5× that survives a day on the market is usually decaying.

**Steelman:** the capital stays in T-bills if nothing qualifies, so the downside is only a few hours of memo reading.

**Score: 2.** It is an option, not a business.
- **Kill shot:** no deal clears the box before a faster buyer takes it.
- **Fix:** go off-market. Have the AI screen TrustMRR's **unlisted** verified-revenue startups for abandonment signals (no commits or updates in 6+ months, unanswered reviews). The sponsor sends ≤10 personal "would you sell?" notes a month. That brings deal flow nobody else is racing for.

## B1: HSK 3.0 Speaking Mock

**First buyer:** a US/UK learner at HSK 3–4 level, registered for the **13 Dec 2026** first worldwide HSK 3.0 sitting (confirmed by several prep sites), who googles "HSK 3.0 speaking practice".

**Channels:**
- **Google exact/phrase match is optimistic.** Its intent is real, but the volume probably isn't.
  - English searches for "HSK 3.0 speaking" are likely tens to low hundreds a month across the target countries.
  - Google flags terms with "low search volume" as ineligible to serve.
  - The plan needs about 285 clicks at $0.70 inside 14 days. Expect the $200 to under-deliver, or to need broad match, which brings junk.
- **Reddit Ads is optimistic.** About 80 clicks at a 1–2% conversion rate gives about 1 pre-order.
- **Affiliates are fantasy within 30 days.**

**Conversion math:**
- Cold pre-orders for an unbuilt $29 product from an unknown site convert at about 1–2%, not 3.8%.
- That gives 4–7 pre-orders from roughly 350 clicks, so the "≥8 at CAC ≤$22" pass is unlikely. The likely outcome is the "5 plus 60 sign-ups" retest branch, or a kill.

**Alternatives:**
- the official HSK mock (≈$8);
- Mandarin Temple ($19/mo, which includes mocks);
- ChatGPT voice role-play (free).

**Trust gap:** moderate. $29 is impulse-sized, and the free demo task helps.

**Timing:** excellent. The first sitting is 68 days out.

**Steelman:** a new exam format, a hard date and anxious candidates is the most purchase-ready intent in all of round 3.

**Score: 5.**
- **Kill shot:** too little search volume to run a valid test.
- **Fix:** before building, check volume in Google Keyword Planner (sponsor account, $0). Make the **Reddit cell the primary test**, and add one paid newsletter or YouTube sponsorship slot with an HSK creator ($100–200) for audience that actually exists.

## B2: SubWatch, OSHA history monitoring for general contractors

**First buyer:** the prequalification coordinator at a 40-person regional GC who searches "subcontractor OSHA history".

**Channels:**
- **Google Search is optimistic on volume and fantasy on intent mix.**
  - "OSHA violations by company" and similar terms are mostly searched by journalists, job-seekers, students and homeowners.
  - The B2B prequalification slice is small.
  - The new 2026-10-05 government-documents policy is a real disapproval risk.
- **Bing** has the same problem with less volume.
- **LinkedIn retargeting** is meaningless at this lead count.

**Conversion math:**
- $500 at $3.50 buys about 143 clicks. At 10% that's about 14 free checks.
- The plan assumes **8%** free→paid with a card on file, for an anonymous $79/mo tool with no sales calls. A realistic rate is 2–4%.
- That gives **0.3–0.6 expected customers** from the whole test, so the pass rule (≥3 trials) needs the P90 case.
- The 14-day trial pushes the earliest paid conversion to about day 30–35.

**Why they wouldn't pay:**
- The free check **gives away the unit** (lesson §12). Pre-award vetting is a one-time lookup per sub, and the free tool does it.
- "Monitoring" is a need the buyer has to be taught.
- Larger GCs already push prequalification costs onto subs through Highwire, ISN or Avetta.
- Small GCs just use the free OSHA search.

**Timing:** neutral to slightly negative. Prequalification renewals cluster in Jan–Mar.

**Steelman:** a sticky, budgeted B2B workflow with LTV around $1,600. Even one customer a month compounds.

**Score: 3.**
- **Kill shot:** the free check satisfies the need, and nobody converts to monitoring.
- **Fix:** cap the free tool at **1 sub**, gate the 5-sub report and PDF behind a paid $29 one-off "prequal pack", and test that before monitoring.

## B3: Heirloom recipe-card cookbook (Q4 gift)

**First buyer:** a 45-year-old woman on Instagram in late October who sees a card-to-page reveal ad and buys a $119 certificate for her mother.

**Channels:**
- **Meta is realistic for a first sale and optimistic for the economics.**
  - A brand-new ad account with no pixel history doesn't exit the learning phase on $300.
  - New Business Manager accounts often hit spend limits or reviews, which is a day 16 → day 20+ risk.
- **Google high-intent search is realistic** but low volume.
- **Pinterest Ads is optimistic.**

**Conversion math:**
- A $119 brand with no reviews on cold social converts at about **0.8–1.5%**, not 2.5%.
- At $1.05 CPC that gives a **CAC of $70–130**.
- The $500 test yields about 4–7 orders, so the first sale is likely. The pass rule (≥10 orders at ≤$47) is unlikely.

**Why they'd pay versus the alternatives:**
- Mixbook and Shutterfly make you type every recipe.
- Storyworth is a different product.
- **Etsy sellers** already turn handwritten recipes into cookbooks, with reviews.
- Apps exist (lesson §19).
- The "we transcribe it" angle is a real differentiator.

**Trust gap:** high for $119 from a site with no reviews, and the book arrives in January.

**Fulfilment:** Lulu prints in 3–5 days but ships slowly in December. The "upload by Nov 20 → under the tree" promise is an FTC Mail Order Rule hazard. Keep the claim conservative.

**Timing:** peak. This is the best in round 3.

**Steelman:** the gift-certificate structure sidesteps the print cutoff and catches the last-minute December buyer, the highest-intent shopper of the year.

**Score: 6.**
- **Kill shot:** CAC of about $100 against a $47 gate.
- **Fix:**
  - Order the samples on **day 1**, not day 4.
  - Seed 5–8 real books for friends and family to get reviews and UGC before ads.
  - Spend the first $200 on Google exact-match "recipe cards into cookbook" terms, and use Meta only for retargeting until the pixel has conversions.

## P1: Merchant-loaded ATMs

**First buyer (host):** a cash-tip nail salon owner who just lost an ISO's ATM. The end user is a client paying $3.25 to withdraw.

**Who signs the host, and how fast?**
- Lob postcards from an unknown AI-run company offering a "free ATM" compete with ISOs that pitch in person.
- 300 cards at a 0.5–1% response rate gives 2–3 replies. Getting ≥3 signatures *and* ≥150-withdrawal evidence in 3 weeks is fantasy.
- Most merchants want a person on site before bolting a safe to their floor. That means the $100 field rep, if one can be found, or the sponsor at $300/h.

**Adverse selection:**
- A merchant with ≥150 withdrawals a month already has a free ATM, because ISOs place at 100+.
- Merchants whose machines were "removed" mostly lost them for low volume.
- A merchant savvy enough to load cash can buy its own refurbished unit and keep 100%.

**Is the outsourced labour done?**
- Mostly yes. The merchant loads cash because it gets 40%, and ATM techs exist in every metro.
- Processor/ISO onboarding and KYC (1–3 weeks) plus freight push the first transaction to about **day 90–150**.

**Timing:** neutral to positive (holiday cash).

**Steelman:** the merchant does the labour for a 40% split, a physical moat, and verified transaction data from day 1.

**Score: 3.**
- **Kill shot:** good-volume merchants are already served.
- **Fix:** target **cash-only businesses with no ATM within 0.25 mi** and new openings (from business-licence feeds). Hire the local commission rep from day 1 rather than as an option.

## P2: Power-bank stations in bars and breweries

**First buyer (host):** the owner of a neighbourhood brewery that stays open late. The end user is a guest at 3% battery who needs an Uber.

**Who signs the host?**
- Bar owners rarely act on postcards or info@ emails. 150 contacts likely gives **1–2 signatures, not 4**.
- The ask is low-friction (plug it in, get 20%), which is the steelman.

**Speed:** sea or DG-air lithium freight plus customs takes 25–45 days. First live station around **day 70–100**, unless the express sample is deployed.

**Is the outsourced labour done?**
- Plausibly. Plugging in is trivial.
- But stations get unplugged to free outlets, banks walk, and staff don't troubleshoot. The AI can only email.

**Conversion math:**
- First rental is near-certain once a station is live. Even 4 rentals a month gives a first sale within about 7 days.
- Brick's European data shows about 1 rental a day at *good* venues. AnkerBox failed in the US.
- 20 rentals a month at a small US bar is optimistic. The $300/mo fleet target is fantasy at P50.

**Timing:** positive (holiday parties).

**Score: 4.** First revenue is plausible but late, and it is tiny.
- **Kill shot:** venues don't sign by mail, and utilisation of 2–8 rentals a month.
- **Fix:** put the express sample station live at the **first** signed venue by about day 25, to pull first revenue and real utilisation data forward before the pilot order.

## P3: PlacementDesk (location sourcing for route operators)

**First buyer:** the owner of a 15-machine vending route who says yes to a pay-on-install referral agreement.

**Two-sided cold start:**
- **Operators: optimistic.** Pay-on-install is attractive, but the yes-rate is 5–15% and each yes needs a sponsor call.
- **Hosts: fantasy at the planned pace.**
  - 400 postcards gives 2–4 replies.
  - Workplaces with 40+ staff mostly already have vending or a micro-market.
  - Q4 facilities decisions stall, as the ideator concedes.
- **The operator then has to act.** Operators are slow, especially for a ~$650/mo machine, and "we already knew them" circumvention is common.

**Cash timing:** the first Net-15 invoice is paid around **day 150–200**.

**Timing:** Q4 off-season. **−1** applied.

**Steelman:** zero inventory, under $600 at risk, and a pitch ("pay only on install") that beats the distrusted upfront-fee locators.

**Score: 2.** The P50 is above 180 days, which is a **hard-gate risk**.
- **Kill shot:** hosts don't respond, and operators circumvent the fee.
- **Fix:** source hosts from **new-facility signals** (certificates of occupancy, new warehouse leases, new business licences). New buildings have no vending incumbent and a fresh decision-maker, and the AI can mine this public data.

## U5: Owned vending machines with outsourced restocking

**First buyer (host):** the office manager of a 60-person warehouse with no break-room vending.

**Who signs the host, and how fast?**
- Hosts expect a site visit: power, doorway width, placement, and a face they can call.
- The AI can't visit. The sponsor costs $300/h. Locators at $200–500 have a poor reputation for placement quality.
- Good hosts are already served by route operators who restock weekly and handle service.
- A realistic first signed placement is **day 45–90**. Then come the machine purchase, freight, and a two-person move with a pallet jack.
- First vend is around **day 100–160**.

**Is the outsourced labour done?** This is the weakest link.
- A TaskRabbit or Craigslist restocker has to buy stock, rotate expiry dates, count cash and show up weekly, unsupervised.
- At 1–3 machines no professional restocker prioritises you. Missed visits mean empty slots, and empty slots lose the host.
- A visit at $25–40 a week is $100–160/mo per machine, against a typical $300–800 gross with 45% COGS.

**Timing:** slightly negative (Q4 office decisions).

**Steelman:** the end demand (snacks at work) is proven and needs no marketing once the machine is in place.

**Score: 3.**
- **Kill shot:** no host signs without a visit, and restocking reliability and cost eat the margin.
- **Fix:** acquire an **existing 1–3 machine mini-route with locations already signed** (BizBuySell or Craigslist). That buys the placement and the restocking relationship together, and turns it into an acquisition problem like Q\*.

---
Sources checked on 2026-10-06:
- [TrustMRR UltraWideo](https://trustmrr.com/startup/ultrawideo)
- [TrustMRR Wheel of Life](https://trustmrr.com/startup/wheel-of-life)
- [Lemon Squeezy, multiple stores](https://docs.lemonsqueezy.com/help/your-account/multiple-stores)
- [Lemon Squeezy, migrating from Gumroad](https://docs.lemonsqueezy.com/help/migrating/migrating-from-gumroad) (no subscription-migration path)
- [HSK 3.0 Dec 13 launch (hsklord)](https://hsklord.com/blog/hsk-3-0-changes-2026)
- [GoEast Mandarin, HSK dates](https://goeastmandarin.com/hsk-exam-dates-details/)
