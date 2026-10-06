# Run parameters: round 3 (capital allowed)

These parameters **override** the defaults in `.claude/skills/business-ideation/reference/operator-constraints.md` and the upfront-capital hard gate in `scoring-rubric.md` for this run only. Every agent in this run must apply them.

## Capital
- **Hard cap: $10,000** upfront (replaces the $100 cap).
- **Strong preference: under $1,000.**
  - The higher the capital, the stronger the projected payout must be.
  - Ideas above $1k must show a payback period of **12 months or less** at the P50 (realistic) case.
  - Ideas above $1k must show a downside (P10) case that loses no more than about 50% of the capital.
- **Opportunity-cost benchmark:** idle capital in Treasury bills earns roughly 4%/yr. Report each idea's annualised return on capital against that.
- Capital may be spent on:
  - equipment;
  - inventory;
  - buying an existing business;
  - paid advertising;
  - contractors.

## Sponsor time is worth $300/hour
- **Every hour of human sponsor work is a cost of $300.** This includes physical work, sales calls, outreach, account setup and support.
- **Gate:**
  - ongoing sponsor hours per month must be no more than **net monthly profit ÷ $300**;
  - one-time setup hours × $300 are charged against **first-year** profit.
- At the $300/month target this allows about **1 sponsor hour per month**. More profit buys more hours: $1,500/month net allows 5 h/month.
- **Physical work must be outsourced** (paid contractor, service company, marketplace labour such as TaskRabbit, or a revenue-share operator) unless it meets the $300/h test. Contractor costs count as normal operating costs.
- The AI operator's time is not sponsor time. Its token cost (~$50–150/mo) is still an operating cost.

## Targets (unchanged)
- **Net profit after all costs:** $300/month (break-even target); $1,000/month stretch.
  - "All costs" means COGS, fees, contractors, AI operator tokens and the depreciation or payback of capital.
- **P50 time to first revenue: 90 days or less preferred.** For an acquisition, first revenue arrives at close.

## Physical ideas are in scope
Physical assets, locations and contracts are welcome. They are moats that AI-built clones can't copy (see lessons-learned §19). But they must satisfy the sponsor-time rule through outsourcing.
