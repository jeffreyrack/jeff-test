# Autonomy Auditor: U3, AI Mandarin tutor (2026-10-06)

Scored against `operator-constraints.md` (sponsor budget: 2–4 h one-time, 1 h/week or less ideally, 3 h/week hard maximum) and the Autonomy row of `scoring-rubric.md`. Companion to `autonomy-auditor.md`, which covers U1 and U2.

| ID | Idea | Score | Human setup hrs (one-time) | Human hrs/week ongoing | Hard gates | Scales without humans? |
|---|---|---|---|---|---|---|
| U3 | AI Mandarin tutor (AI-led lessons, text and voice practice) | **7** | 4–6 h sponsor (MoR KYC, LLM/speech API billing and possible ID verification, recruiting the calibrator, 1–2 h recording his own learner audio for the gold set), plus 6–10 h of **paid** native calibration (about $100–250, deferred until after first revenue to stay under the $100 cap) | 0.75–1.5 h (Reddit presence, API spend/limit decisions, rare escalations), plus **event-triggered re-calibration** when the model changes: about 2–3 contractor hours, 2–4 times a year (under 0.25 h/week averaged) | MoR KYC; API accounts with a card (OpenAI org ID verification for some newest models; Azure card and phone verification); hiring and paying the native calibrator; YouTube/TikTok API audit before automated public posting; Reddit posting | **Yes for labour.** No human work per sale or per lesson, and no content library to review. Inference cost scales with use, but that is a unit-economics issue, not a labour one. Escalations grow slowly with users |

---

## Lifecycle

| # | Step | Who | Hours |
|---|---|---|---|
| 1 | Domain, MoR KYC (Lemon Squeezy/Paddle store review), payout bank | Human-once | 1.25 |
| 1 | LLM + realtime/TTS/STT API accounts, card, auto-recharge and spend caps; OpenAI Verified Organization (government ID) if the chosen model needs it | Human-once | 0.5–0.75 |
| 1 | Transactional email, Cloudflare Turnstile (to stop bots burning free voice minutes) | Human-once / AI | 0.25 |
| 2 | PWA, lesson engine, learner memory, SRS of mistakes, voice pipeline, eval harness | AI | 0 |
| 2 | **Gold set:** sponsor records about 100 of his own utterances (real learner tone errors); a native contractor labels them, plus about 300 text corrections and 20 lesson transcripts | Sponsor 1–2 h; contractor 6–10 h | |
| 3 | Launch on own site as a PWA (no app-store fee or review) | AI | 0 |
| 4 | Reddit show-and-tell and genuine participation | Human-recurring | 0.5–1/wk |
| 4 | Demo clips: the AI can generate them, but an authentic one needs the sponsor's voice; YouTube/TikTok channels need phone verification | Human-once | 1–2 |
| 4 | SEO pages | AI | 0 |
| 5 | Sale: MoR webhook unlocks the plan; lessons delivered live | AI | 0 |
| 6 | Support (microphone and browser problems, refunds through the MoR API) | AI | ~0 |
| 6 | Disputed corrections ("my teacher says this is fine"), safety incidents (minors, jailbreaks over voice) | AI triage, human escalation | ~0.25/wk |
| 7 | Prompt and curriculum maintenance; nightly eval run; migrating to a new model when the old one is deprecated | AI | 0 |
| 7 | **Re-calibration when the model changes** (refresh the gold set, spot-check about 50 new outputs) | Contractor, sponsor approves payment | 2–3 h, 2–4×/yr |
| 8 | VAT handled by the MoR; raising API spend limits; annual taxes | Human | 0.25/wk + 2–3 h/yr |

## Is a one-time native calibration plus automated evals enough?

**For text lessons and corrections: mostly yes, with event-triggered re-calibration.** Live delivery does remove U2's scaling cliff, because there is no per-user content to review. It also means nobody sees the errors. Learners can't detect wrong corrections, so user reports are a weak signal and automated evals are the only check that keeps running. Here is what the AI can run on its own:
- Regression tests against the native-labelled gold set on every prompt or model change.
- Multi-model judging of sampled transcripts, including a Chinese-native model such as Qwen or DeepSeek. Disagreements between judges get flagged.
- Deterministic checks: pinyin against CC-CEDICT plus polyphone rules, tone-sandhi rules (3-3, 一, 不), and HSK-level coverage.
- A TTS-to-STT round trip to catch audio that misreads polyphones.

Pure one-time calibration is not enough because the gold set ages as models change. Budget a short re-calibration each time the model changes.

**For tone and pronunciation grading: no.** This feature cannot be validated autonomously:
- For zh-CN, Azure pronunciation assessment gives phoneme accuracy scores but does not return the phonemes the learner actually spoke. Prosody scoring is en-US only. So it can say "this syllable was weak" but not "you said tone 2, not tone 3".
- Realtime speech-to-speech LLMs judging tones are unverified.
- SSML-forced wrong tones can serve as synthetic test cases, but they are not the same as real learner errors.

There are two options:
1. Keep the feature descriptive. Show the learner's pitch contour (pYIN) against the native reference, plus "I heard: …" from STT, and make no claims about correctness.
2. Budget recurring native audio checks of about 0.5 h/week, which lowers autonomy to 6.

**Platform/policy flags.**
- EU AI Act Art. 50(1) requires telling users they are talking to an AI. It has been in force since 2 Aug 2026.
- Art. 50(2) machine-readable marking of synthetic audio applies to new systems now. Legal should confirm whether we are the "provider".
- OpenAI policy requires telling users that TTS voices are AI-generated, and requires users to be 13+.
- Videos uploaded through the YouTube API from unaudited projects are locked to private. TikTok is similar.
- Don't store voiceprints (Illinois BIPA).
- Reddit self-promotion limits apply.

Sources: [Azure pronunciation assessment](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-pronunciation-assessment), [OpenAI org verification](https://help.openai.com/ca-es/articles/10910291-api-organization-verification), [Goodwin: Art. 50 in force](https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force).
