# Market Analyst review: run 2026-10-06

_Reviewer: market-analyst. Date: 2026-10-06. Method: about 2–4 web searches or fetches per idea (WebSearch/WebFetch), cross-checked against the evidence the ideators cited. Etsy search pages returned 403, so Etsy volume figures come from third-party trackers (findniche, RankHero) or search snippets. Claims I could not verify are marked `(unverified)`._

**Score = Market dimension (1–10)** per `scoring-rubric.md`: 10 = proven demand, beatable competitors, room for a newcomer; 1 = no demand, or saturated with free alternatives.

| ID | Idea | Score | Demand evidence (short) | # Competitors | Saturation | AI-commoditization risk |
|---|---|---|---|---|---|---|
| T1 | RainCheck for Jobber (weather-risk scheduling) | **7** | Jobber forum "mass reschedule" threads; Jobber++ extension shows weather on the calendar; rival FSMs (MowHQ, Groundcut) sell weather rescheduling as a feature | ~5 (none found as a dedicated Jobber Marketplace app) | Low | Low |
| T2 | Accela/EnerGov permit extractor (Apify) | **5** | Shovels.ai reached $3M ARR (Aug 2026) selling permit data; 10+ permit Actors on Apify, but the one with Accela support has 38 total users and 6 monthly | ~15 on Apify + Shovels, BuildZoom, ConstructConnect | Medium | Medium |
| T3 | TipSplit for Clover (tip-pool calculator) | **7** | TipHaus claims 500k+ users; 7shifts charges $49.99/location/mo for tip management; Clover marketplace has known organic pull | ~10 (TipHaus, Tipout, 7shifts, TipJar, Kickfin, Push, Homebase…) | Medium | Low |
| W1 | Bid Brief: federal janitorial and grounds bids | **4** | Large paid "janitorial GovCon" course ecosystem; ~10.5k janitorial bids published by GovernmentBids | ~20+ (SamSearch, PursuitCue, GovTribe, HigherGov, GovernmentBids, govcontractfinder, free SAM.gov alerts) | High | High |
| W2 | Florida HOA board letter and notice kit | **4** | Search demand for "HOA violation letter template" (unverified volume); paid kits exist on Payhip and Etsy | ~10+ named, plus hundreds of free templates; Common Elements gives away FL Ch. 720 templates | Medium–High | High |
| W3 | Grant Deadline Desk (one-state grant calendar) | **4** | Paid grant databases at every price point (GrantWatch $249/yr, GrantStation $199/yr, Instrumentl $299+/mo) | ~10 national + free state portals (grants.ohio.gov) + community-foundation deadline pages | High | Medium–High |
| A1 | "Closing Day" house portraits | **4** | Top Etsy listing: 34.5k sales, ~122 sales/mo at $24.99; another: 5.8k sales at $12.53 | Hundreds+ | Red ocean | High |
| A2 | Personalised kids' wedding activity book | **5** | Etsy kids' wedding activity packs: 9.0k and 15.4k lifetime sales (findniche) | Hundreds+ generic; ~5–15 photo-personalised | High (generic) / Medium (photo-personalised) | Medium–High |
| A3 | "Looks Like Me" visual schedule cards | **5** | ~7.2k Etsy "visual schedule printable" listings; TPT top products have 800–6,000+ ratings; personalised skin-tone sets sell at $30–60 | Hundreds+; ~10 offer skin-tone or avatar options | Medium–High | Medium–High |
| D1 | LanguageBids (translation/interpreting tender alerts) | **5** | ~10k small US language-services firms; steady public RFP flow; no dedicated US alert service found | ~5 (Stotles free alerts for UK/EU, plus generic aggregators) | Low | Low–Medium |
| D2 | InspectionWatch (OSHA inspection alerts) | **6** | 4+ Apify "OSHA leads" Actors exist (a buyer-demand signal); consultants pay $10–40 per click for "OSHA consultant" ads (ideator, unverified) | ~6 (Apify Actors, safetyrecord.org, osha.gov) | Medium | Medium |
| D3 | LabelScout (TTB COLA and new-permittee intel) | **4** | BW166 sells paid approvals reports; COLA Cloud and Apify COLA alert Actors exist | ~5 (BW166, COLA Cloud, Apify COLA scrapers, TTB registry) | Medium | High |
| S1 | Done-for-you Airbnb guidebook | **4** | ~1,000 Etsy searches/mo for "airbnb welcome book"; Fiverr done-for-you gigs at $50–200 | Hundreds+ (Etsy templates, Fiverr gigs, Touch Stay, StayScan, GuestGuidePDF, Hostfully) | High | High |
| S2 | Bilingual trade-specific toolbox talks | **4** | Paid Etsy packs ($19–$99); NRCA charges $95/$195; CPWR Spanish talks passed 100k downloads | ~20+ including free (NAWIC, TDI, ALCA, CPWR) and AI generators (HandsHQ free, ISN Empower, toolboxtalk-ai) | Medium–High | High |
| S3 | Custom wedding toasts and eulogies | **3** | One Etsy shop has 4,111 sales; a Fiverr seller has 1,000+ orders | Hundreds+ (Etsy writers, Fiverr, My Wedding Toast, Speechcraft, ToastWiz, Speech Smith, free generators) | Red ocean | High |

**Read-across.** The three ideas with the best markets are integrations inside a platform's own marketplace (T1, T3) or a niche, recurring B2B data feed (D2). They score well because chatbots cannot replace them and their competitors charge 3–5x more. Etsy personalisation and writing ideas (A1, S1, S3, W2) face either a red ocean or a one-prompt chatbot substitute, and in some cases both. Their demand is real but the newcomer's slice is thin.

---

## T1 — RainCheck for Jobber

**Score: 7/10**

- **Demand signals.**
  - Jobber's community forum has recurring "mass reschedule" and "rescheduling multiple clients at once" threads ([thread 1](https://community.getjobber.com/discussions/job-details-scheduling/mass-reschedule/5442), [thread 2](https://community.getjobber.com/discussions/job-details-scheduling/rescheduling-multiple-clients-at-once/1284)).
  - A user built the Jobber++ Chrome extension specifically to show weather on the Jobber calendar ([Chrome Web Store](https://chromewebstore.google.com/detail/ajndglfjbcifnlheimmalgblmigcpiea)).
  - Competing field-service platforms advertise weather rescheduling as a feature: MowHQ (from $49) flags rain days, and Groundcut ($99/mo) auto-reschedules and notifies clients ([MowHQ](https://www.capterra.com/p/10038735/MowHQ/), [Groundcut](https://www.capterra.com/p/10043210/Groundcut/)). The feature is clearly valued.
- **Competitors (~5).**
  - Jobber's native "move visits" bulk tool, which has no weather data.
  - Jobber++ (free; display only).
  - Custom automation consultancies: US Tech Automations ([guide](https://ustechautomations.com/resources/blog/automate-weather-delay-notification-landscaping-2026)) and Fieldproxy ([page](https://www.fieldproxy.ai/automations/painting-reschedule-on-weather)).
  - Switching to MowHQ or Groundcut.
  - I found no dedicated weather app in the Jobber App Marketplace `(unverified: the marketplace page returned 404)`.
- **Saturation: Low.** A newcomer is noticed through the marketplace listing alone. The real threat is Jobber shipping weather natively, not other indie apps.
- **AI commoditization: Low.** The value is OAuth access, overnight monitoring and acting on the schedule, none of which a chatbot does.
- **Market size.** Jobber reports 100k+ businesses. If even 30% are weather-dependent, 16 customers at $19–39 is about 0.05% of that pool. The market is large enough, but signups will be seasonal and slow until March 2027.
- **Wedge.** Trade-specific rules (pressure-washing temperature floors, painting dry windows) plus client notices, priced well below switching to an FSM with built-in weather.

## T2 — Accela & EnerGov Permit Extractor (Apify)

**Score: 5/10**

- **Demand signals.**
  - Permit data is a proven market: Shovels.ai reached $3M ARR in August 2026, up from $1.5M at the end of 2025 ([Sacra](https://sacra.com/c/shovels/)).
  - Apify search shows 10+ building-permit Actors ([handstands](https://apify.com/handstands.io/us-building-permit-scraper/api), [careybrown](https://apify.com/careybrown/permit-signal-scout/api), [samstorm](https://apify.com/samstorm/building-permit-lead-scraper/api), [maydit](https://apify.com/maydit/us-building-permits-scraper.md), and others).
  - **Per-Actor demand looks thin.** The handstands Actor covers 36 jurisdictions at $1.50/1k permits and has only **38 total users and 6 monthly active users** ([fetched](https://apify.com/handstands.io/us-building-permit-scraper)).
- **Competitors.**
  - ~15 Apify Actors.
  - Shovels, which covers 1,800+ jurisdictions with API, credit and enterprise plans; Accela counties are likely included.
  - BuildZoom and ConstructConnect.
  - The handstands Actor already advertises "Accela ONE" open-data support, but not ACA portal scraping.
- **Saturation: Medium.** The "permits on Apify" shelf is crowded. The narrow ACA/EnerGov coverage gap is real but defensible only briefly.
- **AI commoditization: Medium.** AI coding tools make Actors cheap to clone, which already explains the flood of near-identical permit Actors.
- **Market size.** Break-even needs about 90k paid permits a month. If the best-known peer has 6 monthly users, reaching about 10 steady daily-run agencies is a stretch. The market exists, but the Apify slice is thin and leaks to free-plan users.
- **Wedge.** Long-tail counties that are only on ACA or EnerGov (the Sun Belt roofing and solar markets), sold through Clay and n8n recipes that create daily repeat usage.

## T3 — TipSplit for Clover

**Score: 7/10**

- **Demand signals.**
  - Tip pooling is a category people already pay for. TipHaus claims "500,000+ users" ([Capterra](https://www.capterra.com/p/10042325/TipHaus/)).
  - 7shifts charges **$49.99/location/month** for its tip-management add-on, and one reviewer says it requires 7shifts payroll ([turnozo comparison](https://turnozo.com/blog/turnozo-vs-homebase-vs-7shifts)).
  - TipHaus on Clover is $99/location plus $300 setup (ideator source).
  - The Clover App Market has a proven organic channel (ideator's Flippa comp: about 25k merchants on a cash-discount app).
- **Competitors (~10).**
  - On Clover: TipHaus ([integration](https://tiphaus.com/integration/clover)) and Tipout by OrderOut, which pays tips instantly onto virtual cards ([page](https://clover.orderout.co/solutions/tipout)).
  - Elsewhere: 7shifts, TipJar, Kickfin, Push Operations, Branch and TipMeOut ([G2](https://www.g2.com/products/tipmeout/competitors/alternatives)).
  - Homebase (free to $30/mo) integrates with Clover; whether its tip pooling works on Clover is `(unverified)`.
- **Saturation: Medium.** The category is full, but every incumbent sells a bundle (instant payout, payroll, scheduling) at $50–100/location. A "math plus audit log for $14.99" option is a clear low-end gap.
- **AI commoditization: Low.** The value is pulling data from the POS and keeping persistent rules and history.
- **Market size.** Clover has hundreds of thousands of food-and-beverage merchants `(unverified count)`. About 29 locations is a tiny share.
- **Wedge.** Cafés and bakeries with 4–15 staff that pool by hours and don't need instant payout. Lead with "no setup fee, 1/7th the price".

## W1 — Bid Brief: Facilities Services

**Score: 4/10**

- **Demand signals.**
  - A paid course and YouTube "janitorial government contracting" ecosystem exists (ideator).
  - GovernmentBids reports about 10.5k janitorial bids published, and the federal government spends billions a year on janitorial services ([search summary](https://samsearch.co/gov-explore/contract-categories/porter-services)).
  - Direct willingness to pay for a $19 newsletter is `(unverified)`.
- **Competitors (~20+), and the closest one does exactly this pitch.** SamSearch's janitorial page advertises AI extraction of "square footage, cleaning frequencies, special requirements… SCA wage determinations", geographic alerts by zip, county or state, and recompete tracking ([SamSearch](https://samsearch.co/industries/janitorial-services)). Others:
  - PursuitCue, a bid-fit tool built specifically for NAICS 561720 ([SaaSHub](https://www.saashub.com/pursuitcue)).
  - govcontractfinder.com, which publishes free indexable janitorial notice pages ([example](https://govcontractfinder.com/contracts/janitorial-services-glacier-public-service-center-psc-1240bd26q0002)).
  - GovTribe, HigherGov, GovDirections and GovernmentBids.
  - SAM.gov's own free saved-search alerts, and Swept's guides.
- **Saturation: High.** The ideator's core differentiator, the AI-summarised SOW, is already productised.
- **AI commoditization: High.** AI GovCon tools are multiplying, and SOW summarisation is one prompt away for anyone with the PDF.
- **Market size.** It is adequate on paper: tens of thousands of small cleaning firms, and 20 subscribers needed. Churn is the issue, because most never win.
- **Wedge.** Price-anchored, human-readable newsletter format for first-time bidders, plus award-price recaps for learning to price. This is a modest edge at best.

## W2 — Florida HOA Board Letter & Notice Kit

**Score: 4/10**

- **Demand signals.** HOA template queries are common, judging by the many SEO-spam template pages in the search results. An Etsy "HOA violation notice dispute letter" listing exists ([Etsy](https://www.etsy.com/listing/1352941737/hoa-violation-notice-dispute-letter)). I could not verify sales counts because Etsy returned 403, so actual Etsy volume is `(unverified)`. Florida has a large self-managed HOA base, and the 2024 HB 1203 changes create real confusion.
- **Competitors (~10 named + hundreds of free templates).**
  - **Common Elements publishes free Florida Chapter 720 templates**: notice of violation, board meeting agenda, and fining-committee guidance ([violation notice PDF](https://jleqsdacvgktabpuwdpt.supabase.co/storage/v1/object/public/governance-templates/fl-notice-of-violation/fl-notice-of-violation.pdf), [agenda PDF](https://jleqsdacvgktabpuwdpt.supabase.co/storage/v1/object/public/governance-templates/fl-board-meeting-agenda/fl-board-meeting-agenda.pdf)).
  - PayHOA and Condo Control free templates.
  - The HOA Board Compliance Kit (Payhip) and HOA Board Studio (ideator sources).
  - Law-firm blogs explaining the fining steps for free.
- **Saturation: Medium–High.** Free, state-specific, statute-aware templates already exist, so this is not an empty niche.
- **AI commoditization: High.** "Write a Florida 720.305 violation letter" is a one-prompt task, and free competitors are clearly AI-assisted.
- **Market size.** It is borderline at 9 kits a month. It depends on Etsy ranking for low-volume queries, and it is seasonal (January–March).
- **Wedge.** The full sequenced process (flowchart plus letters plus an annual law-change update) for boards that have never run a fining hearing. Expansion to Texas Ch. 209 doubles the pool.

## W3 — Grant Deadline Desk: [State]

**Score: 4/10**

- **Demand signals.** Nonprofits clearly pay for grant discovery at every price point:
  - GrantWatch at $249/yr, with state subsites such as [oh.grantwatch.com](https://oh.grantwatch.com/).
  - GrantStation at $199/yr via TechSoup.
  - Grantsights at $29/mo.
  - Grantable, with a free tier and a $25/mo nonprofit price.
  - Instrumentl at $299–$999/mo.

  Sources: [Grantable comparison](https://grantable.co/best-instrumentl-alternatives), [aitoolsbakery](https://aitoolsbakery.com/blog/instrumentl-alternatives/).
- **Competitors (~10 national + free local).**
  - The national databases above, plus Candid.
  - Free state portals ([grants.ohio.gov](https://grants.ohio.gov), referenced by [Zeffy's Ohio guide](https://www.zeffy.com/grant-finder/grants/ohio)).
  - Community foundations publishing their own deadline calendars ([Columbus Foundation deadlines](https://columbusfoundation.org/nonprofit-center/deadlines-open-houses)).
  - State nonprofit associations: Philanthropy Ohio and OANO.
- **Saturation: High.** "Deadlines in my state" is already what GrantWatch's state subsites sell. The ideator's "verified small local funders" angle is the only gap.
- **AI commoditization: Medium–High.** AI grant-finders (Grantable, Grantsights, Instrumentl's AI) are cutting prices quickly. Chatbots can't know this year's deadlines, but those tools can.
- **Market size.** Ohio has tens of thousands of small nonprofits, so 35 annual subscribers is plausible on paper. The trust ramp is slow and buyers are price-sensitive.
- **Wedge.** Freelance grant-writer "consultant licence" with CSV export, and deep coverage of local family and community foundations that national databases miss.

## A1 — "Closing Day" watercolor house portraits

**Score: 4/10**

- **Demand signals: very strong.** One Etsy watercolor home-portrait listing has about **34,513 sales**, about 8.2k reviews and about **122 sales a month** at $24.99 ([findniche](https://findniche.com/etsy-product/home-portrait-house-painting-housewarmin-1176417219)). Another has 5,765 sales at $12.53 ([findniche](https://findniche.com/etsy-product/100-hand-painted-house-painting-custom-w-4326874345)). Realtor closing gifts and Q4 housewarming gifts are durable demand.
- **Competitors: hundreds+.**
  - Etsy listings, many already AI-made at $8–20 ([example](https://www.etsy.com/listing/595774315), [example](https://www.etsy.com/listing/4398624141)).
  - Fiverr hand-painters ([example](https://it.fiverr.com/abagailarton/watercolor-a-house-portrait)).
  - One-tap AI apps that make house watercolors: an iOS "Watercolor Portraits" app, Canva, and Vizbull ([App Store](https://apps.apple.com/us/app/-/id6755938527), [Vizbull](https://vizbull.com/photo-to-watercolor-sketch-painting)).
- **Saturation: Red ocean.** Trackers explicitly call the niche saturated. A newcomer needs reviews, which it can't get without sales, and the new-listing boost is short.
- **AI commoditization: High.** The core output is a one-prompt image edit, and the supply is already AI-flooded.
- **Market size.** It is huge in aggregate, but the newcomer's reachable slice depends on breaking into page 1. 16 sales a month is achievable only with ads, a Q4 tailwind, and some luck.
- **Wedge.** Realtor prepaid credit packs (a B2B repeat buyer) and the 24-hour speed promise, rather than Etsy gift buyers.

## A2 — Personalised kids' wedding activity book

**Score: 5/10**

- **Demand signals: strong for the category.**
  - A personalised pre-filled kids' wedding activity pack has 8,999 sales and about $82.8k revenue ([findniche](https://findniche.com/etsy-product/personalised-pre-filled-wedding-activity-1469549121)).
  - A kids' wedding activity box has 15,416 sales ([findniche](https://findniche.com/etsy-product/kids-wedding-activity-box-black-script-p-1380983514)).

  Both are physical or semi-physical, so digital-only demand is somewhat lower. Printable books sell at about $6–12 ([Etsy](https://www.etsy.com/listing/1758834423)).
- **Competitors.**
  - Hundreds+ generic packs, plus free printables from The Knot and blogs ([The Knot](https://theknot.com/content/printable-wedding-activities-for-kids)).
  - Name-only customisable books.
  - I found **few or no listings converting the couple's photo into coloring pages inside a full book**. The search turned up name and date personalisation, plus separate "photo to coloring page" services.
- **Saturation: High for generic packs, Medium for photo-personalised books.**
- **AI commoditization: Medium–High.** One page is trivially made with ChatGPT. A cohesive, solvable 20-page book is less so, but cloners can follow.
- **Market size.** It is enough for about 15–18 sales a month at peak season. October–February is a weak period, so expect a slow start.
- **Wedge.** "A coloring book of YOU" built from the couple's photo, pets and venue, which no top seller does. Birthday editions fill the off-season.

## A3 — "Looks Like Me" visual schedule cards

**Score: 5/10**

- **Demand signals.**
  - Visual-schedule printables have about 7.2k Etsy listings at an average of $6.73 ([makerwords](https://www.makerwords.com/keyword/visual-schedule-printable)).
  - TPT's top visual-schedule products carry 800–6,000+ ratings (ideator).
  - Specialist Etsy shops have only modest volumes: AutismvisualsShop has 481 sales and AutismVisualDesigns has 276 ([shop](https://www.etsy.com/ca/shop/AutismvisualsShop), [shop](https://www.etsy.com/de-en/shop/AutismVisualDesigns)).
  - **Personalised illustrated sets already sell at $30–60** (204 cards), and some products offer girl/boy and skin-tone variants ([Etsy](https://www.etsy.com/listing/1688239009), [Etsy](https://www.etsy.com/listing/1665535011)).
- **Competitors.** Hundreds+ generic sellers, about 10 with representation or avatar options, and free symbol sets (ARASAAC). TPT incumbents have thousands of reviews.
- **Saturation: Medium–High.** The representation sub-angle (wheelchair, AFOs, hearing aids, glasses) is genuinely thin, but it isn't empty.
- **AI commoditization: Medium–High.** TPT is visibly fighting "AI slop" (Chalkbeat, Aug 2026). Disclosure may depress conversion among SLPs and teachers.
- **Market size.** It is adequate: about 25 ready-made plus 5 custom sales a month is plausible across Etsy and TPT within a few months, if quality is high.
- **Wedge.** Disability-representation avatars (wheelchair, AFO, hearing aid) with strict consistency and accuracy QA. This sub-niche is where parents report they "can't find" visuals.

## D1 — LanguageBids

**Score: 5/10**

- **Demand signals.**
  - The US has about 10k small (1–9 employee) linguistic firms ([worldmetrics](https://worldmetrics.org/linguistic-consulting-industry-statistics/), [Nimdzi on LSP counts](https://www.nimdzi.com/how-many-language-service-providers/)).
  - Public language-services RFPs are frequent at state level and among NGOs ([Louisiana example](https://wwwcfprd.doa.louisiana.gov/osp/lapac/agency/pdf/8966801.pdf), [Mercy Corps](https://www.mercycorps.org/tenders/rfp-translation-services)).
  - I found no direct proof that LSPs pay for a niche feed. Willingness to pay is `(unverified)`.
- **Competitors (~5).**
  - **Stotles** already offers free email alerts on CPV 79530000/79540000 translation and interpretation tenders for UK and Europe, with award and expiry tracking ([Stotles translation](https://www.stotles.com:443/explore/notices/topics/79530000/translation-services), [interpretation](https://www.stotles.com/explore/notices/topics/79540000/interpretation-services)).
  - Generic US aggregators: HigherGov, GovDirections, BidNet, GovSpend, nationgraph.
  - No dedicated US language-services alert product turned up.
- **Saturation: Low in the US, Medium in the EU** (Stotles is free, so the EU portion is not a selling point).
- **AI commoditization: Low–Medium.** It requires persistent multi-source monitoring. Generic AI bid tools could add a filter.
- **Market size.** It is small but sufficient: 10–15 Solo subscribers at $29, or 4–5 Agency subscribers. The hard part is coverage, because most US spend is on state, county, court and school portals that are hard to scrape.
- **Wedge.** US state, court and healthcare interpreting RFPs plus award and incumbent pricing history. Drop the EU emphasis.

## D2 — InspectionWatch

**Score: 6/10**

- **Demand signals.**
  - At least four Apify Actors sell OSHA inspection and citation leads to safety consultants: [tagadanar](https://apify.com/tagadanar/osha-inspection-leads) (from $3.50/1k), [ayoub_highlighter](https://apify.com/ayoub_highlighter/osha-enforcement-leads), [belcaidsaad violations](https://apify.com/belcaidsaad/osha-violations-demand) and [belcaidsaad citations](https://apify.com/belcaidsaad/osha-citation-scraper). Builders keep making them, which is a signal that someone buys.
  - Safety consulting retainers run $7,950–$34,950 a year (Lancaster Safety, from search results), so the ROI of finding one client is obvious.
- **Competitors (~6).** Those Actors, free osha.gov establishment search (inspections appear within 0–2 days), safetyrecord.org, and general data vendors (ZoomInfo).
- **Saturation: Medium.** The raw data is commoditised for technical buyers. The non-technical consultant wanting a daily territory email with enrichment is underserved. None of the Actors package it that way.
- **AI commoditization: Medium.** Pressure comes from cheap scrapers rather than chatbots.
- **Market size.** It is adequate. There are thousands of independent safety consultants and trainers (ASSP has about 36k members, `(unverified)`). Break-even needs only about 7 subscribers at $49.
- **Wedge.** "Inspections opened yesterday in your territory, with 5-year history and plain-English 'what to pitch'", sold to trainers and consultants rather than law firms (those face solicitation rules).

## D3 — LabelScout

**Score: 4/10**

- **Demand signals.**
  - BW166 sells monthly Product Approvals Reports and a Label Inquiry tool, which proves B2B demand ([BW166 sample](https://www.bw166.com/wp-content/uploads/2025/11/bw166_product_approvals_report_202506-Sample.pdf)).
  - Whiskey media regularly mine COLAs (ideator).
  - Whether label printers pay $49/mo for "first-time applicant" leads is `(unverified)`.
- **Competitors (~5).**
  - BW166.
  - **COLA Cloud**: 2.5M+ COLAs with AI-enriched fields, permittee data, an MCP server and a 500 request/month free tier ([glama](https://glama.ai/mcp/servers/@cola-cloud-us/colacloud-mcp/blob/e5f4b3488506f41a3b320a00b1d569838bb1001c/README.md)).
  - The Apify **scrapersdelight TTB COLA Scraper**, which ships "new approvals" email, webhook and RSS recipes at $4/1k ([Apify](https://apify.com/scrapersdelight/ttb-cola-scraper)).
  - The free TTB registry.
- **Saturation: Medium.** The B2B data layer is already productised at both the cheap end (Apify, COLA Cloud) and the premium end (BW166).
- **AI commoditization: High.** COLA Cloud's MCP server lets a buyer ask Claude or ChatGPT directly for "new whiskey labels this week". That is close to the exact chatbot substitute the operator-constraints warn about.
- **Market size.** It is uncertain. There are a few thousand potential B2B buyers (label printers, agencies). The consumer affiliate side is restricted by alcohol-marketing rules.
- **Wedge.** The COLA × new-permittee join ("brand-new distilleries and importers this week") packaged for label and packaging sales reps, if COLA Cloud doesn't already surface it.

## S1 — Done-For-You Airbnb Guidebook

**Score: 4/10**

- **Demand signals.**
  - About 1,000 Etsy searches a month for "airbnb welcome book" (RankHero, per ideator).
  - Fiverr done-for-you gigs at $50–200 ([sahl01](https://fiverr.com/sahl01/digital-airbnb-welcome-book)).
  - SaaS incumbents with recurring revenue (Touch Stay from $19/mo, Hostfully).
- **Competitors: hundreds+.**
  - Etsy templates (median $8).
  - Fiverr gigs.
  - Etsy sellers already offering "fully custom 15–20-page" done-for-you books (search summary).
  - **AI generators that do exactly this offering**:
    - Touch Stay's AI guidebook generator builds a branded guide from an Airbnb link in minutes ([Touch Stay](https://touchstay.com/features/ai-guidebook-generator)).
    - StayScan says "60 seconds" ([G2](https://www.g2.com/sellers/stayscan)).
    - GuestGuidePDF is an AI PDF guidebook generator ([Capterra](https://www.capterra.co.za/software/1083880/GuestGuidePDF)).
- **Saturation: High.** The "done-for-you" sub-angle the ideator saw as empty is already served both by humans on Etsy and Fiverr and by AI SaaS.
- **AI commoditization: High.** The output is literally what incumbents now auto-generate from a listing URL.
- **Market size.** It is fine in aggregate (millions of hosts). For an Etsy newcomer, about 10 orders a month at $39 is possible but not assured.
- **Wedge.** One-time price with no subscription, plus "local places verified with a last-checked date", aimed at 1–3 property hosts who resent paying Touch Stay monthly.

## S2 — Trade-Specific Bilingual Toolbox Talks

**Score: 4/10**

- **Demand signals.**
  - Paid Etsy packs sell at $16.85–$99.99 (ideator snippets).
  - NRCA charges $95 for members and $195 for non-members.
  - CPWR's Spanish talks passed 100k downloads.
  - toolboxtalk-ai charges $49–149/mo.

  The underlying need is real and recurring, because insurers and GCs expect documented weekly meetings.
- **Competitors (~20+), with a large free supply.**
  - Free: NAWIC bilingual weekly PDFs ([NAWIC](https://nawic.org/safety-toolbox-talks/)), the Texas Department of Insurance's free bilingual talks, ALCA's 180 landscape safety talks in Spanish ([Lawn & Landscape](https://www.lawnandlandscape.com/news/alca-offers-spanish-translation-of-safety-book)), and academic landscaping/tree-care bilingual talks ([Frontiers](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1690149/full)).
  - Free AI generators: HandsHQ (any language, no account) ([HandsHQ](https://handshq.com/free-templates/ai-powered-toolbox-talk-generator)) and ISN Empower's in-app AI talks.
- **Saturation: Medium–High.**
- **AI commoditization: High.** Free AI generators already produce talks in any language.
- **Market size.** The ideator concedes it may be "a few hundred dollars a month". Reaching $300 needs about 15 packs plus some subscribers, which is plausible but not easy against free supply.
- **Wedge.** Non-construction trades that free libraries skip (janitorial, pest control, pool service, tree care), plus a dated meeting log for insurer and GC audits. The documentation trail is worth more than the talk.

## S3 — Custom Wedding Toasts & Eulogies

**Score: 3/10**

- **Demand signals: real.**
  - The PersonalWordsmith Etsy shop has 4,111 sales.
  - A Fiverr seller has 1,000+ speech orders.
  - Bespoke writers charge up to £399.
- **Counter-signals: decisive.**
  - Wedding Speech AI makes about $17/mo on TrustMRR ([TrustMRR](https://trustmrr.com/startup/wedding-speech-ai)).
  - A large field of AI speech products competes directly with the same questionnaire-to-speech flow:
    - My Wedding Toast: from $34, with a free version ([Capterra](https://www.capterra.com/p/10046108/My-Wedding-Toast/)).
    - Speechcraft: Trustpilot reviews ([Trustpilot](https://es.trustpilot.com/review/speechcraft.co)).
    - ToastWiz ([theaireport](https://www.theaireport.ai/tooldatabase/toastwiz)).
    - Speech Smith: a free preview, then a small fee.
    - Free generators such as InsertChat ([InsertChat](https://insertchat.com/free-tools/wedding-speech-generator)).
    - Etsy listings that are already "AI speech generators" at $7.35.
- **Saturation: Red ocean.**
- **AI commoditization: High.** This is the purest "why not just ask ChatGPT" case in the batch, and buyers increasingly know it. Mandatory AI disclosure on Etsy removes the main reason buyers pay a human writer.
- **Market size.** It is huge in aggregate. A disclosed-AI newcomer's slice is small, and October–December is the off-season.
- **Wedge.** Eulogies, which are urgent and emotionally hard to self-prompt, and where reassurance and a guided questionnaire matter more than wit. That is a sensitive category, though, and the ideator flags that it needs human review.
