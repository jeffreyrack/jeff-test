# Legal Risk Review — run 2026-10-06

> **Not legal advice.** This is a risk screen from an AI reviewer. The human sponsor should get advice from a licensed attorney before relying on any of it.

Scale: 10 = ordinary e-commerce risk only; ≤ 3 = hard-gate reject. Overall risk bands: **Low** = 8–10, **Med** = 5–7, **High** = ≤ 4. L × S = likelihood × severity (each Low/Med/High).

## Summary

| ID | Idea | Legal safety score | Overall risk (Low/Med/High) | Top risk | Key mitigation |
|---|---|---|---|---|---|
| T1 | RainCheck for Jobber | 8 | Low | SMS "client notices" sent for owners trigger TCPA/A2P 10DLC duties; weather-reliance claims | Ship email-only v1; SMS only after 10DLC registration and owner consent attestation; "forecast is advisory" terms; follow Jobber developer and brand terms |
| T2 | Accela/EnerGov Permit Extractor (Apify) | 5 | Med | Automated scraping of hundreds of government/Accela-hosted portals, then reselling homeowner names and addresses for lead gen. Expect C&D letters, IP blocks and Apify Actor takedowns | Never bypass CAPTCHA or login; honour robots.txt and portal use notices; rate-limit; make owner name off by default; acceptable-use terms (no TCPA/DNC-violating outreach); drop any jurisdiction that objects |
| T3 | TipSplit for Clover | 6 | Med | Wrong tip-pool math becomes a wage claim. State rules differ (e.g. CA Lab. Code §351 bans deducting card fees from tips, a feature the idea includes) | State-aware rule presets that block illegal settings; "owner reviews and approves" workflow; EULA with liability cap and indemnity; LLC before launch |
| W1 | Bid Brief: Facilities Services | 8 | Low | SAM.gov terms ban web scraping. Fetching attachments by page scraping can get the sponsor's login.gov account cut off; Substack is not a merchant of record (sales tax/VAT) | Use only the public Opportunities API and data extracts; link to attachments instead of rehosting them; turn on Stripe Tax or move to an MoR; "confirm on SAM.gov" line on every card |
| W2 | Florida HOA Board Letter Kit | 6 | Med | Legal-adjacent product: an outdated or wrong statute mapping can void a board's fines. That brings refund demands, reliance claims and unauthorized-practice exposure if support gives tailored advice | Forms only, with no personalised advice in Etsy messages (Florida Bar v. Brumbaugh line); prominent disclaimer; dated "current as of" edition; attorney review from early revenue; no collection or lien letters |
| W3 | Grant Deadline Desk: [State] | 9 | Low | Wrong or missed deadline causing customer loss; copying funder text verbatim | "Last verified" date and a link to the official RFP on each row; paraphrase rather than copy; accuracy disclaimer in the terms |
| A1 | "Closing Day" house portraits | 7 | Med | Etsy off-platform/fee-avoidance violation from the "Realtor? 5-packs here" link in delivery files; customers uploading photographers' MLS photos | Keep all realtor sales on Etsy (or keep off-Etsy marketing fully separate); buyer warrants photo rights; disclose AI use and Printify as production partner; label sample mockups as samples |
| A2 | Little Guests wedding activity book | 7 | Med | Handling photos of children and couples; derivative use of professional engagement and venue photos | Privacy notice, private storage, 30-day deletion, never used in marketing; buyer photo-rights warranty; no photorealistic outputs; check the image provider's rules on minors |
| A3 | "Looks Like Me" visual schedule cards | 8 | Low | Implied therapeutic claims to autism/ADHD parents; using the PECS®/Boardmaker® trademarks as keywords | No efficacy or "therapy tool" claims; avoid third-party marks in titles and tags; AI disclosure; strict QA |
| D1 | LanguageBids tender alerts | 8 | Low | Breaching portal terms (SAM.gov scraping ban; Bonfire/BidNet terms); GDPR for EU subscribers | API/open-data sources only; attribution for TED/CanadaBuys; GDPR-grade privacy policy and an MoR; fact-check market-report numbers |
| D2 | InspectionWatch OSHA alerts | 7 | Med | Defamation or false-light claims from public SEO pages naming companies with "fatality" inspections; reputational "ambulance-chasing" | Quote DOL fields verbatim with dates and source links; state that inspection ≠ violation; correction/takedown process; acceptable-use policy covering attorney-solicitation rules |
| D3 | LabelScout COLA intelligence | 8 | Low | Alcohol affiliate marketing rules (age-gate, responsible marketing, FTC disclosure); rehosting label artwork | Age-gate the consumer site; clear affiliate disclosures; link to TTB images rather than mirroring them; polite, low-rate crawling |
| S1 | Done-For-You Airbnb Guidebook | 6 | Med | Etsy rule breaches: the $29/yr refresh is a subscription Etsy bans, and selling it off-Etsy to Etsy buyers is fee avoidance. Also public web guides exposing Wi-Fi codes and addresses | Sell the refresh plan only off-Etsy to non-Etsy buyers; unguessable, noindex URLs and no door/lock codes; intake form instead of scraping Airbnb; nominative-only use of "Airbnb/VRBO" |
| S2 | Bilingual Toolbox Talks | 7 | Med | Safety-content errors that contribute to an injury; "OSHA-compliant" claims; Etsy fee avoidance from the in-PDF subscription upsell | Cite OSHA text, keep advice conservative, add a "supplements, not replaces" disclaimer, get a native-speaker review, make no OSHA endorsement claims; run the subscription funnel only through direct and Gumroad sales |
| S3 | Custom wedding toasts and eulogies | 8 | Low | Buyer deception if an AI-written speech reads as human-written; sensitive personal data about third parties in questionnaires | Prominent AI disclosure in every listing and delivery; no invented "writer" persona; data minimisation and deletion; human review of flagged eulogies |

## Cross-cutting notes

- **Etsy concentration (W2, A1–A3, S1–S3).** These would likely all run on the sponsor's one KYC'd Etsy account, so a suspension over any one of them freezes payouts for all of them. Rules checked for this review:
  - AI use must be disclosed in the listing description.
  - Since 11 Aug 2026, production partners must be disclosed.
  - Services are banned except custom writing and design delivered as files. Memberships, subscriptions and professional (legal or coaching) services are explicitly banned.
  - The off-platform policy bans encouraging buyers to purchase Etsy-shop items elsewhere, including through QR codes.
- **AI output copyright.** Pure AI output is weak or unprotectable in the US for every idea. That is a competitive issue, not a liability issue. Don't claim copyright you don't have (e.g. "© all rights reserved, no copying" on pure AI art).
- **Subscriptions.** The FTC click-to-cancel rule was vacated (8th Cir., July 2025). The FTC opened a new ANPRM in March 2026, and ROSCA still applies. California's amended ARL (July 2025) applies to consumer buyers. Use an MoR checkout with clear renewal terms, an annual-plan renewal reminder and online cancellation.
- **EU sales.** Since 19 Jun 2026 the EU "withdrawal button" (Dir. 2023/2673) applies to online B2C contracts, and the 14-day waiver must be captured for digital content. An MoR (Lemon Squeezy/Paddle) or Etsy covers most of this. Substack does not.
- **Entity.** An LLC is advisable before launch for T3, W2 and S2, and once revenue exists for the rest. Its cost may exceed the $100 cap in some states, so fund it from early revenue.

---

## T1 — RainCheck for Jobber (score 8, Low)

- **SMS client notices (TCPA, carrier 10DLC rules)** — L: Med × S: Med. Texts sent to the owner's customers on the owner's behalf need prior express consent, opt-out handling and A2P 10DLC brand/campaign registration, which is ISV-style registration per merchant. Statutory damages are $500–$1,500 per text. *Mitigation:* email-only v1. For SMS, have each owner attest that they hold consent, honour STOP, and register through Twilio's ISV flow.
- **Reliance on forecasts** — L: Low × S: Low. A crew sent out into a storm, or a lost job. *Mitigation:* terms state that forecasts are advisory from NWS/ECCC with no warranty, plus a liability cap. NWS data is public domain, so licensing is not an issue.
- **Platform terms (Jobber)** — L: Low × S: High. Jobber can delist the app or revoke API access. *Mitigation:* follow the Developer Center terms and brand guidelines, describe the app as "for Jobber" (nominative use), and never store more client PII than needed.
- **Client data** — L: Low × S: Med. The app processes customers' names and addresses. *Mitigation:* privacy policy, a data-processing clause in the EULA, and deletion on disconnect.
- **Name** — do a quick USPTO knockout search for "RainCheck" in class 9/42 before printing branding.
- **Tax** — Lemon Squeezy as MoR handles it.

## T2 — Accela & EnerGov Permit Extractor (score 5, Med)

- **Scraping and terms of use** — L: Med × S: Med. Each portal is run by a government agency, often hosted by Accela or Tyler, and many have use disclaimers. Accela's site terms grant only non-commercial use. CFAA exposure is low for unauthenticated public pages after *Van Buren*/*hiQ*. The real outcomes are cease-and-desist letters, IP bans and complaints to Apify. *Mitigation:* no logins, no CAPTCHA solving, honour robots.txt and per-portal notices, conservative rate limits, and drop a jurisdiction on any objection.
- **Platform (Apify)** — L: Med × S: High, and this is business-ending. Apify can remove an Actor on a credible complaint. *Mitigation:* a README legality section, a fast takedown response, and no personal-data marketing claims.
- **Personal data for lead gen** — L: Med × S: Med. Selling owner names and addresses so buyers can cold-call and text homeowners invites TCPA/DNC misuse. Some state privacy and data-broker laws exempt government records, but reputational risk remains. *Mitigation:* make the owner field off by default, add acceptable-use terms that forbid unlawful outreach, and avoid "homeowner leads" in marketing copy.
- **Server load and trespass to chattels** — L: Low × S: Med. *Mitigation:* HTTP-only requests, caching and off-peak scheduling.
- **Tax** — Apify bills users, so the sponsor handles only income tax.

## T3 — TipSplit for Clover (score 6, Med)

- **Wage and tip liability** — L: Med × S: High. A miscalculated pool means back pay, penalties and class claims against the merchant, who then looks to the vendor. Under the FLSA (2018 amendments), managers and supervisors may not share tips, and back-of-house may share only if no tip credit is taken. California Lab. Code §351 forbids deducting card-processing fees from tips, and SB 648 (2026) lets the Labor Commissioner cite for it, so the planned "credit-card-fee deduction toggle" is illegal in CA. MA and NY have stricter pool rules. *Mitigation:* state-aware presets that hard-block disallowed settings, show-your-work statements, explicit owner approval of each pool, a EULA with liability capped at 12 months' fees and no-warranty wording ("calculator, not payroll or legal advice"), and an LLC before launch.
- **Employee PII** — L: Low × S: Med. Names, hours and earnings. *Mitigation:* least-privilege Clover scopes, encryption, deletion on uninstall, and a privacy policy.
- **Platform (Clover App Market)** — L: Low × S: High. Clover handles billing and has approval and delisting power. *Mitigation:* follow the developer agreement and its data-use rules.
- **SEO page "is tip pooling with managers legal"** — keep it general information with citations, not advice.

## W1 — Bid Brief: Facilities Services (score 8, Low)

- **SAM.gov terms** — L: Med × S: Med. The terms say "automated data gathering, web scraping tools are prohibited," and the penalty is denial of the associated login.gov account, which is the sponsor's. *Mitigation:* use only the public Get Opportunities API and the public data extract within quota. Link to attachments rather than mirroring them. Never share the API key. Rotate keys every 90 days.
- **Accuracy** — L: Med × S: Low. A wrong deadline or set-aside causes a lost bid, but damages are speculative. *Mitigation:* a source link and "confirm on SAM.gov" on every card, plus a no-warranty clause in the subscription terms.
- **Tax** — L: Med × S: Low. Substack is not a merchant of record, so sales tax and EU/UK VAT on paid subscriptions fall on the sponsor. *Mitigation:* enable Stripe Tax and limit to US buyers, or use an MoR.
- **Outreach** — L: Low × S: Low. APEX emails are one-to-one and fine under CAN-SPAM with a sender identity and opt-out.
- **Subscriptions** — B2B buyers, so ARL exposure is minimal. Substack provides self-serve cancellation.

## W2 — Florida HOA Board Letter & Notice Kit (score 6, Med)

- **Unauthorized practice of law** — L: Low × S: Med. Selling blank forms is permitted (*Florida Bar v. Brumbaugh*; Texas Gov't Code §81.101(c) also excludes forms products with a conspicuous disclaimer). Advising a buyer which notice to send or how to apply the statute is not. *Mitigation:* Etsy and email replies stay factual and process-level, with no tailored advice. The operator's reply templates must enforce this.
- **Reliance and misrepresentation** — L: Med × S: Med. "Chapter 720-aware" implies compliance. If a template is outdated after a legislative session, a board's fine can be voided, leading to a refund demand, a bad review, or a small-claims suit. *Mitigation:*
  - Stamp each edition "current as of [date]".
  - Include statute citations.
  - Add a disclaimer that the governing documents control.
  - Get one attorney review, paid from revenue.
  - Avoid collection, lien and estoppel-substance letters.
- **Etsy** — L: Low × S: High. Templates are digital goods, not banned "legal services". Disclose AI assistance. Keep the paid "law-change update" a re-purchasable Etsy listing, not an off-Etsy subscription.
- **Deceptive marketing** — don't use "attorney-approved" until it is true.

## W3 — Grant Deadline Desk (score 9, Low)

- **Accuracy** — L: Med × S: Low. A missed deadline is costly to a nonprofit, but claims are unlikely and damages speculative. *Mitigation:* a "last verified" date and official link on every row, plus a no-warranty clause.
- **Copyright** — L: Low × S: Low. Deadlines are facts, but funder descriptions are expression. *Mitigation:* write one-line paraphrases, and don't copy RFP text.
- **Crawling** — L: Low × S: Low. Foundation pages are low-risk. Respect robots.txt and monthly cadence. 990-PF data is public.
- **Outreach** — L: Low × S: Low. Individual B2B emails to grant writers are fine under CAN-SPAM (identification, physical address, opt-out).
- **Subscriptions and tax** — Lemon Squeezy MoR. Nonprofit buyers are B2B.

## A1 — "Closing Day" house portraits (score 7, Med)

- **Etsy off-platform/fee avoidance** — L: Med × S: High. A "Realtor? 5-packs here" link to a direct prepaid page inside Etsy deliveries pushes Etsy buyers to buy Etsy-listed items elsewhere, which risks shop suspension. *Mitigation:* sell packs on Etsy only, or keep the direct channel fully separate (its own marketing, no links in Etsy orders).
- **Copyright in input photos** — L: Med × S: Low. Realtors often upload MLS photos owned by listing photographers. Painting a building itself is fine under 17 U.S.C. §120(a). *Mitigation:* a buyer warranty of photo rights in the order terms; prefer the buyer's own snapshots.
- **Etsy disclosure** — L: Low × S: High. AI disclosure and the Printify production-partner disclosure (rule since Aug 2026); use "Designed by", never "Handmade".
- **Deceptive mockups** — label samples made from CC0 stock houses as samples, and don't present them as customer reviews or results.
- **Physical goods** — Printify ornaments and frames are adult decor with no CPSIA exposure. Printify handles defects.
- **Tax** — Etsy collects marketplace sales tax and VAT.

## A2 — Little Guests wedding activity book (score 7, Med)

- **Children's and couples' images** — L: Med × S: Med. Flower-girl and birthday-child photos are sensitive. COPPA doesn't apply because adults upload them, but a leak or misuse is a real reputational and legal event, including GDPR if EU Etsy buyers upload. *Mitigation:* privacy notice at upload, private storage, auto-delete at 30 days, never used in marketing without written opt-in, and stylised line art only, never photorealistic. Confirm the image API's terms allow edits of uploaded photos of minors; some providers block or restrict these.
- **Third-party photo copyright** — L: Med × S: Low. Engagement photos are usually owned by the photographer, and venue photos are often from the venue's website. *Mitigation:* buyer rights warranty, and suggest buyers use their own snapshots.
- **Etsy** — L: Low × S: High. Personalised digital design is allowed, with AI disclosure. Keep the "Made by <shop>" footer as plain branding, not an off-Etsy link.
- **Brand** — check that wedding-trademarked phrases aren't used in titles.

## A3 — "Looks Like Me" visual schedule cards (score 8, Low)

- **Health and efficacy claims** — L: Med × S: Med. Marketing to autism/ADHD parents with "reduces meltdowns" or "therapy tool" invites FTC substantiation problems. *Mitigation:* describe features and representation only, with no outcome claims, and "not a substitute for your child's therapist/SLP".
- **Trademarks in keywords** — L: Med × S: Low. PECS® (Pyramid) and Boardmaker® (Tobii Dynavox) are registered marks, and using them as tags invites Etsy IP takedowns. *Mitigation:* use generic terms ("picture cards", "visual schedule").
- **Platform AI rules** — L: Low × S: Med. Etsy requires AI disclosure. TPT demotes low-quality AI stores, so disclose and QA strictly.
- **Privacy** — the design already avoids child photos (web-form avatar), which is good.
- **Product liability** — paper printables, negligible.

## D1 — LanguageBids tender alerts (score 8, Low)

- **Source terms** — L: Med × S: Med. SAM.gov bans scraping, so use the public API only (quota-limited) and keep the sponsor's key private. Bonfire, BidNet, DemandStar and OpenGov forbid scraping; the idea already excludes them, so keep it that way. TED and CanadaBuys permit reuse with attribution (EU reuse decision, OGL-Canada).
- **GDPR** — L: Med × S: Low. EU subscribers and EU press pitches. *Mitigation:* privacy policy, lawful basis (contract and legitimate interest), an MoR for VAT, unsubscribe in every email, and an EU Art. 27 representative only if processing becomes regular and large-scale.
- **Market-report claims** — L: Low × S: Low. Contract-value and ROI figures must come from award data (FTC substantiation).
- **Accuracy** — standard no-warranty terms.

## D2 — InspectionWatch OSHA alerts (score 7, Med)

- **Defamation and false light** — L: Low–Med × S: Med. Public state pages naming establishments under "fatality/accident inspection" can be misread as fault, and inspections aren't violations. *Mitigation:* reproduce DOL fields verbatim with dates and source links, label citations "initial, may be contested", add a correction/takedown form, and drop names from public pages (put names only in the paid feed).
- **Solicitation rules** — L: Med × S: Low (to the sponsor). Attorney subscribers face Rule 7.3 limits on direct solicitation. *Mitigation:* an acceptable-use clause, and market to consultants first.
- **Privacy** — L: Low × S: Low. Establishment data, though some sole proprietorships carry personal names. Government records are exempt under most state privacy laws.
- **CAN-SPAM** — editor pitches are fine. LinkedIn posts by the sponsor must be disclosed founder posts within group rules.

## D3 — LabelScout COLA intelligence (score 8, Low)

- **Alcohol affiliate marketing** — L: Med × S: Med. Spirits affiliate programs require an age-gate and responsible-marketing terms, and some states restrict shipping. *Mitigation:* 21+ age-gate, FTC affiliate disclosures, no content aimed at minors, and check each program's terms.
- **Label artwork and trademarks** — L: Low × S: Med. Label images are copyrighted and trademarked. *Mitigation:* link to TTB images rather than mirroring them, use brand names only nominatively, and add no "endorsed by" implication.
- **Source access** — L: Low × S: Med. The COLA registry has no login, but it is a federal system. *Mitigation:* polite date-range crawling at low rate. The FOIA permittee lists are published for download.
- **Lead-quality claims** — avoid overstating ("every new brand").
- **Tax** — MoR checkout.

## S1 — Done-For-You Airbnb Guidebook (score 6, Med)

- **Etsy rules** — L: Med × S: High. Custom writing and design delivered as files is allowed. The "$29/yr Keep it fresh" plan is a subscription, which Etsy bans, and pitching it to Etsy buyers for off-Etsy purchase is fee avoidance. A hosted web guide (not a file) stretches "digital item". *Mitigation:* the Etsy deliverable is the PDF and QR files. Present the web guide as a free bonus. Offer refresh plans only through the direct site and SEO channel.
- **Security and privacy** — L: Med × S: Med. Public pages that pair a property address with Wi-Fi passwords and check-in steps invite burglary, squatting and liability claims. *Mitigation:* random unguessable slugs, noindex, an optional password, and never publish door or lock codes.
- **Trademarks** — L: Med × S: Low. "Airbnb"/"VRBO" in titles is nominative but draws IP reports. *Mitigation:* "for Airbnb hosts", no logos or brand colours.
- **Airbnb terms** — fetching the listing URL by bot breaches Airbnb's anti-scraping terms. Use host-supplied intake data instead.
- **Map data** — don't cache Google Places data against its terms. Use web verification or OSM.
- **Accuracy** — wrong urgent-care information is a safety issue. Show a "last verified" date.

## S2 — Bilingual Toolbox Talks (score 7, Med)

- **Safety-content liability** — L: Low × S: High. US courts generally don't hold publishers liable for informational errors (*Winter v. G.P. Putnam's Sons*), but an injury suit naming the sponsor is the worst case. *Mitigation:* conservative content tied to cited OSHA/eCFR text, a "supplements, does not replace a site-specific safety program or competent person" disclaimer, native-speaker review of the Spanish, an LLC, and a liability cap in the terms.
- **OSHA name and claims** — L: Med × S: Low. Don't claim "OSHA-approved" or "OSHA-compliant", and don't use the OSHA logo (implied endorsement is deceptive).
- **Etsy** — L: Med × S: High. The "4 free weeks" subscription offer inside Etsy PDFs funnels Etsy buyers off-platform. *Mitigation:* put the subscription offer only in Gumroad and direct-sold files. Etsy files may reference only the free sample library.
- **Copyright** — write original talks and don't adapt the NRCA/CPWR texts.
- **Subscriptions** — MoR with online cancellation (ARL/ROSCA). CAN-SPAM for the Sunday emails.

## S3 — Custom wedding toasts & eulogies (score 8, Low)

- **AI disclosure and deception** — L: Med × S: Low. Etsy requires AI disclosure, and a buyer who believed a human wrote the speech can claim misrepresentation and demand a refund. *Mitigation:* say "written with AI assistance" in the title area, description and delivery. Create no fictional "writer" persona and post no fake reviews.
- **Sensitive personal data** — L: Low × S: Med. Questionnaires collect third parties' stories, health and death details, and family conflicts. *Mitigation:* data minimisation, auto-delete after the event date plus 30 days, and a privacy notice (GDPR for EU buyers).
- **Etsy service fit** — L: Low × S: Med. Custom writing delivered as files is explicitly allowed, so keep the "digital file" framing.
- **Content harms** — L: Low × S: Low. Speeches mocking named people can embarrass the buyer, but the buyer delivers the speech, so defamation exposure to the sponsor is remote. Keep the "topics to avoid" check and human glance for flagged eulogies.

---

### Sources checked (2026-10-06)
- Etsy services policy: https://www.etsy.com/legal/policy/services/242665313101
- Etsy off-platform transactions policy: https://www.etsy.com/legal/policy/off-platform-transactions/1254654515806
- Etsy 2026 AI and production-partner disclosure: https://beancount.io/blog/2026/07/09/etsy-2026-fee-hike-ai-disclosure-rules-handmade-sellers-guide , https://www.listadum.com/blog/etsy-creativity-standards
- FTC click-to-cancel status (vacated July 2025; ANPRM March 2026): https://www.bclplaw.com/en-US/events-insights-news/im-not-dead-yet-is-the-demise-of-the-ftcs-click-to-cancel-exaggerated.html
- EU withdrawal button (Dir. 2023/2673, from 19 Jun 2026): https://www.gtlaw.com/en/insights/2026/5/eu-consumer-law-new-withdrawal-button-requirements-for-online-contracts
- SAM.gov terms of use (scraping ban, API keys): https://sam.gov/about/terms-of-use
- CA Labor Code §351 and SB 648: https://dir.ca.gov/dlse/faq_tipsandgratuities.htm , https://beancount.io/blog/2026/07/13/california-sb-648-tip-skimming-credit-card-guide
- Substack is not a merchant of record: https://newsletter.alexhyett.com/p/eu-vat-substack-patreon
- Florida Bar v. Brumbaugh, 355 So. 2d 1186 (Fla. 1978): https://quimbee.com/cases/florida-bar-v-brumbaugh
- TTB Public COLA Registry: https://www.ttb.gov/regulated-commodities/labeling/cola-public-registry
- Jobber Developer Center: https://developer.getjobber.com/docs/getting_started
- Not verified: Accela Citizen Access per-portal terms (vary by jurisdiction; Accela's own site terms are non-commercial), Clover developer agreement text, and current image-provider rules on edits of minors' photos.
