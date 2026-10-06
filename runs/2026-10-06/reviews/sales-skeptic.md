# Sales Skeptic review — 2026-10-06

Reviewer: `sales-skeptic`. All 15 briefs in `runs/2026-10-06/ideas/` were judged against `operator-constraints.md` and `scoring-rubric.md`.

Assumptions:
- Every idea starts with zero audience, zero domain authority, a new seller account with no reviews, and an operator that cannot post on social platforms.
- "First sale" means the first money charged to a stranger. It does not mean an install, a trial or a free signup.
- "P90 = never" means I put less than a 90% chance on any sale within 12 months.
- Days are counted from today (2026-10-06), so build and review time is included.

| ID | Idea | Score | P(≤30d) | P(≤90d) | P50 days | P90 days | Kill shot |
|---|---|---|---|---|---|---|---|
| T1 | RainCheck for Jobber | 3 | 3% | 20% | 170 | never | Jobber review delay plus the off-season: an approved listing arrives in November, when lawn and exterior crews have stopped caring about rain. |
| T2 | Accela/EnerGov Permit Actor (Apify) | 6 | 30% | 60% | 50 | 200 | Few paid Apify users need *their* Accela county, and most runs come from free-plan users who earn nothing. First revenue is cents, not dollars. |
| T3 | TipSplit for Clover | 2 | 1% | 10% | 185 | never | Clover approval plus a self-imposed 30-day trial pushes the earliest charge to about day 75. Tip apps already exist in the Clover market (TipHaus, Tipout). Trips the P50 > 180 gate as designed. |
| W1 | Bid Brief: Facilities Services | 4 | 10% | 35% | 120 | never | A zero-audience Substack can't build the ~200 free readers that 2–5 paid conversions need. Owners stay on free SAM.gov alerts and their course group's free bid lists. |
| W2 | Florida HOA Board Letter Kit | 4 | 15% | 40% | 110 | never | The Etsy search pool for *Florida-specific* HOA letters is tiny. Board volunteers Google and use free PayHOA or Condo Control templates. |
| W3 | Grant Deadline Desk: [State] | 3 | 3% | 22% | 160 | never | The paid product isn't credible until coverage is complete. Nonprofit buying is slow. Free alternatives (library Candid FDO, state associations, Grantable free tier) are good enough. |
| A1 | "Closing Day" house portraits | 5 | 30% | 55% | 70 | never | Buried under hundreds of $10–$20 AI house-portrait listings and one incumbent with about 8k reviews. Q4 traffic goes to shops with reviews. |
| A2 | Little Guests wedding activity book | 4 | 15% | 40% | 110 | never | Off-season launch into a niche long-tail search. Generic $1–$13 packs and "custom coloring page from photo" sellers already cover both halves. |
| A3 | "Looks Like Me" visual schedule cards | 5 | 25% | 50% | 90 | never | A $3–$15 commodity category with free symbol sets, TPT incumbents with thousands of ratings, and an audience hostile to AI art. |
| D1 | LanguageBids tender alerts | 3 | 3% | 20% | 170 | never | A few thousand possible buyers, and coverage misses where US spending actually happens (state, county, court portals). A cold trade-press pitch from an unknown sender is ignored. |
| D2 | InspectionWatch OSHA alerts | 4 | 8% | 30% | 130 | never | Free osha.gov search plus cheap Apify "OSHA leads" actors. Consultants won't pay $49/mo for a list they must still cold-call, and the sponsor's LinkedIn posts won't produce trials. |
| D3 | LabelScout TTB COLA intel | 3 | 3% | 18% | 175 | never | Label printers don't buy lead feeds from an anonymous newsletter. The consumer half earns affiliate pennies, and the registry source is fragile. |
| S1 | Done-For-You Airbnb Guidebook | 5 | 25% | 50% | 90 | never | A ~1k/mo keyword dominated by $8 templates. A $39 offer from a review-less shop competes with Fiverr sellers and free "paste your Airbnb URL" AI generators. |
| S2 | Bilingual Toolbox Talks | 4 | 15% | 40% | 110 | never | New listings (IDs 4536xxxxxx) show other, probably AI-driven, sellers already flooding this exact niche. Free CPWR and NAWIC talks undercut it. |
| S3 | Custom Wedding Toasts & Eulogies | 6 | 35% | 65% | 45 | 160 | Launching in the wedding off-season against review-rich speech shops. AI disclosure cuts conversion on the one product where buyers expect a human writer. |

Overall: no idea scores above 6. The best two (S3, T2) win because they skip the trust gap: Etsy and Apify handle checkout and supply the buyers. The "integration app" ideas (T1, T3) and the "data subscription" ideas (W1, W3, D1–D3) all depend on a review queue or audience-building, and those almost never finish inside 30 days.

---

## T1 — RainCheck for Jobber — Score 3

**First buyer:** a 3-crew lawn-care owner in Georgia or Texas who browses the Jobber App Marketplace looking for "weather". That is a concrete buyer, but in October most of them are winding down for the season.

**Traffic:**
- Jobber marketplace: *optimistic*. Approval time is unverified, and the brief admits it is unclear whether the API can even move visits.
- Jobber community replies: *realistic*, but the volume is tiny.
- SEO: *fantasy* within 90 days.
- Partner program: needs 10+ installs first.

**Why pay instead of the alternatives:** the main alternative is doing nothing. Owners already glance at a weather app, and the free Jobber++ extension shows forecasts on the calendar. A $19/mo bill only beats that in peak season with multiple crews.

**Trust gap:** small, because the app is listed inside Jobber. But billing runs through Lemon Squeezy, outside the platform, so there is still a second card prompt.

**Conversion math:** install volume for a new app in a ~100-app marketplace is unknown, maybe 5–20 a month. Trial-to-paid at 20–30% gives 1–5 paying customers a month, and only once there is weather to worry about.

**Steelman:** it is the only weather app in a captive marketplace. Southern pressure-washing and painting crews work all winter.

**Kill shot:** the timeline. Building and review take until about day 30–60, then a 14-day trial, all landing in Nov–Dec.

**Fix:** reposition the v1 for snow and ice plus southern exterior trades, and charge from day 1 of a "founding" annual plan, so the first sale doesn't wait for spring.

---

## T2 — Accela/EnerGov Permit Extractor (Apify) — Score 6

**First buyer:** a lead-gen freelancer on a paid Apify plan who builds roofing leads in an Accela county, e.g. a Florida or Arizona county with no Socrata feed, and who searches the Store for "Accela" or "building permits".

**Traffic:**
- Apify Store search: *realistic*. Self-serve publishing, buyers already present, and an exact-match niche keyword. My own search found 10+ permit Actors and none that advertise Accela coverage.
- Apify newsletter and showcase: *optimistic*.
- Disclosed forum replies: *realistic*, but small.
- Programmatic docs site: *fantasy* inside 90 days.

**Why pay instead of the alternatives:**
- Hand-copying permits, or hiring an Upwork freelancer for $100–$300 one time.
- Shovels.ai already covers many Accela jurisdictions, with a polished API.
- Pay-per-event pricing is cheap enough that "try it" costs nothing, which is the point.

**Trust gap:** almost none. Apify bills the buyer, there is no checkout, and runs are cheap.

**Conversion math:** a first paid event needs one paid-plan user to run it once, which is a low bar. $300/mo net needs about 90k permits a month, or 10 daily-run agencies. That is many months away and depends on scraper reliability across heterogeneous ASP.NET portals, some with reCAPTCHA.

**Steelman:** the fastest route on this list to *a* dollar from a stranger. It needs no audience, no reviews and no app approval.

**Kill shot:** the first "sale" is $0.04–$2 from someone testing. Scaling it needs users whose specific counties actually work, and free-plan usage pays nothing.

**Fix:** before building, use Upwork, r/webscraping and Apify issue requests to pick the 20 Accela jurisdictions people have actually asked for, and launch with those verified, rather than "120+ jurisdictions" of unknown quality.

---

## T3 — TipSplit for Clover — Score 2

**First buyer:** the owner of a 12-staff café on Clover who pools tips by hours, does it in a spreadsheet every Sunday, and searches "tip" in the Clover App Market.

**Traffic:**
- Clover App Market: *optimistic*. Approval time is unverified (the brief guesses 2–4 weeks), and a new app with no reviews ranks below TipHaus and OrderOut's Tipout, which already cover tips in Clover.
- Reseller emails: *optimistic*. ISOs push apps that pay them.
- SEO calculator: *fantasy* inside 90 days.
- Reddit replies from the sponsor: *realistic*, but tiny.

**Why pay instead of the alternatives:** the spreadsheet already works, and free tip-pool calculator phone apps exist. Many shops don't use Clover's timeclock, which removes most of the "automatic" value.

**Trust gap:** low, because Clover bills. But payroll and wage data plus an unknown developer is a real hesitation: if the app gets a share wrong, the owner faces a wage claim.

**Conversion math:** suppose 10 installs a month after listing at about 25% trial conversion. With a 30-day trial, the first charge lands around day 75–100 *at best*.

**Steelman:** a real price gap ($14.99 vs $99 plus $300 setup) in a marketplace with millions of merchants.

**Kill shot:** the time stack. Build (~15 days), then approval (unknown), then a 30-day trial puts P50 at about 185 days, which trips the hard gate. Existing Clover tip apps take the remaining search intent.

**Fix:** cut the trial to 7 days, or use a free tier that limits history, and verify Clover approval timelines with the developer community *before* building.

---

## W1 — Bid Brief: Facilities Services — Score 4

**First buyer:** the owner of a 6-person janitorial company in Texas who is watching "government contracts for cleaning companies" YouTube and has never won a federal bid.

**Traffic:**
- APEX counselors: *optimistic*. They share free resources, but they are publicly funded and wary of endorsing paid products, so at best they send free-tier readers.
- Substack cross-recommendations: *optimistic* with zero subscribers to offer in return.
- Sponsor posts in GovCon Facebook groups: *realistic*, and this is the best channel, but only for 4 weeks at 20 min/week.
- State SEO pages: *fantasy* inside 90 days.

**Why pay instead of the alternatives:** SAM.gov saved searches are free. Course gurus give their students free bid lists. Many of these buyers never win a bid and churn. ChatGPT can summarise a SOW if the owner pastes it in.

**Trust gap:** moderate. Substack plus $19/mo is a normal purchase, but an anonymous newsletter with no track record in a scam-heavy niche (bid-alert scams are common) raises suspicion.

**Conversion math:** free-to-paid newsletters convert at 2–5%. One paid subscriber needs about 30–50 engaged free readers, and break-even needs about 600 or more. Reaching 100 free readers in 30 days from zero is *optimistic*.

**Steelman:** this audience already spends $300–$2,000 on courses and is hungry for "where are the bids". The SOW extraction is real, visible value.

**Kill shot:** distribution. No owned audience, and the only realistic channel is a sponsor who posts for 4 weeks.

**Fix:** launch paid from issue 1 with a cheap founding price, and get one course creator or YouTuber in the janitorial-GovCon niche to recommend it, e.g. with an affiliate share. They own the buyers.

---

## W2 — Florida HOA Board Letter & Notice Kit — Score 4

**First buyer:** the volunteer secretary of a 90-home self-managed HOA in Florida who has just been told the fining process changed and searches Etsy for "HOA violation letter template".

**Traffic:**
- Etsy search: *realistic* that the listings get seen, but *optimistic* on volume. Generic "HOA letter template" bundles already sell for $3–$10, and "Florida" narrows the pool a lot.
- Gumroad Discover: *fantasy* (it is close to dead for niche items).
- HOA board forums: *optimistic*. Facebook and Nextdoor need the human, and self-promotion rules bite.
- SEO: *fantasy* inside 90 days.

**Why pay instead of the alternatives:** PayHOA and Condo Control give templates away. Management companies and attorneys publish sample letters. ChatGPT plus "Florida 720.305" gets close. The board's attorney is the trusted source when the stakes are real.

**Trust gap:** moderate to high. This is "legal-adjacent" content from an AI shop with no reviews, and the buyer is afraid of getting a fine thrown out.

**Conversion math:** Etsy digital templates convert at roughly 1–3%. At 30–100 views a month for niche FL listings, that is 0.3–3 sales a month at best.

**Steelman:** it is a real, dated pain (HB 1203), and the buyer's habit is to search for a template rather than prompt a chatbot.

**Kill shot:** low search volume. The FL-specific value only matters to buyers who already know the law changed.

**Fix:** make the listings generic ("HOA violation letter set, all states") with a FL/TX statute appendix, to capture the whole Etsy HOA search pool. Sell the FL depth as an upsell.

---

## W3 — Grant Deadline Desk: [State] — Score 3

**First buyer:** the executive director of a $400k Ohio youth nonprofit, or a freelance grant writer serving five such nonprofits.

**Traffic:**
- State nonprofit association: *optimistic*. A 2–6 week newsletter cycle, and associations often sell or promote their own resources.
- Freelance grant writers on a free license: *realistic* for adoption, but it delays paying customers by 30 days by design.
- Libraries: *optimistic*. They already provide free Candid FDO access.
- SEO: *fantasy* inside 90 days.

**Why pay instead of the alternatives:** Candid's Foundation Directory is free at partner libraries. GrantStation is $199/yr via TechSoup. Grantable has a free tier. Many local funders are invitation-only or roll their deadlines, so the "complete calendar" promise is fragile.

**Trust gap:** high. A new site asks for $99/yr to replace research the buyer currently does themselves. One missing local funder ends the trust.

**Conversion math:** 150–300 free readers by day 45 is *optimistic*. At 2–4% conversion that is 3–12 paid, but only after a ramp, with first paid realistically around day 60–120.

**Steelman:** strong annual-prepay and retention profile if it works. The freelance grant writer pays personally and decides fast.

**Kill shot:** too slow. The build-and-verify cycle and the nonprofit buying cycle push the first sale far past 90 days.

**Fix:** sell to freelance grant writers first, as a $15/mo consultant feed with paid access from day 1 and no free license, and narrow it to one cause area to shrink the coverage problem.

---

## A1 — "Closing Day" watercolor house portraits — Score 5

**First buyer:** someone in early December searching Etsy for "first christmas new home ornament custom house" for their sister.

**Traffic:**
- Etsy search plus the Q4 surge: *realistic* for impressions, *optimistic* for ranking against incumbents with thousands of reviews.
- Etsy Ads at $1–$2/day: *realistic*. This is the main lever.
- Pinterest API: *optimistic*. 3–8 weeks, and pins rarely convert to Etsy custom orders quickly.
- Realtor 5-packs: *fantasy*. Realtors don't find new AI shops on Etsy, and "AI-made" is not a gift they want their name on.

**Why pay instead of the alternatives:**
- Buyers who know they can use ChatGPT or Nano Banana will. Gift buyers mostly don't, but they will pick the $15 AI listing with 2k reviews over a new shop at $22.

**Trust gap:** high for a custom item. The buyer must trust that a stranger will render *their* house correctly and on time for the gift.

**Conversion math:** $40 of ads is roughly 80–120 clicks. A new shop with no reviews converts at about 0.5–1.5%, which gives 0.5–2 sales. Organic search adds a little in Q4.

**Steelman:** "house portrait" is a proven, high-volume, gift-season Etsy category, and the 24-hour turnaround is a real edge in December.

**Kill shot:** saturation. Many AI sellers already sell this at $10–$20 with reviews.

**Fix:** lead with the ornament and framed-print listings, which sell in Q4 at higher prices and face fewer pure-digital AI competitors. Drop the realtor angle until there are reviews.

---

## A2 — The Little Guests wedding activity book — Score 4

**First buyer:** a bride planning a May 2027 wedding with 10 kids invited, browsing Etsy in January. That is 3+ months away. In October the realistic buyer is a parent planning a birthday party.

**Traffic:**
- Etsy search: *realistic* for the $6 entry pack, *optimistic* for the personalised book.
- Pinterest: *optimistic*. It compounds slowly.
- Birthday edition: *optimistic*. It competes with established "custom coloring page from photo" sellers.
- SEO: *fantasy*.

**Why pay instead of the alternatives:** generic packs cost $1–$13, The Knot and others offer free wedding coloring pages, and kids' tables run on crayons and generic sheets. "About us" is a nice-to-have.

**Trust gap:** moderate. Uploading engagement and kids' photos to an anonymous AI shop with no reviews is a hesitation.

**Conversion math:** in a deep category, the new-listing boost fades in about 2 weeks. A $6 sale is plausible, but the $19–$32 personalised book needs reviews to move.

**Steelman:** the $6 non-personalised pack can earn a first sale and early reviews cheaply, and the photo-to-coloring hook is visually strong.

**Kill shot:** timing and depth. October is the trough, and the category is deep with cheap substitutes.

**Fix:** treat the $6 pack and the birthday edition as the main products until January, with ad spend on them, and wait to push the wedding book until engagement season.

---

## A3 — "Looks Like Me" visual schedule cards — Score 5

**First buyer:** the parent of a 4-year-old autistic girl with brown skin and glasses who searches Etsy for "visual schedule cards brown skin girl" after a therapy session.

**Traffic:**
- Etsy long-tail representation queries: *realistic*. They are specific, high-intent and less contested.
- Pinterest: *optimistic*.
- TPT: *optimistic*. TPT now demotes "AI slop" stores, and SLPs and teachers are vocally anti-AI.
- SEO tool: *fantasy*.

**Why pay instead of the alternatives:** ARASAAC and Boardmaker-style symbols are free or provided by schools. Real-photo cards can be made on a phone. TPT incumbents sell at $4–$13 with thousands of ratings. A mandatory AI disclosure on a product for a vulnerable child is a conversion drag.

**Trust gap:** moderate. A $9 purchase is low risk, but this audience reads reviews closely and punishes errors such as six fingers or ambiguous actions.

**Conversion math:** $9 listings at 1–3% conversion need 50–100 views per sale, which long-tail tags can deliver within weeks. Break-even (25 ready-made plus 5 custom sales a month) is far off.

**Steelman:** a real, emotional, under-served angle with precise search terms, a low price and no per-order work for ready-made packs.

**Kill shot:** a cheap commodity category with free alternatives plus anti-AI sentiment. One bad review about a wrong card sinks a new shop.

**Fix:** launch only the 6 ready-made avatars × 3 routines at $6–$9, with heavy QA, and add the custom $29 tier only after 10 reviews.

---

## D1 — LanguageBids tender alerts — Score 3

**First buyer:** the bid manager at a 15-person US interpreting agency who already pays HigherGov or BidNet and is tired of noise.

**Traffic:**
- Trade-press pitches (Slator, MultiLingual): *optimistic*. Unknown senders get ignored, and Slator sells its own data reports.
- ProZ and ATA listserv posts: *optimistic*. ProZ is freelancer-heavy (non-buyers), and listservs restrict promotion.
- Programmatic tender pages: *fantasy* inside 90 days, with scaled-content risk.
- Newsletter swaps: *optimistic*.

**Why pay instead of the alternatives:** buyers already have generic aggregators with saved keyword filters. Free SAM.gov, TED and CanadaBuys alerts exist. The big US spend sits on state, county and court portals the product can't cover.

**Trust gap:** high. This is $29–$79/mo B2B data from an unknown brand, and coverage gaps are visible on day 1.

**Conversion math:** the buyer pool is a few thousand LSPs. Even a 14-day trial with 20 trial starters at 10% gives about 2 sales, and getting 20 trials needs channels that don't exist yet.

**Steelman:** a genuinely uncurated niche with high contract values, which makes for a strong ROI pitch.

**Kill shot:** a tiny reachable audience plus thin coverage of where US buyers' contracts actually are.

**Fix:** sell only the EU/TED and Canada feed to EU and Canadian LSPs, where open data covers most of the market, and drop the US-first framing.

---

## D2 — InspectionWatch OSHA alerts — Score 4

**First buyer:** a solo safety consultant in Ohio who sells OSHA 30 training and written safety programs, and pays $10–$40 per click for "OSHA consultant near me".

**Traffic:**
- ASSP chapter editors and trade press: *optimistic*. There is a 2–4 week reply cycle, and data columns go to people the editors already know.
- Sponsor LinkedIn posts: *realistic* for engagement, *optimistic* for trials.
- State × industry SEO: *optimistic* to *fantasy* inside 90 days.
- Product Hunt: *fantasy* for this buyer.

**Why pay instead of the alternatives:** osha.gov establishment search is free, safetyrecord.org is free, and Apify "OSHA leads" actors are cheap. A consultant can check their state weekly in 10 minutes. Cold-calling inspected employers also has poor hit rates and can feel like ambulance-chasing.

**Trust gap:** moderate. A $49/mo B2B subscription with a 7-day trial is normal, but a brand-new site needs proof the data is fresher than osha.gov.

**Conversion math:** at 1–2% visitor-to-trial and 20% trial-to-paid, one sale needs about 250–500 targeted visitors. That needs either the LinkedIn posts or the editors to land.

**Steelman:** the buyer decides alone, has an obvious ROI, and already pays for leads.

**Kill shot:** free substitutes plus a channel (the sponsor's LinkedIn) that is unlikely to produce paying trials quickly.

**Fix:** launch one state at $19/mo with a free weekly sample sent to 30 hand-picked consultants (personal, opt-out emails from the sponsor), to test willingness to pay before building 50 states.

---

## D3 — LabelScout TTB COLA intelligence — Score 3

**First buyer:** a sales rep at a regional label printer or a beverage design agency who wants a list of new brands. These buyers don't search for this product. They would have to be found.

**Traffic:**
- Scoop pitches to whiskey writers: *realistic* for citations, but they produce enthusiast traffic, not B2B buyers.
- Trade-press stat packages: *optimistic*.
- Brand-page SEO: *optimistic* inside 90 days.
- Organic Reddit sharing: *fantasy* as a plan.

**Why pay instead of the alternatives:** the TTB registry is free. Label printers get leads from brokers, trade shows and existing customers. BW166 sells to the people who do pay for this. Enthusiasts won't pay at all, and the affiliate side needs age-gating and approvals the sponsor has to handle.

**Trust gap:** high. This is a $49/mo B2B "lead list" from an anonymous newsletter, sold to a buyer who never asked for it.

**Conversion math:** the trade-digest audience is effectively zero for months. The consumer list grows faster but doesn't convert to B2B.

**Steelman:** "first-time applicant" is a genuinely new signal, and BW166 proves the market pays.

**Kill shot:** a buyer-audience mismatch. The traffic engine attracts bourbon fans, and the revenue needs packaging salespeople.

**Fix:** sell a one-time $99 "Q3 new-brand entrants" CSV report on Gumroad and pitch it by personal email to 20 label printers and design agencies, testing demand before building the subscription.

---

## S1 — Done-For-You Airbnb Guidebook — Score 5

**First buyer:** a host with 2 cabins in Broken Bow who bought a Canva template last spring, never filled it in, and searches Etsy for "airbnb welcome book".

**Traffic:**
- Etsy search: *realistic*, but the pool is small (~1k searches/mo) and the "done-for-you" thumbnail must win clicks next to $8 templates.
- Etsy Ads: *realistic*.
- Sample-guide SEO pages: *fantasy* inside 90 days.
- Gumroad Discover: *fantasy*.

**Why pay instead of the alternatives:** Airbnb's built-in guidebook is free. Hostfully and Touch Stay include guides. A free "paste your Airbnb URL" AI guidebook generator already exists (seen in search). Fiverr sellers do the same work with reviews.

**Trust gap:** moderate. $39 to an unknown shop with an intake form after purchase. Hosts are pragmatic, but they also run the business on reviews.

**Conversion math:** if 10% of ~1k searches see our listing, that is about 100 impressions-to-views a month. At 1–2% conversion that is about 1–2 sales a month at best before reviews. Ads double it.

**Steelman:** Fiverr proves hosts pay $50–$200 for exactly this, and "we fill it in" is a clear upgrade over every template in the search results.

**Kill shot:** a small search pool plus free AI generators that compress the value of "done-for-you".

**Fix:** list at $19–$24 for the first 10 orders to buy reviews, and add "VRBO / cabin / beach house" variants to widen the keyword pool.

---

## S2 — Bilingual Toolbox Talks — Score 4

**First buyer:** the office manager at a 20-person Texas landscaping company with a Spanish-speaking crew who searches Etsy or Google for "toolbox talk spanish landscaping".

**Traffic:**
- Etsy search: *realistic* for views, *optimistic* for sales. The brief's own evidence (listing IDs 4536xxxxxx) shows a cluster of brand-new sellers, likely AI-assisted, already publishing near-identical bilingual packs.
- Gumroad and Payhip: *fantasy*.
- SEO sample pages: *fantasy* inside 90 days.
- Resource roundups: *optimistic*.

**Why pay instead of the alternatives:** CPWR's free Spanish talks (100k+ downloads) and NAWIC's free bilingual PDFs. Insurers and GCs often provide talks. Foremen do read generic ones.

**Trust gap:** low at $4–$24, but safety content from an anonymous AI shop invites skepticism about the Spanish.

**Conversion math:** 26 listings × low views (10–30/mo each) at 1–2% conversion gives about 3–15 sales a month *if* they rank. The subscription conversion is a further step down.

**Steelman:** it is proven sold on Etsy right now, and "landscaping" or "tree care" titles are more specific than the competitors' "construction".

**Kill shot:** a commodity race with copycat AI sellers already on the shelf, and free institutional content at the top of Google.

**Fix:** pick the 2 trades with zero trade-specific Etsy listings, price the 52-pack at $14 to get early reviews, and drop the subscription until there are 50 pack buyers.

---

## S3 — Custom Wedding Toasts & Eulogies — Score 6

**First buyer:** a best man with a wedding in 3 weeks who searches Etsy for "best man speech custom", or a grieving son who needs a eulogy by Friday.

**Traffic:**
- Etsy search by role: *realistic*. High-intent, deadline-driven searches, and proven shop volume (4k+ sales for one shop).
- Etsy Ads: *realistic*.
- Eulogy and retirement listings: *realistic*, and they matter most in Oct–Dec.
- SEO examples: *fantasy* inside 90 days.

**Why pay instead of the alternatives:** ChatGPT is free and many buyers know it. The pay-to buyer wants reassurance and a "writer". Established shops have years of reviews. Mandatory AI disclosure tells them it's "just ChatGPT".

**Trust gap:** moderate. $29 is low, and the deadline makes the buyer decisive, but an anxious buyer chooses the shop with 4,000 reviews.

**Conversion math:** role-specific listings at 1–2% conversion. Plausibly 100–300 views a month across 12 listings once indexed gives 1–5 sales. Ads speed this up. Eulogies have urgent, year-round demand.

**Steelman:** proven buyer intent on Etsy, urgency, low price, near-zero marginal cost, and a 24h turnaround that beats human writers.

**Kill shot:** October is the wedding trough, and AI disclosure lowers conversion against human-written incumbents.

**Fix:** lead with eulogy and retirement listings now, frame the product around the guided interview, cue cards and delivery coaching (not "AI wrote it"), and launch at $19 to get the first 10 reviews before wedding season starts in January.
