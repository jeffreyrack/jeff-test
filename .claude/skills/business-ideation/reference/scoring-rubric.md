# Scoring Rubric

Each evaluator scores each idea **1–10 on its own dimension** (10 = best for the business, i.e. least risk or most favourable).
Write a one-line justification for every score. Avoid clustering at 5–7: use the whole scale.

| Dimension | Owner agent | 10 means… | 1 means… |
|---|---|---|---|
| Sale plausibility | `sales-skeptic` | Clear buyer with intent, reachable now, first sale in < 2 weeks | No credible path to a stranger paying |
| Market | `market-analyst` | Proven demand, beatable competitors, room for a newcomer | No demand, or saturated with free alternatives |
| Autonomy | `autonomy-auditor` | < 2 h one-time human setup, ~0 h/week ongoing | Human needed daily or for each sale |
| Legal safety | `legal-risk-analyst` | Ordinary e-commerce risk only | Real exposure to lawsuits, regulators, or bans |
| Unit economics | `unit-economics-analyst` | $0 upfront, high margin, < 30 sales/month to hit $300 | Costs exceed realistic revenue |

## Hard gates (automatic reject, regardless of score)
- Upfront capital > $100.
- Legal safety ≤ 3.
- Requires > 3 human hours/week on an ongoing basis.
- P50 time to first sale > 180 days.

## Composite score (used by `investment-committee`)

```
composite = 0.30 * sale_plausibility
          + 0.20 * market
          + 0.20 * autonomy
          + 0.15 * unit_economics
          + 0.15 * legal_safety
```

Sale plausibility gets the highest weight on purpose: the goal is a business that actually earns, not one that sounds clever.
