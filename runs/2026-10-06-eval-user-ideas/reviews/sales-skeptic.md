# Sales Skeptic review: user ideas U1 and U2 (2026-10-06)

| ID | Idea | Score | P(≤30d) | P(≤90d) | P50 days | P90 days | Kill shot |
|---|---|---|---|---|---|---|---|
| U1 | OSRS GE flip advisor (paid tier) | **2** | 2% | 8% | >180 (hard gate fail) | never | The product's own backtest shows its core promise ("profitable flips") is false after the 2% tax, and the closest competitors are free (Flipping Copilot, in the client) or £2/mo (GE Tracker) with years of trust. |
| U2 | Mandarin personalised reader (assumed form) | **4** | 12% | 35% | ~80 | never (~45% chance of no sale by day 180) | AI-written Chinese that no native speaker has checked, sold into a field crowded with 2026 "AI graded reader" apps. One learner posting "this sentence is unnatural" kills trust in the one channel that works (Reddit). |

Scoring: 1–10 sale plausibility per `scoring-rubric.md`. The probabilities assume the human sponsor does the KYC and any community posting.

---

## U1: OSRS Grand Exchange flip advisor

### Part A: Is the flipping model itself profitable? (personal-profit question)
**Verdict: not proven, and the evidence leans negative for a scanner-driven approach. Even if it works, the profit cannot fund tokens.**

- **The evidence is fair, but it does not settle the question.** `sim.py` picks the 60 *most liquid* items, which have the tightest spreads, so it is biased against profit. It uses 1h *average* prices, which hide the intra-hour spread that real flippers capture. It covers only 12.8 days. On the other hand, its fill rule (buy fills only when the next hour's average low is at or below the bid) correctly models adverse selection, and the forced 12h dump with tax is realistic. Conclusion: "a naive liquid-item margin scanner loses after a 2% tax" is credible. "All flipping is unprofitable" is not shown.
- **The snapshot numbers are fantasy.** `snap.py` reports 3.9M per 4h and `cap.py` reports 6.4M per hour. Both assume fills at the extremes of the spread and/or more than 100 simultaneous items. A member has 8 slots.
- **Where an edge probably still exists:** mid-liquidity items with 2–30% spreads, margin-checked every few minutes, with active slot rotation. That is hands-on human work, contested by thousands of other flippers, and the 2% tax takes a fixed bite from every round trip.
- **What the gp is worth:** 12.06M gp buys one bond, which is 14 days of membership. That is roughly **$0.5–0.8 of membership value per 1M gp** (check the current store price of a bond). A strong flipper earning 2M gp/hour therefore "earns" about $1–1.50/hour of membership, which cannot legally become USD. **Personal use contributes $0 to the $300/month target.**

### Part B: Will anyone pay for it?
1. **First buyer:** a member who flips on r/2007scape or r/OSRSflipping and already has RuneLite installed. That player already has **Flipping Copilot** (free, an "AI flipping assistant" that suggests trades inside the client), **Flipping Utilities** (free profit tracking), and **GE Tracker**, whose premium is **£2/month** and includes a flip finder, alerts and profit tracking ([pricing](https://www.ge-tracker.com/pricing)). The proposed $4–6/month is 2–3x the price of the established paid incumbent and is offered as a web tab outside the client.
2. **Traffic in 30 days:** Reddit posted by the human is *optimistic*. A post showing a backtest that loses money will not sell anything, and self-promotion rules apply. Creator affiliates are *fantasy* with no proof and no audience. SEO for "best items to flip osrs" is *fantasy* within 90 days: GE Tracker, the Wiki and YouTube own that search.
3. **Why pay instead of the free options?** Only if the recommendations visibly beat Copilot. Right now there is no evidence they do, and the evidence that exists is negative.
4. **Trust gap:** moderate. Players do pay small amounts for game tools. But an anonymous site that sells "profit" calls with no track record looks like the many flipping scams the community already distrusts.
5. **Conversion math:** $5/month × about 0.9 after fees means **about 67 subscribers** to reach $300/month. At a 2–4% free-to-paid rate that is 1,700–3,300 active free users, all won from incumbents. The *first* sale needs about 1–3k visits from a well-received Reddit post, which is not achievable without a winning record.
6. **Structural problem:** if the signals ever work, selling them to many users crowds the same thin-volume items and destroys the edge. "If it works, why sell it?" applies with full force.
7. **Steelman:** OSRS has a large, engaged player base that already pays for tools (GE Tracker's subscription business exists). A *verifiably* tax-aware advisor with a public, audited P&L could get attention.

**Kill shot:** the value proposition is "profit", and the operator's own data says the naive version loses money. Free in-client alternatives already exist.
**Fix:** treat U1 as a hobby, not a token-funding business. Only reconsider if (a) a 5m-data backtest on mid-liquidity items **and** (b) two weeks of real manual trading with 8 slots both show positive gp/hour after tax, published openly. Even then, price it at or below GE Tracker's £2 level and accept that it will probably fail the P50 ≤ 180-day gate.

---

## U2: Mandarin learning tools (assumed: personalised known-word reader)

1. **First buyer:** an English-speaking adult self-learner at HSK 3–4 who has a Pleco flashcard list or Anki deck of 1–2k words, posts on r/ChineseLanguage, and already pays for Du Chinese, Maayot or LingQ. This buyer is concrete and already spends money, which is good.
2. **Traffic in 30 days:** a Reddit show-and-tell by the human, who is a genuine learner, is *realistic* once: a free, useful tool from an actual learner is tolerated, and that post could bring 1–3k visits. An AnkiWeb shared deck as lead magnet is *optimistic*: it brings slow trickle downloads, and links out are weak. SEO for "HSK 3 reading practice" is *fantasy* before day 90.
3. **Why pay instead of the alternatives?** ChatGPT: "write me an HSK 3 story" gets 80% of the value for free. Established sellers: Du Chinese, Chairman's Bao and Mandarin Companion have human-edited text and native audio. Direct AI competitors launched in 2026 include Read Bean, ChineseBoo, Pocket Chinese Reader, Audibee, and yaya.press's DIY graded reader. Doing nothing: Pleco plus free graded readers. The only real gap is **matching to the learner's own known-word list** (an imported Pleco/Anki export rather than an HSK level). That gap is real but narrow, and LingQ, Migaku and yaya.press partly cover it.
4. **Trust gap:** high on quality, not on payment. Learners cannot judge the Chinese themselves, so they rely on reputation, and no one on the team can check the text to native level. One public catch of an error does lasting damage.
5. **Conversion math:** at $7/month net about $6.15, you need **about 49 subscribers** for $300/month. A Reddit launch of 2k visits × 5–10% email capture gives 100–200 free users. At 2–4% conversion that is 2–8 paid users, so a first sale is plausible but $300/month is far off. Churn on consumer language subscriptions is brutal: expect 3–4 months of average lifetime.
6. **Steelman:** the founder is a real user scratching his own itch, which gives an authentic voice in a community that rewards that. Generation cost is almost zero, and "import your Pleco list, get a story at 97% coverage tomorrow morning" is a clear and demonstrable hook.

**Best-fit wedge (the assumed form is weak).** I recommend **HSK 3.0 exam prep**. The new 9-level HSK 3.0 replaced HSK 2.0 worldwide on **1 July 2026**, and it adds new vocabulary (about 11,000 words) and *new mandatory speaking and translation sections* ([Beijing gov](https://english.beijing.gov.cn/studyinginbeijing/news/202512/t20251222_4355931.html), [hsklord](https://hsklord.com/blog/hsk-3-0-changes-2026)). Exam takers have a deadline, have already paid exam fees, search with clear intent ("new HSK 3 vocabulary list", "HSK 3.0 level 4 speaking practice"), and much of the existing material is still based on 2.0. Concrete form: a one-time **$19–29 per-level pack** sold through a merchant of record. It contains the official word-list deltas (2.0 → 3.0) as an Anki deck with audio, plus a web drill for the new speaking and translation tasks with AI feedback. This scores better because the core content is the deterministic official word list (less exposure to errors in generated Chinese), there is a deadline-driven buyer, and one-time payment avoids subscription churn. The weakness: hsklord, HSK Online, Hack Chinese and free AnkiWeb decks are moving in too, so speed matters. Second choice: a known-word coverage **Chrome extension** (no generated Chinese, and the Chrome Web Store provides distribution), though Migaku and the free Zhongwen extension limit the price you can charge.

**Kill shot:** unchecked AI-written Chinese in a crowded field of AI readers, where ChatGPT is the free substitute.
**Fix:** change the form to the HSK 3.0 per-level one-time pack, and pay a native speaker on a per-piece basis (about $20–50, within the $100 cap) to spot-check the sample sentences before launch.
