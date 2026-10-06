# Sales Skeptic review: U3, the AI Mandarin tutor (2026-10-06)

U3 replaces U2 (the graded-reader form). The U2 review in `sales-skeptic.md` still stands for that form and is not repeated here.

| ID | Idea | Score | P(≤30d) | P(≤90d) | P50 days | P90 days | Kill shot |
|---|---|---|---|---|---|---|---|
| U3 | AI Mandarin tutor, general form (lessons + text/voice chat, $9–15/mo) | **3** | 6% | 25% | ~130 | never (~45% chance of no sale by day 180) | "Cheaper than a human tutor" is true of every rival. The buyer is really comparing it with ChatGPT/Gemini voice (free or already paid for) and with funded Mandarin AI tutors that cost the same or less. An unknown PWA has nothing that stands out. |
| U3-W | Recommended wedge: HSK 3.0 speaking-section mock and feedback (one-time $19–29 per level) | **5** | 15% | 40% | ~70 | never (~35% chance of no sale by day 180) | Mock-test incumbents (Mandarin Temple, SuperTest, HanSpik) already advertise AI speaking feedback for HSK 3.0. With the official scoring method unpublished, "AI predicts your speaking score" can't be backed up. |

Scoring: 1–10 sale plausibility per `scoring-rubric.md`. Assumes the human sponsor does the merchant-of-record KYC and any Reddit posting. Build time (about 2–3 weeks for a usable voice tutor) eats into the 30-day window.

---

## U3: AI Mandarin tutor (general form)

**The comparison is wrong.** The user compares the product with italki/Preply at $10–30/hour. People who pay for human tutors are buying a human: accountability, cultural nuance, someone who notices them. They are a different segment. Someone choosing an *AI* tutor compares it with other AI options, and those cost **$0–25/month**:
- **General assistants:** ChatGPT voice speaks Mandarin. Free accounts get a daily Advanced Voice preview and then drop to standard voice; Plus ($20) gives about 5x the free limit, and many learners already pay for it for work. Gemini Live is free. "Talk to me in HSK 3 Chinese and correct my mistakes" is one prompt away.
- **Mandarin-specific AI tutors:** SuperChinese CHAO AI $24.99/mo; HelloChinese $11.99/mo (or $69.99/yr); Mandarin Temple Pro $19/mo with AI speaking, roleplay and HSK mocks; the "Speak Chinese" AI tutor app; Lyrin AI (free with in-app purchases).
- **Multi-language AI tutors:** TalkPal $9.99, Talkio $9, Speak $14.99, Langua $19.99.

Once AI is the reference point, $9–15/month is the market median. "Cheaper than a human" is true of every competitor, so it doesn't set this product apart.

1. **First buyer:** an English-speaking adult at HSK 2–4 on r/ChineseLanguage who wants speaking reps without the awkwardness of a human tutor. This buyer is real and pays for apps, but usually already has HelloChinese or ChatGPT.
2. **Traffic in 30 days:** a Reddit show-and-tell by the human is *optimistic*. AI-tutor launch posts are now routine on the language subreddits and often get a cold reception, and self-promotion rules apply. Demo clips are *optimistic*: the human would have to post them, since the operator can't. The AnkiWeb lead magnet is *optimistic* (slow trickle, weak link to a tutor product). SEO for "AI Chinese tutor" is *fantasy*: funded apps and listicles own that search.
3. **Why pay instead of:** (a) free options: Gemini Live and the ChatGPT free voice preview; (b) ChatGPT: about 80% of the conversation value for $0 extra; (c) doing nothing: Pleco plus shadowing; (d) established apps: they have app-store reviews, native-recorded audio and years of curriculum. The only pitch left is "persistent memory + mistake SRS + tone feedback". ChatGPT memory partly covers memory, and tone feedback is the weak spot (point 4).
4. **Trust gap:** the problem is product trust more than payment trust. *Tone feedback is the stated differentiator, and it is the part an LLM pipeline gets wrong most easily.* Speech-to-text tends to "correct" a mistoned syllable to the intended character, so the tutor praises wrong tones. The learner can't tell, and nobody on the team can check it to native level. If the product claims tone feedback, it needs a real pronunciation-assessment API (e.g. Azure's zh-CN pronunciation assessment; verify pricing and tone granularity), not LLM judgement.
5. **Conversion math:** $12/mo is about $10.90 net, so **about 28 subscribers** for $300/month. A good Reddit post brings 1–2k visits; ~15% try it (≈225), 2–3% convert, giving **4–7 paid** at best. A first sale is plausible only if the post lands. Each free-tier voice minute costs real money, which keeps the free trial stingy and lowers conversion further. Consumer language-app churn means ~3–4 months average lifetime.
6. **Steelman:** willingness to pay is proven (SuperChinese charges $24.99 for an AI tier), and speaking practice is the most-cited unmet need among self-learners. A founder who built it for his own daily use has an authentic story, and a polished 60-second demo of the tutor catching a tone error *correctly* would get attention.

**Kill shot:** the product's niche gets squeezed from both sides: free general voice assistants below, funded Mandarin AI tutors above. "Cheaper than a human" isn't a reason to choose *this* AI.
**Fix:** narrow it to a deadline-driven exam wedge (below) with grounded pronunciation scoring, and sell it as a one-time purchase rather than a subscription.

---

## U3-W: Best wedge, the HSK 3.0 speaking-section mock and coach

**Why this wedge:** HSK 3.0 makes speaking **mandatory from Level 3**, built into the main exam. The tasks are reading aloud (pronunciation and tones), picture description, short answers on familiar topics, and a brief opinion with a reason. Translation starts at Level 4. The **first official HSK 3.0 sitting is reported for 13 December 2026**, which is 68 days away (verify on chinesetest.cn). That gives a buyer with a deadline, a sunk exam fee, a format they've never seen, and searches with clear intent ("HSK 3.0 speaking practice", "new HSK 3 speaking test"). Material written for HSK 2.0 does not cover the new tasks.

**Form:** timed, exam-format speaking mocks per level (L3–L6). Read-aloud items are scored by a pronunciation-assessment API, so tone scoring is grounded rather than LLM guesswork. Picture prompts use generated images (cents each). The LLM grades the free-response tasks against a published-style rubric and gives model answers, and the product produces a report of weak tones and phrases to drill. Price: **$19–29 one-time per level, with access through the exam date**. A free single mock acts as the demo.

- **First buyer:** a Western learner registered for the December HSK 3 or HSK 4 sitting who has never taken a speaking test and searches "HSK 3.0 speaking practice" in late October.
- **Traffic:** a Reddit post by the human, "free HSK 3.0 speaking mock: here's the new format", is *realistic* because it is useful, timely news rather than an app pitch. Long-tail SEO on new 3.0 speaking keywords is *optimistic* but better than for "AI tutor", since the terms are new and competition is thinner. Exam-prep teachers and blogs linking to a free mock is *optimistic*.
- **Why pay instead of ChatGPT:** format fidelity, timing, picture prompts, and grounded tone scores. ChatGPT gives none of these unless the learner builds them.
- **Weaknesses:** Mandarin Temple ($19/mo) already advertises HSK 3 mocks with AI speaking feedback, and SuperTest (780k users), HanSpik and HSK Training are in the space. CTI hasn't published how the speaking score combines into a pass, so **never claim score prediction**. Most HSK candidates are in Asia (Thailand, Korea, Indonesia, Vietnam), so an English-only product reaches a minority of takers. Demand comes in spikes around test dates, so revenue will be lumpy.
- **Conversion math:** $24 one-time is about $22.30 net, so about **14 sales/month** for $300. That is much less traffic than 28 retained subscribers, and there's no churn problem.

**Second-choice wedge:** a standalone **tone-accuracy drill** (read-aloud plus pronunciation-API scoring on your own Pleco/Anki words). It is narrow, easy to demonstrate, and sidesteps the generated-Chinese QA problem. It has a lower price ceiling and no deadline.

Sources: [Mandarin Temple pricing](https://mandarintemple.com/pricing), [fast.io AI language tools 2026](https://fast.io/resources/best-ai-for-language-learning-2026/), [italki: best AI apps for Chinese](https://www.italki.com/en/blog/best-ai-app-to-learn-chinese), [HelloChinese App Store](https://apps.apple.com/us/app/-/id1001507516), [Engadget: ChatGPT free features 2026](https://engadget.com/2234173/chatgpt-free-features-2026), [hsklord: new HSK 3 under 3.0](https://hsklord.com/blog/new-hsk-3-3-0-guide), [hsklord: HSK 3.0 changes](https://hsklord.com/blog/hsk-3-0-changes-2026), [GoEast Mandarin: 2026 HSK dates](https://goeastmandarin.com/hsk-exam-dates-details/), [HanSpik](https://mwm.ai/apps/hanspik/6769252925), [SuperTest](https://spark.mwm.ai/en/apps/hsk-study-and-exam-supertest/1335503360), [Mandarin Temple HSK 3 mock](https://mandarintemple.com/learning-materials/mock-tests/3).
