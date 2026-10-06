# User-supplied ideas

Both ideas came from the user and were normalised into the Idea Brief template. Fields the user did not specify are marked `(assumed)`.

## U1 — OSRS Grand Exchange flip advisor ("tell it your gp and items; it tells you what to buy/sell and at what price")

- **Persona:** User-supplied
- **One-liner:** A tool for Old School RuneScape players. The player enters their gp bankroll (optionally an item watchlist). The tool recommends buy prices, sell prices and quantities for Grand Exchange "flips", then tracks and backtests the profit. It is for personal use first, and becomes a paid product only if it is shown to be profitable.
- **Customer:** (assumed) OSRS players who flip on the GE, i.e. those already using RuneLite flipping plugins, GE Tracker, or flipping Discords and YouTube.
- **Problem / desire:** "I want to grow my gp without grinding, and I don't know which items have a real margin after the GE tax or how many I can move."
- **Offering:** A web app or RuneLite-adjacent companion that recommends flips. The trades are placed **manually by the player**: there is no game-client automation, so it does not break the macroing rules. Data comes from the public OSRS Wiki real-time prices API (`/latest`, `/1h`, `/5m`, `/timeseries`, `/mapping`), which allows reuse with a descriptive User-Agent.
- **Price & revenue model:** (assumed) Free tier plus a $4–6/month premium for more slots, faster refresh and alerts, through a merchant of record or Patreon. **Gp itself cannot legally be turned into USD:** real-world trading is banned by the Jagex ToS. Personal "profit" can only be spent in-game, including on Old School Bonds (membership).
- **Physical items required?** No

### Evidence gathered before review (live data, 2026-10-06; scripts in `../evidence/`)
- **GE tax:** 2% of the sale price, rounded down, capped at 5M per item. Items under 50 gp and a list of exempt items pay none. The rate went from 1% to 2% on 29 May 2025 (OSRS Wiki, Grand Exchange page).
- **Buy limits** apply per item per 4 hours. Members have **8 GE offer slots**, free-to-play players have 3.
- **Old School Bond:** about 12.06M gp on the GE today. A bond is 14 days of membership; check the current USD price of a bond to convert gp into membership value.
- **Snapshot (`snap.py`, latest instant prices):** 1,105 items show a fresh, positive after-tax spread. If every order filled at the quoted price, a 10M bankroll would "earn" about 3.9M gp per 4 h. **This is not realistic:** it assumes fills at the extremes of the spread.
- **Hourly backtest (`sim.py`):**
  - Setup: 12.8 days of 1h data on the 60 most-liquid items, chosen by liquidity only. Bid at last hour's average instant-sell price, ask at last hour's average instant-buy price, only after a positive after-tax spread for 3 hours in a row. Fills limited to 5–10% of the next hour's volume, with buy limits respected and a forced dump after 12 h.
  - **The median after-tax hourly spread on these 60 items is −0.36%.** Only 3 of the 60 had a positive median.
  - **The strategy lost money at every bankroll tested:** 10M about flat, 100M −8 to −12M, 1B −25 to −71M over 12.8 days.
- **Capacity upper bound (`cap.py`, 1h averages):** 924 of 1,337 actively traded items had a positive after-tax average spread in the last hour. Taking 10% of the volume on **all** of them at once would give about **6.4M gp/hour** with about 868M tied up. That is impossible for a person limited to 8 GE slots. The opportunities that remain are mid-liquidity items with 2–30% spreads but thin volume.
- **Interpretation:** a naive margin-scanner loses to the 2% tax on liquid items. Any profit needs wider-spread, lower-volume items, intra-hour (5m) timing, and active slot management. That makes it a hands-on activity, and the edge is contested by many other flippers.

### Upfront capital
| Item | Cost |
|---|---|
| Hosting (Cloudflare Pages/Workers free tier) | $0 |
| Domain (optional) | $12 |
| **Total** | **$0–12** |

### Monthly running costs (excluding operator tokens)
About $0 on free tiers. Merchant-of-record fees are around 5% + $0.50 per transaction, or Patreon takes 8–12%.

### Customer acquisition plan
(assumed) Run a free public site with flip suggestions and earn SEO from "osrs flipping" and "best items to flip osrs" searches. Post on r/2007scape and r/OSRSflipping (subject to their self-promotion rules). Get mentioned by flipping YouTubers. Use a free-to-premium upsell.

### Initial traffic approaches
1. Reddit: share the backtest and profit-tracking results as a post on r/OSRSflipping. Fast, if the community allows it.
2. YouTube or Twitch flipping creators, through an affiliate code. Medium speed.
3. SEO "best items to flip" pages generated from live data. Slow, 3–6 months.

### Path to first sale
Personal use for 2–4 weeks to prove the gp/hour. Publish a free site plus the proof. Add a premium tier after hitting a traffic threshold. (assumed) First paid subscriber in 45–90 days.

### Who does what
- **AI operator:** build the site and engine, refresh the data, generate content, handle support email.
- **Human sponsor:** merchant-of-record or Patreon KYC, any Reddit or Discord posting (bot accounts are banned), and placing their own trades during the personal test phase.

### Moat — why not just ask ChatGPT?
A chatbot has no live price data. But free specialised tools already exist: the Flipping Copilot RuneLite plugin, Flipping Utilities, GE Tracker, and prices.runescape.wiki itself. Any moat would have to come from better recommendations, which need proof.

### Biggest risks (user/ideator view)
- The 2% tax has made flipping much less profitable, and the backtest above shows a naive strategy loses money.
- Free incumbents, with an in-client RuneLite plugin advantage.
- Profit is in gp, which cannot be legally converted to USD. Personal use does not fund tokens; only product subscriptions do.

---

## U2 — Chinese (Mandarin) learning tools productised from the user's personal practice repo

- **Persona:** User-supplied
- **One-liner:** (assumed concrete form) A personalised Mandarin reading-practice service. Learners import their known-word list (an Anki or Pleco export, or an HSK level) and get daily short stories or news rewrites at ~95–98% known-word coverage, with TTS audio, a pinyin toggle and tap-to-save new words. It grows out of tools the user already built for their own study.
- **Note:** The user has a private repo of personal Chinese-practice tooling, which was not inspected in this run (access was not granted), so the exact features are unknown. **Evaluators should also suggest the best-fit wedge** within Chinese learning: HSK 3.0 decks, graded readers, tone or listening drills, character-writing practice, a heritage-learner niche, and so on.
- **Customer:** (assumed) Self-directed adult Mandarin learners at HSK 2–5 who use Anki or Pleco, are active on r/ChineseLanguage and r/LearnChinese, and already pay for Du Chinese, The Chairman's Bao, LingQ, Maayot, HelloChinese, etc.
- **Problem / desire:** "Graded readers are either too easy or too hard, and none of them match the words I actually know."
- **Offering:** A web app (PWA) with a daily email or push lesson.
- **Price & revenue model:** (assumed) $6–9/month or $49/year subscription, with a free daily story.
- **Physical items required?** No

### Upfront capital
| Item | Cost |
|---|---|
| Domain | $12 |
| Hosting (free tier) + TTS (browser/free tier or ~$1–5/mo at low volume) | $0 |
| **Total** | **~$12** |

### Monthly running costs (excluding operator tokens)
LLM generation per user per day: (assumed) about $0.002–0.01 for a short story on a small model. TTS: $0–5. Merchant-of-record fees: about 5% + $0.50.

### Customer acquisition plan
(assumed) A free daily story with a public archive, giving SEO for "HSK 3 reading practice" and similar searches. Learner communities, the Anki shared-decks listing as a lead magnet, and a Chrome extension for reading assistance.

### Initial traffic approaches
1. A free Anki deck or Pleco flashcard export as a lead magnet, listed on AnkiWeb shared decks. Medium speed.
2. Reddit: r/ChineseLanguage and r/LearnChinese, as genuine participation by the human, plus a show-and-tell post. Fast.
3. SEO graded-reading pages per HSK level. Slow.

### Path to first sale
Launch the free daily story, collect emails, and open the paid personalisation tier. (assumed) First sale in 30–60 days.

### Who does what
- **AI operator:** generate and QA content (needs a native-level check for errors), build the app, send emails, support.
- **Human sponsor:** payment KYC and community posting. The user is a learner, not a native speaker, so they cannot fully QA the Chinese.

### Moat — why not just ask ChatGPT?
Weak on its own. A learner can ask ChatGPT for "a story using HSK 3 words". The moat would be persistent known-word tracking, spaced repetition integration, audio, and daily habit and delivery.

### Biggest risks (user/ideator view)
- A saturated market with well-funded apps (Duolingo, HelloChinese, Du Chinese) and direct "AI personalised reader" competitors.
- AI-generated Chinese can contain unnatural phrasing, which damages trust with learners.
- Consumer subscription churn is high.
