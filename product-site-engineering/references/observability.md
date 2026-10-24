# Privacy-aware observability

Use this reference whenever a website adds a user flow, API, background job, external dependency, model call, or production release.

## Four separate data planes

Do not collapse these into one “logs” bucket:

1. **Product analytics**: aggregate use of consented product events.
2. **Operational telemetry**: availability, latency, errors, saturation, retries, and dependency health.
3. **Security audit events**: privileged or sensitive state changes, with actor scope and outcome.
4. **Research or quality data**: explicitly consented, access-controlled, time-bounded material for human review or model improvement.

Each plane needs its own allowed fields, access, retention, and deletion policy.

## Correlation contract

- Generate a high-entropy `request_id` at the edge or first backend boundary.
- Accept an incoming ID only from a trusted proxy or after strict validation.
- Return it as `X-Request-ID` and in JSON error envelopes.
- Pass it to services, database annotations, external calls, jobs, and completion logs.
- Use a separate `trace_id` only if a tracing system exists; do not pretend a request ID is distributed tracing.

## Backend structured event

Use JSON or the platform's native structured event format. Recommended allowlist:

| Field | Purpose |
|---|---|
| `timestamp` | UTC event time |
| `level` | debug/info/warn/error |
| `event_name` | Stable, low-cardinality name |
| `service` | Logical service or worker |
| `environment` | local/preview/production |
| `release` | Commit or deployment identifier |
| `request_id` | Cross-boundary correlation |
| `trace_id` | Optional real trace identifier |
| `route` | Route template, not a URL containing personal data |
| `method` | HTTP method |
| `status_code` | Final status |
| `duration_ms` | Measured server duration |
| `outcome` | success/rejected/timeout/cancelled/error |
| `error_code` | Stable internal category, not an exception message |
| `dependency` | Named external system when relevant |
| `retry_count` | Bounded retry count |

High-cardinality business IDs should be omitted, hashed with a rotating secret, or placed in a restricted audit stream only when operationally necessary.

## Never log by default

- form fields, search text, chat messages, uploaded document text, or prompt content;
- request or response bodies;
- authorization headers, cookies, session IDs, API keys, tokens, connection strings, or signed URLs;
- full IP addresses, exact GPS, raw emails, phone numbers, legal names, or device fingerprints;
- model system prompts, retrieved private context, raw model output, or raw upstream error bodies;
- database rows or stack traces in user-visible responses.

Prefer an allowlist serializer. Redaction after arbitrary objects are logged is a last line of defense, not the primary design.

## Frontend events

Keep the browser payload smaller than the backend payload:

```json
{
  "event_name": "feedback_submit_result",
  "timestamp": "2026-01-01T00:00:00Z",
  "release": "abc1234",
  "route": "/feedback",
  "request_id": "019...",
  "outcome": "timeout",
  "duration_bucket": "8s_plus"
}
```

Do not send the form text. Avoid unrestricted properties from DOM elements, query strings, referrers, or exception objects. Disable noisy production `console.log`; route expected telemetry through one typed adapter.

## Streaming and AI lifecycle

For a streaming request, useful events include:

- `request_accepted`
- `upstream_started`
- `first_chunk_received` with `time_to_first_chunk_ms`
- `stream_completed` with duration and byte/token bucket
- `stream_cancelled`
- `stream_failed` with stable error code
- `output_guard_retry`
- `safe_fallback_used`

Never log stream chunks. Track first-pass, retry-pass, and fallback separately so a high fallback rate cannot masquerade as model success.

## Audit events

Sensitive mutations should record who/what/when/outcome without recording content:

```text
actor_scope, action, resource_type, resource_id_hash, policy_version,
request_id, outcome, timestamp
```

Use immutable or append-oriented storage where required by the risk model. Product analytics is not an audit log.

## Dashboards and alerts

Start with signals tied to a user journey:

- request volume and success rate by route template;
- p50/p95/p99 latency and time to first streamed chunk;
- validation, authorization, rate-limit, timeout, dependency, and 5xx rates;
- durable-write success and duplicate prevention;
- client error rate by release;
- model first-pass, retry, blocked, and fallback rates when applicable;
- deployment comparison and rollback marker.

Alert on sustained user impact, not every single error. Every alert should link to a runbook with owner, query, mitigation, and rollback instructions.

## Retention and access

- Define retention per data plane and environment.
- Keep production access least-privileged and auditable.
- Sample high-volume success events; retain error categories, not private payloads.
- Test deletion and access revocation.
- Document vendor region, subprocessors, and export behavior when user data might leave the primary system.

The workbench includes `log-event.schema.json` as a starting contract. Customize it to the platform, then validate emitted events in tests.

It also includes `frontend-event.schema.json`. Keep the two schemas separate: the browser must not inherit server-only fields merely because both are called telemetry.

## Minimal TypeScript adapter

The bundled [observability.ts](../assets/examples/typescript/observability.ts) demonstrates an explicit-field adapter for both sides. Its main properties are:

- callers cannot pass an arbitrary request, error, user, or provider object;
- routes are supplied as templates without query strings;
- the server sink receives structured JSON;
- the browser sink is injected, so the template does not silently choose a vendor;
- user content has no field in either type.

Copy it into the target project only after adapting event names, environment/release injection, transport, sampling, consent, and retention. A type definition reduces accidental collection but does not replace runtime schema validation at ingestion.
