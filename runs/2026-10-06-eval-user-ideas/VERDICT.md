# Verdict: user-supplied ideas (2026-10-06)

Composite score = 0.30·Sale + 0.20·Market + 0.20·Autonomy + 0.15·UnitEcon + 0.15·Legal, as defined in `.claude/skills/business-ideation/reference/scoring-rubric.md`.

| ID | Idea | Sale | Mkt | Auto | UnitEc | Legal | Composite | Gate | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| U1 | OSRS GE flip advisor (paid product) | 2 | 3 | 5 | 3 | 6 | **3.55** | **REJECT**: sales-skeptic P50 > 180 days | **No-go** as a business; fine as a hobby |
| U2 | Mandarin personalised graded reader (as briefed) | 4 | 4 | 6 | 5 | 7 | **5.00** | Pass | **Pivot** |
| U2-W | U2 re-aimed at the HSK 3.0 transition | 4* | 6 | 6* | 5* | 7* | **~5.40** (indicative) | Pass | **Pivot → test cheaply** |

\*Only the market analyst re-scored the HSK 3.0 wedge (6). The other scores are carried over from U2, so 5.40 is indicative only. The sales skeptic also named HSK 3.0 as the best-fit wedge, but did not score it.

For comparison, the top picks from the 15-idea run scored 6.20 (D2) and 5.95 (T2). U2-W would rank around 9th of 15.

## U1: OSRS GE flip advisor

**Is the profit model itself sound?** Not in its naive form.
- **Backtest (12.8 days, top 60 liquid items):** the median after-tax spread is −0.36%, and the strategy lost money at 100M and 1B bankrolls.
- **Where an edge might remain:** hands-on, minute-by-minute flipping of mid-liquidity items. The backtest neither proves nor rules this out, because it used hourly averages.

**The gp it makes is not money.**
- Real-world trading of gp is banned, and gp has no legal USD value.
- A bond costs $9.99 or about 12.06M gp, so 1M gp ≈ $0.83 of membership.
- Typical case (P50): about 0.4M gp/h. That is about one bond a month for roughly 30 hours a month of trading, i.e. about $0.33/h of membership value.
- **It can never pay for tokens.**

**As a product:**
- Flipping Copilot already gives free item, price and quantity suggestions inside RuneLite. Flipping Utilities has about 75k active installs.
- GE Tracker Premium costs £2/month, which caps what players will pay.
- At $4/month the product needs about 93 subscribers to hit $300/month. The model plateaus around 40.

**Legal:** medium risk.
- The OSRS Wiki price data is under a CC BY-NC-SA licence; the "NC" (non-commercial) term vs paid use is unresolved.
- Jagex's fan content policy restricts profiting from Jagex property.
- Earnings claims would be unsubstantiated.

**The one fix that would change the verdict:** prove a positive after-tax gp/hour with a 5-minute-data backtest **and** two weeks of real manual trades. Even then, it is a hobby unless the price is at or below £2 and it stands out clearly from Flipping Copilot.

## U2: Mandarin learning tools

**Is there open demand?**
- **For the general personalised reader: no.** It is a red ocean. Read Bean, Maayot, Mandarin Mosaic, Readibu, HSKStory and an Obsidian plugin already offer it, and anyone can just ask ChatGPT.
- **For the HSK 3.0 transition: yes, but the window is limited.**
  - The 9-level syllabus was released in November 2025 and is being implemented from July 2026.
  - Gumroad sellers already get paid $3–30 per level deck. Content for the new speaking and translation sections is thin.
  - **Conflicting evidence on exam start dates:** one reviewer cites a worldwide switch on 1 July 2026. Another found no announced formal start date, only one test centre listing 13 Dec 2026. **Check this first.**

**Other openings, ranked:**
1. Cantonese (underserved, but needs a native reviewer).
2. Adult heritage learners who speak but can't read.
3. Tones and listening (getting crowded).
4. Business Chinese (weak evidence).

**Recommended shape:**
- A one-time **$19–29 pack per HSK 3.0 level**, which avoids the 18%/month churn of a subscription. It contains a 2.0→3.0 change deck with audio, level-matched original stories, and a web drill for the new speaking and translation tasks.
- Sell on Gumroad or Lemon Squeezy.
- Use a **free AnkiWeb deck as the lead magnet**.
- Pay a native speaker **$20–50** to spot-check, within the $100 cap.
- Offer the known-word reader later as an upsell.

**Risks:**
- **AI-generated Chinese** without native QA: one public "this sentence is unnatural" post kills trust.
- **Legal:** low.
  - Use CC-CEDICT under its CC BY-SA licence with attribution.
  - Write original stories, not news rewrites.
  - Don't claim to be "official".
  - Use properly licensed text-to-speech (TTS) audio.
  - Label content as AI-generated (EU AI Act Article 50).

**Founder fit (not scored by the rubric):** the user is an active learner who already builds study tools. That is a real advantage for taste and dogfooding, and a reason to prefer U2-W over similarly scored ideas from the first run if the user wants to work on it personally. It does not replace native QA.
