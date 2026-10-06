# Legal Risk Analyst review: user idea U3, AI Mandarin tutor (2026-10-06)

> This is a risk screen, **not legal advice**. The human sponsor carries the risk and should consult a lawyer before relying on it.

| ID | Idea | Legal safety score | Overall risk (Low/Med/High) | Top risk | Key mitigation |
|---|---|---|---|---|---|
| U3 | AI Mandarin tutor (AI-led lessons + text/voice conversation) | 5/10 (6/10 if the day-one mitigations below ship at launch) | Med | Class-action exposure from voice data and open-ended chat. BIPA-style voiceprint claims (a June 2026 ruling held that BIPA can apply when voice data *could* identify someone), plus the new companion-chatbot laws with private rights of action (CA SB 243 now; OR, WA, RI from 2027), triggered if a minor or a vulnerable user reaches self-harm or sexual content | Make the service 18+ only. Do not store raw audio or build speaker models, and use a zero-retention API tier. Get a BIPA-style written consent before turning on voice mode. Keep conversations inside lesson scenarios with moderation and a crisis-referral flow. Disclose "AI tutor" at the start and on a recurring basis. Sell through a merchant of record with click-to-cancel. |

This does not trigger the hard gate (legal safety ≤ 3). Nearly all of the risk comes from design choices, and each mitigation is cheap. Compared with U2 (a graded reader, scored 7/10), the score is lower because U3 adds **live voice and open conversation**.

---

## U3: AI Mandarin tutor

**1. Voice as personal and biometric data.** Likelihood Med × severity High.
- **Illinois BIPA.**
  - Statutory damages are $1,000 per negligent violation and $5,000 per reckless one. The 2024 amendment limits recovery to one per person.
  - In *Delgado v. Meta* (N.D. Cal., June 2026), the court said "BIPA applies if it could" identify the speaker. Voice-AI vendors are active litigation targets (Fireflies, Otter, and the May 2026 voice-model suits).
- **Other US biometric laws.**
  - Texas CUBI is enforced by the state attorney general.
  - Washington's My Health My Data Act arguably reaches voice recordings from which a voiceprint can be extracted, and it carries a private right of action.
- **CCPA.** It probably does not apply until revenue passes about $26.6M or the service reaches 100k consumers. Comply voluntarily anyway.
- **GDPR.**
  - Voice is personal data. It becomes special-category biometric data only if it is processed to identify the speaker (EDPB Guidelines 02/2021).
  - A lawful basis, a privacy notice, a data processing agreement (DPA) and a transfer mechanism are still required.

*Mitigation:*
- Stream audio to speech-to-text and discard it. Do not store raw audio by default.
- Never use speaker recognition. Pronunciation and tone scoring is fine.
- Use paid API tiers with zero or short retention.
- Show a clickwrap biometric consent with a published retention and destruction policy before voice mode is enabled.
- Do not use China-hosted ASR, TTS or LLM APIs, even though they are tempting for Mandarin quality:
  - The DOJ bulk-data rule restricts sending biometric identifiers of more than 1,000 US persons to covered persons.
  - iFlytek is on the US Entity List.

**2. Minors.** Likelihood Med × severity High.
- Language learners include teens, and parents of heritage-language children buy these apps.
- The amended COPPA Rule (compliance date 22 Apr 2026) lists voiceprints as personal information, and audio files were already covered.
- Provider terms make the choice for you:
  - The Gemini API forbids services "likely to be accessed by" under-18s.
  - OpenAI requires parental consent for ages 13–17 and zero data retention for any data from under-13s.
- *Mitigation:*
  - Make the service 18+ through a neutral age gate at signup, with no child-directed design or marketing.
  - Do not build a "heritage kids" wedge.
  - Close any account where you learn the user is a minor.

**3. Chatbot disclosure and companion-chatbot laws.** Likelihood Med × severity Med–High.
- **EU AI Act Article 50(1)** has applied since 2 Aug 2026 and was not delayed by the Digital Omnibus. Users must be told they are dealing with an AI at the first interaction. Article 50(2) also requires synthetic TTS audio to be marked.
- **Whether US companion-chatbot laws apply is unsettled.**
  - California SB 243 (in force 1 Jan 2026, private right of action) covers bots that are "capable of meeting a user's social needs" with anthropomorphic features and sustained relationships.
  - A named, voiced tutor with memory that makes small talk may fall inside that definition. Its exclusions (customer service, productivity, technical assistance) do not clearly cover education.
  - The New York law is in force now. Oregon, Washington and Rhode Island follow in 2027, and Oregon allows $1,000 per violation. Idaho, Nebraska and Iowa will cover all conversational AI from July 2027.
- *Mitigation:*
  - Comply with SB 243 by default:
    - Disclose AI status at the start and every 3 hours.
    - Run a suicide and self-harm protocol that refers the user to crisis lines.
    - Never claim to be human or sentient.
    - Use no romance or "AI girlfriend" scenarios.
    - Use no engagement manipulation.
  - Track SB 243's annual reporting duty, which starts 1 Jul 2027.

**4. Harmful content in open conversation.** Likelihood Med × severity High.
- Learners can steer role-play toward sexual or self-harm topics.
- Character.AI-type product-liability suits have survived motions to dismiss.
- Mandarin complicates naive filters, because 死 is an everyday intensifier ("累死了", "笑死我了"). Naive filters will over-trigger, and blunt crisis flows will annoy learners.
- *Mitigation:*
  - Keep chat inside lesson scenarios.
  - Use a provider moderation API plus a system prompt that refuses off-scenario sexual content.
  - Add context-aware crisis detection and log the incidents.
  - Never present the tutor as a therapist or friend. Illinois and Tennessee restrict AI therapy.

**5. Provider terms.** Likelihood Low–Med × severity High, because losing the provider ends the business.
- Do not use the Gemini free tier: it is barred for EEA, UK and Swiss users, and Google trains on that data.
- OpenAI requires disclosure that its TTS voices are AI-generated.
- Do not clone real voices.

**6. Subscriptions and consumer claims.** Likelihood Med × severity Med.
- **Auto-renewal and cancellation rules.**
  - Comply with ROSCA and California's amended auto-renewal law (express consent, online click-to-cancel, annual reminders).
  - The EU "withdrawal button" rule has applied since 19 Jun 2026.
  - A merchant of record covers VAT and most of the EU withdrawal obligations.
- **Voice credits.** If you sell per-minute voice credits, say clearly whether unused credits expire.
- **Advertising claims.** Avoid "fluent in 90 days" and "native-level tone accuracy" claims. The FTC's Operation AI Comply targets unsubstantiated AI claims, and the backlog notes that tone feedback is unreliable.

---

### Sources
- [California SB 243 summary (Gunderson)](https://www.gunder.com/en/news-insights/insights/client-insight-california-sb-243-new-compliance-requirements-for-operators-of-ai-companion-chatbots)
- [National Law Review: SB 243](https://natlawreview.com/article/ai-regulatory-update-californias-sb-243-mandates-companion-ai-safety-and)
- [Orrick: 2026 state chatbot laws](https://www.orrick.com/en/Insights/2026/04/2026-State-Chatbot-Laws-Key-Provisions-and-Regulatory-Trends)
- [Transparency Coalition: 14 state chatbot laws in 2026](https://www.transparencycoalition.ai/news/watershed-year-for-chatbot-safety-measures-14-new-state-laws-enacted-so-far-in-2026)
- [Hunton: Washington companion chatbot law](https://www.hunton.com/privacy-and-cybersecurity-law-blog/washington-state-enacts-law-regulating-ai-companion-chatbots-with-private-right-of-action)
- [Baker Botts: EU AI Act Article 50 goes live](https://www.bakerbotts.com/thought-leadership/publications/2026/september/eu-ai-act-article-50-transparency-obligations-go-live)
- [ABA: Voiceprints, AI and BIPA](https://www.americanbar.org/groups/litigation/resources/newsletters/class-actions-derivative-suits/voiceprints-ai-bipa-new-trends-biometric-privacy-litigation/)
- [Barnes & Thornburg: Delgado v. Meta](https://laborandemployment.btlaw.com/post/102n7n1/the-voiceprint-you-didnt-mean-to-create-what-delgado-v-meta-means-for-employer)
- [Bloomberg Law: voice-model BIPA suits (May 2026)](https://news.bloomberglaw.com/ip-law/nvidia-sued-by-journalists-podcasters-over-ai-biometric-claims)
- [Hunton: final COPPA Rule amendments](https://www.hunton.com/privacy-and-cybersecurity-law-blog/ftc-publishes-final-coppa-rule-amendments)
- [OpenAI Under-18 API guidance](https://developers.openai.com/api/docs/guides/safety-checks/under-18-api-guidance)
- [Gemini API Additional Terms](https://ai.google.dev/gemini-api/terms)
