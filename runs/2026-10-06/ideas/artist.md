# AI art ideas — The Studio

_Run date: 2026-10-06. Web research used (Etsy/TPT/itch.io policy pages, Etsy sales-tracker data, TPT search results); sources are listed at the bottom. Sales figures from third-party trackers are estimates._

**Shared approach.** Pure AI art is commodity-priced and easy to copy, so all three ideas sell **personalisation or a finished, usable format** rather than raw images. All three use **Etsy as the first channel** because it brings its own buyers, and they are built to run on one shop. Each idea's capital table still assumes it runs alone, so the evaluators can score them separately.

**Etsy rules that apply to every idea (checked Oct 2026):**
- AI use must be disclosed in the listing description.
- Items go under "Designed by seller", never "Made by" or "Handmade".
- Since Aug 11 2026, production partners such as Printify must be disclosed.
- New shops pay a one-time setup fee of $15–$29. Other fees are $0.20 per listing, a 6.5% transaction fee, and about 3% + $0.25 payment processing.

**Etsy automation limits:**
- The operator can read orders through the Etsy Open API v3. The human must register the app.
- The API cannot send or read Etsy messages. Every flow below therefore collects photos and delivers files through a small upload/delivery site that the operator controls. The human spends a few minutes a week on the Etsy inbox.

---

## A1 — "Closing Day" watercolor house portraits for homebuyers and realtors

- **Persona:** The Studio (ideator-artist)
- **One-liner:** A personalised watercolor or ink-line portrait of a customer's house, made from their photo and delivered as a print-ready file within 24 hours. It is sold on Etsy to gift buyers and offered in prepaid multi-packs to real-estate agents who buy closing gifts every month.
- **Customer:**
  - **(a) Gift buyers.** People shopping for a housewarming, "first home", or "our first Christmas in our new home" gift, or a memorial for a family home. They search Etsy and Pinterest and already pay $25–$150 for hand-painted versions.
  - **(b) Realtors.** Solo agents and small teams who budget $50–$150 per closing for gifts. They hang out in agent Facebook groups and on Instagram, and already buy from Etsy, Cutco, and Closing Gift services.
- **Problem / desire:**
  - Gift buyer: "I want a meaningful, personal gift for their new home — fast, because the housewarming is Saturday."
  - Realtor: "I need a closing gift that doesn't look generic and that I don't have to think about every month."
- **Offering:**
  - **Digital files:** a 300-DPI print-ready file in 8x10, 11x14 and 16x20, an optional hand-lettered-style family name, address or date added by code (not by the AI), and a phone wallpaper bonus.
  - **Optional physical upsell through Printify:** a framed poster, a canvas, and (for Q4) a ceramic "Our first Christmas in our new home" ornament.
  - **Realtor pack:** 5 or 10 prepaid credits. A realtor submits a photo through a simple web form per closing and gets the files back, with an optional discreet "Congratulations from <Agent>" back card.
- **Price & revenue model:** One-time purchases.

  | Product | Price |
  |---|---|
  | Digital portrait | $22 ($29 with lettering and a second style) |
  | Rush delivery in under 6 hours | +$8 |
  | Printify framed print (cost about $25–$35) | $59–$79 |
  | Printify ornament (cost about $9–$12) | $24 |
  | Realtor 5-pack, digital, sold on Etsy or by direct checkout | $85 |
  | Realtor 10-pack | $150 |

  Break-even is about 16 digital sales a month at a net of about $19 each.
- **Physical items required?** Digital is the core product. The optional prints, canvases and ornaments are made and shipped by Printify, and the human never touches them. Customisation means returns are only for defects, which Printify reprints. Printify must be disclosed as a production partner (Etsy rule since Aug 2026). The quality-control risks are colour shifts on canvas and damaged ornaments, and Printify handles reprint claims.

### Upfront capital
| Item | Cost |
|---|---|
| Etsy one-time shop setup fee (varies $15–$29) | $29 |
| 25 initial listings × $0.20 | $5 |
| Image API credit: ~150 images for sample portraits and mockups at ~$0.04, plus upscaling | $8 |
| Upload/delivery site (Cloudflare Pages + R2 free tier) | $0 |
| Domain (optional; a Pages subdomain works at launch) | $0–$12 |
| **Total** | **$42–$54** |

### Monthly running costs (excluding operator tokens)
- **Generation per order:** 4–8 image-edit attempts at about $0.04, plus about $0.01 for upscaling, for **about $0.20–$0.40 per order**.
- **Etsy fees:** listing renewals of about $2–$5 a month, 6.5% transaction fee, and about 3% + $0.25 processing. That comes to about $2.60 on a $22 sale.
- **Etsy Ads:** optional, $1–$3 a day once there are reviews. Keep at $0 for the first 2 weeks.
- **Offsite Ads:** 15% on attributed sales. This is mandatory only above $10k a year in sales.
- **Hosting:** Cloudflare free tier, $0.
- **Email delivery:** Resend or Postmark free tier, $0.
- **Total fixed costs:** about $5 a month plus ads.

### Customer acquisition plan
1. **Etsy search.** Build 25 listings targeting long-tail combinations of style and occasion, such as:
   - "watercolor house portrait closing gift"
   - "ink sketch house drawing digital"
   - "first christmas new home ornament custom house"
   - "childhood home memorial painting"
   - "realtor closing gift bulk"
2. **Listing photos.** Each listing gets professional-looking mockups of before/after photo pairs. The source photos are CC0 house photos from Pexels/Unsplash, which permit modification.
3. **Conversion.** Promise turnaround "within 24 hours" and offer a $8 rush option. Most competitors quote 2–7 days, so speed is the AI's natural edge.
4. **Repeat business.** Realtor buyers get a direct, prepaid credit page, and every delivery file carries a small "Realtor? 5-packs here" link.
5. **Reviews.** After each delivery, an auto-email asks for an Etsy review. Reviews are the compounding asset.

### Initial traffic approaches (ranked by expected speed)
1. **Etsy search plus the Q4 gift surge.** New listings get a short visibility test from Etsy. Mid-October to mid-December is peak season for housewarming, Christmas and ornament gifts, and "first Christmas in new home" ornaments sell heavily. **Expected speed: days to 3 weeks.**
2. **Etsy Ads at $1–$2 a day for 2–3 weeks.** These buy impressions before the shop has reviews, and the human only has to switch them on once. **Expected speed: 1–2 weeks.**
3. **Pinterest via the official API.** The human creates a business account. The operator then auto-pins about 3 before/after images a day to boards such as "housewarming gift ideas" and "realtor closing gifts". Scheduled API posting is allowed on Pinterest, and pins keep working for months. **Expected speed: 3–8 weeks.**
4. **Realtor SEO page.** A page titled "closing gifts realtors can order in 2 minutes" with a free sample. Traffic is slow because the domain is new. **Expected speed: 3–6 months.**

### Path to first sale
- **Day 0–2:** The human opens the Etsy shop and connects Printify. The operator builds:
  - the upload/delivery site, keyed by Etsy receipt ID
  - the generation pipeline, which runs image-edit, structure checks (a vision comparison against the source photo), a 2× upscale, lettering and PDF/JPG export
  - 30 sample portraits and their mockups
- **Day 2–4:** 25 listings go live, all with the AI disclosure.
- **Day 4–21:** The operator watches stats and rewrites titles and tags. It turns on $1–$2 a day of ads on day 7.

**My estimate: first sale in about 14–21 days.** The Q4 timing helps.

### Who does what
- **AI operator:**
  - Builds the generation pipeline and the upload/delivery site.
  - Polls Etsy orders through the API, generates and checks each portrait, and emails buyers a download link plus a single free revision.
  - Marks orders complete, writes listings, and posts pins.
  - Runs the reporting.
- **Human sponsor:**
  - **One-time (about 2.5 hours):** opens the Etsy shop (ID/KYC and payout), registers the Etsy API app, connects Printify, and creates a Pinterest business account.
  - **Recurring (about 30–45 minutes a week):** checks the Etsy inbox and pastes replies the operator has drafted. Etsy messages are not available through the API.

### Moat — why not just ask ChatGPT?
**Weak, but real for this buyer.** ChatGPT, Gemini or Nano Banana can turn a house photo into a watercolor in one prompt, and tech-savvy buyers will do exactly that. The buyers who pay are different:
- **Gift buyers** want a guaranteed result for someone else. That means:
  - a print-ready 300-DPI file in standard frame sizes
  - lettering that is not garbled
  - a preview before paying
  - a revision included
  - a framed print or ornament that arrives without any effort from them
- **Realtors** want a monthly routine that takes no thought.

The trust signals (reviews) and the speed promise are the moat. A tracked bestseller in this niche is a $24.99 watercolor home portrait with about 34.5k sales and about 8.2k reviews since 2022. That shows demand, and it also shows that the niche is crowded.

### Biggest risks (ideator's own view)
- **Saturation and price pressure.** Etsy is full of "custom house portrait" listings, many of them already AI-made at $10–$20. Without fast reviews, a new shop gets buried after the new-listing boost.
- **Fidelity complaints.** Image-edit models sometimes change windows, rooflines or the number of doors, and homeowners notice. Mitigations are an automatic vision diff against the source photo, a free revision, and showing the preview before the final file. Each refund also costs Etsy shop health.
- **Ops leakage through Etsy messages.** Buyers will message instead of using the upload page. If the message volume grows, the human's weekly time goes above 1 hour. Personalisation-field instructions and an auto-reply template reduce, but don't eliminate, this.

---

## A2 — Personalised kids' wedding activity book ("The Little Guests Book")

- **Persona:** The Studio (ideator-artist)
- **One-liner:** A 16–24 page printable activity book for the kids' table at a wedding, personalised to the couple. It includes:
  - a coloring page of the couple drawn from their engagement photo
  - their pets
  - their venue as line art
  - their names and wedding date woven into word searches, mazes and "how well do you know the couple?" quizzes

  It is sold on Etsy, with a birthday-party version for year-round demand.
- **Customer:** Brides and couples 2–9 months before the wedding, and their mothers and planners. They live on Etsy, Pinterest and The Knot/Zola, and already pay $5–$15 for generic kids' wedding activity packs, or $20–$40 for editable Canva/Corjl template suites.
- **Problem / desire:**
  - "We have 12 kids coming and I need something to keep them busy during dinner. Bonus if it's actually *about us*."
  - "Generic coloring pages feel cheap; I want it to match our wedding."
- **Offering:** Personalised PDFs in US Letter and A4, ready to print at home or at Staples. Each book contains:
  - 1–3 custom AI line-art pages: the couple, their pet or pets, and the venue. Each is converted to clean, thick-line, printable black-and-white art.
  - 12–20 pages built by code from a curated base library:
    - word search, crossword and maze, all generated by code so they are guaranteed solvable
    - "draw the cake", "I spy at the wedding" bingo, and a name-tag cover
  - Names, date and colours set by a layout engine, with no AI-rendered text.
  - A matching "kids' table" sign.

  Delivery is within 48 hours by download link.
- **Price & revenue model:** One-time purchases.

  | Product | Price |
  |---|---|
  | Personalised book, base | $19 |
  | Plus pet page | $24 |
  | Plus pets, venue page and two age versions (toddler 2–4 and kids 5–10) | $32 |
  | Rush delivery | +$8 |
  | Birthday-party edition (same pipeline) | $16 |
  | Non-personalised wedding pack, a low-price entry listing that earns reviews | $6 |

  Break-even is about 15 to 18 sales a month at an average net of about $20.
- **Physical items required?** No. It is a digital PDF only. A printed-book upsell through Lulu's print API is possible later, but it is not in scope.

### Upfront capital
| Item | Cost |
|---|---|
| Etsy one-time shop setup fee (varies $15–$29) | $29 |
| 20 listings × $0.20 | $4 |
| Image API credit: base library of ~40 wedding and party line-art pages × ~3 attempts, plus ~10 sample personalised books, about 180 images at ~$0.04 | $8 |
| PDF/puzzle generation (open-source libraries) and hosting (Cloudflare free tier) | $0 |
| **Total** | **$41** |

### Monthly running costs (excluding operator tokens)
- **Generation per order:** 3–8 images at about $0.04, plus vectorising or line cleanup in code at $0, for **about $0.15–$0.35 per order**.
- **Etsy fees:** about 10% + $0.25 per sale, plus about $3–$4 a month in listing renewals.
- **Etsy Ads:** optional, $1–$2 a day.
- **Hosting and email:** free tiers.
- **Total fixed costs:** under $5 a month plus ads.

### Customer acquisition plan
1. **Etsy search** on long-tail terms, such as:
   - "personalized kids wedding activity book"
   - "custom wedding coloring page from photo"
   - "kids table wedding activity personalized with pets"
   - "flower girl activity book custom"
   - "kids birthday coloring book of my child's party theme"
2. **Listing images.** Listings use a sample couple (CC0 or model-released stock photos, never real customers without opt-in). The images show the transformation from photo to coloring page, because that is the hook.
3. **The free $6 pack** collects early reviews and cross-sells: "Make it about YOU — upgrade for $13".
4. **Pinterest** drives wedding planning, so every finished sample becomes a pin.
5. **Referrals.** The PDF has a small footer reading "Made by <shop>". Every wedding puts the product in front of 50–150 guests, and some of them are planning their own wedding.

### Initial traffic approaches (ranked by expected speed)
1. **Etsy search, new-listing boost and ads.** Wedding printables are a deep Etsy category, and personalised photo-to-coloring is a fresh angle with fewer direct competitors than generic packs (which sell for $1–$13). **Expected speed: 2–5 weeks.**
2. **Pinterest via the official API.** The operator auto-pins 2–4 pins a day to wedding-planning boards. Wedding planners use Pinterest more than any other platform, and pins compound over time. **Expected speed: 3–8 weeks.**
3. **Birthday-party edition listings.** These cover the wedding off-season (Oct–Feb is low for weddings, but engagement and planning season runs Dec–Feb). Parents buy for birthday parties year-round, often 1–2 weeks before the event. **Expected speed: 2–4 weeks.**
4. **SEO blog/landing page.** Pages such as "kids table ideas for weddings" and "free wedding coloring page" act as lead magnets. **Expected speed: 4–6 months.**

### Path to first sale
- **Day 0–3:** The human opens the Etsy shop. The operator builds:
  - the puzzle generators and the layout engine
  - the photo-to-line-art pipeline, with checks for line weight, no grey fills and no text
  - the upload form, which asks for names, date, colours, a couple photo, pet photos and a venue photo
- **Day 3–6:** The operator produces 3 complete sample books and publishes 20 listings: wedding variants, birthday variants and the $6 entry pack.
- **Day 6–35:** The operator optimises titles and tags, runs ads at $1–$2 a day from day 10, and pins daily.

**My estimate: first sale in about 21–35 days.** It is slower than A1 because October is past peak wedding-planning season, and the birthday edition fills that gap.

### Who does what
- **AI operator:**
  - Builds all the generators.
  - Processes orders via the Etsy API and the upload site, generates and QA-checks each book (vision check that it is printable, the likeness is reasonable and it is safe for kids), and emails the PDF plus one revision.
  - Writes listings and pins, and drafts replies to Etsy messages.
- **Human sponsor:**
  - **One-time (about 2 hours):** opens the Etsy shop, registers the API app, and creates a Pinterest business account.
  - **Recurring (about 20–40 minutes a week):** relays Etsy messages and handles any dispute.

### Moat — why not just ask ChatGPT?
**Moderate.** A bride can get *one* coloring page of herself and her partner from ChatGPT. She cannot easily get:
- a cohesive, print-ready 20-page book
- puzzles that are actually solvable and built from her names
- consistent line weight that prints well on a home printer
- two age-level versions
- a matching sign

All of that in 48 hours, while she is planning a wedding. Done-for-you convenience during a stressful, deadline-driven event is the real product. The puzzle and layout engine is genuine code that a casual cloner won't rebuild for a $19 item. The weakness is that a competitor *can* rebuild it, and generic template shops are already cheap.

### Biggest risks (ideator's own view)
- **Seasonality and timing.** Launching in October misses peak demand. Revenue may not reach $300 a month until spring if the birthday edition underperforms.
- **Likeness disappointment.** Line-art versions of real people sometimes look "off", which leads to revisions or refunds. Mitigations are offering a stylised cartoon style rather than a realistic one, setting expectations in the listing, and showing a preview before the full book.
- **Children's-content and privacy care.** Customers may upload photos of children such as the flower girl or a birthday child. The operator must store photos privately, delete them after 30 days, never use them in marketing, and refuse anything that isn't kid-appropriate. A privacy slip carries real legal and reputational risk for the human.

---

## A3 — "Looks Like Me" visual schedule and routine cards with matching avatars

- **Persona:** The Studio (ideator-artist)
- **One-liner:** Printable visual-schedule and routine picture cards (morning routine, school day, therapy, potty training, calm-down) with one consistent illustrated child. Buyers pick a child who looks like their own: skin tone, hair, glasses, hearing aids, wheelchair or AFOs, and gender expression. The cards are sold to parents of autistic and ADHD kids, special-education teachers and SLPs. There are ready-made avatar packs and a per-order "build your child's avatar" custom pack.
- **Customer:**
  - Parents of autistic or ADHD kids aged 2–10. They search Etsy and Pinterest and are active in parenting groups. They already pay $3–$15 for routine-card printables and $100+ a year for apps.
  - Special-education teachers and SLPs. They buy on TPT, where top "visual schedule" products sell at $4–$13.50 with 800–6,000+ ratings.
- **Problem / desire:**
  - "My son doesn't connect with the clip-art kid — he needs to see *himself* brushing his teeth."
  - "I can't find visuals with a kid in a wheelchair / with glasses / who looks like my daughter."
  - "Real-photo cards are inconsistent and the free symbol sets look clinical."
- **Offering:** Printable PDFs with a print-and-laminate layout in 2", 3" and 4" sizes. Each pack includes:
  - 120+ cards
  - a first/then board, a token board and a daily strip
  - **labels typeset in code** with font choice and a Spanish option, so there are no AI-rendered words
  - **Ready-made packs:** 6 launch avatars covering a range of skin tones, hair types and one wheelchair user, expanding as revenue allows.
  - **Custom pack:** the buyer configures an avatar with a web form (no child photo uploads). The operator generates a consistent character sheet, then 100–150 cards, and delivers within 72 hours.
- **Price & revenue model:** One-time purchases.

  | Product | Price |
  |---|---|
  | Ready-made avatar pack | $9 |
  | Ready-made mega bundle (3 routines + boards) | $16 |
  | Custom-avatar pack | $29 |
  | Custom-avatar pack with a "sibling add-on" | $39 |
  | Classroom set of 4 avatars (teachers) | $24 |

  Break-even is about 25 ready-made sales plus 5 custom sales a month.
- **Physical items required?** No. It is digital only. Parents print and laminate the cards themselves.

### Upfront capital
| Item | Cost |
|---|---|
| Etsy one-time shop setup fee (varies $15–$29) | $29 |
| 20 listings × $0.20 | $4 |
| Image API credit for the base library: 6 avatars × ~100 cards = 600 finals, about 1.5× rerolls, so about 900 images at ~$0.04 | $36 |
| Avatar-builder web form and delivery (Cloudflare free tier) | $0 |
| TPT Basic seller account (reported $29 one-time) | deferred and paid from revenue, $0 now |
| **Total** | **$69** |

### Monthly running costs (excluding operator tokens)
- **Generation per custom order:** about 150 images at $0.04, for **about $6**.
- **Ready-made packs:** $0 marginal cost.
- **New avatars:** expanding the library costs about $6 per avatar added.
- **Etsy fees:** about 10% + $0.25 per sale, plus about $4 a month in renewals.
- **TPT, later:** the Basic tier pays out only 55% plus $0.30 per resource, so upgrade to Premium ($59.95 a year, 80% payout) only once TPT sales exceed about $25 a month.
- **Total fixed costs:** under $5 a month plus ads.

### Customer acquisition plan
1. **Etsy search** with listings per avatar and per routine, such as:
   - "visual schedule cards brown skin girl"
   - "autism routine cards boy with glasses"
   - "visual schedule wheelchair user"
   - "custom visual schedule that looks like my child"
   - "potty training visual cards"

   The demand exists, and the representation angle is under-served in the top listings.
2. **A free 12-card sample pack** sold on Etsy for $0–$1 earns reviews and leads to an upsell.
3. **TPT store** once revenue covers it. The classroom sets and editable boards suit teachers and SLPs.
4. **Pinterest pins** for each routine theme, since "visual schedule printable" is a popular search on Pinterest.

### Initial traffic approaches (ranked by expected speed)
1. **Etsy long-tail search.** Representation-specific queries are low-competition and high-intent, and new-listing visibility arrives in days. **Expected speed: 1–4 weeks.**
2. **Pinterest via the official API.** Daily pins of each routine and avatar. Parents save these, and the long tail compounds. **Expected speed: 3–8 weeks.**
3. **TPT marketplace,** opened once there is about $30 of revenue to cover setup. TPT search reaches SLPs and special-education teachers directly, and the back-to-school and January "new routine" spikes help. **Expected speed: 4–10 weeks after opening.**
4. **SEO page.** A free routine-card generator page ("make a free 5-card morning routine") as a lead magnet. **Expected speed: 4–6 months.**

### Path to first sale
- **Day 0–5:** The human opens the Etsy shop. The operator:
  - designs the style guide and the 6 avatar character sheets
  - generates and vision-QAs the base library, checking that each action is unambiguous, has correct objects and hands, uses no text and stays consistent across cards
  - builds the PDF/label engine and the avatar-builder form
- **Day 5–7:** About 20 listings go live (avatar × routine), plus the free sample.
- **Day 7–30:** Tag tuning, pins, and $1 a day of ads from day 10.

**My estimate: first sale in about 14–30 days.**

### Who does what
- **AI operator:**
  - Generates the art and QAs every card.
  - Builds the PDF engine and the avatar-builder form, and generates custom orders.
  - Delivers by email link, writes listings and pins, drafts message replies, and later builds TPT listings.
- **Human sponsor:**
  - **One-time (about 2 hours):** opens the Etsy shop, registers the API app, creates a Pinterest account, and later opens the TPT seller account (KYC and payout), which takes about 30 minutes.
  - **Recurring (about 20–30 minutes a week):** relays Etsy messages.

### Moat — why not just ask ChatGPT?
**Moderate.** One-off images are easy to make. The hard part is **120+ cards with the *same* child, in the same style, with each action unambiguous and correct**, laid out for laminating with clean labels. Ad-hoc prompting does that badly, and it is tedious for an exhausted parent. The real competitors are:
- **free symbol sets** (ARASAAC, which is clinical-looking and has no "looks like my child" option)
- **real-photo packs**
- **TPT incumbents** with thousands of reviews

The differentiators are representation and consistency, delivered as a finished product. A cloner *could* copy the ready-made packs because AI art has thin copyright protection. The custom-avatar workflow is harder to copy.

### Biggest risks (ideator's own view)
- **Quality on a sensitive audience.** A wrong object, a six-fingered hand or a confusing action hurts a child's routine, and the reviews will say so. Chalkbeat (Aug 2026) documented "AI slop" on TPT, and TPT says it algorithmically demotes stores associated with low-quality AI. Strict QA is essential, and so is honest disclosure.
- **Anti-AI sentiment among SLPs, teachers and parts of the autism community.** Required disclosure may lower conversion, especially on TPT. Etsy parents are likely more pragmatic.
- **Character consistency at scale.** Even with reference-image conditioning, some avatar/action combinations will need many rerolls. If the reroll rate exceeds 3×, per-order cost and turnaround rise, and the base-library budget ($36) could overrun the plan. That would still be under the $100 cap.

---

### Sources
- [Etsy Creativity Standards 2026 summary (listadum)](https://www.listadum.com/blog/etsy-creativity-standards)
- [Etsy 2026 fees & AI disclosure / production-partner rules (beancount.io)](https://beancount.io/blog/2026/07/09/etsy-2026-fee-hike-ai-disclosure-rules-handmade-sellers-guide)
- [Etsy variable shop setup fee (Value Added Resource)](https://www.valueaddedresource.net/etsy-variable-shop-setup-fee/)
- [Watercolor home portrait listing sales estimate (findniche)](https://findniche.com/etsy-product/home-portrait-house-painting-housewarmin-1176417219)
- [Hand-painted house painting listing estimate (findniche)](https://findniche.com/etsy-product/100-hand-painted-house-painting-custom-w-4326874345)
- [AI slop on Teachers Pay Teachers (Chalkbeat, Aug 2026)](https://www.chalkbeat.org/2026/08/03/ai-slop-on-teachers-curriculum-marketplace/)
- [TPT seller fees (third-party summary)](https://www.tpt.it.com/fees/)
- [TPT "visual schedule" search results](https://www.teacherspayteachers.com/browse?search=visual%20schedule)
- [itch.io generative AI disclosure requirement (80.lv)](https://80.lv/articles/asset-creators-on-itch-io-now-have-to-disclose-the-use-of-generative-ai/). Considered for a game-asset idea and rejected: AI-tagged assets are filtered by much of itch's audience.
