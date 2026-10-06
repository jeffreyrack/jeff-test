# Unit Economics Analyst review: user ideas U1, U2 (2026-10-06)

| ID | Idea | Score | Upfront $ | Monthly fixed $ | Net $/sale | Sales/mo for $300 | Est. operator tokens $/mo | Months to break-even |
|---|---|---|---|---|---|---|---|---|
| U1a | OSRS flipping for personal use | n/a (pays $0 in USD) | $0 | $0 | n/a. gp cannot legally become USD. P50 is about $0.33/h *membership-equivalent* | Impossible: gp never pays for tokens | ~$100–150 if the engine is built | Never, in USD terms |
| U1b | OSRS flip advisor, paid product | **3** | $0–12 (+$5 if a Chrome extension) | $0 (up to $5 for Workers Paid at scale) | **$3.25** on a $4/mo sub | **93 active subs** (46 just to cover $150 tokens) | $250 in month 1, then ~$150 | **Not within 12 months.** At about 6 new subs/mo and 15% churn, it plateaus near 40 subs, below the 46 needed |
| U2 | Personalised Mandarin graded reader | **5** | $12 (+$5 for an optional Chrome extension). It must stay a PWA, because Apple ($99) + Google ($25) + domain = $136, over the cap | $0 at first, then ~$20 (email) once the free list passes ~100/day | **$5.31** on a $7/mo sub, after LLM + TTS of ~$0.75/user/mo | **57 active subs** (42 at $9/mo) | $300 in month 1, then ~$200 | **Monthly break-even around month 8. Cumulative break-even not within 12 months (around month 21)** |

Common assumptions:
- **Merchant of record:** Lemon Squeezy at 5% + $0.50, plus 0.5% on subscriptions and 1.5% on international sales (assume half the buyers are international). That is about 6.25% + $0.50 per charge.
- **Patreon:** 10% for creators who started after Aug 2025, plus about 2.9% + $0.30 processing. That nets about the same as Lemon Squeezy at a $4 price point.
- **Projections:** every projection counts operator tokens as a cost.

---

## U1: OSRS Grand Exchange flip advisor

### (a) Personal flipping: gp/hour converted to membership value

The only legal value gp can have is through the Old School Bond:
- A bond costs **$9.99** in real money and about **12.06M gp** on the GE.
- So **1M gp ≈ $0.83 of membership value**.
- Membership costs $14.99/mo, or $10.99/mo on an annual plan. Keeping membership with bonds needs about 26.2M gp per 30 days.

| Scenario | gp/h (8 slots, after tax) | 12 h/mo | 30 h/mo | $-equiv at 30 h |
|---|---|---|---|---|
| P10: liquid items, like the backtest | −0.1M | −1.2M | −3.0M | −$2.49 |
| P50: 10–50M bankroll, mid-liquidity items | 0.4M | 4.8M | 12.0M (1 bond) | $9.94 |
| P90: 100M+ bankroll, 5-minute timing, active slot management | 1.5M | 18M | 45M (3.7 bonds) | $37 |

Why these numbers:
- The P50 figure sits inside third-party guide claims of "500K–1M/h for 10M+ bankrolls", discounted for the 2% tax.
- The backtest lost money on every bankroll tested. The 6.4M gp/h "capacity" figure cannot be reached with 8 slots.

What this means:
- P50 covers about **38% of membership**.
- The most this can ever be worth is the membership the player would otherwise buy, which is $11–15/mo. Anything above that is in-game value only.
- Real-world trading breaks the Jagex ToS, so **gp contributes $0 to tokens**.
- It also takes human time: 30 h/mo is about 7 h/week, well over the 3 h/week sponsor cap. This is a hobby, not business time.
- A 2–4 week test cannot tell P10 from P50 with any statistical confidence.

### (b) Paid product

| Item | $ |
|---|---|
| Upfront | Domain $12 (optional). Data comes from the OSRS Wiki API, which is free. |
| Monthly fixed | $0. The Cloudflare free tier handles 5-minute polling (288 writes/day). |
| Price ceiling | GE Tracker Premium is **£2/mo (~$2.65)** and Flipping Utilities is free, so $4 is the realistic price. |
| Net/sale at $4 | 4 − 0.25 − 0.50 = **$3.25** (a $5 price gives $4.19) |
| Operator tokens | Build $250 in month 1. Then ~$150/mo for backtests, programmatic "best flips" pages and support. |

Realistic ramp assumptions:
- Months 1–3: build, personal test and a free launch.
- First paid subscribers in month 4. After that, 3, 5, then 6 new subscribers per month, with 15% monthly churn. Flipping tools churn when the tips stop paying.

| Month | Subs | Net rev | Costs | Cum cash |
|---|---|---|---|---|
| 1 | 0 | $0 | $262 | −$262 |
| 2 | 0 | $0 | $150 | −$412 |
| 3 | 0 | $0 | $150 | −$562 |
| 4 | 3.0 | $10 | $150 | −$702 |
| 5 | 7.5 | $25 | $150 | −$828 |
| 6 | 12.4 | $40 | $150 | −$937 |

Outcome:
- At month 12 it has about 30 subs and cumulative cash of −$1,373. It levels off near 40 subs, so it never covers $150 of tokens.
- Reaching $300 needs 93 paying subs in a niche where the paid incumbent charges £2 and the backtest does not yet show an edge.
- **Score 3.** The upfront cost is $0 and the margin percentage is high. The absolute net per sale is tiny, and the required volume is about 3× the rubric's "<30 sales" mark.

---

## U2: Personalised Mandarin graded reader

### Upfront and fixed costs

| Item | $ |
|---|---|
| Domain | $12 |
| CC-CEDICT dictionary, AnkiWeb deck listing | $0 |
| Chrome Web Store, only if the extension is built | $5 |
| Native apps | **Avoid.** $99 + $25 + $12 = $136 breaks the $100 cap. |
| Email | Resend free tier (100/day) for months 1–2. **~$20/mo** from month 3 for a daily free email. Web push is $0. |

### Per paid user per month (one daily story of ~600 characters)

| Item | Low | Mid | High |
|---|---|---|---|
| LLM: ~8k input tokens (the known-word list in context), ~2k output, ×1.5 for a QA pass and retries | $0.11 (Flash/mini-class model) | $0.45 | $0.81 (Haiku-class model) |
| TTS: 18k characters/mo | $0 (free tier covers ~55 users) | $0.29 (Neural2, $16/M) | $0.54 (Chirp 3 HD, $30/M) |
| **Total** | ~$0.11 | **~$0.75** | ~$1.35 |

Notes on these costs:
- The ideator's $0.002–0.01/day is optimistic once a 2–3k-word known list sits in the prompt. Prompt caching, or picking from a shared pool of stories per level and filtering by vocabulary, gets close to the low column.
- Free users share one story per HSK level, which costs about $0.20/mo in total.
- On-demand "generate another story" must be capped. Otherwise heavy users push the cost toward the high column.

### Net margin per sale

| Plan | Calculation | Net |
|---|---|---|
| $7/mo | 7 − 0.44 − 0.50 − 0.75 | **$5.31** (76% margin) |
| $49/yr | (49 − 3.56) / 12 − 0.75 | **$3.04/mo** |

Du Chinese charges $12.99/mo, so **$9 is defensible**. At $9 the net is $7.19, which means 42 subs for $300.

### Six-month projection

Assumptions:
- **Churn:** 18% per month, typical for consumer language-learning subscriptions. Holding 57 subs means winning ~10 new payers every month forever.
- **New paid subs per month:** 0, 2, 5, 8, 10, then 12. This comes from a free list growing through Reddit (posted by the human) and AnkiWeb, converting at 2–4%.

| Month | Subs | Net rev | Costs (tokens + email + domain) | Cum cash |
|---|---|---|---|---|
| 1 | 0 | $0 | $312 | −$312 |
| 2 | 2.0 | $11 | $250 | −$551 |
| 3 | 6.6 | $35 | $220 | −$736 |
| 4 | 13.4 | $71 | $220 | −$885 |
| 5 | 21.0 | $112 | $220 | −$993 |
| 6 | 29.2 | $155 | $220 | −$1,058 |

Outcome:
- Monthly break-even comes around **month 8** (~41 subs).
- At steady state (~67 subs) the net is about $354/mo, roughly $134 after costs. That just clears the $300 target, and only in gross terms.
- Cumulative cash turns positive around **month 21**.
- **Score 5.** The margin is good and variable costs are small and controllable. The required volume, combined with 18% churn, is the problem.

---

## Sources
- [OSRS Wiki: Membership & Bonds price change (Mar/Apr 2026; bond $9.99, 1 month $14.99, 12 months $10.99/mo)](https://oldschool.runescape.wiki/w/Update:Membership_&_Bonds_Price_Change)
- [OSRS Wiki: Old school bond (GE price ~12.1M; bond packs)](https://oldschool.runescape.wiki/w/Old_school_bond)
- [GE Tracker pricing (£2/month)](https://www.ge-tracker.com/pricing)
- [OSRS merchanting guide 2026 (claimed gp/h ranges)](https://osrstoolkit.com/osrs-merchanting-flipping-guide-2026/)
- [Lemon Squeezy fee breakdown 2026](https://dodopayments.com/blogs/lemonsqueezy-review)
- [Patreon 10% fee for new creators after Aug 4, 2025](https://support.patreon.com/hc/en-us/articles/36426991446797)
- [Google Cloud Text-to-Speech pricing](https://cloud.google.com/text-to-speech/pricing)
- [Du Chinese pricing](https://duchinese.net/l/discount)
- Evidence scripts: `/home/user/jeff-test/runs/2026-10-06-eval-user-ideas/evidence/{snap,sim,cap}.py`
