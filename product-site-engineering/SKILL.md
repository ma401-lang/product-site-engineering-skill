---
name: product-site-engineering
description: Build, audit, refactor, migrate, or release a user-facing website or web app when the work spans product requirements, acceptance criteria, frontend and backend boundaries, observability, deployment, AI behavior, data safety, or user feedback. Use for engineering-grade delivery of landing sites, portals, dashboards, SaaS products, MVPs, and beta releases, especially when the user asks for a product workbench, real buttons and failure states, frontend/backend logs, protected-asset checks, or a requirement-to-production workflow. Do not use for an isolated copy edit, a single CSS tweak, or a question that requires no product workflow.
---

# Product Site Engineering

Turn a website request into a coherent vertical slice that can be inspected, tested, observed, released, and improved from evidence.

## Operating contract

1. Read repository instructions and the current product, acceptance, architecture, and deployment sources of truth before changing behavior.
2. Inspect the working tree and preserve unrelated user changes.
3. Name the acceptance IDs the implementation is intended to satisfy. If the project has no acceptance matrix, create the minimal workbench or add scoped IDs before implementation.
4. Ask the product owner only when a choice changes positioning, billing, data boundaries, content rights, regulated or psychological safety scope, or causes an irreversible external effect. Decide reversible implementation details from evidence.
5. Work in one coherent vertical slice. Do not add adjacent features merely because they are easy to generate.
6. Report missing source material, unrun production checks, failed tests, and runtime blockers as soon as known. Never turn “specified” into “implemented” or “locally passed” into “production verified.”

## Delivery loop

Follow this order unless the repository defines a stricter one:

`requirement -> source-of-truth spec -> acceptance IDs -> task split -> implementation -> automated tests -> review -> preview/production verification -> user feedback`

For the detailed artifact contract and exit criteria, read [references/delivery-loop.md](references/delivery-loop.md).

### 1. Establish the product contract

- Write one sentence for the primary outcome, the target user, the main loop, and explicit non-goals.
- Separate current facts, decisions, hypotheses, and future ideas.
- Keep historical PRDs as history; do not let them silently override the current source of truth.
- Convert subjective goals such as “natural,” “premium,” or “fast” into observable scenarios and thresholds.

### 2. Protect existing product assets

Before navigation or visual restructuring, make an internal before/after asset map covering every route, user-facing capability, saved-data key, and minimum discoverable entry point.

Stop and request approval if the change would delete, hide, rename beyond recognition, redirect, or reinterpret a protected asset. Prefer migration and backward compatibility over silent data loss. See [references/frontend-quality.md](references/frontend-quality.md).

### 3. Choose the smallest mature architecture

Use this decision order:

1. Existing project and official platform capability.
2. Mature library, framework, hosted service, or factual standard.
3. Configuration, extension point, adapter, or orchestration.
4. Custom code for product differentiation or an integration boundary.
5. A new core capability only after documenting the unmet constraint, alternatives, exit cost, and maintenance owner.

Do not mix a framework migration with unrelated feature development. Freeze observable behavior, migrate behind a preview, and prove equivalence before switching traffic.

### 4. Implement the complete slice

Cover the path from the user's entry point through state, API, persistence, feedback, and recovery. Every public control must:

- perform a real action with visible outcome;
- navigate to a real destination;
- clearly say it is unavailable; or
- be absent from the released UI.

Validate empty, loading, success, error, timeout, retry, cancellation, duplicate submission, malformed input, stale data, and storage failure where applicable. Apply the frontend checklist in [references/frontend-quality.md](references/frontend-quality.md) and the API/data contract in [references/backend-api-data.md](references/backend-api-data.md).

### 5. Add observability as product behavior

Generate one correlation ID at the request boundary, return it to the client, and propagate it through backend dependencies. Log events and outcomes, not user content.

Use an allowlist schema. Do not log request bodies, chat or form text, cookies, authorization headers, tokens, full IP addresses, raw email addresses, or secrets by default. Keep browser analytics, operational logs, security audit events, and consented research data as separate datasets with separate retention.

For fields, streaming lifecycle events, dashboards, alert signals, and TypeScript examples, read [references/observability.md](references/observability.md). Copy and customize the workbench log schema rather than inventing ad hoc `console.log` payloads.

### 6. Treat AI behavior as tested application code

Only apply this section when the product calls a model.

- Keep model calls, prompts, secrets, safety logic, and private retrieval on the server.
- Version prompts in code and test prompt changes in the same review as the product behavior they change.
- Prefer state contracts, retrieval quality, and deterministic guards before making the prompt larger.
- Build eval cases from real, de-identified failures; separate deterministic assertions, human review, and model-graded checks.
- Require user approval for long-term memory and keep it viewable, editable, and deletable.
- Do not claim a prompt rule is implemented until an executable test or production guard enforces it.

Read [references/ai-product-safety.md](references/ai-product-safety.md) for high-stakes and knowledge-grounded products. Read [references/prompt-learning-resources.md](references/prompt-learning-resources.md) only when designing or reviewing prompts.

### 7. Verify and release

Run the repository's relevant format, lint, typecheck, unit, integration, end-to-end, build, security, migration, and AI eval commands. Test a real mobile-sized flow and a deployed smoke path when release is in scope.

Record the release identifier in frontend and backend telemetry. Verify secrets, environment variables, data migrations, rollback, regional dependencies, and user-facing error states. See [references/release-operations.md](references/release-operations.md).

## Product workbench

Initialize a reusable workbench when the repository lacks equivalent documents:

```bash
python3 scripts/init_workbench.py --target /absolute/path/to/project --project "Project name"
python3 scripts/audit_workbench.py --target /absolute/path/to/project
```

Use `--dry-run` before writing when the target is unfamiliar. The initializer refuses to overwrite existing files unless `--force` is explicit. Prefer adapting existing repository sources of truth instead of creating duplicates.

The workbench includes:

- product system spec and non-goals;
- acceptance matrix with stable IDs;
- engineering boundaries and reuse decisions;
- protected asset register;
- delivery roadmap and decision log;
- observability plan and log-event JSON Schema;
- incident runbook and sanitized feedback log.

## Completion response

Lead with the outcome. State:

- what works now and which acceptance IDs it satisfies;
- files or deployed surfaces changed;
- tests and production checks actually run;
- anything still unverified, risky, or requiring product-owner authority;
- the smallest useful next step, if one remains.

Do not expose private prompts, internal knowledge, secrets, raw logs, or user data in the handoff.
