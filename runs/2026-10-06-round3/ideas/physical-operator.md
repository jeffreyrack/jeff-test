# Physical ideas — The Operator

_Persona: ideator-physical-operator. Date: 2026-10-06. Inputs: `../PARAMS.md` (binding: $10k cap, preference under $1k, sponsor time at $300/h, physical labour outsourced), `operator-constraints.md`, `idea-brief.md` and `lessons-learned.md`. U5 (owning snack or drink vending machines) is the user's idea and is **not** repeated here. Web research was done on 2026-10-06. Sources are listed at the end. Any figure marked "(assumed)" still needs checking._

## Summary for the panel

| ID | Idea | Capital (pilot → full) | P50 net per unit/mo | Units for $300/mo net (after tokens) | P50 payback (full build) | Recurring physical labour |
|---|---|---|---|---|---|---|
| **P1** | ATMs placed in cash-heavy small businesses, with the merchant loading the cash | ~$2.6k → ~$6.4k | ~$210 per ATM (only if the location passes the ≥150 withdrawals/mo gate) | 2 (3 recommended) | ~11 months at run-rate (~14 from today) | Merchant loads cash and paper; contractor tech 1–2 visits/yr |
| **P2** | Countertop power-bank rental stations in bars, breweries and bowling alleys | **~$870** → ~$2.7k | ~$50 per station | 8 | ~8 months | **None.** Venue staff plug it in; spares and relocations go by mail |
| **P3** | Location-sourcing agent for established route operators, paid per install plus a residual (owns no machines) | **~$300–600** | ~$250 per installed placement + ~$20/mo residual | ~1.6 installs per month | ~2 months after steady state (~5 from today) | **None.** Operators do visits, installs and restocking |

**How these differ from U5:**
- In P1 and P2 the host or the venue staff do the only recurring physical work, so there is **no restocking route** at all.
- P3 owns no equipment. It is the materially different "partner with an existing route operator" structure: the operator owns the labour and the machines, and we are paid for locations.
- P3 could also feed U5, P1 and P2 with locations. The committee should treat that as correlation, not diversification.

### Ideas considered and rejected (so the panel doesn't re-propose them)
| Idea | Why rejected under this run's rules |
|---|---|
| **Revenue-share capital partner** (sponsor buys a used combo machine; an existing route operator places, restocks and splits) | Once COGS (~45%), card fees, location commission and the operator's labour share (~15–20% of gross) are paid, the sponsor's share is ~15–20% of gross. That is roughly $100–140/mo on a ~$2.5k machine, so payback is **18–25 months** and fails the 12-month rule. It is also a passive investment, which leaves little for the AI to do. |
| **Pay tire-air machines** at independent gas stations | A new card-reader machine costs **$5,286** (J.E. Adams 8799PV). Car-wash forum operators report from about $2/day up to $500/mo at a strong gas station. After a 25–30% station commission and a quarterly tech visit, P50 is ~$80–120/mo per machine, so payback is >24 months new and ~15–20 months used. AIR-serv installs free and shares revenue, so it wins most stations. Free-air laws apply in CA and CT. |
| **Vending massage chairs** | A new commercial chair is **$3,499** (Infinity IT-6900). A broker listing claims $150–980/mo per chair. After a 25–35% host commission, a card-reader fee and cleaning visits, P50 payback is ~20+ months. |
| **Voozaa power-bank partner programme** | Minimum **$7,500 for 3 kiosks** (~$2.5k each), with the owner keeping 80%. At US P50 utilisation, payback is ~25 months. P2 uses ~$300 OEM stations instead. |
| **Buying a managed ATM portfolio** | Listings of 240–286-placement routes sold at ~**3.5× cash flow**, about $1.8k per placement. That implies only ~$40–45/mo of owner cash flow per placement, so payback is ~40 months. It is also a useful sanity check on P1's P50 (see P1's risks). |
| **Turo car with a co-host doing handoffs** | ~$9k of capital. After Turo's cut, a 25% co-host fee, maintenance and depreciation, payback is ~30 months. |

---

## P1 — Merchant-loaded ATMs in cash-tip and cash-only small businesses

- **Persona:** The Operator
- **One-liner:** Own 1–3 refurbished EMV ATMs placed in cash-heavy small businesses (nail salons, barbershops, tattoo studios, cash-only taquerias, dive bars, laundromats, flea-market stalls). The **merchant loads its own cash** from the till and keeps ~40% of the surcharge, so no armoured car or route driver is ever needed. The AI operator finds locations, monitors every transaction, and dispatches a contractor tech when needed.
- **Unit economics (P10/P50/P90 per ATM per month):** **−$13 / +$212 / +$617** net, before AI tokens and depreciation.
  - The P50 holds **only for locations that pass the purchase gate** below.
  - An ungated location at ~100 withdrawals/mo nets ~$110, so payback is ~17 months and **fails** the 12-month rule.
  - Full working is below.
- **Outsourced labour plan & cost:**
  - **Delivery:** freight with liftgate straight to the merchant, ~$200, arranged by the seller.
  - **Installation:** bolt-down by a local ATM tech or a handyman found through Thumbtack or TaskRabbit, $150–250.
  - **Cash and receipt paper:** loaded by the merchant under the placement agreement. Paper is mailed from Amazon about every 2 months, ~$5/mo.
  - **Repairs:** an on-call ATM tech at $100–175 per visit. Expect 1–2 visits per year, about $30/mo in reserve with parts.
  - **Relocation:** if needed, a contractor charges $250–400.
  - **Optional field rep:** a local commission rep at $100 per *signed* placement, for merchants who will only commit in person.
- **Sponsor touchpoints (hours × $300):**
  - **One-time setup:**
    - processor/ISO application, KYC and settlement bank account: 1.5 h;
    - general-liability insurance: 0.5 h;
    - state ATM registration check or filing: 0.5 h;
    - e-signing 3 placement agreements: 0.75 h;
    - approving 3 ATM purchases: 0.3 h.
  - **Setup total:** ≈ **3.5 h = $1,050**, charged against first-year profit.
  - **Ongoing:** about 0.3 h/mo (≈ **$90/mo**) for monthly approvals and rare escalations such as a police report after a break-in or a merchant dispute.
  - **Gate check:** P50 net of ~$560/mo allows 1.8 h/mo. **Pass.**
- **Demand test:** Buy no ATM until the location is proven.
  1. **Outreach.** Over 3 weeks the AI contacts 300 cash-heavy businesses in one metro: Lob postcards plus email where a public address exists.
  2. **Pass to buy the first unit:**
     - ≥ 3 merchants sign a merchant-load placement agreement; **and**
     - at least one shows evidence of **≥ 150 withdrawals/month**, either the statement from an ATM that was removed in the last 12 months, or a cash-only shop with ≥ 80 customers/day (verified by the AI from Google "popular times" and a photo of the till count the merchant sends).
  3. **Kill rules once installed:**
     - **< 75 withdrawals in month 2:** relocate once, at ~$300.
     - **< 75 in the month after relocation:** sell the unit, recovering ~50–55%.
  4. **Scale to 3 ATMs** only after the pilot does ≥ 150 withdrawals/mo for 2 consecutive months.
- **Customer:**
  - **Host (the B2B customer):** an owner-operated small business whose customers need cash. Typical cases:
    - nail and hair salons, where cash tips are the norm;
    - barbers;
    - cash-only food and bars;
    - laundromats.

    These owners already pay **$2.5–3.5 card-processing percentages** on every card sale and lose sales when customers walk to a bank ATM.
  - **End user:** a customer who needs $20–100 in cash and pays a ~$3.25 surcharge. The 2026 national average surcharge is a record **$3.22**.
- **Problem / desire:** "Half my clients ask where the nearest ATM is and some never come back." "Card fees eat 3% and my techs want cash tips." "The last ATM company pulled their machine because it only did 120 transactions." The merchant also gets the withdrawn cash back in its own account the next day. Operators report that cash withdrawn is often spent on site.
- **Offering:**
  - A free-to-merchant ATM with no lease, a share of each surcharge, next-day settlement of the principal to the merchant's account, and a monthly statement the AI writes.
  - The machine is a refurbished, EMV-compliant Hyosung Halo II or Genmega Onyx-class unit with a cellular modem.
- **Price & revenue model:**
  - **Surcharge:** $3.25 per withdrawal, split **60% owner / 40% merchant**. The merchant share is higher than the usual $0.50–1.00 per transaction because the merchant does the cash work.
  - **Interchange:** a few cents to ~$0.10 net per transaction, kept by the owner.
- **Physical items required?** **Yes.** An ATM and its paper.
  - The seller ships the unit, and a contractor bolts it down.
  - The merchant handles cash and paper.
  - A contractor tech handles jams the merchant can't clear by following the AI's photo guide.
  - The sponsor never touches the machine.

### Upfront capital
| Item | Cost |
|---|---|
| Refurbished EMV ATM, programmed, with cellular modem. New list prices: Halo II $2,652–2,825; Genmega Onyx $2,705. Refurbished price (assumed) $1,300–1,600 | $1,450 |
| Freight with liftgate | $200 |
| Bolt-down install by a contractor | $200 |
| Decals, "ATM inside" window cling, starter paper | $50 |
| **Per ATM installed** | **≈ $1,900** |
| Lob postcards for the demand test (300 × $0.61) | $185 |
| General-liability insurance, first quarter (assumed ~$500–600/yr for a small equipment owner) | $150 |
| Processor setup / state registration, if any (assumed) | $0–200 |
| Optional field rep, 3 signed placements × $100 | $300 |
| **Pilot total (1 ATM)** | **≈ $2,600** |
| **Full build (3 ATMs, staged)** | **≈ $6,400** — above $1k, so it must pass the 12-month payback and P10 tests (see below) |

### Monthly running costs (excluding operator tokens), per ATM at P50 (150 withdrawals)
| Line | P10 (40 tx) | P50 (150 tx) | P90 (350 tx) |
|---|---|---|---|
| Owner surcharge share ($3.25 × 60% = $1.95) + interchange ~$0.10 | $82 | $307 | $717 |
| Processing / ISO fee (beancount guide: $20–50) | −$25 | −$25 | −$30 |
| Cellular modem ($10–15; assumed $15) | −$15 | −$15 | −$15 |
| Repair reserve (1–2 tech visits/yr + parts) | −$30 | −$30 | −$30 |
| Paper | −$5 | −$5 | −$10 |
| Insurance share | −$15 | −$15 | −$15 |
| Bank and reconciliation fees | −$5 | −$5 | −$5 |
| **Net per ATM** | **−$13** | **+$212** | **+$617** |

**Business level at the full build (3 ATMs, P50):**
- Net is $636 − AI tokens ~$75 (light workload) = **≈ $560/mo** before depreciation.
- 5-year straight-line depreciation of ~$5.7k of hardware is $95/mo, which leaves **≈ $465/mo** after all costs.
- **Payback:** $6,400 ÷ $560 ≈ **11.4 months** at run-rate. Units go live in months 2, 3 and 4, so the ramp makes it about **14 months from today**. This is **borderline** and should be flagged.
- **Annualised return on capital:** ≈ 105% at run-rate, against **4%** for T-bills.
- **First-year profit after the sponsor's setup time:** ≈ $4.4k (30 ATM-months × $212, less $900 tokens and the $1,050 setup).

**P10 (bad location) downside:**
- All 3 units at ~40 tx.
- One contractor relocation per unit (~$300 each), then resale of refurbished EMV units at ~$800–1,000.
- Recoverable ≈ $2.7–3.0k of $6.4k, so the loss is **≈ 50–55%**. That is **at the edge** of the PARAMS limit.
- The staged gate (one pilot unit first) caps the realistic P10 loss at ~$1.3k (the pilot's ~$2.6k less ~$1.3k recovered).

### Customer acquisition plan
1. **Build the target list.** The AI uses the Google Places API (within its terms; no scraping) to list salons, barbers, tattoo studios, laundromats and bars in one metro.
2. **Score each business:**
   - "cash only" or "ATM" mentions in public review text;
   - opening hours and busy-times data;
   - distance to the nearest bank ATM;
   - whether an ATM was reported "out of order" or removed.
3. **Mail the top 100 per week** a personalised Lob postcard: "Free ATM. You keep 40% of every fee. No lease. Cash settles to your bank next day." It carries a QR code to a 2-minute form and an email reply address.
4. **The AI answers by email or the form,** sends the plain-English placement agreement for e-signature, and asks for gate evidence.
5. **Install the ATM by contractor.** The AI writes the merchant's one-page guide: loading cash, changing paper, clearing a jam. It then monitors volumes daily.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Merchants whose ATM was recently removed or keeps breaking.** Found in public reviews ("ATM broken again", "they took the ATM out"). These merchants already know their volume and feel the loss. **Speed:** replies in 1–2 weeks.
2. **Lob postcards to scored cash-heavy businesses.**
   - Why it works with no audience: physical mail reaches owner-operators who ignore cold email, and an AI can send it through an API without breaking any platform rule.
   - About $0.61 per card.
   - **Speed:** delivered in 5–7 days; replies in weeks 2–4.
3. **Email to bars and venues with a public contact address.** Kept to ≤ 30/day from a Google Workspace mailbox, and CAN-SPAM compliant: a physical address, an opt-out, and no purchased lists. **Speed:** weeks 1–3.
4. **Referral from installers.** Local ATM techs and handymen often know who just lost a machine. Pay $50 per lead that converts. **Speed:** weeks 3–6.

### Path to first sale
- **Day 0–7:** the sponsor applies to a processor/ISO and buys insurance. The AI builds the scored list and the landing form.
- **Day 7–30:** postcard waves 1–3 go out, with email follow-ups.
- **Day 25–40:** the first signed placement that passes the gate.
- **Day 35–45:** buy the refurbished ATM; freight takes 5–10 days.
- **Day 45–55:** contractor install; the first surcharge settles the next business day.
- **Estimate:** P50 first revenue at **≈ day 50–60 (late Nov to early Dec 2026)**, which falls in the holiday cash and tipping season, a tailwind. P90 is ≈ day 120.

### Who does what
- **AI operator:**
  - prospect scoring and Lob/email outreach;
  - merchant Q&A, agreement drafting from a fixed template, and gate verification;
  - ordering the ATM from an approved vendor list, within the spend limit;
  - booking the contractor install;
  - daily processor-portal reconciliation;
  - out-of-cash and low-paper alerts to the merchant by email;
  - anomaly detection (for example, volume drops of more than 40% week on week, or a jam pattern);
  - dispatching the tech;
  - monthly merchant statements;
  - bookkeeping and a 1099 for each merchant's share;
  - surcharge experiments, within guardrails.
- **Human sponsor:**
  - **one-time:** about 3.5 h as itemised above;
  - **recurring:** about 0.3 h/mo for approvals over the spend limit and police or insurance matters.
- **Project Vend guardrails** (the AI shop that lost money through discounts and errors):
  - **Surcharge:** floor $2.75, ceiling $3.75; at most one ±$0.25 change per unit per month, and only as a logged A/B test.
  - **Merchant split:** the AI may offer only 35–45%. Anything else needs the sponsor.
  - **Spending:** any single spend over **$200** (ATMs, relocations, repairs over $175) and any total over $400/month needs sponsor approval.
  - **No promises:** no "free" promotions and no volume guarantees to merchants.
  - **Contracts:** the AI never edits contract terms beyond the template's blanks.

### Moat — why not just ask ChatGPT?
- The value is a **bolted-down machine plus a signed placement agreement** in a specific shop. No AI clone can copy that.
- **Competition** comes from national ISOs and local independent ATM deployers offering the same "free ATM". Our edges:
  - targeting small cash-tip businesses those firms skip because they want 250–400+ transactions;
  - a higher merchant split;
  - fast, data-driven support.
- **Not a moat:** this is a commodity offer, and a merchant can also buy its own ATM for ~$2.7k.

### Biggest risks (ideator view)
- **Volume is lower than the marketing claims.** Industry blogs claim 150–300 tx/mo. The beancount guide says 100–200 is typical. Managed portfolios trading at ~3.5× cash flow imply much less per placement. **Without the gate the P50 fails payback.**
- **Cash is declining.** The Federal Reserve's 2026 Diary found cash at **6 payments/month, 14% of payments**, down from 7. The decline is slow but real. Cash-tip niches are more resilient.
- **Regulation and partner risk:**
  - processor/ISO approval and KYC;
  - state ATM registration rules (verify for the target state);
  - ADA and surcharge-disclosure rules;
  - processors refuse cannabis and other high-risk merchants, so avoid them;
  - smash-and-grab theft (insurance plus indoor, bolted placement).

---

## P2 — Countertop power-bank rental stations for bars, breweries and bowling alleys

- **Persona:** The Operator
- **One-liner:**
  - **What:** small 8-slot power-bank rental stations (scan a QR code or tap, rent a charged battery, return it to the same station). Each costs about $300 landed and is placed free in long-dwell venues that big networks ignore: neighbourhood bars, breweries, bowling alleys and arcades, car-dealer service lounges, laundromats.
  - **Revenue split:** the venue gets 20% of rentals.
  - **Labour:** **there is no physical labour**. Stations are mailed to the venue, plugged in by staff, and relocated or re-supplied by mail.
- **Unit economics (P10/P50/P90 per station per month):** **−$5 / +$50 / +$330** net, at 4 / 20 / 90 rentals a month.
- **Outsourced labour plan & cost:**
  - **Installation:** venue staff plug the station into a wall socket. It is part of the placement agreement and paid for by their 20% share.
  - **Missing or damaged banks:** a replacement pack is mailed for ~$15, and staff slot it in.
  - **Relocation:** the venue boxes the station; we send a prepaid ground label suitable for lithium batteries, $25–40.
  - **Paid contractor visits:** none needed. If a venue insists on a site visit, TaskRabbit at ~$60/h covers it.
- **Sponsor touchpoints (hours × $300):**
  - **One-time setup:**
    - Stripe account KYC and the OEM rental-platform account: 1 h;
    - approving the import order (supplier ships DDP): 0.5 h;
    - general-liability and product-liability insurance: 0.5 h;
    - sales-tax permit for rentals (taxable in most states): 0.5 h;
    - e-signing venue agreements: 0.1 h each.
  - **Setup total:** ≈ **2.5–3 h = $750–900**.
  - **Ongoing:** about 0.2 h/mo (**$60**). Net of ~$325 allows 1.1 h. **Pass**, but tight.
- **Demand test:** Get venues before buying stations.
  1. **Sign the venues.** In 3 weeks the AI contacts 150 bars, breweries and bowling alleys by Lob and email, and must get **4 venues** to sign a free, cancel-anytime placement.
  2. **Pilot.** Then order 2 stations plus spares (~$870).
  3. **Pass to scale:** **≥ 20 rentals per station per month** at either station for 2 consecutive months. Then buy 6 more (~$1.8k).
  4. **Kill:** < 8 rentals per station per month after 60 days **and** after one relocation. Stop and sell the hardware for ~$100–150.
  5. **Maximum loss:** ≈ $750 plus the sponsor's setup time.
- **Customer:**
  - **Host:** owners and managers of independent bars, breweries and entertainment venues. They want guests to stay longer, ordering another round instead of leaving at 5% battery. They get a free amenity and a 20% share.
  - **End user:** a guest whose phone is dying and who needs it for a ride home, payments or tickets. They already pay $3–4 per half hour at ChargeFUZE and Voltage Nexus kiosks.
- **Problem / desire:**
  - Guests: "Can you charge my phone behind the bar?"
  - Staff hate holding guests' phones, and it is a liability.
  - Guests say "my phone's at 3%, I need to get an Uber."
- **Offering:** A branded station with 8 × 5,000 mAh banks with built-in USB-C and Lightning cables. QR scan, Apple Pay or Google Pay through the OEM app, linked to the sponsor's own Stripe account.
- **Price & revenue model:**
  - **Rental:** $3 for the first 30 minutes, then $1.50 per extra 30 minutes, capped at $12/day. The assumed average is ~$5 per rental.
  - **Non-return:** $40, disclosed before rental.
  - **Venue:** 20% of net rentals.
- **Physical items required?** **Yes.** The stations and batteries.
  - The OEM ships delivered duty paid (DDP) by sea or DG air.
  - The AI forwards one station to each venue by ground mail.
  - Venue staff plug it in.
  - Nobody on our side visits.

### Upfront capital
| Item | Cost |
|---|---|
| 2 × 8-slot stations with 8 banks each. Listed at $128 (ChargeEight) and $174–220 (Y2 Power NEO). Assumed $200 each FOB | $400 |
| US tariff: 3.4% MFN + 25% Section 301 on Chinese lithium-ion (HTS 8507.60) ≈ 28.4%, plus any other China tariffs in force (assume ~30–35%) | $130 |
| Dangerous-goods freight, DDP (assumed) | $150 |
| 4 spare banks | $50 |
| Table tents, decals, QR stickers | $40 |
| Insurance, first quarter (GL and product liability, assumed) | $100 |
| **Pilot total** | **≈ $870 (under $1k)** |
| Scale-up: 6 more stations at ~$300 landed each | $1,800 |
| **Full fleet (8 stations)** | **≈ $2,700** |

### Monthly running costs (excluding operator tokens), per station
| Line | P10 (4 rentals) | P50 (20 rentals) | P90 (90 rentals) |
|---|---|---|---|
| Gross rentals (avg $5; $5.50 at P90) | $20 | $100 | $495 |
| Venue share 20% | −$4 | −$20 | −$99 |
| Stripe fees (2.9% + $0.30) | −$2 | −$9 | −$41 |
| OEM platform/SaaS + SIM (assumed $5–10; **verify**) | −$8 | −$8 | −$8 |
| Battery wear (≈ 500 cycles; replace ~25%/yr) | −$1 | −$4 | −$7 |
| Lost banks net of non-return fees, chargebacks ($15 each) and refunds | −$4 | −$6 | −$10 |
| Sales tax collected and remitted (pass-through) | 0 | 0 | 0 |
| **Net per station** | **≈ −$5** (relocate) | **≈ +$50** | **≈ +$330** |

**Business level at the full fleet (8 stations, P50):**
- Net is $400 − AI tokens ~$75 = **≈ $325/mo** before depreciation.
- 3-year depreciation is ~$75/mo, so **≈ $250/mo** after all costs. That is **just under** the $300 target at P50; it reaches $300+ with 1–2 more stations or 25 rentals per station.
- **Payback:** $2,700 ÷ $325 ≈ **8.3 months**.
- **Annualised return:** ≈ 145% vs 4%.

**P10 downside:**
- If the pilot fails, the loss is ~$750 of $870.
- If utilisation collapses after scaling, stations can be mailed to better venues for ~$30 each, but resale value is low (~30–40%). The fleet P10 loss is therefore **~60% of $2.7k**, above the ~50% guide.
- The two-tranche gate is the mitigation: the second $1.8k is only spent after 2 months of ≥ 20 rentals per station.

### Customer acquisition plan
1. **Build the list.** The AI pulls bars, breweries, bowling alleys and arcades within one metro from the Places API.
2. **Score each venue on:**
   - open until ≥ midnight;
   - review mentions of "charge my phone" or "no outlets";
   - Google "popular times" dwell time;
   - not already served by ChargeFUZE or a similar network (checked against their public venue maps).
3. **Send the pitch** by Lob postcard plus email where public: "Free phone-charging station for your guests. You earn 20% and do nothing."
4. **Sign and ship.** The AI handles e-signature, ships the station with a one-page setup card, and checks telemetry for the first rental.
5. **Optimise monthly:**
   - move stations from the bottom 25% of venues to venues on a waiting list;
   - test prices within guardrails.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Lob postcards to scored venues.** Physical mail reaches owners who never read cold email; it costs ~$0.61. **Speed:** replies in weeks 1–3.
2. **Email to venues with public event or booking addresses** (bowling alleys and breweries publish them), ≤ 30/day and CAN-SPAM compliant. **Speed:** weeks 1–3.
3. **Venue-to-venue referral.** Pay a $25 bar-tab credit for each referred venue that reaches 10 rentals. Brewery and bar owners know each other. **Speed:** month 2+.
4. **Seasonality.** October to December brings holiday parties and bowling and arcade season. Outdoor or beach venues are the wrong target until spring.

### Path to first sale
- **Day 0–5:** the sponsor sets up Stripe and the OEM platform account. The AI orders 1 sample station by express.
- **Day 0–21:** venue outreach, aiming for 4 signed venues.
- **Day 10–20:** test the sample end-to-end: rental, return, non-return charge and refund flow.
- **Day 20–45:** the pilot order clears production, DG freight and customs.
- **Day 45–50:** stations go live. The first rental pays out through Stripe in about 2 days.
- **Estimate:** P50 first revenue at **≈ day 45–55 (late November 2026)**. P90 is ≈ day 90, if customs holds the lithium shipment.

### Who does what
- **AI operator:**
  - venue scoring and outreach;
  - agreement drafting from the template;
  - the OEM order, within the spend limit;
  - shipping labels;
  - telemetry monitoring: slot count, offline alerts and battery health;
  - support for renters by email or SMS reply, but **not cold SMS**;
  - the refund queue;
  - chargeback evidence;
  - monthly venue statements and payouts;
  - sales-tax return preparation;
  - deciding relocations.
- **Human sponsor:**
  - **one-time:** about 2.5–3 h as itemised above;
  - **recurring:** about 0.2 h/mo to approve spends over the limit and sign each new venue agreement.
- **Project Vend guardrails:**
  - **Price:** floor $3 per 30 minutes; the AI cannot create promo codes or free rentals.
  - **Refunds:** automatic only for device faults (a battery that won't charge), capped at $5 per user per month and $50 per month overall. Anything else goes to a sponsor-approved queue.
  - **Non-return fee:** waived only when the station's telemetry confirms the return.
  - **Spending:** over $150 at once, or $300 a month, needs approval.
  - **Venue share:** fixed at 20%, with no AI negotiation.

### Moat — why not just ask ChatGPT?
- The station sitting on the bar and the venue agreement are physical. A software clone cannot copy them.
- **But the hardware moat is thin:**
  - a venue can buy its own $128 station;
  - ChargeFUZE and Voltage Nexus place stations free at bigger venues.
- Our edge is serving small venues those networks skip, at zero hassle to the venue, with AI support for renters. Agreements are month-to-month, so retention depends on venue staff liking it.

### Biggest risks (ideator view)
- **US demand is unproven at small venues.** Brick says a typical European station earns about €2,500/year at about 1 rental a day, and 100+ rentals a month is a showcase result. AnkerBox's 2016 US pilot ($1.99/day) did not scale. The P50 of 20 rentals a month is a guess. **The pilot exists to test it.**
- **Platform lock-in and data risk.** The stations only work with the OEM's server and app. If the OEM shuts down or changes prices, the hardware is bricked. Card data must stay in the sponsor's Stripe account, never on OEM servers. Check FCC and UL certificates and the OEM's terms before ordering.
- **Lithium-battery liability:** fire, recalls and CPSC exposure. Product-liability insurance is needed, and its cost may exceed the $100/quarter assumed. Tariffs on Chinese batteries could rise further.

---

## P3 — PlacementDesk: AI location sourcing for established route operators, paid per install

- **Persona:** The Operator
- **One-liner:**
  - **What:** the AI finds, qualifies and introduces host locations (offices with 40+ staff, warehouses, laundromats, gyms, apartment clubhouses, auto shops) to **established local route operators** in several non-competing categories: snack and drink vending or micro-markets, ATMs, massage chairs, air and vacuum machines, and power banks.
  - **How we are paid:** **only after the machine is installed**, with a flat fee plus a small residual.
  - **What we own:** no machines, no inventory, no labour. This is the "partner with an existing route operator" structure, materially different from U5: the operator owns the machines and does all physical work.
- **Unit economics (P10/P50/P90 per qualified lead sent to an operator):**
  - **P10:** $0. The lead is rejected or the host backs out.
  - **P50:** **$250 one-time + ~$20/mo residual** (3% of a ~$650/mo machine for 24 months).
  - **P90:** $400 + $40/mo, for a micro-market or a high-volume ATM.
  - **Assumed lead-to-install rate:** ~30%.
  - Industry guides claim $500–1,500 per placement or 5–20% residuals. Those figures come from sellers and are **discounted here**.
- **Outsourced labour plan & cost:** None needed. The operator does the site visit, installation, restocking and service as part of its normal business; that labour is why the operator pays for the location. No contractor is ever paid by us.
- **Sponsor touchpoints (hours × $300):**
  - **One-time setup:**
    - a 30-minute intro call with each of 3 operators, because the AI cannot make calls: 1.5 h;
    - e-signing referral agreements: 0.75 h;
    - domain, Workspace and business bank account (assumed existing): 0.5 h;
    - optional review of the template by a lawyer: 0.5 h.
  - **Setup total:** ≈ **3.25 h = $975**.
  - **Ongoing:** about 0.5 h/mo (**$150**) for one new-operator call or a payment dispute. At $300+ net this allows 1 h. **Pass.**
- **Demand test (two-sided; operators first):**
  1. **Operators.** The AI emails 25 established operators in one metro (≥ 2 years trading, ≥ 10 machines), found through Google Maps, NAMA member listings and ISO referral programmes. **Pass:** ≥ 2 sign a pay-on-install referral agreement with written lead criteria within 21 days.
  2. **Hosts.** Then 400 host contacts by Lob and email over 30 days. **Pass:** ≥ 6 leads accepted by operators and ≥ 2 installs by day 75.
  3. **Kill:** < 2 accepted leads by day 60. The loss is ~$400 plus the sponsor's setup time.
- **Customer (who pays):**
  - **Who:** local vending, micro-market, ATM, massage-chair and amusement route operators, plus ATM ISOs with partner or referral programmes.
  - **What they already pay for:** locator services (whose reputation is poor) and their own time spent cold-calling.
  - **Where they are:** NAMA, VendingMarketWatch, and Google Maps "vending service" listings.
  - **Hosts pay nothing.** They get a free amenity and sometimes a commission.
- **Problem / desire:**
  - Operators: "Finding good locations is the whole business, and I hate prospecting." "Locators sold me junk leads for $1,000 upfront." Our answer is to charge nothing until the install happens.
  - Hosts: "Our break room has nothing and staff leave the site for snacks." "Customers keep asking for an ATM."
- **Offering:**
  - **Operators get:** qualified, consented host introductions. Each comes with a one-page brief: headcount or traffic, hours, existing amenities, decision-maker contact, and the host's stated preferences.
  - **Hosts get:** one point of contact who can arrange **several** amenities from vetted local operators, for example vending plus an ATM plus a massage chair at a laundromat.
- **Price & revenue model:**
  - **Pay on install:** $150–400 per installed placement, depending on category. P50 is $250.
  - **Residual:** 2–5% of the machine's gross for 24 months, reported from the operator's telemetry statements. For ATMs, a per-transaction referral residual where the ISO offers one.
  - **Upfront fees:** none.
  - **Invoicing:** monthly, Net-15.
- **Physical items required?** **No.** We hold none. Operators supply and service all machines.

### Upfront capital
| Item | Cost |
|---|---|
| Domain + Google Workspace mailbox (3 months) | $55 |
| Google Places API (assumed mostly free tier) | $0–50 |
| Lob postcards for host outreach (400 × $0.61) | $245 |
| Simple site with an operator page and a host intake form (Cloudflare Pages) | $0 |
| Optional: flat-fee lawyer review of the referral-agreement template | $0–250 |
| **Total** | **≈ $300–600 (under $1k)** |

### Monthly running costs (excluding operator tokens)
- **Overheads:** Workspace $14, Places API $0–20, Lob postcards ~$60 (100/mo), domain $1. **≈ $95/mo.**
- **Payment fees:** ACH invoicing through the bank, ~$0; Stripe invoicing 0.4–0.5% if needed.
- **AI tokens:** ~$100/mo, the heaviest of the three ideas because of research and writing.
- **Break-even for $300 net:** ≈ $495/mo revenue. That is ~1.6 installs/month at $250 plus accumulated residuals, or fewer installs once residuals stack up.
- **Ramp:**
  - **P50 month 4:** 2 installs → $500 + $40 residual − $195 = **≈ $345 net**.
  - **P50 month 9:** 2 installs/mo + ~$200/mo residual → **≈ $500 net**.
  - **P90:** 5 installs/mo → $1,250 + residuals → **≈ $1,200+ net**.
  - **P10:** 0–0.3 installs/mo → **≈ −$150/mo**, killed at day 60–90.
- **Payback:** capital of ~$500 ÷ $345 ≈ **1.5 months** at P50 run-rate (≈ 5 months from today including ramp).
- **Annualised return:** hundreds of percent at P50, against 4% for T-bills. On so little capital, the real cost is the sponsor's $975 of setup time.

### Customer acquisition plan
1. **Operators (supply side).**
   - The AI compiles 25–40 established operators per metro and emails each one personally.
   - The pitch: "We send you consented, qualified locations in [area]. You pay only when the machine is installed."
   - Interested operators get a 30-minute call with the sponsor and then a template agreement. Each agreement includes lead registration, non-circumvention and statement access for the residual.
2. **Hosts (demand side).**
   - The AI scores businesses by headcount (job postings, LinkedIn company size shown on public pages, and number of reviews), hours and existing amenities.
   - It sends Lob postcards and low-volume email offering "free break-room vending / ATM / massage chair from a vetted local provider."
3. **Qualification.**
   - The host answers 6 questions on a form.
   - The AI writes the brief and registers the lead with a timestamp with the matching operator, who must accept or reject within 5 days.
4. **Close.**
   - The operator visits and installs; that is their labour.
   - The AI confirms the install with the host, invoices, and tracks the residual.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Operator side: personalised email to established operators.** They are few, findable and motivated, and pay-on-install removes the "locator scam" objection. Lesson 14 sets the expectation at a **5–10% yes-rate**. **Speed:** first signed operators in weeks 1–3.
2. **Host side: Lob postcards to mid-size workplaces and laundromats.** Physical mail reaches facility managers and owners. **Speed:** replies in weeks 2–5.
3. **Host side: ATM and vending requests that are already public.** Examples: reviews saying "wish they had a vending machine" or "no ATM", and building-amenity RFPs posted by property managers. **Speed:** ad hoc, from week 2.
4. **Seasonality.** Q4 is slow for host decisions (holidays). Facilities budgets and new-year amenity refreshes make January–February the stronger window, so first installs most likely land in January 2027.

### Path to first sale
- **Day 0–21:** operator outreach and calls; 2–3 agreements signed.
- **Day 14–45:** host outreach; first accepted leads.
- **Day 45–75:** operators' site visits; first install.
- **Day 75–90:** first invoice paid (Net-15).
- **Estimate:** P50 first cash at **≈ day 80–100 (late Dec 2026 to mid Jan 2027)**. This is at or just past the ≤ 90-day preference. P90 is ≈ day 150.

### Who does what
- **AI operator:**
  - building and scoring operator and host lists;
  - all written outreach (Lob plus low-volume, compliant email);
  - host intake, briefs and lead registration;
  - operator follow-ups;
  - install confirmation;
  - invoicing and residual reconciliation against operator statements;
  - spotting non-circumvention breaches (for example, an installed machine that was never invoiced, found through follow-up emails to hosts);
  - CRM and bookkeeping.
- **Human sponsor:**
  - **one-time:** about 3.25 h, mostly operator calls;
  - **recurring:** about 0.5 h/mo for new-operator calls and disputes.
- **Project Vend guardrails:**
  - the AI cannot offer hosts money, gifts or commissions beyond what the operator's written terms allow;
  - it cannot discount our fee below $150, or waive or extend terms;
  - it cannot promise a host any machine or service level, and quotes only the operator's written terms;
  - outreach is capped at 30 emails/day and ≤ 150 postcards/week;
  - total spend over $150/month needs sponsor approval.

### Moat — why not just ask ChatGPT?
- **The moat is weak to moderate.**
  - AI SDR tools and human locators already exist (lesson 19).
  - Operators can prospect for themselves.
- **What can't be cloned:**
  - signed agreements with local operators (each territory supports only a few);
  - the record of qualified leads and outcomes;
  - the multi-category "amenity bundle" relationship with each host.
- Pay-on-install is a real differentiator against the upfront-fee locators that operators distrust.

### Biggest risks (ideator view)
- **Regulation and licensing:**
  - **FTC Business Opportunity Rule (16 CFR 437).** The Rule applies to sellers who promise to provide locations to buyers starting a new business. *Never* serve new or aspiring operators or anyone buying machines; serve only established operators, and charge no upfront fee. Many states have similar laws.
  - **Real-estate brokerage.** Brokering a lease of space for a fee can require a real-estate licence in some states. Keep placement agreements as equipment licences between operator and host, and position our fee as lead generation. **The legal analyst should check this.**
- **Two-sided cold start and the partner-channel trap** (lesson 14):
  - operators may sign up and then not act on leads;
  - hosts may want a call, which the AI can't make (the operator makes it);
  - hidden sponsor time can creep above 0.5 h/mo.
- **Non-payment and circumvention.** An operator may claim "we already knew them" or install quietly. Mitigations: timestamped lead registration, the host's written acknowledgement, and small claims if needed. Without a residual this is a one-off business.

---

## Sources (accessed 2026-10-06)
- Brick partner FAQ: 70/30 split, €5/station/mo, €10k minimum, ~1 rental/day typical, 5–15 at strong venues, ~1% of banks bought — https://articles.brick.tech/faq/
- Brick bar case study: 100+ rentals/month in a busy Stockholm bar — https://articles.brick.tech/case-study-placing-a-powerbank-station-in-a-bar/
- Voltage Nexus US kiosks, $4/h capped at $50, partner-owned kiosks (Vending Times, 2026-08-13) — https://www.vendingtimes.com/news/voltage-nexus-launches-portable-battery-rental-kiosk-network/
- Voozaa partner terms: $7,500 for 3+ kiosks, 80% to the owner, $65 non-return fee (BizQuest listing, via search) — https://www.bizquest.com/start-up-business/voozaa-power-banks-7-4k-minimum-buy-in-massive-potential/BW2552133/
- $128 8-slot station (Notebookcheck, 2024) — https://www.notebookcheck.net/128-8-slot-Power-Bank-may-entice-small-shop-owners.881504.0.html
- US rental power-bank pricing (ChargerLab) — https://www.chargerlab.com/charge-on-the-go-exploring-rental-power-bank-options-at-ces-2024-and-the-us/
- AnkerBox US pilot, $1.99/day — https://techcrunch.com/2016/03/29/anker-ankerbox/
- HTS 8507.60 duty and Section 301 tariff — https://www.htshub.com/us-hs/head/85076000
- ATM economics (ATM Marketplace / ATM Link, 2025-09-23) — https://www.atmmarketplace.com/blogs/are-atms-still-a-profitable-business/
- ATM bookkeeping guide: $3.22 average surcharge, 100–200 tx typical, $20–50 processing, $10–15 wireless (beancount.io, 2026-09-14) — https://beancount.io/blog/2026/09/14/atm-vault-cash-surcharge-bookkeeping-interchange-reconciliation-guide
- Merchant-load volume thresholds of 250–300 tx (ATM Marketplace, 2002) — https://www.atmmarketplace.com/news/return-of-the-placement/
- Hyosung Halo II price, $2,652–2,825 — https://www.ebay.com/p/1672533568
- Genmega Onyx price, $2,705 — https://mossdistributing.com/atm/pid308/venco-genmega-onyx-atm
- ATM portfolio sold at 3.5× cash flow (275 placements, $500k) — https://joinaccredited.com/deals/275-location-atm-portfolio-duval-county-fl
- Federal Reserve 2026 Diary of Consumer Payment Choice (cash 14% of payments) — https://www.frbservices.org/binaries/content/assets/crsocms/news/research/2026-diary-consumer-payments-choice.pdf
- Lob postcard pricing, $0.582–0.612 — https://lob.com/pricing
- Locator compensation claims, $500–1,500 or 5–20% (vmfsusa; seller-biased) — https://vmfsusa.com/blogs/business/get-paid-to-find-locations-for-vending-machines-guide
- Vending revenue splits and commissions (vmfsusa) — https://vmfsusa.com/blogs/business/vending-machine-revenue-split-operator-vs-location-vs-supplier
- FTC Business Opportunity Rule overview — https://www.sgrlaw.com/business-opportunity-rule/
- J.E. Adams 8799PV card air machine, $5,285.71 — https://www.kleen-ritecorp.com/p-45043-j-e-adams-8799pv-digital-air-machine-with-credit-card-vault-and-monitoring.aspx
- Car-wash forum air-machine revenues — https://www.carwashforum.com/threads/air-machine-again.13814
- Free-air laws in CA and CT — https://engineerfix.com/is-gas-station-air-free-the-laws-and-reality/
- Infinity IT-6900 vending massage chair, $3,499 — https://selectfitness.com/products/infinity-it-6900-vending-massage-chair
- Vending massage chair route, $150–980/mo per chair (BizQuest, via search) — https://images.bizquest.com/business-for-sale/turnkey-vending-massage-chair-route/BW2331746
