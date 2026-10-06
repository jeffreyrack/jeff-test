# Legal Risk Screen: Round 2 (2026-10-06)

> **This is not legal advice.** It is a risk screen by an AI analyst. The human sponsor carries all legal risk and should use a licensed attorney for anything scored 6 or below before launch.

**Scope:** 13 ideas (G1–G3, C1–C3, I1–I3, M1–M3, U4).
**Scale:** Legal safety runs 1–10, where 10 means ordinary e-commerce risk. A score of 3 or below is a hard reject.
**Notation:** L×S means likelihood × severity. Each is rated L (low), M (medium) or H (high).

## Summary

| ID | Idea | Legal safety score | Overall risk (Low/Med/High) | Top risk | Key mitigation |
|---|---|---|---|---|---|
| G1 | Keyword→Brief Apify Actor (DataForSEO) | 6 | Med | DataForSEO ToS neither allows nor bans resale. §7.2 makes us indemnify DataForSEO, and §6.1 lets it suspend us at will. | Get written resale confirmation before building. Keep a BYO-key fallback. Return only metrics and outlines, never page text. |
| G2 | LongForm Transcripts Apify Actor | 6 | Med | Users submit recordings of third parties: copyright, GDPR processor duties and wiretap/BIPA. The claim "audio deleted when run ends" is untrue, because the speech-to-text providers keep data. | No live-meeting bots and no speaker ID or diarization. Fix the retention claim. Add an AUP and a DMCA agent. Get DPAs from the speech-to-text providers. |
| G3 | AnswerShare AI-visibility API | **4** | **High** | Gemini API terms ban caching, reselling or analysing Grounded Results, which is exactly what this product does. Perplexity's Output licence is non-sublicensable. | Drop Gemini grounding. Get Perplexity's written OK, or drop it too. Keep "ChatGPT" out of names. Check tax handling, because MCPize is not a merchant of record. |
| C1 | FunderFit 990-PF prospect reports | 8 | Low | Using the ProPublica API in a paid product breaches its CC BY-NC-ND licence. Grant lines name individual grantees. | Use only IRS bulk XML. Drop grants to individuals. Require FTC affiliate disclosure from partners. |
| C2 | Client Safety Kit (white-label bilingual toolbox talks) | 5 | Med | A wrong talk or a bad Spanish translation contributes to an injury, and the sponsor is the author. | Use the LLC. The licence makes the consultant adopt and review the content. Never claim "OSHA-compliant" or "training". Get native review of each talk before it enters the library. |
| C3 | Interpreter Practice Lab | 7 | Low | Cease-and-desist over CCHI/NBCMI marks or exam content. Unsupported "helps you pass" claims. | Original items only, and never ask candidates to recall exam content. Nominative use of marks plus a disclaimer. No score-prediction claims. No speaker ID on recordings. |
| I1 | Zì Bot for Discord | 6 | Med | Discord's payment-parity rule: selling through Lemon Squeezy before Premium Apps is enabled can get the app delisted. Users can be 13–17. | Get written confirmation from Discord developer support, or run pre-orders off-Discord as a web product. Make the paid tier 18+. Meet CC-CEDICT CC BY-SA attribution and share-alike. |
| I2 | Episode Study Packs for Chinese-learning creators | 8 | Low | Cold B2B email to EU/German creators, and building packs from content the requester does not own. | Process only creator-owned content. Skip German and other EU consent-required recipients. Samples only from CC licences without the ND (NoDerivatives) term. |
| I3 | Role-Play Room for college Chinese classes | 6 | Med | FERPA and institutional-procurement exposure when instructors adopt the tool without a contract. "18+ only" fails for dual-enrolment minors. | Design with no personal data. Publish FERPA "school official" terms. Purge at semester end. Don't claim 18+. Treat accessibility (an ACR) as part of the product. |
| M1 | ChatRelay for Jira (Google Chat) | 8 | Low | Signing the Marketplace Partner Agreement (security SLAs, privacy duties). A false "data stays in Atlassian / Runs on Atlassian" claim. | Claim the badge only if Atlassian confirms. Accurate privacy policy. Nominative "for Google Chat" only, with no Google logos. |
| M2 | SpecView for Confluence (Swagger/OpenAPI + migration) | 7 | Low | A converter that rewrites customer pages and loses data. Naming competitors in the listing. | Dry-run first, per-page rollback, page-count gate, EULA liability cap. Factual competitor references only. "Swagger" used descriptively. |
| M3 | SheetSync Apify Actor (Sheets export) | 6 | Med | The shared service account is a confused deputy: any user can overwrite any other customer's shared sheet. | Require proof of ownership per sheet (a token in the sheet or BYO credentials) before any write. Factual comparative claims only. |
| U4 | AI-matched job board (user idea) | **4** | **High** | Resumes are sensitive personal data. Copyright and ToS limits on job content. The later employer-side ranking falls under NYC LL144, Colorado's AI law and EU AI Act high-risk rules. | v1 is US-only and seeker-only: snippets that link out, and nothing that ranks candidates for employers. Minimal resume retention. LLC. Get counsel before any employer product. |

## Cross-cutting notes (these apply to many ideas, so they are not repeated below)

- **Entity.**
  - An LLC is advisable before launching C2, G2, U4 or I3, because those carry tort or personal-data exposure. It is cheap insurance for the rest.
  - LLC filing fees vary by state. Some exceed the $100 cap (California charges an $800/yr franchise tax). Pick a low-fee state of residence, or accept sole-proprietor risk for the low-risk ideas only.
- **Apify ideas (G1, G2, M3).**
  - Under the Store Publishing Terms, **the contract for an Actor is between the developer and the user**. The sponsor, not Apify, is the provider.
  - Apify can unpublish without notice, withhold all outstanding payouts, and impose a "contractual penalty up to the total amount of your outstanding unpaid balance".
  - Apify bans promoting off-platform products, and bans soliciting or incentivising reviews.
  - Platform risk is business-ending for each Apify idea. Concentration on one account multiplies it.
- **Subscriptions (C1–C3, I1–I3, U4).**
  - The FTC click-to-cancel rule was vacated (8th Cir., July 2025), but ROSCA and state auto-renewal laws still apply. California's ARL (as amended July 2025) requires clear terms, affirmative consent, online cancellation and renewal reminders.
  - A merchant of record (Lemon Squeezy, or Stripe Managed Payments) handles VAT and sales tax and EU withdrawal-right mechanics. You must still set the "waive withdrawal on immediate delivery" consent checkbox.
- **Affiliate and partner programmes (C1–C3).**
  - Partners must disclose the 40% material connection (FTC Endorsement Guides). Put the disclosure line in every partner kit.
  - If you fall back to paying partners by PayPal, issue 1099s above the IRS threshold.
- **1:1 B2B outreach (C1–C3, I2, I3).**
  - CAN-SPAM applies in the US. Include the physical address, opt-out and honest subject lines.
  - The UK (PECR) allows email to corporate subscribers with an opt-out.
  - Canada (CASL) allows it only where the address is conspicuously published and the message relates to the recipient's role.
  - Germany and some other EU states effectively require consent even for B2B email. Skip them.
- **AI output copyright.** Generated reports, talks, dialogues and packs have weak or no US copyright. Competitors can copy them. That is a moat problem, not a liability.

---

## G1 — Keyword→Brief (Apify Actor, DataForSEO)
**Score 6 · Med**

- **Supplier resale terms** (L×S: M×H).
  - DataForSEO's ToS is silent on redistribution. §7.1 bars using SERP data "to compete with or adversely affect" search engines. §7.2 makes us indemnify DataForSEO for any §7.1 breach. §6.1 lets it "refuse, cancel or suspend service, at our sole discretion".
  - Several public Apify Actors already resell DataForSEO, so tolerance is likely, but tolerance is not a licence.
  - **Mitigation:** get written email confirmation before building, as the ideator proposes, and keep it on file. Keep the BYO-key mode ready.
- **Google-side SERP legality** (L×S: L×M).
  - Google's DMCA §1201 suit against SerpApi was dismissed on 20 Jul 2026. The judge held that SERP facts are not protected works, with leave to amend for Knowledge Panels only.
  - The remaining risk is a supply disruption at DataForSEO, not direct liability for us.
  - **Mitigation:** don't return Knowledge Panel media, and keep a second supplier identified.
- **Page fetching and copyright** (L×S: L×M).
  - H2/H3 outlines, word counts and entity lists are facts and short phrases.
  - Returning full page text or AI Overview text verbatim at scale invites claims.
  - **Mitigation:** honour robots.txt, use a truthful user-agent, and truncate any AI Overview text to a short excerpt plus the URL.
- **Comparative claims** (L×S: M×L). "Competitors fail 25%" must be dated and sourced from Apify's public stats. Unsupported claims can draw a Lanham Act or Apify complaint.
- **Tax.** Apify bills users. Payouts are ordinary income to the sponsor.

## G2 — LongForm Transcripts (Apify Actor)
**Score 6 · Med**

- **Copyright in submitted audio** (L×S: M×M).
  - A transcript is a reproduction or derivative of the recording.
  - The tool has substantial non-infringing uses (own content, CC content, research), which makes contributory liability unlikely, but rights holders may send notices.
  - **Mitigation:**
    - an AUP;
    - register a DMCA agent ($6) and publish a repeat-infringer and blocklist policy;
    - keep platform downloaders (YouTube, TikTok, IG) excluded.
- **Third-party voices: wiretap and biometrics** (L×S: L×H).
  - In re Otter.AI, ECPA, CIPA and Illinois BIPA claims survived dismissal on 13 Aug 2026. Those claims attach to *live* capture of calls and to speaker identification.
  - **Mitigation:**
    - never offer a meeting-bot or live-capture mode;
    - never add diarization or speaker identification based on voiceprints;
    - the AUP makes the user warrant that they hold the necessary recording consents.
- **GDPR processor role** (L×S: M×M).
  - EU users will upload meetings. The sponsor becomes a processor, with Groq and OpenAI as subprocessors in the US.
  - **Mitigation:** Article 28 terms in the Actor's end-user terms, the providers' DPAs, and a subprocessor list.
- **Deceptive privacy claim** (L×S: M×M).
  - "Audio is deleted when the run ends; nothing is kept" is false if Groq or OpenAI keep inputs for abuse monitoring, typically up to 30 days unless zero-retention is approved.
  - **Mitigation:** state the providers' actual retention, or obtain zero-data-retention.
- **Commercial-use rights:** Groq and OpenAI API outputs belong to the customer. OK.

## G3 — AnswerShare AI-visibility API
**Score 4 · High**

- **Gemini grounding terms** (L×S: H×M).
  - The Gemini API terms say you "will not… cache, frame, syndicate, resell, analyze, train on, or otherwise learn from Grounded Results or Search Suggestions".
  - They also require Search Suggestions to be shown "to the end user who submitted the prompt", and they bar using links to build an index.
  - The product's core (stored mention, rank and citation analysis, resold through an API, with 12-month history) breaches this directly. Expect termination of the Google AI account.
  - **Mitigation:** remove the Gemini engine, or get a written licence from Google.
- **Perplexity API licence** (L×S: M×M).
  - Output may be used "solely within the Customer Applications" on a non-sublicensable basis.
  - Passing raw Sonar outputs to other businesses through an API, and storing them as a dataset, sits in a grey zone.
  - **Mitigation:** get written confirmation, or return only derived metrics (mentioned yes/no, position, cited domains), not answer text.
- **OpenAI.** The terms allow output use, but the brand rules ban "GPT" and "ChatGPT" in product, app or company names.
  - Label results "OpenAI API with web search", as planned.
  - Never imply that the results reflect the consumer ChatGPT app (FTC §5 deception risk with agency buyers).
- **No consumer-UI scraping** (L×S: L×H). Programmatic querying of chatgpt.com, perplexity.ai or Gemini web would breach all three ToS. The plan uses APIs only. Keep it that way.
- **Tax** (L×S: M×L).
  - MCPize pays out through Stripe Connect and is probably not the merchant of record, so sales tax and VAT on those sales may fall on the sponsor.
  - Confirm how RapidAPI handles tax.
- **Fixed version:** without Gemini, and with Perplexity confirmed, the score rises to about 6.

## C1 — FunderFit (990-PF prospect reports)
**Score 8 · Low**

- **Data licensing** (L×S: L×L for IRS data; M×M for ProPublica).
  - IRS 990-series XML is public under IRC §6104. The facts are not copyrightable and there is no use restriction.
  - **ProPublica's Nonprofit Explorer API is CC BY-NC-ND, and its terms say "you can't charge people money to look at the data".** Do not use it in the paid pipeline, not even for lookups, without a commercial licence.
  - Don't use Candid or GuideStar data.
- **Personal data** (L×S: L×M).
  - Part XV lists grants to individuals (scholarships, hardship aid).
  - Exclude individual grantees, and officer compensation, from reports. They add no value and create privacy and reputational risk.
- **Accuracy and reliance** (L×S: M×L).
  - Stale or wrong funder data could damage a freelancer's client relationship.
  - **Mitigation:** show the filing year on every line, cap liability at the fee in the terms, and state that this is "research, not a guarantee of eligibility or funding".
- **White-label resale.** This is B2B. The freelancer's representations to their client are their own responsibility. Say so in the licence.
- **Affiliates:** see the cross-cutting notes (FTC disclosure, 1099s).
- **Not regulated advice.** Prospect research is not legal or tax advice. Avoid statements about a nonprofit's tax status or eligibility.

## C2 — Client Safety Kit
**Score 5 · Med**

- **Personal-injury and negligence exposure** (L×S: L×H).
  - Courts rarely hold publishers of general information liable (the *Winter v. G.P. Putnam's* line). These kits are different: paid, client-specific, trade-targeted instructions sold as a professional deliverable, which brings negligent-misrepresentation theories closer.
  - The highest-risk vector is a **Spanish mistranslation** of a control measure (lockout, fall protection, trenching). An AI second pass is not native QA.
  - **Mitigation:**
    - LLC;
    - a licence clause making the consultant the professional who reviews, adopts and delivers the content, with a liability cap and a disclaimer of fitness for any specific site;
    - a native-speaker review of every library talk before release, not just a monthly spot check;
    - the high-hazard trades (trenching, confined space, electrical) stay out until reviewed.
- **Regulatory misrepresentation** (L×S: M×M).
  - Toolbox talks do not satisfy specific OSHA training standards (e.g. 1926.503 fall-protection training).
  - Never market them as "OSHA-compliant", "certified" or "training". Never use the OSHA or DOL logo, and never imply endorsement.
- **Copyright** (L×S: L×M). 29 CFR text and DOL data are public domain. CPWR, NRCA and ANSI materials are not: don't paraphrase them closely.
- **Defamation** (L×S: L×M). The briefs aggregate data by NAICS and state. If an employer is ever named, say "citation issued; may be contested or unresolved".

## C3 — Interpreter Practice Lab
**Score 7 · Low**

- **Trademarks** (L×S: M×L).
  - CCHI, CoreCHI™, CHI™, NBCMI, CMI, *The Community Interpreter®* and LanguageLine are marks.
  - Use them only nominatively ("practice in the format of…"), with a non-affiliation disclaimer, and with no logos.
  - The co-branded publisher deal needs a written trademark licence from the partner for its logo.
- **Exam content** (L×S: L×H).
  - Candidates sign confidentiality undertakings, and recalled items are protected trade secrets or copyright.
  - **Never** solicit, accept or crowdsource "what was on my exam". Add a reporting and takedown path.
  - Build dialogues around textbook *topics* only, as planned. Never copy textbook dialogue text or structure.
- **Advertising claims** (L×S: M×M).
  - "Raises your pass rate" or "predicts your score" needs substantiation under FTC §5.
  - Opt-in testimonials need FTC-compliant disclosures, and must not be cherry-picked as typical.
- **Voice recordings** (L×S: L×M).
  - These are adults recording their own voices. Under BIPA, transcription without speaker identification is not a voiceprint. Do not add voice-matching features.
  - Keep the 7-day deletion, a plain privacy notice and recording consent at first use.
  - Bar partners from uploading real patient audio (HIPAA).
- **Content safety.** The dialogues are fictional medical scenarios, not medical advice. Add a footer saying so.

## I1 — Zì Bot (Discord)
**Score 6 · Med**

- **Discord payment parity** (L×S: M×H).
  - Since 7 Oct 2024, developers in supported regions (US, EU, UK) who sell paid features "are required to support purchase… through Discord's Premium Apps" at no higher price.
  - Premium Apps needs a verified app, which needs about 75–100 servers. Selling Supporter through Lemon Squeezy before then is a parity breach on the business's only channel. Ban or delisting is business-ending.
  - **Mitigation:**
    - get written guidance from Discord developer support;
    - or sell the founding pre-order as a *web* product (a practice web app) that is not unlocked inside the bot until Premium Apps SKUs exist;
    - or take refundable waitlist deposits only.
- **Minors** (L×S: M×M).
  - Discord allows users from age 13. An AI conversation partner for teens draws scrutiny.
  - The ToS sets the paid tier at 18+ (the merchant of record collects the payer). The free tier gets no LLM.
  - Keep `/practice` task-bound, with no persona or relationship features, to stay outside "companion chatbot" laws such as California SB 243. Disclose that it is AI.
- **Discord data rules** (L×S: L×M). Store only user IDs and SRS state. Process message content only on user-invoked commands. No training on API Data. Publish a privacy policy; monetisation requires one.
- **Licensing** (L×S: M×L).
  - CC-CEDICT is CC BY-SA 4.0: give attribution, and **share-alike applies to derived dictionary data** such as the HSK-tagged table. Publish that derived table under CC BY-SA.
  - Use "HSK" descriptively.
  - Don't market the bot publicly as "Kotoba for Mandarin".
- **Promotion.** Only the sponsor may post, disclosed, within each server's and subreddit's rules (lessons-learned §5).

## I2 — Episode Study Packs
**Score 8 · Low**

- **Content rights** (L×S: L×M).
  - Packs are translations and derivatives of the creator's work. Process only content the requester owns or controls.
  - The ToS has the creator warrant ownership and grant a processing-only licence, and assigns to the creator whatever rights exist in the output.
  - Never build an unsolicited pack from a creator's episode. A "free pack for episode X" only happens after a yes.
- **Sample library** (L×S: L×M). Use only CC BY or CC BY-SA audio, plus the sponsor's own recordings. **ND-licensed works cannot be translated.** NC licences are acceptable for samples shown free, but avoid them for anything sold.
- **Outreach email** (L×S: M×L).
  - Sending 40–120 one-to-one emails to public business addresses is lawful under CAN-SPAM, PECR and CASL (published-address exemption), with an opt-out and the sponsor's identity.
  - Skip recipients in Germany and Austria.
  - Creators in mainland China: keep to business-contact use only (PIPL).
- **Quality and brand harm** (L×S: M×L). Errors published under the creator's brand are contractual, not tort. Cap liability at fees, and require creator review before publishing (already in the design).
- **Third-party formats.** Anki .apkg and Pleco import files are formats, not licences. OK.

## I3 — Role-Play Room
**Score 6 · Med**

- **FERPA** (L×S: M×M).
  - Class-linked transcripts and completion stats kept for an instructor are education records.
  - The *institution* is liable, and a vendor that misuses records can be barred from access. When an instructor adopts the tool alone, there is no "school official" agreement, so procurement or the registrar can shut the tool down mid-semester.
  - **Mitigation:**
    - publish standard FERPA terms (school-official designation, use only for the class, no redisclosure, no training, deletion);
    - collect no names or emails;
    - offer a pre-signed standard DPA rather than negotiating each one.
- **Minors** (L×S: M×M).
  - Community colleges enrol dual-enrolment high-school students, so a blanket "18+ only" is likely false.
  - Drop the claim. Rely on the no-personal-data design, and treat students' free text as potentially containing personal data (purge each semester).
  - State K-12 student-privacy laws (SOPIPA-type) apply if any high school adopts it. Exclude K-12 in the terms.
- **Accessibility** (L×S: M×M). The DOJ Title II WCAG 2.1 AA deadline for large public entities moved to **26 Apr 2027**. Public colleges will ask for an ACR or VPAT. Build to WCAG 2.1 AA.
- **Student-pays model** (L×S: L×M). Some institutions restrict required paid materials, and students are consumers (refund rights). The per-class licence is cleaner.
- **Outreach.** Faculty addresses are published, so the cross-cutting rules apply. US and Canadian faculty are fine under CASL's published-address exemption.

## M1 — ChatRelay for Jira
**Score 8 · Low**

- **Partner agreement** (L×S: L×M).
  - The sponsor signs the Atlassian Marketplace Partner Agreement and takes on the security requirements for cloud apps (vulnerability fix SLAs), the privacy-policy and data-handling duties, and indemnities.
  - Atlassian can delist the app. That is platform risk shared with M2.
- **Personal data** (L×S: L×M).
  - Matching Atlassian and Google emails for @mentions processes personal data, and messages egress to Google.
  - The privacy policy must say so. Offer a mentions-off mode.
  - Webhook URLs are bearer secrets: store them encrypted, as planned, and never log them.
- **Accuracy of trust claims** (L×S: M×M). "No customer data leaves Atlassian except the message sent to Google" is accurate only as phrased. Claim "Runs on Atlassian" only if Atlassian confirms eligibility with the declared Google egress. A wrong badge claim is a deceptive-marketing issue and a listing violation.
- **Trademarks** (L×S: L×L).
  - "ChatRelay for Jira" follows Atlassian's "Acme for Jira®" rule.
  - Use "Google Chat" nominatively, with no Google logos. "Replacement for Google Chat for Jira Cloud" is acceptable as a factual reference without implying Google affiliation.
  - SEO pages quoting the old app's error strings are fine.
- **Reliability** (L×S: M×L). Missed notifications are not a tort. Use a EULA (or Atlassian's standard) with a warranty disclaimer and liability cap.
- **Tax:** Atlassian is the seller of record.

## M2 — SpecView for Confluence
**Score 7 · Low**

- **The converter rewrites customer pages** (L×S: M×M).
  - Silent data loss across hundreds of API docs is the realistic claim, mostly contractual and reputational.
  - **Mitigation:**
    - dry-run report first;
    - per-page version snapshot and one-click rollback;
    - the >500-page gate (as planned);
    - explicit admin confirmation;
    - a EULA cap of 12 months' fees.
- **Competitor references** (L×S: M×L).
  - Naming orphaned apps ("replacement for Open API (Swagger) Integration") is nominative. Keep it factual ("last release 2024-09-19") rather than "abandoned" or "dead".
  - Atlassian bars unsubstantiated claims.
- **Trademarks** (L×S: L×M). "Swagger" is a SmartBear mark and "OpenAPI" belongs to the Linux Foundation. Use both descriptively only, never in the app name. "SpecView" is fine; run a quick USPTO search first.
- **Open-source licences** (L×S: L×L). Bundled Swagger UI (Apache-2.0) and Redoc (MIT) need their notices in the app and listing.
- **Capturing orphan storage formats.** Reading macro XHTML from your own dev site is not reverse-engineering their code. Don't decompile their bundles, and check each evaluation EULA.
- **Partner agreement:** same as M1 (shared account).

## M3 — SheetSync (Apify Actor)
**Score 6 · Med (8 once the auth design is fixed)**

- **Confused-deputy security flaw** (L×S: M×H).
  - With one shared service account, every customer's sheet is shared with the same identity. Any Apify user who enters another customer's sheet URL can append to it or *replace* it.
  - That is a data-integrity incident for which the sponsor, as Actor provider, is liable. Apify could also pull the Actor.
  - **Mitigation:**
    - require per-sheet proof of ownership before writing, for example a one-time token the user places in a named range, bound to their Apify user ID;
    - or default to BYO service-account credentials;
    - never offer "replace" mode on the shared identity without that proof.
- **Personal data in transit** (L×S: M×M). Scraped datasets (Maps, Instagram) contain personal data, so the sponsor is a processor. Write nothing to logs, publish a data-handling note, and include GDPR processor terms in the Actor's end-user terms.
- **Google APIs terms** (L×S: L×M). They ban creating a client that "functions substantially the same as the APIs" and offering it to third parties. SheetSync adds real transformation (dataset mapping, de-duplication, rollover), so the risk is low. Respect quotas. Don't spread load across multiple projects to evade limits.
- **Comparative claims** (L×S: M×L). The incumbent is maintained by Apify staff. Cite "51% failed runs, Apify stats, 2026-10-06" factually, and drop the disparaging framing.
- **Platform:** Apify concentration (see the cross-cutting notes).

## U4 — AI-matched job board (user idea)
**Score 4 · High** as proposed. About 6 for a US-only, seeker-only v1 that links out.

- **Job-data sourcing** (L×S: M×M).
  - Greenhouse and Lever public board APIs are unauthenticated and widely aggregated. The job descriptions remain the employers' copyright.
  - Show title, company, location, a short snippet, and a link to apply. Don't republish full descriptions.
  - Avoid LinkedIn, Indeed and any careers page whose ToS bans automated access (hiQ: CFAA defence, but contract claims succeeded).
  - Follow Google JobPosting structured-data policies and expire jobs promptly. Violations bring manual actions.
- **Resume data** (L×S: M×H).
  - Resumes contain contact details, work history and data that reveals age, ethnicity or disability. A breach triggers state breach-notification laws in every US state, whatever the CCPA thresholds.
  - **Mitigation:** extract the skills profile, then delete the PDF; encrypt the profile; offer deletion on request; no training. For EU users, GDPR applies in full. Geo-limit v1 to the US.
- **Automated employment decisions** (L×S: M×H in phase 2).
  - EU AI Act Annex III 4(a) covers AI to "place targeted job advertisements" and to "analyse and filter applications". Its obligations now start **2 Dec 2027** (Omnibus, Reg. 2026/1744).
  - NYC LL144 bias audits apply when employers or *employment agencies* use AEDTs on NYC candidates.
  - Colorado SB 26-189 takes effect 1 Jan 2027.
  - Selling ranked candidates to employers also raises FCRA "consumer report" and Title VII "employment agency" disparate-impact risk.
  - **Mitigation:** seeker-side recommendations only. Never rank candidates for employers without counsel and a bias audit. Never use protected or proxy traits (graduation year, name, photo).
- **Consumer claims** (L×S: M×M). "Exact matches" and "only jobs you're qualified for" are AI-capability claims the FTC targets. Use softer, substantiated wording. A paid seeker tier must follow auto-renewal law.

---

### Sources checked (2026-10-06)
- [DataForSEO Terms of Service](https://dataforseo.com/terms-of-service)
- Google v. SerpApi dismissal (20 Jul 2026): [Search Engine Roundtable](https://seroundtable.com/google-lawsuit-serpapi-dismissed-41731.html), [PPC Land](https://ppc.land/google-loses-dmca-bid-to-treat-search-scraping-like-dvd-piracy/)
- [Gemini API Additional Terms of Service (Grounding with Google Search)](https://ai.google.dev/gemini-api/terms)
- [Perplexity API Terms of Service](https://hub-prod.perplexity.ai/hub/legal/perplexity-api-terms-of-service) (via search summary; direct fetch blocked)
- [OpenAI brand guidelines](https://openai.com/brand/)
- [Apify Store Publishing Terms](https://docs.apify.com/legal/store-publishing-terms-and-conditions), [Standard Actor Contract](https://docs.apify.com/legal/standard-actor-contract)
- In re Otter.AI Privacy Litigation: [NPR](https://www.npr.org/2026/08/15/g-s1-83087/otter-ai-transcription-class-action-lawsuit), [UC Today on the motion-to-dismiss ruling](https://www.uctoday.com/?p=748128)
- [ProPublica Nonprofit Explorer API terms](https://www.propublica.org/datastore/api/nonprofit-explorer-api); [IRS Form 990 series downloads](https://www.irs.gov/node/70096)
- [DOL Open Data Portal / OSHA enforcement data](https://enforcedata.dol.gov/)
- Discord: [Developer Policy](https://support-dev.discord.com/hc/en-us/articles/8563934450327), [Premium Apps required support](https://support-dev.discord.com/hc/en-us/articles/23810643331735), [Enabling monetization](https://docs.discord.com/developers/monetization/enabling-monetization)
- [CC-CEDICT licence (CC BY-SA 4.0)](https://en.wikipedia.org/wiki/CEDICT)
- [FERPA school-official exception discussion (AACRAO)](https://www.aacrao.org/resources/newsletters-blogs/aacrao-connect/article/ask-the-ferpa-professors--webinar-edition-1-20-26)
- [DOJ Title II accessibility deadline extension](https://campustechnology.com/articles/2026/04/27/doj-extends-deadline-for-ada-title-ii-compliance.aspx)
- [Atlassian brand guidelines for Marketplace partners](https://developer.atlassian.com/platform/marketplace/atlassian-brand-guidelines-for-marketplace-partners/)
- [Google APIs Terms of Service](https://developers.google.com/terms)
- [Greenhouse public job board aggregation notes](https://jobspipe.dev/sources/greenhouse.md); [Lever postings API](https://100hires.com/lever-api.html)
- EU AI Act Omnibus delay: [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/), [Mondaq](https://www.mondaq.com/eu-digital-omnibus-on-ai-enters-into-force/1825722)
- [NYC LL144 2026 enforcement (DLA Piper)](https://www.dlapiper.com/insights/publications/2026/01/critical-audit-of-nyc-ai-hiring-law-signals-increased-risk-for-employers)
- [Colorado SB 26-189 (McDermott)](https://www.mcdermottlaw.com/insights/colorado-ai-law-in-flux-comprehensive-replacement-bill-signed-after-federal-court-blocks-predecessors-enforcement/)
- [FTC click-to-cancel vacatur (Latham)](https://www.lw.com/en/insights/eighth-circuit-vacates-ftc-click-to-cancel-rule)
