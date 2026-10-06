# Autonomy Auditor: user ideas U1 and U2 (2026-10-06)

Scored against `operator-constraints.md` (sponsor budget: about 2–4 h one-time, 1 h/week or less ideally, 3 h/week hard maximum) and the Autonomy row of `scoring-rubric.md`.

| ID | Idea | Score | Human setup hrs (one-time) | Human hrs/week ongoing | Hard gates | Scales without humans? |
|---|---|---|---|---|---|---|
| U1 | OSRS GE flip advisor | **5** | 3–4 h for accounts, **plus 15–30 h of in-game trading** during the 2–4 week personal validation phase | 1–2 h (Reddit/Discord presence, creator outreach) | Human must place every validation trade (no game automation); MoR/Patreon KYC; Reddit/Discord accounts; RuneLite Plugin Hub PR and review (only if the plugin route is taken) | **Yes** after validation. No per-sale human work. Edge crowding is a product risk, not a labour risk |
| U2 | Mandarin personalised graded reader | **6** | 4–6 h (MoR KYC, email/TTS/LLM billing, AnkiWeb/Reddit accounts, recruiting a native-speaker reviewer) plus about 4–6 h of **paid** native calibration review | 1–1.5 h sponsor, plus about 1 h/week of **paid native-speaker QA** (contractor, roughly $60–100/month) | MoR KYC; API billing cards; contracting and paying the native reviewer; Reddit posting | **Partly.** Sales and delivery scale. Quality only scales if stories come from a pre-reviewed library; with per-user generation, QA and error reports grow with users |

---

## U1: OSRS Grand Exchange flip advisor

| # | Stage / step | Who | Hours |
|---|---|---|---|
| 1 | Domain, Cloudflare account (email verification/CAPTCHA), support inbox | Human-once | 0.75 |
| 1 | Merchant-of-record or Patreon KYC, payout bank | Human-once | 1 |
| 1 | OSRS Wiki prices API User-Agent with contact address | AI | 0 |
| 2 | Price engine, 5m/1h backtester, web app, profit tracker | AI | 0 |
| 2 | **Personal validation: log in, place and re-price GE offers, record real fills** | Human (time-boxed) | about 1 h/day for 2–4 weeks = 15–30 |
| 2 | Optional RuneLite plugin for automatic trade import: AI writes it; the human submits the PR from their GitHub account; RuneLite devs review it manually | Human-once | 0.5, plus days to weeks of review wait |
| 3 | Launch on own site (no store review) | AI | 0 |
| 4 | Reddit posts (r/OSRSflipping, r/2007scape), Discord server creation and moderation | Human-recurring | 0.5–1/wk |
| 4 | Creator/affiliate outreach: AI drafts emails; deals often close over Discord DMs or calls | Mixed | 0.5/wk |
| 4 | SEO "best items to flip" pages from live data | AI | 0 |
| 5 | Sale: MoR/Patreon webhook unlocks premium | AI | 0 |
| 6 | Email support, refunds through MoR API; chargebacks handled by MoR | AI (human for escalations) | about 0 |
| 7 | Data cron, new items via `/mapping`, tax-rule changes | AI | 0 |
| 8 | VAT handled by MoR/Patreon; annual income tax filing | Human | 2–3 h/yr |

**Hard gates.** The validation phase is the big one. Game automation is off-limits, so the AI cannot place, adjust or observe real trades; it is blocked until a human plays. The phase also assumes the human has membership (a bond, about 12.06M gp, or cash) and an existing gp bankroll. The repo's backtest is negative (median after-tax spread −0.36%), so the most likely outcome is that the human spends 15–30 h and the "prove it's profitable" gate stays closed. That gp also cannot fund tokens.

**Platform policies.**
- Jagex: the advisor must never add auto-offer or click automation.
- The Third Party Client Guidelines checked today do not restrict GE price-suggestion features, but the RuneLite Plugin Hub rules are silent on paywalls. Jagex's modding guidelines for its other game ban paid features. Keep premium gating on the website, not in-plugin.
- Reddit bans self-promotion spam. Discord bans automated user accounts ("self-bots"); a declared bot in your own server is fine.
- Mass-generated item pages risk Google's scaled-content demotion.

**Scaling.** No human work per sale. Community presence is a fixed 1–2 h/week.

**Reducing human load.** Replace the sponsor's live trading with paper trading on 5m data, plus a 3–5 h human spot check. Or crowd-source validation from opt-in beta users through plugin trade import.

---

## U2: Mandarin personalised graded reader

| # | Stage / step | Who | Hours |
|---|---|---|---|
| 1 | Domain, MoR KYC | Human-once | 1.25 |
| 1 | Transactional email (Resend/Postmark) signup; AI sets DNS if given an API token | Human-once | 0.5 |
| 1 | LLM and TTS API accounts with a billing card | Human-once | 0.5 |
| 1 | AnkiWeb account; Chrome Web Store developer account ($5, identity check) only if the extension is built | Human-once | 0.25–0.75 |
| 1 | **Recruit native reviewer (Upwork/Fiverr/italki tutor), agree terms, set up payment** | Human-once | 2 |
| 2 | PWA, Anki/Pleco import, jieba segmentation, coverage scoring, generation, TTS, pinyin | AI | 0 |
| 2 | **Native calibration audit of about 50 stories** to measure the error rate and tune prompts and rules | Contractor (paid, about $60–150) | 4–6 |
| 3 | Launch on own site; Anki lead-magnet deck upload | AI / Human-once | 0.25 |
| 4 | Genuine Reddit participation (r/ChineseLanguage, r/LearnChinese) | Human-recurring | 1/wk |
| 4 | SEO archive of daily stories | AI | 0 |
| 5 | Sale: MoR webhook provisions access; daily personalised story generated and emailed | AI | 0 |
| 6 | Email support, MoR refunds | AI | 0 |
| 6 | "This sentence is wrong" reports: AI triages, disputed cases go to native reviewer | AI + contractor | grows with users |
| 7 | **Weekly sampled native QA** (about 10 stories); sponsor approves the contractor payment | Contractor 1/wk, sponsor 0.25/wk | |
| 8 | VAT by MoR; contractor payments; annual taxes | Human | 2–3 h/yr |

**Native-speaker QA is the core hidden task.** The sponsor is a learner and cannot certify the Chinese. LLM output can have unnatural collocations and wrong measure words. Dictionary-based pinyin (pypinyin and similar) and TTS both mis-handle polyphones such as 行, 了, 得, 长 and 还. For a learner product these are trust-killing errors. The AI cannot hire, contract or pay a reviewer, so that is a human gate.

Per-user generated stories can never be human-reviewed: the QA burden scales with users. That is the scaling cliff.

The calibration audit ($60–150), plus the $12 domain and the $5 Chrome Web Store fee, can push upfront spend toward the $100 cap. Defer the audit until after the first revenue, or cap it at about $80.

**Platform policies.**
- Mass AI story pages risk Google's scaled-content demotion.
- Label content as AI-generated. "News rewrites" published to the public may fall under the EU AI Act Article 50 transparency duty (applicable since 2 Aug 2026); legal should confirm. Original stories avoid this and the copyright issue.
- Reddit self-promotion limits apply.
- AnkiWeb shared decks must not contain copyrighted material.

**Best wedge for autonomy.**
1. **Personalisation by selection, not generation.** Batch-generate a library of stories per HSK level, have a native reviewer check each batch once, then personalise by picking the reviewed stories at 95–98% coverage for each user's known words and glossing the rest. QA becomes a fixed cost per batch instead of a per-user cost.
2. Lower-QA wedges: HSK 3.0 Anki decks as a one-time product, reviewed once; character-writing practice built on open stroke data (Make Me a Hanzi), which needs almost no native QA.
3. Avoid tone drills. They depend on TTS tone sandhi being correct, which makes them the highest-QA wedge.

Sources checked: [Third Party Client Guidelines](https://oldschool.runescape.wiki/w/Update:Third_Party_Client_Guidelines), [RuneLite plugin-hub](https://github.com/runelite/plugin-hub), [Jagex modding guidelines (Dragonwilds)](https://legal.jagex.com/docs/policies/runescape-dragonwilds-community-modding-guidelines).
