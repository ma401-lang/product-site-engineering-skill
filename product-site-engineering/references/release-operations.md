# Release, deployment, and operations

Use this reference for previews, production deployments, hosting changes, regional access claims, or rollback planning.

## Pre-release gate

- The benchmark is frozen, current, and mapped to the release acceptance IDs; `audit_workbench.py --release` passes when the workbench is used.
- Acceptance matrix identifies every P0 item and its evidence state.
- Format, lint, typecheck, tests, evals, and production build pass where relevant.
- Secrets and private data scans are clean.
- Database migrations are forward-compatible and restore/rollback implications are understood.
- Public buttons, links, empty states, errors, and unavailable features are truthful.
- One real mobile-sized primary flow passes on the deployed preview.
- Observability includes the new release identifier and user journey.
- On-call or owner knows how to detect, mitigate, and roll back.

## Environment contract

Document per environment:

- runtime and region;
- public origin and custom domain;
- required and optional environment variables;
- secret source and rotation owner;
- database/project identifiers without secret values;
- external dependencies and their timeouts;
- logging/metrics destination and retention;
- migration command;
- smoke-test command;
- rollback mechanism.

Configuration absence should produce a controlled user state, not an internal stack trace.

## Deployment sequence

1. Freeze the intended diff and acceptance IDs.
2. Build from a clean, reproducible state.
3. Apply backward-compatible data changes first when possible.
4. Deploy to preview/staging.
5. Run API and browser smoke checks, including failure states.
6. Deploy gradually or to a limited beta when risk warrants it.
7. Watch error, latency, dependency, write, and fallback signals by release.
8. Roll back or disable via a prepared mechanism if user impact crosses the threshold.
9. Record production evidence separately from local evidence.

## Framework or hosting migration

Treat migration as behavior-preservation work:

- inventory routes, APIs, cookies, headers, redirects, storage keys, streaming behavior, metadata, jobs, and environment bindings;
- freeze public contracts;
- establish an old-versus-new equivalence suite;
- run the new system on a separate preview origin;
- migrate low-risk pages before authentication, payments, streaming, or privileged writes;
- avoid simultaneous product redesign;
- retain the old release until the rollback window closes.

## Regional access

Do not infer reachability or performance from the hosting vendor's global marketing. Verify with real networks, browsers, DNS, TLS, static assets, API calls, streaming, third-party scripts, fonts, analytics, CAPTCHA, and identity providers in the target region.

Separate these claims:

- technically reachable;
- reliably reachable across major networks;
- meets latency and availability targets;
- legally and contractually suitable for public operation.

Only the first three can be answered by technical testing; the last may require legal and business review.

## Rollback

A rollback plan names:

- the last known-good release;
- the exact traffic or deployment action;
- whether data migrations are compatible;
- what user data could be lost or duplicated;
- how success is verified after rollback;
- who communicates user impact.

Exercise rollback before depending on it for a high-risk release.
