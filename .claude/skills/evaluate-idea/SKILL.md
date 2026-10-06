---
name: evaluate-idea
description: Run the evaluation panel (sales skeptic, market analyst, autonomy auditor, legal risk analyst, unit economics analyst) on a single business idea the user supplies, then give a go/no-go verdict. Use when the user has their own idea and wants it stress-tested for AI-run viability.
---

# Evaluate a Single Idea

1. **Normalize the idea** into the template in `.claude/skills/business-ideation/reference/idea-brief.md`, using ID `U1`. Fill in missing fields with your best assumptions and mark them `(assumed)`. Save it to `runs/<YYYY-MM-DD>-eval-<slug>/ideas/user.md`.
2. **Launch the five evaluators in parallel** in a single message: `sales-skeptic`, `market-analyst`, `autonomy-auditor`, `legal-risk-analyst`, and `unit-economics-analyst`. Write each output to `runs/<...>/reviews/<agent>.md`.
   If the custom agent types are not registered in this session, use `general-purpose` agents told to act as `.claude/agents/<name>.md`.
3. **Compute the composite score** and apply the hard gates from `.claude/skills/business-ideation/reference/scoring-rubric.md`.
4. **Reply with:**
   - verdict (**Go / Pivot / No-go**);
   - composite score;
   - one line per evaluator;
   - P50/P90 days to first sale;
   - upfront $;
   - human hours;
   - top legal risk;
   - the single highest-leverage fix.
