# Channel-first ideas — The Channel Partner

_Run 2026-10-06, round 2. Persona: The Channel Partner (ideator-channel-partner). Day 0 is today, 2026-10-06. All "days to first sale" figures count from today. They include build time, partner reply lag, editorial-calendar lag and payout timing (lesson 2)._

**How these three differ from round 1.** Every idea here starts from a named person or organisation that already owns the buyer's trust. The product comes second. That answers the round-1 committee finding that "few B2B buyers with real budgets were found through partners who already own them" (REPORT.md §5). Each idea uses a different deal shape:

| ID | Deal shape | Partner type | Fixes a listed idea? |
|---|---|---|---|
| C1 | Affiliate share (40%) plus a free member perk | Grant-writing course creators and podcasters | No. It is new. It uses public 990-PF data, but the channel is solved first (lesson 9). It does not overlap W3, which was a deadline calendar. |
| C2 | White-label licence that the consultant resells | Safety-consultant podcasters, consultant networks, associations | **Yes: S2.** S2 had no channel and faced a flooded Etsy shelf. C2 also reuses D2's ingest. |
| C3 | Co-branded practice lab plus a per-student school licence | Medical-interpreter training publishers, schools and YouTubers | No. It is new. |

**Affiliate mechanics for all three.** Lemon Squeezy's built-in Affiliates hub handles affiliate sign-up, tracking and payouts. Lemon Squeezy adds a 2% fee on referred orders, so the partner does no admin. Lemon Squeezy is moving to Stripe Managed Payments, and that product has no affiliate tool. The fallback is Gumroad's affiliate feature. Failing that, the sponsor pays partners monthly by PayPal at about 10 min/month.

---

## C1 — FunderFit: white-label funder prospect reports for freelance grant writers, sold through grant-writing academies

- **Persona:** The Channel Partner (ideator-channel-partner)
- **One-liner:** For $39, a freelance grant writer gets a 25-funder prospect report for one client nonprofit. The report is built from real IRS 990-PF grant records and branded with the freelancer's logo, so they can resell it as "prospect research". It is distributed by the academies and podcasts that train freelance grant writers, for a 40% affiliate share.
- **Channel partners (named):**
  1. **Holly Rustick.** She hosts the *Grant Writing & Funding* podcast (top-ranking in the category; she says she coaches "thousands of people" weekly) and runs the **Freelance Grant Writer Academy**. Her students are exactly this buyer: they say they have "$4M+ in revenue in their grant writing businesses". First contact: the sponsor sends her a personal email with a free sample report built for one of her public case-study nonprofits, plus a pitch to be a podcast guest. ([podcast](https://podcasts.apple.com/podcast/id1235917132), [episodes](https://share.transistor.fm/s/132c9bbf))
  2. **Meredith Noble, Learn Grant Writing.** It is an online membership for people building grant-writing careers. Her book *How to Write a Grant* was a #1 Amazon bestseller in nonprofit fundraising, and she says her students have secured more than $627M. She already teaches funder research publicly (the "100+ grants to best fits" webinar). First contact: a personal email offering a free member perk, one report per member, with the code tracked through the affiliate hub. ([npconnect webinar](https://info.npconnect.org/events/details/how-to-go-from-100-grants-to-the-best-fits-for-you-the-grant-writing-unicorn-method-w-meredith-noble-5389), [We Are For Good episode](https://weareforgood.buzzsprout.com/1258940/episodes/16146768-587-how-to-find-the-right-grants-to-go-after-leveraging-ai-to-work-smarter-not-harder-meredith-noble))
  3. **Queen Israel, Grant Writing Academy.** A Substack with about 1.9k subscribers that trains grant writers. Substack has no API, but that does not matter here, because she sends the mention herself. First contact: a Substack DM or reply from the sponsor's own account, plus a sample report. ([Substack](https://substack.com/@grantwritingacademy))
  4. **Camille Ricks, Gladiator Grant Writing.** A Substack newsletter; she says she has raised over $7M. Audience size is unverified. First contact: the same way as #3. ([Substack](https://gladiatorgrantwriting.substack.com))
  5. **Instrumentl's partner roster**, shown as a list of who already sells tools to this audience: GPA Approved Trainers, the podcasters Teresa Huff and Jenni Hargrove, and RBW Strategy. They already promote a $299+/mo tool. FunderFit is pitched as the **low-end complement for clients who can't afford Instrumentl**, not as a replacement. First contact: a personal email after the first 2 partners are live, so the pitch can include proof. ([Instrumentl partners](https://instrumentl.com/partners))
  - *Not in the 30-day path:* the Grant Professionals Association (GPA) member-benefit programme. Associations take 60–120 days to decide.
- **Demand test:**
  - **Step 1, partner pre-sale:** the sponsor pitches 10 partners one-to-one, each with a free custom sample report. **Pass:** at least 2 agree in writing to mention it to their list or members within 30 days. **Fail:** fewer than 2 agree by day 35. In that case, kill the idea or pivot to a direct Gumroad listing.
  - **Step 2, willingness to pay:** in the first 2 partner mentions, offer a $19 founding price for the first report. **Pass:** at least 5 paid reports within 14 days of the first mention. **Fail:** fewer than 2.
  - The build stops at a manual "sample report" pipeline until Step 1 passes.
- **Customer:**
  - **Who:** freelance and part-time grant writers, often graduates of FGWA or Learn Grant Writing, serving 2–10 small nonprofits each.
  - **Where:** they listen to *Grant Writing & Funding*, join the academies' private communities, and read grant-writing Substacks.
  - **What they pay for now:** academy memberships, Instrumentl (from $299/mo billed annually), Candid (about $60–$179/mo), and GrantStation.
  - **Secondary buyer:** small-nonprofit EDs who do their own grants.
- **Problem / desire:** "My client wants a list of foundations that will actually fund them, but they won't pay me 10 hours of research and I can't justify $299/month of Instrumentl for two clients." Q4 is when clients plan their 2027 grant calendars, so prospect lists are requested now.
- **Offering:**
  - **Input:** a web form for the client's EIN or mission, geography, budget size, program areas and 3 "peer" organisations.
  - **Output in about 10 min:** a PDF and DOCX report with no FunderFit branding (white-label: the freelancer's logo and name), containing:
    - 25 ranked private foundations;
    - for each funder: the **actual grants they made to similar organisations in the last 3 filed years**, with grantee, amount, purpose and year, from 990-PF Part XV;
    - median grant size, geographic pattern, and whether they accept unsolicited proposals (the 990-PF "only contributes to preselected organisations" flag);
    - the website and application page where the operator can find them;
    - a 2-sentence fit rationale for each funder;
    - a closing "top 5 to approach first" page.
  - **Data:** the IRS Form 990 e-file XML bulk downloads (public). Grantmakers.io shows the 990-PF dataset can be parsed this way. ProPublica's Nonprofit Explorer API is used only for lookups (check its terms before relying on it).
- **Price & revenue model:**
  - $39 per report, one-time.
  - "Practice" plan at $99/mo for 5 reports plus a quarterly refresh of past reports.
  - Founding price for the demand test: $19.
  - Partners get 40% of first-year revenue from referred buyers.
  - Partner members get 1 free report (a perk that costs us about $0.50 in compute).
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Domain | $12 |
| Lemon Squeezy store + Affiliates (MoR) | $0 |
| Hosting: Cloudflare Pages/Workers + R2/D1 free tier for parsed grant tables (only 990-PF filers, last 3 years) | $0 |
| IRS bulk XML download + parse (GitHub Actions free minutes) | $0 |
| LLM test runs for 10 sample reports | ~$5 |
| **Total** | **~$17** |

### Monthly running costs (excluding operator tokens)
- Hosting/storage: $0–$5. The 990-PF grants table for 3 years is a few million rows, so only the grant lines and filer metadata are kept.
- Per-report compute: about $0.30–$1.00 for embedding and ranking with a small model, plus PDF generation.
- Email delivery: Resend free tier.
- MoR: 5% + $0.50 per order, plus 2% on affiliate-referred orders.
- Affiliate share: 40% of referred revenue.
- **Unit economics:**
  - A $39 report through an affiliate nets about $20. A direct sale nets about $36.
  - A $99/mo plan through an affiliate nets about $52.
  - **$300/mo net ≈ 15 affiliate-referred reports, or 6 Practice subscribers, or a mix.**

### Customer acquisition plan
1. The sponsor emails 10–15 partners one-to-one (named above). Each email includes a free sample report built for a nonprofit the partner has publicly worked with or featured. Showing the product does the selling.
2. Partners who agree get a ready-made kit: a 120-word newsletter blurb, a podcast talking point, a member-perk code, and their affiliate link. Their effort is close to zero: paste, or mention once.
3. Members redeem a free report → they send it to a client → the client asks for more → the freelancer buys a report or the $99/mo plan.
4. Each report's DOCX has a small, removable "prepared with FunderFit" line in the document properties only, not on the page. White-label means the client never sees our brand. Growth comes from the freelancer reusing it, not from the client.
5. After 2 partners are live, the sponsor uses their quotes to pitch the Instrumentl partner roster and GPA Approved Trainers.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Small Substack and newsletter partners (Queen Israel, Camille Ricks)** — a one-to-one pitch with a free sample — small writers answer DMs and can mention it in their next issue — a mention within about 2–4 weeks of agreement.
2. **Academy member perk (Learn Grant Writing, FGWA)** — a free first report posted in the members' community by the partner — a perk costs the partner nothing and makes them look good — 3–6 weeks, because academies batch announcements.
3. **Podcast guest spot or host mention (Grant Writing & Funding, Instrumentl-roster podcasters)** — the sponsor appears as a guest. The AI preps the talking points and a free listener offer. If the sponsor can't commit about 45 minutes, a host-read mention replaces the guest spot — slowest: podcast calendars run 4–10 weeks.

### Path to first sale
- **Days 0–3:** the sponsor sets up Lemon Squeezy (KYC), turns on Affiliates and buys the domain (about 1.5 h).
- **Days 1–10:** the AI downloads and parses 3 years of 990-PF XML, builds the ranking pipeline, and hand-checks 10 sample reports against the filings.
- **Days 7–14:** the AI drafts 12 personalised partner emails, each with its own sample report. The sponsor reviews and sends them from a personal address (about 1 h total).
- **Days 14–35:** replies arrive and the first 1–2 partners agree. Expected: about a 25% reply rate and a 10–20% agreement rate, so **about 12 pitches land 2 partners**.
- **Days 30–50:** the first newsletter mention or member-perk post goes out, free reports are redeemed, and the first paid reports follow.
- **Estimate: first sale around day 45 (range 35–75).** The first affiliate payout runs on Lemon Squeezy's monthly cycle, so about day 75–90.
- **Seasonality:** good. Oct–Dec is grant-calendar planning season for 2027, and many foundations have Jan–Mar deadlines. The second half of December is dead, so if partners slip past early December, the first sale moves to mid-January.

### Who does what
- **AI operator:**
  - quarterly IRS data refresh and parse;
  - generates reports on demand;
  - QA spot-checks 1 in 10 reports against the source XML;
  - drafts partner kits and pitch emails;
  - answers support email;
  - tracks partner performance and suggests re-pitches.
- **Human sponsor:**
  - **One-time, about 2.5 h:** MoR and affiliate setup, domain, and sending the first 12 partner emails.
  - **Recurring, about 0.5 h/week for the first 8 weeks, then about 0.25 h/week:** replies that need a human voice, occasional partner payouts if the fallback is needed, and an optional 30-min partner call. Calls count against the budget, so offer async first.

### Moat — why not just ask ChatGPT?
- **ChatGPT and other chatbots can't reliably say who actually funded whom.** They hallucinate foundations and grant amounts. The value here is **grant-level evidence from parsed 990-PF filings**: "this foundation gave $15k to a food bank 20 miles from your client in 2024".
- **Free substitutes:**
  - **grantmakers.io:** free search of the same data, but no ranking, no fit rationale and no client-ready document.
  - **ProPublica:** free, but one filing at a time.
- **Paid substitutes:**
  - Instrumentl ($299+/mo) and Candid ($60–$179/mo) are better products, but they are subscriptions sized for full-time grant shops.
  - Several Apify Actors already do 990-PF prospecting for technical users.
- **Why the freelancer pays anyway:**
  - It is a **per-client, white-label deliverable** they can bill at $200–$500.
  - It is bought through **someone they already trust** (their academy or podcast).
- **Honest weakness:** the data is public and the parse is reproducible. The real moat is the channel and the report format, not the data.

### Biggest risks (ideator's own view)
- **Partner conflict.** Several channel owners are Instrumentl partners or sell their own prospect-research training. They may decline in order to protect that income. Mitigation: position FunderFit for the "client can't afford Instrumentl" segment, and offer 40% (likely higher than incumbent referral rewards; Instrumentl's rate is unverified).
- **Data quality.** Grant purpose fields in 990-PF filings are messy, and recent years lag by 12–24 months. A report with stale or wrong funders hurts the freelancer's reputation and therefore ours. Mitigation: show the filing year on every line, and spot-check 1 in 10 reports.
- **Thin per-sale revenue after the affiliate share.** If buyers take only the free perk, revenue stalls. Kill rule: fewer than 5 paid reports after 2 partner mentions.

---

## C2 — Client Safety Kit: a white-label monthly bilingual safety pack that independent safety consultants resell to their clients (fixes S2, reuses D2)

- **Persona:** The Channel Partner (ideator-channel-partner)
- **One-liner:** Every month, an independent safety consultant receives a ready-to-send, **consultant-branded** kit for each client. Each kit has 4 trade-specific English/Spanish toolbox talks, bilingual sign-in sheets, and a one-page "OSHA cited your industry for this last month" brief built from live OSHA citation data. The consultant licenses it for $49–$99/mo and resells it as a retainer deliverable. It is distributed through safety-consultant podcasts and consultant networks.
- **Channel partners (named):**
  1. **Sheldon Primus, *The Safety Consultant Podcast*.** A weekly show since 2019, billed as "your ultimate weekly guide to starting or growing a profitable occupational safety and health consulting business". He also runs YouTube @safetyconsultant and a Facebook group for safety consultants. His audience is literally people who are starting consulting practices and need deliverables. Audience size is unverified. First contact: the sponsor emails the public contact address on the show page with a sample kit branded with *his* logo, plus a guest-pitch on "productizing a safety retainer". ([show page](https://share.transistor.fm/s/0d9decab))
  2. **Inogen Alliance.** A network of 70+ independent EHS firms with about 6,000 consultants worldwide. It also runs the *Rethinking EHS* podcast. A white-label kit lets small member firms offer a monthly client touchpoint without staff time. First contact: a personal email to the alliance's US member firms, one at a time (not a blast), starting with Antea Group USA, the podcast sponsor. This is a slower, higher-value path. ([Inogen podcast](https://www.3blmedia.com/news/inogen-alliance-launches-season-2-global-podcast-rethinking-ehs))
  3. **ASSP Consultants Practice Specialty.** ASSP's community of external OSH consultants. It publishes a *Consultants Business Development Guide*, runs open webinar calls for consultants, and runs mentoring. Member count is unverified. First contact: the sponsor, if an ASSP member, or an existing member, offers a free 20-minute "productized retainer" webinar segment with a member-only discount. Not counted in the 30-day path. ([ASSP page](https://www.assp.org/membership/communities/practice-specialties/consultants))
  4. **Jay Allen, *Rated R Safety Show* (formerly *Safety FM*).** *Safety FM* averaged about 90k downloads per episode and had 72M+ listens before it ended in November 2025. Allen continues on the *Rated R Safety Show*. This audience is broad, so it is used for an affiliate or sponsored mention only after the consultant-specific partners convert. ([Libsyn ads page](https://advertising.libsyn.com/SafetyFM), [Apple](https://podcasts.apple.com/podcast/id1377151103))
  5. **D2 InspectionWatch subscribers**, once they exist. The same buyer, the same data, and an upsell inside the product we already run. The committee anticipated this in REPORT.md §3: "a client safety kit keyed to the most-cited standards in each inspected client's NAICS code".
- **Demand test:**
  - **Step 1, partner:** pitch 10 partners or consultant firms one-to-one, each with a sample kit branded for them. **Pass:** at least 2 agree to promote it to their audience or members, or at least 2 firms agree to a paid pilot, by day 35. **Fail:** 0–1 agree.
  - **Step 2, pre-sale:** a founding offer of "$29/mo for life, first month billed when the first kit ships" goes to the partners' audiences. **Pass:** at least 4 consultants pay within 21 days of the first mention. **Fail:** fewer than 2.
  - The first kit is produced only after payment.
- **Customer:**
  - **Who:** independent safety consultants and 1–10-person EHS firms with small-contractor clients, such as landscaping, roofing, concrete, janitorial, tree care and light manufacturing. Many of those clients have Spanish-speaking crews.
  - **Where they hang out:** *The Safety Consultant Podcast* and its Facebook group, ASSP chapters and the practice specialty, and safety podcasts.
  - **What they pay for now:** CRM, insurance, training content licences (e.g. NRCA toolbox talks at $95–$195), and SafetyCulture/iAuditor.
- **Problem / desire:**
  - "My retainer clients need something from me every month or they cancel. Writing four talks per client in two languages eats my billable time."
  - "Free CPWR talks are generic, and my client's GC and insurer want proof of weekly meetings."
- **Offering:**
  - **Per client, per month:**
    - 4 one-page toolbox talks matched to the client's trade, region and season (for example, cold stress and ice in January for northern crews). English and Spanish are side by side, each talk cites its OSHA standard, and it has 2 crew questions.
    - A bilingual sign-in sheet.
    - **A one-page "Your industry in OSHA's eyes this month" brief.** It lists the most-cited standards and the largest penalties issued last month in the client's NAICS code and state, built from DOL OSHA enforcement data through D2's ingest. **This is the data hook free talks don't have.**
  - **Branding:** the consultant's logo, name and contact on every page. There is no Client Safety Kit brand.
  - **Delivery:** PDFs plus a ready-to-forward client email, delivered to the consultant by the 25th of each month. A simple meeting-log page per client lets crews' sign-in photos be uploaded for audit records (optional, phase 2).
- **Price & revenue model:**
  - Consultant licence: **$49/mo for up to 10 client kits**, or **$99/mo unlimited** (+ a Spanish-language client email template).
  - Founding price: $29/mo.
  - Partners get 40% of revenue for 12 months.
  - Inogen-style firm deals: a $199/mo firm licence.
  - Consultants typically resell the kit inside a $300–$1,500/mo retainer.
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Domain (or a subdomain of D2's domain: $0) | $0–$12 |
| Lemon Squeezy (shared with D2's MoR account) | $0 |
| DOL OSHA enforcement data API key | $0 |
| Hosting (Cloudflare free tier, shared with D2) | $0 |
| LLM generation + second-pass Spanish review for a 150-talk seed library across 6 trades | ~$15 |
| **Total** | **~$15–$27** |

### Monthly running costs (excluding operator tokens)
- Hosting: $0, shared with D2.
- Per-kit generation: about $0.05–$0.20. Talks come from a reviewed library; only the citation brief is generated fresh each month.
- Email: Resend free tier.
- MoR: 5% + $0.50, plus 2% on affiliate orders.
- Affiliate share: 40%.
- **Unit economics:**
  - A $49 licence through an affiliate nets about $25. A direct sale nets about $46.
  - **$300/mo ≈ 7 direct or 12 affiliate-referred consultants at $49**, or 4 at $99 through an affiliate.

### Customer acquisition plan
1. The AI builds a **sample kit branded with each target partner's logo**, using a trade that matches their public client examples. Seeing your own name on a finished product is the pitch.
2. The sponsor sends 10–12 one-to-one emails: Sheldon Primus, 6–8 Inogen US member firms, an ASSP Consultants PS leader, and Jay Allen last.
3. A partner that agrees gets a kit: an episode or newsletter blurb, a Facebook-group post the partner writes or approves (the AI drafts it; **the partner posts it** as their own recommendation, not a bot), and an affiliate link with a founding-price code.
4. Consultants buy → add clients → kits ship monthly. Churn is low because cancelling means the consultant loses a client deliverable.
5. Once D2 has subscribers: an in-email upsell, "Turn this week's inspections into a client kit".

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **Small consulting firms (Inogen members and the sponsor's own network)** — a sample kit with their logo and a 30-day free pilot for 3 of their clients — firms decide quickly when it costs them no time — 2–4 weeks to a pilot, 5–7 weeks to paid.
2. **Sheldon Primus' podcast and group** — a host mention or guest episode, plus the group post — his audience is consultants actively building offers — 4–8 weeks, depending on his calendar.
3. **D2 cross-sell** — an upsell line in D2's daily email — zero acquisition cost, but it depends on D2 reaching subscribers — 60+ days.
4. **ASSP Consultants PS webinar slot** — a member discount — slow (association calendar), but high trust — 60–120 days.

### Path to first sale
- **Days 0–14:** D2's ingest is built under the D2 plan. C2 adds about 3 days to generate and review the 150-talk seed library and the monthly citation-brief template.
- **Days 10–18:** the AI produces 10 partner-branded sample kits. The sponsor sends the pitches (about 1 h).
- **Days 18–40:** replies come in. Expect about a 20–30% reply rate and a 10–20% agreement rate, so **10–12 pitches land 1–2 partners or firms**.
- **Days 35–55:** the first pilot converts, or the first podcast mention runs with the founding code.
- **Estimate: first sale around day 50 (range 40–80).**
- **Seasonality:** neutral to good.
  - Q4 is when consultants renew annual client contracts and budgets for 2027.
  - Winter hazards (cold, ice, holiday rush in warehousing) give timely content.
  - Northern landscaping and roofing clients slow down in Dec–Feb, so lead with year-round trades: janitorial, warehousing, light manufacturing and concrete in Sun Belt states.

### Who does what
- **AI operator:**
  - maintains the talk library, checks each talk against eCFR 29 CFR 1910/1926 text, and does a second-pass plain-field-Spanish review;
  - generates monthly citation briefs from the D2 ingest;
  - assembles and brands kits per consultant;
  - emails consultants on the 25th of each month;
  - support email;
  - partner kits and pitch drafts.
- **Human sponsor:**
  - **One-time, about 1.5 h if D2's MoR and domain already exist:** product setup and the first 10–12 pitches.
  - **Recurring, about 0.25–0.5 h/week:** partner replies, optional 30-min pilot calls (counted against budget), and one native-Spanish spot check per month by a paid freelancer (about $20/mo, optional) or by a bilingual consultant-customer in exchange for a free month.

### Moat — why not just ask ChatGPT?
- **Substitutes:**
  - Free CPWR/ASSE Spanish talks and NAWIC bilingual PDFs.
  - Insurer-provided talks.
  - AI talk generators (e.g. toolboxtalk-ai at $49/mo).
  - ChatGPT itself.
- **What none of them do:**
  - **Brand it as the consultant's work**, ready to forward every month, for every client, without the consultant touching it.
  - **Tie it to real, current OSHA enforcement in that client's industry and state**, using D2's parsed DOL data. "OSHA issued 41 fall-protection citations to roofers in Texas last month; here is this week's talk" is a reason for the client to read it. A free generic talk is not.
- **The buyer is the consultant, not the foreman.** The consultant's alternative is their own unbilled time.
- **Honest weakness:** a capable consultant could build this with ChatGPT plus D2's CSV in about 2 hours a month. The bet is that most won't.

### Biggest risks (ideator's own view)
- **Safety-content liability.** A wrong instruction in a talk could contribute to an injury. Mitigations:
  - every talk cites and paraphrases the OSHA standard;
  - the licence says the consultant reviews and adopts the content as a professional;
  - a disclaimer is included;
  - a talk is never "certified training".
  The legal-risk analyst should check this.
- **Small, slow partners.** The named safety-consultant channel owners are niche, and audience sizes are unverified. The real conversion may come one firm at a time (Inogen members), which is slower than one newsletter blast.
- **Dependence on D2.** If D2's ingest slips, C2 loses its data differentiator and becomes a generic white-label talk pack, which is weak.

---

## C3 — Interpreter Practice Lab: co-branded oral-exam and agency-test practice for Spanish medical interpreters, licensed to the trainers who teach them

- **Persona:** The Channel Partner (ideator-channel-partner)
- **One-liner:** A web app for Spanish medical-interpreter candidates. It plays realistic bilingual patient–provider dialogues, records the candidate's consecutive interpretation and sight translation, and scores accuracy, omissions and terminology in the format of the CCHI/NBCMI oral exams and agency screening tests. It is sold co-branded through the publishers, 40-hour training schools and YouTubers who already train these candidates.
- **Channel partners (named):**
  1. **Cross-Cultural Communications / Culture & Language Press.** Publisher of *The Community Interpreter®*, a 40-hour foundation programme. It has licensed **500+ trainers** across health systems, school districts, nonprofits and agencies in 44 US states. A co-branded "CLP Practice Lab" for its trainers' students is a product line it doesn't have, with no effort on its part. First contact: the sponsor emails the company directly with a demo login pre-loaded with dialogues matching its textbook chapters' topics (original content, no copied text). ([about](https://cultureandlanguage.net/about-us), [ATA listing](https://www.atanet.org/?p=37646))
  2. **Medical Interpreting Training School (MITS).** Sells a $640 self-paced Spanish 40-hour course to "thousands of bilingual students". It includes mock exams, but these are static. Our lab adds unlimited scored audio practice. Deal: a per-student licence bundled into the course, or an affiliate upsell at checkout. First contact: email through the site's student-support channel, asking for the partnerships contact. ([course page](https://medicalinterpretingtrainingschool.com/spanish-medical-interpreter-course))
  3. **InterpreMed.** A learning community for medical interpreters and students. It posts scripted dialogues and glossaries and runs weekly Zoom practice in Spanish, Portuguese, Arabic and Russian. Deal: a free perk for members (10 scored sessions), with an upsell to paid at 40% to InterpreMed. First contact: a personal email offering to auto-score the dialogues it already uses (with permission) inside the lab. ([site](https://interpremed.com/1-new-frontpage/))
  4. **Bridging Words (YouTube, about 3.1k subscribers).** Helps Spanish speakers pass the CMI (NBCMI) and CCHI tests with free study material. Deal: an affiliate link in video descriptions plus a pinned comment, at 40%. First contact: a YouTube "business inquiry" email from the sponsor with a free creator account. ([channel stats](https://vling.net/en/channel/UCsGiDGyBVRTOJ2BsV0mejBg/channel-info))
  5. **ALTA Language Services.** Runs a 40-hour course with oral exam practice in the national format. It is a long shot and a possible competitor, so it is contacted only after 2 smaller partners prove conversion. ([ALTA](https://learn.altalang.com/?p=50678))
- **Demand test:**
  - **Step 1, partner:** pitch 10 partners (the 5 above plus 5 more 40-hour providers from the CCHI/NBCMI approved-training lists) with a working demo of 10 dialogues. **Pass:** at least 2 agree to put it in front of current students (a perk, link or bundle) by day 40. **Fail:** fewer than 2.
  - **Step 2, willingness to pay:** a 30-day pass at $29 (founding price $19) offered to partner audiences. **Pass:** at least 8 paid passes in the first 21 days after the first partner promotion. **Fail:** fewer than 3.
  - **Quality gate before Step 2:** the AI's scores must agree with a human rater (a bilingual partner instructor scores 20 recordings) within ±1 point on a 5-point rubric for at least 80% of items. **If this gate fails, the idea is killed.**
- **Customer:**
  - **Who:** bilingual adults (mostly English/Spanish) who completed or are taking a 40-hour medical interpreter course and must pass:
    - (a) the CCHI CoreCHI-P/CHI-Spanish or NBCMI CMI oral exam (about $485 in exam fees at stake), or
    - (b) an agency screening test (LanguageLine's 35-minute Interpreter Skills Test and similar), to get remote OPI/VRI work.
  - **Where they are:** inside 40-hour courses, InterpreMed's Zooms, interpreter YouTube channels, and interpreter Facebook groups.
  - **What they pay for now:** courses at $300–$700, exam fees, glossaries and workbooks.
- **Problem / desire:**
  - "I know the vocabulary, but I freeze on long segments and I have no one to practise with at 10pm."
  - "I failed the oral by a few points and don't know what I'm omitting."
  - Peer Zoom practice depends on schedules, and static mock exams can't be repeated.
- **Offering:**
  - **Practice items:**
    - 150 original scripted dialogues (ER, pediatrics, oncology, discharge, mental health, insurance calls) at 3 difficulty levels, voiced with distinct TTS voices for provider and patient;
    - consecutive segments that lengthen as the candidate improves;
    - sight-translation passages (consent forms and discharge instructions written from scratch).
  - **Scoring of each recording:** transcription, then rubric scoring of meaning errors, omissions, additions, register and terminology, against a key-unit checklist written per segment. The candidate gets a per-session report and a running weak-term glossary.
  - **Co-branding:** the partner's logo and a "recommended by" line. Schools get an instructor view of student progress.
  - **Disclaimer:** it practises the *format*. It does **not** use or imitate confidential exam items, and it is not affiliated with CCHI/NBCMI.
- **Price & revenue model:**
  - Candidates: a **30-day pass at $29** (founding price $19) or **$19/mo**. Usage is capped at 120 scored segments per month.
  - Schools: **$6 per enrolled student per month**, or $150/mo flat for up to 40 students.
  - Partners get 40% of referred candidate revenue for 12 months.
- **Physical items required?** No.

### Upfront capital
| Item | Cost |
|---|---|
| Domain | $12 |
| TTS generation of 150 dialogues (~400k characters, generated once and cached) | ~$6–$12 |
| STT + scoring test runs during the calibration gate | ~$10 |
| Hosting: Cloudflare Pages/Workers + R2 for cached audio (free tier) | $0 |
| Lemon Squeezy (MoR + affiliates) | $0 |
| **Total** | **~$28–$34** |

### Monthly running costs (excluding operator tokens)
- **Per active user at the heavy cap (120 segments, about 3 min each):**
  - transcription ≈ 360 min × $0.003–$0.006 = $1.10–$2.20;
  - rubric scoring with a small model ≈ $0.60–$1.20;
  - **total ≈ $2–$3.50 per heavy user per month.** A median user is about $0.80.
- There is no realtime voice API. Recordings are uploaded per segment and scored once, which avoids lesson 7's re-billing trap.
- R2 storage: recordings are deleted after 7 days, so about $0.
- MoR: 5% + $0.50, plus 2% on affiliate orders.
- Affiliate share: 40%.
- **Unit economics:**
  - A $29 pass through an affiliate nets about $14 after inference. A direct sale nets about $25.
  - **$300/mo ≈ 22 affiliate passes, or 2 schools at $150 plus a few passes.** The school licence is the real target.

### Customer acquisition plan
1. Build a 10-dialogue demo, then 150 dialogues once Step 1 passes.
2. The sponsor pitches the 10 partners one-to-one, each with a partner-branded demo link.
3. **School and publisher deals (CCC/CLP, MITS):** the lab goes into the course as a bundled practice tool. Students arrive through the course with no marketing from us. This is the recurring revenue base.
4. **Community and creator deals (InterpreMed, Bridging Words):** a free perk of 10 scored segments, then an upsell to a 30-day pass with the partner's affiliate code.
5. Candidates who pass are asked, inside the app and on an opt-in basis, for a testimonial their trainer can share. That gives the partner a success story and so makes the partner look good.

### Initial traffic approaches (at least 3, ranked by expected speed)
1. **InterpreMed and Bridging Words** — a free perk and an affiliate link — small creators decide alone and their audience is pre-exam right now — 3–5 weeks to the first promotion.
2. **Self-paced 40-hour schools (MITS and others on the approved-training lists)** — an upsell link on the course's final-module or mock-exam page — they gain a revenue line for free — 4–8 weeks.
3. **Publisher licence (CCC/CLP, 500+ licensed trainers)** — co-branded, announced to their trainer network — the biggest reach per yes, but the slowest (a contract to sign) — 8–16 weeks.

### Path to first sale
- **Days 0–3:** sponsor setup: MoR, affiliates, domain (about 1.5 h).
- **Days 2–16:** the AI writes 30 dialogues and segment keys, voices them, and builds the recorder, scoring and report app. It tests the app on synthetic recordings.
- **Days 12–20:** partner pitches go out with the demo. The sponsor sends about 10 emails (about 1 h).
- **Days 20–40:** replies come in. Expect a 25–35% reply rate (niche educators answer, and the tool helps their pass rates) and a 15–25% agreement rate, so **about 10 pitches land 2 partners**. The calibration gate runs with a partner instructor.
- **Days 35–55:** the first perk or affiliate promotion runs, followed by the first paid passes.
- **Estimate: first sale around day 50 (range 40–85).**
- **Seasonality:** neutral. Certification exams run year-round. There is a mild January bump from new-year career changers and healthcare hiring. December is slower.

### Who does what
- **AI operator:**
  - writes and maintains original dialogues and segment keys;
  - voices them with TTS;
  - runs the scoring pipeline and calibration checks;
  - runs school dashboards and per-student reports;
  - answers support email;
  - writes partner kits, pitch drafts and monthly partner performance reports;
  - adds 10 new dialogues each month.
- **Human sponsor:**
  - **One-time, about 2.5 h:** MoR, domain, the first 10 pitches, and recruiting one bilingual instructor for the 20-recording calibration (paid with free school access, or about $40 from the upfront budget, which still keeps the total under $100).
  - **Recurring, about 0.25–0.5 h/week:** partner replies, and signing a simple school licence (a click-through order form, not a negotiated contract, wherever possible).

### Moat — why not just ask ChatGPT?
- **Free substitutes:**
  - ChatGPT voice mode can role-play a patient.
  - Free YouTube practice playlists and InterpreMed's scripts give unscored practice.
- **AI competitors:** Inter Practice (Feb 2026), TerpWise (2026), Simultalive and Interpretrain all exist, but they focus on conference simultaneous interpreting.
- **What this adds:**
  - US medical-certification and agency-test format: consecutive segments, sight translation, healthcare terminology.
  - **Consistent rubric scoring against a fixed key**, so progress is measurable session to session. A chatbot grading itself is not.
  - **Distribution through the trainer the student already paid**, which makes it part of the course rather than one more app to evaluate.
- **Honest weakness:** a larger player (ALTA, or a funded AI-interpreting startup) could add this. The partner contracts and the dialogue bank are the only defensible parts.

### Biggest risks (ideator's own view)
- **Scoring accuracy.** If the AI's scores don't match human raters, candidates and trainers will distrust it, and one bad review in a small, tight-knit community spreads fast. The calibration gate is a hard kill switch.
- **Small market.** CoreCHI is taken about 1,000 times a year (CCHI annual reports), and oral exams are a similar order of magnitude. Agency-test candidates are the larger pool but harder to reach. Revenue depends on landing 1–2 school licences, not on retail passes.
- **Exam-content and trademark exposure.** Any resemblance to confidential CCHI/NBCMI items, or marketing that implies endorsement, invites a cease-and-desist. Mitigations: all content is original; "CCHI" and "NBCMI" appear only in descriptive, nominative use; a clear disclaimer; and voice recordings are deleted after 7 days under a plain privacy notice.

---

### Sources checked (2026-10-06)
- Grant: [Instrumentl pricing 2026 (Grantable guide)](https://grantable.co/best-instrumentl-alternatives), [GrantSights Instrumentl vs Candid](https://grantsights.com/blog/instrumentl-vs-candid-2026), [Instrumentl partners](https://instrumentl.com/partners), [Grantmakers.io (GitHub)](https://www.github.com/grantmakers), [ProPublica Nonprofit Explorer API](https://www.propublica.org/nerds/announcing-the-nonprofit-explorer-api), [Apify 990-PF prospector](https://apify.com/immense_greenery/foundation-grant-prospector), [Grant Writing & Funding podcast](https://podcasts.apple.com/podcast/id1235917132), [Grant Writing Academy Substack](https://substack.com/@grantwritingacademy), [Gladiator Grant Writing](https://gladiatorgrantwriting.substack.com).
- Safety: [The Safety Consultant Podcast](https://share.transistor.fm/s/0d9decab), [ASSP Consultants Practice Specialty](https://www.assp.org/membership/communities/practice-specialties/consultants), [Inogen Alliance podcast](https://www.3blmedia.com/news/inogen-alliance-launches-season-2-global-podcast-rethinking-ehs), [Safety FM ad page](https://advertising.libsyn.com/SafetyFM), [NAWIC free bilingual talks](https://nawic.org/safety-toolbox-talks/), [NRCA Toolbox Talks pricing](https://www.nrca.net/RoofingNews/nrca-offers-toolbox-talks-publication.12-9-2019.8205/details/story).
- Interpreting: [Culture & Language Press about](https://cultureandlanguage.net/about-us), [MITS course](https://medicalinterpretingtrainingschool.com/spanish-medical-interpreter-course), [InterpreMed](https://interpremed.com/1-new-frontpage/), [Bridging Words stats](https://vling.net/en/channel/UCsGiDGyBVRTOJ2BsV0mejBg/channel-info), [ALTA training](https://learn.altalang.com/?p=50678), [CCHI 2022 annual report](https://cchicertification.org/uploads/2022-CCHI_Annual_Report.pdf), [Inter Practice](https://mwm.ai/apps/inter-practice/6759309847), [TerpWise](https://www.startuphub.ai/startups/terpwise.md).
- Payments: [Lemon Squeezy / Stripe Managed Payments status 2026](https://fungies.io/lemon-squeezy-stripe-acquisition-saas-founders-2026/), [Lemon Squeezy affiliate fee](https://learnwithhasan.com/payment-gateways/lemonsqueezy/).
