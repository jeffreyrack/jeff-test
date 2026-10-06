# Media Buyer ideas: round 3 (capital allowed)

_Persona: The Media Buyer (ideator-media-buyer). Date: Tue 2026-10-06. Binding parameters: `../PARAMS.md` ($10k cap with a preference for under $1k; sponsor time at $300/h; payback ≤ 12 months and a P10 loss of ≤ ~50% for anything over $1k; compare returns with 4%/yr T-bills)._

**Thesis.** Every earlier round failed on the same thing: no channel reached the buyer within 30 days. Capital can buy that channel, but only where the maths works. Each idea below has:
- a buyer who can be targeted precisely (search intent, subreddit, or a gift-intent audience);
- a capped test of $300–500 with a pre-committed kill rule;
- scale spending released only after the test passes.

Two ideas are paid-distribution fixes for earlier ideas whose fatal flaw was distribution:
- **B1** fixes **U3-W**, the HSK 3.0 speaking-mock wedge.
- **B2** fixes **D2** InspectionWatch. Its weak spot was the channel (sales score 4): the planned buyer, safety consultants, can't be reached. B2 changes the buyer to one that searches.

**B3** is new. It is a physical product with no handling, launched into the Q4 gift peak.

### Shared benchmark sheet (Oct 2026)
| Channel | CPC | CPM | CTR | CVR | Source |
|---|---|---|---|---|---|
| Google Search, all industries (Apr 2025–Mar 2026) | $5.42 avg | — | 6.64% | 8.18% (all conversion types, mostly leads) | WordStream 2026 |
| Google Search, education | $2.40 | — | — | 3.39% | Usermaven/SEJ 2026 roundup |
| Google Search, business services / industrial | $5.87 | — | — | 4.85% / 3.37% (industrial services) | WordStream 2026; Webtonic |
| Google Search, general construction | ~$6.45 | — | — | 3.4% (materials) | Webtonic 2026 |
| Reddit Ads | $0.50–3.50 (median $1.25–1.85) | median ~$6.50 | — | — | Stackmatix 2026 |
| Meta (FB/IG) | $0.78 traffic / $1.70 blended | median ~$14 (+20% YoY); **Q4 +25–50%, BFCM week 2–3×** | gifts ~4% (highest category) | e-com avg 2.7%, top quartile 4.1% | ContentStudio 2026; Lebesgue 2026 |
| LinkedIn, construction | $5–9 (narrow titles $15+) | — | — | CPL $50–110 | ClickMinded / GrowthSpree 2026 |

**How the CVRs are used:** benchmark CVRs mix leads and purchases. For purchases from cold traffic, I haircut them to 2–4%.

**Costs included in every unit-economics model:**
- merchant-of-record or Stripe fees;
- per-unit inference;
- AI operator tokens: $60–100/mo per idea; the incremental cost is lower when infrastructure is shared;
- sponsor hours at $300/h.

---

## B1 — HSK 3.0 Speaking Mock: paid search plus creator affiliates (paid-distribution fix for U3-W)

- **Persona:** The Media Buyer
- **One-liner:** A web-based, timed, exam-format mock trainer for the new **integrated speaking section of HSK 3.0 Levels 3–6**. It sells for a one-time $29 per level, or $39 for a two-level bundle, to English-speaking candidates registered for the first HSK 3.0 sittings (13 Dec 2026 onward). Buyers are reached through high-intent Google Search, subreddit-targeted Reddit ads, and 30%-commission YouTube/blog affiliates.
- **Channel & benchmarks (CPC/CPM, CTR, CVR, with sources):**
  - **Google Search, exact and phrase match** on new long-tail terms: "HSK 3.0 speaking", "new HSK 3 speaking test", "HSK 4 speaking practice", "HSK 3.0 mock test".
    - **CPC:** the education average is $2.40 (3.39% CVR). These terms are new and thin, so I plan on **$0.50–1.20**, with geo-targeting limited to US/CA/UK/AU/NZ/SG/MY/EU.
    - **CTR:** 6–9% on exact match.
    - **CVR** (landing page with a free single-task demo → purchase): **3–5%**.
  - **Reddit Ads**, community-targeted (r/ChineseLanguage, r/LearnChinese and HSK keyword targeting): CPC $0.50–1.50, median CPM ~$6.50. CVR is lower (2–3%) because the intent is weaker.
  - **Affiliates:** the Lemon Squeezy affiliate programme at 30%, offered to small Chinese-learning YouTubers and bloggers who already publish "HSK 3.0 changes" videos. CAC = 30% of price, paid only on a sale.
- **CAC / LTV / payback:**
  - **Net first purchase (blended):** $29 single / $39 bundle → **$33 average**.
    - Lemon Squeezy fee (5% + $0.50): −$2.15.
    - Speech scoring plus LLM grading with capped attempts (~25 scored minutes per buyer: Azure pronunciation assessment plus a small LLM): −$2.50.
    - **Net: ≈ $28.35.**
  - **CAC by case (search):**

    | Case | CPC | CVR | CAC | First-purchase LTV:CAC |
    |---|---|---|---|---|
    | P10 | $1.40 | 2.5% | $56 | 0.5 |
    | P50 | $0.70 | 3.8% | **$18.40** | **1.54** (passes the ≥ 1.5 bar, barely) |
    | P90 | $0.50 | 5% | $10 | 2.8 |

  - **Affiliate CAC:** $10–12 per sale, a 2.4–2.8 ratio by construction.
  - **Repeat:** about 20% buy the next level within 6 months. This is upside only and excluded from the gate.
  - **Payback:** on search spend, payback is immediate on each sale. Capital payback is under "Payback" below.
- **Capped ad test & kill rule:**
  - **Budget:** $300 over 14 days: $200 Google Search, $100 Reddit. It runs against a **live pre-order page** with a free demo task.
  - **Pass:**
    - blended CAC ≤ **$22** on at least 8 pre-orders; **or**
    - CAC ≤ $30 on at least 5 pre-orders **plus** at least 60 email sign-ups for the free demo. In this case, test once more at $150 with the best ad group only.
  - **Kill:**
    - $150 spent with 0 pre-orders: stop paid and keep affiliates only; **or**
    - 14-day CAC above $30: stop paid; **or**
    - refund rate above 15%.
  - **Scale:** after a pass, a $400 tranche, then spend funded from revenue, capped at 3× the trailing net CAC headroom. Spend is weighted towards registration windows: the ~4–6 weeks before each monthly sitting.
- **Demand test:**
  - **Day 0 check, before any build:** verify the HSK 3.0 L3–L6 speaking-task specs and the 13 Dec sitting on chinesetest.cn. Sources conflict on 1 Jul vs 13 Dec as the first regular HSK 3.0 sitting.
  - **The test itself:** a $29 pre-order (refundable, delivery promised by 1 Nov) on a landing page with one free demo speaking task. Traffic comes from the $300 paid test above.
  - **Pass:** at least 8 pre-orders in 14 days at CAC ≤ $22. **Fail:** fewer than 5 pre-orders, which means refund everyone and kill.
- **Customer:**
  - English-speaking adults at HSK 2–4 level who have registered or plan to register for an HSK 3.0 sitting. Typical reasons are a scholarship (CSC), a university application or a job in China or Taiwan.
  - Where they hang out: r/ChineseLanguage and r/LearnChinese, Chinese-learning YouTube channels, Pleco and Anki.
  - What they already pay for: exam fees of $30–80, HelloChinese/SuperChinese ($12–25/mo), Mandarin Temple ($19/mo, which already includes HSK mocks), and italki tutors.
- **Problem / desire:** "I've never done a speaking test, the format is new, and HSK 2.0 materials don't cover it. I want to rehearse the exact tasks under time pressure and know which tones and sentences are failing."
- **Offering:**
  - Per level: 5 full timed mocks in the official task order: read-aloud, picture description, short answers, opinion with a reason (L5–6).
  - Grading:
    - read-aloud is scored per syllable by a pronunciation-assessment API, with the learner's pitch curve shown against the native model;
    - free-response tasks are graded by an LLM against a published-style rubric.
  - Model answers are native-recorded once, using contractor capital.
  - After each session: a "weak tones and phrases" error report, plus an Anki export.
  - **No score prediction is claimed.** CTI has not published how speaking combines into the pass.
- **Price & revenue model:**
  - One-time $29 per level, or a $39 two-level bundle (L3+L4 or L5+L6).
  - Access runs until 30 days after the buyer's chosen exam date.
  - Attempts are capped at 3 scored attempts per mock, to bound inference.
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Native-speaker contractor (Upwork/italki teacher): QA of all prompts plus recorded model answers, ~10 h at $25 | $250 |
| Domain | $12 |
| Capped ad test (Google $200 + Reddit $100) | $300 |
| Scale tranche, released only on pass | $400 |
| **Total** | **$962** (under the $1k preference; $562 at risk before the pass decision) |

### Monthly running costs (excluding operator tokens)
- Hosting: Cloudflare Pages/Workers free tier, $0–5.
- Speech scoring plus LLM grading: ~$2.50 per buyer, capped by attempts.
- Lemon Squeezy: 5% + $0.50 per sale.
- Affiliate commissions: 30% of affiliate sales.
- Ads: revenue-funded after the scale tranche, at a P50 of ~$400/mo.
- Operator tokens: ~$80/mo.

**P50 steady month (Dec–Apr):**

| Line | Amount |
|---|---|
| Sales: 18 paid + 8 affiliate + 6 organic/lead-magnet = 32 at $33 | $1,056 revenue |
| Lemon Squeezy fees | −$85 |
| Inference | −$80 |
| Affiliate commissions | −$80 |
| Ads | −$400 |
| Hosting | −$10 |
| Tokens | −$80 |
| **P50 net** | **≈ $320/mo** |

The off-peak months (summer) are ~$100. **The year averages about $250/mo at P50.**

Other cases:
- **P10:** the test fails and $562 is lost (capital) plus $750 of sponsor time.
- **P90:** about $700/mo in peak months.

**Return:**
- Year-1 net ≈ $2,250, minus $750 of sponsor setup = **$1,500 on $962**, about **155% annualised** vs 4% T-bills.
- **Payback of capital:** about month 4 (Feb 2027) at P50; about month 7 including sponsor time.

### Customer acquisition plan
1. A live pre-order page, with a free demo task, goes up by day 10.
2. Google Search on exact and phrase match only, with HSK 3.0 speaking-specific keywords. Negatives: "free", "pdf", "download", "HSK 2.0", "HSKK", plus Chinese-language queries.
3. Reddit community-targeted ads run in parallel, as a small test cell.
4. The free demo collects an email address. A 4-email sequence keyed to the buyer's exam date ("you sit in 23 days: here's your read-aloud weak-tone report") converts sign-ups who didn't buy.
5. Affiliate pitches go to about 15 creators who already post "HSK 3.0 changes" content. The operator sends them one-to-one from a real mailbox, each with a free account.
6. Spend is re-weighted towards each registration window (monthly sittings in 2027).

### Initial traffic approaches (ranked by expected speed)
1. **Google Search** on new HSK 3.0 speaking terms. There is effectively no organic incumbent on many exact phrases. Clicks arrive within 24 h of ad approval.
2. **Reddit Ads** targeting the communities above. Same-day delivery, and it doesn't depend on the human posting.
3. **A genuine Reddit post by the sponsor:** "Free HSK 3.0 speaking mock: here's the new format". It is useful news, not an app pitch, and takes about 0.5 h.
4. **Creator affiliates:** slower, 2–6 weeks; pay only on sale.
5. **Free AnkiWeb 2.0→3.0 change deck** as a lead magnet. A slow trickle, but it compounds.

### Path to first sale
| Day | Step |
|---|---|
| D0–1 | Verify the specs and dates. Sponsor: Lemon Squeezy KYC, Google Ads advertiser verification, Reddit ads account (about 2 h). |
| D2–9 | Operator builds the demo task, the pre-order page and the first level (L3), and hires the native contractor. |
| D10 | Ads go live. |
| ~D14–18 (P50) | First pre-order. |
| D24 | Pass/kill decision. |
| ~D26 | Full L3–L4 delivery. |
| ~D30–40 | First cash (Lemon Squeezy payout cadence). |

**Ideator estimate:** first sale about day 16, first cash about day 35. Apply the 3–5× skeptic haircut to the organic channels, but not to paid search, which is the point of buying it.

### Who does what
- **AI operator:** build; ad copy and keyword lists; daily bid/negative-keyword management through the Google Ads API (developer token: basic access); landing-page A/B tests; email sequences; affiliate pitches and payouts through Lemon Squeezy; support inbox; monthly spec-change checks.
- **Human sponsor:** one-time, about 2.5 h ($750): Lemon Squeezy KYC, Google Ads advertiser verification, Reddit Ads account, approving the native contractor. Optional 0.5 h Reddit post. **Recurring: ~0 h/mo.** Within the gate: $250 net allows 0.8 h.
- **Contractors:** native speaker for prompt QA and model-answer audio (one-time, plus about 1 h per new level).

### Moat — why not just ask ChatGPT?
- **The substitute:** ChatGPT and Gemini voice can role-play an HSK speaking task.
- **What they don't do:**
  - the exact timed task sequence;
  - grounded per-syllable tone scoring with pitch curves;
  - native-recorded model answers;
  - an exam-date-keyed plan.
- **Funded competitors:** Mandarin Temple ($19/mo), SuperTest, HanSpik and the official HSK Mock app (an HSKK mock costs about ¥60, roughly $8.40) already sell mocks.
- **Honest view:** **the moat is the paid distribution and the timing, not the product.** What compounds:
  - the email list of candidates, who return for the next level;
  - the affiliate roster;
  - reviews and testimonials;
  - the Anki lead-magnet deck, which keeps generating sign-ups.

### Biggest risks (ideator's own view)
- **Search volume is small and spiky.** English-speaking takers of L3–6 are a minority of HSK candidates, most of whom are in Asia. Paid search may cap at about 20 sales/mo. P50 sits just below the $300 target on an annual average.
- **Incumbents are cheaper.** The official mock costs about $8 and Mandarin Temple is $19/mo. If CVR comes in at 2.5% or less, LTV:CAC falls below 1, and the kill rule fires on day 24.
- **Accuracy and trust:** an unnatural model answer or a wrong spec kills conversion. Mitigations: native QA, a day-0 spec check, no "official" claims, nominative use of "HSK" only, and an AI-content label.

---

## B2 — SubWatch: OSHA-history monitoring for general contractors' subcontractor lists (adjacent to D2; fixes its channel flaw)

- **Persona:** The Media Buyer
- **One-liner:** A general contractor pastes in a subcontractor list. SubWatch returns each sub's 5-year federal OSHA inspection and citation history: matched across name variants, with penalties, fatality and serious flags, and a prequalification PDF. It then emails an alert whenever a monitored sub gets a new inspection or citation. Prices are $79/mo (50 subs) and $199/mo (250 subs). Customers are acquired through Google Search for "check a contractor's OSHA record" intent.
- **Fatal flaw fixed:** D2's sales score was 4 because its buyer, independent safety consultants, has no searchable intent and was reachable only through sponsor emails and LinkedIn. B2 reuses D2's DOL ingest but sells to a buyer that **searches**. GC safety and prequalification staff have a recurring, budgeted need: OSHA's multi-employer citation policy exposes the GC to its subs' hazards.
- **Channel & benchmarks (CPC/CPM, CTR, CVR, with sources):**
  - **Google Search** on phrases like "check contractor OSHA violations", "subcontractor OSHA history", "subcontractor prequalification OSHA", "OSHA violations by company".
    - Benchmarks: business services CPC $5.87 with 4.85% CVR; general construction ~$6.45; industrial services CVR 3.37%. These long-tail informational phrases face little advertiser competition, so I plan on **$2.50–6.00, P50 $3.50**.
    - Landing CVR to the free "check 5 subs now" tool (email-gated, instant result): **8–14%**. Lead-gen benchmarks reach 9.5% for top construction campaigns.
    - Free check → paid (14-day trial with card, then $79+): **4–12%, P50 8%**.
  - **LinkedIn**, retargeting only: CPC $5–9 in construction, and $15+ on narrow titles. Cold LinkedIn is too expensive at this ARPA.
- **CAC / LTV / payback:**
  - **ARPA and margin:** blended ARPA $95/mo (80% Starter, 20% Pro). Lemon Squeezy fees −$5.25; per-account compute and tokens −$1. **Margin $88.75/mo.**
  - **LTV:** churn of 4%/mo at P50 (it is a workflow tool, sticky once the sub list is loaded), capped at 18 months for LTV. **LTV = $1,598.**
  - **CAC by case:**

    | Case | CPC | Click → free check | Free → paid | CAC | LTV:CAC |
    |---|---|---|---|---|---|
    | P10 | $6 | 6% | 4% | $2,500 | 0.6 |
    | P50 | $3.50 | 10% (CPL $35) | 8% | **$437** | **3.7** (passes ≥ 3) |
    | P90 | $2.50 | 14% | 12% | $149 | 10.7 |

  - **CAC payback:** about 4.9 months at P50.
- **Capped ad test & kill rule:**
  - **Day 0 ($0) policy pre-check:** submit the ads for review before any spend. Google's *Government documents and official services* policy was tightened on 2026-10-05 and covers "information derived from official registries".
    - Copy positions SubWatch as **risk-monitoring software**, never as an "OSHA records lookup".
    - If the ads are disapproved and the appeal fails, kill the paid channel at $0.
  - **Budget:** $500 over 21–30 days on Google Search, exact and phrase match only.
  - **Pass** (both conditions):
    - CPL for the free check ≤ $50 by day 14; **and**
    - at least 3 card-on-file trials by day 21, **or** at least 1 paid conversion by day 30.
  - **Kill:**
    - CPL above $80 at $250 spent; **or**
    - 0 trials at $500 spent.
  - **Partial pass** (CPL passes but trials don't): change the offer once (annual prepay at $790 or a lower $49 tier), then re-test with $200.
  - **Scale:** a $400 tranche, then revenue-funded spend of up to ~$600/mo while blended CAC ≤ $530 (a 3:1 ratio on the capped LTV).
- **Demand test:**
  - **Offer:** the free "check 5 subs" instant report, plus a "Monitor your list: $79/mo" upsell with card on file.
  - **To whom:** US GC safety and prequalification staff, via Google Search.
  - **Pass/fail:** the $500 test rule above. The free check also measures **search intent** before the monitoring pipeline is fully built.
  - **Policy gate:** the ad-approval check on day 0 costs $0.
- **Customer:**
  - Safety directors, prequalification coordinators and project managers at US general contractors with 10–200 staff.
  - These firms are too small for, or don't want to pay for, Highwire, Avetta, ISNetworld or TradeTapp, which are funded by the subs or by enterprise budgets.
  - Where they hang out: Google; the AGC, ABC and ASSP construction practice specialty; LinkedIn.
  - What they already pay for: Procore, prequal questionnaires, EMR letters from insurers.
- **Problem / desire:** "Before award we're supposed to check the sub's OSHA history. The OSHA establishment search is one name at a time, misses name variants, and nobody re-checks a sub after it's approved. Then a sub gets a serious citation on another job and we find out from the inspector."
- **Offering:**
  - **Matching:** list upload (CSV or paste) → fuzzy matching to OSHA establishments (DBA, LLC and Inc. variants; city and state disambiguation), with human-confirmable match suggestions.
  - **History report:** 5-year history per sub, giving inspection type, serious, willful and repeat counts, penalties, fatality and catastrophe flags, and status (open, contested, closed).
  - **Prequalification PDF** per sub.
  - **Alerts:** a daily delta from the DOL enforcement API, emailed when any monitored sub gets a new inspection or citation.
  - **Data presentation:** DOL fields quoted verbatim with source links, plus "citations may be contested; an inspection is not a violation".
- **Price & revenue model:** subscription: Starter $79/mo (50 subs), Pro $199/mo (250 subs plus a shared team inbox), annual at 2 months free. Sold through Lemon Squeezy (merchant of record; handles SaaS sales tax).
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Domain | $12 |
| Capped Google Search test | $500 |
| Scale tranche, released only on pass | $400 |
| DOL API and Cloudflare free tiers | $0 |
| **Total** | **$912** (under the $1k preference; $512 at risk before the pass decision) |

### Monthly running costs (excluding operator tokens)
- Hosting and database: $0–10 (D1/Neon free tiers).
- Email: $0–20 (Resend; alerts are well under the cap).
- Lemon Squeezy: 5% + $0.50.
- Ads: P50 ~$600/mo once scaling.
- Incremental operator tokens: ~$60/mo, since the ingest and self-test library is shared with D2 (otherwise ~$100).

**P50 trajectory:**
- About 1.4 new customers per month from $600/mo of ads, plus a trickle from organic and word of mouth.
- **Month 6:** about 8 accounts, ≈ $710 margin against $660 of ads and tokens, which is **≈ break-even**.
- **Month 12:** about 14 accounts → **≈ $540/mo net**.
- **Year-1 cumulative:** ≈ +$780 before sponsor time; **≈ +$180 after** 2 h of setup ($600).

**Return:**
- Year 1 is about **20% on $912**, vs 4% T-bills. This is a SaaS J-curve.
- At P50, year 2 runs at about $540–900/mo net, roughly 700% on the original capital.

**Payback of capital:** about month 10–11 at P50 (under 12).

**Other cases:**
- **P10:** the test fails and the loss is $512 (56% of the committed $912, but only $512 is ever spent) plus $600 of sponsor time.
- **P90:** about $1,500/mo net by month 12.

### Customer acquisition plan
1. On day 0, ads are submitted for policy review. On day 1, the free check is live, rebuilt on D2's ingest.
2. Google Search runs exact and phrase match on contractor-OSHA-history intent. Negatives: "complaint", "report", "file", "jobs", "training", "10 hour", "30 hour", "card".
3. Free check: the email-gated instant report, with a monitoring CTA in the report itself ("2 of your 5 subs had serious citations in 2025. Get alerted next time").
4. Trial nurture: on day 3 a "what changed on your list" digest; on day 10 a sample alert.
5. LinkedIn retargeting of free-check users only.
6. The prequalification PDF footer carries "Generated by SubWatch". This is an organic loop: PDFs are forwarded to owners and sureties.

### Initial traffic approaches (ranked by expected speed)
1. **Google Search** (above). Clicks arrive within 24–48 h of approval.
2. **Microsoft/Bing Ads** import of the same campaign. These clicks are usually 20–40% cheaper, and Bing users skew towards desktop and B2B. Live the same week.
3. **D2's channels as a cross-sell:** D2's safety consultants advise GCs. Use a "refer a GC" link with a 20% recurring commission. 2–4 weeks.
4. **A sponsored placement in a construction-safety newsletter** (a single send at $150–400). Only after the search test passes, to measure CAC against the search benchmark.

### Path to first sale
| Day | Step |
|---|---|
| D0 | Policy pre-check submitted. Sponsor: Lemon Squeezy KYC (shared with D2 if done), Google Ads advertiser verification, DOL key (about 2 h). |
| D1–7 | Fuzzy-matching layer and free check built on D2's ingest. |
| D8 | Ads live. |
| ~D10 | First free checks. |
| ~D20–30 | First card-on-file trials. |
| ~D35–50 (P50) | First paid conversion. |
| ~D50–65 | First cash. |

**Ideator estimate:** first paid sale about day 40.

### Who does what
- **AI operator:** ingest, matching and alert pipeline; nightly self-test; ad management through the API; negative-keyword mining; nurture emails; support by email only; churn surveys; DOL API breakage watch.
- **Human sponsor:** one-time, about 2 h ($600). **Recurring: ~0.25 h/mo** for refund and dispute approval and any legal letter. **No sales calls**: email-only support is stated on the pricing page. Within the gate: $540 net allows 1.8 h.

### Moat — why not just ask ChatGPT?
- **The substitutes:**
  - a chatbot with browsing can look up one company, but it can't fuzzy-match 50 subs against the enforcement dataset or watch them daily;
  - the free OSHA establishment search does one name at a time and has no alerts;
  - enterprise prequalification platforms (Highwire, Avetta, ISN) cost thousands and push fees onto the subs.
- **What compounds:**
  - every customer's loaded sub list, which is switching cost;
  - the match-confirmation corrections, which make a proprietary entity-resolution table that improves matching for everyone;
  - the PDF footer loop;
  - shared infrastructure with D2.
- **Clone risk is real** (DOL data is public). The ads, the loaded lists and the match table are the edge.

### Biggest risks (ideator's own view)
- **Ad policy:** Google's government-documents policy, tightened on 2026-10-05, may treat OSHA-derived data as restricted. Mitigations: the $0 day-0 pre-check, "risk monitoring" positioning, and no "records lookup" keywords. A disapproval in the account shared with B1 could spill over, so **run B2 in its own Google Ads account**.
- **Low volume:** P50 adds only about 1.4 customers a month, so $300/mo net arrives around month 9–10, not in 90 days. Sustaining payback depends on churn staying at or below 4%.
- **Legal:**
  - Defamation or false light through mis-matched entities. Mitigations: show match confidence; require user confirmation before a sub appears on the PDF; quote verbatim and link the source.
  - FCRA-adjacent wording for sole-proprietor subs. Mitigations: business purpose only; never use "background check".

---

## B3 — Recipe-Card Heirloom Cookbook: Q4 gift certificate now, printed hardcover in January (new)

- **Persona:** The Media Buyer
- **One-liner:**
  - **What the buyer gets:** a $119 gift that turns Grandma's handwritten recipe cards into a printed, full-colour hardcover heirloom cookbook. Each page shows the original card's scan facing a cleanly typeset recipe.
  - **How it is made:** the family just photographs the cards; AI vision transcribes them; the customer approves a PDF proof; Lulu's Print API prints and ships direct, so nobody touches a book.
  - **How it sells:** Meta (gift-intent creative from real sample books) plus Google Search, as a **gift certificate for Christmas, with the book made in January**. This removes the December print-cutoff problem.
- **Channel & benchmarks (CPC/CPM, CTR, CVR, with sources):**
  - **Meta:**
    - median CPM ~$14 in 2026 (+20% YoY), **+25–50% in Q4, and 2–3× in BFCM week**;
    - gifts and collectibles have the highest CTR, ~4%;
    - e-commerce CVR averages 2.7%, top quartile 4.1%;
    - median DTC purchase ROAS is 2.96.
    - **P50 plan:** CPM $19, link CTR 1.8% → CPC ~$1.05; CVR 2.5%.
  - **Google Search** on "turn recipe cards into a cookbook", "handwritten recipe book", "family recipe book gift": e-commerce/gift CPC is roughly **$1.20–2.00**, with CVR 3–4% on high-intent phrases.
  - **The category is proven buyable with paid traffic:** Storyworth sells a $109 family-memoir book gift (extra colour copies $79), and its model depends on paid social.
- **CAC / LTV / payback:**
  - **Unit cost:** Lulu premium colour hardcover, ~100 pages, ≈ $30–32.50 to print; fulfilment $1.75; US shipping ~$8. **≈ $40 per book.**
  - **Contribution per order (first purchase):**

    | Line | Amount |
    |---|---|
    | Price | $119 |
    | Book cost | −$40 |
    | Stripe | −$3.75 |
    | Vision and layout tokens | −$3 |
    | Reprint/refund reserve (4%) | −$4.75 |
    | Attach rate: 20% buy an extra copy at $59 at checkout ($17 margin each) | +$3.40 |
    | **Contribution** | **≈ $71** |

    About 15% of gift certificates historically go unredeemed. That saves print cost but stays a liability, so it is **excluded** here.
  - **Gate:** first-purchase LTV:CAC ≥ 1.5 means **CAC ≤ $47**.
  - **CAC by case:**

    | Case | CAC | First-purchase ratio |
    |---|---|---|
    | P10 | $90 (CVR 1.2% in BFCM-inflated CPMs) | 0.8 |
    | P50 | **$42** (Meta $1.05 / 2.5%; Google $1.60 / 3.5% → $46) | **1.7** |
    | P90 | $25 | 2.8 |

  - **Follow-on LTV, not counted in the gate:**
    - relatives order copies through the family share link after the proof: P50 0.6 copies × $17;
    - Mother's Day repeat gifting to the list;
    - "Volume 2" books.
- **Capped ad test & kill rule:**
  - **Budget:** $500 from about Oct 22 to Nov 8 ($300 Meta Advantage+ with 6 creatives from real sample-book photos; $200 Google Search). This runs **before** BFCM CPM inflation.
  - **Pass:** CAC ≤ **$47** on at least 10 orders.
  - **Kill:**
    - 0 orders after $250; **or**
    - CAC above $70 at $500; **or**
    - proof-approval or print defects above 10% in the first 10 books.
  - **Scale, only on pass:**
    - a $1,500 tranche from Nov 9 to Dec 20, with daily budget rules:
      - pause any ad set above $55 CAC over 3 days;
      - raise winners by 20% a day while under $40;
      - hold spend during BFCM week unless CAC stays at or below $47.
    - Gift-certificate sales run to Dec 23, because the certificate is delivered instantly as a PDF.
- **Demand test:**
  - **Offer:** the real gift certificate at $119, with a printed sample shown, and stated timelines:
    - "Upload by Nov 20 → book under the tree";
    - otherwise a beautiful printable certificate now, book in ~3 weeks after upload.
  - **Channel and audience:** the $500 Meta and Google test above, aimed at gift-buying adult children of grandparents (35–60).
  - **Pass/fail:** at least 10 orders at CAC ≤ $47; fail and refund-on-request if fewer than 5.
  - **Pre-check:** order 3 Lulu sample books on day 4 to verify print quality before any ad money is spent.
- **Customer:**
  - Adults aged 30–60, mostly women, buying a Christmas or Mother's Day gift for a parent or grandparent, or making a keepsake after a death in the family.
  - Where they are: Facebook and Instagram, and Google gift searches.
  - What they already pay for: Storyworth ($109), Shutterfly/Mixbook photo books ($40–90), Etsy handwritten-recipe tea towels and cutting boards ($25–60).
- **Problem / desire:** "Mom's recipe box is falling apart and nobody can read Grandma's handwriting. I'd love a real book for everyone, but typing 80 recipes into Mixbook is never going to happen."
- **Offering:**
  1. Gift certificate (PDF, instant).
  2. Upload by phone: the family photographs the cards. Multiple relatives can contribute through a share link.
  3. AI vision transcribes each card into a standard recipe layout (title, ingredients, method), with low-confidence words flagged for the family to confirm.
  4. Optional dedication page and family photos.
  5. PDF proof, then the customer's approval.
  6. Lulu prints a 100-page full-colour hardcover and ships it to the address given.
  7. Extra copies at $59 each, ordered by anyone with the family link.
- **Price & revenue model:**
  - One-time $119 (book plus US shipping); extra copies $59.
  - Later: a $149 "large" edition (up to 200 pages).
  - Paid through Stripe Checkout with Stripe Tax: it is a physical good, so the merchant-of-record digital platforms don't apply.
- **Physical items required?** **Yes**, but nobody handles them.
  - Lulu's Print API prints and drop-ships each book.
  - Lulu's misprint and damage policy covers reprints; the operator submits the photo claims.
  - There is no inventory, no packing, and no returns to a human address.

### Upfront capital
| Item | Cost |
|---|---|
| 3 Lulu sample books (QA and ad photography) | $135 |
| Lifestyle photo shoot of the samples (Upwork/Fiverr photographer with props) | $150 |
| Domain | $12 |
| Home-state sales-tax permit (varies by state) | $0–50 |
| Capped ad test (Meta $300 + Google $200) | $500 |
| Q4 scale tranche, released only on pass | $1,500 |
| **Total** | **≈ $2,350** (over $1k; see the payback and P10 checks below) |

### Monthly running costs (excluding operator tokens)
- Per order:
  - Lulu print, fulfilment and shipping: ~$40 per book;
  - Stripe 2.9% + $0.30, plus Stripe Tax 0.5%;
  - vision and layout tokens: ~$3 per book.
- Fixed:
  - hosting: $0–10;
  - transactional email: $0–20;
  - operator tokens: ~$100/mo during Oct–Jan, ~$50/mo off-season.

**P50 Q4 season (test + scale = $2,000 of ads at $42 CAC):**

| Line | Amount |
|---|---|
| 48 paid orders × $71 | $3,408 |
| About 10 organic and referral orders | +$710 |
| Relatives' copies | +$600 |
| Ads | −$2,000 |
| Tokens (Oct–Jan) | −$400 |
| Fixed costs | −$60 |
| **Season net** | **≈ $2,250** |

**Rest of the year (P50):**
- Mother's Day season (a $1,000 ad budget in April–May) nets about $900.
- Off-peak copies and organic sales bring about $60/mo.
- **Year-1 P50 net ≈ $3,700 → about $310/mo averaged.**

**Payback and return:**
- **Payback of capital:** ad spend is recouped within the season. The full $2,350 is recovered by **about mid-January 2027 (month 3–4)** at P50, and **about month 6** including the sponsor's setup time ($1,200).
- **P10:** the test fails on Nov 8 and $797 is lost (**34% of the $2,350 committed**, within the PARAMS ~50% limit) plus $1,200 of sponsor time.
- **P90:** CAC of $25 lets the season scale to about $5,000 of ads, for a year-1 net of about $9,000.
- **Annualised return (P50):** ($3,700 − $1,200 sponsor time) / $2,350 ≈ **105%**, vs 4% T-bills.

### Customer acquisition plan
1. Sample books are photographed by about day 16. These photos are the creative; there are no AI-generated product images, to stay truthful under FTC rules and avoid Meta's "AI info" labels.
2. Meta Advantage+ shopping campaign, with 6–10 creatives: the before/after card-to-page reveal, "Grandma's handwriting, saved forever", and the gift certificate shown being opened.
3. Google Search on high-intent recipe-book phrases. Negatives: "template", "free", "printable", "binder", "blank".
4. Checkout: gift certificate or "start now", with the extra-copies upsell.
5. Post-purchase loop: the family share link drives relatives' copy orders. A review request goes out on delivery, and a Mother's Day email goes to the whole list in April.
6. In January: a "book-in-progress" nudge sequence so certificates are redeemed and printed (cash flow) rather than left as a liability.

### Initial traffic approaches (ranked by expected speed)
1. **Meta paid social:** live within 24–48 h of ad review. Gift-intent targeting needs no audience.
2. **Google Search:** live the same day. Smaller volume but higher intent.
3. **Pinterest Ads**, manual campaign only, no auto-pinning. Recipe and heirloom gifting is a strong Pinterest category. Week 2.
4. **The family share link (organic):** every book order exposes 3–10 relatives to the product. It compounds after the first deliveries in December and January.

### Path to first sale
| Day | Step |
|---|---|
| D0–2 | Sponsor: Stripe KYC, Meta Business verification, Google Ads verification, Lulu account with payment card, sales-tax permit (about 4 h). |
| D1–4 | Operator builds the upload, transcription and layout pipeline using public-domain handwritten recipe card scans; orders 3 samples on D4. |
| ~D14 | Samples arrive; photographer shoot. |
| D16 | Ads live. |
| ~D17–22 (P50) | First order. |
| ~D20–25 | First cash (Stripe pays out in 2 business days). |

**Ideator estimate:** first sale about day 18.

### Who does what
- **AI operator:** pipeline build; transcription and layout; proof generation; low-confidence-word confirmation loop with the customer; Lulu Print API order submission and tracking; misprint claims; ad creative variants and daily budget rules through the Meta and Google APIs; support inbox; review requests; sales-tax report preparation.
- **Human sponsor:**
  - **One-time, about 4 h ($1,200):** KYC for Stripe, Meta and Google; Lulu account; sales-tax permit; approving the photographer.
  - **Recurring, about 0.25 h/mo:** signing and filing the home-state sales-tax return, which the operator prepares, and approving chargeback responses.
  - **Gate:** $310/mo average net allows 1 h.
- **Contractors:** a one-time photographer, and Lulu as the printing and shipping supplier.

### Moat — why not just ask ChatGPT?
- **The substitutes:**
  - ChatGPT can transcribe a card but can't print and ship a hardcover;
  - Mixbook and Shutterfly print but make you type every recipe;
  - AI recipe-scanner apps (Old Family Recipe, WeeChef, Heirloom Kitchen, ReciScan) exist, and some print, but they are apps waiting for organic discovery.
- **Per lesson 19, the copyable part is already copied.** **The edge here is capital applied to a proven gift channel in the right season**, plus things that compound:
  - reviews and UGC photos of real books;
  - the family share link and its copy orders;
  - a list of gift buyers who return for Mother's Day;
  - per-customer "Volume 2" demand.
- **Honest view:** if CAC can't be held at or below $47, the clones' existence doesn't matter. The kill rule ends it in November.

### Biggest risks (ideator's own view)
- **Q4 auction inflation:** BFCM CPMs are 2–3× normal, so the ROAS needed at a 1.5× ratio may not hold from mid-November. Mitigation: test before BFCM, hold spend in BFCM week, and use the gift-certificate model to keep selling through Dec 23.
- **Transcription errors in heirloom content:**
  - **The risk:** one wrong quantity in "Grandma's pound cake" means a 1-star review and a reprint.
  - **Mitigations:**
    - low-confidence words are flagged for the family to confirm;
    - mandatory proof approval, with a clear "you approved this proof" reprint policy;
    - Lulu's quality-claim process for physical defects;
    - a 4% reprint reserve.
- **Legal and ops:**
  - **Gift certificates:** the CARD Act requires at least 5 years before expiry. Unredeemed balances may trigger state unclaimed-property rules, so they are treated as a liability.
  - **FTC Mail/Internet Order Rule:** delivery times must be stated and met, or the customer notified.
  - **Sales-tax nexus:** home state only below the economic thresholds.
  - **Uploaded copyrighted cookbook pages:** handled by terms of service and private printing only.
  - Sponsor KYC across three ad and payment platforms is a concentration point.

---

## Comparison (P50)
| | B1 HSK Speaking Mock | B2 SubWatch | B3 Heirloom Cookbook |
|---|---|---|---|
| Capital (test + scale) | $562 + $400 = **$962** | $512 + $400 = **$912** | $850 + $1,500 = **$2,350** |
| Paid channel | Google Search + Reddit + affiliates | Google Search (+ Bing, LinkedIn retargeting) | Meta + Google (+ Pinterest) |
| CAC / gate | $18 / ratio 1.54 (one-off ≥ 1.5) | $437 / ratio 3.7 (subscription ≥ 3) | $42 / ratio 1.7 (one-off ≥ 1.5) |
| P50 monthly net | ~$250 avg (~$320 in peak months) | ~$0 at month 6 → ~$540 at month 12 | ~$310 avg (seasonal: Q4 + Mother's Day) |
| Payback of capital | ~month 4 (7 incl. sponsor time) | ~month 10–11 | ~month 3–4 (6 incl. sponsor time) |
| Year-1 return on capital | ~155% | ~20% (year 2 ~700%) | ~105% |
| Sponsor h: setup / ongoing | 2.5 / ~0 | 2 / 0.25 per mo | 4 / 0.25 per mo |
| First sale (ideator) | ~D16 | ~D40 | ~D18 |

**Media buyer's ranking:**
1. **B3** has the best-proven channel economics (Storyworth's paid model) and lands in the right season, but the CAC margin is thin. **The test decides it.**
2. **B2** has the best long-run LTV:CAC, but it is slow and carries ad-policy risk.
3. **B1** has the best founder fit and the cheapest test, but the smallest ceiling.

All three can be tested for under $1,400 combined before any scale tranche is released.

## Sources
- WordStream, Google Ads benchmarks 2026: https://www.wordstream.com/blog/2026-google-ads-benchmarks
- Usermaven, Google Ads benchmarks (education CPC $2.40, CVR 3.39%): https://usermaven.com/blog/google-ads-benchmarks
- Webtonic, construction Google Ads statistics 2026: https://www.webtonic.io/blog/construction-materials-google-ads-statistics
- Stackmatix, Reddit Ads cost 2026: https://stackmatix.com/blog/reddit-ads-cost-guide-2026
- ContentStudio, Meta ads benchmarks 2026: https://contentstudio.io/blog/meta-ads-benchmarks
- Lebesgue, Meta benchmarks by industry and AOV 2026: https://lebesgue.io/facebook-ads/meta-ads-benchmarks-by-industry-and-aov
- ClickMinded, LinkedIn Ads benchmarks 2026: https://www.clickminded.com/linkedin-ads-benchmarks/ ; GrowthSpree: https://www.growthspreeofficial.com/blogs/linkedin-ads-benchmarks-2026
- Google Ads, Government documents and services policy: https://support.google.com/adspolicy/answer/13156083 ; Oct 5 2026 update: https://www.techwyse.com/news/platform-updates/google-ads-government-documents-services-policy-update-october-2026
- HSK 3.0 dates and format: https://hsklord.com/blog/hsk-3-0-test-dates-2026 ; https://studycli.org/learn-chinese/the-new-hsk ; https://edu.sh.gov.cn/study_en_hsk/20260107/5292266eca744a959c1db43237fbc185.html
- HSK speaking competitors: https://apps.apple.com/app/id6744699753 (HSKK Test Prep); https://alternativeto.net/software/hsk-university/about/ ; https://mandarintemple.com/pricing (via the round-1 U3 sales-skeptic review)
- Lulu print costs: https://podvector.ai/articles/print-on-demand/costs-and-suppliers/lulu-print-on-demand-pricing ; Lulu API fees: https://help.api.lulu.com/en/support/solutions/articles/64000254631-are-there-fees-to-use-lulu-s-print-api-
- Storyworth pricing: https://welcome.storyworth.com/storyworth-pricing
- Recipe-scanner clones: https://peerpush.com/p/old-family-recipe ; https://apps.apple.com/mx/app/heirloom-kitchen/id6757515427 ; https://appshunter.io/ios/app/reciscan-cookbook-maker/id6478405196
- Subcontractor prequalification context: https://www.meltplan.com/blogs/best-subcontractor-prequalification-software-for-general-contractors-2026
