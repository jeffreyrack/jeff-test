# Writing ideas — The Wordsmith

_Run date: 2026-10-06. I checked comparables and pricing with WebSearch where I could; the sources are listed at the bottom. Any figure marked "verify" is from memory and still needs checking._

---

## W1 — Bid Brief: Facilities Services (federal janitorial & grounds bids, in plain English)

- **Persona:** The Wordsmith (writer)
- **One-liner:** A twice-weekly paid newsletter for small janitorial and landscaping companies. Each issue lists every new federal solicitation in their trade, and the AI reads the 40-page Statement of Work so the owner doesn't have to.
- **Customer:** Owners of small (1–50 employee) commercial cleaning and grounds-maintenance companies, many of them new to government contracting. They watch the YouTube "government contracting for janitorial companies" gurus, buy $300–$2,000 courses, sit in GovCon Facebook groups, and use their local APEX Accelerator (the former PTAC). They already pay for QuickBooks and Jobber/Swept, and some pay for courses. They do **not** pay for GovTribe ($1,350+/yr) or HigherGov ($500+/yr), which are priced for BD teams.
- **Problem / desire:** "SAM.gov alerts send me 30 junk notices a day. I have to open every PDF to find out the square footage, how often they want it cleaned, whether there's a site visit, and whether it's even a small-business set-aside. By the time I figure it out the site visit is over."
- **Offering:** A digest emailed Tuesday and Friday. It covers every new or amended solicitation and sources-sought notice under NAICS 561720 (janitorial) and 561730 (landscaping), grouped by state. Each entry is a 6-line card: agency and location, set-aside type, response deadline, site-visit date, a scope summary pulled from the SOW (sq ft, frequency, special requirements such as floor care or snow removal), the Service Contract Act wage-determination note, and the prior award amount and incumbent from USAspending.gov. There is also a "Deadline in ≤7 days" section and a monthly "what got awarded and for how much" recap for pricing intelligence. A free weekly edition carries only the 5 best opportunities.
- **Price & revenue model:** Subscription at $19/month or $149/year, with the free tier as the funnel. At 20 paid subscribers it breaks even ($300/mo after fees). The stretch target is about 60 subscribers.
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Domain (optional; Substack subdomain works on day 1) | $12 |
| Substack account (paid subscriptions built in, no platform fee upfront) | $0 |
| SAM.gov public data extract + USAspending API | $0 |
| **Total** | **$12** |

### Monthly running costs (excluding operator tokens)
- Substack takes 10% of paid revenue, plus Stripe at about 2.9% + $0.30 per charge.
- Hosting and data: $0. Data comes from the SAM.gov daily public opportunities extract, the free USAspending.gov API and a GitHub Actions cron.
- Optional: about $0–$5 for parsing scanned PDF attachments, if needed.

### Customer acquisition plan
1. Publish every free issue on Substack. Each one is a public, indexable page with a state-by-state list. Substack's recommendation network and search give some built-in discovery.
2. Build a small static site (Cloudflare Pages) with one evergreen, regularly updated page per state, e.g. "Open federal janitorial contracts in Texas, updated twice weekly". These are long-tail, low-competition queries, and freshness is a real ranking signal for this kind of query.
3. Each free issue ends with a "you missed 23 more opportunities this week" teaser and an upgrade link.
4. Write a few genuinely useful guides, such as "How to read a federal janitorial SOW" and "What the Service Contract Act wage determination means for your bid". These earn links and newsletter signups.
5. Retention comes from consistency. Two issues a week, every week, is the trust product.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **APEX Accelerator counselors (human-sent intro, one-time).** The sponsor emails 10–15 APEX Accelerator offices (about 90 exist, and they are public and free) offering the free edition as a resource for their janitorial and landscaping clients. These are warm, relevant gatekeepers whose job is pointing small firms at opportunities. This is personal outreach, not mass cold email. Expected speed: 1–3 weeks.
2. **Substack discovery and cross-recommendations.** Ask 3–5 small GovCon Substacks and newsletters to swap recommendations. The operator can draft the asks; the sponsor sends them. Expected speed: 2–4 weeks.
3. **Comment and value posts by the human sponsor** in 1–2 GovCon or janitorial-business communities, sharing a free "this week's 5 best bids" post as a human, about 20 min/week, for 4 weeks only. Bots can't do this under platform rules. Expected speed: 1–4 weeks.
4. **Per-state SEO pages.** Expected speed: 2–4 months. This is long-tail and slow, but it compounds.

### Path to first sale
- **Days 0–3:** The sponsor sets up Substack with Stripe and buys the domain. The operator builds the pipeline: daily extract, then NAICS filter, then fetch attachments, then LLM summary cards, then a USAspending lookup for the incumbent and prior value.
- **Days 4–10:** Publish 3 back-filled free issues so the archive isn't empty. Launch the state pages.
- **Days 7–14:** The sponsor sends the APEX intros and makes the community posts.
- **Days 14–30:** Free list grows to about 100–200. Turn on paid at a launch price ($12/mo founding rate).
- **Estimate:** first sale in **~30 days**. Getting 20 paid subscribers (break-even) is likely a 3–5 month effort.

### Who does what
- **AI operator:** Build and run the data pipeline. Write and QA every issue, spot-checking cards against the source PDFs. Publish the twice-weekly issues, maintain the state pages and guides, answer reader email, and draft the outreach and recommendation-swap messages.
- **Human sponsor:** One-time (~3 h): Substack + Stripe KYC, domain, SAM.gov/login.gov account if an API key is needed for attachments, and the APEX intro emails. Recurring (~0.5–1 h/week): community posting in the first month, skimming one issue a week, payouts.

### Moat — why not just ask ChatGPT?
ChatGPT doesn't watch SAM.gov twice a week, and it can't tell you which of today's 40 notices is a 20,000 sq ft small-business set-aside with a site visit on Thursday. The value is the **monitoring, filtering and SOW extraction**, done on schedule. A reader could build this with code, but this buyer is a cleaning-company owner, not a developer. Price is the second moat: an incumbent tool costs $500–$1,350/yr and does far more than this buyer needs. Weak point: SAM.gov's own free saved-search alerts exist. Our edge over them is the summarised scope and the incumbent/price context, so that is what every issue must sell.

### Biggest risks (ideator's own view)
- **Willingness to pay.** Small contractors are price-sensitive and many never win a bid. Churn could be high after 2–3 months with no win. Mitigation: annual pricing and the award-price recaps, which are useful even when you lose.
- **Data access friction.** SAM.gov API keys for non-federal users have tight daily quotas (roughly 10–1,000 calls depending on approval). Attachments may need the API or page fetches. The daily public extract covers the notice metadata. Verify quotas before building.
- **Accuracy and trust.** One wrong deadline in a card destroys trust. Every card must link the source notice and carry an "always confirm on SAM.gov" line. Low legal exposure, because this is information, not bid advice.

---

## W2 — Florida HOA Board Letter & Notice Kit (Chapter 720-aware, plain English)

- **Persona:** The Wordsmith (writer)
- **One-liner:** A fill-in-the-blanks pack of ~40 letters, notices and checklists for volunteer board members of self-managed Florida HOAs, with each template mapped to the Chapter 720 step it supports (including the 2024 HB 1203 fining and hearing changes).
- **Customer:** Volunteer HOA board presidents, secretaries and treasurers in small self-managed Florida HOAs (roughly 20–300 homes) with no management company. They search Google for "HOA violation letter template", buy on Etsy, and sit in Nextdoor and Facebook HOA board groups. They already pay for PayHOA or similar dues software, and sometimes for a one-hour attorney consult ($250–$400).
- **Problem / desire:** "I'm a volunteer. I just got told we have to do director education and that our fines process changed. I need to send a violation letter and a hearing notice and I don't want to get it wrong and have the fine thrown out."
- **Offering:** A digital download in two formats: editable DOCX/Google Docs files plus a 25-page PDF guide. It contains:
  - A violation notice sequence: courtesy letter, formal notice, notice of fining-committee hearing, and hearing-outcome letter.
  - Meeting notices (board, annual and budget) and an agenda and minutes template.
  - Records-request response letters, an ARC (architectural review) approval/denial pack, welcome and estoppel cover letters, and a delinquency reminder series (friendly versions, explicitly **not** collection or lien letters).
  - A one-page "which step am I on" flowchart for each process, citing the statute section in plain English.
  - A free bonus: a "What changed in 2024–2026" one-pager.

  Version 2 adds a Texas kit (Property Code ch. 209, with its certified-mail notice and hearing rules) using the same template engine.
- **Price & revenue model:** One-time purchase at $39 for the full kit, or $12–$15 for single-process mini-packs (e.g. the violation letter set alone) to capture Etsy search traffic. An annual "law-change update" email goes to buyers, and the operator adds an updated version each July after the legislative session as a $15 upgrade. Break-even is about 9 full kits or 25 mini-packs a month.
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Etsy shop setup fee (one-time for new US sellers, verify current) | ~$15 |
| Etsy listing fees (10 listings × $0.20) | $2 |
| Gumroad or Lemon Squeezy store for direct sales | $0 |
| Domain (optional for v1) | $0–$12 |
| **Total** | **~$17–$29** |

### Monthly running costs (excluding operator tokens)
- Etsy: $0.20 per renewal or sale listing, 6.5% transaction fee and about 3% + $0.25 payment processing. Offsite-ads fee only applies if a sale comes from Etsy ads.
- Lemon Squeezy: about 5% + $0.50 per sale (verify). Gumroad: 10% + $0.50 direct, higher via Discover.
- Hosting: $0, using Cloudflare Pages for the landing page and SEO articles.

### Customer acquisition plan
1. **Etsy as the primary storefront.** It has buyer-intent search for "HOA letter template", "HOA violation notice" and "HOA meeting minutes", which have low supply relative to wedding and resume templates. List 1 full kit and 6–9 single-process mini-packs, each targeting a different search phrase, with honest "created with AI assistance, reviewed against statute text" disclosure under Etsy's creativity standards.
2. **Gumroad or Lemon Squeezy** for direct links from SEO content, where margin is higher.
3. **SEO articles** on a small site, linking to the kit: "Florida HOA fining process step by step (2026)", "How to write an HOA violation letter in Florida", "What HB 1203 changed for small HOAs".
4. **Annual law-update loop.** Each July 1 the operator reads the session's HOA bills, updates the kit, emails past buyers the paid upgrade and refreshes the listings ("2027 edition").

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Etsy search** — 10 keyword-targeted listings plus 2–3 Pinterest-style preview images per listing (image API, ~$1 total). Etsy's built-in buyer traffic works with zero audience. Expected speed: first views in days, first sale in 1–4 weeks if the listings rank.
2. **Gumroad Discover / Lemon Squeezy** — marketplace exposure plus a link-in-bio for the SEO site. Expected speed: weak but non-zero, 2–6 weeks.
3. **Human-sponsor answers in HOA board forums.** The sponsor posts helpful, non-spammy answers about the fining process in 1–2 HOA board communities, about 20 min/week, linking only where allowed. Expected speed: 2–4 weeks.
4. **SEO articles** — "Florida HOA violation letter" style queries. Expected speed: 3–6 months.

### Path to first sale
- **Days 0–2:** The sponsor opens the Etsy shop and Lemon Squeezy store (KYC). The operator researches Chapter 720 (current statute text from the Florida Legislature site) and outlines the kit.
- **Days 3–7:** The operator writes the templates, guide and flowcharts, builds the DOCX/PDF files and preview images, and writes the listings.
- **Days 7–8:** Listings go live, 10 in total.
- **Days 8–30:** The operator tunes titles and tags weekly using Etsy stats and adds 2 mini-packs a week based on which searches get views.
- **Estimate:** first sale in **~14–21 days**. This is the fastest of the three ideas because of Etsy's built-in demand. Revenue is lumpy and seasonal (it peaks around annual-meeting season, January–March).

### Who does what
- **AI operator:** Research statutes, write and format every template, make the preview images, write the listings and SEO articles, do the weekly listing optimisation, answer buyer messages through the Etsy/Lemon Squeezy inbox, and run the annual law-change refresh.
- **Human sponsor:** One-time (~2–3 h): Etsy and Lemon Squeezy KYC, approve the disclaimer wording, and ideally pay a Florida HOA attorney for one review of the kit. That review is optional, and its ~$250–$400 is outside the $100 cap, so it would come from early revenue, not upfront. Recurring (~0.5 h/week): Etsy messages that need a human and payouts.

### Moat — why not just ask ChatGPT?
A board volunteer *can* ask ChatGPT for "an HOA violation letter". They'll get a generic letter that may miss the Florida-specific steps: written notice, the 14-day hearing notice, the fining committee's independence, the no-fine-if-cured-before-hearing rule and the $1,000 lien threshold. Our moat is that **the sequence is the product**: a mapped process plus statute-checked wording and a yearly update. The other moat is distribution. The buyer's habit is to search Etsy or Google for a "template", not to prompt a chatbot. The moat is moderate, not strong. AI output isn't copyrightable, so the kit can be copied, but the annual update and Etsy reviews are what compound.

### Biggest risks (ideator's own view)
- **Legal-adjacent liability.** If a board uses a template and loses a fine dispute, the sponsor could get an angry customer or a refund demand. Mitigations: prominent "not legal advice; your declaration and bylaws control; consult an attorney" language, no collection, lien or foreclosure letters, statute citations so boards can verify, and ideally one paid attorney review once revenue allows.
- **Etsy policy and competition.** AI-assisted digital templates must be disclosed, and listing rules or search ranking could change. Competition comes from free templates (Condo Control, PayHOA blogs) and paid kits such as the "HOA Board Compliance Kit" on Payhip and the HOA Board Studio SaaS.
- **Small, seasonal market.** Self-managed Florida HOAs are a finite pool. The Texas version (v2) and other big-HOA states (Georgia, North Carolina, Arizona) are the expansion path, each needing a new statute review.

---

## W3 — Grant Deadline Desk: [State] (monthly foundation and state grant calendar for small nonprofits)

- **Persona:** The Wordsmith (writer)
- **One-liner:** A verified, monthly-refreshed calendar of every open grant with a deadline in the next 90 days from foundations, community foundations, corporate giving programs and state agencies in **one state**, sold to small nonprofits that can't afford Instrumentl. The pilot state is Ohio or North Carolina.
- **Customer:** Executive directors, development directors and volunteer grant writers at small nonprofits (budget under $1M) in one state, plus freelance grant writers who serve them. They read their state nonprofit association's newsletter, attend Candid/Foundation Center webinars, and use free Candid/GuideStar profiles. Some pay for GrantStation through TechSoup ($150–$199/yr). Most can't justify Instrumentl, which costs $299/month and up as of 2026.
- **Problem / desire:** "Every foundation posts its deadlines on its own website, in a different format, and changes them every year. I spend hours a month hunting for what's open, and I still miss the community foundation cycle by a week."
- **Offering:** A paid web calendar (sortable and filterable by deadline, cause area, county and award size) behind a license-key login, plus a monthly email with "new this month", "closing in 30 days" and "funders that just reopened" sections. Each entry gives the funder, program, deadline, award range, eligibility in one plain-English line, a link to the official RFP and a "last verified" date. Freelance grant writers get a CSV export. A free monthly teaser edition lists the 10 biggest deadlines.
- **Price & revenue model:** $15/month or $99/year per organisation, and $199/year for a "consultant" license with CSV export. Break-even is about 35 annual subscribers, or a mix including a handful of consultant licenses. Adding a second state reuses the same machinery.
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Domain | $12 |
| Lemon Squeezy (subscriptions + license keys) | $0 |
| Cloudflare Pages + Workers + D1 free tier | $0 |
| Beehiiv Launch plan (free list ≤2,500) for the free edition | $0 |
| **Total** | **$12** |

### Monthly running costs (excluding operator tokens)
- Lemon Squeezy: about 5% + $0.50 per transaction (verify).
- Transactional email to paid users (Resend or similar free tier, about 3,000 emails/month): $0 at this scale.
- Hosting: $0 on free tiers. Data sources are free: funder websites, state agency grant portals, and the ProPublica Nonprofit Explorer / IRS 990-PF data for finding funders.

### Customer acquisition plan
1. **Build the funder universe once.** Use 990-PF filings and community foundation lists to identify the ~200–400 funders in the state that accept unsolicited proposals, then crawl their grant pages monthly for deadline changes. The calendar is only as good as its coverage, so that is the product.
2. **Monthly free edition plus a public "top 10 deadlines this month" page.** This is fresh and specific ("Ohio grant deadlines November 2026"), ranks on long-tail queries, and grows the free list.
3. **Upgrade path.** Free readers see 10 of about 120 deadlines, and the paid calendar shows all of them with filters.
4. **Annual renewal hooks:** a Q4 "grant season planning calendar" PDF for annual subscribers and a January "funders who changed their cycle this year" report.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **State nonprofit association and regional associations of grantmakers.** The sponsor offers the free edition, or a member discount, to the state nonprofit association's newsletter or resource page. These organisations exist to share resources with exactly this audience. Expected speed: 2–6 weeks, depending on their newsletter cycle.
2. **Freelance grant writers as multipliers.** The sponsor personally emails 10–20 freelance grant writers in the state who list themselves on public directories (a relevant, individual B2B offer with opt-out, not bulk) with a free 30-day consultant license. Each writer serves 3–10 nonprofits. Expected speed: 2–4 weeks.
3. **Public library and Candid Funding Information Network partners.** Libraries keep grant-resource pages for local nonprofits, so offer them a free library license. This earns links and referrals. Expected speed: 4–8 weeks.
4. **SEO deadline pages** per month and per cause ("arts grants in Ohio with deadlines this fall"). Expected speed: 3–6 months.

### Path to first sale
- **Days 0–3:** The sponsor sets up Lemon Squeezy, the domain and beehiiv. The operator picks the pilot state, after checking which state's association does *not* already publish a free grant calendar.
- **Days 3–14:** The operator builds the funder list from 990-PF data and community foundation directories, crawls and verifies about 150 open opportunities, and builds the calendar site with license-key gating.
- **Days 14–21:** Publish the first free edition and public top-10 page. The sponsor sends the association, library and grant-writer emails.
- **Days 21–45:** Free list reaches about 150–300. Run a launch offer of $79 for the first year.
- **Estimate:** first sale in **~40–50 days**. This is the slowest of the three because of the build and trust ramp, but it has the best retention and annual-prepay profile.

### Who does what
- **AI operator:** Discover funders from 990 data, run the monthly crawl and verify every deadline, write the one-line eligibility summaries, maintain the site and license gating, write the monthly emails and SEO pages, handle "you missed a funder" reader submissions and do support.
- **Human sponsor:** One-time (~3–4 h): payment KYC, domain, beehiiv, and the association, library and grant-writer outreach emails. Recurring (~0.5–1 h/week): occasional follow-ups with partner organisations and payouts.

### Moat — why not just ask ChatGPT?
ChatGPT can't tell you which Ohio community foundations open their spring cycle on February 3 *this year*. Deadlines change annually, live on hundreds of separate websites, and are frequently wrong in training data and search snippets. The moat is the **funder universe plus a monthly verification crawl plus a "last verified" date on every row**, which is exactly the "time saved and trust" product readers pay for. Instrumentl and GrantStation cover this, but at 3–30x the price and without state-level depth on small local funders. The data compounds: year 2 is cheaper to produce than year 1 because the funder list already exists.

### Biggest risks (ideator's own view)
- **Coverage gaps kill trust.** If a subscriber's favourite local funder is missing, they churn. Mitigations: publish the coverage list openly, add a "suggest a funder" form, and fix gaps within a week.
- **Free substitutes.** Some state associations, community foundations and libraries publish free grant lists. Pilot in a state where these are thin, which the operator checks before choosing. Grantable's free tier and GrantStation via TechSoup also compete on price.
- **Slow B2B/nonprofit buying.** Some nonprofits need board or ED sign-off even for $99. Annual billing, invoices (Lemon Squeezy supports them) and the consultant license, where the freelancer pays personally, reduce the friction.

---

## Sources checked (2026-10-06)
- beehiiv pricing 2026 (paid subscriptions require the Scale plan from ~$43/mo, which is why W1 uses Substack and W3 uses Lemon Squeezy): https://www.sendx.io/blog/beehiiv-pricing-plans-costs-alternatives-for-newsletter-publishers-2026
- GovTribe/HigherGov pricing (GovTribe Launch $1,350/yr; HigherGov from $500/yr): https://samsearch.co/blog/govtribe-alternatives-and-competitors-in-2026 , https://highergov.com/alt/govtribe
- SAM.gov API quotas for non-federal keys, and third-party scrapers showing the data is reachable: https://www.cleat.ai/developers/sam-gov-api , https://apify.com/bigjoecoding/sam-gov-set-aside-contract-radar
- Florida HB 1203 (2024) HOA fining and hearing changes: https://www.floridacondohoalawblog.com/2024/06/25/hb-1203-effective-july-1-2024-changes-hoa-fining-requirements/ , https://www.payhoa.com/the-guide-to-florida-hoa-laws/
- Texas Property Code §209.006 notice requirements: https://texas.public.law/statutes/tex._prop._code_section_209.006
- HOA template competitors (HOA Board Studio, HOA Board Compliance Kit on Payhip, Condo Control free templates): https://www.capterra.co.uk/software/1108644/HOA-Board-Studio , https://payhip.com/b/V8Nm4 , https://condocontrol.com/condo-homeowners-association-templates/
- Instrumentl ($299/mo+ as of 2026) and GrantStation ($199/yr via TechSoup) pricing: https://aitoolsbakery.com/blog/instrumentl-alternatives/ , https://grantable.co/best-instrumentl-alternatives
- I considered and dropped a short-term rental regulation digest because the niche is crowded with free newsletters (RedAwning, OwnerRez, Rental Scale-Up, STR Update): https://redawning.com/pm/post/short-term-rental-regulation-updates-september-2026
