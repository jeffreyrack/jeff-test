# Market Analyst review — Round 2 (2026-10-06)

_Evaluator: market-analyst. Dimension: **Market** (10 = proven demand, beatable competitors, room for a newcomer; 1 = no demand or saturated with free alternatives). All live checks were made on 2026-10-06 via the Apify Store API, the Atlassian Marketplace REST API and web search. Claims I could not check are marked (unverified)._

| ID | Idea | Score | Demand evidence (short) | # Competitors | Saturation | AI-commoditization risk |
|---|---|---|---|---|---|---|
| G1 | Keyword→Brief SEO Actor (Apify) | **4** | Verified: keyword-volume shelf has 720 + 396 + 267 users in 30 days. The "content brief" shelf is near zero (best brief Actor: 1 user). | ~20 direct keyword-volume Actors; 8+ already at or below $0.004 | High | High |
| G2 | LongForm Transcripts Actor (Apify) | **3** | Verified: memo23 has 158 users in 30 days but only 1,122 runs. Top podcast/audio transcribers have 68–135 users. The target of 49k paid minutes a month likely exceeds the shelf's paid volume. | 1,675 search hits; ~15 real audio transcribers, several at $0.003–0.008/min | High | High |
| G3 | AnswerShare AI-visibility API (MCPize/RapidAPI) | **2** | Weak: 125 Apify GEO Actors, the best has 17 users in 30 days. Paid demand sits in SaaS dashboards. | Hundreds+ (Otterly, Peec, Profound, Semrush, Ahrefs, MentionsAPI, 125 Actors) | Red ocean | High |
| C1 | FunderFit white-label funder reports | **5** | Freelance grant writers already pay for Instrumentl, Candid and academies. The white-label per-client deliverable is unserved. | ~10 direct tools (Instrumentl, Candid FDO, Grantable, Granted AI, OpenGrants, GrantStation, Apify 990 Actors) | High for tools; Low for white-label per-report | Medium-High |
| C2 | Client Safety Kit (white-label bilingual talks) | **4** | Indirect: consultants sell retainers and NRCA sells talk packs. No evidence yet that consultants pay for white-label packs. | ~30+ (NAWIC/CPWR free, HandsHQ free AI, ISN AI talks, SafetyCulture, Etsy packs) | High | High |
| C3 | Interpreter Practice Lab (medical, ES) | **3** | Real but tiny: about 1,000 CoreCHI takers a year, plus NBCMI and agency tests. The named partners already sell their own prep. | ~5–10 prep sellers; no AI-scored medical consecutive tool found | Low (AI scoring); Medium (prep) | Medium |
| I1 | Zì Bot (Mandarin Kotoba for Discord) | **4** | Gap verified: no Chinese quiz or dictionary bot on discordbotlist. Kotoba is in 50,297 servers but has no visible monetisation. Paid conversion is unproven. | ~0 Discord equivalents; dozens of paid apps (HelloChinese, SuperChinese, Du Chinese) | Low (bot) / High (AI practice) | High (for `/practice`) |
| I2 | Episode Study Packs for Chinese creators | **3** | Verified: about 6–8 creators sell Patreon transcript PDFs. The total pool is about 100–200 creators. | Few dedicated; the substitutes are ChatGPT and freelancers | Low supply, tiny market | High |
| I3 | Role-Play Room for Chinese classes | **3** | Instructors want assignable practice, but a free tool (Mizou) already serves L2 university classes. Chinese enrollment is falling. | ~10+ (Mizou free, SchoolAI, Brisk, Extempore, publisher drills) | Medium-High | High |
| M1 | ChatRelay for Jira (Google Chat, Forge) | **6** | Verified: 11,008 installs, 2.3★ from 109 reviews on Google's unmaintained Connect app. Forge alternatives total about 690 installs. A paid competitor exists. | 5 (Move Work Forward free, Canary paid, Jigo, ChatBridge, Automation Actions app) + Zapier/Pabbly | Low-Medium | Medium |
| M2 | SpecView for Confluence (Swagger + migration) | **4** | Verified: about 5,500 installs on stale Swagger macros. But 20 listings, including well-installed Forge/multi-macro apps, and 4+ fresh clones with 1–5 installs. | 20 listings on "swagger" | Medium-High | Medium-High |
| M3 | SheetSync (Apify → Google Sheets) | **5** | Verified: incumbent has 825 users in 30 days and 42,240 of 83,014 runs failed (51%). But two "reliable" clones already exist with 1–2 users each. | ~3 Actors + Console "Export → Sheets" + Coupler.io + Make/Zapier | Low supply, but a free incumbent | Medium |
| U4 | AI-matched job board | **2** | Demand is huge but captured: HiringCafe (2M MAU, 5.7M jobs) launched a **free** resume-matching AI agent on 2026-09-28. | Hundreds+ (HiringCafe, Jobright $39.99/mo, Teal $29/mo, Simplify, LoopCV, Google for Jobs, many niche boards) | Red ocean | High |

**Cross-cutting findings**
1. **On Apify, undercutting price is not a wedge.** On the keyword shelf, 8+ Actors priced at or below G1's planned $0.004 per keyword have 0–10 users each. On the transcription shelf, Actors at $0.0025–0.008/min have 2–13 users. The leaders win on ranking, history and reliability, not price. G1 and G2 both lean on "cheaper than the leader". The evidence says that does not work by itself.
2. **"Reliability" clones also fail to get found.** For M3's exact pitch, `lizaraco/google-sheets-import-export — Reliable Bridge` (1 user) and `srd836` (2 users) already exist. Store search ranking favours the incumbent. The integration picker and README cross-links matter more than the listing title.
3. **The Atlassian Connect deadline is softer than the ideators claim.** Atlassian says customers "won't lose access" to Connect apps after end of support. What ends is updates and non-critical fixes. The in-UI "might stop working soon" banner started 20 May 2026, and Atlassian later said it was meant for non-Marketplace apps. Urgency is real for apps that are *already broken* (M1). It is weaker for working macros (M2).
4. **Platform concentration.** 3 of 13 ideas use Apify (G1, G2, M3) on top of T2. 2 use Atlassian (M1, M2). 3 share the Mandarin market (I1–I3).

---

## G1 — Keyword→Brief (Apify Actor, PPE) — Market 4/10

**Demand (verified).** `aitorsm/keyword-volume` was created 2026-07-07. It has 720 users in 30 days, 7,061 runs with 0 failures, and charges $0.012–0.008 per keyword. `khadinakbar/dataforseo-keyword-research` has 396 users at $0.01. `steadyfetch/keyword-search-volume-scraper` has 267 users at $0.002–0.008. The ideator's numbers check out. Keyword *metrics* is a real, recurring, paid-per-call shelf.

**Competitors.** About 20 direct keyword-volume Actors. Critically, **at least 8 are already at or below the planned $0.004**, and every one is near zero:
- lizaraco: $0.0007–0.001, 0 users;
- curly: $0.0015, 1 user;
- s-r: $0.003, 5 users;
- jotowl: $0.003, 1 user;
- meridianlabs: $0.003, 5 users;
- khadinakbar's second Actor: $0.004, 10 users.

The ideator's planned entry price is therefore an *already-failed* positioning.

**The "Brief" event has no demand evidence.** On the SERP-brief / PAA shelf, `serp-content-brief-generator` ($0.05/brief) has 1 user, and the best PAA scraper has 23 users. The $0.04 brief, which was supposed to carry most of the revenue, sits on an empty shelf.

**Saturation:** High. Expect AI-operator clones of whatever ranks.
**AI-commoditization risk:** High. The supply side is AI-built, and DataForSEO ships its own MCP server.

**Market size.** About 1,400 monthly users across the top 3, but many are free-plan users. At about $3 net per paying user, $300 needs about 100 paying users. That is roughly the whole #2 Actor's user base.

**Wedge.** Don't fight on price. The best available angle is a **0%-failure, agent-native schema** sold through n8n templates, and a bundle the leader lacks (for example AI-search volume plus intent in one call). Even that is a follow-the-leader bet.

Sources: [aitorsm/keyword-volume](https://apify.com/aitorsm/keyword-volume) · [Store search "keyword search volume"](https://api.apify.com/v2/store?search=keyword%20search%20volume) · [Store search "content brief SERP PAA"](https://api.apify.com/v2/store?search=content%20brief%20SERP%20people%20also%20ask)

## G2 — LongForm Transcripts (Apify Actor) — Market 3/10

**Demand (verified, with a caveat).** `memo23/video-audio-transcriber` has 158 users in 30 days but only **1,122 runs in 30 days**. It now charges $0.0008/sec (≈ $0.048/min). `steadyfetch/media-transcriber` has 134–135 users and 883 runs, and has repriced three times, now $0.006/min (Oct). `amanatools/whisper-transcriber` has 68 users at $0.008/min plus $0.005 per file.

Run counts in the low thousands mean the shelf's *total* paid audio minutes are probably far below the 49k paid minutes a month G2 needs (unverified; minutes per run are not public). The large-volume Actors (`invideoiq`, 129 users; `tictechid`, 99 users) are **social-video** transcribers. G2 deliberately excludes that use case.

**Competitors.** A 1,675-hit search, with about 15 real audio/podcast transcribers. Cheaper entrants already exist and are not winning:
- `conserving_celerytop`: $0.0025/min, 2 users;
- `tidytools`: $0.006/min, 8 users;
- `sian.agency` podcast-to-text with show notes and SRT: 5 users.

The "chapters + quotes + RSS" differentiator is already listed, at 5 users.

**Saturation:** High.
**AI-commoditization risk:** High. ASR is a commodity at $0.0007/min (Groq), and ChatGPT transcribes uploads.

**Size check.** Reaching $300 needs about 35 heavy users at 23 h/month each. That is implausible on a shelf whose second-largest player logs about 900 runs a month.

**Wedge.** The only defensible angle is **scheduled RSS watch mode for podcast agencies**, which creates recurring minutes. But that is a template play, not a shelf-capture play.

Sources: [memo23 Actor](https://apify.com/memo23/video-audio-transcriber) · [steadyfetch Actor](https://apify.com/steadyfetch/media-transcriber) · [Store search "transcribe"](https://api.apify.com/v2/store?search=transcribe) · [Store search "podcast transcription"](https://api.apify.com/v2/store?search=podcast%20transcription)

## G3 — AnswerShare AI-visibility API — Market 2/10

**Demand.** Paid demand for GEO tracking is real, but it flows to SaaS dashboards: Otterly from $29/mo (API/MCP only at $189), Peec about $95, Profound $99, Semrush AI toolkit $99/domain, Ahrefs Brand Radar $199+, Scrunch $250, AthenaHQ $295.

The *pay-per-check API* sub-segment shows weak pull. Apify has **125 AI-visibility Actors, and the top one (`doesaiknow`, $0.18–0.30/query) has 17 users in 30 days**. Most of the rest have 0–11.

**Direct API competitor (verified).** MentionsAPI is MCP-native and pay-as-you-go: $0.02 cached or $0.39 fresh per check, with a $1 free credit. It covers ChatGPT, Claude, Gemini, Perplexity, AI Overviews, AI Mode and Copilot. It is listed on mcp.so, glama and enterprisedna. It covers more engines than G3 at a lower cached price.

**Saturation:** Red ocean.
**AI-commoditization risk:** High. This is a weekend build for any AI operator, as the 125 Actors show.

**Size check.** RapidAPI and MCPize publish no buyer volume for this category. I see no evidence that 24 subscribers at $29 would find an unknown seller there.

**Wedge.** None strong. The only defensible angle would be an **outreach-target export** ("domains cited for your prompt set", with contact discovery) sold to digital-PR agencies, which is closer to link-building than to tracking. Not recommended.

Sources: [AI visibility pricing 2026 (ud.hk)](https://www.ud.hk/en/insight/article/ai-visibility-tool-pricing-2026-09-03) · [ainora comparison](https://ainora.lt/blog/best-ai-visibility-tracking-tools-2026) · [MentionsAPI MCP (glama)](https://glama.ai/mcp/servers/mukul-dutt/mentionsapi-mcp) · [mcp.so listing](https://mcp.so/servers/mentionsapi-mcp) · [Apify search](https://api.apify.com/v2/store?search=AI%20visibility%20chatgpt%20brand)

## C1 — FunderFit — Market 5/10

**Demand.** Strong evidence that the buyer pays for funder research:
- Instrumentl costs $299+/mo and runs a partner programme with GPA trainers and podcasters;
- Candid FDO costs about $60–179/mo;
- the academies (FGWA, Learn Grant Writing) sell careers built on prospect research.

Freelancers bill clients for "prospect research", so a per-client deliverable has a resale logic.

**Competitors (verified, more than the ideator lists).** The low end is filling fast:
- **Grantable:** 990-based funder discovery from $0;
- **Granted AI:** $29/mo, discovery plus drafting;
- **OpenGrants:** free Explorer, $49 paid;
- **GrantStation;**
- **grantmakers.io:** free;
- Apify 990-PF Actors. The cited `immense_greenery/foundation-grant-prospector` now returns 404.

Total: about 10 direct tools, plus AI writing suites that are adding discovery.

**Saturation:** High for "cheap funder search". Low for a **white-label, client-ready PDF priced per report**. None of the competitors I found sells that form.
**AI-commoditization risk:** Medium-High. 990 data plus an LLM is easy to replicate, and Grantable already does it for free. The defence is format plus channel.

**Size check.** A few thousand active freelance grant writers in the US (unverified; GPA has several thousand members). 15 affiliate-referred reports a month is a small share, *if* partners promote. Q4 timing is favourable.

**Wedge.** The **white-label "prospect report you can invoice"** sold *through* the academies, not as a search tool. The risk is that partners already earn affiliate income from Instrumentl.

Sources: [Grantable Instrumentl alternatives](https://grantable.co/best-instrumentl-alternatives) · [GrantSights alternatives 2026](https://grantsights.com/blog/instrumentl-alternatives-2026) · [Granted AI vs Instrumentl](https://grantedai.com/compare/instrumentl) · [Instrumentl partners](https://instrumentl.com/partners)

## C2 — Client Safety Kit — Market 4/10

**Demand.** The underlying need for weekly toolbox talks in English and Spanish is real. GCs and insurers require them, and paid packs exist: NRCA sells at $95–195, and Etsy sells "52 bilingual toolbox talks" PDFs. The *specific* buyer, an independent safety consultant paying a monthly white-label licence, has **no observed demand signal**. I found no existing white-label subscription and no forum or podcast threads asking for one. That absence cuts both ways: no competitor, but also no proof.

**Competitors / substitutes:**
- NAWIC free bilingual PDFs;
- CPWR free talks;
- HandsHQ free AI generator ("any language, no account");
- ISN's AI Toolbox Talks (EN/ES/FR, award-winning, bundled for contractors);
- SafetyCulture;
- toolboxtalk-ai at $49/mo (unverified);
- Etsy packs.

About 30+ in total.

**Saturation:** High for talks. Low for the "OSHA cited your industry last month" brief, which depends on D2's ingest.
**AI-commoditization risk:** High. Free AI generators already produce bilingual talks on demand.

**Size check.** There are thousands of independent OSH consultants in the US (unverified). 7–12 paying consultants is achievable only if a partner channel converts. Audience sizes for Sheldon Primus and the ASSP practice specialty are unverified.

**Wedge.** The **NAICS-and-state citation brief** is the only non-commodity element. It works best as a **D2 upsell**, not a standalone product. Without D2 it is a generic white-label talk pack in a free-content category.

Sources: [HandsHQ toolbox talks](https://handshq.com/resources/toolbox-talks) · [ISN AI toolbox talks](https://www.businesswire.com/news/home/20250508221766/en/ISN-Honored-with-Multiple-Gold-Stevie-Awards-for-AI-Powered-Innovation) · [NAWIC free bilingual talks](https://nawic.org/safety-toolbox-talks/) · [Etsy bilingual pack](https://www.etsy.com/listing/4536964410)

## C3 — Interpreter Practice Lab — Market 3/10

**Demand.** The candidates pay real money: $485 in exam fees and $300–700 for courses. Prep products sell:
- InterpreMed's "Mini-Sprint" oral-exam prep (15 days, 23 exercises);
- MITS's "Consecutive Interpreting Prep" add-on;
- open-exam-prep study guides.

**But the pool is small.** About 1,000 CoreCHI takers a year (CCHI report, per the ideator), with NBCMI of a similar order. Agency-test candidates are a larger pool but unreachable through these channels.

**Competitors.** No AI-*scored* medical consecutive practice tool surfaced in search. The AI-interpreting startups (No Barrier, Opalite Health YC W26, Boostlingo AI) replace interpreters rather than train them. Conference-interpreting trainers exist: Inter Practice, TerpWise, Interpretrain (per the ideator).

**Channel conflict.** Two of the named "partners" (InterpreMed, MITS) **already sell oral-exam prep**, so they are competitors as much as channels.

**Saturation:** Low for AI scoring, Medium for prep.
**AI-commoditization risk:** Medium. ChatGPT voice can role-play, but rubric-consistent scoring against a key is harder.

**Size check.** 22 affiliate passes a month is about 25% of all monthly CCHI oral candidates. That is not plausible. It works only through school licences (2 at $150).

**Wedge.** A **B2B licence to 40-hour training schools** as an embedded practice module, with the scoring calibration as the product. AI-replacement of medical interpreters is also a long-term headwind for the whole candidate pool.

Sources: [InterpreMed oral-exam prep](https://interpremed.com/blog-post/mini-sprint-practice-for-the-nbcmi-cchi-oral-exams-or-skills-assessment/) · [MITS consecutive prep](https://medicalinterpretingtrainingschool.com/consecutive-exam-practice/) · [No Barrier funding](https://slator.com/ai-interpreting-startup-no-barrier-raises-2-7m/) · [Opalite Health](https://yespress.io/opalite-health-yc-w26.md)

## I1 — Zì Bot — Market 4/10

**The gap is verified.** A discordbotlist search for "chinese" returns translators, music bots and a Simplified↔Traditional converter. It has **no Chinese learning, quiz or dictionary bot**. Web search found only Studybot (generic custom quizzes) and LanguageInfoBot. top.gg blocked the fetch (403). Kotoba, the Japanese analogue, is in **50,297 servers** and shows **no monetisation**. The free-bot demand model is proven. The paid one is not.

**Demand for paid AI practice** exists, but it goes to apps:
- HelloChinese / SuperChinese at about $11.99/mo;
- Du Chinese;
- Pleco add-ons;
- ChatGPT Go at $8.

Discord users are price-averse, and a 1.5–2% conversion to $4.99 is optimistic (unverified). Break-even needs about 85–100 paying seats, which means about 5–6k MAU. For a niche bot that is months of server accumulation.

**Competitors:** about 0 Discord equivalents; dozens of paid apps; free chatbots.
**Saturation:** Low for the bot, High for "AI conversation practice".
**AI-commoditization risk:** High for `/practice`, because ChatGPT will role-play at a stated HSK level for free. Low for the social quiz layer.

**Size check.** Chinese-learning Discord servers are listed at 6.5k–77k members (per the ideator). Reach exists, but the monetisable fraction is unproven.

**Wedge.** Be the **default quiz and dictionary bot in the top 5 servers** before January and Chinese New Year. Monetise Server Pro (custom class decks) for teachers who run servers, which is a more natural payer than individual learners. Expect $300/mo to be a 9–15-month target, as the ideator concedes.

Sources: [Kotoba on discordbotlist](https://discordbotlist.com/bots/kotoba) · [discordbotlist "chinese" search](https://discordbotlist.com/search?q=chinese)

## I2 — Episode Study Packs — Market 3/10

**Demand (verified).** These creators already gate transcript PDFs behind Patreon or donations, which proves *their* audience pays and the PDF is a conversion asset:
- Grace Mandarin Chinese (transcripts and vocab lists, 130+ mini podcasts);
- Chinese Around You (PDFs with pinyin, hanzi, English and grammar notes);
- 中文花園 Chinese Garden (PDF with homework);
- Learning Chinese Through Stories (annotated transcripts for patrons);
- 7 Minute Chinese;
- Mandarin with Gisele;
- Mandarin Corner (per the ideator).

**But every example already produces its PDFs in-house**, often as native-speaker teachers. Their stated pain, 2–3 hours per episode, is the ideator's inference, not something the creators have said (unverified).

**Competitors.** No dedicated "study pack as a service" was found. The substitutes are ChatGPT plus a template, Fiverr transcription/translation freelancers, and the creators' own assistants.

**Saturation:** Low supply, but the market is tiny: about 100–200 relevant creators worldwide, and maybe 30–60 who publish weekly and monetise.
**AI-commoditization risk:** High. The core transformation (transcript → pinyin + translation + vocab) is exactly what a chatbot does. Polyphone-correct pinyin and Anki/Pleco exports are conveniences.

**Size check.** 9 Studio creators means 5–10% of the reachable pool converting. That is possible but fragile: losing 2 clients breaks even.

**Wedge.** **HSK 3.0 band tagging plus Pleco/Anki exports as a weekly pipeline** for the 20–40 creators who publish weekly. Positioned as "launch a patron tier" for creators who *don't yet* sell PDFs. Those creators have the larger unmet need.

Sources: [Grace Mandarin Patreon](https://www.patreon.com/12905618/join) · [Learning Chinese Through Stories](https://www.alllanguageresources.com/learning-chinese-through-stories/) · [Chinese Garden](https://castbox.fm/channel/6661088) · [7 Minute Chinese](https://rephonic.com/podcasts/7-minute-chinese-zhong-wen-qi-fen-zhong) · [Hacking Chinese Patreon](https://www.hackingchinese.com/hacking-chinese-patreon-support-get-awesome-rewards/)

## I3 — Role-Play Room — Market 3/10

**Demand.** Language teachers do want assignable AI conversation practice. But the evidence shows it being met by **free** general-purpose classroom AI platforms. **Mizou** is free: teachers create chatbots with a persona, instructions and uploaded worksheets, and students join via link, by text or voice. FLTMag (March 2026) documents its use in an **Italian L2 university class** to drill past tenses, which is I3's exact use case. Other substitutes:
- SchoolAI and Brisk (free teacher tiers, unverified details);
- Extempore (paid oral-assessment platform for world-language classes; unverified current pricing);
- textbook-publisher drills (Integrated Chinese companion products).

**Market size is shrinking.** US postsecondary Chinese enrollment fell 14.3% from 2016 to 2021 (MLA). Instructors buy per semester, so the next window after November is July–August 2027.

**Saturation:** Medium-High. The category is generic "AI chatbot assignment"; the Chinese-specific level-lock is a feature.
**AI-commoditization risk:** High. Mizou and its peers can be prompted with "use only these words" for free.

**Size check.** 6–11 paying classes at $149/semester is small. But a *paid* product has to beat a free tool that departments already approve, and that is hard.

**Wedge.** **Chinese-specific correctness:** hanzi/pinyin-aware corrections, measure-word and tone feedback, and a class error heatmap mapped to textbook chapters (Integrated Chinese lesson presets). These are things a generic chatbot builder can't do. Price per *student seat as required course material* only.

Sources: [FLTMag on Mizou in L2 classes](https://fltmag.com/chatbots-collaboration-mizou/) · [ECML Mizou entry](https://www.ecml.at/en/Resources/ICT-tools/InventoryID/357) · [MLA enrollment trend](https://pinyin.info/news/2023/us-postsecondary-enrollments-in-chinese-trending-down/)

## M1 — ChatRelay for Jira — Market 6/10 (highest this round)

**Gap evidence (verified).** The Atlassian Marketplace API confirms "Google Chat for Jira Cloud" (Google LLC, `linovi-hangoutschat-bot`) at **11,008 installs and 2.3★ from 109 reviews**. The listing was last modified 2025-12-11; I did not check the 2021 release date.

Forge alternatives:
- Advanced Google Chat for Jira (Move Work Forward): 407 installs, 5.0★, **free**;
- Jigo: 137;
- Canary Apps "Google Chat for Jira": 123, paid via Atlassian; the $5/mo 10-user tier is confirmed by the pricing API;
- ChatBridge: 16;
- "Google Chat Automation Actions for Jira" (v2.2.0, Nov 2025; install count unknown).

Total: about 690 or more. **Jira Automation has no native Google Chat action** (verified by search), so a gap exists. Zapier, Pabbly, Tray and Latenode are paid substitutes.

**Caveats that lower the score:**
1. "Installs" includes dormant sites. Active, Google-Workspace-using installs could be a fraction (unverified).
2. **Google's app is free.** These buyers have never paid for this function, and a free 5.0★ Forge rival exists.
3. **Connect apps do not stop working on 31 Jan 2027.** Atlassian says customers "won't lose access". The "might stop working soon" banner started 20 May 2026 and was reportedly meant for non-Marketplace apps. The real push is that the app is *already broken*, per the 1★ reviews.

**Saturation:** Low-Medium. Only 5 Forge entrants have about 6% of the base.
**AI-commoditization risk:** Medium. Clone vendors like Apps+ ship Forge copies weekly, but reviews and first-mover ranking matter on Atlassian.

**Size check.** 12 paying sites from an 11k orphan base is about 0.1%. That is plausible even if 80% of installs are dead.

**Wedge.** The **migration guide, per-JQL routing and threading** for mid-size sites (more than 10 users), where the free rival's price is not the issue, positioned as "Runs on Atlassian". This is the cleanest demand evidence in the round. The cash timing ($500 payout threshold) is the weakness, not the market.

Sources: [Atlassian addon API: Google Chat for Jira Cloud](https://marketplace.atlassian.com/rest/2/addons/linovi-hangoutschat-bot) · [Search "google chat"](https://marketplace.atlassian.com/rest/2/addons?text=google%20chat&application=jira&hosting=cloud) · [Connect EoS blog](https://www.atlassian.com/blog/developer/announcing-connect-end-of-support-timeline-and-next-steps) · [EoS extended to 31 Jan 2027](https://community.developer.atlassian.com/t/connect-end-of-support-extended-to-january-31-2027/102002) · [Banner thread](https://community.developer.atlassian.com/t/new-this-app-might-stop-working-soon-banner-in-all-our-uis/100817) · [Automation Actions app](https://marketplace.atlassian.com/apps/1252695580/google-chat-automation-actions-for-jira)

## M2 — SpecView for Confluence — Market 4/10

**Gap evidence (verified).** The four stale Connect Swagger apps match the ideator's numbers: Toshihiro Sato 2,873, Dutch Beginners 1,218, Tech Labs 657, EliteSoft 601. About 5,350 installs, plus SwaggerHub at 153.

**But the shelf is crowded.** The "swagger" Confluence Cloud search returns **20 listings**, including:
- Just Add+ (Modus Create): 8,135 installs; embeds markdown, diagrams and code; Swagger support not verified;
- Warsaw Dynamics multi-macro: 3,186;
- O'Hara "Open API Documentation": 1,800;
- Narva: 387;
- Apps+ "Swagger UI+": 201;
- **four brand-new clones with 1–5 installs** (NGPILOT, SpecDock, Alidade, Get Report).

The clone flood is already here and getting nothing. That shows a plain viewer cannot win.

**Weak urgency.** Unlike M1's orphan, these macros *work*: 4.3–4.6★, and Atlassian says Connect apps keep running. Atlassian also says over 95% of paid seats have migrated (per the ideator).

**Saturation:** Medium-High.
**AI-commoditization risk:** Medium-High for the viewer. Low for the page converter.

**Size check.** At about $10–15 per site, 20 paying sites is about 0.4% of the orphan base. That is arithmetically plausible, but switching demand is mostly latent until something breaks.

**Wedge.** The **migration scan/converter is the only differentiated asset**. Better still, sell it as a *feature inside a broader Forge diagram/macro migrator* covering Swagger + Mermaid + PlantUML (the same vendor's stale apps). Treat it as M1's phase-2 listing, not a standalone pick.

Sources: [Atlassian search "swagger" (Confluence Cloud)](https://marketplace.atlassian.com/rest/2/addons?text=swagger&application=confluence&hosting=cloud) · [Connect EoS blog](https://www.atlassian.com/blog/developer/announcing-connect-end-of-support-timeline-and-next-steps)

## M3 — SheetSync — Market 5/10

**Gap evidence (verified exactly).** `lukaskrivka/google-sheets` has:
- 4,891 total users;
- **825 in the last 30 days and 625 in the last 7**;
- 83,014 runs in 30 days, with **42,240 FAILED, 40,708 succeeded**;
- 4.81★ from 7 reviews, 88 bookmarks;
- last modified 2026-07-29.

Next-best Sheets writers: `srd836` (2 users) and **`lizaraco` "Google Sheets Import & Export — Reliable Bridge" (1 user)**. The reliability-positioned clone already exists and has not been found.

**Caveats:**
1. A 51% run-failure rate may be concentrated in a few high-frequency scheduled integrations with stale OAuth tokens, not spread across 825 users. The rating is still 4.8★ (unverified distribution).
2. The incumbent is **free** and maintained by Apify staff. One fix removes the pain.
3. The substitutes include Console **"Export → Google Sheets"** (native, per Apify docs), the native "Upload results to GDrive" integration, **Coupler.io's** Apify→Sheets connector (SaaS with a free tier), and Make/Zapier.
4. Only paid-plan users generate payout, and the buyers are used to paying $0.

**Saturation:** Low in supply, but a free incumbent dominates ranking.
**AI-commoditization risk:** Medium. Clones are trivial to build, as shown, but they fail on discovery.

**Size check.** 45 paying users is about 5% of monthly users. That is plausible only if switchers find it, and the lizaraco precedent says Store search alone won't deliver them.

**Wedge.** Distribution *inside* the workflow: **integration-ready listing plus README templates for the top 10 scrapers**, and upsert/dedupe-by-key (incumbent feature parity unverified). Charging at $0.40 per 1k rows against a free incumbent is the test, so the demand test should measure paid-plan users specifically.

Sources: [lukaskrivka/google-sheets](https://apify.com/lukaskrivka/google-sheets) · [Store search "google sheets"](https://api.apify.com/v2/store?search=google%20sheets) · [Coupler.io Apify→Sheets](https://www.coupler.io/google-sheets-integrations/apify-dataset-to-google-sheets) · [Apify Sheets integration notes](https://use-apify.com/docs/apify-for-developers/apify-google-sheets-integration)

## U4 — AI-matched job board — Market 2/10

**Demand.** Enormous, and already captured by well-funded free products:
- **HiringCafe** (TNW, **28 Sept 2026**) raised $6.8M pre-seed. It indexes **5.7M active listings** pulled from company ATS feeds, has **2M MAU**, and just launched a **100% free "AI Talent Agent"**. That agent parses an uploaded resume, recommends matching roles, monitors continuously for new matches and filters ghost jobs. **This is U4's exact core feature, free, at scale, launched eight days ago.**
- **Jobright.ai:** matching plus Turbo at $39.99/mo (raised from $29.99).
- **Teal+:** $29/mo or $9/week.
- **Simplify:** free autofill/copilot extension with a paid tier (unverified current price).
- LoopCV, Google for Jobs, Indeed and LinkedIn matching.

**Niche-board economics (indie data).** Posts sell for $99–299, up to $400–500 in specialised niches. Successes are slow:
- €700 MRR after a year for an Irish accountants board;
- $92 in the first month for two boards;
- the outlier Japan Dev at $62k/mo after years.

Boards cite about 2,500–6,000 monthly visits for small revenue, and meaningful revenue took about a year. Employer revenue needs traffic that a new domain won't have for 3–6 months (lesson 2).

**Saturation:** Red ocean for general resume-matching. Medium for single-niche boards.
**AI-commoditization risk:** High. Matching is a free feature of incumbents.

**Size check.** Charging seekers $9–19/mo competes with free HiringCafe and with Jobright/Teal at known brands. Employer posts need audience first, so the path to 10–60 paying customers a month runs past 90 days.

**Wedge.** Only an **ultra-niche board where the operator owns a data advantage**, not general matching. Examples: one profession whose roles sit on government/ATS feeds that HiringCafe under-indexes, or one licensed trade with credential-level matching. Even then, expect 6–12 months to $300/mo. Not a fit for the autonomous-$300 goal as proposed.

Sources: [TNW: HiringCafe $6.8M + free AI Talent Agent](https://thenextweb.com/news/hiringcafe-6-8m-pre-seed-ai-talent-agent) · [Pulse 2.0 on HiringCafe](https://pulse2.com/hiringcafe-raises-6-8-million-pre-seed-and-launches-free-ai-talent-agent-for-job-seekers/) · [Jobright review 2026](https://resumehog.com/blog/posts/jobright-ai-review-2026-is-this-job-search-copilot-worth-it.html) · [Teal pricing](https://toolradar.com/tools/teal-hq/pricing) · [IH: niche job board $62k/mo](https://www.indiehackers.com/post/how-this-ultra-niche-job-board-makes-62k-mo-175387d0af) · [IH: two boards, $92 first month](https://www.indiehackers.com/post/i-launched-two-job-boards-and-earned-92-50-in-my-first-month-of-charging-fully-automated-9105160b52) · [IH: first sale non-clinical board](https://www.indiehackers.com/post/first-sale-on-our-non-clinical-jobs-board-d8e1f13ec4)
