# Autonomy Auditor review: round 3 (capital allowed)

Date: 2026-10-06. Inputs: `../PARAMS.md` (sponsor time = $300/h; gate: ongoing sponsor h/mo ≤ net monthly profit ÷ $300; setup h × $300 charged against year-1 profit), `operator-constraints.md`, `scoring-rubric.md`, `lessons-learned.md`, and the four idea files.

## Method

**Hours.** For each idea, every lifecycle step is marked **AI**, **H1** (human, one-time) or **HR** (human, recurring). The ideator's sponsor-hour claim is shown next to the auditor's realistic estimate. Realistic hours add the steps the ideators left out: seller and partner calls, lawyer review, 2FA and agreement re-acceptance, appeals, inbound phone calls, receiving physical goods, and annual tax and registration filings (annualised).

**Net used for the gate.** PARAMS defines net profit as "after all costs", including "depreciation or payback of capital". So the gate uses **P50 net after capital amortisation**:
- acquisitions are amortised over 36 months;
- Q3's fire-sale asset is amortised over 24 months;
- equipment uses the ideator's stated depreciation;
- one-time non-ad capital for the B ideas is spread over year 1.

The **operating-basis** result (before amortisation) is also given wherever the verdict changes.

**Effective $/h** = year-1 P50 net (all-cost basis) ÷ year-1 sponsor hours (setup + 12 × monthly, at auditor hours). Anything under $300/h means the sponsor would earn more billing their time elsewhere.

## Summary table

| ID | Idea | Autonomy score | Human setup hrs, one-time (ideator → auditor) | Human hrs/mo ongoing (ideator → auditor) | $ cost of sponsor hours (setup / yr-1 ongoing) | P50 net/mo, all-cost (operating) | Allowed h/mo | Effective $/h, yr-1 | PARAMS sponsor-time gate | Hard gates | Scales without humans? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | UltraWideo-class extension acquisition | 6 | 6 → **12** (16–18 if entity purchase) | 0.5 → **0.75** | $3,600 / $2,700 | **$80** ($290) | 0.27 (0.97) | **$46** ($166 operating) | **FAIL** all-cost; pass operating | Seller calls, APA/lawyer, escrow KYC + wire, Lemon Squeezy/Stripe KYC, CWS dev acct + DSA trader verification, CWS transfer form (seller-initiated), AMO, registrar/Railway/GitHub/Discord handovers | Yes. Marketplace + merchant of record; no per-sale human |
| Q2 | Wheel of Life-class mobile app acquisition | 5 | 8 → **13** | 0.5–1 → **1.0** | $3,900 / $3,600 | **$171** ($370) | 0.57 (1.23) | **$82** ($178 operating) | **FAIL** all-cost; pass operating (marginal) | D-U-N-S + **Apple verification phone call**, Play org verification, escrow, App Store agreements/tax/banking, both app transfers, RevenueCat/Firebase transfer | Mostly. Stores handle billing/refunds; Apple agreements, 2FA and review-rejection replies recur |
| Q3 | Standing fire-sale buy order (≤$3k) | 4 | 5/deal → **9/deal + ~3 h screening** | 0.5 → **0.6 post-close; 0.75–1.5 while searching** | $3,600 / ~$1,600 | **$107** ($230); **$0 while searching** | 0.36 (0.77); 0 while searching | **$55** ($119 operating) | **FAIL** (search phase always; post-close all-cost) | 48-h sponsor availability to bid, per-deal KYC on whatever platform the asset uses (Apple adds D-U-N-S + call), escrow, APA | Depends on asset; buy-box restricts to marketplace-billed assets |
| B1 | HSK 3.0 Speaking Mock + paid search | **8** | 2.5 → **4** | ~0 → **0.35** | $1,200 / $1,260 | **$170** ($250) | 0.57 (0.83) | **$157** ($274 operating) | **PASS** | Lemon Squeezy KYC, Google Ads advertiser verification + API developer-token application, Reddit Ads account, Upwork client verification and contractor hire | Yes. Lemon Squeezy (MoR) + API-managed ads; no per-sale human |
| B2 | SubWatch (OSHA history for GCs' subs) | 6 | 2 → **5** | 0.25 → **0.75** (rising with accounts) | $1,500 / $2,700 | **~$65 yr-1 avg**; ~$0 months 1–6; $540 at month 12 | 0.22 yr-1; 1.8 at month 12 | **$56** | **FAIL year 1**; passes from ~month 10–11 | Second Google Ads account + verification, likely policy appeal (2026-10-05 gov-docs policy), Bing, LinkedIn (personal profile), lawyer review of defamation/FCRA wording | Partly. B2B vendor paperwork (W-9, COI, security questionnaires, POs) and subs' dispute letters grow with accounts |
| B3 | Recipe-Card Heirloom Cookbook (Q4 gift) | 6 | 4 → **6** | 0.25 → **0.6 avg (1.5 in Nov–Jan)** | $1,800 / $2,160 | **$281** ($310) | 0.94 (1.03) | **$254** | **PASS** (thin) | Stripe KYC (plus a likely presale risk review), Meta Business verification (needs the sponsor's personal FB profile), Google Ads, Lulu card, **home-state sales-tax permit**, sample-book QA, photographer hire | Mostly. Lulu drop-ships; chargebacks and emotional heirloom escalations grow with orders |
| P1 | Merchant-loaded ATMs (1→3) | 4 | 3.5 → **9** | 0.3 → **0.75** (+ incident tail) | $2,700 / $2,700 | **$465 at 3 ATMs**; **$105 at the 1-ATM pilot** | 1.55 (pilot 0.35) | **$248** | **PASS at full build; FAIL during pilot** | **ATM ISO/processor KYC + background check + personal guarantee**, settlement bank account, **state ATM registration** (e.g. Texas per-machine), GL insurance, merchant signatures (merchants want a call or a visit), key loading/terminal programming, liftgate delivery acceptance, contractor bolt-down | No. Each new ATM needs a placement, a signature, freight, an install and a processor terminal; break-ins need the owner |
| P2 | Countertop power-bank stations (2→8) | 3 | 2.5–3 → **7** (+2–3 at scale-up) | 0.2 → **0.75–1** self-shipped / **0.4** with a hazmat 3PL | $2,100 / $3,150 | **$250 at 8 stations** ($175 with a 3PL); **$25 at the pilot** | 0.83 (0.58 with 3PL); pilot 0.08 | **$114** | **FAIL as written** (pilot fails; full fleet borderline) | Stripe + OEM platform KYC, **importer/CPSC eFiling (from 2026-07-08) under DDP**, product-liability insurance, rental sales-tax permit, **A2P 10DLC SMS registration**, **someone must receive, test, repack and ship lithium stations** | No. Spares, relocations and non-return disputes go to a human queue |
| P3 | PlacementDesk (location sourcing for route operators) | 2 | 3.25 → **6** | 0.5 → **2.5** (lesson 14: 4–6) | $1,800 / $9,000 | **~$260 yr-1 avg** ($345 at month 4, $500 at month 9) | 0.87 (1.67 at month 9) | **$89** | **FAIL** | Operator calls (phone-first industry), lawyer check on real-estate brokerage and the FTC Business Opportunity Rule, collections; **small-claims court in person** for non-payment | No. Each operator relationship and each disputed install needs the sponsor |
| U5 | AI-managed vending, outsourced restocking (1–3 machines) | 2 | n/a → **15** | n/a → **2.0** | $4,500 / $7,200 | **~$100** (auditor estimate) | 0.33 | **$31** | **FAIL** (decisively) | Host site walk-throughs, used-machine inspection/pickup, vending licence/decals and sales-tax permit, card-reader merchant KYC, hiring restocker/installer by phone, wholesale-club membership | No. Restocking labour is linear per machine; restocker supervision and shrink disputes recur |

**Gate results:**
- **Pass:** B1 and B3. Both run on merchant-of-record or Stripe billing with API-managed ads and no per-sale human.
- **Conditional pass:** P1, at full build only.
- **Fail on the all-cost reading of PARAMS:** Q1, Q2, Q3, B2 (year 1), P2 (as written), P3 and U5.
- **Q1 and Q2 pass on the operating basis.** The committee must decide which reading of "net" binds.

---

## Q1: UltraWideo-class aged extension acquisition

| Stage | Step | Who | Hours |
|---|---|---|---|
| 1 Setup | TrustMRR contact + NDA (sponsor's account) | H1 | 0.5 |
| | Seller calls: DD walkthrough, then handover (sellers at $7–13k expect calls) | H1 | 3 |
| | LOI; lawyer engagement + APA review | H1 | 2.5 |
| | Escrow.com KYC + wire (~$7k; bank may call to confirm) | H1 | 1 |
| | Lemon Squeezy store KYC, or Stripe KYC plus the migration decision | H1 | 1 |
| | CWS developer account ($5, 2-step, EU DSA trader declaration with address/phone); accept transfer (seller submits Google's transfer form) | H1 | 1 |
| | AMO account, accept author invite | H1 | 0.5 |
| | Registrar (`uw.wtf`), Cloudflare, Railway, GitHub, Discord ownership (each needs a human account with 2FA) | H1 | 1.5 |
| | Bookkeeping/tax setup | H1 | 0.5 |
| | *If entity purchase (option a): registered agent, IRS 8822-B responsible-party change, LLC bank account* | H1 | +4–6 |
| 2 Build | Code audit, MV3 fixes, Edge port | AI | 0 |
| 3 Listing | Listing rewrites, localisation; Edge Add-ons developer account | AI / H1 | 0.25 |
| 4 Marketing | In-product prompts, store SEO | AI | 0 |
| 5 Each sale | Lemon Squeezy checkout, licence API | AI | 0 |
| 6 Support | Email support; Discord only as a disclosed bot | AI | 0 |
| | Chargeback or refund escalations | HR | 0.1/mo |
| 7 Maintenance | Site/DOM breakage fixes | AI | 0 |
| | CWS policy-violation emails, appeals, re-auth on 2FA | HR | 0.25/mo |
| 8 Finance | Lemon Squeezy is the MoR (sales tax/VAT handled) | AI | 0 |
| | Payouts, plus annual income-tax filing (~3 h/yr) | HR | 0.4/mo |

**Totals:** 12 h one-time ($3,600); 0.75 h/mo ($225/mo).

**Gate:**
- P50 operating net is $290. After amortising the $7,565 outlay over 36 months ($210/mo), net is **$80**, which allows **0.27 h/mo**.
- **Result: FAIL all-cost; PASS operating** (0.97 allowed).
- Year-1 profit after the setup charge is about −$120 operating.

**Hard gates:**
- The seller must initiate the CWS transfer.
- Lemon Squeezy subscriptions can't move between stores. Search found no evidence of a store-ownership transfer, so it needs an entity purchase (more sponsor hours, plus liability) or a Stripe migration (15–30% churn).

**Platform policy:** Discord support is fine only as a bot account; a self-bot on the sponsor's user account is banned.

**Scaling cliff:** none. Sales are marketplace- and MoR-handled.

---

## Q2: Wheel of Life-class mobile app acquisition

| Stage | Step | Who | Hours |
|---|---|---|---|
| 1 Setup | D-U-N-S request; Apple org enrolment. **Apple phones the enrollee to verify**, and the business must show its address and hours on its own website | H1 | 2 |
| | Google Play org account (D-U-N-S, ID, phone verification) | H1 | 1 |
| | Seller calls (DD + handover) | H1 | 2 |
| | LOI/APA + lawyer | H1 | 2 |
| | Escrow KYC + wire | H1 | 1 |
| | App Store Connect Paid Apps agreement, tax forms, banking; Play payments profile | H1 | 1 |
| | Accept both app transfers; RevenueCat, Firebase/backend, domain | H1 | 1.5 |
| | Privacy/GDPR review (journaling data); App Store Connect API key for the AI | H1 | 0.75 |
| | Tax setup | H1 | 0.5 |
| 2 Build | SDK updates; builds via cloud macOS CI with an API key | AI | 0 |
| 3 Listing | Submissions through the API | AI | 0 |
| | Review rejections: Resolution Center replies are web-UI with 2FA (verify API coverage) | HR | 0.25/mo |
| 4 Marketing | ASO, in-app events, paywall tests | AI | 0 |
| 5 Each sale | Store billing via RevenueCat | AI | 0 |
| 6 Support | Email support; refunds handled by Apple and Google | AI | 0 |
| 7 Maintenance | Apple agreement re-acceptance (Account Holder only); Play policy declarations (Data safety, yearly target-API deadline) in the Console UI | HR | 0.4/mo |
| 8 Finance | Stores remit most sales tax/VAT. Payouts, plus annual tax | HR | 0.35/mo |

**Totals:** 13 h ($3,900); 1.0 h/mo ($300/mo).

**Gate:**
- P50 operating net is $370. Amortising $7,146 over 36 months ($199/mo) leaves **$171**, which allows **0.57 h**.
- **Result: FAIL all-cost; marginal PASS operating** (1.23 allowed).

**Hard gates:**
- D-U-N-S plus the Apple verification call takes 1–3+ weeks. Forum reports show enrolments stuck for more than 3 weeks.
- Both stores must confirm the transfer is eligible.

**Platform policy:** none beyond the store terms.

**Scaling cliff:** none per sale. The recurring load is fixed overhead (Apple 2FA and agreements). That overhead is the reason the comparable seller exited.

---

## Q3: Standing fire-sale buy order

| Stage | Step | Who | Hours |
|---|---|---|---|
| Pre-deal | Daily screens of public listings, buy-box memos | AI | 0 |
| | Sponsor reads ~3–6 memos/mo at 0.25 h each, and must stay on call to bid within 48 h | HR | 0.75–1.5/mo (no revenue yet) |
| 1 Setup (per deal) | Seller call, offer and negotiation | H1 | 2 |
| | APA (template plus light lawyer review), escrow KYC + wire | H1 | 2.5 |
| | Platform accounts for the asset type (CWS $5; Play; **Apple + D-U-N-S + phone call** if iOS) | H1 | 1–3 |
| | Billing-account KYC; accept transfers; handover | H1 | 2.5 |
| 2–6 Ops | Same playbook as Q1/Q2 | AI | 0 |
| 7–8 | Escalations, payouts, tax | HR | 0.6/mo |

**Totals:** ~9 h per deal plus ~3 h of screening ($3,600, which is about **120% of a $3k purchase price**); 0.6 h/mo post-close.

**Gate:**
- **While searching:** net is $0 and hours are above 0, so it **fails by construction**.
- **After close:** $230 operating less $123/mo amortisation (24 months) leaves **$107**, which allows **0.36 h**. Realistic hours are 0.6, so **FAIL** (operating basis passes at 0.77 allowed).

**Hard gate:** the 48-hour sponsor availability requirement is a recurring human dependency. Good deals clear in days.

**Scaling cliff:** each additional deal repeats about 9 h of fixed sponsor work.

---

## B1: HSK 3.0 Speaking Mock with paid search

| Stage | Step | Who | Hours |
|---|---|---|---|
| 1 Setup | Lemon Squeezy KYC | H1 | 0.5 |
| | Google Ads account + advertiser verification (ID; can need resubmission) | H1 | 1 |
| | Google Ads API developer-token application (manager account, basic-access form) | H1 | 0.5 |
| | Reddit Ads account + card | H1 | 0.5 |
| | Upwork client account (ID verification, payment method); hire and approve the native-speaker contractor | H1 | 1 |
| 2 Build | Demo, levels, scoring pipeline | AI | 0 |
| 3 Listing | Pre-order page; domain (AI, using the sponsor's card on file) | AI | 0 |
| 4 Marketing | Ads via API, email sequence, one-to-one affiliate pitches | AI | 0 |
| | Optional genuine Reddit post | H1 | 0.5 |
| 5 Each sale | Lemon Squeezy checkout; automated delivery | AI | 0 |
| 6 Support | Inbox; refunds via the Lemon Squeezy API; MoR handles chargebacks | AI | 0 |
| 7 Maintenance | Spec checks | AI | 0 |
| | Contractor approval and payment for each new level (~2/yr); Google Ads re-verification or suspension appeals | HR | 0.2/mo |
| 8 Finance | Lemon Squeezy is the MoR; payouts plus annual income tax | HR | 0.15/mo |

**Totals:** 4 h ($1,200); 0.35 h/mo ($105/mo).

**Gate:**
- Year-1 average P50 is $250. Spreading the $962 of capital over year 1 leaves **$170**, which allows **0.57 h**. **PASS.** In year 2 it allows 0.83 h.

**Flags:**
- **italki:** its terms bar teachers from off-platform engagement, so hire through Upwork or Preply-style marketplaces instead.
- **Upwork:** an AI operating the sponsor's account is a ToS grey area. The sponsor should send the hire and approval clicks.
- **The Reddit post** must be written and posted by the sponsor as genuine participation, with the affiliation disclosed. An AI-written post put up under the sponsor's name breaks the spirit of lessons-learned §5.
- **Lemon Squeezy pre-orders** need a clear delivery date. Refunds are automatic on a kill.

**Scales without humans:** yes.

---

## B2: SubWatch

| Stage | Step | Who | Hours |
|---|---|---|---|
| 1 Setup | Lemon Squeezy KYC (may be shared with D2) | H1 | 0.5 |
| | A **separate** Google Ads account + advertiser verification | H1 | 1 |
| | A likely policy appeal under the 2026-10-05 government-documents policy | H1 | 0.75 |
| | Microsoft Ads account; LinkedIn Campaign Manager (needs the sponsor's personal profile + company page) | H1 | 1 |
| | DOL API key; developer token if not shared | H1 | 0.25 |
| | Lawyer review of the ToS and disclaimers (defamation, FCRA-adjacent wording) | H1 | 1 |
| 2 Build | Ingest, fuzzy matching, alerts | AI | 0 |
| 4 Marketing | Ads via API; nurture emails | AI | 0 |
| 5 Each sale | Lemon Squeezy subscription | AI | 0 |
| 6 Support | Email support | AI | 0 |
| | **B2B buyers' vendor onboarding**: W-9, certificate of insurance requests, security questionnaires, POs. Prospects who insist on a call are lost or cost sponsor time | HR | 0.3–0.6/mo, grows with accounts |
| | **Subs disputing their record** (demand letters) | HR | 0.2/mo |
| 7 Maintenance | DOL API breakage watch | AI | 0 |
| 8 Finance | MoR; payouts and tax | HR | 0.15/mo |

**Totals:** 5 h ($1,500); 0.75 h/mo ($225/mo).

**Gate:**
- The year-1 P50 total is about $780, or $65/mo. Months 1–6 net about $0, so year 1 allows only **0.22 h/mo**: **FAIL**.
- Month-12 run-rate of $540 allows 1.8 h, so the gate passes from about month 10–11.
- Year-1 profit after the setup charge and ongoing hours is about −$3,400.

**Flag:** "Separate Google Ads account" doesn't isolate risk if the same person verifies both accounts or the same payment profile pays for them. Google links related accounts for suspensions.

**Scaling cliff:** moderate. Paperwork and legal-letter load grows with the customer count.

---

## B3: Recipe-Card Heirloom Cookbook

| Stage | Step | Who | Hours |
|---|---|---|---|
| 1 Setup | Stripe KYC; Stripe may also review the presale (certificate now, goods in January) or impose a reserve | H1 | 1 |
| | Meta Business Manager (needs the sponsor's real Facebook profile) + Business verification | H1 | 1 |
| | Google Ads verification (shared with B1 = concentration); Pinterest Ads | H1 | 1 |
| | Lulu account with the sponsor's card | H1 | 0.25 |
| | **Home-state sales-tax permit** | H1 | 0.75 |
| | Gift-certificate terms review (CARD Act 5-year rule, state unclaimed property) | H1 | 0.5 |
| 2 Build | Upload, transcription, layout, proofs | AI | 0 |
| 3 Launch | Hire the photographer (Fiverr/Upwork, sponsor account) | H1 | 0.5 |
| | **Receive and judge 3 sample books.** A physical quality call on the product itself | H1 | 1 |
| 4 Marketing | Ads via the Meta and Google APIs | AI | 0 |
| | **New-advertiser restrictions or disabled ad accounts during the Q4 ramp**: appeals require the sponsor's ID | HR | ~0.5/mo in Nov–Dec |
| 5 Each sale | Customer approves the proof; Lulu prints and drop-ships | AI | 0 |
| 6 Support | Misprint claims via Lulu | AI | 0 |
| | Chargeback approvals; family disputes over a wrong recipe in a memorial book | HR | 0.3–0.5/mo in peak |
| 7 Maintenance | Light | AI | 0 |
| 8 Finance | **Not MoR.** Sponsor signs and files sales-tax returns and the annual unclaimed-property report | HR | 0.25/mo |

**Totals:** 6 h ($1,800); 1.5 h/mo in Nov–Jan and 0.3 h/mo otherwise, averaging **0.6 h/mo**.

**Gate:**
- Year-1 average P50 is $310, less about $29/mo of non-ad capital, leaving **$281**, which allows **0.94 h**. **PASS.**
- Peak-month net (about $600+) also covers peak hours.

**Flags:**
- The FTC Mail Order Rule requires delay notices; the AI can send them.
- Meta "AI info" labels apply. The ideator correctly uses real photos.

**Scaling cliff:** mild. There is no per-order human, but disputes and chargebacks rise with volume.

---

## P1: Merchant-loaded ATMs

| Stage | Step | Who | Hours |
|---|---|---|---|
| 1 Setup | **ISO/processor application**: ID, background check, usually a personal guarantee | H1 | 2 |
| | Business entity and settlement bank account (some banks need a branch visit) | H1 | 1 |
| | GL and equipment insurance | H1 | 0.75 |
| | **State ATM registration** (Texas requires registration and a sticker on each machine; check the target state) | H1 | 0.5 |
| | Hire and brief the field rep; take merchants' pre-signing calls (cash-heavy owner-operators rarely e-sign from a postcard) | H1 | 2.5 |
| | Approve purchases; coordinate the vendor's terminal programming and key loading with the ISO | H1 | 0.8 |
| | Thumbtack/TaskRabbit install booking (sponsor-owned account); collect merchants' W-9s | H1 | 0.75 |
| 3 Launch | **Liftgate delivery** (merchant signs); **bolt-down** (contractor); merchant's own processor paperwork for principal settlement | Contractor / merchant | — |
| 4 Marketing | Lob postcards and email | AI | 0 |
| 5 Each sale | Merchant loads cash and paper; the AI monitors | Merchant / AI | 0 |
| 6 Support | "Cash not dispensed" disputes need an electronic-journal pull (remote if supported, otherwise a tech); skimmer checks | AI / contractor | — |
| | **Merchants phone when the ATM is down** (the AI can't take calls); ISO compliance calls | HR | 0.4/mo |
| 7 Maintenance | Contractor repairs; relocations | Contractor | — |
| | Approvals over $200; **break-in → police report and insurance claim by the owner** (3–5 h per incident, amortised) | HR | 0.2/mo |
| 8 Finance | Processor settlement; reconciliation | AI | 0 |
| | 1099s for merchants; annual registration renewal; tax | HR | 0.15/mo |

**Totals:** 9 h ($2,700); 0.75 h/mo ($225/mo).

**Gate:**
- **Full build (3 ATMs):** net after depreciation is $465, which allows **1.55 h**: **PASS**.
- **Pilot (1 ATM, months 2–4):** $212 − $75 tokens − $32 depreciation = $105, which allows **0.35 h** while pilot hours run at about 1 h/mo: **FAIL**.

**Hidden cash and KYC exposure:**
- The vault combination sits with the merchant. Disputes over cash shortages are a sponsor matter.
- The ISO's KYC/AML due diligence names the sponsor personally.

**Scaling cliff:** yes. Every ATM repeats a signature, freight, install, terminal setup and registration.

---

## P2: Countertop power-bank stations

| Stage | Step | Who | Hours |
|---|---|---|---|
| 1 Setup | Stripe KYC; OEM rental-platform account and contract (Chinese OEMs often require a WeChat or video call) | H1 | 1.5 |
| | **Import compliance**: CPSC eFiling of certificates has been required since 2026-07-08; under DDP, confirm who is importer of record and holds the certificate; FCC/UL documents | H1 | 0.5 |
| | Product-liability insurance for lithium (underwriter questions) | H1 | 0.75 |
| | Rental sales-tax permit | H1 | 0.5 |
| | **A2P 10DLC registration** for SMS support | H1 | 0.25 |
| 3 Launch | **Receive the DG freight and the sample; physically test rent/return/non-return; repack; label (lithium Section II); ship one station to each venue.** The idea says "the AI forwards", but no one is assigned this physical work | H1 (sponsor) or a hazmat-capable 3PL | 3.5 (+2–3 at scale-up) |
| | Venue staff plug in | Venue | — |
| 4 Marketing | Lob + email | AI | 0 |
| 5 Each sale | OEM app + Stripe | AI | 0 |
| 6 Support | Renter email/SMS | AI | 0 |
| | **Refunds outside the auto rules and disputed $40 non-return fees go to a "sponsor-approved queue"**; this grows with rentals | HR | 0.25/mo |
| 7 Maintenance | **Mailing spare packs and relocation labels.** Whoever holds the spares does physical work | HR (self) or 3PL | 0.4/mo |
| | Signing new venue agreements | HR | 0.1/mo |
| 8 Finance | Sponsor files the rental sales-tax return | HR | 0.1/mo |

**Totals:** 7 h ($2,100), plus 2–3 h at scale-up; **0.75–1 h/mo self-shipped**, or about 0.4 h/mo with a 3PL.

**Gate:**
- **Pilot (2 stations):** net about $25, which allows 0.08 h: **FAIL**.
- **Full fleet (8 stations):** $250 allows 0.83 h. Self-shipped hours (0.75–1) make this borderline. A 3PL fee (about $75/mo) lowers net to $175, which allows 0.58 h against about 0.4 h used: a thin pass.

**Verdict as written: FAIL.** It could become a conditional pass with a hazmat 3PL and 10+ stations.

**Scaling cliff:** yes. Each station is a physical shipment and a venue relationship.

---

## P3: PlacementDesk

| Stage | Step | Who | Hours |
|---|---|---|---|
| 1 Setup | Operator calls. At a 5–10% yes-rate, 3–5 interested operators each want a call and a follow-up; the industry is phone-first | H1 | 3.5 |
| | Lawyer check: real-estate brokerage licensing and the FTC Business Opportunity Rule | H1 | 1 |
| | E-sign agreements; bank and Workspace | H1 | 1.5 |
| 4 Marketing | Lob and email to hosts and operators | AI | 0 |
| | **Hosts asking for a call before committing.** The operator is meant to take it; when the operator is slow, the deal stalls or the sponsor steps in | HR | 0.5/mo |
| 5 Each sale | Lead brief, registration, install confirmation | AI | 0 |
| 6 Support | **Collections and circumvention disputes** ("we already knew them"). Calls, and ultimately **small-claims court in person** | HR | 0.75/mo |
| 7 Maintenance | **Partner management**: re-engaging operators who sit on leads, and recruiting replacements (lessons-learned §14 puts this at 1–1.5 h/week) | HR | 1.25/mo |
| 8 Finance | ACH invoicing and reconciliation; tax | AI / HR | 0.1/mo |

**Totals:** 6 h ($1,800); **about 2.5 h/mo** ($750/mo). That is already below §14's 4–6 h/mo, because the AI does the written outreach.

**Gate:**
- The year-1 average net of about $260 allows 0.87 h; month 9 ($500) allows 1.67 h. **FAIL** at every point on the ramp.

**Hard gate:** two-sided cold start. Nothing earns until an independent operator installs a machine.

**Scaling cliff:** yes. Revenue scales with operator relationships, which are human.

---

## U5: AI-managed vending with outsourced restocking

| Stage | Step | Who | Hours |
|---|---|---|---|
| 1 Setup | Business registration and EIN; sales-tax permit; **local vending licence and per-machine decals** (plus a health permit if perishables) | H1 | 2.5 |
| | Insurance | H1 | 0.75 |
| | **Host walk-throughs** (doorway, power, floor; office and warehouse hosts expect a person), 3 sites | H1 | 4.5 |
| | **Used-machine inspection and pickup** (marketplace sellers are local and want cash) or dealer purchase | H1 | 2 |
| | Card-reader (Nayax/Cantaloupe) merchant KYC and contract | H1 | 1 |
| | **Hiring the restocker and installer**: phone screens, references, a company card or reimbursement setup | H1 | 2 |
| | Wholesale-club membership (person-bound) or Vistar account; sign the location contracts | H1 | 2 |
| 3 Launch | Delivery and installation (appliance dolly, sometimes stairs) | Contractor | — |
| 5 Each sale | Card reader and telemetry; stock purchasing | AI | 0 |
| | **Weekly restock visits**: about $35–45 each, about $150–195/mo per machine | Contractor | — |
| 6 Support | QR refunds | AI | 0 |
| | Host complaints, theft and vandalism, **restocker shrink disputes, restocker turnover** | HR | 1.25/mo |
| 7 Maintenance | Bill-validator and coin jams (go card-only to avoid cash collection and deposits); repairs | Contractor / HR | 0.4/mo |
| 8 Finance | Sales-tax returns; licence renewals | HR | 0.35/mo |

**Totals:** about 15 h ($4,500); about 2 h/mo ($600/mo).

**Economics (auditor estimate):**
- At $800/mo gross per machine, a machine nets about $100 after COGS, commission, card fees, telemetry and paid weekly restocking.
- Three machines, less tokens and 5-year depreciation, net about **$100/mo**. That allows **0.33 h**.
- **FAIL decisively.** The physical-operator ideator independently found the revenue-share variant pays back in 18–25 months.

**Scaling cliff:** severe. Restock labour is linear per machine and has no density benefit at 1–3 machines.

---

## Cross-idea observations

1. **The ideators under-counted sponsor setup hours by about 2×** (ideator 37 h in total across the 9 ideas that gave a figure; auditor 74 h on the same ideas). The commonest omissions were:
   - phone calls the AI can't make (sellers, operators, merchants, Apple verification);
   - lawyer reviews;
   - physically receiving goods (P2 samples and stations, B3 samples).
2. **Capital amortisation decides the acquisition verdicts.** On the operating basis Q1 and Q2 pass; on PARAMS' "all costs" basis they fail. The committee should state which basis binds.
3. **Platform concentration of the sponsor's identity:**
   - B1, B2 and B3 all need Google Ads advertiser verification by the same person. A suspension can spill across accounts linked by verifier or payment profile.
   - B3 adds Meta. The P ideas add a personal guarantee to an ATM ISO.
4. **Only B1 and B3 keep sponsor hours flat as sales grow.** Every physical idea (P1, P2, P3, U5) has a per-unit human or contractor touch, and B2's B2B paperwork grows with accounts.

## Sources
- [Chrome Web Store: register your developer account (transfer form, email cannot change)](https://developer.chrome.com/docs/webstore/register)
- [Extension ownership transfers via marketplaces (MakeTechEasier)](https://maketecheasier.com/stay-safe-chrome-extensions-ownership-transfer-threat/)
- [Lemon Squeezy / Stripe acquisition context (fungies.io, 2026)](https://fungies.io/lemon-squeezy-stripe-acquisition-saas-founders-2026/)
- [ATM ISO processing agreement: serial number, banking, personal ID for background checks (LegalClarity)](https://legalclarity.org/how-to-own-an-atm-legal-requirements-and-setup-steps/)
- [Due diligence for private ATM owners (Wipfli)](https://wipfli.com/insights/articles/fi-fs-due-diligence-for-private-atm-owners-or-operators)
- [Texas ATM registration and sticker requirement (HB 2629 analysis)](https://capitol.texas.gov/tlodocs/87R/analysis/html/HB02629H.htm)
- [Illinois repeal of non-bank ATM registration (IDFPR)](https://idfpr.com/banks/cbt/pawnbrok.html)
- [CPSC eFiling required from 2026-07-08 (UPS)](https://www.ups.com/ca/en/shipping/international-shipping/tariffs/cpsc)
- [Apple org enrolment verification call (Fasten Health docs)](https://docs.fastenhealth.com/technical/marketplace/apple-store.html)
- [Apple enrolment pending more than 3 weeks with D-U-N-S verified (Apple Developer Forums)](https://developer.apple.com/forums/thread/815009)
