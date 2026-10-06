# Legal Risk Analyst: round 3 (2026-10-06)

*This is a risk screen, not legal advice. Before any capital is committed, a licensed attorney in the launch state should review the contracts and every regulated activity.*

Scale: 10 = ordinary e-commerce risk only; ≤ 3 = hard-gate reject. Each risk is rated **likelihood × severity** (L × S).

## Summary

| ID | Idea | Legal safety score | Overall risk (Low/Med/High) | Top risk | Key mitigation |
|---|---|---|---|---|---|
| Q1 | UltraWideo-class extension acquisition | 6 | Med | Billing transfer. Lemon Squeezy subscriptions can't be ported. Buying Devilos LLC inherits its liabilities. Moving to plain Stripe makes the sponsor the seller of record for EU VAT and US digital-goods tax. | Asset purchase (not entity) under a lawyer-reviewed APA: IP assignment, reps, indemnity and an escrow holdback. Stay on a merchant of record (Lemon Squeezy written confirmation, or Stripe Managed Payments). |
| Q2 | Wheel of Life-class app acquisition | 6 | Med | Inherited privacy exposure on wellbeing and journaling data (Washington My Health My Data Act private right of action, FTC Health Breach Notification Rule, GDPR), plus transfer snags (Sign in with Apple, subscription shared secret). | Data-flow and SDK due diligence, APA privacy reps, strip health claims. Hold the developer accounts in an LLC with a D-U-N-S number. |
| Q3 | ≤ $3k fire-sale standing buy order | 5 | Med | A 48-hour close squeezes legal due diligence on assets from serial AI-app builders: unclear IP chain (AI or GPL code, others' trademarks), platform-ToS breaches, faked revenue, accounts shared across many apps. | Short-form APA and checklist pre-approved once by a lawyer. Escrow with a holdback. Walk away if any account lacks a documented transfer route. |
| B1 | HSK 3.0 speaking mock | 7 | Low | Affiliate and testimonial disclosure (FTC Endorsement Guides; fake-review rule penalties), plus the pre-order delivery promise. | Affiliate terms that require disclosure, plus monitoring. Real testimonials only. Nominative "HSK" with no "official". Auto-refund if 1 Nov is missed. Consent to voice recording and no audio retention. |
| B2 | SubWatch OSHA monitoring | 6 | Med | Defamation or tortious-interference claim when a sub is wrongly matched to another firm's citations and loses an award. | Human-confirmed matches only. Verbatim DOL data with source links and "contested / not final" labels. Correction process. E&O cover. (The ad-policy risk is lower than the ideator assumed.) |
| B3 | Heirloom cookbook gift certificate | 6 | Med | Gift-certificate law (no expiry; CA bans expiry; unclaimed property), plus the FTC Mail Order Rule against "under the tree" claims in peak shipping. | No expiry and no fees. Delivery claims carry a Lulu and carrier margin. Rights warranty in the ToS and screening for published clippings. Written release before any customer content appears in ads. |
| P1 | Merchant-loaded ATMs | 5 | Med | Placement compliance stack: ADA (CA Unruh suits), expired PCI PTS PIN pads on refurbished units, state registration and surcharge rules, EBT blocking in bars, money transmission if the principal flows through the sponsor. | Use an established ISO that pre-approves the model and serial. Principal settles from the ISO straight to the merchant. ADA install spec. LLC, plus GL and theft cover. Screen out high-risk merchants. |
| P2 | Power-bank rental stations | 4 | High | Lithium fire and product liability on imported OEM stations, where the sponsor is the first US party in the chain. Hazmat mailing by untrained venue staff. | Only UL 2056 banks and NRTL-listed stations with UN38.3 reports. Bind and price product-liability cover before ordering. LLC. Pre-marked OEM return kits; never mail damaged banks. |
| P3 | PlacementDesk location sourcing | 6 | Med | The FTC Business Opportunity Rule's "provide locations" prong is triggered whenever a client enters a "new line or type of business". Fees may be unenforceable under state real-estate broker laws. | Refer only within categories each operator already runs. No earnings or location-quality claims. Introduction-only role. Check the launch state's bizopp and broker law. |
| U5 | AI-managed vending (outsourced labour) | 6 | Med | Individual restockers misclassified under ABC tests, plus uninsured injury claims. | Contract an established route-operator business (own insurance, certificate of insurance, multiple clients). Per-state vending sales tax and permits. GL and product cover. Avoid government property. |

**Cross-cutting notes**
- **Entity.** Form an LLC before signing any APA, placement or venue contract (all Q, P and U5 ideas). Apple organisation accounts need a D-U-N-S number anyway. Under the EU DSA, a "trader" developer's address and phone are published on Apple, Google Play and the Chrome Web Store. An LLC with a business address keeps the sponsor's home address off those pages.
- **Lemon Squeezy concentration.** B1, B2, D2 and Q1 would all run on Lemon Squeezy. Lemon Squeezy is being folded into Stripe Managed Payments (public preview since Feb 2026), and its affiliate tools, which B1 relies on, are not in Stripe Managed Payments. Use separate stores per product (lesson 17) and plan for a forced migration.
- **Google Ads accounts.** Google suspends *related* accounts and treats new accounts opened to escape enforcement as circumvention. A separate account for B2 does not protect B1.

---

## Q1: UltraWideo-class extension acquisition (score 6, Med)
- **Billing transfer.** L: High × S: Med.
  - Lemon Squeezy documents no store-ownership transfer.
  - The merchant of record holds the card tokens, so route (b) means asking customers to re-subscribe. That needs fresh ROSCA and state auto-renewal-law consent. A new descriptor also invites chargebacks.
  - Moving to plain Stripe ends merchant-of-record cover. The sponsor would then owe EU/UK VAT on digital services from the first sale (OSS registration) plus US state digital-goods tax.
  - *Mitigation:* get Lemon Squeezy's answer in writing before the LOI. If migrating, go to Stripe Managed Payments. Use an auto-renewal-compliant checkout and a one-click cancel.
- **Entity-purchase liabilities.** L: Med × S: Med–High. Buying Devilos LLC brings unknown tax, IP and contract claims with it. *Mitigation:* buy the assets. If it must be an entity purchase, require full reps, an indemnity, a 10–15% escrow holdback and seller tax clearance.
- **IP chain of title.** L: Med × S: Med.
  - The APA must assign:
    - the copyright in the code;
    - the "UltraWideo" name and its common-law trademark;
    - the domain, the listing content and the Discord server.
  - Audit open-source licences: GPL code inside a paid extension is a problem.
- **Chrome Web Store.** L: Med × S: High (business-ending).
  - Transfer goes through Google's form.
  - Extension ownership changes are under heightened 2026 scrutiny because bought extensions have been weaponised.
  - New permissions or remote code trigger a re-review.
  - Keyword-stuffed listings in 41 locales breach the spam policy.
  - *Mitigation:* make no permission changes for 90 days. Update the privacy policy to name the new owner. Get the strike history.
- **Privacy.** L: Low × S: Med. Transferring user data must be permitted by the current privacy policy. Notify users after close.
- **Listing trademarks.** Use "Netflix" and "YouTube" nominatively only, with no logos.

## Q2: Wheel of Life-class app acquisition (score 6, Med)
- **Wellbeing data.** L: Med × S: Med–High.
  - Life-area ratings and journaling can reveal mental or emotional health. That puts the app within reach of the Washington My Health My Data Act (separate consent, private right of action), the FTC Health Breach Notification Rule, and GDPR special-category data.
  - Third-party analytics SDKs that share event data are the GoodRx/BetterHelp-style enforcement pattern.
  - *Mitigation:* map the data flows and SDKs during due diligence. Put privacy reps and an indemnity in the APA. Remove the "therapists use it" copy. Offer in-app account deletion.
- **Transfer mechanics.** L: Med × S: Med.
  - Apple requires an app-specific shared secret for auto-renewable subscriptions.
  - Sign in with Apple user IDs are team-scoped and need the migration process.
  - Google Play and RevenueCat have their own transfer steps.
  - *Mitigation:* make transfer completion an escrow release condition.
- **Pricing changes.** L: Low × S: Med. Existing lifetime buyers must keep access; taking it away would be deceptive. Price rises for existing subscribers must use the stores' consent flows.
- **Reviews.** L: Low × S: Med. Review prompts must not be incentivised (FTC fake-review rule; App Store guidelines).
- **Trademark.** L: Low × S: Low. "Wheel of Life" is a generic coaching term, so expect a weak mark. Run a knockout search and get assignment of the code, art and any font or stock licences.
- **Entity.** Hold the accounts in an LLC. Apple 2FA and agreement acceptances stay with the sponsor.

## Q3: ≤ $3k fire-sale buy order (score 5, Med)
- **Compressed legal due diligence.** L: High × S: Med. A 48-hour decision window means legal defects become part of the adverse selection.
- **IP chain.** L: Med × S: Med.
  - AI-written code has thin copyright. That doesn't stop the buyer using it, but it gives no exclusivity.
  - Check for GPL code and code copied from competitors.
  - Many flipped apps put others' trademarks in their names ("AI YouTube…"). That is a trademark issue and a store-rejection risk.
- **Inherited platform-ToS breaches.** L: Med × S: High.
  - Watch for products that scrape or automate in breach of ToS, or that run on the seller's YouTube, OpenAI or Google API keys. Many API terms bar transferring keys.
  - Serial builders often run 10–35 apps in one Stripe, Lemon Squeezy or Apple account. Only an app-level transfer works; payment accounts can't be split.
- **Faked revenue.** L: Med × S: Med. Watch for self-purchases and one-off deals. *Mitigation:* accept only API-verified revenue, and add a revenue-accuracy rep with clawback.
- **Marketplace terms.** L: Low × S: Low. Flippa and Microns bar going around them to avoid their fees. Close on-platform.
- **Mitigation overall:**
  - one standing short-form APA and checklist, reviewed once by a lawyer (about $300–500, amortised);
  - Escrow.com with an inspection period and a 14-day holdback;
  - reps covering title, IP, ToS compliance, no pending claims and data practices.

## B1: HSK 3.0 Speaking Mock (score 7, Low)
- **Affiliates and testimonials.** L: Med × S: Med.
  - The advertiser is liable for affiliates' undisclosed endorsements.
  - The FTC's Consumer Reviews & Testimonials rule (16 CFR 465) carries civil penalties of about $53k per violation for fake or AI-written testimonials.
  - *Mitigation:* the affiliate terms require a clear disclosure, and the operator spot-checks. Use real testimonials only.
- **Pre-order promise.** L: Low × S: Med. Confirm Lemon Squeezy permits pre-sales. Disclose the 1 Nov date, and refund every pre-order automatically if it is missed.
- **"HSK" mark and official claims.** L: Low × S: Med.
  - HSK is CLEC/CTI's mark: nominative use only, with no logo and no "official" or "pass guaranteed".
  - Google may restrict the trademark in ad text if the owner complains.
  - Write original prompts. Don't copy official specimen papers or audio.
- **Voice data.** L: Low × S: Med. Illinois BIPA plaintiffs target voice data. Pronunciation scoring isn't speaker identification, but still:
  - get consent at the first recording;
  - delete audio after scoring;
  - confirm Azure is set to no retention.
- **AI accuracy claims.** L: Low × S: Med. Make no score-prediction or accuracy claims without evidence (the FTC's AI enforcement).
- **EU buyers.** Capture the 14-day withdrawal waiver for digital content at checkout, or honour refunds.
- **Minors.** Some candidates are teenagers. Set terms to 18+ or require parental consent.

## B2: SubWatch (score 6, Med)
- **Defamation, false light and tortious interference.** L: Med × S: High.
  - A wrong fuzzy match pins another firm's fatality or willful citation on a small sub, and the GC drops it.
  - The fair-report privilege covers accurate reproduction of official records. It does not cover misattribution.
  - *Mitigation:*
    - only user-confirmed matches go on the PDF;
    - show match confidence;
    - quote verbatim and link the source;
    - label citations "contested / not final";
    - run a 48-hour correction and takedown process for subs;
    - carry E&O and media-liability cover;
    - cap liability in the ToS.
- **Ad policy (corrected).** L: Low × S: Med.
  - Google's *Government documents and official services* policy lists specific acquisitions: business identifiers, criminal background checks, licences, vehicle registration and similar.
  - The 5 Oct 2026 change tightens *authorisation* of providers. Third-party analysis of OSHA enforcement data is not listed.
  - Still avoid the OSHA logo and any "official" claim (Misrepresentation policy).
  - A separate Ads account does not isolate a suspension.
- **FCRA.** L: Low × S: Med. Reports on businesses for business purposes are generally not consumer reports. Sole proprietors are the edge case. The ToS should bar employment, credit and insurance uses about individuals, and the site should never use "background check".
- **Data licence.** L: Low. DOL data is a public-domain government work. Attribute it and imply no endorsement.
- **Marketing.** Nurture email must be CAN-SPAM compliant. The privacy policy must disclose LinkedIn retargeting, with US-only targeting.

## B3: Heirloom Cookbook (score 6, Med)
- **Gift certificates.** L: Med × S: Med.
  - Under Reg E §1005.20, an emailed or PDF certificate is *not* excluded as "paper form only", so the CARD Act applies if a dollar value is stated: at least 5 years before expiry, and no dormancy fees in year 1.
  - A "one cookbook" certificate with no amount is generally outside it.
  - California (Civ. Code 1749.5) bans expiry on gift certificates outright. Unredeemed balances may be unclaimed property in some states.
  - *Mitigation:* no expiry and no fees; a refund on request; book the unredeemed amounts as a liability and check the home state's escheat rules.
- **FTC Mail/Internet Order Rule.** L: Med × S: Med.
  - "Upload by Nov 20 → under the tree" needs a reasonable basis given Lulu's December production and carrier times.
  - If a book will be late, the buyer must be notified and offered a refund.
  - Use an approval cutoff with a buffer, and hedged wording.
- **Copyright in uploads.** L: Med × S: Low–Med.
  - Ingredient lists aren't protected, but recipe boxes often hold clipped magazine or branded recipe cards (Betty Crocker card-library-style) with protected text and photos.
  - The business prints the copies, and printing gets no DMCA safe harbour.
  - Lulu's terms put the rights warranty on the business.
  - *Mitigation:* a rights warranty and indemnity in the ToS; an AI flag for printed or branded cards, which are then excluded.
- **Publicity and privacy in ads.** L: Med × S: Med.
  - Customers' handwriting, names and photos need a written release before use in Meta creative. Some states (e.g. CA) protect publicity rights after death.
  - Verify the terms of the "public-domain" card sources.
  - Bereavement or personal-attribute ad copy ("Lost your mom?") breaches Meta policy.
- **Product.** L: Low × S: Low. Add a disclaimer: "transcribed as written; recipes untested".
- **Tax.** Use Stripe Tax, and give Lulu a resale certificate to avoid double tax.
- **Share links.** Use unguessable, expiring links, and delete uploads after printing.

## P1: Merchant-loaded ATMs (score 5, Med)
- **Network and sponsor-bank compliance.** L: Med × S: High.
  - An ATM must connect through an ISO with a sponsor bank.
  - Refurbished units with an expired PCI PTS PIN pad (EPP) or an unsupported OS can be refused or cut off.
  - *Mitigation:* the ISO approves the model and serial before purchase.
- **Money transmission.** L: Low × S: High. Limited-service ATMs are not MSBs (FinCEN FIN-2007-G006). But if the merchant's principal is routed through the sponsor's account and then paid on, that resembles money transmission, and some states treat it that way. Settlement must go directly from the ISO to the merchant.
- **AML exposure.** L: Low × S: High.
  - Cash-only targets are FinCEN high-risk. A merchant can load illicit cash and receive clean ACH settlement.
  - *Mitigation:* the ISO does KYC on the merchant's account; flag volume that doesn't match foot traffic; never accept changes to where settlement is paid.
- **State rules.** L: Med × S: Med.
  - At least 21 states have surcharge statutes.
  - Texas has pursued a non-bank ATM registry and sticker (HB 2629 / SB 337); verify its status. Illinois repealed its registration requirement.
  - Federal law requires EBT cash blocking at ATMs in liquor stores, casinos and adult venues, and some states extend this to bars.
  - The Reg E on-screen fee notice is required.
- **ADA.** L: Med × S: Med.
  - The 2010 Standards §707 require speech output and Braille, plus reach ranges and clear floor space.
  - In California, Unruh suits carry statutory damages of $4,000 or more per visit.
  - Mitigation: a written install specification.
- **Cash, skimming and robbery.** L: Low–Med × S: Med–High.
  - The placement agreement must allocate:
    - who owns cash in the machine;
    - who bears losses;
    - who bears misdispense chargebacks;
    - daily skimmer checks;
    - who insures what;
    - removal rights.
  - Carry an LLC and GL plus equipment and theft cover. Issue 1099s for the merchant shares.

## P2: Power-bank rental stations (score 4, High)
- **Fire and product liability.** L: Low–Med × S: High.
  - Power-bank recalls continue; Casely's 429k-unit recall involved a death.
  - Rental banks get dropped and abused.
  - When the OEM has no US presence, the sponsor is the first US party in the chain: strict liability as distributor or lessor, and a CPSA §15(b) duty to report defects.
  - *Mitigation:*
    - UL 2056-certified banks;
    - NRTL-listed stations (OSHA 1910.303 requires approved electrical equipment in the venue's workplace);
    - FCC Part 15 and cellular certification;
    - UN38.3 test reports;
    - an LLC;
    - product-liability cover **quoted before ordering**. Lithium exclusions or premiums may break the $100/quarter assumption.
- **Hazmat shipping.** L: Med × S: Med.
  - 49 CFR 173.185 and USPS Pub 52: ground only, marked packages, and no damaged or defective cells by mail.
  - When venue staff pack a station, the sponsor is the offeror. PHMSA penalties run per violation.
  - Mitigation: send pre-marked OEM return kits.
- **Venue contracts.** L: Med × S: Med. Venues will want an indemnity and additional-insured status. Cap the indemnity at the policy limits.
- **Import.** L: Low × S: Med. Chinese DDP shippers sometimes undervalue goods, which raises a customs-penalty risk. Tariffs are volatile.
- **Rentals and payments.** L: Med × S: Low.
  - Disclose the $40 non-return fee in a clickwrap before rental.
  - Confirm the sponsor's Stripe is the merchant, and check the OEM's PCI status and renter-data terms.
  - SMS: replies only (TCPA).
  - Register for rental sales tax.

## P3: PlacementDesk (score 6, Med)
- **FTC Business Opportunity Rule (16 CFR 437).** L: Low–Med × S: High.
  - "Providing locations" for vending machines is the Rule's core prong.
  - The only thing keeping P3 out is the "new business" element. That *includes a "new line or type of business"*. Pitching ATMs to a vending operator, or massage chairs to an ATM ISO, could bring P3 back in.
  - A pay-on-install fee is still a "required payment".
  - Penalties are about $53k per violation, and several state bizopp acts add private rights of action.
  - *Mitigation:*
    - refer only within categories the operator already runs, with written acknowledgement;
    - make no earnings or location-quality claims;
    - never serve people who are buying machines.
- **Real-estate licensing.** L: Low–Med × S: Med.
  - Placement agreements are usually licences, not leases. But some states' broker definitions cover anyone soliciting occupants of property for a fee, and California's finder exception is narrow.
  - The realistic harm is an operator refusing to pay and a court declining to enforce the fee.
  - *Mitigation:* introduction only, with no negotiation of host terms; describe the fee as lead generation; run a launch-state check.
- **Collection and circumvention.** L: Med × S: Low–Med. Use timestamped registration, the host's acknowledgement, and small claims if needed.
- **Google Maps Platform terms.** L: Med × S: Low. Places content can't be cached beyond the permitted window (place IDs excepted). Store only the operator's own notes.
- **Outreach.** CAN-SPAM. Never quote host commissions beyond the operator's written terms.

## U5: AI-managed vending (score 6, Med)
- **Contractor misclassification.** L: Med–High × S: Med.
  - An individual restocker paid weekly to do the core work fails ABC-test prong B (CA, MA, NJ).
  - An injured, uninsured restocker can sue the sponsor directly.
  - *Mitigation:* contract an established route-operator business with its own vehicle, clients, workers' comp and a certificate of insurance. Use TaskRabbit only for one-off tasks.
- **Sales tax.** L: Med × S: Low–Med. Vending has special rules: tax-included pricing, partial-receipt formulas, and per-location or per-machine registration in some states. Register before the first sale.
- **Food permits.** L: Med × S: Low–Med.
  - Shelf-stable prepackaged food is often exempt from health permits. Refrigerated or fresh items (micro-markets) usually need a state or local food-vending licence.
  - Many cities require per-machine business licences.
  - FDA calorie labelling only applies at 20 or more machines.
- **Product liability.** L: Low × S: Med. Covers expired product, allergens and recalls. Carry GL plus products cover; hosts will want a certificate of insurance and an indemnity.
- **ADA.** L: Low × S: Med. Operable parts must be within reach range.
- **Government property.** L: Low × S: Med. Federal property gives blind vendors priority (Randolph–Sheppard), and state equivalents do the same; avoid public buildings.
- **Host agreement.** Commission, term, removal, damage and theft. A card-only setup cuts cash-handling risk. Use an LLC.
