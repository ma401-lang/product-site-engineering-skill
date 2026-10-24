---
name: product-site-engineering
description: Carry a user-facing website or web app from idea and product research through requirements, design, implementation, testing, release, and evidence-led iteration. Use when work needs benchmarked product discovery, engineering-grade vertical slices, protected assets, observability, AI/data safety, deployment, or durable bad-case regression memory. Do not use for an isolated copy edit, one CSS tweak, or a question that needs no product workflow.
---

# Product Site Engineering

Carry a website from an early idea through research, requirements, design, implementation, release, and evidence-led improvement. Keep unsatisfactory results as durable bad cases so the same failure does not quietly return.

## Operating contract

1. Read repository instructions and the current product, acceptance, architecture, and deployment sources of truth before changing behavior.
2. Inspect the working tree and preserve unrelated user changes.
3. For non-trivial work, begin the benchmark while the idea is still being shaped. Record research questions and evidence, then trace the chosen requirement and design direction back to them before implementation.
4. Name the acceptance IDs the implementation is intended to satisfy. If the project has no acceptance matrix, create the minimal workbench or add scoped IDs before implementation.
5. Ask the product owner only when a choice changes positioning, billing, data boundaries, content rights, regulated or psychological safety scope, or causes an irreversible external effect. Decide reversible implementation details from evidence.
6. Work in one coherent vertical slice. Do not add adjacent features merely because they are easy to generate.
7. Put every failed test, rejected output, repeated complaint, or product-owner “this is not right” into the bad-case register before the conversation or test report disappears. Link the case to a regression check and the layer responsible for preventing it.
8. Report missing source material, unrun production checks, failed tests, and runtime blockers as soon as known. Never turn “specified” into “implemented” or “locally passed” into “production verified.”

## Delivery loop

Follow this order unless the repository defines a stricter one:

`idea -> research questions -> evidence -> requirements -> design hypothesis -> frozen benchmark -> acceptance IDs -> implementation -> tests -> bad cases -> release -> user feedback -> next benchmark`

For the detailed artifact contract and exit criteria, read [references/delivery-loop.md](references/delivery-loop.md).

### 1. Turn the idea into evidence

- Write the original idea in the owner's language, including why it matters now and what remains unknown.
- Research the user, triggering situation, current alternatives, comparable products, standards, technical constraints, and likely failure modes in proportion to the decision.
- Keep research notes separate from decisions. Record source, author or publisher, method, date, finding, confidence, and what the finding changes.
- Trace the chosen requirement and design hypothesis to the idea and evidence that support them. Mark assumptions that still need a prototype, interview, usability test, or production signal.

Use [references/benchmark-first.md](references/benchmark-first.md) for the idea-to-product trace. When specialized external Skills would help with discovery, visual direction, UI review, or React performance, read [references/external-skill-integration.md](references/external-skill-integration.md) and compose only the relevant one.

### 2. Establish the product contract

- Write one sentence for the primary outcome, the target user, the main loop, and explicit non-goals, grounded in the discovery evidence.
- Separate current facts, decisions, hypotheses, and future ideas.
- Keep historical PRDs as history; do not let them silently override the current source of truth.
- Convert subjective goals such as “natural,” “premium,” or “fast” into observable scenarios and thresholds.

### 3. Freeze the benchmark

- Include the idea thesis, research questions and findings, requirement decisions, design hypotheses, and current-state evidence before implementation.
- Select two to five comparable products, standards, or baselines and record each source, author or publisher, verification date, useful principle, and excluded copying.
- Define anti-benchmarks, weighted quality dimensions, targets, measurement methods, and mapped acceptance IDs.
- Set the benchmark to `frozen` before task splitting. When direction changes, increment its version, update it first, re-align affected sources of truth, and re-freeze it before code changes.
- Never move the benchmark after implementation merely to make the result pass.

Read [references/benchmark-first.md](references/benchmark-first.md) for the full contract. Use [references/website-building-resources.md](references/website-building-resources.md) only when selecting relevant learning sources; do not load every external rule into every task.

### 4. Protect existing product assets

Before navigation or visual restructuring, make an internal before/after asset map covering every route, user-facing capability, saved-data key, and minimum discoverable entry point.

Stop and request approval if the change would delete, hide, rename beyond recognition, redirect, or reinterpret a protected asset. Prefer migration and backward compatibility over silent data loss. See [references/frontend-quality.md](references/frontend-quality.md).

### 5. Choose the smallest mature architecture

Use this decision order:

1. Existing project and official platform capability.
2. Mature library, framework, hosted service, or factual standard.
3. Configuration, extension point, adapter, or orchestration.
4. Custom code for product differentiation or an integration boundary.
5. A new core capability only after documenting the unmet constraint, alternatives, exit cost, and maintenance owner.

Do not mix a framework migration with unrelated feature development. Freeze observable behavior, migrate behind a preview, and prove equivalence before switching traffic.

### 6. Implement the complete slice

Cover the path from the user's entry point through state, API, persistence, feedback, and recovery. Every public control must:

- perform a real action with visible outcome;
- navigate to a real destination;
- clearly say it is unavailable; or
- be absent from the released UI.

Validate empty, loading, success, error, timeout, retry, cancellation, duplicate submission, malformed input, stale data, and storage failure where applicable. Apply the frontend checklist in [references/frontend-quality.md](references/frontend-quality.md) and the API/data contract in [references/backend-api-data.md](references/backend-api-data.md).

### 7. Preserve bad cases and prove prevention

- Create a bad case whenever a test fails in a meaningful way, the owner rejects an output, a user cannot complete the intended task, or a known problem returns.
- Remove personal or secret content. Preserve the triggering situation, expected result, observed result, severity, responsible layer, owner, and recurrence count.
- Add or update an acceptance/eval ID before fixing. Record the prevention guard: deterministic test, browser scenario, AI eval, monitoring rule, content review, or explicit product decision.
- A resolved label is insufficient. Store evidence that the original scenario now passes. If the problem returns, increment recurrence and explain why the earlier guard failed.
- Block release for unresolved P0 bad cases unless the product owner explicitly accepts the documented risk.

The initialized workbench contains `BAD_CASES.md`; its structure is checked by the release audit. Do not leave durable failure knowledge only in chat, issue comments, screenshots, or model memory.

### 8. Add observability as product behavior

Generate one correlation ID at the request boundary, return it to the client, and propagate it through backend dependencies. Log events and outcomes, not user content.

Use an allowlist schema. Do not log request bodies, chat or form text, cookies, authorization headers, tokens, full IP addresses, raw email addresses, or secrets by default. Keep browser analytics, operational logs, security audit events, and consented research data as separate datasets with separate retention.

For fields, streaming lifecycle events, dashboards, alert signals, and TypeScript examples, read [references/observability.md](references/observability.md). Copy and customize the workbench log schema rather than inventing ad hoc `console.log` payloads.

### 9. Treat AI behavior as tested application code

Only apply this section when the product calls a model.

- Keep model calls, prompts, secrets, safety logic, and private retrieval on the server.
- Version prompts in code and test prompt changes in the same review as the product behavior they change.
- Prefer state contracts, retrieval quality, and deterministic guards before making the prompt larger.
- Build eval cases from the bad-case register and real de-identified failures; separate deterministic assertions, human review, and model-graded checks.
- Require user approval for long-term memory and keep it viewable, editable, and deletable.
- Do not claim a prompt rule is implemented until an executable test or production guard enforces it.

Read [references/ai-product-safety.md](references/ai-product-safety.md) for high-stakes and knowledge-grounded products. Read [references/prompt-learning-resources.md](references/prompt-learning-resources.md) only when designing or reviewing prompts.

### 10. Verify and release

Run the repository's relevant format, lint, typecheck, unit, integration, end-to-end, build, security, migration, and AI eval commands. Test a real mobile-sized flow and a deployed smoke path when release is in scope.

Record the release identifier in frontend and backend telemetry. Verify secrets, environment variables, data migrations, rollback, regional dependencies, and user-facing error states. See [references/release-operations.md](references/release-operations.md).

## Product workbench

Initialize a reusable workbench when the repository lacks equivalent documents:

```bash
python3 scripts/init_workbench.py --target /absolute/path/to/project --project "Project name"
python3 scripts/audit_workbench.py --target /absolute/path/to/project
python3 scripts/audit_workbench.py --target /absolute/path/to/project --release
```

Use `--dry-run` before writing when the target is unfamiliar. The initializer refuses to overwrite existing files unless `--force` is explicit. Prefer adapting existing repository sources of truth instead of creating duplicates.

The workbench includes:

- product system spec and non-goals;
- versioned benchmark, current baseline, references, anti-benchmarks, and weighted targets;
- idea thesis, product-research evidence, requirement/design trace, and durable bad-case register;
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
