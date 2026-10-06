# Legal Risk Analyst review: user ideas U1 and U2 (2026-10-06)

> This is a risk screen, **not legal advice**. The human sponsor carries the risk and should consult a lawyer before relying on it.

| ID | Idea | Legal safety score | Overall risk (Low/Med/High) | Top risk | Key mitigation |
|---|---|---|---|---|---|
| U1 | OSRS GE flip advisor | 6/10 (game-IP and data-licence dependency, but strong paid precedent) | Med | Licensor or platform action: the OSRS Wiki prices API sits under a CC BY-NC-SA site licence, and Jagex's Fan Content Policy bars commercial gain from Jagex Property without permission. Either could end a paid tier. | Get a written OK from the wiki team before charging. Sell the analytics software only: no Jagex art, sprites or logos, no "RuneScape" in the brand or domain, and carry the required "not endorsed by Jagex" notice. Keep trades manual, with no input automation. |
| U2 | Mandarin personalised graded reader | 7/10 (ordinary subscription risk plus avoidable content-licence issues) | Low (Med if it does news rewrites) | Copyright in **news rewrites**: simplifying specific articles creates derivative works and a paid archive of them | Write original stories. Use CC-CEDICT under its CC BY-SA terms, with attribution, as a separate dataset. Use browser or paid-tier TTS. Label content as AI-generated. Comply with auto-renewal law. |

Neither idea triggers the hard gate (legal safety ≤ 3).

---

## U1: OSRS Grand Exchange flip advisor

The real exposure is **action by a licensor or platform, not a lawsuit**.

- **Jagex IP and commercial use.** Likelihood Low–Med × severity Med. The Fan Content Policy (updated 30 Jun 2025) says "generally" you cannot use Jagex Property for commercial gain without asking, and it says nothing about fansites or tools. GE Tracker has run a paid premium tier (about £2/month) for years without visible enforcement, so Jagex tolerates this in practice, but that is not a licence. *Mitigation:*
  - Use no item sprites, game art or Jagex logos in the product.
  - Use "for OSRS" only descriptively, never as the brand or domain.
  - Show the required "not endorsed by or affiliated with Jagex" notice.
  - If revenue becomes material, ask Jagex for permission.
- **OSRS Wiki real-time prices API.** Likelihood Med × severity High, because this is the only data source.
  - The acceptable-use paragraph is permissive ("build cool projects and tools").
  - However, the site licence is CC BY-NC-SA 3.0, and the page does not resolve whether the "NC" (non-commercial) term applies to a paid tier.
  - Prices are facts. But `/mapping` carries wiki and Jagex text, and the host (Weird Gloop) is in the UK, where database rights exist.
  - The realistic outcome is a blocked User-Agent or a request to stop.
  - *Mitigation:*
    - Email the wiki team for written approval before charging.
    - Use a descriptive User-Agent with contact details, bulk endpoints and caching, and attribute the wiki.
    - Do not resell the raw feed or the examine text.
- **Rules of RuneScape: account bans and RWT.** Likelihood Low × severity Med.
  - Manual trades by a human are fine. The AI operator must never log in or place trades, because that counts as macroing plus account sharing.
  - Any RuneLite plugin must be display-only and go through Plugin Hub review. It must not auto-fill offers or generate input.
  - Selling software is not RWT. Never accept or sell gp. Never offer "we flip for you": RWT includes paying someone to play your account. Never take gold-seller sponsorships.
- **Deceptive claims.** Likelihood Med × severity Med. The backtest shows a naive strategy loses money, so "X M gp/hr" claims would be unsubstantiated (FTC Act §5). Never frame results as real-money earnings: that clashes with the merchant of record's "get-rich-quick" ban and looks like RWT.
- **Subscriptions and minors.** Likelihood Med × severity Low.
  - The audience includes many teens. Do not allow under-13 accounts (COPPA), and require parental consent for 13–17s.
  - Comply with ROSCA and state auto-renewal laws (California's amended ARL took effect 1 Jul 2025). The FTC is redoing its negative-option rule (advance notice published March 2026).
  - Use a merchant of record to handle VAT and EU withdrawal rights.

## U2: Mandarin personalised graded reader

- **News rewrites.** Likelihood Med × severity Med. Simplifying a specific article creates a derivative work. Facts are free to use, but the expression is not, and a paid public archive adds to the exposure. *Mitigation:*
  - Write original stories instead.
  - If you cover news, combine facts from several sources, avoid close paraphrase, and link to the sources.
  - Alternatively, use permissive sources: Chinese Wikipedia (CC BY-SA, share-alike applies) or original US-government VOA content, excluding wire copy.
- **Dictionary data.** Likelihood Low × severity Low–Med.
  - CC-CEDICT is CC BY-SA 3.0. Commercial use is fine with attribution. Any modified version you distribute must stay CC BY-SA, so keep it as a separate dataset.
  - Do not scrape Pleco, MDBG or other commercial dictionaries.
  - For a character-writing wedge, check the Make Me a Hanzi data licences (Arphic/LGPL).
- **HSK word lists and the HSK name.** Likelihood Low × severity Low.
  - Word lists are factual compilations and are widely reused.
  - The test is run by Chinese Testing International (CTI), which has official partners. Say "HSK 3 vocabulary" descriptively. Never claim "official", never use HSK logos, and never copy real exam or mock papers.
- **TTS licensing.** Likelihood Low × severity Med.
  - The browser Web Speech API runs on the user's device and is the cleanest option.
  - Paid tiers of Azure, Google and OpenAI TTS permit commercial use of the output. Microsoft says free-credit resources are not for commercial use. OpenAI requires disclosure that the voice is AI.
  - Avoid the unofficial "edge-tts" endpoint and any audio ripped from textbooks or shared decks.
- **AI transparency and quality claims.** Likelihood Med × severity Low–Med.
  - Article 50 of the EU AI Act has applied since 2 Aug 2026. It requires disclosure of AI-generated text on public-interest topics (which covers news rewrites) and marking of synthetic audio.
  - Label content "AI-generated, not native-reviewed". This also prevents deceptive claims about quality.
- **Subscriptions, privacy and email.** Likelihood Med × severity Low–Med.
  - Comply with auto-renewal law and ROSCA, and send renewal reminders for annual plans. The merchant of record handles EU withdrawal rights.
  - Known-word lists and email addresses are personal data. Publish a privacy policy, use GDPR double opt-in for EU marketing emails, and include a CAN-SPAM footer.
  - Do not allow under-13 users.
  - Share only your own content as AnkiWeb decks, and attribute CC-CEDICT.

**Lowest-risk wedge:** original stories personalised to each learner's word list, with CC-CEDICT glosses and browser TTS. Skip news rewrites and exam-mock content.

---

### Sources
- [Jagex Fan Content Policy](https://legal.jagex.com/docs/policies/fan-content-policy)
- [Rules of RuneScape](https://legal.jagex.com/docs/rules/rules-of-runescape)
- [Jagex macro and client features not permitted](https://legal.jagex.com/docs/rules/macro-and-client-features-not-permitted)
- [OSRS Wiki Real-time Prices API](https://oldschool.runescape.wiki/w/RuneScape:Real-time_Prices)
- [GE Tracker pricing](https://www.ge-tracker.com/pricing)
- [Lemon Squeezy prohibited products](https://docs.lemonsqueezy.com/help/getting-started/prohibited-products)
- [CC-CEDICT](https://cc-cedict.org/wiki/)
- [Wo Hui Mandarin / CTI partnership](https://www.eimglobal.com/news/wo-hui-mandarin-partners-with-cti-to-bring-in-app-hsk-courses)
- [Azure TTS commercial use (Microsoft Q&A)](https://learn.microsoft.com/en-us/answers/questions/1192398/can-i-use-azure-text-to-speech-for-commercial-usag)
- [OpenAI usage policies](https://openai.com/policies/usage-policies/)
- [Goodwin: EU AI Act transparency obligations in force (Aug 2026)](https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force)
- [Mondaq: FTC revives click-to-cancel rule](https://www.mondaq.com/unitedstates/advertising-marketing-branding/1748974/ftc-revives-click-to-cancel-rule-a-fast-vast-update)
