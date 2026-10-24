# {{PROJECT_NAME}} delivery roadmap

Initialized: {{DATE}}

Each phase needs a visible outcome and exit criteria. Do not stack major features on top of unresolved P0 gates.

## Phase 0 — product truth and frozen benchmark

Deliver product intent, current-state evidence, an attributed and frozen benchmark, acceptance matrix, asset register, data boundary and unresolved owner decisions.

Exit: positioning, target user, main loop, non-goals, benchmark targets, protected assets and P0 scenarios are unambiguous; the release audit's benchmark checks pass.

## Phase 1 — engineering baseline

Deliver reproducible build, type/lint/test commands, server-only secrets, validated APIs, real persistence, data deletion and public-control inventory.

Exit: baseline P0 engineering, data and API cases pass locally.

## Phase 2 — primary vertical slice

Deliver the smallest complete path from entry to durable outcome, including empty/error/retry/duplicate states and telemetry.

Exit: the primary flow passes on a deployed preview and no public button is fake.

## Phase 3 — safety and quality

Deliver domain-specific regression cases, accessibility/mobile checks, rights review, security review and AI evals when applicable.

Exit: all release-blocking cases pass or are explicitly blocked with an owner.

## Phase 4 — limited release

Deliver production configuration, smoke test, dashboards, alerts, runbook, rollback and a deliberately small user cohort.

Exit: production flow works, feedback arrives, and rollback is executable.

## Phase 5 — evidence-led next decision

Choose one next constraint from real evidence: discoverability, retention, quality, performance, trust, synchronization, billing, or scope reduction.

If evidence changes the intended direction, revise and re-freeze the benchmark before changing the roadmap or implementation. Do not expand feature count by default.
