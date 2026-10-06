---
name: business-ideation
description: Run the full autonomous-business ideation pipeline - persona ideators generate ideas, an evaluation panel (sales skeptic, market analyst, autonomy auditor, legal risk analyst, unit economics analyst) reviews them, and an investment committee picks the top 1-2 with a launch plan. Use when asked to generate, evaluate, or pick business ideas an AI could run to cover its own token costs.
---

# Business Ideation Pipeline

Goal: find a business an AI agent can run **mostly on its own** that earns at least **$300/month** (enough to pay for its own tokens), starting from **~$0 capital**.

## Agents

| Phase | Agent | Role |
|---|---|---|
| 1. Ideate | `ideator-tech` | The Builder: micro-SaaS, extensions, dev tools, templates |
| 1. Ideate | `ideator-writer` | The Wordsmith: newsletters, guides, content |
| 1. Ideate | `ideator-artist` | The Studio: AI art, digital downloads, POD, assets |
| 1. Ideate | `ideator-data-analyst` | The Analyst: datasets, monitoring/alerts, directories |
| 1. Ideate | `ideator-niche-scout` | The Scout: demand-first, mined from complaints and gigs |
| 2. Evaluate | `sales-skeptic` | Adversarial review of sale plausibility and time to first sale |
| 2. Evaluate | `market-analyst` | Demand, competitors, saturation, AI commoditization |
| 2. Evaluate | `autonomy-auditor` | Human intervention required |
| 2. Evaluate | `legal-risk-analyst` | Legal risk to the human runner |
| 2. Evaluate | `unit-economics-analyst` | Costs, token burn, break-even |
| 3. Decide | `investment-committee` | Scoreboard, hard gates, top picks, 30-day plan |

Shared references are in `reference/`:
- `operator-constraints.md`: what the AI and the human can do, plus targets.
- `idea-brief.md`: the template ideas must follow.
- `scoring-rubric.md`: scores, hard gates, and the composite formula.

## Arguments (optional)
- `focus`: restrict or bias the ideators, e.g. "B2B only" or "no physical goods".
- `personas`: subset of ideators to run (default: all five).
- `ideas_per_persona`: default 3.
- `target`: monthly break-even target (default $300).

## Procedure

1. **Set up the run directory:** `runs/<YYYY-MM-DD>/` with `ideas/` and `reviews/` subfolders. If the directory exists, append `-2`, `-3`, and so on.
2. **Phase 1 — Ideate (parallel).** Launch every ideator agent **in a single message** so they run concurrently. Give each one:
   - its output path `runs/<date>/ideas/<persona>.md`;
   - any `focus` argument.
   Wait for all of them to finish.
3. **Check the ideas.** Read the idea files. Confirm the IDs are unique and every brief has the template fields. Fill small gaps yourself, or re-prompt the ideator.
4. **Phase 2 — Evaluate (parallel).** Launch all five evaluators **in a single message**. Each one reviews **all** ideas, so relative scoring stays consistent. Give each one:
   - the ideas folder;
   - its output path `runs/<date>/reviews/<agent>.md`.
   Wait for all of them to finish.
5. **Phase 3 — Decide.** Run `investment-committee` with the run directory. It writes `runs/<date>/REPORT.md`.
6. **Sanity-check the report.**
   - Composite scores must match the rubric formula.
   - The hard gates must be applied.
   - The top picks' numbers must match the reviewer files.
   Fix any discrepancies.
7. **Present the results to the user:** the top 1–2 ideas with upfront capital, P50/P90 time to first sale, human hours, legal risk, and a pointer to `REPORT.md`.

## Notes
- If the custom agent types are not registered in the current session (e.g. they were just created), launch `general-purpose` agents instead. Tell each one to "act as the agent defined in `.claude/agents/<name>.md`", read that file, and follow it.
- Evaluators should use WebSearch/WebFetch where available. If web access is unavailable, findings must be marked `(unverified)`.
- To evaluate a single externally-supplied idea, use the `evaluate-idea` skill instead.
