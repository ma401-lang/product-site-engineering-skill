# {{PROJECT_NAME}} product workbench

Initialized: {{DATE}}

This directory is the delivery control plane for the product. Keep it current with behavior changes; do not turn it into a speculative document archive.

## Reading order

1. `PRODUCT_SYSTEM_SPEC.md` — product outcome, users, scope, non-goals, data and safety.
2. `BENCHMARK.md` — current baseline, attributed references, anti-benchmarks, quality targets and direction-change history. Freeze it before implementation.
3. `ACCEPTANCE_MATRIX.md` — executable scenarios and evidence state.
4. `ENGINEERING_BOUNDARIES.md` — current architecture and decision limits.
5. `PRODUCT_ASSET_REGISTER.md` — routes, capabilities and saved data that must survive changes.
6. `DELIVERY_ROADMAP.md` — ordered vertical slices and exit criteria.
7. `OBSERVABILITY_PLAN.md` — privacy-aware events, dashboards and alerts.
   The two JSON Schemas define separate browser and backend event allowlists.
8. `RUNBOOK.md` — incident response and rollback.
9. `DECISION_LOG.md` — product and architecture decisions, including benchmark freezes and version changes.
10. `USER_FEEDBACK_LOG.md` — sanitized evidence and resulting acceptance cases.

## Evidence language

Use explicit states: `not_started`, `implemented_unverified`, `locally_passed`, `preview_passed`, `production_passed`, `user_validated`, or `blocked`.

Do not mark work complete because a document, prompt, UI shell, or local test exists. Record the highest evidence level actually achieved.
