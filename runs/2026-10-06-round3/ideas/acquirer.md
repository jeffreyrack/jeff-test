# Ideas: The Acquirer (round 3, capital allowed)

The binding parameters are in `../PARAMS.md`: a $10k hard cap, $300/h sponsor time, a P50 payback of 12 months or less above $1k, P10 losing no more than about 50% of capital, and a 4%/yr T-bill benchmark.
Research date: **2026-10-06**. All listings were read from public pages on that date. I contacted no sellers and created no accounts.

## Market reality check (read this first)

**Inside the $10k cap, real businesses that earn $300/mo or more are rare.** Here is what is listed today:

- **TrustMRR `/acquire`, first page (30 listings, revenue verified via payment-provider API).** Only 3 ask $10k or less:
  - FigForm: $4,900, $0 revenue.
  - Brevik: $4,900. It shows $490 in the last 30 days, but was founded 2026-08-10, has 3 users and $0 MRR.
  - OUT23: $10,000, $0 revenue.
- **The aged, real assets ask a little above the cap.** All of these have to be negotiated down:

  | Asset | Ask | Verified revenue | Implied multiple |
  |---|---|---|---|
  | UltraWideo | $13,000 | $4,684 TTM | 2.8× |
  | Wheel of Life | $11,111 | $6,648 TTM | 1.7× |
  | Toeic Mastery | $12,000 | 3 months of data | n/a |
  | VoiceBrief | $12,000 | $2,223 TTM | 5.4× |

- **Flippa, plugins & extensions category (21 listings):**
  - All 10 listings under $10k are under 1 year old (except Verify It, 5 years old, which reports no revenue).
  - The best monthly profit among them is **$129/mo** (Reelyzer, asking $9,900).
  - The rest show ≤$30/mo or no revenue: Sell 9 Shopify Apps ($9,899 for $30/mo), WooAccount ($6,480), AddiPress ($8,099), AskScoobyAI (−$87/mo).
  - This is lessons-learned §19 seen from the sell side: AI-built clones are now being flipped as "businesses".

**Typical multiples cannot pass the 12-month payback gate.**
- A 12-month payback means paying at most **1× annual net profit**.
- Healthy small assets trade at 2–4× annual profit, which is a 24–48 month payback.
- The only sub-1× deals I found had already **sold**, and fast:
  - Microns "AI YouTube Growth Platform": $3,000 for a claimed $1,250/mo.
  - "Old Photo Restore iOS": $2,000 for $151 MRR.

**My honest summary:**
- **Q1 and Q2 are good businesses at the wrong multiple for this gate.** Both pass the P10 test and beat T-bills by 10×, but their P50 payback is 19–26 months.
- **Q3 is the only route that can meet 12 months, and only marginally.** It also has a worse P10.
- **Recommendation to the committee:** either relax payback to about 24 months for verified-revenue acquisitions, or run Q3 as a standing buy order that only fires on a qualifying deal. If no deal qualifies, the capital stays in T-bills.

---

## Q1 — UltraWideo-class aged subscription browser extension

- **Persona:** The Acquirer
- **One-liner:** Buy a 5-year-old Chrome + Firefox extension with a paid Pro subscription. Its Chrome Web Store / AMO placement (70k+ users, 591 reviews, "Featured" badge, 41 languages) can't be cloned. The AI operator then runs maintenance, support, listing optimisation and pricing.
- **Example listings (real, current):**
  1. **UltraWideo** ([trustmrr.com/startup/ultrawideo](https://trustmrr.com/startup/ultrawideo)) — **lead target**.
     - Price and revenue:
       - Asks **$13,000**.
       - Revenue is verified via the Lemon Squeezy API: **$4,684 TTM**, $1,411 in the last 3 months, **$346 MRR** from 130 active subscriptions.
       - Last 30 days: $440 (−8%), with MRR down 21% over the same period.
     - Monthly gross revenue for Nov 2025 → Sep 2026: $212, $365, $189, $147, $168, $388, $700, $764, $476, $588, $358.
     - Founded 2021-07. Publisher: Devilos LLC (Wyoming).
     - Chrome store: 70k users, 4.2★ from 591 reviews, MV3, v4.2.0 (per [extscope](https://extscope.org/extension/bfbnagnphiehemkdgmmficmjfddgfhpl)).
     - Firefox store: 15,860 users, 4.4★ from 239 reviews, updated 2026-09-08 (per [AMO](https://addons.mozilla.org/en-US/firefox/addon/ultrawideo/)).
     - Pro is $2.99/mo or $29.90/yr. The seller claims 100% margin and no marketing ever.
  2. **Bulk File Downloader** ([flippa.com/12839069](https://flippa.com/12839069)): asks **$21,000**.
     - Claims $546/mo profit, 17.4k active users and a $9.99 one-time Pro via Stripe.
     - Rating 3.2★ from 54 reviews; churn 71%.
     - The same asset was earlier listed at **$10,000** ([flippa.com/12085118](https://flippa.com/12085118), ended). The seller re-anchored *up* after it did not sell. This is useful negotiation evidence: at $10k the market did not clear it.
  3. **Anti-examples (in budget, not businesses):**
     - Reelyzer ([flippa.com/14173315](https://flippa.com/14173315)): $9,900 for $129/mo, under 1 year old.
     - Notate ([flippa.com/13592033](https://flippa.com/13592033)): $2,000 for $21/mo.
- **Price / multiple / payback:**
  - Offer and walk-away:
    - Target offer **$7,000** (1.5× TTM revenue, about 2× TTM net).
    - Walk-away **$8,500**.
  - P50 economics:
    - Monthly net **~$290** (year-1 average).
    - Payback **~26 months**. **FAILS the ≤12-month gate.** Passing would need an all-in price of about $3,500 or less, which is unrealistic against a $13k ask.
    - Annualised return on capital: ~46% steady state, ~22% in year 1 after sponsor hours. T-bills earn 4%.
- **Due-diligence checklist:**
  - **Billing transfer (the #1 risk).** Lemon Squeezy subscriptions can't be moved between stores. Pick one of these and get it confirmed in writing before the LOI:
    - (a) buy Devilos LLC itself: an entity purchase with liability review, a new beneficial owner and Lemon Squeezy KYC;
    - (b) seller-assisted migration to the buyer's Stripe. The seller says a "Stripe integration is built and switchable". Expect 15–30% of subscribers to be lost;
    - (c) a Lemon Squeezy-supported store-ownership transfer, if it exists. Verify with Lemon Squeezy, not the seller.
  - **Read-only billing access.** Get read-only Lemon Squeezy API or finance access, and reconcile against TrustMRR. Check refunds and chargebacks (<3%), annual vs monthly mix, and country mix.
  - **Chrome Web Store.** Check the ownership-transfer path, policy-strike history, and MV3 compliance. "Medium-risk" permissions (tabs, all-site data) are a likely review-scrutiny point.
  - **Firefox (AMO).** Add the buyer as an author, then remove the seller.
  - **Install trend.** Get weekly-user history for 12 months from the CWS developer dashboard (export) or chrome-stats. It must be flat or rising.
  - **Code.** The repo must build from clean; the GitHub repo is connected per TrustMRR. Also inventory the self-hosted licensing API on Railway, the Cloudflare site, the domain `uw.wtf`, and the Discord server.
  - **Clone audit (§19).** Competitors include:
    - Zoom to Fill Ultrawide Video (200k+ users);
    - Ultrawidify (free, open source);
    - Ultrawide Fill (newer).

    Count same-pitch listings launched in the last 90 days and their user numbers. Free alternatives cap pricing power.
  - **Seasonality.** May–Jun 2026 was $700–764/mo against ~$150–200 in Jan–Mar. Find out why: a feature, a store feature placement, or a one-off spike.
- **Demand test:** Due diligence plus verified revenue. Money moves only if **all** of these pass:
  - trailing 6-month verified gross is **≥$400/mo**, and MRR is not down more than 15% over 6 months;
  - no single month is more than 25% of TTM;
  - active subscribers are ≥120 on the closing date, with an escrow clause to adjust price if they are lower;
  - the billing-transfer route is confirmed in writing;
  - CWS weekly users are ≥65k and not declining;
  - price ≤ $8,500.

  **Fail any one and walk away.**
- **Customer:**
  - End users: owners of ultrawide (21:9/32:9) and multi-monitor setups, streamers, and film/anime viewers on Netflix, Prime, Disney+ and YouTube.
  - They find the product by searching the Chrome Web Store and Firefox Add-ons.
  - They already pay for streaming subscriptions and $1,000+ monitors.
- **Problem / desire:** "I bought a 34-inch ultrawide and Netflix still shows a third of the screen as black bars."
- **Offering:** A browser extension: free core plus Pro ($2.99/mo or $29.90/yr) with per-site profiles, letterbox detection, ambient light, sharpening and cloud sync.
- **Price & revenue model:** Subscription via Lemon Squeezy (merchant of record) or Stripe. The planned changes are listed under growth levers in the acquisition plan.
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Purchase price (target; walk-away $8,500) | $7,000 |
| Escrow.com fee (~3.25%; verify) | $230 |
| Domain transfer/renewal (`uw.wtf`) and CWS dev registration ($5) | $35 |
| Operating reserve (hosting, buffer) | $300 |
| **Total** | **$7,565** (walk-away case ≈ $9,100) |

### Monthly running costs (excluding operator tokens)
- **Lemon Squeezy fees:** 5% + $0.50 per transaction. That is ~22% on a $2.99 monthly charge and ~7% on a $29.90 annual one, so about 12% blended (~$47).
- **Hosting:** Railway licensing API, Cloudflare and site, ~$20.
- **Domain:** ~$3 amortised.
- **Operator tokens:** $60 at P50, because this is a light-touch, mature product.

**Monthly net by case**

| Case | Gross | Net/mo | Payback | Notes |
|---|---|---|---|---|
| P50 | $390 (TTM average) | ~$260 at close, ~$330 by month 6 | ~26 months | Year-1 average **~$290**. Year-1 profit after one-time sponsor hours (6 h × $300 = $1,800): ~$1,680. |
| P10 | ~$250 (YouTube/Netflix DOM changes, MV3 policy friction, subscriber loss in billing migration) | ~$120 | — | 12 mo × $120 = $1,440, plus resale at ~1.2× TTM (~$3,000), recovers ~$4,440 of $7,565: **−41%**, inside the 50% limit. With no resale buyer: −81%. |
| P90 | ~$650 (price lift and annual mix work, Edge listing adds 10–15%) | ~$500 | ~15 months | |

### Customer acquisition plan
The existing store placement is the channel.
1. **Chrome Web Store, AMO and Edge listings:** the AI operator rewrites the listings and screenshots, A/B tests the store icon and screenshots, and localises copy into the 41 supported languages.
2. **In-extension upgrade prompts:** the AI operator improves the free→Pro upgrade path.
3. **Annual-plan default:** fixes the $0.50 fixed-fee drag and lowers churn.
4. **Pricing:** new monthly subscribers pay $3.49; existing subscribers are grandfathered.

The core loop is: organic installs → free use → a contextual Pro prompt at the moment of letterboxing → annual checkout.

### Initial traffic approaches (ranked by expected speed)
1. **In-product conversion work** on the existing ~86k users across Chrome and Firefox. No new traffic is needed, so the effect shows within 2–4 weeks of close.
2. **Microsoft Edge Add-ons listing.** Edge is Chromium, so this is the same codebase in a new marketplace with its own search. Expect 2–6 weeks for review and first installs.
3. **Store SEO and localisation** across CWS and AMO, aimed at searches like "black bars" and "ultrawide". Expect 1–3 months.
4. **The existing blog/SEO site** (34.7k Google impressions in 30 days, domain rating 3). Content refreshes only, with no scaled AI content. Expect 3–6 months.

### Path to first sale
- **Days 0–10:** DD request through TrustMRR, done by the sponsor's account (not this agent); NDA; read-only billing.
- **Days 10–25:** verify, then LOI, with the billing-route decision and lawyer-reviewed asset purchase agreement (APA) template.
- **Days 25–45:** escrow; transfer of CWS, AMO, domain, repo, Railway, Cloudflare and billing.

First revenue arrives **at close (~day 40–50)**. First cash comes at the next Lemon Squeezy/Stripe payout, about 1–2 weeks later.

### Who does what
- **AI operator:**
  - before close: DD analysis on read-only data, code audit, the transfer checklist, and clone and install-trend audits;
  - after close: MV3 and site-compatibility fixes, support (email `contact@uw.wtf`; Discord support only as a disclosed bot inside the owned server), listing and pricing experiments, the Edge port, monitoring and bookkeeping exports.
- **Human sponsor:**
  - one-time, ~6 h ($1,800): TrustMRR contact and NDA, LOI and APA signature, escrow funding, Lemon Squeezy/Stripe KYC, accepting the CWS transfer, AMO account, and domain registrar;
  - recurring, ~0.5 h/mo: payout and tax admin. This is within the gate of net ÷ $300 ≈ 1 h.

### Moat — why not just ask ChatGPT?
- The product runs inside the browser on every video player, which a chatbot can't do.
- An AI *can* rebuild the code in a week, as §19 warns. What it can't rebuild quickly is 70k installs, 591 reviews, the Featured badge, 5 years of store ranking history and 130 paying subscribers.
- The real competition is free incumbents (Ultrawidify; Zoom to Fill, 200k users), not ChatGPT. That caps price increases.

### Biggest risks (ideator's own view)
- **Billing transfer may lose 15–30% of subscribers**, unless the deal is an entity purchase, which carries inherited-liability risk. Lemon Squeezy's long-term future after Stripe's acquisition is also a platform risk.
- **The multiple:** even at $7k this is a ~26-month payback. It fails this run's gate unless the committee relaxes it.
- **Platform fragility:** a Netflix or YouTube player change, or a CWS policy action on broad permissions, can break the core feature or the listing overnight.

---

## Q2 — Aged subscription mobile app with an established review base (Wheel of Life-class)

- **Persona:** The Acquirer
- **One-liner:** Buy a 3–5-year-old iOS + Android self-improvement app with RevenueCat subscriptions, 500+ reviews at 4.7★ and ~1,800 organic installs a month. The AI operator runs app store optimisation (ASO), paywall and pricing tests, localisation and support.
- **Example listings (real, current):**
  1. **Wheel of Life** ([trustmrr.com/startup/wheel-of-life](https://trustmrr.com/startup/wheel-of-life)) — **lead target**.
     - Asks **$11,111**.
     - Revenue verified via RevenueCat: **$6,648 TTM**, $2,798 over 6 months, $552 in the last 30 days, **$181 MRR** from 122 active subscriptions.
     - Monthly revenue for Nov 2025 → Sep 2026: $315, **$830, $1,063**, $532, $616, $384, $583, $386, $430, $469, $513. There is a clear New Year spike.
     - Live since 2021; TrustMRR founded date 2023-03.
     - Store standing: 10k+ Play downloads at 4.7★ (500+ reviews); 4.8★ on the App Store; ~27k users.
     - Pricing: $1.99/mo, $14.99–29.99/yr, lifetime $24.99–39.99. The seller states 85% margin.
     - The sale includes both store apps, source code, the domain, the RevenueCat project and handover support.
  2. **Old Photo Restore iOS** ([microns.io](https://www.microns.io/startup-listings/old-photo-restore-ios-app)): **sold** for ~$2,000.
     - Numbers: $151 MRR, $1,900 annual revenue, 4.8★ from 60 reviews.
     - The founder exited because of app-admin burden. That burden is exactly what an AI operator plus a $300/h sponsor has to price in.
     - This is the comparable for a ~1× revenue exit.
  3. **Anti-examples:**
     - **Toeic Mastery** ([trustmrr.com/startup/toeic](https://trustmrr.com/startup/toeic)): asks $12,000 on only $928 all-time revenue, 6 subscriptions and 3 months of history.
     - **Blur Your Bub** ([trustmrr.com/startup/blur-your-bub](https://trustmrr.com/startup/blur-your-bub)): asks $15,000 on $241 in the last 30 days.
- **Price / multiple / payback:**
  - Offer and walk-away:
    - Target offer **$6,500** (~1× TTM gross, ~1.4× TTM net after store fees).
    - Walk-away **$8,000**.
  - P50 economics:
    - Monthly net **~$370** (year-1 average, including the January peak).
    - Payback **~19 months**. **FAILS the ≤12-month gate.** Passing needs about $4,400 all-in, roughly 0.65× TTM.
    - Annualised return: ~62% steady state, ~29% in year 1 after sponsor hours.
- **Due-diligence checklist:**
  - **Gross vs proceeds.** Confirm whether RevenueCat's $6,648 is gross or proceeds net of the store commission. It changes net by 15–30%.
  - **App Store Connect and Play Console.** Get read-only finance and sales reports for 12 months. Check refund rate, trial-to-paid conversion and renewal rates by plan. Find how much of TTM is lifetime purchases, which are not recurring.
  - **Transfer eligibility.**
    - Apple app transfer: both accounts in good standing; check whether any transfer-blocking entitlements or features apply.
    - Google Play app transfer: subscriptions and users carry over; verify against the current docs.
    - RevenueCat project ownership transfer.
    - Small Business Program (15%) enrolment for the buyer's developer account.
  - **Backend inventory.** Check whether the apps need a server or Firebase, plus its cost and credentials. Check the React Native / Flutter versions, Xcode/SDK currency, and whether a fresh build compiles and passes review.
  - **Data and privacy.** Life-satisfaction and journaling data is sensitive-adjacent. Check the privacy policy, GDPR handling and account deletion. Strip any therapy or medical claims from the listing copy ("coaches and therapists use it").
  - **Clone audit (§19).** There are several "Wheel of Life" apps on the App Store, for example "Wheel of Life: Mentor yourself" and "Evaluation Wheel". Record their ratings and review counts and their keyword overlap.
- **Demand test:** Due diligence plus verified revenue. Money moves only if **all** of these pass:
  - proceeds (after store fees) over the trailing 6 months are **≥$380/mo**;
  - lifetime purchases are under 40% of TTM;
  - active subscriptions are ≥110 at close, with an escrow price adjustment if lower;
  - a fresh build passes TestFlight / internal testing before close;
  - both stores confirm the transfer is eligible;
  - price ≤ $8,000.

  **Timing matters (§3):** to capture the Dec–Jan peak in year 1, the deal must close by about 2026-12-01. If it can't, renegotiate down, because the buyer would miss ~25% of annual revenue.
- **Customer:** Self-improvement-minded adults; life and wellness coaches, who use it with clients; and New Year goal-setters. They arrive through App Store and Play search. They already pay for Headspace/Calm-type subscriptions and journaling apps.
- **Problem / desire:** "I want to see which part of my life is out of balance and track whether I'm actually improving."
- **Offering:** An iOS and Android app: rate life areas, see the visual wheel, add action steps, track progress. Subscriptions are managed through RevenueCat.
- **Price & revenue model:**
  - **Current:** $1.99/mo and $14.99–29.99/yr subscriptions, plus a lifetime option.
  - **Planned:**
    - test $3.49/mo and $24.99/yr for new users;
    - sunset or raise the lifetime price (it cannibalises recurring revenue);
    - add a "Coach" tier for coaches who share wheels with clients.
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Purchase price (target; walk-away $8,000) | $6,500 |
| Escrow fee (~3.25%; verify) | $210 |
| Apple Developer Program, year 1 | $99 |
| Google Play developer registration | $25 |
| Domain transfer (`trywheeloflife.com`) | $12 |
| Operating reserve | $300 |
| **Total** | **$7,146** (walk-away case ≈ $8,700) |

### Monthly running costs (excluding operator tokens)
- **Store commission:** 15% (Small Business Program), ~$83 on TTM-average gross of $554.
- **RevenueCat:** $0 below its free-tier revenue threshold (verify the current limit).
- **Developer fees:** ~$8 amortised.
- **Backend/hosting:** ~$10 (verify).
- **Operator tokens:** $70 at P50.

**Monthly net by case**

| Case | Net/mo | Payback | Notes |
|---|---|---|---|
| Pre-growth baseline | ~$383 | — | TTM gross less the costs above, before decay. |
| P50 | ~$345 → **~$370** | **~19 months** | Applies 10% decay, then +15% by month 6 from pricing, paywall and localisation work. Year-1 profit after one-time sponsor hours (8 h × $300 = $2,400): ~$2,040. |
| P10 | ~$180 | — | Ratings slip after a bad update, and the price test backfires. 12 × $180 = $2,160, plus resale ~$3,000, recovers $5,160 of $7,146: **−28%**. |
| P90 | ~$600 | ~12 months | The price lift holds, the Coach tier lands, and the January spike is ≥$1,200. |

### Customer acquisition plan
- **Main channel: App Store and Play search.** The app already gets ~1,800 organic installs a month, so no new channel is needed.
- **Funnel:** organic search → install → onboarding wheel → paywall at "track progress over time".
- **AI operator's levers:**
  - ASO for keywords, screenshots and localisation;
  - RevenueCat paywall experiments (check plan requirements);
  - the onboarding-to-paywall flow;
  - review prompts timed after a "wheel improved" moment;
  - a December "New Year reset" in-app event, using App Store in-app events, which have their own placement.

### Initial traffic approaches (ranked by expected speed)
1. **Paywall and price tests** on existing installs. These show up within 2–4 weeks of close.
2. **App Store in-app event and promotional text for New Year 2027.** These are store-controlled placement and need a December submission, which suits the timing.
3. **ASO localisation** of the listing into the top 10 languages. Expect 1–3 months.
4. **Coach tier via the existing coach users.** In-app ask and referral only, with no cold outreach. Expect 3–6 months.

### Path to first sale
- **Days 0–14:** DD with read-only finance reports; the sponsor creates the Apple and Google developer accounts. Apple organisation enrolment may need a D-U-N-S number, which takes 1–2 weeks, so start on day 0.
- **Days 14–30:** LOI and APA.
- **Days 30–50:** escrow and the app transfers. Apple and Google transfers are each typically days, but can stall.

First revenue arrives **at close (~day 45–55)**. **First cash is Apple's payout, ~33–45 days after the close of the month**, so the first cash lands around 2027-01 if the deal closes in November.

### Who does what
- **AI operator:**
  - DD analysis, a build-and-compile check (where a cloud macOS CI runner allows it) and the transfer checklist;
  - after close: OS and SDK updates, store submissions prepared for sponsor approval where needed, support inbox, ASO, paywall tests, review responses, the New Year campaign and bookkeeping.
- **Human sponsor:**
  - one-time, ~8 h ($2,400): developer accounts with identity checks, D-U-N-S, escrow, APA, accepting the app transfers, tax forms (W-8/W-9, banking);
  - recurring, ~0.5–1 h/mo: accepting Apple agreement updates, payouts, 2FA prompts on Apple ID. Apple 2FA is a real recurring human dependency. This is within the gate of $370 ÷ $300 ≈ 1.2 h.

### Moat — why not just ask ChatGPT?
- **Partly vulnerable.** ChatGPT can walk a user through a wheel-of-life exercise for free.
- **What the app has that a chatbot doesn't:** persistent visual tracking over time, reminders, and a store-search position. It also has 500+ reviews that a new AI-built clone can't replicate quickly.
- **This is the weakest moat of the three.** It rests on placement and habit, not capability.

### Biggest risks (ideator's own view)
- **Gross vs net ambiguity and lifetime-purchase revenue** may mean true recurring net is 20–30% below the headline.
- **Apple and Google account dependencies** need recurring sponsor actions: 2FA, agreements, and identity re-verification.
- **The multiple:** ~19-month P50 payback fails the gate. The deal only passes at ≈$4,400 all-in, and the seller anchors at $11,111.

---

## Q3 — Standing "fire-sale" buy order: ≤ $3,000 for verified, aged, abandoned revenue

- **Persona:** The Acquirer
- **One-liner:** Don't pick an asset now. Instead, set a strict buy-box and have the AI operator screen TrustMRR, Microns and Flippa daily for founder-abandoned assets.
  - **Target:** browser extensions, plugins and small apps.
  - **Price:** ≤ $3,000.
  - **Revenue:** API-verified, ≥12 months of history, and trailing-6-month revenue of **≥$450/mo**.
  - The sponsor makes an offer only when an asset clears every gate. If none does, capital stays in T-bills at 4%.
- **Example listings (real; the good ones sold fast):**
  1. **AI YouTube Growth Platform** ([microns.io](https://www.microns.io/startup-listings/ai-youtube-growth-platform)): **sold for $3,000**.
     - Claimed $1,250/mo profit from 138 customers, with 8% monthly churn. Launched in 2025.
     - The seller was shifting focus to "4 new SaaS apps".
     - This is the archetype: a serial builder dumping a working asset at ~0.2× annual revenue.
  2. **Old Photo Restore iOS** ([microns.io](https://www.microns.io/startup-listings/old-photo-restore-ios-app)): **sold for ~$2,000** on $151 MRR and 4.8★. The founder was "leaving the app business".
  3. **AI Writing Assistant** ([microns.io](https://www.microns.io/startup-listings/ai-writing-assistant)): **sold**; asked $5,500 on $2,250/yr. The founder runs "35+ apps". This is what *doesn't* qualify: about 2.4× revenue, with LLM API costs.
  4. **Brevik** ([trustmrr.com/startup/brevik](https://trustmrr.com/startup/brevik)): **current**, asking $4,900.
     - It shows $490 in the last 30 days, but has 3 users, 88 visitors, $0 MRR, and was founded 2026-08-10.
     - This is the red-flag pattern the buy-box rejects: a one-month spike that may be self-purchases or one-off deals.
- **Price / multiple / payback:**
  - Buy-box: price ≤ $3,000, which is ≤ ~0.55× verified annual revenue.
  - P50 economics:
    - Monthly net **~$230**.
    - Payback **~13 months**. This **marginally FAILS** the ≤12-month gate. It passes at ≤$2,750 all-in or ≥$250/mo net.
    - Annualised return: ~93% steady state, ~44% in year 1 after sponsor hours.
  - Capital is under $3k, closer to the run's under-$1k preference than Q1 or Q2.
- **Due-diligence checklist:**
  - **Verified history.** Revenue verified through the payment-provider API (TrustMRR-verified, or read-only Stripe / Lemon Squeezy / RevenueCat), with **≥12 months** of history.
  - **Revenue spread.** No month above 20% of TTM. Revenue from at least 30 distinct customers.
  - **Hidden costs.** LLM or API cost per user, measured from real invoices. Prefer assets with **no LLM COGS** (extensions, utilities), because those are cheaper to clone *and* to run.
  - **Why it's cheap.** Is the seller abandoning it (good) or is it decaying (bad)? Check 6-month MRR slope, churn, rating trend and the last commit date.
  - **Clone audit (§19).** Count same-pitch listings created in the last 90 days. If there are more than 5 with traction, pass.
  - **Transfer.** Placement asset (store listing, plugin slug), billing, domain, repo and any API keys, each with a named transfer method.
  - **Seller handover.** At least 30 days of handover support, written into the APA.
- **Demand test:** The test is free, because capital moves only on a qualifying deal.
  - **Pipeline target (first 30 days):** the AI operator screens public listings daily and logs every candidate against the buy-box. Go if **≥3 candidates/month** pass a desk screen; otherwise abandon the thesis and keep the cash.
  - **Per-deal gates (all required):**
    - verified trailing-6-month revenue ≥ $450/mo;
    - ≥12 months of history;
    - MRR slope over 6 months no worse than −10%;
    - no LLM COGS above 15% of revenue;
    - price ≤ $3,000;
    - the seller agrees to a 14-day post-close revenue check held in escrow.
- **Customer:** Depends on the asset. The buy-box restricts it to products that sell through a marketplace with built-in discovery and billing (Chrome Web Store, AMO, App Store/Play, WordPress.org with Freemius), never ones that depend on the founder's personal brand.
- **Problem / desire:** On the supply side, solo builders with 10–35 apps who want cash and less admin. On the demand side, whatever the asset's existing paying users already want.
- **Offering:** The acquired product, unchanged at first.
- **Price & revenue model:** The asset's existing model, preferring subscriptions.
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Purchase price (cap) | $2,500–3,000 |
| Escrow fee (~3.25%, min ~$50; verify) | $80–100 |
| Platform developer accounts (if needed: CWS $5, Play $25, Apple $99) | $0–130 |
| Operating reserve | $250 |
| **Total** | **~$2,950** (cap $3,450) |

### Monthly running costs (excluding operator tokens)
- **Payment fees:** ~10%.
- **Hosting and API:** ~$40.
- **Operator tokens:** $50 at P50, for a small, light-touch asset.

**Monthly net by case**

| Case | Gross | Net/mo | Payback | Notes |
|---|---|---|---|---|
| P50 | $360 ($450 trailing, less 20% post-sale decay, which is typical for abandoned assets) | **~$230** | ~13 months | One-time sponsor hours (5 h × $300 = $1,500) leave ~$1,260 year-1 profit. |
| P10 | — | ~$50 within 6 months (−60% decay: clone flood or a platform change) | — | Resale ~$500. Recovered ~$1,100 of $2,950: **−63%**. **This fails the P10 ≤50% gate** unless the buy-box also requires ≥18 months of history and no LLM COGS, which shrinks the deal pool further. |
| P90 | — | ~$450 | ~7 months | The asset was simply abandoned, not decaying, and the operator's fixes lift conversion. |

### Customer acquisition plan
1. **Before purchase:**
   - The AI operator monitors public listing pages daily: TrustMRR `/acquire`, Microns, and Flippa's plugins/extensions and SaaS categories. Read-only, no accounts.
   - It scores each listing against the buy-box and drafts a one-page memo for each pass.
   - The sponsor sends the offer.
2. **After purchase:** run the same marketplace-native playbook as Q1 and Q2: listing optimisation, conversion, pricing, and bug fixes from support tickets.

### Initial traffic approaches (ranked by expected speed)
1. **Fix whatever the founder neglected.** Broken onboarding, unanswered reviews and stale listings typically convert within 2–4 weeks.
2. **Price and plan restructure:** move to annual by default and remove lifetime deals. Expect 1–2 months.
3. **Second-marketplace listing** (Edge Add-ons, AMO, or the other mobile store). Expect 1–3 months.

### Path to first sale
- **Days 0–30:** screening only. Expect ~35% odds of finding a qualifying deal within 90 days. These deals sell in days, so the sponsor must be able to act within 48 h, which is a hidden sponsor-availability cost.
- **Close:** ~2–3 weeks after the offer. First revenue arrives at close.

**P50 time to first revenue: ~60–90 days.** At P10 it is never, but capital is then not at risk.

### Who does what
- **AI operator:** daily listing screens, buy-box scoring, DD memos, data reconciliation, code audit, transfer checklist, and all post-close operations.
- **Human sponsor:**
  - per deal, ~5 h ($1,500): offer, NDA, APA, escrow, account KYC, accepting transfers;
  - per rejected candidate, ~0.25 h to read a memo;
  - recurring after close, ~0.5 h/mo. This is within the gate of $230 ÷ $300 ≈ 0.77 h.

### Moat — why not just ask ChatGPT?
- Only what the specific asset carries: a store position, reviews and a paying base.
- The **sourcing edge** is speed plus a strict, AI-run screen. But other buyers (and their agents) watch the same feeds. The $3,000 AI YouTube Growth Platform shows good deals clear quickly.
- This is a **capital-and-speed edge**, which §19 allows, not a product edge.

### Biggest risks (ideator's own view)
- **Adverse selection.** Assets priced at 0.2–0.5× revenue are often cheap because they are decaying, and the seller knows it. That is why the P10 fails.
- **Deal flow may not exist.** Today's live sub-$5k inventory is almost all zero-revenue AI clones; the good fire-sales had already sold. The thesis may simply never trigger.
- **Sponsor time per deal ($1,500) is ~50% of the purchase price.** At this size, fixed transaction costs dominate. Buying two $1,500 assets is worse than one $3,000 asset.

---

### Cross-idea note for the evaluators
- **This persona's ideas are limited by price (the multiple), not by distribution.** That is the opposite of rounds 1–2.
- **Q1 and Q2 have the strongest §19 moats seen so far** (aged store placement plus paying users) and pass P10. They fail the 12-month payback, coming in at 19–26 months, yet still return 10–15× the T-bill rate.
- **If the committee wants an acquisition, the decision is about the gate, not the idea.** Relax the gate for verified-revenue acquisitions, or accept Q3's thin, risky deal flow.
