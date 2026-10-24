# {{PROJECT_NAME}} product workbench

Initialized: {{DATE}}

This directory is the delivery control plane for the product. Keep it current with behavior changes; do not turn it into a speculative document archive.

## Reading order

1. `BENCHMARK.md` — original idea, research evidence, requirement/design trace, current baseline, references, targets and direction history. Start it during discovery and freeze it before implementation.
2. `PRODUCT_SYSTEM_SPEC.md` — the chosen product outcome, users, scope, non-goals, data and safety.
3. `ACCEPTANCE_MATRIX.md` — executable scenarios and evidence state.
4. `BAD_CASES.md` — durable memory for failed tests, rejected results, repeated problems and their prevention evidence.
5. `ENGINEERING_BOUNDARIES.md` — current architecture and decision limits.
6. `PRODUCT_ASSET_REGISTER.md` — routes, capabilities and saved data that must survive changes.
7. `DELIVERY_ROADMAP.md` — ordered vertical slices and exit criteria.
8. `OBSERVABILITY_PLAN.md` — privacy-aware events, dashboards and alerts.
   The two JSON Schemas define separate browser and backend event allowlists.
9. `RUNBOOK.md` — incident response and rollback.
10. `DECISION_LOG.md` — product and architecture decisions, including benchmark freezes and version changes.
11. `USER_FEEDBACK_LOG.md` — sanitized evidence, linked bad cases and resulting acceptance cases.

## Evidence language

Use explicit states: `not_started`, `implemented_unverified`, `locally_passed`, `preview_passed`, `production_passed`, `user_validated`, or `blocked`.

Do not mark work complete because a document, prompt, UI shell, or local test exists. Record the highest evidence level actually achieved.

When a test or review is unsatisfactory, record it in `BAD_CASES.md` before fixing it. The chat, issue, screenshot or evaluator output can disappear; the bad case and its regression guard stay with the product.
