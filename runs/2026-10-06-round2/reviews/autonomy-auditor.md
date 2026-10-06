# Autonomy Audit — 2026-10-06, round 2

_Reviewer: autonomy-auditor. Scale: 10 = < 2 h one-time human setup and ~0 h/week ongoing; 1 = a human is needed daily or for every sale. Hours are my estimates of real sponsor time, including tasks the ideators left out. Rubric hard gate: > 3 h/week recurring. Partner-led ideas are shown with two recurring figures: the launch/outreach phase and the steady state._

| ID | Idea | Score | Human setup hrs (one-time) | Human hrs/week ongoing | Hard gates | Scales without humans? |
|---|---|---|---|---|---|---|
| G1 | Keyword→Brief Apify Actor | 8 | 1.5–2 (0.5–0.75 if the Apify account already exists) | 0.1–0.25 | Apify KYC (photo ID) + payout method; DataForSEO signup + $50 card deposit; written resale OK from DataForSEO (go/no-go decision is human) | Yes. Only risk: the prepaid DataForSEO balance must be topped up by a human card, or runs fail. |
| G2 | LongForm Transcripts Apify Actor | 8 | 1–1.5 (0.5 if Apify exists) | 0.1–0.25 | Apify KYC; Groq + OpenAI billing (cards); DMCA agent designation (recommended) | Yes. Rights complaints grow slowly with volume and need human sign-off. |
| G3 | AnswerShare API (MCPize + RapidAPI) | 7 | 2.5–3.5 | 0.25–0.5 | RapidAPI provider + PayPal + tax form; MCPize Stripe Connect KYC; 3 AI-provider billing accounts; MCP Registry namespace auth | Yes. Per-check billing is self-serve. Check the Gemini grounding display/storage terms. |
| C1 | FunderFit via grant-writing academies | 6 | 3–4 | 1–1.5 (weeks 1–10), then 0.25–0.5 | Lemon Squeezy KYC; every partner pitch, reply and agreement is human; podcast guest spot needs the sponsor's voice | Mostly. Fulfilment is AI. Partner count drives human time, and so do manual affiliate payouts if LS Affiliates goes away. |
| C2 | Client Safety Kit via safety consultants | 5 | 2.5–3.5 (1.5 if D2's MoR and domain exist) | 1–1.5 (weeks 1–10), then 0.5 | LS KYC; depends on D2 being built; firm-licence agreements; ASSP access needs membership (dues above the $100 cap); monthly Spanish QA by a paid human | Partly. Consulting firms buy via calls and pilots, and each firm deal adds human time. |
| C3 | Interpreter Practice Lab via trainers | 5 | 4–6 | 1–1.5 (weeks 1–10), then 0.5 | LS KYC; a calibration gate that needs a human rater **and ~20 real human candidate recordings**; publisher/school licence contracts | Retail passes, yes. School and publisher deals, no: each needs a contract or invoice. |
| I1 | Zì Bot (Discord) | 6 | 3.5–4.5 (split: ~2.5 now, ~1.5 at 76 servers) | 0.5–1 (weeks 1–6), then 0.25 | LS KYC; Discord team + 2FA; **bot capped at 100 servers until the owner passes Stripe Identity verification**; Premium Apps onboarding (monetisation terms, payout KYC) | Growth stops at 100 servers until a human verifies; after that, yes. Admin outreach must be done by the sponsor's own Discord account. |
| I2 | Episode Study Packs for creators | 7 | 2–2.5 | 0.5–0.75 (outreach weeks), then 0.25–0.5 | LS KYC; a real sending mailbox (transactional ESPs forbid cold outreach); CAN-SPAM postal address | Yes. Packs are AI-made and the creator does native QA. |
| I3 | Role-Play Room for Chinese classes | 5 | 2.5–3 | 0.5–1 in season, **plus 0.5–1.5 h per institutional buyer** | LS KYC; university vendor/supplier registration and W-9; HECVAT/VPAT/DPA requests that only the sponsor can attest or sign | No for department-paid classes, since paperwork is per institution. Mostly yes for the student-pays seat model. |
| M1 | ChatRelay for Jira (Forge) | 7 | 3–4, plus **~3 weeks of partner-verification wait** | 0.1–0.25 | Atlassian partner identity form (via an ECOHELP ticket), W-9/W-8BEN, bank details, Partner Agreement, security questionnaire; app approval (10–15 business days per docs); Google Workspace test space | Yes. Atlassian handles billing, tax and refunds. |
| M2 | SpecView for Confluence (Forge) | 6 | 3–4 standalone (~0.25 if M1's partner account is done) | 0.25–0.5 | Same Atlassian gates as M1; human approval for conversions over 500 pages; human handling of any "you broke our pages" incident | Mostly. Large-site conversions add a human approval per customer. |
| M3 | SheetSync Apify Actor | 9 | 0.5–1.25 | ~0.1 | Apify KYC (0 if shared); Google Cloud project on a phone-verified Google account; Sheets quota-increase request | Yes. This is the most autonomous idea in the round. |
| U4 | AI-matched job board | 3 (5–6 if seeker-pays, no employer side) | 2.5–3.5 | 2–4+ with the employer side; 0.5–1 seeker-only | Payment KYC; human-only community promotion; employer sales calls, invoices, and moderation of scam/discriminatory posts; resume-data controller duties | No. Employer revenue needs human selling and moderation that grow with posts. **It risks the > 3 h/week hard gate.** |

**Ranking by autonomy:** M3 (9) > G1, G2 (8) > G3, I2, M1 (7) > C1, I1, M2 (6) > C2, C3, I3 (5) > U4 (3).

---

## Cross-cutting findings

1. **Partner and 1:1 outreach hours are under-counted in every C-idea and in I2/I3.** Ideators count only the *send* time (about 1 h for 10–12 emails). The real work is:
   - reviewing 10–12 personalised drafts (5–10 min each);
   - 2–4 reply exchanges per interested partner;
   - follow-ups to non-responders;
   - agreeing affiliate terms in writing;
   - partners asking for a call (30 min each; podcast and association people often prefer calls);
   - a second wave of pitches when the first wave yields under 2 partners.

   With a 25% reply rate across two waves, that is about 6–10 live threads. **Realistic load: 1–1.5 h/week for weeks 1–10, then 0.25–0.5 h/week.** This stays under the 3 h gate but is above the 1 h ideal, so these ideas score 5–6.
2. **Outreach emails cannot go through transactional ESPs.** Resend, SendGrid, Postmark and similar services prohibit unsolicited and cold mail in their acceptable-use policies. Cloudflare Email Routing only receives mail. Any AI-sent 1:1 outreach (I2, I3, U4) therefore needs a real mailbox, which means a Google or Microsoft account (phone verification, human) or a paid mailbox. CAN-SPAM also requires a valid physical postal address in each commercial email: the sponsor's own address, or a virtual mailbox that costs money.
3. **Apify payout setup (G1, G2, M3):**
   - The one-time steps are billing details, a payout method (PayPal or Wise, $20 minimum; other methods $100) and KYC (legal name matching the ID, plus a high-resolution photo of the ID). Changing billing details beyond the payout method forces a repeat of KYC.
   - Invoices are issued on the 11th and **auto-approve on the 14th**, so there is no monthly human action.
   - All Apify ideas plus T2 can share one KYC'd account. That costs 0 extra setup hours but concentrates the risk (lesson 4).
4. **Atlassian partner onboarding (M1, M2) is heavier and slower than the ideator says.**
   - Paid-via-Atlassian needs an identity-information form, submitted through an ECOHELP ticket: name, DOB, home address, tax ID, sole-proprietor confirmation.
   - It also needs the Marketplace security questionnaire, a W-9 (US) or W-8BEN (non-US; otherwise there is 30% default withholding), bank details, and acceptance of the Partner Agreement.
   - One individual developer reported about **3 weeks** for verification (Aug 2026).
   - The app approval docs say **10–15 business days**, not 5–10.
   - Bug-bounty participation is a membership-tier obligation (Silver and above), not an entry requirement. However, the minimum cloud security requirements, the Privacy & Security tab and security-fix obligations apply to every app.
5. **Discord app verification (I1).**
   - A bot qualifies at 76 servers and **cannot join more than 100 servers unverified**.
   - Verification needs the team owner's ID through Stripe Identity plus an operations questionnaire.
   - Monetisation additionally needs: a verified app, a developer team, an owner aged 18+ in a supported locale, verified email and 2FA for every team member, and acceptance of the Monetization Terms.
   - It is a gate that fires mid-growth, not at setup.

---

## G1 — Keyword→Brief (Apify) — Score 8

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | Apify account, billing details, PayPal/Wise, KYC (photo ID) | Human-once (0.75–1 h; 0.1 h if shared with T2) | Required before any payout. |
| 1 Setup | DataForSEO account + $50 card deposit | Human-once (0.25–0.5 h) | A card is needed, and new accounts may be screened. |
| 1 Setup | Read DataForSEO's resale reply; make the go/no-go call | Human-once (0.25 h) | **Hard gate.** Without a yes, the plan falls back to BYO-key. |
| 2 Build | Actor, self-tests, schemas | AI | |
| 3 Launch | Publish to the Store with PPE pricing | AI | No human review queue. Accepting the publishing and monetisation terms is a click by the account owner. |
| 4 Marketing | Store SEO, MCP metadata | AI | |
| 4 Marketing | n8n creator account + template submission | Human-once (0.25 h) if signup hits a CAPTCHA; otherwise AI | n8n reviews templates. |
| 4 Marketing | Apify Discord #showcase post | Human-once (0.1 h) | Posting must come from a human Discord account, not a bot. |
| 5 Each sale | PPE billing | AI/platform | |
| 6 Support | Apify issue threads | AI | |
| 7 Maintenance | Nightly self-test, pricing | AI | |
| 7 Maintenance | **DataForSEO balance top-ups** | Human-recurring (0.1–0.2 h/wk) | Prepaid COGS on the sponsor's card. Turn on auto-recharge if it is offered. |
| 8 Finance | Invoice auto-approves; income tax | Human (~0.05 h/wk) | |

**Hard gates:** Apify KYC; DataForSEO deposit and resale permission.
**Platform policies:** none on Apify. DataForSEO ToS §7.1 is the supplier risk: a suspension stops every run at once.
**Scaling cliff:** None in labour. COGS grows with volume, so the top-up frequency grows unless auto-recharge exists.

## G2 — LongForm Transcripts (Apify) — Score 8

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | Apify KYC/payout | Human-once (0.75–1 h; 0.1 h if shared) | |
| 1 Setup | Groq card (postpaid), OpenAI $5 credit | Human-once (0.25 h) | Enable OpenAI auto-recharge, or the fallback will silently die. |
| 1 Setup | DMCA designated agent ($6, US Copyright Office) | Human-once (0.25 h) | Recommended. The filing names the sponsor. |
| 2 Build | ffmpeg chunking, ASR, outputs | AI | |
| 3 Launch | Publish | AI | |
| 4 Marketing | Store SEO, n8n/Make templates | AI (+0.25 h human if n8n/Make signups hit a CAPTCHA) | The ideator correctly makes the *sponsor* post any LinkedIn drafts. Keep those out of the operator. |
| 5 Each sale | Per-minute billing | AI/platform | |
| 6 Support | Issues | AI | |
| 6 Support | **Rights or privacy complaints** (someone else's podcast, meeting recordings with personal data) | AI drafts; Human approves (rare, ~0.1 h/wk averaged) | The sponsor is the legal respondent. |
| 7 Maintenance | WER drift, Groq availability | AI | |
| 8 Finance | Auto-approved invoices | Human (~0.05 h/wk) | |

**Hard gates:** Apify KYC; provider billing.
**Platform policies:** Clean, because YouTube/TikTok/IG downloading is excluded. Keep it excluded: platform downloaders breach those platforms' terms and attract complaints.
**Scaling cliff:** Small. Complaint volume rises with minutes processed, but the block-on-complaint policy keeps each one to minutes of human time.

## G3 — AnswerShare API — Score 7

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | RapidAPI provider account, PayPal payout, tax form | Human-once (0.75 h) | |
| 1 Setup | MCPize account + Stripe Connect KYC | Human-once (0.5–0.75 h) | |
| 1 Setup | OpenAI, Perplexity, Google AI Studio billing | Human-once (0.5–0.75 h) | Three cards/accounts. Enable auto-recharge on the two prepaid ones. |
| 1 Setup | Official MCP Registry namespace (GitHub or DNS auth), glama/PulseMCP/mcp.so submissions | Human-once (0.25–0.5 h) | GitHub login or CAPTCHA forms. A GitHub org owned by the sponsor is cleanest. |
| 2 Build | Worker, D1, 3 engine adapters | AI | |
| 3 Launch | Listings | AI | MCPize review time is unknown. |
| 4 Marketing | Sample report page, n8n template | AI | No social posting (correct). |
| 5 Each sale | Free key → paid plan, all self-serve | AI/platform | |
| 6 Support | Email support | AI | |
| 6 Support | RapidAPI refund or dispute requests | Human approves (~0.1 h/wk) | |
| 7 Maintenance | Engine API drift, cost dashboard | AI | |
| 8 Finance | Two payout streams, both slow; check whether MCPize acts as merchant of record (unverified) | Human (~0.1 h/wk) | If neither acts as MoR for MCPize sales, sales tax and VAT fall on the sponsor. |

**Hard gates:** two marketplace KYCs plus three provider accounts. This is the heaviest setup of the agent ideas.
**Platform policies:** the Gemini "Grounding with Google Search" terms include display and storage conditions. Reselling grounded answers through an API, and keeping 12 months of history, needs a legal check. Label the OpenAI results "API, not consumer ChatGPT", as the ideator plans.
**Scaling cliff:** None in labour.

## C1 — FunderFit — Score 6

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | LS store + KYC, Affiliates, domain | Human-once (1.25–1.5 h) | Lemon Squeezy's move to Stripe Managed Payments (which has no affiliate tool) may force a later re-onboarding. |
| 2 Build | 990-PF parse, ranking, report generator, 12 sample reports | AI | |
| 3 Launch | Checkout, intake form | AI | |
| 4 Marketing | Review and send 12 personalised partner emails from the sponsor's address | Human-once (1.5–2 h, not 1 h) | Drafts need human judgement of tone with named people. |
| 4 Marketing | Reply threads, follow-ups, second wave, written affiliate terms | **Human-recurring (1–1.5 h/wk, weeks 2–10)** | This is the main hidden load. |
| 4 Marketing | Podcast guest spot | Human-once (1–1.5 h incl. prep and scheduling) | Needs the sponsor's voice. The AI cannot appear. |
| 5 Each sale | Form → report → delivery | AI | No per-sale human. |
| 6 Support | Freelancer questions, "this funder is wrong" | AI | Refund approvals by the human, rare. |
| 7 Maintenance | Quarterly IRS refresh, 1-in-10 QA | AI | |
| 8 Finance | LS MoR; affiliate payouts automated, or **manual PayPal if LS Affiliates goes away** (0.25 h/month, grows with partners) | Human (~0.1 h/wk) | |

**Hard gates:** LS KYC; human-only partner relationships.
**Platform policies:** Substack DMs (Queen Israel, Camille Ricks) must come from the sponsor's own account, and Substack has no API. The partner, not us, posts in member communities. Good.
**Scaling cliff:** Fulfilment is flat. Partner management grows with the number of partners, about 10–15 min/month each once they are live.

## C2 — Client Safety Kit — Score 5

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | LS (shared with D2) + product, domain | Human-once (0.5–1.5 h) | **Depends on D2 existing.** If D2 isn't run, add the full LS setup and the DOL key. |
| 1 Setup | Arrange a native-Spanish reviewer (freelancer or customer swap) | Human-once (0.5 h) | |
| 2 Build | 150-talk library, citation brief, branding pipeline | AI | |
| 4 Marketing | 10–12 partner-branded pitches (Primus, Inogen firms, ASSP, Allen) | Human-once (1.5–2 h) | Inogen member firms are B2B consultancies and expect a call. |
| 4 Marketing | Replies, **pilot calls (30 min each, 2–4 expected)**, follow-ups | **Human-recurring (1–1.5 h/wk, weeks 2–10)** | |
| 4 Marketing | ASSP Consultants PS webinar | Human (1 h incl. prep) | Live human presence. ASSP membership dues are above the $100 cap, so this needs an existing member. |
| 4 Marketing | $199 firm licence | Human-once per firm (0.5 h) | Firms ask for a written agreement. |
| 5 Each sale | Consultant uploads a logo → monthly kits on the 25th | AI | |
| 6 Support | Content questions | AI; Human for any injury or "your talk was wrong" claim (rare, serious) | |
| 7 Maintenance | Monthly Spanish spot check (paid freelancer, ~$20) | Human-recurring (0.1 h/wk to pay and coordinate) | |
| 8 Finance | LS MoR, affiliates | Human (~0.1 h/wk) | |

**Hard gates:** D2 dependency; LS KYC; human-only consultant selling.
**Platform policies:** the partner posts in Facebook groups (correct). No bot posting.
**Scaling cliff:** Partial. Individual consultants are self-serve, but firm deals and pilots each cost human time.

## C3 — Interpreter Practice Lab — Score 5

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | LS + affiliates, domain | Human-once (1.25–1.5 h) | |
| 2 Build | Dialogues, TTS, recorder, scoring | AI | |
| 2 Build | **Calibration gate: recruit a bilingual instructor, and source ~20 real candidate recordings** (AI cannot generate human interpreting performances honestly) | Human-once (1.5–2.5 h) | **Hard gate.** Get consent to keep the labelled set as a regression suite, so later model changes do not need a new human round. |
| 4 Marketing | 10 pitches with demo links | Human-once (1–1.5 h) | |
| 4 Marketing | Replies, follow-ups, demo calls with school owners | **Human-recurring (1–1.5 h/wk, weeks 3–12)** | |
| 4 Marketing | Publisher licence (CCC/CLP) or MITS bundle: contract negotiation and signature | Human-once per deal (1–2 h) | A contract is unavoidable for a per-student bundle. |
| 5 Each sale | Retail pass via LS | AI | |
| 5 Each sale | School licence: invoices, W-9, sometimes POs | Human (0.25–0.5 h per school) | |
| 6 Support | Score disputes ("I failed the real exam") | AI; Human approves refunds | |
| 7 Maintenance | 10 new dialogues a month | AI | |
| 8 Finance | LS MoR | Human (~0.1 h/wk) | |

**Hard gates:** human calibration data; contracts with schools or publishers.
**Platform policies:** none of note. YouTube creator deals are human-to-human.
**Scaling cliff:** Retail passes scale. The revenue plan rests on school licences, and each one adds paperwork.

## I1 — Zì Bot — Score 6

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | LS KYC, domain | Human-once (1.25 h) | |
| 1 Setup | Discord developer team, owner 2FA, verified email | Human-once (0.5 h) | All team members need 2FA. |
| 1 Setup | top.gg / discordbotlist / discord.bots.gg submission (OAuth login with the owner's Discord) | Human-once (0.5 h) | Directory review queues apply. |
| 2 Build | Workers interactions endpoint, quiz, dictionary, `/practice` | AI | |
| 4 Marketing | **Messages to server admins asking permission** | Human-recurring (0.5–1 h/wk, weeks 2–6) | Discord bans self-bots and unsolicited bot DMs. Only the sponsor's real account can do this. |
| 4 Marketing | One r/ChineseLanguage post | Human-once (0.5 h incl. replies) | |
| 3 Launch (later) | **Verification at 76 servers: Stripe Identity + questionnaire** | Human-once (0.5–1 h) + a review wait | **Hard gate: the bot cannot pass 100 servers until this is done.** |
| 3 Launch (later) | Premium Apps onboarding: monetisation terms, team payout and tax setup | Human-once (0.5–1 h) | Payment parity then forces SKUs on Discord as well as LS. |
| 5 Each sale | LS checkout or Discord SKU | AI/platform | |
| 6 Support | `/feedback`, inbox | AI | |
| 6 Support | Discord T&S reports, user-generated Server Pro decks | AI moderation; Human for T&S escalations (rare) | |
| 7 Maintenance | Prompt caps, Discord API changes | AI | |
| 8 Finance | Two revenue streams (LS + Discord) | Human (~0.1 h/wk) | |

**Hard gates:** LS KYC; Discord verification (mid-growth); Premium onboarding.
**Platform policies:** no automated promotion on Discord or Reddit. The sponsor must disclose being the maker. Label AI corrections. The 18+ paid tier needs at least an attestation step at checkout.
**Scaling cliff:** none per user, apart from the one-time 100-server wall.

## I2 — Episode Study Packs — Score 7

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | LS KYC, domain | Human-once (1.25 h) | |
| 1 Setup | **Sending mailbox** (Google Workspace or Microsoft account, phone-verified) + CAN-SPAM postal address | Human-once (0.5 h) | ESPs such as Resend ban cold outreach. A virtual mailbox address costs money. |
| 1 Setup | Approve the template and the first 5 sends | Human-once (0.5 h) | |
| 2 Build | ASR → pinyin → PDF/apkg/Pleco pipeline; CC samples | AI | |
| 4 Marketing | 40–120 1:1 emails, ≤ 5/day | AI sends in the sponsor's name | Emails must not imply a human wrote each one if one did not. |
| 4 Marketing | Replies that want "the person": calls, partnership or rev-share talks | **Human-recurring (0.5–0.75 h/wk, weeks 2–5)** | Under-counted by the ideator (0.25). |
| 5 Each sale | Pack generation, revisions | AI | Require the creator to upload audio or a script. **Do not download from YouTube links**, which breaches YouTube's terms. |
| 6 Support | Quality complaints under the creator's brand | AI; Human for refunds | |
| 7 Maintenance | Dictionary and polyphone fixes | AI | |
| 7 Maintenance | Weekly pack spot-check (dogfooding) | Human-recurring (0.25 h/wk) | |
| 8 Finance | LS MoR | Human (~0.05 h/wk) | |

**Hard gates:** LS KYC; a real mailbox.
**Platform policies:** CAN-SPAM-compliant B2B outreach is lawful at this volume. Fiverr is correctly deferred, because it has no messaging API.
**Scaling cliff:** None. The market is small (100–200 creators), so outreach is finite.

## I3 — Role-Play Room — Score 5

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | LS KYC, domain, review of ToS/privacy | Human-once (1.75–2 h) | |
| 1 Setup | Sending mailbox + postal address | Human-once (0.5 h) | |
| 2 Build | PWA, dashboard, caps | AI | |
| 4 Marketing | 60 instructor emails | AI sends; Human approves the template (0.25 h) | |
| 4 Marketing | Instructor replies and **demo-call requests** (faculty often want a Zoom) | **Human-recurring (0.5–1 h/wk, Oct–Dec; again Jul–Aug)** | |
| 5 Each sale | Instructor card purchase via LS | AI | Many departments cannot pay by card. |
| 5 Each sale | **University vendor or supplier-portal registration, W-9, PO, invoice** | **Human per institution (0.5–1.5 h)** | Hidden per-sale cost. |
| 6 Support | Student support | AI | |
| 6 Support | **HECVAT security questionnaire, VPAT/accessibility report, DPA/FERPA addendum** | Human attests or signs (1–3 h each when requested) | The ideator's "decline" option loses the sale. |
| 7 Maintenance | Semester purge, accessibility fixes | AI | |
| 8 Finance | LS MoR | Human (~0.1 h/wk) | |

**Hard gates:** institutional procurement and compliance paperwork that only the sponsor can sign.
**Platform policies:** Reddit or teacher-forum posts by the sponsor only.
**Scaling cliff:** **Yes, for department-paid classes.** Switching to student-paid seats removes most of it, which would raise the score to about 6–7.

## M1 — ChatRelay for Jira — Score 7

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | Atlassian ID, developer console, partner profile | Human-once (0.5 h) | |
| 1 Setup | **Partner verification: identity form via an ECOHELP ticket (name, DOB, home address, tax ID), W-9/W-8BEN, bank details, Partner Agreement** | Human-once (1–1.5 h) + **~3 weeks of waiting** (reported Aug 2026) | **Hard gate** before a paid listing. The ideator's "days 0–2" is optimistic. |
| 1 Setup | Marketplace security questionnaire, privacy policy sign-off | AI drafts; Human attests (0.5 h) | |
| 1 Setup | Google Workspace test space (a trial needs a card and a domain; cancel it later) | Human-once (0.5 h) | |
| 2 Build | Forge app, automation action | AI | |
| 3 Launch | App approval: **10–15 business days per the docs** | AI submits; Human answers reviewer questions (0.25 h) | Listing date ≈ day 25–40, not 17–31. |
| 4 Marketing | Listing SEO, troubleshooting pages | AI | |
| 4 Marketing | Atlassian Community answers (optional) | Human (0.1–0.25 h/wk) | Disclosed human only. |
| 5 Each sale | Evaluation → paid via Atlassian | Platform | |
| 6 Support | Support inbox | AI | Refunds are handled by Atlassian. |
| 7 Maintenance | Forge/API changes; **security-fix obligations and Atlassian scanner tickets** | AI; Human for portal logins and 2FA (0.1 h/wk) | |
| 8 Finance | $500 payout threshold; Atlassian handles tax | Human (~0.05 h/wk) | Pricing changes need the partner admin login. |

**Hard gates:** partner verification and tax forms; app approval.
**Platform policies:** no bot posting in Atlassian Community. "Runs on Atlassian" eligibility with Google webhook egress is unverified.
**Scaling cliff:** None.

## M2 — SpecView for Confluence — Score 6

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | Same Atlassian partner verification as M1 | Human-once (3–3.5 h standalone; ~0.25 h if M1 has done it) | The ~3-week wait applies if this is run first. |
| 2 Build | Macro; storage-format capture from the orphan apps' trials; converter | AI | |
| 3 Launch | App approval (10–15 business days); approval again for the converter version if its permissions change (write scopes) | AI; Human for reviewer emails (0.25 h) | Adding `write:confluence-content` scopes forces customers to re-consent. |
| 5 Each sale | Evaluation → paid | Platform | |
| 5 Each sale | **Approve conversions over 500 pages** | Human per large customer (0.1–0.25 h each) | Designed-in per-sale gate. |
| 6 Support | **"The converter broke our pages" incidents** | AI rolls back; Human owns customer comms and liability (rare, urgent) | |
| 7 Maintenance | Regression suite | AI | |
| 8 Finance | As M1 | Human (~0.05 h/wk) | |

**Hard gates:** as M1, plus the converter safety gate.
**Platform policies:** listing copy that names competitors' products must stay within Atlassian's listing rules.
**Scaling cliff:** Mild. Large-site approvals grow with the number of enterprise customers.

## M3 — SheetSync (Apify) — Score 9

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | Apify KYC/payout | Human-once (0.75–1 h; 0 if shared) | |
| 1 Setup | Google Cloud project, Sheets API, service account (a new Google account needs phone verification) | Human-once (0.25 h) | |
| 1 Setup | Sheets quota-increase request | Human-once (0.1–0.25 h) | Google may ask for justification or a billing account. |
| 2 Build | Actor, retries, canary | AI | |
| 3 Launch | Publish, integration-ready | AI | |
| 4 Marketing | Store SEO, README templates | AI | |
| 4 Marketing | Apify Discord post | Human-once (0.1 h) | |
| 5 Each sale | PPE | Platform | |
| 6 Support | Issues | AI | |
| 7 Maintenance | Daily canary, key rotation | AI | The shared service account can read every customer's shared sheet. A key leak is the sponsor's liability, so rotate keys and store them in Apify secrets. |
| 8 Finance | Auto-approved invoices | Human (~0.05 h/wk) | |

**Hard gates:** Apify KYC; Google Cloud account.
**Platform policies:** none.
**Scaling cliff:** None in labour. Throughput is capped by the per-project Sheets quota until a human gets an increase.

## U4 — AI-matched job board — Score 3 (5–6 seeker-pays only)

| Stage | Step | Who | Notes |
|---|---|---|---|
| 1 Setup | Payment KYC (LS/Stripe), domain | Human-once (1.25 h) | |
| 1 Setup | Email provider for alerts: domain verification, plus a possible manual review for volume | Human-once (0.25–0.5 h) | |
| 1 Setup | Privacy posture as data controller for resumes (GDPR/CCPA), approval of the ToS | Human-once (0.5–1 h) | |
| 2 Build | ATS feed ingest (Greenhouse/Lever/Ashby public APIs), USAJobs key, matching | AI | |
| 4 Marketing | **Community show-and-tell posts (job-seeker subreddits and Discords ban bot promotion)** | Human-recurring (0.5–1 h/wk, open-ended) | Programmatic SEO needs 3–6+ months and competes with Indeed and Google for Jobs. |
| 5 Each sale (employer) | **Employer sales conversations, demos, invoices, POs** | **Human-recurring (1–3 h/wk)** | The idea itself says "if employers want a human". They do. |
| 5 Each sale (employer) | **Moderation of fake, scam or discriminatory postings** | Human-recurring (0.25–0.5 h/wk, grows with posts) | Needs human judgement. |
| 6 Support | Seeker support, data deletion requests | AI | |
| 6 Support | Employer refunds ("no applicants") | Human | |
| 7 Maintenance | Feed breakage, dedupe, expiry | AI | |
| 7 Maintenance | NYC LL144 bias audit, if employers use the rankings to screen | Human (paid auditor) | |
| 8 Finance | MoR for seekers; employer invoicing | Human (0.1–0.25 h/wk) | |

**Hard gates:** employer-side human selling and moderation. Recruitment AI is in the EU AI Act's high-risk category.
**Platform policies:** promotion on Reddit, LinkedIn and Discord must be human-only. No LinkedIn or Indeed scraping.
**Scaling cliff:** **Yes.** As proposed it likely breaks the > 3 h/week gate once employers pay. The seeker-subscription-only variant drops recurring time to 0.5–1 h/week, but still needs a human for marketing.

---

## Sources (checked 2026-10-06)
- Apify payouts (billing, KYC, PayPal/Wise $20 minimum, auto-approval on the 14th): https://docs.apify.com/platform/actors/publishing/monetize/monthly-payouts
- Atlassian individual-partner verification (ECOHELP identity form, W-8BEN, ~3 weeks): https://community.developer.atlassian.com/t/individual-developer-no-registered-company-whats-the-minimum-verification-needed-to-publish-a-paid-via-atlassian-app/102404
- Atlassian app approval (10–15 business days): https://developer.atlassian.com/platform/marketplace/app-approval-guidelines/
- Atlassian security requirements: https://developer.atlassian.com/platform/marketplace/security-requirements/
- Atlassian bug bounty by partner tier: https://developer.atlassian.com/platform/marketplace/atlassian-marketplace-security-bug-bounty-program/
- Atlassian security enforcement: https://developer.atlassian.com/platform/marketplace/marketplace-security-enforcement-policy/
- Discord verification (76/100 servers, Stripe Identity): https://support-dev.discord.com/hc/articles/23926564536471
- Discord monetisation eligibility: https://docs.discord.com/developers/monetization/enabling-monetization
- Discord Premium Apps onboarding: https://support-dev.discord.com/hc/en-us/articles/17708927296663-Premium-Apps-Onboarding

_Not verified: DataForSEO new-account screening and auto-recharge; whether MCPize acts as merchant of record; the exact Gemini grounding display and storage terms; n8n/Make creator signup CAPTCHAs; Atlassian security-fix SLA durations._
