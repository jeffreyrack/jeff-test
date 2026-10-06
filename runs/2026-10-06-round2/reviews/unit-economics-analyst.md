# Unit Economics Analyst review: round 2 (2026-10-06)

Scope: 13 ideas (G1–G3, C1–C3, I1–I3, M1–M3, U4). U4 is modelled as two variants.
Score = unit-economics dimension (1–10) from `scoring-rubric.md`.

| ID | Idea | Score | Upfront $ | Monthly fixed $ | Net $/sale | Sales/mo for $300 | Est. operator tokens $/mo | Months to break-even |
|---|---|---|---|---|---|---|---|---|
| G1 | Keyword→Brief Apify Actor | **6** | $50 (DataForSEO prepaid minimum) | $0 | $0.028/brief; $0.0026/metric keyword | ~10.7k briefs (≈70 paying users at ~$6 gross) | $150 build month, then ~$80 | **4** (Jan) accrued; cash ~month 5; cumulative ~month 7 |
| G2 | LongForm Transcripts Apify Actor | **5** | $5 | $0 | $0.0061/min at list; ~$0.0053 blended after price pressure | ~49k–57k audio min (≈35–50 paying users) | $150 build, then ~$80 | **4–5** accrued; cumulative ~month 7 |
| G3 | AnswerShare API (MCPize + RapidAPI) | **2** | $10 | $0–5 + free-tier subsidy ~$20–40 | $6–14 per $29 plan (RapidAPI, 50–100% use); $0.04 per pay-per-call check | ~22–45 $29 subs, or ~7.5k PPC checks | $200 build, then ~$120 | **Not within 12 months** |
| C1 | FunderFit 990-PF reports via academies | **7** | $17 (+$0–5 if Workers Paid is needed for the grants table) | ~$5 | $18.88 affiliate report; $35.26 direct; $45.73 Practice plan via affiliate | 17 affiliate reports (or 9 direct) | $250 build, then ~$120 | **5** (Feb); cumulative ~month 8–9 |
| C2 | Client Safety Kit, white-label | **6** | $15–27 | ~$20 (optional Spanish spot-check) | $22.86 per $49 licence via affiliate; $12.51 at the $29 founding-for-life price | 14 at $49 via affiliate (26 at founding price) | $250 build, then ~$150 | **~8–9** (not within 6) |
| C3 | Interpreter Practice Lab | **4** | $28–34 (up to $74 with the paid calibration rater) | $0 | $13.65 per $29 pass via affiliate; $25.83 direct; school $45–108 (median use) | 22 affiliate passes, or 3 direct school licences | $300 build, then ~$200 | **~10–12, only if 2 schools sign**; otherwise not within 12 |
| I1 | Zì Bot (Discord) | **3** | $12 | $0 (+ free-trial inference $5–25) | $3.58/Supporter-month (Lemon Squeezy); $2.89 via Discord's 70% split | 84 Supporters (104 on Discord billing) | $200 build, then ~$100 | **~9–12** to cover own tokens; $300 not within 12 |
| I2 | Episode Study Packs for creators | **7** | $12 | $0 | $32.06 per $39 Studio month | 10 Studio subs | $150 build, then ~$100 | **4** (Jan); cumulative ~month 6 |
| I3 | Role-Play Room for Chinese classes | **4** | $12 | $0 | $114.93 per $149 class-semester (≈$19/mo annualised); $9.81 per $12 student seat | ~16 renewing classes per semester (licence) or ~7–8 classes of 25 (seat model) | $200 build, then $60–150 (seasonal) | **Lumpy. Sustained only ~month 11–12 (fall 2027) at best** |
| M1 | ChatRelay for Jira (Forge) | **9** | $0–8 | $0 | ~$20 per paying site/month (0% rev share) | 15 paying sites | $150 build, then ~$60 | **3–4** accrued; first *cash* ~month 6 ($500 threshold) |
| M2 | SpecView for Confluence (Forge) | **8** | $0 | $0 | ~$12–15 per paying site/month | 20–25 paying sites | $100 + $150 converter, then ~$60 | **5** accrued; first cash ~month 7–8 |
| M3 | SheetSync Apify Actor | **6** | $0 | $0 | ~$6.73/paying user/month after the promo; **~$0.40 during the promo as written** | ~45 paying users (~60 at a realistic $5) | $100 build, then ~$50 | **2–3**; cumulative ~month 3 |
| U4a | AI job board, free then employer posts | **2** | $12 | $0 → $60–180 by month 6 (email, vector DB, free-user inference) | $139.93 per $149 employer post | 3 posts/mo (≈5 to also cover tokens and infra) | $300 build, then ~$250 | **Not within 12 months** (employer revenue unlikely before month 12–18) |
| U4b | AI job board, $12/mo seeker subscription | **4** | $12 | ~$10–55 (scales with users) | $10.15 per sub-month after inference | 30 subs (~57 to also cover tokens and infra) | $300 build, then ~$250 | **Not within 12 months (P50)**; best case ~10–12 |

---

## Common assumptions

- **Calendar:** month 1 = October 2026, so month 6 = March 2027.
- **Break-even:** the first month in which accrued net revenue covers fixed costs plus operator tokens. Cash can arrive later because of payout lags; these are noted per idea.
- **Lemon Squeezy:** consistent with the round-1 review, about 6.25% + $0.50 on subscriptions and about 5.75% + $0.50 on one-off sales. This includes the international surcharge on about half of buyers. Affiliate-referred orders cost a further 2%.
  - If Lemon Squeezy's move to Stripe Managed Payments completes, fees are similar: about 3.5% plus Stripe processing. There is no built-in affiliate tool, so the C-series affiliate payouts become a sponsor task.
- **Apify PPE:** the developer receives 80% of paid-plan revenue minus platform costs.
  - Free-plan users generate no revenue and no platform cost.
  - However, **any external API cost (DataForSEO, Groq) that free-plan users trigger is billed to the operator's own account.** G1 and G2 must check whether the user is paying and gate free users. Otherwise the leak is uncapped.
  - Minimum payout is $20. Earnings are invoiced on the 11th of month+1 and paid on the 21st–25th.
- **Atlassian (M1, M2):**
  - 0% revenue share on the first $1M of lifetime Forge revenue, and Atlassian handles tax.
  - **No payout until $500 of cumulative earnings**, then net 30 after month-end. The sponsor therefore fronts the operator tokens for about 5–7 months.
- **RapidAPI:** 25% fee plus PayPal fees, paid in the first week of month+2. **MCPize** takes 20%.
- **Projections:** all are rounded. Operator tokens are counted as a cost in every month.

---

## G1: Keyword→Brief (Apify, PPE)

**Upfront:** $50, the DataForSEO minimum top-up. It is consumed as COGS, but it is still cash out on day 0. No domain is needed. Total **$50**, inside the cap.

**Variable costs:**
- Brief: 0.8 × $0.04 = $0.032, minus SERP (~$0.002), keyword data (~$0.0001) and the page-fetch compute share (~$0.002). That leaves **$0.028**. If PAA expansion or AI Overview parameters are billed as SERP add-ons, net falls to ~$0.025.
- Metrics: 0.8 × $0.004 − ~$0.0006 = **$0.0026**, not the ideator's $0.0031.
- PayPal payout fees are ~2%.

**Leak to fix:** DataForSEO calls made for free-plan users are paid by us and never reimbursed. Gate the brief event to paying users.

**Sales needed:**
- $300 needs ~10.7k briefs a month.
- At a realistic ~$6 gross per paying user, that is ~70 paying users, not the ideator's 40. Apify user counts include free users, so ~70 paying means roughly 200+ total monthly users, which is about 30% of the shelf leader.

**Operator tokens:** $150 in month 1, $120 in month 2 (building the brief event), then ~$80 (light: scripted self-tests, README, issue replies).

| Month | Net rev $ | Other $ | Tokens $ | Monthly $ | Cumulative $ |
|---|---|---|---|---|---|
| Oct | 3 | 0 | 150 | −147 | −197 |
| Nov | 27 | 0 | 120 | −93 | −289 |
| Dec | 75 | 0 | 80 | −5 | −295 |
| Jan | 122 | 0 | 80 | +42 | −252 |
| Feb | 163 | 0 | 80 | +83 | −169 |
| Mar | 204 | 0 | 80 | +124 | −45 |

Gross revenue ramps $5 → $300, with net ≈ 68% of gross.

**Break-even:**
- Accrued: month 4. January earnings are paid Feb 21–25.
- $300 net plus tokens needs ~$560 gross a month, which is reached around month 9–12 if a price war doesn't compress margins.
- Downside: DataForSEO refuses resale, forcing BYO-key mode, which cuts net per brief roughly in half.

---

## G2: LongForm Transcripts (Apify, PPE)

**Upfront:** $5 OpenAI fallback credit; Groq is postpaid. Total **$5**.

**Variable costs per audio minute at $0.009:**
- 0.8 × $0.009 = $0.0072;
- minus Groq ($0.00067);
- minus compute and bandwidth (~$0.0004);
- leaves **$0.0061**.

The ideator's claim to be "far below the shelf" is only half true: `steadyfetch` already charges $0.006/min. I therefore model a blended realised price of ~$0.008, giving **~$0.0053/min**. At $0.006 the net is $0.0037.

The OpenAI fallback at $0.003/min costs more than half the net margin on every minute it handles, so keep it under 5% of volume. Gate free-plan users, because their Groq cost is ours. It is small, ~$7 per 10k minutes.

**Sales needed:**
- $300 needs ~49k minutes at list price, or ~57k blended (~820–950 audio hours).
- That is roughly 35–50 paying users at ~20 h/month. It depends heavily on a few agency-scale users.

**Operator tokens:** $150 build, $100 for chapters and RSS watch, then ~$80.

| Month | Paid min | Net rev $ | Tokens $ | Monthly $ | Cumulative $ |
|---|---|---|---|---|---|
| Oct | 1k | 5 | 150 | −145 | −150 |
| Nov | 8k | 42 | 100 | −58 | −207 |
| Dec | 15k | 80 | 80 | 0 | −208 |
| Jan | 22k | 117 | 80 | +37 | −171 |
| Feb | 28k | 148 | 80 | +68 | −103 |
| Mar | 34k | 180 | 80 | +100 | −3 |

**Break-even:** month 4–5 accrued, and cumulative around month 7. $300 net above tokens needs ~72k minutes a month, around month 10–14. Price compression is the main threat: each $0.001 cut removes ~13% of net.

---

## G3: AnswerShare API (MCPize + RapidAPI)

**Upfront:** $5 OpenAI + $5 Perplexity = **$10**. Workers Paid ($5/mo) is likely needed once `watch` crons run.

**Variable cost per 3-engine check:** $0.035–0.07; I use **$0.05**.

| Product | RapidAPI net (75%, −2% PayPal) | MCPize net (80%) |
|---|---|---|
| $29 plan, 300 checks, 50% used | $13.82 | $15.70 |
| $29 plan, 100% used | $6.32 | $8.20 |
| $99 plan, 1,200 checks, 50% used | $42.77 | $49.20 |
| $0.12 pay-per-call | $0.038 | $0.046 |

**Hidden fixed cost: the free tier.** 25 free checks × $0.05 = **$1.25 per active free key per month**. At 30–50 free keys that is $20–40/mo, with no revenue against it. MentionsAPI sells cached checks at $0.02, which is **below our cost floor**, so the price ceiling sits under COGS for the price-sensitive segment.

**Sales needed:** ~22 $29 subscribers at half usage. If heavy users concentrate on the plan, it is closer to 45. Covering tokens as well pushes the requirement past 30–50 subscribers on an unproven channel.

**Operator tokens:** $200 build, then ~$120 (three engine adapters drift, six listings, support).

| Month | Net rev $ | Free tier + infra $ | Tokens $ | Monthly $ | Cumulative $ |
|---|---|---|---|---|---|
| Oct | 0 | 8 | 200 | −208 | −218 |
| Nov | 0 | 19 | 120 | −139 | −357 |
| Dec | 14 | 31 | 120 | −137 | −494 |
| Jan | 33 | 35 | 120 | −122 | −616 |
| Feb | 66 | 39 | 120 | −93 | −709 |
| Mar | 85 | 43 | 120 | −78 | −787 |

**Break-even:** not within 12 months. Costs exceed realistic revenue throughout.

---

## C1: FunderFit

**Upfront:** domain $12 + sample-report LLM runs $5 = **$17**.

The ideator's $0 hosting is optimistic. Three years of 990-PF grant lines is likely 1–2 GB, which exceeds D1's free 500 MB per database. Use R2 plus Parquet, or pay $5/mo for Workers Paid. I model $5/mo.

**Variable cost per $39 report:**
- Lemon Squeezy ~$2.74;
- affiliate share 40% ($15.60) plus the 2% affiliate fee ($0.78);
- compute ~$1.

That leaves **$18.88 via an affiliate** and **$35.26 direct**.

Other price points:
- The $19 founding price nets only **$8.43** via an affiliate.
- The $99 Practice plan nets **$45.73** via an affiliate. The ideator's $52 omitted compute for 5 reports.

**Perk exposure:** each free member report costs ~$0.50–1. A large academy could redeem hundreds in a launch week, so cap redemptions per partner (for example, the first 100).

**Sales needed:**
- $300 needs 17 affiliate reports, or 9 direct, or ~7 Practice subscribers.
- Covering ~$120 tokens and $5 hosting as well needs ~23 affiliate reports.

| Month | Net rev $ | Hosting + perks $ | Tokens $ | Monthly $ | Cumulative $ |
|---|---|---|---|---|---|
| Oct | 0 | 5 | 250 | −255 | −272 |
| Nov | 26 | 25 | 150 | −149 | −421 |
| Dec | 83 | 35 | 120 | −72 | −493 |
| Jan | 143 | 25 | 120 | −2 | −495 |
| Feb | 228 | 20 | 120 | +88 | −407 |
| Mar | 247 | 20 | 120 | +107 | −300 |

The ramp assumes 2 partners go live in late November: 3 founding reports in November, 5–8 reports in each later month, and 1–2 Practice subscriptions from January.

**Break-even:** month 5, with cumulative around month 8–9. Margin per sale is good. The risk is binary partner uptake: with 0 partners, revenue is ~$0.

---

## C2: Client Safety Kit

**Upfront:** $15 for the seed library, plus $0–12 for a domain = **$15–27**. That assumes D2's ingest exists. If D2 is not live, C2 must build the OSHA ingest itself, adding ~$100–150 of build tokens but no cash.

**Fixed costs:** the optional native-Spanish spot-check (~$20/mo). Hosting is $0 while shared with D2.

**Variable costs:**
- Kit generation is ~$0.20 × up to 10 kits = $2 per licence.
- The $49 licence nets **$22.86 via an affiliate** and $43.44 direct.

**Pricing trap:** the "founding $29/mo **for life**" price nets only **$12.51** via an affiliate (40% for 12 months). Founders then sit at about half the margin of a $49 customer indefinitely. Cap the lifetime price at 12 months, or limit it to the first 10 seats.

**Sales needed:**
- $300 plus $20 fixed needs 14 consultants at $49 via an affiliate, 8 direct, or 26 at the founding price.
- Covering ~$150 tokens as well needs ~21 affiliate consultants at $49.

**Operator tokens:** content-heavy. The monthly briefs, branded kits per consultant and library upkeep cost ~$150/mo.

| Month | Subs | Net rev $ | Other $ | Tokens $ | Monthly $ | Cumulative $ |
|---|---|---|---|---|---|---|
| Oct | 0 | 0 | 0 | 250 | −250 | −277 |
| Nov | 0 | 0 | 0 | 150 | −150 | −427 |
| Dec | 2 | 26 | 20 | 150 | −144 | −571 |
| Jan | 4 | 83 | 20 | 150 | −87 | −658 |
| Feb | 6 | 98 | 20 | 150 | −72 | −730 |
| Mar | 8 | 145 | 20 | 150 | −25 | −755 |

**Break-even:** about month 8–9 if consultants keep accruing (churn is low by design). $300 net is reached around month 12+. The recurring margin is good, but the founding-price policy and the token load make this slow.

---

## C3: Interpreter Practice Lab

**Upfront:** domain $12 + TTS $6–12 + calibration runs $10 = **$28–34**. Paying the calibration rater $40 raises it to $74, still under the cap.

**Variable costs:**
- Inference is $0.80 for a median user and up to $3.50 for a heavy user.
- A $29 pass nets **$13.65 via an affiliate** (−40%, −2%, Lemon Squeezy, ~$1 inference) and $25.83 direct. The $19 founding price via an affiliate nets $8.43.
- **The flat school licence is the trap:** $150/mo for 40 students.
  - Direct at median usage it nets $108.
  - Via a partner it nets $45.
  - If all 40 students hit the cap it nets **~$0**.
  - Fix this with per-student caps of ~60 segments, or bill the $6 seat price (which nets $4.33 at median usage).

**Sales needed:** $300 needs 22 affiliate passes a month, or 3 direct school licences. The retail pool is small (CoreCHI ≈ 1,000 candidates a year).

**Operator tokens:** ~$200/mo. Content-heavy: 10 new dialogues and keys each month, calibration, school dashboards and partner reports.

| Month | Net rev $ | Other $ | Tokens $ | Monthly $ | Cumulative $ |
|---|---|---|---|---|---|
| Oct | 0 | 0 | 300 | −300 | −334 |
| Nov | 0 | 10 | 250 | −260 | −594 |
| Dec | 34 | 10 | 200 | −176 | −770 |
| Jan | 112 | 10 | 200 | −98 | −868 |
| Feb | 140 | 10 | 200 | −70 | −938 |
| Mar | 187 | 10 | 200 | −23 | −961 |

The ramp assumes 4 founding passes in December, 8–10 passes a month afterwards, and 1 partner school licence from March.

**Break-even:** month 10–12, and only if 2 school licences sign. School contracts take 8–16 weeks. Otherwise not within 12 months.

---

## I1: Zì Bot (Discord)

**Upfront:** domain **$12**.

**Variable costs:**
- A $4.99 Supporter month nets **$3.58** after Lemon Squeezy (the $0.50 fixed fee alone is 10%) and ~$0.60 inference.
- The $39 annual plan nets ~$2.41/month.
- After the move to Discord Premium Apps, Discord's ~30% cut makes it **$2.89**.
- Free users' "3 trial turns/week" cost a few cents each, ~$5–25/mo at 1–2k monthly active users.
- Founding pre-orders ($29/yr, $26.83 cash) arrive as one lump but carry 12 months of inference (~$7). Treat them as deferred revenue, not break-even.

**Sales needed:**
- $300 needs **84 Supporters**, or 104 on Discord billing.
- At 1.5–2% conversion, that requires ~4–7k monthly active users.
- Covering only the ~$100 tokens plus trial inference needs ~34 Supporters.

| Month | Net rev $ | Inference (free + founders) $ | Tokens $ | Monthly $ | Cumulative $ |
|---|---|---|---|---|---|
| Oct | 0 | 0 | 200 | −200 | −212 |
| Nov | 108 (4 pre-orders) | 0 | 150 | −42 | −254 |
| Dec | 108 (4 pre-orders) | 10 | 100 | −2 | −256 |
| Jan | 44 (12 monthly) | 15 | 100 | −71 | −327 |
| Feb | 73 (20) | 20 | 100 | −47 | −374 |
| Mar | 87 (24) | 25 | 100 | −38 | −412 |

**Break-even:** covering its own tokens takes until month 9–12, after the January and Chinese New Year peaks. $300 is not within 12 months. Server Pro at $7.99 (net $6.99) improves the mix, but admins of free communities rarely pay.

---

## I2: Episode Study Packs

**Upfront:** domain **$12**.

**Variable costs:**
- The ideator's $0.20–0.50 LLM cost per episode is low for polyphone-aware pinyin, translation, notes and exercises on ~4k characters. I use **~$1/episode** including ASR.
- Resulting nets:
  - Studio $39 (4 episodes): **$32.06**, an 82% margin;
  - Pro $79: $61.56;
  - pay-as-you-go $12: $9.81;
  - founding $29 month: $22.69.
- Free sample packs cost ~$1 each.
- **Revisions are the hidden cost:** each email revision is an operator session, already included in the token budget.

**Sales needed:** $300 needs **10 Studio subscribers**. Covering ~$100 tokens as well needs 13. The ideator's ceiling of 100–200 creators makes the $1k stretch roughly the maximum.

**Operator tokens:** $150 build and list, $120 during outreach, then ~$100.

| Month | Net rev $ | Other $ | Tokens $ | Monthly $ | Cumulative $ |
|---|---|---|---|---|---|
| Oct | 0 | 5 | 150 | −155 | −167 |
| Nov | 46 | 5 | 120 | −79 | −246 |
| Dec | 98 | 0 | 100 | −2 | −248 |
| Jan | 160 | 0 | 100 | +60 | −188 |
| Feb | 226 | 0 | 100 | +126 | −62 |
| Mar | 226 | 0 | 100 | +126 | +64 |

The ramp: 2 founding months in November, 3 Studio in December, then 4–5 Studio + 1 Pro, with one churn by March. It assumes a second outreach batch (up to 120 contacts).

**Break-even:** month 4, with cumulative around month 6. This has the best margin per sale in the C/I set. Its limits are market size and churn, not unit cost.

---

## I3: Role-Play Room

**Upfront:** domain **$12**.

**Variable costs:**
- A $149 class-semester licence nets **$114.93** after Lemon Squeezy and ~$25 semester inference for 25 students.
- The $99 founding class nets $67.81.
- A $12 student seat nets **$9.81**, so a 25-student class yields $245 per semester.

**The ideator's "6–11 classes" is wrong.** A class pays once per semester (two per year). $300/mo is $1,800 per semester, which needs **~16 licence classes**, or ~7–8 classes on the student-seat model. The seat model is clearly the better economics, if instructors will require it.

**Operator tokens:** $200 build, $150 during outreach, ~$100 during the semester, $60 off-season.

| Month | Net rev $ | Tokens $ | Monthly $ | Cumulative $ |
|---|---|---|---|---|
| Oct | 0 | 200 | −200 | −212 |
| Nov | 0 (trials cost ~$9) | 150 | −159 | −371 |
| Dec | 137 (2 founding) | 120 | +17 | −354 |
| Jan | 232 (2 licences) | 100 | +132 | −222 |
| Feb | 0 | 60 | −60 | −282 |
| Mar | 0 | 60 | −60 | −342 |

**Break-even:** December and January look positive only because cash arrives as a lump once a semester. Sustained coverage needs the fall 2027 cohort, around month 11–12 at best. Between semesters, the tokens must be pre-funded from the lump.

---

## M1: ChatRelay for Jira (Forge)

**Upfront:** **$0–8**, a Google Workspace test month only if the sponsor has none. There are no Atlassian fees.

**Fixed costs:** $0. Forge stays inside the free allowance, since a webhook post takes milliseconds.

**Variable costs:** 0% revenue share up to $1M, and Atlassian covers payment processing and tax. Net ≈ gross.

**Revenue per site:** I lower the ideator's blended $25 to **~$20**. At $0.35/user, a 40-user site pays $14. Sites with 10 or fewer users (Jira Free) pay $0.

**Sales needed:** **15 paying sites** for $300, or 18 to also cover ~$60 tokens.

**Operator tokens:** $150 build, $80 for listing and review, then ~$60. This is a running integration needing light maintenance and support.

| Month | Paying sites | Net rev $ | Tokens $ | Monthly $ | Cumulative $ (accrued) |
|---|---|---|---|---|---|
| Oct | 0 | 0 | 150 | −150 | −158 |
| Nov | 0 (evaluations) | 0 | 80 | −80 | −238 |
| Dec | 3 | 60 | 60 | 0 | −238 |
| Jan | 8 | 160 | 60 | +100 | −138 |
| Feb | 14 | 280 | 60 | +220 | +82 |
| Mar | 18 | 360 | 60 | +300 | +382 |

**Cash reality:**
- Cumulative earnings first pass the **$500 payout threshold** at the end of February. Paid net 30, so the **first cash arrives around late March (month 6)**.
- The sponsor fronts ~$470 of tokens until then.

**Break-even:** month 3–4 accrued, with $300 net above tokens around month 6. Main risk: the free competitor caps price and site count. At 8 sites, revenue covers tokens but never reaches $300.

---

## M2: SpecView for Confluence (Forge)

**Upfront:** **$0**.

**Fixed costs:** $0. Rendering is client-side and scan calls stay within the Forge allowance.

**Variable costs:** 0% revenue share, so net ≈ gross.

**Revenue per site:** ~$12–15 per paying site. Orphan pricing ($1 for 10 users, ~$0.10/user at 100 users) anchors it low.

**Sales needed:** 20–25 paying sites for $300, plus 4–5 more to cover ~$60 tokens. That is ~0.5% of the ~5,500-install orphan pool.

**Operator tokens:**
- $100 for the viewer build.
- $150 in November for the converter, which is genuinely harder work: each orphan's storage format, dry-run and rollback.
- ~$60 afterwards.
- Plus a reserve for converter incidents, since one bad bulk rewrite costs a support-heavy month.

| Month | Paying sites | Net rev $ | Tokens $ | Monthly $ | Cumulative $ |
|---|---|---|---|---|---|
| Oct | 0 | 0 | 100 | −100 | −100 |
| Nov | 0 | 0 | 150 | −150 | −250 |
| Dec | 1 | 15 | 60 | −45 | −295 |
| Jan | 4 | 60 | 60 | 0 | −295 |
| Feb | 7 | 105 | 60 | +45 | −250 |
| Mar | 10 | 150 | 60 | +90 | −160 |

**Cash reality:** the $500 threshold is not reached until about April, so **first cash arrives around month 7–8**. If M1 runs on the same partner account, the threshold is pooled and cash arrives earlier.

**Break-even:** month 5 accrued, with $300 around month 10–12. The economics are excellent per unit but small per site.

---

## M3: SheetSync (Apify, PPE)

**Upfront:** **$0**.

**Fixed costs:** $0. Compute is ~$0.0003–0.001 per run.

**Pricing bug:** the launch promo makes "the first 1,000 rows of each run free", but the ideator's own usage profile is ~200 rows per run. During the promo a typical user therefore pays only the $0.005 start event: **~$0.50 gross, $0.40 net per user per month**, not $8.50. Make the free allowance 1,000 rows **per user per month**, or end the promo after 2–3 weeks.

**Variable costs after the promo:**
- 100 runs × ($0.005 + 200 × $0.0004) = $8.50 gross per user;
- × 0.8, minus ~$0.07 compute;
- leaves **$6.73 net**.
- Many switchers will run less than the incumbent's power users, so I use ~$5 per paying user.

**Sales needed:** ~45 paying users at $6.73, or ~60 at $5. The binding constraint is that a free incumbent sets a $0 reference price.

**Operator tokens:** $100 build, then ~$50. This is the lightest operator load in the round: a canary self-test and issue replies.

| Month | Paying users | Net rev $ | Tokens $ | Monthly $ | Cumulative $ |
|---|---|---|---|---|---|
| Oct | ~15 (promo) | 6 | 100 | −94 | −94 |
| Nov | ~25 (promo ends mid-month) | 88 | 60 | +28 | −66 |
| Dec | 25 | 125 | 50 | +75 | +9 |
| Jan | 32 | 160 | 50 | +110 | +119 |
| Feb | 38 | 190 | 50 | +140 | +259 |
| Mar | 42 | 210 | 50 | +160 | +419 |

**Break-even:** month 2–3, with cumulative around month 3. November earnings are paid Dec 21–25. $300 net is reached around month 9–12 at best. If the Apify-staff incumbent fixes its failure rate, revenue plateaus near $100–150.

---

## U4: AI-matched job board, in two variants

**Upfront for both:** domain **$12**. Use Cloudflare or Netlify rather than Vercel, because Vercel Hobby is non-commercial.

**Shared cost drivers:**
- **Job index embeddings:** ~$1 per full re-embed of 50k jobs, plus ~$0.10/day for new jobs. Negligible.
- **Match explanations:** this is the real per-user cost. Top-5 to 10 explanations daily with a small model run **$0.15–0.30 per active user per month**; a mid-tier model costs $1+.
- **Email:**
  - Resend's free tier is 100/day, so past ~100 daily-alert users the cost is $20/mo (50k emails/mo).
  - At ~3k users it becomes $35–90/mo. SES would be cheaper but needs an AWS account.
- **Vector DB:** Supabase free tier (500 MB) suffices to ~50k jobs at 384–512 dimensions. Moving to Pro adds $25/mo.
- **Operator tokens: ~$250/mo, the highest in the round.** The work is multi-source ingestion, de-duplication and expiry, SEO pages, emails, support and matching tuning.

### U4a: free for seekers, then paid employer posts
- **Revenue:** a $149 post nets **$139.93**. **3 posts a month** reach $300, and ~5 also cover tokens and infra. That is few sales, but employers pay only for an audience. Niche boards usually need ~10k+ monthly seekers first, which realistically takes 12–18 months with no channel.
- **Months 1–6:** revenue $0. Costs grow with free users (inference $15 → $135; email and DB $20 → $45).

| Month | Free active users | Infra $ | Tokens $ | Cumulative $ |
|---|---|---|---|---|
| Oct | 0 | 0 | 300 | −312 |
| Nov | 100 | 20 | 250 | −582 |
| Dec | 250 | 58 | 250 | −890 |
| Jan | 500 | 95 | 250 | −1,235 |
| Feb | 700 | 150 | 250 | −1,635 |
| Mar | 900 | 180 | 250 | **−2,065** |

**Break-even:** not within 12 months. The more successful the free side becomes, the faster it burns cash.

### U4b: $12/month seeker subscription from day 1
- **Revenue:** $12 nets **$10.15** after Lemon Squeezy and inference.
  - **30 subscribers** reach $300; ~57 also cover tokens and infra.
  - At $19 the net is $16.71, so 18 subscribers reach $300.
- **Retention:** churn is structurally high (~30–40%/mo) because subscribers leave when hired, so the funnel must keep refilling. January is the peak job-search month, which helps.

| Month | Paid subs | Net rev $ | Infra $ | Tokens $ | Monthly $ | Cumulative $ |
|---|---|---|---|---|---|---|
| Oct | 0 | 0 | 0 | 300 | −300 | −312 |
| Nov | 2 | 21 | 10 | 250 | −239 | −551 |
| Dec | 5 | 52 | 30 | 250 | −228 | −779 |
| Jan | 12 | 124 | 45 | 250 | −171 | −950 |
| Feb | 16 | 165 | 50 | 250 | −135 | −1,085 |
| Mar | 18 | 185 | 55 | 250 | −120 | −1,205 |

**Break-even:** not within 12 months at P50, because free AI job tools (Hiring Cafe, Jobright and others) cap conversion. The best case is month 10–12 with a narrow niche and $19 pricing. U4b is clearly the better of the two variants. It still scores below every non-G3 idea because of the token load and the absence of a channel.

---

## Cross-cutting observations

1. **Fastest cash:** M3 and G1/G2 on Apify (cash from late December), then M1 (accrued break-even early, but first cash only around month 6).
   - **Lowest burn:** M1, M2 and M3 (~$50–60/mo tokens).
   - **Best margin per sale with partners:** C1 and I2.
2. **Apify concentration:** G1, G2 and M3 (plus T2) share one platform. Only one should be chosen. M3 has the lowest burn but the promo bug. G1 has the larger upside but supplier risk.
3. **Atlassian's $500 threshold** makes M1/M2 profitable on paper about 2–3 months before any money lands. The sponsor must pre-fund ~$300–500 of tokens.
4. **Pricing fixes that change the numbers:**
   - M3: end the per-run free 1,000 rows.
   - C2: no "for life" founding price.
   - C3: cap per-student usage on the flat school licence.
   - I3: prefer the student-seat model.
   - G1 and G2: gate free-plan users before calling paid external APIs.
