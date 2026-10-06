# Lessons Learned from Earlier Runs

Every ideator must read this file and apply it. Every evaluator should check ideas against it.
These are the failure patterns the evaluation panel found in earlier runs.

## Run 2026-10-06: 15 ideas, plus 3 user ideas
Results:
- The best composite was 6.20/10, and no idea scored above 6 on sale plausibility.
- 13 of 15 ideas had a P90 time to first sale of "never".

### 1. Distribution is the binding constraint, not the product
- Most ideas had a credible product and buyer but **no channel that reaches the buyer within 30 days**.
- **Name the channel concretely.** That means a marketplace with built-in search and billing, or a named partner who already owns the audience. "SEO", "post in Facebook groups" and "LinkedIn" are not plans.
- The fastest idea (an Apify Store Actor) was fast because **the marketplace provided both discovery and billing**.

### 2. Ideators underestimate time to first sale by 3–5×
- Count from **today**, not from launch. Include build time, marketplace review queues, trial periods and payout delays.
- Assume a new seller account with zero reviews.

### 3. Timing and seasonality matter
- Check where the launch month sits in the buyer's yearly cycle.
- Earlier ideas launched into troughs:
  - lawn care in November;
  - weddings off-season;
  - HOA annual meetings, which fall in January–March.

### 4. Don't concentrate on one platform account
- 7 of 15 ideas depended on a single Etsy account. Etsy has no messaging API (so a human must answer every message). Off-platform upsells break Etsy's fee-avoidance rule.
- One suspension would kill everything on that account.

### 5. Known platform blockers
| Platform | Blocker |
|---|---|
| Substack | No publishing API |
| Pinterest | Auto-pinning is banned |
| TPT | No upload API |
| Reddit, LinkedIn, X | Bot-run promotion gets accounts banned. Only the human can post, and only as genuine participation. |
| Apple and Google app stores | Developer fees of $99 and $25 plus the domain exceed the $100 cap |
| Email providers | Daily send caps on free tiers (e.g. 100/day) |

### 6. "Cheaper than a human" is not a differentiator
Buyers compare against **other AI products and free chatbots**, not against human labour. Name the free or AI substitute and say why the buyer pays anyway.

### 7. Inference cost per user is real
For AI-heavy consumer products (voice especially), model the cost per active user at heavy usage and plan usage caps. Realtime voice APIs re-bill the whole conversation on every turn.

### 8. Validate willingness to pay before building
No idea included a $0 pre-sale, a test listing or a deposit waitlist. Every idea must now include a **demand test**: what is offered, to whom, through which channel, and the pass/fail number.

### 9. Ideators converged on one pattern
6 of 15 ideas were "public government records → paid feed". These have a real data moat but no buyer channel. Avoid that pattern unless the channel is solved.

### 10. Ideas already evaluated: do not resubmit
| ID | Idea | Outcome |
|---|---|---|
| T1 | RainCheck for Jobber | |
| T2 | Accela/EnerGov permit Actor on Apify | Pick #2 |
| T3 | TipSplit for Clover | |
| W1 | Federal janitorial bid digest | |
| W2 | Florida HOA letter kit | |
| W3 | State grant calendar | |
| A1 | AI house portraits | |
| A2 | Kids' wedding activity book | |
| A3 | Personalised visual schedules | |
| D1 | Translation tender alerts | |
| D2 | OSHA inspection alerts | Pick #1 |
| D3 | TTB label intel | |
| S1 | Airbnb guidebooks | |
| S2 | Bilingual toolbox talks | |
| S3 | Custom wedding toasts | |
| U1 | OSRS GE flip advisor | No-go. Gp cannot become USD; free incumbents. |
| U3 | AI Mandarin tutor | No-go in general form. The HSK 3.0 speaking-mock wedge is pending a demand test. |

## Run 2026-10-06 round 2: 13 ideas
Results:
- The best composite rose to 6.70 (M3), and M3's sale score of 7 is the first above 6.
- The winners came from the marketplace persona, which looked for **stranded paying users**: customers of a broken or abandoned incumbent.

### 11. Model first *cash*, not only first sale
Count payout thresholds and timing in the time to first cash:
| Platform | Payout rule |
|---|---|
| Atlassian | Nothing paid until $500 cumulative |
| Apify | $20 minimum; paid on the 21st–25th of the next month |
| RapidAPI | Paid in month +2 |

### 12. Never give away the unit you charge for
Two launch promos in this run destroyed the unit economics:
- M3 made the first 1,000 rows of every run free, but typical runs are about 200 rows, so almost every run was free.
- C2 offered a "founding price for life".

On Apify, free-plan users pay out nothing, but supplier APIs still bill you for their runs. Gate supplier calls on the user's plan.

### 13. Multi-tenant designs need per-customer authorization
A shared credential that lets one customer write to another customer's resources is a launch blocker.

### 14. Partner channels are not marketplaces
- Expect a 5–10% yes-rate from an unknown vendor.
- Expect 1–1.5 h/week of hidden sponsor time for pitching and partner management.
- There is no built-in discovery or billing.

### 15. Check supplier and platform terms before building
Terms missed in this run:
- DataForSEO's terms are silent on resale.
- Gemini's grounding terms ban caching or reselling grounded answers.
- ProPublica's API licence is non-commercial (NC).
- Discord requires payment parity for features sold outside its own billing.
- Transactional email providers ban cold outreach.

### 16. Clone floods are now the default
- On every marketplace checked, "few listings" no longer means a gap. AI-built clones fill the long tail.
- Cheaper clones and "reliable" clones both sit at 0–2 users.
- Look for placement advantages (integration pickers, in-product search) and for incumbents that are broken right now.
- Check each incumbent's last-modified date and changelog.

### 17. One production listing per marketplace account
This applies across all runs. Apify can withhold all payouts for a policy breach, so co-located Actors share that risk.

### 18. Who pays compute (checked against platform docs on 2026-10-06)

**Apify pay-per-event (PPE):**
- `profit = 0.8 × revenue − platform costs`, counted for paid-plan users only.
- Apify covers the compute costs of free-plan users.
- An Actor's negative profit is floored at $0 and is **not** netted against other Actors' profit.
- So the developer is never invoiced for compute. The worst case is $0 earned.

**Atlassian Forge:**
- The developer is invoiced monthly in arrears for usage above the free allowance. This includes usage from free-tier installs.
- The allowance includes 200k GB-seconds of function time per month; overage is $0.000025 per GB-second.
- Atlassian holds payouts until $500 is earned, so any overage is paid out of pocket until then.

**On both platforms, operator tokens are the main cost.** Model them as the true break-even line.

### Ideas evaluated in round 2: do not resubmit
| ID | Idea | Outcome |
|---|---|---|
| G1 | Keyword→Brief SEO API (Apify) | |
| G2 | LongForm Transcripts (Apify) | |
| G3 | AnswerShare GEO API | |
| C1 | FunderFit | |
| C2 | Client Safety Kit | |
| C3 | Interpreter Practice Lab | |
| I1 | Zì Bot | |
| I2 | Episode Study Packs | |
| I3 | Role-Play Room | |
| M1 | ChatRelay for Jira | Pick #2 |
| M2 | SpecView for Confluence | |
| M3 | SheetSync Apify→Sheets | Pick #1 |
| U4 | AI-matched job board | No-go |

Adjacent ideas that fix a listed idea's fatal flaw are allowed. Say which one you are fixing.
