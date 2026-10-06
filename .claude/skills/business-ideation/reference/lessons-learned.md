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

Adjacent ideas that fix a listed idea's fatal flaw are allowed. Say which one you are fixing.
