# Founder-fit ideas — The Insider

_Persona: ideator-insider. Date: 2026-10-06. Inputs: the sponsor profile given by the orchestrator only (no employer, no private facts inferred), `operator-constraints.md`, `idea-brief.md`, `lessons-learned.md` (binding), and `runs/2026-10-06-eval-user-ideas/VERDICT.md`._

## Asset inventory and what I did with each

| Sponsor asset | Used as a product? | Why |
|---|---|---|
| **Mandarin learner who has built AI-led lessons and AI conversation practice** (private repo) | **Yes: I1, I2, I3** | This is the asset that faces a market with paying strangers, and the sponsor can dogfood it daily. Each idea reaches a **different buyer through a different channel**: learners in Discord, Chinese-teaching creators, and college/adult-class instructors. |
| **Claude Code / multi-agent pipeline builder** | **As the operator, not as a product** | It is why all three ideas can run at about 0.25–0.5 h/week. As a standalone product it is saturated with free tools. Apify Store "market research / idea validator" Actors have **0–3 monthly users** each. Free "validate idea" skills fill the Claude plugin directories. Paid skill marketplaces (Capafy, Agent37, SkillPie) have no public traction data. Polsia sells "AI runs your company" at $49/mo, and its top earner makes about $50/mo. claude.ai toolbox extensions (AI Toolbox 40k users, Claude Toolbox) and agent cost monitors already exist. |
| **OSRS / RuneLite / Wiki prices API** | **No** | Jagex's Fan Content Policy §6.1.1 bars creating content using Jagex property "for commercial gain". The Wiki price data is CC BY-NC-SA. The niche's tools are free by norm: WOM, Hawks OSRSbot, Trackscape and Evently already auto-verify bingo tiles. U1's fatal flaw (no lawful path from gp to USD) is not fixable inside OSRS. |

**Correlation warning for the committee:** all three ideas sell into the Mandarin-learning market. They share demand risk, but they do **not** share a channel or a seller account. All three also deliberately avoid the pending HSK 3.0 mock-exam wedge (U3-W) and the general AI tutor (U3).

---

## I1 — Zì Bot: the missing "Kotoba for Mandarin" quiz and practice bot for Chinese-learning Discord servers

- **Persona:** The Insider
- **One-liner:** A Discord app for Chinese-learning servers and individual learners. It is free for the group features: HSK 3.0-tagged dictionary lookups, channel quiz races with leaderboards and a daily word. Learners pay a small subscription for capped, text-only AI conversation practice and personal spaced-repetition (SRS) reviews by DM. It fixes U3's fatal flaws of distribution, inference cost and price ceiling.
- **Founder-fit asset used:** The sponsor's AI conversation-practice and AI-lesson code becomes `/practice`, and the sponsor uses the bot as a daily learner, which acts as quality control. Building a multi-agent operator means the bot's support, content and listings can run without the sponsor.
- **Demand test:** Ship only the free quiz and dictionary core (about 5 days). It includes a `/supporter` command offering **"Founding Supporter: AI practice + personal SRS, $29 for the first year, delivered by 15 Dec 2026, automatic refund if not delivered"** through a Lemon Squeezy checkout. **Pass:** ≥ 10 founding pre-orders, plus ≥ 15 servers or ≥ 300 weekly active users, within 30 days of the first community post. **Pivot zone:** 3–9 pre-orders; keep the free bot and test Server Pro instead. **Fail:** < 3 pre-orders; stop and refund.
- **Customer:** Adult self-study Mandarin learners at roughly HSK 1–5 who already hang out in Chinese-learning Discord servers. Examples: 中英交流 Chinese-English Language Exchange (listed at 25k–77k members), the r/ChineseLanguage server (~30k), Learn Mandarin 学中文 (~6.5k), Refold 汉语 ZH (~7.3k) and Chinese Plus. They already pay for HelloChinese or SuperChinese ($11.99/mo), Du Chinese and Pleco add-ons. The second buyer is **server admins**, who want engagement tools.
- **Problem / desire:** "Our server has HSK-level channels but nothing to *do* in them." "I want to practise writing Chinese every day without a tutor, at my level, without ChatGPT throwing HSK 6 words at me." Japanese learners have Kotoba, a quiz, dictionary and leaderboard bot that is a staple of Japanese servers. **I found no widely adopted Mandarin equivalent** on top.gg or discordbotlist, or in a review of the major Chinese servers (none mentions a quiz bot). The only results were a Taishanese dictionary bot and hobby projects.
- **Offering:** A Discord app that can be installed on a server *and* by an individual user, so it works in DMs and in any server that allows external apps.
  - **Free:** `/zi` dictionary (CC-CEDICT, pinyin, HSK 3.0 level tag, TTS audio); `/quiz` channel races (reading, meaning, tone, measure word, by HSK 3.0 band) with weekly leaderboards; an optional daily word.
  - **Supporter, per user:** `/practice` text role-play at a chosen HSK 3.0 level. The AI partner keeps to the level, corrects each message, and logs errors into personal SRS DM reviews. Capped at 40 AI turns/day.
  - **Server Pro, per server:** custom quiz decks (for example, a class word list), level roles and scheduled study events.
- **Price & revenue model:** Supporter **$4.99/mo or $39/yr**. Server Pro **$7.99/mo**.
  - **Billing:** Lemon Squeezy (merchant of record) until the app is verified. Then the same SKUs are added to Discord Premium Apps at the same price, as Discord's developer policy requires for paid features. Discord keeps about 30%, according to developer reports.
  - **Break-even:** About 85–100 paying seats net $300/mo after fees and inference. At 1.5–2% conversion that means about 5–6k monthly active users.

- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Domain for ToS/privacy pages and a support inbox (Cloudflare Email Routing, free) | $12 |
| Cloudflare Workers + D1 hosting (HTTP interactions endpoint, no gateway server), free tier | $0 |
| Pre-generated TTS audio for about 11k HSK 3.0 headwords, within a cloud TTS free tier | $0 |
| top.gg and discordbotlist listings | $0 |
| **Total** | **$12** |

### Monthly running costs (excluding operator tokens)
- **Hosting:** $0 on the Workers/D1 free tier, up to roughly 100k requests/day.
- **Inference (Supporters only):** text-only with a small model, capped at 40 turns/day. From the repo's own U3 model, text-only use costs $0.16–$1.58 per active user per month at 5–30 min/day, so plan for about $0.60 per Supporter. Free users get no LLM calls; dictionary and quiz lookups are table lookups.
- **Fees:**
  - Lemon Squeezy: 5% + $0.50 per transaction.
  - Discord Premium Apps: about 30% of anything sold through Discord after verification.
- **Domain:** $1/mo amortised.
- **At 100 Supporters:** about $60 inference + about $75 fees.

### Customer acquisition plan
1. The free bot spreads **inside servers**: every quiz race is public, and each result card shows "Add Zì to your server / your account".
2. Personal installs let any member bring the bot along without asking an admin.
3. Learners who use `/quiz` daily see `/practice` locked after 3 free trial turns per week, which leads to the upgrade.
4. Server admins who adopt the bot are offered Server Pro for class or custom decks.
5. Once the bot reaches 76+ servers:
   - the sponsor completes Discord's identity verification;
   - the app goes into the Discord App Directory, which has search plus native billing;
   - Premium App SKUs are added.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Admins of named Chinese-learning servers.** The sponsor, as a genuine learner and the declared maker, asks the admins of 5–6 servers (listed above) for permission to add the bot or post once in #resources. Why it works with zero audience: one admin approval exposes 6k–77k members, and a quiz bot gives the server activity rather than asking for something. **Speed:** days 10–25.
2. **top.gg / discordbotlist / discord.bots.gg listings** under "language learning", "chinese" and "study". These are free directories with search, and the "Chinese" and "Mandarin" tags have no strong incumbent. **Speed:** listed within about 1 week, and installs trickle in from week 2.
3. **One honest show-and-tell post by the sponsor** on r/ChineseLanguage (e.g. in a resources thread, within subreddit rules), framed as "I built a Kotoba-style bot for Chinese, free; feedback wanted". **Speed:** a one-off spike in weeks 2–4.
4. **Seasonality tailwind:** language-learning signups peak in January (New Year resolutions) and around Chinese New Year (17 Feb 2027). An October launch gives 10–12 weeks to collect servers before the peak.

### Path to first sale
- **Day 0–5:** build the free core (dictionary, quiz, leaderboard, daily word) and the `/supporter` pre-order. Write the ToS and privacy page.
- **Day 5–8:** directory listings.
- **Day 8–25:** the sponsor contacts server admins; this is the main lever.
- **Day 20–30:** build `/practice` while the pre-order test runs.
- **First founding pre-order:** about day 30–45.
- **Ideator's estimate:** first sale ≈ **45 days from today (~20 Nov 2026)**; $300/mo net around months 9–15.

### Who does what
- **AI operator:**
  - All code and deployment.
  - Listings and descriptions.
  - Quiz and deck generation from CC-CEDICT and HSK 3.0 lists.
  - Support replies through the support inbox and a `/feedback` command.
  - Weekly metrics.
  - Prompt and cap tuning.
  - Drafts the admin messages for the sponsor to send.
- **Human sponsor:**
  - **One-time, about 3 h:** Lemon Squeezy KYC, domain, Discord developer team with 2FA, and later Stripe identity verification for Discord app verification at 76+ servers (about 0.5 h).
  - **Recurring, 0.25–0.5 h/wk:** sending or answering admin and Reddit messages in the first 6 weeks; then escalations only.
  - Day-to-day participation in the servers as a learner is hobby time and is **not** counted. It should be disclosed whenever the sponsor mentions the bot.

### Moat — why not just ask ChatGPT?
For the free tier, ChatGPT is simply not the comparison. ChatGPT does not run timed multiplayer quiz races, leaderboards or a daily word inside the server where learners already spend time; that social layer is the product.

For `/practice`, the honest answer is a **thin model moat but a real workflow moat:**
- level-locking to HSK 3.0 bands;
- an error log that feeds SRS reviews delivered as DMs in the app learners already have open;
- $4.99 against ChatGPT Go at $8 or HelloChinese at $11.99.

The durable moat is **being the default bot in the big servers first**. Kotoba shows a niche language bot can become entrenched.

### Biggest risks (ideator's own view)
- **Discord bot users expect free.** Kotoba is free, and paid conversion may sit below 1%. The pre-order test exists to find this out before `/practice` is built.
- **Platform dependency and rules:**
  - Discord's monetisation-parity rule takes about 30% of Premium sales.
  - App Directory listing and Premium billing both need verification at 76+ servers, a gate that cannot be bought.
  - A Discord policy change could hit the whole business.
- **Correctness and the minors rule:**
  - AI corrections in Chinese can be wrong. Mitigate by pinning `/practice` to level-bounded prompts, showing a "suggested correction (AI)" label, and spot-checking a sample of corrections against CC-CEDICT and grammar patterns. The sponsor's own daily use acts as QA.
  - Discord allows users aged 13+, so set the paid tier to 18+ in the ToS, store no voice, and keep personal data to Discord user IDs.

---

## I2 — Episode Study Packs: done-for-you transcript PDFs and flashcard decks for Chinese-learning podcasters and YouTubers

- **Persona:** The Insider
- **One-liner:** Creators of Chinese-learning podcasts and YouTube shows send an episode link or script and get back, within 24 h and in their own branding, a study pack: line-by-line hanzi + pinyin + English, an HSK 3.0-tagged vocabulary table, grammar notes, exercises, and Anki and Pleco import files. They review it as native speakers and sell it to their own Patreon or members.
- **Founder-fit asset used:** The sponsor's AI-lesson pipeline already turns Chinese input into level-aware study material. As a learner, the sponsor is also the end consumer of these packs and knows what makes them useful: tone marks on every syllable, correct readings of polyphonic characters (多音字), measure words, and Pleco-ready exports.
- **Demand test:**
  - **Contacts:** 40 named creators, found through the Apple Podcasts "Learn Chinese" lists and YouTube, all with public business emails. Each gets one personalised 1:1 email over 10 business days (≤ 5/day): "I'm a learner who built a pack generator; want a free pack for episode X, in your branding?"
  - **Offer to anyone who accepts:** a **$29 founding month (4 episodes)** through a Lemon Squeezy checkout.
  - **Thresholds (21 days):**
    - **Pass:** ≥ 3 paid creators.
    - **Pivot:** ≥ 8 free-sample requests but < 3 paid. Re-price per episode, or offer a revenue share.
    - **Fail:** < 4 replies.
- **Customer:** Independent creators (often native-speaker teachers) who already **sell or gate PDF transcripts** as patron perks. Examples:
  - Chinese Garden: PDFs with transcripts in Chinese, pinyin and English, plus grammar and homework, supported via Patreon / Buy Me a Coffee.
  - Chinese Around You: PDF transcripts with pinyin, hanzi, English and vocabulary notes.
  - Mandarin Corner: PDF transcripts and flashcards behind a $10 donation.
  - Slow Chinese: script PDFs.
  - Grace Mandarin Chinese, and Mandarin with Miss Lin (Patreon).

  They hang out on Patreon, YouTube and Apple Podcasts. They already pay for Descript, Canva, Riverside, transcription tools and freelance editors.
- **Problem / desire:** "Each episode's PDF takes me 2–3 hours: transcribing, adding pinyin, translating, building the vocab list. Patrons love them, but I can't keep up, so I publish fewer episodes." The PDF is what turns free listeners into paying patrons, and its production cost is the bottleneck.
- **Offering:** A per-episode study pack, delivered by email and a private download link.
  - Branded PDF.
  - Anki `.apkg` deck.
  - Pleco flashcard import file.
  - CSV vocabulary list.
  - Optional bilingual SRT subtitles.
  - The creator's own audio or script is the input. Packs are delivered as editable DOCX/Google-Doc-ready files, so the native-speaker creator corrects anything before publishing. This **solves U2's "no native QA" flaw by design.**
- **Price & revenue model:**
  - Pay-as-you-go **$12/episode**.
  - **Studio $39/mo** (4 episodes).
  - **Pro $79/mo** (10 episodes + subtitles).
  - Monthly subscription through Lemon Squeezy.
  - **Break-even:** 9 Studio or 5 Pro creators clear $300/mo net.

- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Domain + sample page on GitHub Pages / Cloudflare Pages | $12 |
| PDF templating (Typst or HTML-to-PDF, open source) and genanki for decks | $0 |
| **Total** | **$12** |

### Monthly running costs (excluding operator tokens)
- **Speech-to-text:** Whisper-class API at about $0.006/min; a 20-min episode costs about $0.12. Skipped when the creator supplies a script.
- **LLM passes:** pinyin disambiguation, translation, notes and exercises, about $0.20–0.50 per episode.
- **Storage:** Cloudflare R2 free tier.
- **Lemon Squeezy:** 5% + $0.50 per transaction.
- **At 9 Studio creators:** about $15 processing + about $11 fees ≈ $26/mo.

### Customer acquisition plan
1. Build a **list of about 60–120 creators**: Apple Podcasts / Spotify "learn Chinese" shows, and YouTube channels that mention transcripts or Patreon. Record each one's *public* business email and whether they already sell PDFs.
2. Send **one personalised email per creator**, referencing a specific episode and offering a free pack for it on request. No attachments of their content unless invited. Send at most once, plus one follow-up, with a CAN-SPAM-compliant footer and unsubscribe.
3. The free pack is delivered within 24 h of a yes. The follow-up email offers the founding month.
4. **Retention loop:** a creator who publishes weekly needs a pack every week, so this is subscription-shaped.
5. **Referral:** each pack's footer carries a small "pack made with …" credit, removable on Pro. Creators know each other, and podcast guest swaps are common.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Named-creator 1:1 outreach** (above). This is a partner channel: each creator already owns the paying audience. **Speed:** replies within 3–10 days.
2. **Public sample library:** 3 sample packs built only from **Creative Commons or public-domain Chinese audio**, plus one from the sponsor's own recorded practice dialogue, posted on the site. They prove quality without touching anyone's copyright, and they give the outreach emails something to link. **Speed:** live by day 7.
3. **One honest maker post by the sponsor** in a creator-economy or language-teacher community (for example, a r/ChineseLanguage resources thread or a language-teacher forum, within its rules). **Speed:** a one-off, in weeks 2–4.
4. *(Optional, later)* A Fiverr gig, "Chinese learning transcript PDF with pinyin", as a second marketplace with built-in search. It is held back because Fiverr has no messaging API, so every message would cost human time.

### Path to first sale
- **Day 0–7:** pipeline (ASR → segmentation → polyphone-aware pinyin → translation → vocabulary with HSK 3.0 bands → notes and exercises → PDF, apkg and Pleco) and 3 public samples.
- **Day 7–17:** outreach in batches of 5/day.
- **Day 10–24:** free packs delivered and the founding offer sent.
- **First paid founding month:** about day 25–35.
- **Ideator's estimate:** first sale ≈ **30 days from today (~5 Nov 2026)**; $300/mo net around months 4–8, at about 9 creators.

### Who does what
- **AI operator:**
  - Builds the creator list.
  - Writes and sends the personalised emails within the caps.
  - Produces every pack.
  - Handles revisions requested by email.
  - Runs billing reminders and churn follow-ups.
- **Human sponsor:**
  - **One-time, about 2 h:** Lemon Squeezy KYC, domain, inbox; approve the email template and the first 5 sends.
  - **Recurring, about 0.25 h/wk:** read a weekly digest and spot-check one pack as a learner, which is dogfooding.

### Moat — why not just ask ChatGPT?
Creators *can* paste a transcript into ChatGPT, and some will. They pay anyway for a **repeatable, branded, multi-format pipeline**: three exports (PDF, Anki, Pleco) in a consistent template every week, no prompt-wrangling, polyphone-aware pinyin, and HSK 3.0 tagging, which became timely when HSK 3.0 went worldwide in July 2026. The buyer compares against **their own 2–3 hours per episode**, not against a free chatbot. The output is more convenient than a DIY prompt, not something they couldn't do themselves.

**Honest weakness:** a determined creator can rebuild this with a weekend of prompting.

### Biggest risks (ideator's own view)
- **Small total market:** probably 100–200 relevant creators worldwide, so churn of 2–3 creators hurts. The ceiling is near the $1k stretch target, not far above it.
- **Outreach perception:** even careful 1:1 B2B emails can read as spam. Keep it to ≤ 120 total contacts, one follow-up, and an easy opt-out, and stop if any complaint arrives.
- **Quality incidents:** wrong pinyin readings or awkward translations under a creator's brand. The creator review step mitigates this, but the first sloppy pack loses that customer.
- **Copyright and data:** process only content the creator owns or licenses to us. The ToS should grant us a processing licence only and give the creator full ownership of the outputs.

---

## I3 — Role-Play Room: level-locked AI conversation homework for college and adult-education Chinese classes

- **Persona:** The Insider
- **One-liner:** A Chinese instructor sets up a role-play assignment (scenario + the chapter's vocabulary and grammar, pasted in). Students join with a class code and no account, then practise text conversation with an AI partner that stays inside that word list. The instructor gets completion stats, transcripts and the class's top-10 errors. It is sold per class or per student seat, for 18+ classes only.
- **Founder-fit asset used:** This is the sponsor's AI conversation-practice engine, with a teacher dashboard added. Level-locking and error logging are shared code with I1's `/practice`. The sponsor's own learning gives taste for which corrections help and which are noise.
- **Demand test:**
  - **Setup:** a working demo of one assignment (5 days) and a landing page with a **"Spring 2027 founding class: $99 per class (normally $149), card charged now, full refund if not used by 15 Feb"** checkout.
  - **Contacts:** 60 instructors named on public US/UK/Canadian university and community-college Chinese program pages, emailed 1:1 (≤ 6/day), timed for spring syllabus planning in November.
  - **Thresholds (by 15 Dec 2026):**
    - **Pass:** ≥ 4 paid founding classes, or ≥ 10 free-trial assignments actually run with students.
    - **Pivot:** trials but no payment; test the student-pays seat model instead.
    - **Fail:** < 3 trials.
- **Customer:** Instructors of first- to third-year Chinese at colleges, community colleges, university extension programmes and adult language schools. US postsecondary Chinese enrollment is in the tens of thousands, down 14.3% from 2016 to 2021 according to MLA data. These instructors gather at **ACTFL (San Antonio, 20–22 Nov 2026)**, CLTA (Chinese Language Teachers Association), department mailing lists and teacher Facebook groups. They already pay for, or make students pay for, workbook access codes, Quizlet, Pleco and Integrated Chinese companion materials.
- **Problem / desire:** "My students only speak or write Chinese in class, 3–4 hours a week. ChatGPT homework is a mess: it uses words they don't know, and I can't see what they did." Instructors want **assignable, checkable practice at exactly this week's vocabulary**.
- **Offering:**
  - **Hosted web app (PWA)** for students: join by code, choose a nickname (no email needed), and do text role-play, 20–40 turns per session, with inline corrections and an end-of-session summary.
  - **Instructor dashboard:** create an assignment from pasted vocabulary and grammar points, then see per-student completion and transcripts, plus a class error heatmap exportable to CSV. Data is deleted at the end of the semester.
  - Voice is left out of v1 on purpose (BIPA and cost lessons from U3).
- **Price & revenue model:**
  - **Class licence $149/semester** (up to 30 students), paid by the instructor or department card.
  - **Or student seats at $12/semester** each, paid by students as a required material, like a workbook code.
  - **Break-even:** about 6–11 classes clear $300/mo net, depending on the model.

- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Domain | $12 |
| Cloudflare Pages + Workers + D1 (free tier) | $0 |
| ACTFL attendance or booth | $0. Not attended; the booth is far over the cap. |
| **Total** | **$12** |

### Monthly running costs (excluding operator tokens)
- **Inference:** text-only small model, capped at 2 sessions × 40 turns per student per week. That is about $0.15–0.30 per student-month, so roughly $15–30 per 25-student class per semester.
- **Hosting:** $0.
- **Lemon Squeezy:** 5% + $0.50 per transaction.
- **At 10 classes:** about $60/mo inference + about $40/mo fees, averaged.

### Customer acquisition plan
1. Build a list of programmes from public university Chinese department pages: instructor name, course level and textbook if stated.
2. Send a 1:1 email offering a **free trial assignment for this week's chapter**. The operator pre-builds it from the instructor's public syllabus vocabulary when it is published, or the instructor pastes their own list.
3. A trial assignment that students actually complete triggers the founding-price offer for spring.
4. **Spread within a department:** one instructor's dashboard export is shown to colleagues teaching other levels.
5. **Seasonal:** outreach peaks in mid-October–November for spring planning, and again in July–August for fall.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Named-instructor 1:1 emails**, with a ready-made trial for their chapter. Why it works early: the instructor sees their own vocabulary list working with no effort. **Speed:** replies in 1–2 weeks; trials in November.
2. **The sponsor's genuine learner-maker post** on r/ChineseLanguage and in language-teacher forums ("I built a level-locked role-play tool, free for teachers to try this semester"). **Speed:** a one-off, in weeks 2–4.
3. **ACTFL and CLTA follow-ups:** after ACTFL (20–22 Nov), email presenters of public sessions on Chinese or AI in language teaching, referencing their talk. **Speed:** late November to December, landing exactly in spring planning.

### Path to first sale
- **Day 0–10:** build the demo, dashboard and checkout.
- **Day 10–35:** outreach; trials run in late-semester classes in November.
- **Day 35–70:** follow-ups after ACTFL; the founding spring offer.
- **First payment:** most likely in mid-December, when instructors lock their spring materials, or at the start of the January semester.
- **Ideator's estimate:** first sale ≈ **75–100 days from today (late Dec 2026 to mid-Jan 2027)**; $300/mo net in the fall 2027 semester.

### Who does what
- **AI operator:**
  - Builds the app.
  - Builds and maintains the instructor list.
  - Writes and sends 1:1 emails.
  - Pre-builds trial assignments.
  - Handles support email and accessibility fixes.
  - Purges data each semester.
  - Writes the plain-English data-practices page.
- **Human sponsor:**
  - **One-time, about 2.5 h:** Lemon Squeezy KYC, domain, review of the ToS/privacy page.
  - **Recurring, about 0.25–0.5 h/wk:** read and answer the rare instructor question that needs a human; decline any institutional contract (DPA/procurement) above the self-serve terms unless the sponsor chooses to sign it.

### Moat — why not just ask ChatGPT?
For the **instructor**, ChatGPT is not assignable or checkable:
- no class code;
- no locking to this week's word list;
- no transcripts or class error report;
- many institutions bar requiring students to create consumer AI accounts.

For **students**, the role-play is shaped to the chapter they will be tested on. The free substitutes are generic AI tutors (Pingo, Speak) and textbook-publisher drills. The workflow integration is the moat, and the switching cost comes from the instructor's saved assignments.

### Biggest risks (ideator's own view)
- **Slow, seasonal buyer:** instructors adopt per semester. If the November test misses, the next real window is July–August 2027 (P50 risk).
- **Institutional rules:**
  - FERPA and the institution's AI or procurement policies may push instructors to ask for a DPA, which the sponsor would have to sign.
  - Accessibility (WCAG) expectations apply.
  - Mitigate by keeping it 18+ only, with no student emails or real names, deletion at semester end, and no model training on student data.
- **Correction quality and level drift:** a wrong correction in front of a teacher is worse than in front of a learner. Mitigate by showing corrections as "AI suggestion", letting the instructor override a correction and having the tool remember it, and by the sponsor's own weekly dogfooding.

---

## Sources checked (2026-10-06)
- Jagex Fan Content Policy (§2.4, §6.1.1–6.1.3): https://legal.jagex.com/docs/policies/fan-content-policy
- OSRS bingo and clan tools: https://guildorder.com/plugins/osrs-bingo · https://github.com/fatfingers23/trackscape-discord-bot · https://top.gg/bot/467204490895032320
- Discord monetisation eligibility: https://docs.discord.com/developers/monetization/enabling-monetization
- Discord payment parity: https://support-dev.discord.com/hc/en-us/articles/8563934450327
- Discord 70/30 split (developer reports): https://support.discord.com/hc/ko/community/posts/22834240582423-Lower-Premium-App-Subscriptions-fees
- Discord bot verification at 76/100 servers (community and support posts): https://support.discord.com/hc/ko/community/posts/360061569571-Discord-Bot-Verification
- Chinese-learning Discord servers: https://www.maayot.com/blog/?p=1982 · https://discordbotlist.com/servers/refold-yi-yu-zh-784482683282915389 · https://discordhunt.com/es/servers/chinese-english-language-exchange-266695661670367232
- Kotoba (Japanese analogue): https://discordbotlist.com/bots/kotoba · https://www.tofugu.com/japanese-learning-resources-database/kotobaweb/
- Existing Chinese MCP and SRS tools (which killed an "MCP learner-memory" variant): https://claudemarketplaces.com/mcp/kuibin-dev/hsk-mcp · https://glama.ai/mcp/servers/Hyneq00/minddory-mcp
- Tone tools (which killed a tone-mirror extension variant): https://mwm.ai/apps/tonedetector-lite/550854681 · https://chromeboard.com/extension/chinese-ai-pronunciation-ciginfkinhpfknohjbplmlhgmbomgokg
- Creators selling transcript PDFs: https://castbox.fm/channel/6661088 · https://www.alllanguageresources.com/?p=19845 · https://search.podderapp.com/podcast/slow-chinese-podcast-learn-chinese
- HSK 3.0 timing: https://hsklord.com/blog/hsk-3-0-changes-2026 · https://edu.sh.gov.cn/study_en_hsk/20260107/5292266eca744a959c1db43237fbc185.html
- Chinese enrollment trend: https://pinyin.info/news/2023/us-postsecondary-enrollments-in-chinese-trending-down/
- ACTFL 2026 dates: https://bridge.edu/tefl/blog/event/2026-actfl-annual-convention-and-world-languages-expo/
- Agent-asset dead ends:
  - Apify market-research Actors at 0–3 MAU: https://apify.com/synergistic_freedom/apify-store-competitor-intelligence · https://apify.com/scraper_guru/apify-store-analyzer
  - Polsia: https://noqta.tn/en/blog/autonomous-ai-companies-polsia-nanocorp-guide-2026
  - Paid skills marketplaces: https://www.besthub.dev/articles/the-era-of-paid-skills-is-here-how-can-developers-earn-their-first-revenue-ed6aed87021a
  - claude.ai toolbox extensions: https://www.ai-toolbox.co/claude-toolbox-competitors/claude-chrome-extension-what-ai-toolbox-adds-2026
  - Claude Code vocabulary ticker (already exists): https://www.skillsdirectory.com/skills/marcsky-ticker
- ChatGPT apps cannot sell digital goods (as of Sept 2026): https://developers.openai.com/apps-sdk/build/monetization
