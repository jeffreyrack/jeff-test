# Autonomy Audit — 2026-10-06

_Reviewer: autonomy-auditor. Scale: 10 = < 2 h one-time human setup and ~0 h/week ongoing; 1 = a human is needed daily or for every sale. Hours are my estimates of real sponsor time, including tasks the ideators left out. The rubric's hard gate is > 3 h/week of recurring human time; no idea breaks it on paper, but A1 and S3 get close at volume._

| ID | Idea | Score | Human setup hrs (one-time) | Human hrs/week ongoing | Hard gates | Scales without humans? |
|---|---|---|---|---|---|---|
| T1 | RainCheck for Jobber | 8 | 3.5–4 | 0.25–0.5 | Lemon Squeezy KYC; Jobber Developer Center 2FA and a manual app review done over email; Twilio A2P 10DLC brand registration for the SMS tier | Yes. SaaS, so support grows slowly. |
| T2 | Accela/EnerGov Permit Actor (Apify) | 9 | 1–1.5 | 0.1–0.25 | Apify payout KYC (photo ID); tax form | Yes. Portals that use CAPTCHA are dropped, never solved. |
| T3 | TipSplit for Clover | 7 | 4–5 | 0.5–1 | Clover production developer verification (ID, DOB, proof of address, OFAC check, possible document upload); developer agreement; app review (functional video, privacy policy and EULA review) | Mostly. Wage-dispute tickets need a human and grow with the number of locations. |
| W1 | Bid Brief: Facilities Services (Substack) | 5 | 3–3.5 | 1–1.5 as written (0.5 if moved to a platform with an API) | Substack + Stripe KYC; **Substack has no publishing API**, so someone must post twice a week; login.gov MFA for the SAM.gov key | Yes, once publishing is automated. As written, posting is a fixed human chore. |
| W2 | Florida HOA Board Letter Kit | 8 | 2.5–3 (+1 if attorney review is arranged) | 0.25–0.5 | Etsy ID + selfie check (Persona) + bank + card; Lemon Squeezy KYC | Yes. Instant download; only the Etsy inbox grows, and slowly. |
| W3 | Grant Deadline Desk: [State] | 6 | 4–4.5 | 0.75–1 | Lemon Squeezy KYC; personal outreach to associations, libraries and grant writers; nonprofit vendor paperwork (W-9, invoices) | Partly. Org buyers ask for W-9s and invoices one sale at a time. |
| A1 | "Closing Day" house portraits | 4 | 3–3.5 | 1–2 (Q4 peak), possibly more | Etsy ID + selfie; Etsy API app; Printify–Etsy connection; Pinterest business account + Standard API access (video review); ads card | No. Messages, revisions, Printify defect claims and realtor relationships all grow with sales. |
| A2 | Little Guests wedding activity book | 6 | 2.5–3 | 0.5–1 | Etsy ID + selfie; Etsy API app; Pinterest API access | Partly. Likeness revisions and Etsy messages grow with orders. |
| A3 | "Looks Like Me" visual schedule cards | 7 | 3–4 (incl. ~1–2 h human QA of the base library) | 0.25–0.5 (+0.5 once TPT starts) | Etsy ID + selfie; TPT seller account + KYC later (no seller API, so uploads are manual) | Yes for ready-made packs. Mostly yes for custom packs. |
| D1 | LanguageBids tender alerts | 7 | 3 | 0.75 | Lemon Squeezy KYC; login.gov MFA for the SAM.gov key (a higher quota needs a role with a SAM-registered entity, so use the public extract instead); ATA listservs are members-only | Yes |
| D2 | InspectionWatch OSHA alerts | 7 | 2 | 0.5–0.75 | Lemon Squeezy KYC; DOL portal key (simple); main channel is human LinkedIn posting | Yes |
| D3 | LabelScout TTB COLA intelligence | 8 | 3 | 0.25–0.5 | Lemon Squeezy KYC; spirits affiliate applications (human applicant, age gate) | Yes |
| S1 | Done-For-You Airbnb Guidebook | 5 | 3 | 0.75–1.25 | Etsy ID + selfie; Etsy API app; domain | Partly. Buyer chat and change requests grow with orders, and hosted guides become a permanent support duty. |
| S2 | Bilingual Toolbox Talks | 8 | 3–3.5 (incl. arranging a native-Spanish spot check) | 0.25–0.5 | Etsy ID + selfie; Lemon Squeezy/Gumroad KYC | Yes. Instant download plus a scheduled email subscription. |
| S3 | Custom Wedding Toasts & Eulogies | 4 | 3 | 1–1.5 at break-even, growing linearly | Etsy ID + selfie; Etsy API app; **a human looks at about 10% of orders by design** | No. Anxious-buyer messages and sensitive-order review grow with every sale. |

**Ranking by autonomy:** T2 (9) > T1, W2, D3, S2 (8) > T3, A3, D1, D2 (7) > A2, W3 (6) > W1, S1 (5) > A1, S3 (4).

---

## Cross-cutting findings (apply to several ideas)

These were checked on 2026-10-06. Sources are at the bottom.

1. **Etsy API has no messaging endpoint.** Open API v3 has no conversations or messages path. A human must read and answer every Etsy message in the Etsy app. This affects W2, A1–A3, S1–S3. Slow replies hurt Star Seller status and search ranking, so in practice this is a *daily* check, even when it only takes a few minutes.
2. **The Etsy API no longer returns buyer emails** (`buyer_email` has been null for most apps since Feb 2024; access is case-by-case). Any plan that says "the operator emails the buyer a download link" only works if the buyer types their email into our intake or upload form. That form's link must reach the buyer through an **instant-download file** in the listing (S1 and S3 do this; A1 and A2 need to). Otherwise a human sends the link by Etsy message on every order.
3. **New Etsy shops need a photo ID + selfie check (Persona)**, a bank account and a card. This is human-only and occasionally triggers a further review or a payment reserve.
4. **Etsy API access is tiered (as of Jul 2026).** A "Seller App" for your own shop is close to instant. Commercial access is slow and reportedly hard to get. All ideas here need only the Seller App, which is fine. Shop Stats search-term data is **not** in the API, so "tune tags from Etsy stats" means a human exports or screenshots it, about 10 min/week, or the operator works only from per-listing views and favourites.
5. **Etsy off-platform / fee-avoidance policy.** Encouraging buyers to buy through another venue (including by QR code) is prohibited. This affects A1 ("Realtor? 5-packs here" direct-checkout link in delivered files), S2 (subscription offer inside the Etsy pack) and S1 (refresh-plan upsell). These need rewording or removing, or the shop risks suspension, and a suspension takes human effort to appeal.
6. **Etsy services policy.** Custom writing, design and illustration delivered as digital files are an *allowed* service. That lowers the takedown risk the S1 and S3 ideators flagged. AI items must be listed as "Designed by seller" with AI disclosure.
7. **Pinterest automation.** The Developer Guidelines say "end users must choose each Pin to be published" and ban features that "automatically initiate actions without specifically considering each action". Fully autonomous auto-pinning (A1, A2, A3, S-ideas if added) breaks this. Either the sponsor approves a weekly batch (about 10 min/week) or the channel is dropped. Standard API access also needs a recorded OAuth video and a review of 5–10+ business days, and AI images get a "Gen AI" label.
8. **Substack has no content/posting API** (it has "deliberately never shipped" one; unofficial wrappers are ToS-grey). In July 2026 Substack also added a Pangram AI-detection tool and talked about filtering AI content from recommendations.
9. **LinkedIn (2026) is cracking down on automated and AI-written posts** ("Seems like AI slop" flag, reach limits). Sponsor-posted channels (D2) need the sponsor to genuinely write or edit, not paste.
10. **Lemon Squeezy** still takes new stores as a standalone product. Stripe Managed Payments (preview since Feb 2026) is the long-term migration path, so expect a possible one-time human re-onboarding later.

---

## T1 — RainCheck for Jobber — Score 8

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | Jobber Developer Center account with 2FA | Human-once (0.5 h) | 2FA is required before you can submit for review. |
| 1 Setup | Lemon Squeezy store + KYC, domain | Human-once (1.25 h) | MoR handles sales tax and VAT. |
| 1 Setup | Twilio account + A2P 10DLC brand/campaign registration (for the $39 SMS tier) | Human-once (0.5–1 h) | Hidden gate. US business SMS needs brand registration; the sole-prop route needs mobile OTP. Defer SMS to keep setup lean. |
| 2 Build | OAuth, GraphQL sync, forecast scoring, digest, reschedule UI | AI | Unverified whether the API can move visits. |
| 3 Launch | Submit for Jobber review; Jobber "follows up by email to discuss next steps and the testing process" | Human-once (1–1.5 h) | Partner emails and possibly a call. Timeline unpublished. |
| 4 Marketing | Marketplace listing, SEO pages | AI | |
| 4 Marketing | Jobber Community forum replies | Human-recurring (0.25 h/wk) | Disclosed human posts only. |
| 5 Each sale | OAuth install → trial → LS checkout | AI | No per-sale human. |
| 6 Support | Email support, refunds | AI; Human for refunds over $X | Owners may want phone support; politely decline. |
| 7 Maintenance | API changes, rule presets, uptime | AI | |
| 8 Finance | LS payouts, income tax | Human-recurring (~0.25 h/wk averaged) | MoR covers sales tax. |

**Hard gates:** LS KYC, Jobber 2FA + review/approval, A2P 10DLC (only for SMS).
**Platform automation policies:** No bot-posting issue. Forum promotion must be by a disclosed human. The "sent with RainCheck" client-SMS footer has to be in the registered 10DLC campaign sample messages.
**Scaling cliff:** None. Install, trial and billing are self-serve. The real human risk is Jobber partner-team escalation (API misuse, review requests) and liability if an auto-move reschedules a job wrongly. Keep moves owner-confirmed. Setup is a little over the ideal, but recurring time is close to zero.

## T2 — Accela & EnerGov Permit Extractor (Apify) — Score 9

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | Apify account | AI or Human-once (0.1 h) | Email sign-up. |
| 1 Setup | Payout KYC (legal name + photo of ID/driver's licence), billing details, tax form | Human-once (0.75–1 h) | Required before any payout. |
| 2 Build | Accela ASP.NET postback crawler, EnerGov JSON client, schema | AI | |
| 3 Launch | Publish to Apify Store | AI | No long human review. |
| 4 Marketing | Store SEO, README, integration recipes, changelog | AI | |
| 4 Marketing | "Replies" to Upwork asks / r/webscraping | Human-recurring (optional, 0–0.25 h/wk) | Hidden gate: responding on Upwork needs an ID-verified Upwork account and is bidding, not commenting. Recommend dropping this. |
| 5 Each sale | Pay-per-event billing by Apify | AI | No per-sale human. |
| 6 Support | Apify issue threads | AI | |
| 7 Maintenance | Nightly self-test, auto-hide broken jurisdictions | AI | |
| 8 Finance | Monthly payout review, income tax | Human-recurring (~0.1 h/wk) | Apify bills users. |

**Hard gates:** Apify KYC only.
**Platform automation policies:** Apify is built for automation. The risk sits on the target side: agencies that turn on reCAPTCHA must be **dropped, not solved**. Solving CAPTCHAs automatically breaks most portal terms and puts the sponsor at risk. An agency cease-and-desist would need a human response (rare, unpredictable).
**Scaling cliff:** None. More users mean more revenue and zero extra human time. This is the most autonomous idea in the batch.

## T3 — TipSplit for Clover — Score 7

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | Clover production developer account: name, DOB, home address matching a utility bill or bank statement, phone, OFAC check, possible document upload to a Clover Box folder; developer agreement | Human-once (1.5–2 h) | Account must be approved *before* app approval starts. |
| 1 Setup | Tax/payout details, domain | Human-once (0.5 h) | Clover bills merchants, so no MoR is needed. |
| 2 Build | Pool engine, cash-tip UI, exports, audit log | AI | |
| 3 Launch | App review: functional walkthrough video, permissions justification, **legal review of privacy policy and EULA**, listing review | AI drafts; Human-once (1–1.5 h) | The AI can script the screen recording. A human must sign off on the legal terms and answer reviewer emails. Status can loop through "Changes Required". |
| 4 Marketing | App Market listing, SEO calculator | AI | |
| 4 Marketing | Reseller/ISO emails | Human-recurring (0.25 h/wk) | Personal, from the sponsor. |
| 5 Each sale | Install → trial → Clover billing | AI | |
| 6 Support | Ordinary tickets | AI | |
| 6 Support | **Tip-calculation or wage disputes** | Human-recurring (0.25–0.5 h/wk on average) | Wage-and-hour exposure; the sponsor holds liability. |
| 7 Maintenance | Clover API changes, timeclock-data gaps | AI | |
| 8 Finance | Payout review, income tax | Human (~0.1 h/wk) | |

**Hard gates:** Clover identity, OFAC and business verification; Clover legal-document review.
**Platform automation policies:** None against AI building or running the app. The review cares about merchant data permissions.
**Scaling cliff:** Mild. Restaurant owners expect a human for disputes and sometimes phone support, so wage-dispute handling grows with locations. Setup is heavier than T1 because of Clover's KYC-style developer vetting.

## W1 — Bid Brief: Facilities Services — Score 5 (7 if moved off Substack)

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | Substack + Stripe Connect KYC, domain | Human-once (1 h) | |
| 1 Setup | SAM.gov account via login.gov (MFA/phone) to get the API key | Human-once (0.5 h) | The non-federal quota is low. Use the public daily extract for metadata. |
| 2 Build | Extract → NAICS filter → attachments → LLM cards → USAspending | AI | |
| 3 Launch | Back-filled issues, state pages | AI writes; **Human posts to Substack** | **No Substack publishing API.** |
| 4 Marketing | APEX Accelerator intros (10–15), recommendation-swap asks | Human-once (1.5 h) | Personal emails. |
| 4 Marketing | GovCon community posts | Human-recurring (0.33 h/wk, first month) | |
| 5 Each issue | **Paste and schedule each issue in Substack's editor, twice a week** | Human-recurring (0.5–0.75 h/wk) | Hidden ongoing chore. Unofficial wrappers are ToS-grey. |
| 6 Support | Reader email, deadline-error corrections | AI; Human skim (0.25 h/wk) | One wrong deadline kills trust. |
| 7 Maintenance | SAM schema/quota changes; login.gov key renewal | AI; Human-recurring (key renewal every ~90 days) | |
| 8 Finance | Stripe payouts; Substack is not an MoR | Human (~0.1 h/wk) | Digital-subscription sales tax is mostly not collected; this is a small legal exposure. |

**Hard gates:** Stripe KYC, login.gov, and Substack's lack of an API, which is a human gate *every issue*.
**Platform automation policies:** Substack added AI detection (Pangram) in July 2026 and has floated filtering AI content out of recommendations. That hurts the "Substack discovery" channel for an AI-written digest.
**Scaling cliff:** None per subscriber, but the fixed ~1 h/week is at the sponsor's ideal ceiling. **Fix:** publish through a platform with an API and paid tiers that fit the cap, or self-host (Lemon Squeezy subscriptions + Resend + Cloudflare Pages archive). That drops recurring time to about 0.5 h/week and raises the score to about 7.

## W2 — Florida HOA Board Letter & Notice Kit — Score 8

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | Etsy shop: photo ID + selfie (Persona), bank, card, setup fee | Human-once (1 h) | |
| 1 Setup | Etsy Seller App API key; Lemon Squeezy KYC | Human-once (0.75 h) | The Seller App tier is near-instant. |
| 1 Setup | Approve disclaimer wording; optionally arrange a FL HOA attorney review | Human-once (0.5 h, +1 h if attorney) | The attorney is paid from revenue. |
| 2 Build | Templates, guide, flowcharts, DOCX/PDF | AI | |
| 3 Launch | Listings via API with AI disclosure, "Designed by seller" | AI | |
| 4 Marketing | Etsy SEO, SEO articles | AI | Shop Stats search terms are not in the API, so a human exports them (optional, 0.1 h/wk). |
| 4 Marketing | HOA board forum answers | Human-recurring (0.33 h/wk, optional) | |
| 5 Each sale | Instant download (Etsy) / LS file delivery | AI/platform | **No per-sale human.** |
| 6 Support | Etsy messages ("does this work for my HOA?") | Human-recurring (0.15–0.25 h/wk) | No messaging API. The AI drafts replies. |
| 6 Support | Refund demands after a lost fine dispute | Human (rare) | |
| 7 Maintenance | Annual July law-change refresh | AI | Ideally a human or attorney re-check each year (about 1 h/yr). |
| 8 Finance | Etsy collects marketplace sales tax; LS is MoR | Human (~0.1 h/wk) | |

**Hard gates:** Etsy ID/selfie, LS KYC.
**Platform automation policies:** Etsy creativity standards are met with "Designed by seller" plus AI disclosure. Listing via the API on your own shop is allowed.
**Scaling cliff:** None meaningful. Static digital downloads produce few messages per sale. This is the most autonomous Etsy idea.

## W3 — Grant Deadline Desk: [State] — Score 6

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | Lemon Squeezy KYC, domain, beehiiv | Human-once (1.25 h) | |
| 2 Build | 990-PF funder universe, monthly crawl, gated calendar | AI | Some funder portals (Foundant, Fluxx, SmartSimple) need logins to see cycles. Do not create accounts or solve CAPTCHAs on them. |
| 3 Launch | First free edition, public top-10 page | AI | |
| 4 Marketing | Emails to the state association, libraries and 10–20 grant writers | Human-once (2–3 h) | Each is personal. |
| 4 Marketing | Partner follow-ups | Human-recurring (0.5 h/wk) | |
| 5 Each sale | Self-serve checkout + license key | AI | |
| 5 Each sale | **Nonprofit procurement: W-9 requests, vendor forms, invoices, "can we pay by check?"** | Human-recurring (0.25–0.5 h/wk, scales with org sales) | The W-9 must be signed by the sponsor. LS invoices help, but vendor forms don't go away. |
| 6 Support | "You missed a funder" fixes, support | AI | |
| 7 Maintenance | Monthly re-verification crawl | AI | |
| 8 Finance | LS payouts | Human (~0.1 h/wk) | |

**Hard gates:** LS KYC; signed W-9s for nonprofit buyers; human-only partnership outreach.
**Platform automation policies:** None of note. Free channels depend on associations and libraries trusting a human.
**Scaling cliff:** Partial. Each institutional buyer can create a small paperwork task. Data work scales cleanly.

## A1 — "Closing Day" Watercolor House Portraits — Score 4

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | Etsy shop (ID + selfie, bank, card), Seller App key | Human-once (1.25 h) | |
| 1 Setup | Printify account + OAuth to Etsy | Human-once (0.5 h) | |
| 1 Setup | Pinterest business account, developer app, Standard-access OAuth video | Human-once (0.75 h) | The review takes 5–10+ business days. |
| 1 Setup | Card for Etsy Ads | Human-once (0.25 h) | |
| 2 Build | Photo upload site, image-edit + vision diff, lettering | AI | |
| 3 Launch | 25 listings with AI + production-partner disclosure | AI | |
| 4 Marketing | Auto-pin 3/day | **Policy conflict.** Human must pick pins (0.15 h/wk) or drop the channel | Pinterest: "end users must choose each Pin". |
| 4 Marketing | Realtor direct-checkout link in files | **Etsy fee-avoidance risk.** Remove. | |
| 5 Each sale | Buyer reaches the upload page. The API gives no buyer email, so the link must be inside an instant-download file. | AI if the listing is designed this way; otherwise **Human per order** | Physical Printify listings have no instant-download file, so the buyer needs an Etsy message. |
| 5 Each sale | Generate, QA, deliver, 1 revision | AI | |
| 5 Each sale | Printify order with a custom image | AI via the Printify API, or human edits on-hold orders | |
| 6 Support | Etsy messages ("can you remove the car?", "will it arrive by Christmas?") | Human-recurring (0.75–1.5 h/wk in Q4) | |
| 6 Support | Printify defect claims (photos), refunds, cases | Human-recurring (0.25 h/wk) | |
| 6 Support | Realtor pack relationships | Human (ad hoc) | |
| 7 Maintenance | Tag tuning, ads | AI and human (stats not in the API) | |
| 8 Finance | Etsy collects sales tax; payouts | Human (~0.1 h/wk) | |

**Hard gates:** Etsy ID, Printify connection, Pinterest API review, inbox access.
**Platform automation policies:** Pinterest bans fully automated pinning. Etsy prohibits steering buyers to off-Etsy checkout. AI and production-partner disclosure is mandatory.
**Scaling cliff:** **Yes.** Custom photo work + Q4 physical gifts + fidelity complaints means human time grows with sales, likely past 1.5 h/week at break-even in Q4. Physical items add shipping-delay messages the ideator didn't count.

## A2 — Little Guests Wedding Activity Book — Score 6

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | Etsy shop (ID + selfie), Seller App key | Human-once (1.25 h) | |
| 1 Setup | Pinterest business account + API Standard access | Human-once (0.75 h) | Same pin-choice rule as A1. |
| 2 Build | Puzzle generators, layout engine, line-art pipeline, upload form | AI | |
| 3 Launch | 20 listings with disclosure | AI | Each personalised listing must include an instant-download "start here" PDF with the form link, because the API gives no buyer email. |
| 4 Marketing | Pins (human picks weekly), Etsy SEO | AI + Human (0.15 h/wk) | |
| 5 Each sale | Photo upload, generation, kid-safety and likeness QA, delivery | AI | Image APIs may refuse edits of real photos of minors (flower girl, birthday child). Fall back to an avatar-style likeness, not a human. |
| 6 Support | Etsy messages, revision disputes, "doesn't look like us" refunds | Human-recurring (0.33–0.75 h/wk) | |
| 6 Support | Photo deletion and privacy requests | AI (automated 30-day purge) | |
| 7 Maintenance | Seasonal listing swaps (birthday edition) | AI | |
| 8 Finance | Payouts | Human (~0.1 h/wk) | |

**Hard gates:** Etsy ID, Pinterest API review.
**Platform automation policies:** Pinterest pin-choice rule. Photos of children add privacy exposure that the human carries. No Etsy blocker beyond disclosure.
**Scaling cliff:** Partial. Digital only, so better than A1, but personalised likenesses produce revision messages roughly in proportion to orders.

## A3 — "Looks Like Me" Visual Schedule Cards — Score 7

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | Etsy shop (ID + selfie), Seller App key, Pinterest | Human-once (1.75 h) | |
| 2 Build | Avatar sheets, ~600-card base library, PDF/label engine, avatar builder | AI | |
| 2 Build | **Human spot-check of the base library** (sensitive audience: wrong objects or hands hurt children's routines) | Human-once (1–2 h, recommended) | The ideator relies on vision-QA only. |
| 3 Launch | ~20 listings + free sample | AI | |
| 3 Launch | TPT store later: account + KYC, **and manual product uploads** (no public seller API found) | Human-once (0.5 h) + Human-recurring (~0.5 h/wk while building the TPT catalogue) | Hidden recurring cost. |
| 4 Marketing | Pins (human-chosen), Etsy SEO | AI + Human (0.15 h/wk) | |
| 5 Each sale | Ready-made: instant download | AI/platform | No human. |
| 5 Each sale | Custom: form-configured avatar (no child photos), ~150 images, 72 h | AI | Form link goes in an instant-download PDF. |
| 6 Support | Etsy messages, quality complaints | Human-recurring (0.15–0.33 h/wk) | |
| 7 Maintenance | New avatars, Spanish labels | AI | |
| 8 Finance | Payouts | Human (~0.1 h/wk) | |

**Hard gates:** Etsy ID; TPT KYC and manual listing.
**Platform automation policies:** TPT is reported to demote low-quality AI stores (Chalkbeat, Aug 2026), and no automated upload path exists. Etsy requires disclosure.
**Scaling cliff:** Small. Ready-made packs scale freely. Custom orders are AI-fulfilled with no photo uploads, which removes most privacy handling.

## D1 — LanguageBids — Score 7

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | sam.gov account via login.gov (MFA, phone) for the API key | Human-once (0.5 h) | Getting about 1,000 calls/day needs a role tied to a SAM-registered entity, which is heavy identity proofing. **Use the public Contract Opportunities extract instead** and skip the role request. |
| 1 Setup | LS KYC, domain | Human-once (1.25 h) | |
| 2 Build | SAM/TED/CanadaBuys/USAspending ingest, classifier, pages | AI | |
| 3 Launch | Public tender pages, digest | AI | |
| 4 Marketing | Trade-press pitches | AI drafts; Human sends if ignored (0.25 h/wk) | |
| 4 Marketing | ProZ forums, ATA listservs | Human-recurring (0.5 h/wk) | **ATA listservs are member-only; dues are well above the $100 cap.** ProZ forums restrict promotion. |
| 5 Each sale | Trial → LS subscription | AI | |
| 6 Support | Email support; refunds | AI; Human approves refunds | |
| 7 Maintenance | Source schema changes; sam.gov key renewal (periodic) | AI; Human-recurring (a few minutes every ~90 days) | |
| 8 Finance | LS MoR | Human (~0.1 h/wk) | |

**Hard gates:** LS KYC, login.gov, community access that needs membership.
**Platform automation policies:** None for data. Community posting must be by a disclosed human. Portals such as Bonfire and BidNet forbid scraping (the ideator already excludes them).
**Scaling cliff:** None. The human time is fixed marketing time, which can shrink once SEO and press take over.

## D2 — InspectionWatch — Score 7

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | DOL Open Data Portal registration + questionnaire → API key | Human-once (0.25 h) or AI | Key-sharing is prohibited, so keep it out of public repos. |
| 1 Setup | LS KYC, domain | Human-once (1.25 h) | |
| 2 Build | Daily delta ingest, 5-year backfill, state pages | AI | |
| 3 Launch | 50 state pages, digest | AI | |
| 4 Marketing | **LinkedIn safety-group posts (the main early channel)** | Human-recurring (0.5 h/wk) | The 2026 LinkedIn crackdown on AI-written posts means the sponsor must genuinely author or edit them. |
| 4 Marketing | Editor/ASSP pitches | AI; Human when editors want a person (0.1 h/wk) | |
| 5 Each sale | Trial → LS | AI | |
| 6 Support | Support; **"remove my company" requests from inspected employers** | AI; Human judgement (rare) | Public data, but these are reputational calls. |
| 7 Maintenance | DOL v4 API migration breakages | AI | |
| 8 Finance | LS MoR | Human (~0.1 h/wk) | |

**Hard gates:** LS KYC only. The rest is light.
**Platform automation policies:** LinkedIn bans automation, so posting stays human. No bots on r/OSHA.
**Scaling cliff:** None per sale. The score is held at 7 because the key acquisition channel is human-only and open-ended.

## D3 — LabelScout — Score 8

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | LS KYC, newsletter account, domain | Human-once (1.5 h) | |
| 1 Setup | Spirits affiliate program applications (human applicant, tax forms, age-gate review) | Human-once (1–1.5 h) | Optional. Dropping affiliates cuts setup to about 1.5 h. |
| 2 Build | COLA registry ingester (no login, no anti-bot currently), permittee CSV join | AI | Keep request rates polite. A future CAPTCHA would be a stop sign, not something to solve. |
| 3 Launch | Public pages, two digests | AI | |
| 4 Marketing | Scoop pitches to whiskey writers, trade-press stats | AI (from the operator inbox) | One-to-one only. |
| 4 Marketing | Editor relationship needing a human | Human-recurring (0.1–0.25 h/wk) | |
| 5 Each sale | Pro trial → LS; quarterly report purchase | AI | |
| 6 Support | Support | AI | |
| 7 Maintenance | Registry changes, affiliate link upkeep | AI | |
| 8 Finance | LS MoR; affiliate 1099s | Human (~0.15 h/wk) | |

**Hard gates:** LS KYC; affiliate applications.
**Platform automation policies:** No self-promotion on r/bourbon (the ideator already plans this). Alcohol affiliate programs require an age gate and responsible-marketing rules.
**Scaling cliff:** None.

## S1 — Done-For-You Airbnb Guidebook — Score 5

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | Etsy shop (ID + selfie), Seller App key, domain, inbox | Human-once (2–2.5 h) | |
| 2 Build | Intake form, PDF + web-guide generator, QR | AI | |
| 3 Launch | 8–10 listings; instant-download PDF carries the intake link + order code | AI | Custom writing and design is an allowed Etsy service, so takedown risk is lower than the ideator feared. |
| 4 Marketing | Etsy SEO, sample town pages | AI | |
| 5 Each sale | Intake → research → verify places → deliver | AI | Buyer email comes from the intake form (not from the API). |
| 5 Each sale | Order completion | AI/platform | A digital listing auto-completes. |
| 6 Support | **Etsy messages: hosts chat, ask for edits, chase "where's my guide"** | Human-recurring (0.5–1 h/wk, grows with orders) | |
| 6 Support | Wrong-place complaints | AI fixes; Human replies on Etsy | |
| 6 Support | "Keep it fresh" $29/yr upsell to Etsy buyers | **Etsy off-platform risk.** Offer it as a separate Etsy listing instead. | |
| 7 Maintenance | **Hosting every guide forever** | AI (permanent liability) | |
| 8 Finance | Etsy sales tax; payouts | Human (~0.1 h/wk) | |

**Hard gates:** Etsy ID.
**Platform automation policies:** Fine on Etsy services. The off-platform upsell needs reworking.
**Scaling cliff:** **Partial.** Custom, chatty buyers mean message time grows with orders, and the hosted-guide promise piles up obligations if the business stops.

## S2 — Bilingual Toolbox Talks — Score 8

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | Etsy shop (ID + selfie), Lemon Squeezy/Gumroad KYC, domain | Human-once (2.5 h) | |
| 1 Setup | Arrange a native-Spanish spot check (buyer swap or paid) | Human-once (0.5–1 h) | Recommended. Stiff Spanish fails on the jobsite. |
| 2 Build | 6 × 52 talks, OSHA citation checks, sign-in sheets, meeting-log app | AI | |
| 3 Launch | ~26 Etsy listings + Gumroad/Payhip | AI | Payhip is another KYC account (0.25 h). |
| 4 Marketing | Etsy SEO, sample-talk pages | AI | |
| 4 Marketing | Outreach to safety blogs and associations (sponsor sends a handful) | Human-recurring (0.1–0.25 h/wk) | |
| 5 Each sale | Instant download; subscription via LS | AI/platform | No per-sale human. |
| 5 Each sale | "4 free weeks" offer inside the Etsy PDF | **Etsy off-platform risk.** Make it a free sample-library link, not a purchase CTA. | |
| 6 Support | Etsy messages (low volume), subscriber email | Human (0.1–0.2 h/wk); AI | |
| 7 Maintenance | Sunday-night sends, weather triggers, new trades | AI | |
| 8 Finance | MoR + Etsy | Human (~0.1 h/wk) | |

**Hard gates:** Etsy ID, MoR KYC.
**Platform automation policies:** Etsy off-platform rule (above). Otherwise clean.
**Scaling cliff:** None. Static packs plus a scheduled email product. The human carries safety-content liability, not workload.

## S3 — Custom Wedding Toasts & Eulogies — Score 4

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | Etsy shop (ID + selfie), Seller App key, domain | Human-once (2–2.5 h) | |
| 2 Build | Questionnaires, draft + self-critique pipeline, cue-card renderer | AI | |
| 3 Launch | 10–12 role listings with AI disclosure; instant-download questionnaire PDF | AI | Custom writing is an allowed Etsy service. |
| 4 Marketing | Etsy SEO, sample speeches | AI | |
| 5 Each sale | Intake → draft → deliver | AI | |
| 5 Each sale | **Human skim of sensitive orders (eulogies, divorce, estrangement) — about 10% by design** | Human-recurring (2–5 min/order) | A per-sale human gate built into the design. |
| 5 Each sale | Rush 12 h orders | AI; but Etsy questions on rush orders need fast human replies | |
| 6 Support | **Anxious-buyer Etsy messages ("will it be ready Saturday?")** | Human-recurring (0.75–1.25 h/wk at break-even) | Must be checked daily; slow replies cost ranking. |
| 6 Support | Revisions; "I thought a human wrote this" complaints | AI + Human (reviews/cases) | |
| 7 Maintenance | Listing tuning | AI + Human stats export | |
| 8 Finance | Payouts | Human (~0.1 h/wk) | |

**Hard gates:** Etsy ID; a human-review step on some orders.
**Platform automation policies:** AI disclosure is mandatory. Buyers who missed it leave negative reviews and open cases, which need a human.
**Scaling cliff:** **Yes.** Human minutes grow linearly with orders (messages + sensitive-order review). At the stretch target (about 35 orders/month) this approaches 2–3 h/week, close to the hard gate.

---

## Sources (checked 2026-10-06)
- Etsy API has no messaging endpoint: https://www.rapidevelopers.com/api-automations/how-to-automate-etsy-customer-messages-using-the-api
- Etsy buyer_email access restricted since Feb 2024: https://github.com/etsy/open-api/discussions/1185 and the RapiDevelopers guide above
- Etsy API access tiers / commercial-access difficulty: https://github.com/etsy/open-api/discussions/1663 , https://www.itechguides.com/?p=863702
- Etsy services policy (custom writing, design and illustration allowed as digital files): https://www.etsy.com/legal/policy/services/242665313101
- Etsy creativity standards / AI disclosure: https://www.listadum.com/blog/etsy-creativity-standards , https://etsy.com/legal/creativity
- Etsy off-platform / fee-avoidance policy: https://www.etsy.com/legal/policy/off-platform-transactions/1254654515806
- Etsy new-shop photo ID + selfie (Persona) and setup fee: https://www.valueaddedresource.net/etsy-new-shop-set-up-fee-id-checks/
- Pinterest developer guidelines (end users must choose each Pin) and access tiers: https://policy.pinterest.com/en/developer-guidelines , https://developers.pinterest.com/docs/key-concepts/access-tiers/
- Pinterest Gen AI labels: https://zernio.com/blog/pinterest-new-ai-content-filter
- Jobber app review process (2FA, email-driven review/testing): https://developer.getjobber.com/docs/publishing_your_app/app_review_process
- Clover developer account verification and app approval: https://docs.clover.com/docs/developer-account-approval , https://docs.clover.com/docs/developer-app-approval
- Apify payout KYC: https://docs.apify.com/platform/actors/publishing/monetize/monthly-payouts
- Substack has no posting API; AI detection: https://www.usecarly.com/blog/claude-substack-integration , https://www.eweek.com/news/top-substack-newsletters-use-ai-tech/
- LinkedIn 2026 AI-content crackdown: https://www.tubefilter.com/2026/08/10/linkedin-ai-slop-button-thinkfluencing-proofreading-tool/
- SAM.gov Opportunities API: https://open.gsa.gov/api/get-opportunities-public-api/
- DOL Open Data Portal key registration: https://www.dataportal.dol.gov/pdf/dol-api-user-guide.pdf
- TTB COLA registry open, no anti-bot: https://apify.com/scrapersdelight/ttb-cola-scraper
- Lemon Squeezy / Stripe Managed Payments status: https://fungies.io/lemon-squeezy-stripe-acquisition-saas-founders-2026/
- Gumroad payout verification: https://roo.beehiiv.com/p/gumroad-fees-2026
- TPT AI-quality concerns: https://www.chalkbeat.org/2026/08/03/ai-slop-on-teachers-curriculum-marketplace/

_Not verified: Jobber and Clover review durations; whether TPT has any seller upload API (none found); Twilio A2P 10DLC details for sole proprietors in 2026 (based on prior knowledge); the exact Etsy API listing `views` field coverage._
