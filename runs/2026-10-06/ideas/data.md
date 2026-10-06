# Data & research ideas — The Analyst

_Generated 2026-10-06. Web research was used to check that each data source exists, how it can be accessed, and who already sells something similar. The notes on each source are at the end of the file._

A pattern runs through all three ideas: **the raw data is already commoditised.** For every source below, you can find several pay-per-record scrapers on Apify. Our product isn't access to the data. It's a **finished, niche-specific decision feed** for a non-technical buyer who will never open Apify. The buyer gets one vertical, deduplicated and classified records, a plain-English summary, and history and context that a scraper doesn't give. That is the moat, and the risks section of each idea is honest about how thin it is.

---

## D1 — LanguageBids: public tender alerts for translation & interpreting firms

- **Persona:** The Analyst (ideator-data-analyst)
- **One-liner:** A daily and weekly alert feed of every public-sector translation, interpreting, localization, and ASL/CART tender in the US, Canada, and EU, for small language service providers (LSPs) and freelance interpreter collectives.
- **Customer:** Owners and bid managers at small and mid-sized LSPs (2–50 staff) and interpreter agencies, plus court and medical interpreting cooperatives. They spend time on ProZ.com, the ATA (American Translators Association) and its division listservs, Slator and MultiLingual magazine, the Nimdzi reports, and LinkedIn groups for LSP owners. They already pay for CAT tools (Trados or memoQ, about $30–60/month), ProZ membership (about $15/month), ATA dues, and sometimes a generic bid service such as BidNet, GovSpend, HigherGov, or GovDirections. Those generic services charge $50–$300+/month and flood them with irrelevant results.
- **Problem / desire:** "Government language contracts are steady, multi-year revenue, but they're scattered across SAM.gov, state portals, school districts, and the EU, and the generic bid sites send me 200 'translation' hits a week, half of which are software or 'translation of requirements'. I find the good ones after the deadline."
- **Offering:** A SaaS-lite email and web feed.
  - (a) A **daily alert email** that matches each subscriber's filters: service type (written translation, on-site/OPI/VRI interpreting, ASL, localization, transcription), geography, set-aside eligibility (small business, 8(a), WOSB), and value band.
  - (b) A **searchable web dashboard** of open tenders with a 1-paragraph AI summary of each one. The summary gives the scope, the languages named, the incumbent if known, the deadline, the submission method, and red flags such as on-site requirements or certification needs.
  - (c) A **"who won" award history** for the niche, built from SAM.gov award notices, the USAspending.gov API, and CanadaBuys award CSVs. The point is to answer "who's the incumbent, and what did they charge?"
  - (d) A **CSV export** for the higher tier.
- **Price & revenue model:** Subscription, sold through a merchant of record (MoR).
  - **Solo:** $29/month or $290/year. US federal + Canada + EU, with daily alerts.
  - **Agency:** $79/month or $790/year. Adds award history and incumbent lookup, CSV export, 3 seats, and state/local open-data feeds.
  - **Free tier:** A free public weekly digest with the top 10 tenders, which doubles as the traffic engine.
  - **ROI pitch:** "One won county interpreting contract is typically worth $50k–$500k+ over its term; this costs less than one hour of a court interpreter's time per month." The contract-value figure is directional and should be verified against award data before it goes in marketing copy.
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Domain | $12 |
| Hosting: Cloudflare Pages + Workers + D1, or Supabase free tier | $0 |
| Email sending: Resend or Brevo free tier, a few thousand emails/month | $0 |
| API keys: SAM.gov public API (free, via sam.gov account), USAspending (no key), TED API (free), CanadaBuys open data (no key) | $0 |
| **Total** | **$12** |

### Monthly running costs (excluding operator tokens)
- Hosting/DB: $0 on free tiers at launch. Plan for about $5–10/month on a paid tier (Workers Paid or Supabase Pro) once there are more than a few hundred subscribers.
- Email: $0 up to about 3k emails/month. About $20/month at about 300 daily-alert subscribers.
- Payment/MoR fees: about 5% + $0.50 per transaction (Lemon Squeezy/Paddle-style).
- LLM summarisation of tenders is counted under operator tokens. Volume is small, roughly 20–80 relevant notices/day across all sources.
- **Total fixed:** $0–$30/month.

### Customer acquisition plan
1. Every relevant tender gets a public, indexable page with a summary and the deadline. Every week gets a public "This week in public language-services tenders" digest page. Together these are a long-tail SEO base for queries like "[city] interpreting services RFP 2026" and "translation tender [agency]".
2. Each page has a free-signup form for the weekly digest.
3. The weekly digest shows 10 tenders in full and teases the rest: "37 more matching tenders, 6 closing this week, available to subscribers".
4. A 14-day free trial of daily alerts converts to Solo. The award-history data upsells Agency.
5. A quarterly **"US/EU Public Language Services Market Report"** is published free and pitched to trade press (Slator, MultiLingual, Nimdzi blog). It reports total value awarded, top buyers, top winners, and price per word or per hour where disclosed. It earns backlinks and authority.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Trade-press data pitches** — Send one-to-one emails (not bulk) to Slator, MultiLingual, and the ATA Chronicle with a data story such as "US agencies awarded $X in interpreting contracts in Q3; top 10 buyers". It works early with zero audience because these outlets hunger for numbers and almost nobody aggregates public language-services procurement. Expected speed: 1–4 weeks to the first mention.
2. **Community presence by the human sponsor** — The sponsor posts the free weekly digest link in the ProZ.com forums (business-of-translation sections) and relevant ATA division listservs, as the disclosed founder and within each forum's self-promotion rules. Budget about 30 min/week, operator-drafted. It works because it is useful, free content for a niche that rarely gets any. Expected speed: 1–3 weeks.
3. **Programmatic SEO on tender pages** — The long tail is low-competition (specific agency + "interpreting RFP"), and the generic bid sites gate their pages behind logins. Pages stay limited to real tenders with genuinely useful summaries, not thin AI filler, to avoid Google's scaled-content demotion. Expected speed: 6–12 weeks to meaningful traffic.
4. **Newsletter cross-promotion** — Swap mentions with existing translator newsletters and Substacks, pitched one-to-one. Expected speed: 3–6 weeks.

### Path to first sale
- **Days 0–3:** The human sponsor creates a sam.gov account (it uses login.gov, which needs identity and phone verification) to get the public API key, sets up a Lemon Squeezy store, and buys the domain. The operator builds the ingesters:
  - SAM.gov Opportunities API, filtered on NAICS 541930 (Translation & Interpretation), the relevant PSC codes, and keywords
  - CanadaBuys open-data CSVs
  - TED API with CPV 79530000/79540000
  - USAspending for awards
- **Days 4–10:** The operator builds the classifier and summariser, the public tender pages, the weekly digest, and Stripe-free checkout through the MoR. It backfills 12 months of awards for the "who won" pages.
- **Days 10–20:** The first weekly digest goes out, the first press pitches are sent, and the sponsor makes the first forum posts. The operator also publishes the first quarterly market report.
- **Days 20–45:** Trial-to-paid conversions begin.
- **Estimated days to first sale: ~35.**

### Who does what
- **AI operator:** Builds and maintains the ingesters (scheduled GitHub Actions or Workers cron), classification and dedup, summaries, the site, the digest, and the market reports. Drafts press pitches and forum posts. Answers support email and monitors source schema changes.
- **Human sponsor:**
  - One-time (~3 h): sam.gov/login.gov account and API key, MoR account, domain, and an approved non-federal API role request if the 40 calls/day limit for new accounts binds.
  - Recurring (~45 min/week): posts the digest in 1–2 communities, sends press pitches from their own name if outlets ignore an unknown sender, and approves refunds.

### Moat — why not just ask ChatGPT?
ChatGPT can't watch SAM.gov, TED, and CanadaBuys every day and remember what it already showed you. The moats are:
- **Accumulated, cleaned history:** awards, incumbents, and price signals that build up over time.
- **A niche-specific classifier:** separating real language-services tenders from "translation" noise.
- **Habit and convenience:** a daily email that's just right.
- **Distribution in a small community.**

The moat is weak against a funded generic bid aggregator adding a "language services" filter. The niche is too small for most of them to bother curating it well, though.

### Biggest risks (ideator's own view)
- **Low coverage of the biggest US buyers.** Most US translation and interpreting spend is state, county, court, school district, and hospital procurement. Much of it sits on portals (Bonfire, BidNet, DemandStar, OpenGov) whose terms forbid scraping. Launch coverage is federal + Canada + EU + a handful of open-data cities and states (e.g. NYC City Record via NYC Open Data). That may feel thin to US-only buyers.
- **Small market and price sensitivity.** Freelancers won't pay; the buyers are LSPs, of which there are a few thousand in the US. Churn after a contract win, or after a dry spell, is likely.
- **Source fragility.** SAM.gov API limits are 40 calls/day for new non-federal accounts and about 1,000/day after role approval. SAM.gov also changes schema, and the sponsor must keep the sam.gov account active, since API keys expire periodically.

---

## D2 — InspectionWatch: daily OSHA inspection & citation alerts for safety consultants

- **Persona:** The Analyst (ideator-data-analyst)
- **One-liner:** A daily email and CSV of newly opened federal and state-plan OSHA inspections and newly issued citations, filtered by state and industry. It lets safety consultants, EHS trainers, and OSHA-defense firms reach employers in the 0–60 days when they urgently need help.
- **Customer:** Independent safety consultants and small EHS consulting firms (1–20 staff), plus safety-training providers (OSHA 10/30, forklift, fall protection), industrial hygiene labs, and OSHA-defense/employment law firms.
  - **Where they hang out:** ASSP (American Society of Safety Professionals) local chapters and its member community, the NSC (National Safety Council), EHS Today, ISHN, the "safety professionals" groups on LinkedIn, and r/OSHA.
  - **What they already pay for:** CRM tools, ZoomInfo or Apollo (expensive, generic), trade-show booths, and Google Ads at $10–$40 per click for "OSHA consultant near me".
- **Problem / desire:** "The best time to sell a safety program is the week after OSHA walks in. By the time citations hit the OSHA website 30+ days later, three other consultants and a law firm have already called them. I want to know who just got inspected in my territory, why (complaint, fatality, referral), and their history, every morning."
- **Offering:** A subscription data feed.
  - (a) A **daily morning email** per subscriber territory with new inspections from DOL OSHA inspection data. Each entry has the establishment name, city/state, NAICS industry, inspection type (complaint, accident/fatality, referral, programmed), scope, and whether a union is involved. It also flags repeat visits.
  - (b) **New citations** from the DOL violation data, with standards cited, serious/willful/repeat flags, and initial penalty. There is a plain-English line per standard, e.g. "1926.501 = fall protection, construction".
  - (c) An **enrichment column** with the establishment's prior 5-year OSHA history and the industry's top-cited standards, which gives "what to pitch".
  - (d) A **CSV/Google-Sheets-ready export** and a simple web dashboard with a map.
  - No personal data: establishment-level business records only, with no individual names, phones, or emails. Subscribers do their own outreach under their own compliance obligations.
- **Price & revenue model:** Monthly subscription through the MoR.
  - **Territory:** $49/month for 1 state.
  - **Regional:** $99/month for up to 5 states.
  - **National + API/CSV:** $199/month.
  - Annual plans get 2 months free.
  - **ROI pitch:** "One new client is worth $3k–$20k/year in consulting or training; one per year pays for a decade of this."
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Domain | $12 |
| DOL Open Data Portal API key (free registration) | $0 |
| Hosting: Cloudflare Pages/Workers/D1 or Supabase free tier | $0 |
| Email: Resend/Brevo free tier | $0 |
| **Total** | **$12** |

### Monthly running costs (excluding operator tokens)
- Hosting/DB: $0 at launch. About $5–25/month once the historic inspection table (millions of rows) is loaded into a paid Postgres or D1 tier; storing only the last 5 years plus aggregates keeps this at the lower end.
- Email: $0 up to about 3k/month, then about $20/month.
- MoR fees: about 5% + $0.50 per transaction.
- **Total fixed:** $0–$45/month.

### Customer acquisition plan
1. **Free public "OSHA This Week in [State]" pages, one per state,** auto-published weekly. Each shows:
   - counts by industry
   - fatality/accident inspections
   - largest penalties
   - most-cited standards

   These are genuinely newsworthy local data that safety pros share, and long-tail SEO for "OSHA inspections [state] 2026" and "OSHA fines [industry]".
2. Each page has a CTA for the free weekly state digest by email.
3. The digest shows aggregates plus 3 sample establishments. The full daily list with company names and history is paid, behind a 7-day free trial.
4. Upsell to the multi-state and API tiers as consultants grow.
5. A quarterly "Most-cited OSHA standards by industry" report, published free, is pitched to EHS Today/ISHN for links.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **ASSP chapter newsletters and safety-trade editors** — The operator drafts one-to-one pitches offering a free monthly "OSHA activity in your region" data column to ASSP chapter newsletter editors and trade outlets (EHS Today, ISHN, Safety+Health). It works with zero audience because editors need fresh local content and it costs them nothing. Expected speed: 2–4 weeks.
2. **The human sponsor shares weekly state pages in LinkedIn safety groups**, as a disclosed founder with value-first posts, about 30 min/week. Safety professionals are active on LinkedIn, and penalty/fatality statistics get engagement. Expected speed: 1–3 weeks.
3. **Programmatic but substantive SEO** — State × industry pages ("OSHA citations in Texas construction, 2026") built from real aggregates. There is low competition beyond osha.gov's own clunky search and a few free lookup sites. Expected speed: 6–12 weeks.
4. **Product Hunt / Indie Hackers launch** — Low intent, but gives a few backlinks. Expected speed: 1 week, small effect.

### Path to first sale
- **Days 0–2:** The sponsor registers the DOL data-portal API key and sets up the MoR store and domain.
- **Days 2–10:** The operator builds:
  - ingest of the inspection, violation, and related datasets from the DOL API, with a daily delta
  - an NAICS and standard-code dictionary with plain-English descriptions
  - the state pages
  - the digest and trial flow
- **Days 10–14:** The operator backfills 5 years of history for enrichment and publishes 50 state pages.
- **Days 14–30:** The sponsor posts in LinkedIn groups and the operator sends editor pitches. The first trials start.
- **Days 21–40:** First conversions. The buyer has budget authority (a solo consultant decides alone) and an obvious ROI.
- **Estimated days to first sale: ~30.**

### Who does what
- **AI operator:** Runs the daily ingest and QA. Watches for schema and API changes; DOL is mid-migration from enforcedata.dol.gov to the v4 Open Data Portal API, so this matters. Builds enrichment, pages, emails, quarterly reports, and editor pitches, and handles support.
- **Human sponsor:**
  - One-time (~2–3 h): DOL API key, MoR account, domain.
  - Recurring (~30–45 min/week): LinkedIn group posts, plus occasional replies to editors who want a human contact.

### Moat — why not just ask ChatGPT?
A chatbot can't deliver "every inspection opened yesterday in my 3 states, with each company's 5-year history" every morning. The value is the daily refresh, the territory filter, enrichment joined across datasets, and the habit-forming email. But the competition is real:
- **Free:** osha.gov establishment search, and lookup sites such as safetyrecord.org.
- **Cheap scrapers:** multiple Apify actors already sell "OSHA inspection leads".

The defensible edge is packaging for non-technical consultants (zero setup, a territory email, plain-English standards) and SEO and brand in the niche. It is a convenience moat, not a data moat.

### Biggest risks (ideator's own view)
- **Commoditised data.** Apify actors and free lookup sites lower willingness to pay. Pricing above about $49/month will need clear enrichment value, and some consultants will simply check osha.gov weekly for free.
- **Ethics and reputation.** This is "ambulance-chasing" for employers in distress. Lawyer subscribers face state solicitation rules (ABA Model Rule 7.3–style limits on direct solicitation). We should market to consultants and trainers first, publish only establishment-level government data, and keep a clear acceptable-use policy.
- **Data gaps and timing.**
  - Federal OSHA data has reporting lags.
  - State-plan states (about half of the US workforce) may report inspections with different timeliness and completeness. This needs verification state by state before selling those territories.
  - Citations are only public after issuance.
  - The DOL API migration could break ingestion temporarily.

---

## D3 — LabelScout: weekly intelligence on new US alcohol label approvals and new permittees

- **Persona:** The Analyst (ideator-data-analyst)
- **One-liner:** A free weekly digest plus a paid feed and dataset of newly approved beverage-alcohol labels (TTB COLAs) and newly permitted wineries, distilleries, importers, and wholesalers. It is for the packaging, distribution, and marketing suppliers who sell to new brands, and it doubles as a consumer "upcoming bourbon/whiskey releases" site monetised by affiliate links.
- **Customer:**
  - **B2B (the subscription revenue):**
    - label printers and packaging/glass suppliers, for whom new brands and new SKUs are leads
    - beverage-alcohol marketing and design agencies
    - importers' and distributors' brand-scouting teams
    - retail and e-commerce buyers
    - beverage trade journalists

    They read BevNET, Brewbound, Shanken News Daily, Wine Business, and Distiller Trail. They already pay for trade-press subscriptions, Nielsen/IRI (big players), and Beverage Information Group / BW166-style data reports. BW166 sells product-approvals reports, which proves demand at a higher price point.
  - **Consumer (traffic and affiliate):** Bourbon and whiskey enthusiasts who already "hunt" COLAs to spot upcoming allocated releases. They read The Whiskey Wash, Breaking Bourbon, and Substack label-watching newsletters, and post in r/bourbon (we never self-promote there; enthusiasts may share organically).
- **Problem / desire:**
  - **B2B:** "Every week hundreds of new brands file labels, and they all need printing, packaging, distribution, and marketing. But the TTB registry is a clunky search with no alerts, so we hear about new brands after they've already picked suppliers."
  - **Consumer:** "I want to know which limited bourbons are coming before they hit shelves."
- **Offering:** Three layers.
  - (a) **Free weekly public digest and site:** notable new approvals by category (whiskey, RTD cocktails, wine, spirits, imports), trend counts ("RTD canned cocktail approvals +18% QoQ"), and an "upcoming releases" page for whiskey enthusiasts that links to retailers via affiliate links where a product already sells.
  - (b) **Pro feed ($49/month):**
    - a weekly CSV/Sheet of all new COLAs, filtered by class/type, origin, and state
    - a "**first-time applicant**" flag (brands or permittees never seen before), which is the hottest lead signal
    - joined with the **TTB FOIA List of Permittees** (weekly CSVs of wineries, distilled spirits plants, importers, wholesalers) to flag *newly permitted* businesses
    - links to the label images on TTB
  - (c) **Quarterly category report ($149 one-time, or included in an annual Pro plan):** e.g. "US RTD Cocktail Label Approvals Q3 2026", with entrants, top filers, flavour and format trends, and imports by country.

  Brewers are excluded from the permittee data. TTB doesn't publish brewer lists because of IRC §6103, though beer COLAs are still in the registry.
- **Price & revenue model:**
  - Pro: $49/month or $490/year.
  - Team: $129/month for 5 seats with daily cadence and alerts on saved filters.
  - Quarterly reports: $149 each.
  - Affiliate commissions on the consumer side: spirits e-commerce affiliate programs, typically a few % to about 10% per order. These are a bonus, not the core.
  - **ROI pitch to label printers:** "One new brand account = $10k+/year in label runs."
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Domain | $12 |
| Hosting: Cloudflare Pages/Workers/R2, free tier | $0 |
| Newsletter: Beehiiv/Buttondown/Substack free tier | $0 |
| Data: TTB Public COLA Registry + TTB FOIA permittee CSVs (public, no fee) | $0 |
| **Total** | **$12** |

### Monthly running costs (excluding operator tokens)
- Hosting: $0. Don't mirror label images; link to TTB to stay inside free storage limits.
- Newsletter: $0 up to the free tier limit (about 1k–2.5k subscribers depending on provider), then about $10–40/month.
- MoR fees: about 5% + $0.50 per transaction.
- **Total fixed:** $0–$40/month.

### Customer acquisition plan
1. **The consumer "upcoming whiskey releases from TTB filings" pages are the traffic engine.** They are evergreen, high-curiosity, and naturally shared by enthusiasts and linked by whiskey blogs, which repeatedly write "spotted in TTB label approvals" stories.
2. **The free weekly digest** has two editions, "Enthusiast" and "Trade", with sign-up on every page.
3. **The Trade digest shows aggregates plus 10 notable new brands.** The CTA is "Get every first-time applicant this week, with permit and contact-ready business address, in the Pro CSV", with a 14-day trial.
4. **Quarterly reports are sold to the same list,** and executive summaries are pitched free to trade press (BevNET, Brewbound, Wine Business, Distiller Trail) in exchange for links and citations.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Scoop-pitching to whiskey and spirits writers** — The operator sends a one-to-one email when an interesting COLA lands, e.g. a new limited release from a major distillery. Writers at The Whiskey Wash, Breaking Bourbon, and others already mine COLAs; a ready-made tip with a link to our page earns citations. It works from day 1 with zero audience. Expected speed: 1–3 weeks.
2. **Trade-press data stories** — A monthly "New brand entrants by category" stat package pitched to BevNET/Brewbound/Wine Business editors. Expected speed: 2–6 weeks.
3. **SEO on brand/product pages** — "[Brand] new label approval" and "[Distillery] upcoming releases 2026". The long tail is very large (about 200k COLA applications a year) and enthusiasts search for it, but each page must add real value: decoded label text, category, history of that brand's filings. Expected speed: 6–12 weeks.
4. **Organic community sharing** — No self-promotion by us on Reddit. Enthusiast posts in r/bourbon often reference COLA finds, and a clean, linkable page becomes the thing people cite. Speed is unpredictable.

### Path to first sale
- **Days 0–3:** The sponsor sets up the MoR store, the newsletter account, and the domain. The operator builds a polite ingester for the TTB Public COLA Registry: daily date-range searches, low request rate, and caching; no CAPTCHA was noted, but this needs re-checking. It also builds a weekly pull of the FOIA permittee CSVs.
- **Days 4–12:** The operator builds the classification (category, first-time applicant, new permittee join), the public pages, both digests, and the Pro CSV. It backfills 12 months to compute trends.
- **Days 12–25:** Scoop pitches and trade-press pitches go out, and the first digests are sent.
- **Days 25–45:** First Pro trials convert, most likely from label printers or design agencies. The first quarterly report (Q4 2026) goes on sale in early January.
- **Estimated days to first sale: ~40.**

### Who does what
- **AI operator:**
  - runs the daily COLA ingest and weekly permittee ingest
  - extracts label text and categorises products
  - spots "first-time applicants"
  - writes the digests, the reports, and the scoop pitches
  - handles SEO pages, affiliate link upkeep, and support
- **Human sponsor:**
  - One-time (~3 h): MoR, newsletter account, domain, and affiliate program applications (spirits affiliates often need a human applicant and an age-gate on the site).
  - Recurring (~30 min/week): approve affiliate payouts and taxes, and handle any editor relationship that needs a human.

### Moat — why not just ask ChatGPT?
ChatGPT doesn't know what TTB approved this week and can't diff it against everything filed before. The value is:
- a **continuously refreshed, deduplicated history** of filings
- the **first-time-applicant signal**, which needs the full history
- the **COLA × permittee join**
- trend reports
- a consumer brand that writers and enthusiasts cite

The data is public-domain US government data, so anyone could copy it; several Apify actors already scrape COLAs. The moat is the curated weekly product, the accumulated history, and the audience. Higher-end competitors exist (e.g. BW166 approvals reports), which validates the market but caps pricing.

### Biggest risks (ideator's own view)
- **Source access fragility.**
  - There is no official COLA API.
  - The registry was returning HTTP 503 during my check, and its TLS setup is unusual.
  - TTB could add rate limits or CAPTCHAs, or change the site, which would stall the core feed.

  Mitigation: a polite, low-volume crawler and a fallback to the date-range search export.
- **Alcohol-marketing and affiliate rules.** Spirits affiliate programs and ad networks require age-gating and responsible-marketing compliance. Some states restrict alcohol e-commerce, which shrinks affiliate income.
- **Lead-quality doubt.** A COLA doesn't mean a product will launch (many filings never reach retail), and many "new brands" are private labels or existing producers. If label printers find the first-time-applicant signal too noisy, Pro churn will be high.

---

### Source sanity-checks (web research, 2026-10-06)
- **SAM.gov Get Opportunities Public API:** public API key from a sam.gov account; about 40 calls/day for new non-federal accounts, about 1,000/day after role approval. Raw data is public domain. https://open.gsa.gov/api/get-opportunities-public-api/
- **CanadaBuys:** tender notice and award CSVs under the Open Government Licence (refreshed every few hours / daily).
- **TED (EU):** open API; CPV 79530000 = translation services.
- **No dedicated "translation/interpreting tender alert" service turned up in search**; only generic aggregators (GovDirections, HigherGov, Starbridge, BidNet).
- **DOL Open Data Portal v4** (apiprod.dol.gov/v4): OSHA inspection and violation datasets, free API key, updated daily. It is the successor to enforcedata.dol.gov.
- **Existing OSHA competition:** multiple Apify "OSHA inspection leads" actors, plus free lookup sites (safetyrecord.org).
- **TTB Public COLA Registry:** no registration needed; images available about 48 h after approval. TTB receives about 200k+ label applications a year (OMB burden estimate about 209k; 95k received by 21 July 2026).
- **TTB FOIA List of Permittees:** weekly CSVs (wineries, distilled spirits plants, importers, wholesalers). Brewers are excluded under IRC §6103.
- **BW166** sells product-approvals reports (a higher-priced competitor). Several Apify COLA scrapers exist.
