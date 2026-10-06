# Unit Economics Analyst review: U3, AI Mandarin tutor (2026-10-06)

| ID | Idea | Score | Upfront $ | Monthly fixed $ | Net $/sale | Sales/mo for $300 | Est. operator tokens $/mo | Months to break-even |
|---|---|---|---|---|---|---|---|---|
| U3 | AI Mandarin tutor (lessons + text/voice practice) | **5** if built on an STT→LLM→TTS pipeline with hard voice caps at $15/mo. **2** if built on uncapped realtime speech-to-speech | ~$62 (domain $12, API dev credits $20, one-time native-speaker calibration ~$30). PWA only: Apple $99 + Google $25 would break the cap | $0, then ~$5 (Workers Paid for metering) | **$8.29** on a $15/mo sub, after ~$4.27 blended inference and ~$1 free-tier allocation. At $12/mo it is $5.48 | **36 active subs** at $15 (55 at $12). Covering its own $255/mo costs takes 31 | $400 in month 1, $300 in month 2, then ~$250 | **Monthly break-even around month 7, cumulative around month 16. Not within 12 months.** At $12 it is month 10 and month 30+. With realtime flagship voice it never breaks even |

Common assumptions (same as the U1/U2 review):
- **Lemon Squeezy:** about 6.25% + $0.50 per charge.
- **Usage:** 20 active days a month. Light is 5 min/day (100 min/mo), typical is 15 (300), heavy is 30 (600).
- **Blended paying-user mix:** 50% light, 35% typical, 15% heavy.
- **Churn:** 20% a month.
- **Projections:** count operator tokens as a cost.

---

## 1. Per-minute inference cost (current list prices, Oct 2026)

**How one minute of voice practice was modelled:**
- The learner speaks 35% of the time, the tutor 45%, and 20% is silence.
- The tutor takes 4 turns a minute.
- Each turn carries a 3k-token system prompt (lesson plan plus learner memory).
- The conversation context is re-read on every turn.
- The model was run in a session-scratchpad script that is not saved in the repo. Its results agree with published real-world ranges.

| Architecture | Prices used | $/active min | Light/mo | Typical/mo | Heavy/mo |
|---|---|---|---|---|---|
| **(a) Text only:** gpt-5-mini | $0.25 in / $0.025 cached / $2 out per 1M | $0.002–0.003 | $0.16 | $0.61 | $1.58 |
| (a) Text only: Claude Haiku 4.5 | $1 in / $0.10 cached / $5 out | $0.005–0.009 | $0.50 | $1.98 | $5.43 |
| **(b) Pipeline, low:** gpt-4o-mini-transcribe ($0.003/min) + gpt-5-mini + Azure neural TTS (~$0.005 per audio min) | | $0.006–0.008 | $0.58 | $2.02 | $4.93 |
| **(b) Pipeline, mid:** as low, but gpt-4o-mini-tts (~$0.015 per audio min) + Azure pronunciation assessment for tones (~$1/h, est.) | | $0.016–0.019 | $1.61 | $5.13 | $11.13 |
| (b) Pipeline, high: Haiku 4.5, gpt-4o-transcribe, 50% cache hits | | $0.028–0.047 | $2.79 | $10.68 | $28.29 |
| **(c) OpenAI gpt-realtime-2.1-mini**, 85% cache hits, context summarised every 5 min | $10 audio in / $0.30 cached / $20 out | $0.027 | $2.72 | $8.15 | $16.30 |
| (c) Same, *without* resetting context | | $0.027–0.093 | $2.72 | $16.05 | **$55.79** |
| (c) **gpt-realtime-2.1 (flagship)**, cached, with reset | $32 / $0.40 / $64 | $0.084 | $8.38 | $25.13 | **$50.25** |
| (c) Flagship, naive build (50% cache hits, no reset) | | $0.16–0.77 | $16 | $122 | **$462** |
| (c) Gemini Live (3.8 Live / 2.5 Flash native audio), session recycled every 3 min | $3 audio in / $12 out per 1M at 25 tok/s; **no caching**; the full context is re-billed every turn | $0.036–0.039 | $3.61 | $11.69 | $23.37 |
| (c) Gemini Live, naive | | $0.05–0.23 | $5.34 | $37.61 | **$140** |

Key findings:
- **Realtime cost is superlinear in session length.** Both OpenAI and Google re-bill the accumulated conversation context on every turn.
  - Google staff confirmed in July 2026 that the Live API has no context caching and re-bills accumulated audio at the input rate on every turn.
  - A long unbroken session at the 30 min/day heavy tier costs 3–10× the headline per-minute price.
  - Mandatory mitigation: summarise the context to text and restart the session every 3–5 minutes.
- **Gemini's headline price is misleading.** Its "$0.005/min in, $0.018/min out" looks cheapest. Once context re-billing is included, it costs more than OpenAI realtime-mini.
- **The flagship realtime model loses money at any consumer price up to $25.**

## 2. The user's framing: AI vs a human tutor

| | $/hour | $/min | Typical month (300 min) |
|---|---|---|---|
| italki community tutor | $8–15 | $0.13–0.25 | $40–75 |
| italki professional / Preply (US avg $19.84) | $15–40 | $0.25–0.67 | $75–200 |
| AI pipeline (mid) | ~$1.03 | $0.017 | $5.13 |
| AI realtime-mini | ~$1.63 | $0.027 | $8.15 |
| AI realtime flagship | ~$5.03 | $0.084 | $25.13 |

**The cost side of the thesis holds.** AI costs 5–40× less than a human tutor per minute.

**The pricing side does not.** Buyers do not anchor the price to a tutor's hourly rate. They anchor it to apps:

| Competitor | Price |
|---|---|
| HelloChinese Premium | $11.99/mo |
| SuperChinese PLUS | $11.99/mo |
| SuperChinese CHAO AI | $24.99/mo |
| Pingo AI | $14.99/mo |
| Speak Chinese AI+ | $14.99/mo, $59.99/yr |
| ChatGPT Go | $8/mo |
| Gemini Live | free |
| RevenueCat education median | $9.99/mo |

So the realistic price is $12–15, not "half a tutor". At that price, inference takes 10–40% of revenue for a typical user, and more than 100% for an uncapped heavy realtime user.

## 3. Safe price and usage caps

The cap rule is that inference must stay at or below 50% of the net price, even for the heaviest allowed user.

| Mode | Minutes/mo allowed at $12 | at $15 | at $25 |
|---|---|---|---|
| Text | 2,067 (effectively unlimited) | 2,608 | 4,411 |
| Pipeline, mid | 289 | 365 | 617 |
| Realtime-mini (with reset) | 198 | 249 | 422 |
| Gemini Live (recycled) | 138 | 174 | 294 |
| Realtime flagship | 64 | 81 | 137 |

**Recommended plan structure:**

| Plan | What it includes |
|---|---|
| Free | Text only, 10 messages a day, plus a 7-day trial of 5 voice min/day. This costs about $1 per paying sub. Uncapped free voice would cost $4–9 per paying sub. |
| **$15/mo** ($99/yr) | Unlimited text, **300 voice min/mo** on the pipeline, of which up to 60 min is "live" realtime-mini mode |
| $25/mo | 600 voice min + 150 live min, priced against SuperChinese CHAO AI |
| Top-up | $5 per 100 extra pipeline minutes (about $1.90 cost) |

**Caps must be enforced in the app** when it issues the ephemeral session token, with a maximum session length. Provider budgets alert you; they do not hard-stop spending.

**Annual plan risk:** at $99/yr ($8.25/mo), a capped heavy user still costs about $11/mo on the mid pipeline. So annual plans also need the caps.

## 4. Net per sale and subs needed

| Plan | Calculation | Net per sub |
|---|---|---|
| $15 | 15 − 0.94 (fees) − 0.50 − 4.27 (blended inference, mid pipeline) − 1.00 (free tier) | **$8.29** |
| $12 | same calculation at $12 | $5.48 |
| $12, low pipeline (no tone scoring) | same calculation at $12 | $8.01 |

Subs needed:
- **$300 net: 36 subs at $15** (55 at $12).
- Covering the business's own $255/mo: 31 subs.
- $300 *after* own costs: 67 subs. That is above the 59-sub steady state, so it is not reached.

**Survivorship skew:** retained subscribers use the product more. If the mix shifts to 30/40/30, blended inference rises to $5.87 and the subs needed for $300 rise to 45.

## 5. Six-month projection ($15, mid pipeline, 20% churn)

New paid subs per month: 0, 1, 4, 7, 10, then 12 from month 6 on. Steady state is about 59 subs.

| Month | Subs | Net rev | Costs (tokens + fixed) | Cum cash (after $62 upfront) |
|---|---|---|---|---|
| 1 | 0 | $0 | $400 | −$462 |
| 2 | 1.0 | $8 | $300 | −$754 |
| 3 | 4.8 | $40 | $255 | −$969 |
| 4 | 10.8 | $90 | $255 | −$1,134 |
| 5 | 18.7 | $155 | $255 | −$1,234 |
| 6 | 26.9 | $223 | $255 | −$1,266 |

Outcome:
- Monthly break-even comes in **month 7** (about 34 subs).
- Cumulative cash turns positive in **month 16**.
- At steady state, profit after costs is about $238/mo.
- At $12 with tone scoring, monthly break-even moves to month 10 and the cumulative deficit is still −$824 at month 24.

**Score 5.** The upfront cost is low, the margin is about 60% when capped, and 36 subs is close to the rubric's 30. It scores below a static product because inference is a usage-driven variable cost with tail risk, and 20% churn caps the subscriber base near 60. Using uncapped or flagship realtime voice drops it to 2.

## Sources
- [OpenAI API pricing (gpt-realtime-2.1 / -mini, transcribe, mini-tts, gpt-5-mini)](https://developers.openai.com/api/docs/pricing)
- [OpenAI Realtime pricing explainer, Jul 2026 ($0.04–0.10/min flagship, $0.02–0.05 mini)](https://aireiter.com/blog/openai-realtime-api-pricing)
- [Gemini API pricing (Live audio $3/$12 per 1M, 25 tok/s; Flash price doubles 1 Jan 2027)](https://ai.google.dev/gemini-api/docs/pricing)
- [Google forum: Live API re-bills accumulated audio every turn](https://discuss.ai.google.dev/t/pricing-of-speech-to-speech-live-model/140340)
- [Google forum: Live API has no context caching (Jul 2026); a tutoring app at ~16.4k tokens/min/session](https://discuss.ai.google.dev/t/gemini-live-api-caching/174701)
- [Azure Speech pricing (USD figures not rendered; $1/h STT and pronunciation assessment, ~$15–16/M neural TTS are estimates)](https://azure.microsoft.com/en-us/pricing/details/speech/)
- [Claude Haiku 4.5 pricing](https://pricepertoken.com/pricing-page/model/anthropic-claude-haiku-4.5)
- [italki Chinese tutor rates 2026](https://hsklord.com/blog/italki-chinese-review)
- [Preply Chinese tutor rates](https://preply.com/en/New-York-City-NY/tutors-intensive-chinese)
- [LanguaTalk: average Chinese tutor rate $23/h (2022)](https://languatalk.com/blog/how-much-do-chinese-tutors-charge/)
- [AI Chinese app prices 2026 (SuperChinese, HelloChinese, Pingo)](https://prepedu.com/en/blog/chinese-learning-apps)
- [Speak Chinese: Learn Mandarin (App Store)](https://apps.apple.com/us/app/-/id1507511040)
- [ChatGPT Go pricing](https://www.cometapi.com/how-much-is-chatgpt-go/)
- [RevenueCat State of Subscription Apps 2026, Education](https://www.revenuecat.com/state-of-subscription-apps-2026-education)
