# Tech ideas — The Builder

> Research note (2026-10-06): I checked the usual indie channels with web search before choosing these. Chrome Web Store niches are saturated now that AI makes small tools cheap to build. Zillow deal calculators, TpT seller tools, Skool tools, DAT load-board RPM/fraud overlays, AI-crawler WordPress plugins and EU withdrawal-button apps (Woo, Shopify, Wix) each have 3–5+ live competitors. So all three picks below use **smaller marketplaces with built-in buyers**, and two of them have **billing handled by the platform**. Their moat is integration work and approval friction, not prompt cleverness.

---

## T1 — RainCheck for Jobber (weather-risk scheduling app)

- **Persona:** The Builder (ideator-tech)
- **One-liner:** A Jobber App Marketplace integration that checks the forecast for every scheduled outdoor visit. Each evening it emails the owner a "jobs at risk tomorrow and this week" digest, and it gives them a one-screen list to move rained-out visits.
- **Customer:** Owner-operators and small crews (1–10 people) in weather-dependent home services: lawn care, landscaping, pressure washing, exterior painting, window cleaning, gutters, roofing and pool openings. They already pay Jobber about $39–$249/month. They spend time in Jobber's community forum, the r/lawncare and r/pressurewashing subreddits, Facebook groups for their trade, and Jobber's own App Marketplace. Jobber says it serves 100k+ businesses and 400k service pros (May 2026). Its marketplace only recently passed 100 apps.
- **Problem / desire:** "Every rainy morning I'm checking the weather app against my schedule and texting 15 clients one by one." Jobber has manual bulk-move tools but no weather data. The only weather add-on I found is *Jobber++*, a user-built Chrome extension that puts weather emoji on calendar days. It does not show per-job risk, send alerts, or help with rescheduling.
- **Offering:** A SaaS web app connected to Jobber over OAuth through the GraphQL API. It:
  1. Pulls upcoming visits with their geocoded property addresses.
  2. Checks hourly precipitation, wind and temperature forecasts per job location, using the free NWS api.weather.gov in the US and Environment Canada's free GeoMet in Canada.
  3. Applies trade-specific rules, e.g. pressure washing needs above 40°F, painting needs no rain for 24h, mowing needs less than X mm.
  4. Sends an evening digest by email, or SMS later as an add-on.
  5. Offers a "Reschedule plan" screen that proposes the next dry slot per crew and moves visits in one click where the API allows. Otherwise it gives a checklist plus a deep link into each visit.
  6. Optionally sends templated client notices.
- **Price & revenue model:** Subscription through Lemon Squeezy as merchant of record. **$19/mo** (up to 2 crews) or **$39/mo** (unlimited crews plus SMS client notices), with a 14-day free trial. An annual plan at 2 months free.
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Domain (needed for Jobber listing, privacy policy, OAuth redirect) | $12 |
| Jobber Developer Center account | $0 |
| Cloudflare Workers + D1 (free tier), NWS / Env. Canada weather APIs | $0 |
| Lemon Squeezy account | $0 |
| **Total** | **$12** |

### Monthly running costs (excluding operator tokens)
- Hosting on Cloudflare Workers/D1/Cron free tier: $0 up to about 100k requests/day.
- Weather data from NWS and Environment Canada: $0, public domain, no key needed. Rate limits apply, so forecasts are cached per ~2.5 km grid cell.
- Transactional email via Resend free tier (3k/mo): $0.
- SMS, only on the $39 plan, via Twilio: about $0.008/msg, passed through in the plan price.
- Lemon Squeezy fees: 5% + $0.50 per transaction.
- At break-even (16 customers, about $400 gross) running costs are about $30/mo, nearly all payment fees.

### Customer acquisition plan
1. **Jobber App Marketplace listing** is the core channel. Owners browse it inside Jobber. With about 100 apps and no weather category, a "Weather" listing is close to a monopoly for that search intent.
2. Listing copy and screenshots target the words owners use: "rain delay", "weather", "reschedule".
3. Each trial auto-starts after OAuth connect. On day 1 the operator sends a useful "your next 7 days weather risk" email, so the value shows before the trial ends.
4. In-app referral: "Give a month, get a month" for owners in the same trade groups.
5. Owners on the $39 plan send weather-delay notices to clients with a subtle "sent with RainCheck" footer, which gives the product some viral exposure.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Jobber App Marketplace** — publish a polished listing as soon as the app passes review. It has built-in buyer intent and very few apps (about 100), so a new listing is visible on day 1. Expected: first installs within about 1 week of approval.
2. **Jobber Community forum answers** — the human sponsor, in under 30 minutes a week, posts disclosed helpful replies on existing "mass reschedule / rain day" threads with a link to the app. These threads already exist and are the exact pain. Expected: 1–3 weeks.
3. **SEO / programmatic help pages** — e.g. "Jobber rain delay workflow", "how to reschedule lawn care jobs for rain in Jobber" and per-trade weather thresholds. These are long-tail, low-competition queries but on a new domain, so slow. Expected: 2–4 months.
4. **Jobber Technology Partner Program** — apply for co-marketing (newsletter or "new apps" features) once there are 10+ installs. Expected: 2–3 months.

### Path to first sale
- **Days 0–2:** The human creates the Jobber Developer Center account (with 2FA), a Lemon Squeezy store and the domain. The operator scaffolds a Worker with OAuth, a GraphQL client and a D1 schema.
- **Days 3–10:** The operator builds sync, forecast scoring, the digest email and the reschedule screen, and tests against a Jobber tester account.
- **Day ~11:** The app is submitted for Jobber review. Jobber's process is internal testing, then Jobber's own testing and change requests. I estimate 2–3 weeks, but I could not open the docs to confirm this.
- **Day ~30:** Approved and listed. First trials start.
- **Day ~45:** First 14-day trials convert.
- **Estimate: about 45 days to first sale.** That is faster if Jobber review is quick, and up to about 60 days if review asks for changes.

### Who does what
- **AI operator:** builds and deploys the app; writes the listing, help docs and SEO pages; runs forecast cron jobs; monitors errors; handles support email; ships trade-specific rule presets; prepares monthly metrics.
- **Human sponsor:** one-time (about 3 h): Jobber developer account with 2FA, Lemon Squeezy KYC, domain purchase, accepting the Jobber developer terms. Recurring (about 0.5 h/week): occasional disclosed forum posts, approving refunds over $X, and replying to Jobber partner-team emails that need a human.

### Moat — why not just ask ChatGPT?
ChatGPT cannot see the owner's Jobber schedule, cannot watch the forecast overnight, and cannot move visits. The value is persistent OAuth integration, scheduled monitoring and acting inside the tool the owner already uses, which a chat prompt cannot do. The secondary moat is being the first and only weather app in a 100-app marketplace, plus the work of passing Jobber's review. A copycat would need to repeat both.

### Biggest risks (ideator's own view)
- **API capability:** I could not confirm that Jobber's public GraphQL API lets a third-party app reschedule visits. If it cannot, v1 becomes "alert + checklist + deep links". That is still useful, but weaker.
- **Jobber builds it natively.** Weather is an obvious feature for Jobber to add. Mitigation: stay cheap, add trade-specific rules and client notices, and aim for payback within months rather than years.
- **Seasonality:** lawn care and exterior trades slow down a lot from November to March in the US and Canada, and it is October now. Expect a slow first winter (snow-removal rules can partly cover it) and the real ramp in March–April 2027.

---

## T2 — Accela & EnerGov Permit Extractor (Apify Store Actor, pay per result)

- **Persona:** The Builder (ideator-tech)
- **One-liner:** An Apify Store Actor that pulls newly issued building permits from any US jurisdiction running Accela Citizen Access or Tyler EnerGov Citizen Self Service portals and returns them in one clean schema. These are the jurisdictions that existing permit scrapers skip because they have no open-data API.
- **Customer:** Lead-gen agencies and in-house growth people at roofing, solar, HVAC, pool, fence and remodeling companies. Also proptech and data analysts who need permit feeds. They already pay for Apify, Shovels.ai, BuildZoom or ConstructConnect, or pay freelancers on Upwork to scrape their county. They browse the Apify Store, r/webscraping and r/sales, and Clay/n8n automation communities.
- **Problem / desire:** "The permit scrapers only cover big cities with Socrata portals. My market is three counties on Accela, and I'm copying permits by hand." Apify search turns up 10+ building-permit Actors, all built on Socrata, ArcGIS or CKAN open-data APIs. None advertise Accela or EnerGov coverage, even though those portals run permitting for hundreds of US counties and mid-size cities.
- **Offering:** A public Apify Actor (Node/Crawlee). Input is a portal base URL or a jurisdiction picked from a maintained list, a date range, and record-type filters. Output has a normalized schema: permit #, type, description, status, issued date, address, parcel, valuation, contractor, owner where published, and a source URL. A second "watch" mode runs on a schedule and emits only new permits since the last run, which suits Clay, n8n or Zapier lead flows. A public directory page lists jurisdictions that have been verified to work.
- **Price & revenue model:** Apify pay-per-event. **$4.00 per 1,000 permits returned** plus **$0.02 per run start**. Apify bills users and pays the developer 80% of revenue from paid-plan users. Usage by free-plan users is not paid out.
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Apify account (free plan includes monthly platform credit for dev runs) | $0 |
| Domain | $0 (Apify Store page and a GitHub Pages docs site are enough) |
| **Total** | **$0** |

### Monthly running costs (excluding operator tokens)
- Compute and proxy for customer runs: $0 to us. Under pay-per-event, the platform usage cost of each run is set against the event revenue, so the price must cover it. Keeping the Actor HTTP-only (no headless browser where possible) protects margin.
- Our own test and maintenance runs: within free-plan credit, or about $5–10/mo if heavier.
- Apify commission: 20% of revenue.
- Break-even: about $375 gross per month, roughly 90k permits per month across paid users. That is about 10 agencies each pulling daily for 3–5 counties.

### Customer acquisition plan
1. **Apify Store search** is the core channel. People already search "building permits", "permits scraper" and "construction leads", which is why 10+ Actors exist. The listing title and README name the platforms and the covered counties ("Accela, EnerGov — 120+ jurisdictions") so it wins the long-tail searches existing Actors cannot answer.
2. **One SEO-indexed Store page per platform**: separate Actors or README sections for "Accela Citizen Access scraper" and "EnerGov Citizen Self Service scraper". These are exact-match technical queries with almost no competition.
3. **Integration templates**: published Clay, n8n and Make recipes such as "new roofing permits → CRM". These keep users running daily, which produces recurring usage.
4. **Coverage-request loop**: users submit a portal URL they need. The operator verifies and adds it within 48h, then posts it to the changelog.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Apify Store listing** — publishing is self-serve with no long review, the Actor appears in Store search immediately, and the buyers there already pay for runs. Expected: first runs within days, first paid usage in 1–3 weeks.
2. **Apify's own channels** — submit to Apify's Store newsletter and community showcase, and enter any open Apify developer challenges or bounties. Apify actively promotes new pay-per-event Actors. Expected: 2–4 weeks.
3. **Answer existing demand threads** — the sponsor makes disclosed, non-spammy replies to Upwork-style "scrape Accela permits" asks and r/webscraping questions about Accela. Expected: 2–6 weeks.
4. **Programmatic docs site** (GitHub Pages): one page per covered jurisdiction ("Maricopa County permits data export"). Slow on a new domain. Expected: 3–6 months.

### Path to first sale
- **Day 0:** The human creates the Apify account and completes payout KYC (PayPal or bank).
- **Days 1–6:** The operator builds the Accela ACA module, reverse-engineering its ASP.NET search postbacks, and the EnerGov CSS module, which uses its JSON search endpoints. The operator verifies 20–30 jurisdictions and writes the README, input schema and pricing.
- **Day 7:** Published to the Store.
- **Days 7–21:** First paid-plan users run it, and the first pay-per-event revenue registers.
- **Estimate: about 14–21 days to first sale**, with first cash at the next monthly payout cycle. Payout minimums are $20 by PayPal and $100 by bank.

### Who does what
- **AI operator:** builds and maintains the scrapers; runs a nightly self-test against every listed jurisdiction and auto-hides broken ones; adds jurisdictions on request; writes README, changelog and integration recipes; answers Apify issue threads and support messages.
- **Human sponsor:** one-time (about 1–2 h): Apify account, payout and tax info. Recurring (about 0.25 h/week): an occasional disclosed community reply, and reviewing the monthly payout.

### Moat — why not just ask ChatGPT?
ChatGPT cannot reliably page through hundreds of stateful ASP.NET government portals on a schedule and return deduplicated, normalized rows. The value is maintained scraping infrastructure across many portals, a nightly-verified coverage list, and the "only new since last run" state. These are boring maintenance moats that grow with every jurisdiction added. Apify's billing and Store traffic also mean no checkout and no audience are needed.

### Biggest risks (ideator's own view)
- **Technical blockers:** some Accela agencies enable reCAPTCHA or aggressive rate limiting on search. Those jurisdictions get dropped, and the verified list must stay honest. Legal exposure is moderate: these are public records, but the human runner carries risk if an agency objects. Mitigations: obey robots.txt where present, rate-limit politely, and pull no personal data beyond what the portal publishes.
- **Free-plan leakage and copycats:** usage by Apify free-plan users earns nothing. Competitors on Apify move fast, and other permit-Actor authors could add Accela within weeks of seeing traction.
- **Thin per-unit revenue:** reaching $300/mo net needs about 10 steady daily-run customers. Without repeat users it stays a $20–100/mo hobby.

---

## T3 — TipSplit for Clover (tip-pool calculator inside the Clover App Market)

- **Persona:** The Builder (ideator-tech)
- **One-liner:** A low-cost Clover App Market app for cafés, bakeries, bars and quick-service shops. It turns Clover's own shift hours and card tips into a fair, documented weekly tip pool: hours- or points-based, with manager exclusion, cash-tip entry and a payroll-ready CSV.
- **Customer:** Independent food-and-beverage owners and managers on Clover POS, typically 1–3 locations and 4–25 staff, who pool tips. Today they do it in a spreadsheet every week. They already pay Clover for the POS and buy add-ons inside the Clover App Market. They hang out in r/barista, r/restaurantowners and coffee-shop owner Facebook groups, and they get app recommendations from their Clover reseller (ISO).
- **Problem / desire:** "Every Sunday I export tips and the timeclock, paste them into a spreadsheet, and pray I didn't mess up someone's share." The full solution, TipHaus, costs **$99/location/mo plus a $300 setup fee** on Clover. That is overkill for a coffee shop that just needs the math done right and a record of it.
- **Offering:** A Clover web app connected through Clover OAuth and REST API: employees, shifts and payments with tip amounts. Features:
  - Pool rules: by hours, by role points, or equal split; daily or weekly pools; excluded roles (managers and owners, consistent with FLSA tip-pool rules); an optional credit-card-fee deduction toggle.
  - Cash-tip entry per shift.
  - Per-employee statements by email or print.
  - CSV export formatted for Gusto, ADP, QuickBooks Payroll and Square Payroll.
  - An immutable history log, useful if there is ever a wage dispute.
- **Price & revenue model:** Subscription billed by Clover through Clover App Market billing, so no merchant of record is needed. **$14.99/location/month** with a 30-day free trial. Developer share is 70%, about $10.49 net per location. Break-even is about 29 locations, and the stretch target of $1k is about 96.
- **Physical items required?** No. It runs on the merchant's existing Clover device and web dashboard.

### Upfront capital
| Item | Cost |
|---|---|
| Clover developer account + sandbox | $0 |
| Domain (privacy policy, support site, OAuth redirect) | $12 |
| Cloudflare Workers + D1 free tier | $0 |
| **Total** | **$12** |

### Monthly running costs (excluding operator tokens)
- Hosting on Cloudflare free tier: $0 at this scale.
- Email statements via Resend free tier: $0 up to 3k/mo.
- Clover's 30% revenue share is taken before payout, so there are no separate payment-processing fees.
- Effectively $0 fixed cost. Margin is the 70% share.

### Customer acquisition plan
1. **Clover App Market search and categories** ("Employees", "Restaurant/Food & Beverage") are the core channel. Merchants find and install apps inside their Clover dashboard. Evidence the channel works: a Flippa listing for a Clover cash-discount app reports about 25k paying merchants and about $87k/mo profit, reached through organic growth with no marketing spend.
2. **Price positioning against TipHaus**: "Tip pooling for small shops — $14.99, no setup fee". Merchants searching "tip" in the App Market see both.
3. **Clover reseller and ISO channel**: a one-page partner sheet that resellers can hand to café clients. The sponsor emails a handful of Clover resellers who publicly list app recommendations. This is a few personal emails, not bulk outreach.
4. The free trial includes a back-calculated "last 4 weeks of tip pools" on day 1, so value shows immediately.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Clover App Market listing** — built-in buyer traffic from merchants already in the dashboard, with billing included. Expected: first installs within 1–2 weeks of approval.
2. **SEO help content on our domain** — "how to split tips by hours worked (with calculator)", "is tip pooling with managers legal", plus a free web tip-split calculator that links to the Clover app. These are high-intent queries, but slow on a new domain. Expected: 2–4 months.
3. **Clover reseller partnerships** — 5–10 personal emails or LinkedIn messages from the sponsor to resellers who publish "best Clover apps" lists. Expected: 3–8 weeks.
4. **Community answers** — disclosed, helpful sponsor replies in r/restaurantowners and r/barista threads about tip-pool spreadsheets, only where relevant. Expected: 2–6 weeks.

### Path to first sale
- **Days 0–3:** The human registers the Clover developer account (business info, W-9 or tax and payout details) and buys the domain. The operator scaffolds OAuth and sandbox data.
- **Days 4–14:** The operator builds the pool engine, cash-tip UI, statements, CSV exports and history log, and tests on sandbox merchants with synthetic shifts and payments.
- **Day ~15:** Submitted for Clover App Market approval. I estimate 2–4 weeks; Clover reviews apps before listing.
- **Day ~35:** Listed. The first installs start the 30-day trial.
- **Day ~65:** First paid conversion, billed by Clover.
- **Estimate: about 60–65 days to first sale.** That drops to about 50 days with a 14-day trial instead of 30. I'd start with 30 days to capture a full payroll month, then test 14.

### Who does what
- **AI operator:** builds, hosts and maintains the app; writes the listing, help docs and SEO calculator page; handles support email; watches Clover API changes; prepares a monthly churn and installs report.
- **Human sponsor:** one-time (about 3 h): Clover developer account and payout and tax setup, domain, accepting the developer agreement, and sitting through any approval correspondence that needs a human. Recurring (about 0.5 h/week): occasional reseller emails and reviewing any wage-dispute-related support ticket.

### Moat — why not just ask ChatGPT?
ChatGPT can do tip math if you paste in the numbers. Exporting, cleaning and pasting the numbers every week is exactly the chore the owner wants to stop doing. The app pulls hours and tips straight from Clover, applies saved rules automatically, keeps an audit trail and produces payroll-format exports. The value is persistent state plus workflow integration, and the defensible part is the Clover listing and approval plus a price far below the only established competitor.

### Biggest risks (ideator's own view)
- **Liability:** wrong tip calculations can become wage claims, and the human sponsor carries that. Mitigations: clear "calculator, owner approves" terms, an exportable audit log, and conservative defaults that exclude managers from the pool.
- **Data gaps:** many small shops don't use Clover's timeclock, so there are no shift hours. That needs a manual-hours fallback and reduces the "automatic" value. Some Clover plans may restrict the employee and shift features the app depends on.
- **Channel dependence:** Clover's 30% cut, approval timing and possible copycats or TipHaus price cuts. Merchants also churn when they leave Clover.

---

Sources checked (2026-10-06): Jobber community "mass reschedule" thread and Jobber++ Chrome extension (search result summaries); Jobber 100-integration milestone (techintelpro.com, May 2026) and Jobber 100k businesses / 400k pros (getjobber.com/llm-info); Apify Store permit Actors (apify.com search results: burn98, xtracto, maydit, DevilScrapes, etc.); Apify pay-per-event monetization (docs.apify.com, godberrystudios.com 2026 playbook); Clover monetization docs (docs.clover.com/docs/monetizing-your-apps: 70% developer share, Clover-handled billing); Flippa listing 13364296 (Clover cash-discount app, ~25k merchants, ~$87k/mo profit); TipHaus pricing (learn.tiphaus.com: $99/location/mo on Clover + $300 setup). Saturation checks: Zillow investment-calculator extensions, TpT seller extensions, Skool extensions, DAT load-board extensions (Lane Edge, Load Companion, Power Xtension, LoadConnect), WordPress AI-crawler plugins, EU withdrawal-button apps on WooCommerce, Shopify and Wix. Not verified: Jobber review timelines and whether its API can edit visits (docs returned 403), Clover approval timelines, and Accela CAPTCHA prevalence.
