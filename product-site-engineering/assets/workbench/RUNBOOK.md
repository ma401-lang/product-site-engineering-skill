# {{PROJECT_NAME}} operational runbook

Initialized: {{DATE}}

## Service facts

- Production origin:
- Hosting/runtime:
- Current release identifier:
- Primary database/dependencies:
- Logs/metrics location:
- Operational owner:

Do not place secret values in this document.

## Severity

| Severity | Example | Response target | Authority |
|---|---|---|---|
| SEV-1 | Data exposure, destructive corruption, or primary flow unavailable | Immediate | Stop traffic/rollback |
| SEV-2 | Major flow degraded with workaround | Same working period | Mitigate or roll back |
| SEV-3 | Limited defect or non-critical degradation | Planned fix | Normal release |

## Triage

1. Confirm user impact without requesting private content.
2. Record start time, release, route, request ID, outcome and error code.
3. Check whether the issue began with a deployment, dependency, configuration or data migration.
4. Choose mitigation: disable feature, reduce traffic, revert release, pause writes, or communicate limitation.
5. Preserve evidence without copying secrets or raw user data into tickets.

## Primary flow unavailable

- Detection query:
- Known dependency checks:
- Safe mitigation:
- Rollback command/control:
- Verification after mitigation:

## Failed or uncertain writes

- Idempotency/status lookup:
- Duplicate reconciliation:
- User-facing message:
- Data repair owner:

## Suspected data or secret exposure

1. Stop further exposure.
2. Restrict access and preserve audit evidence.
3. Rotate affected secrets.
4. Determine scope and required notifications with the responsible owner.
5. Do not discuss sensitive details in public issues.

## Rollback

- Last known-good release:
- Data compatibility:
- Exact rollback action:
- Post-rollback smoke test:
- Communication owner:

## After the incident

Write a factual timeline, impact, root cause, contributing conditions, detection gap and preventive acceptance case. Avoid blame and avoid storing private payloads.
