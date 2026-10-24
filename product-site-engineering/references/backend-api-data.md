# Backend, API, and data boundaries

Use this reference for API changes, persistence, authentication, server actions, queues, or framework migrations.

## Request boundary

At the first trusted server boundary:

1. Generate or validate a correlation ID.
2. Parse the content type and enforce a body-size limit.
3. Validate shape and semantics with a typed schema.
4. Authenticate identity and authorize the exact operation.
5. Apply rate, abuse, and duplicate controls.
6. Call a business service; keep route handlers thin.
7. Map internal failures to a stable public error contract.
8. Emit a completion event without request content.

Never trust hidden buttons, client roles, client counters, or unsigned local data as authorization.

## JSON contract

A consistent envelope makes clients and operations easier to reason about:

```json
{
  "code": "OK",
  "data": {},
  "message": "ok",
  "requestId": "019..."
}
```

Errors should retain the same shape, set `data` to `null`, and use the correct HTTP status. Keep machine codes stable; make the public message actionable without revealing internals.

Streaming endpoints may use a stream on success, but failures before headers are committed should use the normal error contract. Return the request ID in a response header for every path.

## Reliability controls

- Apply explicit timeouts to external dependencies and propagate cancellation.
- Retry only idempotent operations or writes protected by an idempotency key.
- Use bounded retries with jitter; never create retry storms.
- Distinguish user error, policy rejection, dependency failure, configuration absence, and internal defect.
- For uncertain write outcomes, reconcile by idempotency key or status lookup instead of asking the client to blindly resubmit.
- Make duplicate database writes impossible with constraints where practical.

## Data ownership

For each data category, record:

- authoritative storage;
- owner or tenant scope;
- sensitivity class;
- retention and deletion behavior;
- backup/restore expectations;
- whether it may enter analytics, logs, model calls, or research datasets;
- migration and export obligations.

Keep schema changes in versioned migrations. Add stable primary keys, timestamps, unique constraints, foreign keys, and indexes based on actual access patterns. Test row-level or tenant isolation before claiming multi-user privacy.

## Secret boundary

Keep API keys, signing keys, database admin roles, internal prompts, private retrieval indexes, and privileged mutation logic on the server. Treat all `PUBLIC_*`, `NEXT_PUBLIC_*`, `VITE_*`, browser storage, HTML, and client bundles as disclosed.

Do not log authorization headers, cookies, database connection strings, model prompts, raw provider errors, or environment-variable values.

## Directory boundary

A useful general shape is:

```text
routes/controllers     parse, authenticate, validate, map response
services               product rules and orchestration
repositories/adapters  database and external dependencies
schemas/contracts      input, output, and event schemas
client                 browser-only API and storage adapters
tests                   unit, integration, end-to-end, evals
```

The exact names may differ. The invariant is that browser code cannot import privileged server modules and route files do not become the only home of business rules.
