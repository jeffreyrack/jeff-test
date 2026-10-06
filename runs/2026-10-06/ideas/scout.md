# Demand-first ideas — The Scout

Research date: 2026-10-06. Evidence was gathered with live web search. Etsy and some Fiverr pages block direct fetches, so a few prices and sales counts come from search-result snippets. Those are labelled "(snippet)" and should be spot-checked by hand before launch.

Ideas I checked and dropped because demand is already met cheaply or free: bank-statement PDF→CSV (many free AI converters now exist), PDF→fillable-form (PDF2Fill, Formester and Sejda are free), supplier-sheet→Shopify CSV (ColdPress, Portaim and DataMorph apps exist), POD trademark checkers (CreatorShieldAI, Merch Informer, PODCS), and TV Time migration (the shutdown was on 2026-07-15, Trakt now has a native importer, and the window has closed).

---

## S1 — Done-For-You Airbnb Guidebook ("send us your listing, get a finished guest guide")

- **Persona:** The Scout (demand-first)
- **One-liner:** A fixed-price, AI-fulfilled custom guest guidebook for short-term-rental hosts. The buyer gets a print-ready PDF, a mobile web guide on a permanent URL, and a QR-code sign. Local recommendations are researched for the property's address. It is sold on Etsy, where hosts already shop for templates.
- **Demand evidence:**
  - Etsy: "airbnb welcome book" gets about 1,000 Etsy searches/month (RankHero, Apr 2026). The median template price is $8, and 63% of listings are under $10 (snippet). Top templates have 4.8★ reviews that praise "easy to use", which shows hosts buy, but every one of these is a blank Canva template the host still has to fill in. ([RankHero](https://www.rankhero.com/keywords/airbnb-welcome-book), [Etsy example](https://www.etsy.com/listing/1453313943/airbnb-welcome-book-template-house-host))
  - Fiverr: many gigs sell the *done-for-you* version. They are typically $50–$100 basic, $100–$200 done-for-you, and $400–$600 premium (snippet), which proves hosts pay to avoid filling the template themselves. ([Fiverr: cdub0619](https://fiverr.com/cdub0619/create-a-custom-airbnb-welcome-book), [Fiverr: pine_n_pixal](https://fiverr.com/pine_n_pixal/create-a-custom-airbnb-guest-welcome-guide), [Fiverr: sahl01](https://fiverr.com/sahl01/digital-airbnb-welcome-book))
  - SaaS incumbents charge a recurring fee: Touch Stay from $19/month per property, and Hostfully Guidebook about $89–$129/year. ([STR Specialist review](https://strspecialist.com/reviews/touchstay-guest-guidebook-review), [Uplisting comparison](https://www.uplisting.io/blog/best-guidebook-solutions-vacation-rentals)). Hosts with 1–3 properties resent paying a subscription for what is mostly a static page.
- **Customer:** Independent STR hosts with 1–5 properties (Airbnb, VRBO). They hang out on r/airbnb_hosts, BiggerPockets, and STR Facebook groups, and they shop Etsy for welcome books, house signs and printables. They already pay for Canva templates ($5–$15), PriceLabs/Wheelhouse, cleaning apps, and sometimes Touch Stay or Hostfully.
- **Problem / desire:** "I bought the template and never filled it in." "Guests message me the Wi-Fi password at 11pm." They want fewer repetitive guest questions and better reviews, without spending a weekend in Canva or paying monthly.
- **Offering:** The buyer completes a 10-minute intake form: listing URL, address, Wi-Fi, check-in/out steps, house rules, appliance quirks, parking, trash day, and favourite spots (optional). Within 48h the AI delivers:
  1. A branded 12–20 page PDF guidebook, both print-ready and as an interactive PDF with clickable links.
  2. A hosted mobile web guide at `guides.<domain>/<slug>`, ad-free and kept up for the life of the business.
  3. A printable QR-code sign (PDF) linking to the web guide.
  4. A researched "Local favourites" section of about 15–25 places (food, coffee, groceries, pharmacy, urgent care, attractions). Each place is verified open via web search and includes a map link.

  One free revision round is handled by a form, not chat.
- **Price & revenue model:** One-time prices. Standard (1 property) is $39; Premium is $69 and adds a second language plus extra pages (house manual for hot tub, pool, etc.). Optional "Keep it fresh" is $29/year: the AI re-verifies local listings each quarter and the host can edit through a form. Multi-property bundle: 3 for $99.
- **Physical items required?** No. The QR sign is a PDF the host prints.

### Upfront capital
| Item | Cost |
|---|---|
| Etsy one-time shop setup fee (charged to new sellers in many regions) | $15 |
| Etsy listing fees (10 listings × $0.20) | $2 |
| Domain for hosted guides + intake form | $12 |
| Image API for cover art and icons during setup (~100 images) | ~$5 |
| **Total** | **~$34** |

### Monthly running costs (excluding operator tokens)
- Hosting (Cloudflare Pages + Workers + D1/KV free tier): $0
- Listing renewals: ~$1–2 (each sale auto-renews its listing for $0.20)
- Etsy fees per sale: 6.5% transaction fee, plus payment processing of ~3% + $0.25, plus a 15% Offsite Ads fee only on orders that come from Etsy's offsite ads. That is ~$4.30 on a $39 order, or up to ~$10 with offsite ads.
- Image generation: ~$0.10–$0.40 per order
- Email sending (Resend/Postmark free tier): $0
- Total at 10 orders/month: about $50 in fees, all variable.

### Customer acquisition plan
1. Hosts search Etsy for "airbnb welcome book", "airbnb guidebook", "vacation rental house manual" and similar terms.
2. Our listing shows up as the **done-for-you** option. The thumbnail reads "We fill it in for you — local guide researched for your address," next to a sea of blank templates.
3. Purchase → Etsy delivers a digital PDF with the intake-form link and order code.
4. Buyer completes the intake → the AI generates and checks the guide → it is delivered by email from our domain, with the web guide live.
5. Every web guide has a small footer, "Guide by <brand>". Guests who are also hosts see it, which gives slow viral growth. The delivery email asks for an Etsy review.
6. Upsell at delivery: the $29/yr refresh plan and the multi-property bundle.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Etsy search** — 8–10 listings covering keyword variants (welcome book, house manual, guest guide, VRBO, cabin, beach house) and price tiers — Etsy gives new listings a short visibility test, and "done-for-you" is an underserved sub-angle in a 1,000/mo keyword — first views within days, first sale plausibly in 2–4 weeks.
2. **Etsy Ads at $1–2/day for 2 weeks** — pays for visibility on the best 2 listings while there are no reviews — immediate impressions. This is a recurring cost of $15–30, so the sponsor must approve it, or it can be skipped to stay at $0.
3. **Free "sample guide" SEO pages** — public example guides for popular STR towns (Gatlinburg, Destin, Joshua Tree, Broken Bow) with a "get one for your property" CTA — long-tail local+host intent, low competition, but new-domain SEO means 2–4 months.
4. **Gumroad Discover / a second marketplace listing** — same product, a second shelf — slow, low effort.

### Path to first sale
- Day 0–2: the sponsor opens the Etsy shop and Etsy API app, connects a payout account, and buys the domain.
- Day 2–7: the AI builds the intake form, the generator (HTML→PDF and web guide), and 3 polished demo guides for fictional properties in real towns to use as listing photos. It writes 8–10 listings.
- Day 7: listings go live. The AI polls the Etsy Open API for new receipts every 15 min.
- Day 7–30: tune listing titles and photos from Etsy stats.
- **Estimate: first sale ~21–30 days after launch.**

### Who does what
- **AI operator:** builds and hosts the generator and web guides; creates listings through the Etsy API; watches new receipts; matches intake submissions to orders; researches and verifies local places; generates the PDF, web guide and QR; emails delivery; handles revision forms; re-verifies places for refresh subscribers; reads Etsy shop stats and adjusts listings.
- **Human sponsor:** one-time (~3h): Etsy shop + identity/bank verification, Etsy developer app approval, domain, inbox. Recurring (~30–45 min/week): read and answer Etsy Messages. Etsy's Open API v3 has **no messaging endpoint**, so the AI drafts replies in a shared doc and the sponsor pastes them. The sponsor also clicks "complete order" if API scopes don't allow it.

### Moat — why not just ask ChatGPT?
It's moderate. A host *could* prompt ChatGPT for text, but they would still have to design it, verify the places are open, host a mobile page, and make a QR sign. That assembly work is exactly what they already pay Fiverr $50–$200 for. The moat comes from convenience, a hosted URL that keeps working, local verification, and placement in Etsy search where they already shop. It does not come from the writing. The data moat is weak.

### Biggest risks (ideator's own view)
- **Etsy policy fit:** this sits on the line between a personalised digital item and a service. Etsy allows personalised digital items created by the seller, and AI use must be disclosed under the "designed by" label. A strict reading could treat it as a service listing, so the risk of a listing takedown is real.
- **Message handling:** Etsy buyers expect to chat. With no messaging API, response time depends on the sponsor, and slow replies hurt Star Seller status and ranking.
- **Wrong local info:** a closed restaurant or a wrong urgent-care address hurts trust. Mitigate with verification and a "last verified" date on every place.

---

## S2 — Trade-Specific Bilingual Toolbox Talks (English/Spanish), Packs + Monday Subscription

- **Persona:** The Scout (demand-first)
- **One-liner:** Ready-to-read weekly safety meetings ("toolbox talks") written for one specific trade, in side-by-side English/Spanish with a sign-in sheet. They are sold as Etsy/Gumroad PDF packs, with a $9/month emailed "this Monday's talk" subscription that adds weather and seasonal triggers.
- **Demand evidence:**
  - Etsy listings sell this exact product right now. One is "Bilingual Toolbox Talks English Spanish | 52 Construction Safety Meeting Topics (PDF)" at $19 for the 52-pack, with single talks at $4 each. Others include a "Weekly Construction Safety Toolbox Talks: 52 Topics" at $99.99, a "15 Toolbox Talks pack" at $16.85, and a "25 Safety Toolbox Talks Pack" (snippets). ([Etsy 52 bilingual](https://www.etsy.com/listing/4536964410), [Etsy steel erector pack](https://www.etsy.com/listing/4536878610), [Etsy single talk](https://www.etsy.com/listing/4536976086))
  - Trade associations charge for them: NRCA Toolbox Talks cost $95 for members and $195 for non-members. ([NRCA](https://www.nrca.net/RoofingNews/nrca-offers-toolbox-talks-publication.12-9-2019.8205/details/story))
  - An AI SaaS sells this as a subscription: toolboxtalk-ai, with a Pro plan at $49/month and a Crew plan at $149/month for bilingual video talks. ([pricing](https://toolboxtalk-ai.lovable.app/pricing))
  - The volume signal is strong but free supply exists too: CPWR/ASSE's 52 Spanish toolbox talks passed 100,000 downloads in year one, and NAWIC offers free bilingual weekly PDFs. Demand is proven. The paid gap is **trade-specific** content (landscaping, tree care, roofing, janitorial, solar, pest control) with a **ready sign-in sheet** that doesn't need any searching. ([FMLink on CPWR](https://fmlink.com/articles/asse-cpwr-release-workplace-safety-resources-for-spanish-speaking-construction-workers), [NAWIC](https://nawic.org/safety-toolbox-talks/))
- **Customer:** Owners, foremen and office managers of small contractors with 5–50 workers and Spanish-speaking crews: landscaping, roofing, tree care, commercial cleaning, painting, concrete. Insurers, GCs and OSHA expect documented weekly safety meetings from them. They search Etsy and Google for "toolbox talk" and "safety meeting topics". They already pay for insurance, Jobber/Housecall Pro, and occasionally safety consultants.
- **Problem / desire:** "I need something to read to the crew Monday morning that half of them can understand, and I need the sign-in sheet for the GC/insurance." The generic construction talks don't fit a lawn crew or a janitorial crew.
- **Offering:**
  - **Packs (PDF, instant download):** 52 weekly talks per trade, ordered by season, each 1 page. English and Spanish side by side, with 4–5 talking points, 2 crew questions, the OSHA standard reference, and a 20-line bilingual sign-in sheet. Start with 6 trades.
  - **Monday subscription:** every Sunday night the operator emails a talk picked for the subscriber's trade, region and week. The pick accounts for heat-index forecasts (heat illness talk during a heatwave), seasonal hazards (ice, storm cleanup, pollen, chainsaw season), and recent OSHA emphasis programs. It arrives with a fillable sign-in PDF and a 1-click "log this meeting" link, which builds a dated meeting log the subscriber can download for audits.
- **Price & revenue model:** Trade 52-pack $24, single talks $4, a 3-trade bundle $49 (Etsy + Gumroad). Monday subscription $9/month or $79/year through Lemon Squeezy/Gumroad as merchant of record. Price it well below the $49/month AI-video competitor.
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Etsy setup fee (if charged) | $15 |
| Etsy listings (~30 listings across trades/singles) | $6 |
| Domain (subscription landing page + email sending) | $12 |
| Gumroad / Lemon Squeezy account | $0 |
| **Total** | **~$33** |

### Monthly running costs (excluding operator tokens)
- Hosting (Cloudflare Pages/Workers, D1 for meeting logs): $0
- Weather data (NWS API, free for the US): $0
- Email (Resend free tier up to 3k/month, then $20/month): $0 early
- Etsy fees ~10–25% per sale; Lemon Squeezy/Gumroad ~5–10% + $0.50 per transaction
- Listing renewals: ~$2–5

### Customer acquisition plan
1. Demand shows up as Etsy and Google searches for "toolbox talks", "safety meeting topics", "bilingual safety talks", and "[trade] safety meeting".
2. Publish trade-specific packs on Etsy (titles like "Landscaping Crew Toolbox Talks English Spanish 52 Weeks") and the same packs on Gumroad.
3. Each pack PDF ends with a page offering 4 free weeks of the Monday subscription, which turns one-time Etsy buyers into our own email list. This does not breach Etsy's rules, because the offer lives inside the product file, not in Etsy messages.
4. A free public library of ~20 sample talks on our domain, one page per topic per trade, gives long-tail SEO ("chainsaw safety toolbox talk spanish").
5. Subscribers convert from the trial to $9/month or $79/year.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Etsy search** — 6 trade packs + ~20 single-topic listings at $4 — existing paid listings prove buyers search there, and trade-specific titles face less competition than "construction" — first views in days, sales in 2–5 weeks.
2. **Gumroad Discover + Payhip** — the same files on extra shelves — little effort, slow but free.
3. **SEO sample-talk pages** — "[topic] toolbox talk in Spanish PDF" pages, each with a printable free sample and an upsell — long tail with real search intent, though new-domain SEO means 2–4 months.
4. **Free submissions to resource roundups** — ask safety bloggers and state trade associations to list the free sample talks (the AI drafts the outreach; the sponsor sends a handful, so it isn't mass email) — medium speed.

### Path to first sale
- Day 0–2: the sponsor sets up Etsy, Gumroad/Lemon Squeezy and the domain.
- Day 2–8: the AI writes and lays out 6 × 52 talks. Every claim is checked against the OSHA standard it cites. The Spanish is reviewed by a second model pass for plain field language (not literal translation). The AI also builds the sign-in sheet template.
- Day 8: about 26 listings go live, plus the Gumroad store.
- Day 8–35: iterate titles and thumbnails using Etsy stats.
- **Estimate: first sale ~25 days after launch.** The first subscription conversion comes around day 45–60.

### Who does what
- **AI operator:** writes, translates, typesets and checks all talks against OSHA/eCFR text; creates listings; runs the Sunday-night scheduled send with weather triggers; maintains the meeting-log app; answers subscriber email support; produces new trades and topics monthly.
- **Human sponsor:** one-time (~3h) account and payment setup. Recurring (~20–30 min/week): Etsy messages (no API), and approve any outreach emails.

### Moat — why not just ask ChatGPT?
It's weak to moderate. A foreman *could* ask ChatGPT for a talk, but these buyers mostly don't. They want a print-ready, consistent, bilingual, citation-backed sheet with a sign-in sheet, delivered automatically every week, plus a dated meeting log to show a GC or insurer. The moat is convenience, the weekly habit, the documentation trail, and trade specificity. Free CPWR/NAWIC content is the real competitor, not ChatGPT.

### Biggest risks (ideator's own view)
- **Liability for safety content:** a wrong instruction could contribute to an injury. Mitigate with strict OSHA citations, conservative advice, and a clear "supplements but does not replace a site-specific safety program" disclaimer. The sponsor carries the legal risk.
- **Free substitutes:** CPWR and NAWIC give away good bilingual talks. The paid market is real but may be small, possibly a few hundred dollars a month.
- **Spanish quality:** stiff or regionally wrong Spanish gets laughed off the jobsite. Get an early native-speaker spot check, possibly from a buyer in exchange for a free year.

---

## S3 — Speeches for Big Moments: Custom Wedding Toasts (plus Eulogies and Retirement Toasts off-season)

- **Persona:** The Scout (demand-first)
- **One-liner:** A questionnaire-driven, fixed-price custom speech service. The buyer gets a ready-to-deliver speech, a large-print cue-card PDF, timing notes and one revision, fulfilled entirely by AI with clear AI disclosure and sold on Etsy where speech buyers already are.
- **Demand evidence:**
  - Etsy: the PersonalWordsmith shop shows **4,111 sales since 2016** for written wedding speeches, vows and similar items (snippet). Template speeches sell at $6.97–$25.57, and an "AI wedding speech generator" listing sells at $7.35 (snippet). ([Etsy shop](https://www.etsy.com/shop/PersonalWordsmith), [Etsy best man speech](https://www.etsy.com/ie/listing/1482051482/best-man-speech-digital-download-wedding))
  - Fiverr: one seller has completed **1,000+ orders** for best-man and maid-of-honour speeches (snippet). ([Fiverr: corinapariza](https://fiverr.com/corinapariza/write-your-bridesmaid-speech-1a87), [Fiverr: minah_design](https://de.fiverr.com/minah_design/write-a-custom-wedding-speech-with-heart-and-humor))
  - Premium tier proof: a bespoke speechwriter charges £399. AI-assisted packages run $82–$349. ([allspeechesgreatandsmall](https://allspeechesgreatandsmall.com/pricing))
  - **Counter-evidence (important):** a standalone AI wedding-speech app (Wedding Speech AI, iOS) earns only **~$17/month** across 5 subscriptions on TrustMRR. ([TrustMRR](https://trustmrr.com/startup/wedding-speech-ai)) People don't pay for a *generator*. They pay for a *finished, personalised deliverable on a marketplace they trust*. That supports the Etsy/done-for-you form, and it is also a warning that an app-store route would fail.
- **Customer:** Best men, maids of honour, fathers and mothers of the bride/groom, aged 25–60, 2–8 weeks before the wedding and anxious about public speaking. They shop Etsy for wedding everything (signs, favours, vows). Off-season (Nov–Mar), the same model serves people writing eulogies (urgent, year-round demand) and retirement or milestone-birthday toasts.
- **Problem / desire:** "I'm the best man in 3 weeks and I've written nothing." "I want it funny but not embarrassing, and under 4 minutes." They want it done, personal, and the right length, plus confidence when they deliver it.
- **Offering:** After purchase, the buyer completes a guided questionnaire (15–25 prompts: names, how they met, 2–3 stories, inside jokes to include or avoid, tone, target length, cultural or religious notes). Within 24–48h they get:
  1. The speech (DOCX + PDF) at the requested length.
  2. A large-print cue-card PDF with pause and emphasis marks.
  3. A "delivery notes" page with timing at speaking pace, where to look up, and a pronunciation guide for names.
  4. An alternative opening and closing to choose from.
  5. One free revision through a form.

  Every delivery states that the speech was written with AI assistance.
- **Price & revenue model:** Standard toast (2–4 min) $29; Extended (5–7 min) + 2 revisions $49; Rush 12h +$15. Eulogies are $39 with a gentler questionnaire. All prices are one-time per order.
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Etsy setup fee (if charged) | $15 |
| Etsy listings (~12 listings by role and type) | $2.40 |
| Domain for intake + delivery email | $12 |
| **Total** | **~$29** |

### Monthly running costs (excluding operator tokens)
- Hosting (Cloudflare Pages + Workers, KV for intake): $0
- Email delivery (free tier): $0
- Etsy fees ~10% (~25% with offsite ads) per order
- Listing renewals: ~$1–3

### Customer acquisition plan
1. Buyers search Etsy for "best man speech", "maid of honor speech", "father of the bride speech", "custom wedding speech", "eulogy writer" and similar terms.
2. One listing per role keeps keyword targeting tight. Thumbnails show a sample cue card and the line "Delivered in 48h · 1 free revision".
3. Purchase → the instant-download PDF contains the questionnaire link and order code → the AI drafts, self-critiques against the brief (length, banned topics, names) → delivered by email.
4. The delivery email asks for a review "after the wedding" with a scheduled reminder 1 day after the event date captured in the intake. Reviews are the flywheel.
5. Cross-sell vows or a second speech to the same wedding party.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Etsy search** — 10–12 role-specific listings — existing shops with thousands of sales prove buyers search there, and role-specific long-tail titles are winnable — first sale plausibly in 2–3 weeks.
2. **Etsy Ads ($1/day, optional)** — speeds up visibility before the first reviews — immediate impressions, small budget only with sponsor approval.
3. **Eulogy and retirement listings for off-season** — a different, year-round search pool that smooths wedding seasonality (it is October now, heading into the low wedding season) — similar speed to #1.
4. **SEO "speech examples" pages** — free sample speeches by role on our domain with a CTA — slow (2–4 months), but evergreen.

### Path to first sale
- Day 0–2: sponsor sets up Etsy, the developer app and the domain.
- Day 2–6: the AI builds questionnaires (wedding roles, eulogy, retirement), the generation and self-check pipeline, the cue-card PDF renderer, and 4 sample speeches for listing photos.
- Day 6: listings go live, and receipt polling starts.
- **Estimate: first sale ~20 days after launch.** Volume should rise sharply from January, when engagement season feeds spring/summer weddings.

### Who does what
- **AI operator:** listings; order polling; intake matching; drafting, self-review and revision; PDF rendering; delivery emails; review-reminder scheduling; listing optimisation from stats.
- **Human sponsor:** one-time ~3h account setup. Recurring ~30–45 min/week for Etsy Messages, which matter more here because buyers are anxious and like to ask "will it be ready by Saturday?". **Per-order judgement flag:** eulogies and anything involving sensitive family situations (divorce, estrangement, a recent death) may warrant a quick human glance. The AI flags such orders, the sponsor skims them in 2 min, and this should be about 10% of orders.

### Moat — why not just ask ChatGPT?
This is the weakest moat of the three, and I'll say so. Anyone can prompt ChatGPT for a toast. The evidence says people still pay $7–$400 on Etsy and Fiverr. They are buying structure and reassurance: a guided interview that pulls out the right stories, a fixed length, delivery coaching and cue cards, a revision guarantee, and a marketplace seller with reviews. The real moat is **Etsy reviews and ranking**, which build over time. The failed $17/month AI app shows that the generator itself is worth nothing.

### Biggest risks (ideator's own view)
- **Buyer expectations and disclosure:** some buyers assume a human writer. Etsy requires AI disclosure and so does honesty. Clear disclosure may lower conversion and could draw negative reviews from buyers who expected a person.
- **Seasonality:** launching in October means 2–3 slow months for weddings. The eulogy and retirement listings partly offset this.
- **Etsy service-listing rules and message load:** like S1, this sits between a personalised digital item and a service. With no messaging API, buyer anxiety becomes sponsor time.
