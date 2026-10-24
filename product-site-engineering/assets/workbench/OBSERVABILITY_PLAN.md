# {{PROJECT_NAME}} observability plan

Initialized: {{DATE}}

## 1. User journeys

| Journey | Success signal | Failure signal | Owner |
|---|---|---|---|
| Primary flow |  |  |  |

## 2. Data planes

| Plane | Purpose | Allowed fields | Forbidden fields | Retention | Access |
|---|---|---|---|---|---|
| Product analytics | Aggregate product use | Named events, release, route, outcome | User-entered content, secrets |  |  |
| Operational logs | Reliability and debugging | Request ID, route template, status, duration, error code | Bodies, cookies, tokens, raw upstream text |  |  |
| Security audit | Sensitive state changes | Actor scope, action, resource hash, outcome | Secret values, resource content |  |  |
| Consented quality data | Approved research/evaluation | Explicitly approved, minimized records | Unconsented raw production content |  |  |

## 3. Correlation

- Request ID generated at:
- Returned through:
- Propagated to:
- User support can locate it via:

## 4. Backend event contract

Use `log-event.schema.json` as the allowlist baseline. Record route templates, not URLs containing personal or high-cardinality values.

## 5. Frontend event catalog

| Event name | Trigger | Fields | Sampling | Acceptance ID |
|---|---|---|---|---|
| `primary_action_result` | Primary action finishes | release, route, request_id, outcome, duration_bucket | 100% during beta | OBS-01 |

## 6. Streaming/AI events, if applicable

Record accepted, upstream started, first chunk, completed, cancelled, failed, output-guard retry and safe fallback. Never record chunks, prompts, retrieved private context or model text by default.

## 7. Dashboards and alerts

| Signal | Query/metric | Threshold/window | Runbook section | Owner |
|---|---|---|---|---|
| Primary success rate |  |  |  |  |
| p95 latency |  |  |  |  |
| 5xx/dependency error rate |  |  |  |  |

## 8. Verification

- Schema test:
- Preview log inspection:
- Redaction/allowlist test:
- Request ID end-to-end test:
- Retention/deletion test:
