# {{PROJECT_NAME}} product workbench

Initialized: {{DATE}}

This directory is the delivery control plane for the product. Keep it current with behavior changes; do not turn it into a speculative document archive.

## Reading order

1. `PRODUCT_SYSTEM_SPEC.md` — product outcome, users, scope, non-goals, data and safety.
2. `ACCEPTANCE_MATRIX.md` — executable scenarios and evidence state.
3. `ENGINEERING_BOUNDARIES.md` — current architecture and decision limits.
4. `PRODUCT_ASSET_REGISTER.md` — routes, capabilities and saved data that must survive changes.
5. `DELIVERY_ROADMAP.md` — ordered vertical slices and exit criteria.
6. `OBSERVABILITY_PLAN.md` — privacy-aware events, dashboards and alerts.
   The two JSON Schemas define separate browser and backend event allowlists.
7. `RUNBOOK.md` — incident response and rollback.
8. `DECISION_LOG.md` — product and architecture decisions.
9. `USER_FEEDBACK_LOG.md` — sanitized evidence and resulting acceptance cases.

## Evidence language

Use explicit states: `not_started`, `implemented_unverified`, `locally_passed`, `preview_passed`, `production_passed`, `user_validated`, or `blocked`.

Do not mark work complete because a document, prompt, UI shell, or local test exists. Record the highest evidence level actually achieved.
