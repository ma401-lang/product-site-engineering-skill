# {{PROJECT_NAME}} engineering boundaries

Status: draft

Initialized: {{DATE}}

## 1. Current stack

| Layer | Current choice | Why | Explicitly not adding now |
|---|---|---|---|
| UI/runtime |  |  |  |
| Server/API |  |  |  |
| Data |  |  |  |
| Hosting |  |  |  |
| AI, if any |  |  |  |

## 2. Reuse-first decision order

1. Existing project and official platform capability.
2. Mature library, framework, hosted service, or factual standard.
3. Configuration, plugin, extension, adapter, or orchestration.
4. Custom code for product differentiation or integration boundaries.
5. New core infrastructure only after recording the unmet constraint, alternatives, exit cost, and maintenance owner.

## 3. Trusted boundaries

- Browser/public:
- Server/private:
- Administrative:
- Third-party processors:

Treat client bundles, source maps, public environment variables, browser storage and network responses as public.

## 4. API contract

```json
{
  "code": "OK",
  "data": {},
  "message": "ok",
  "requestId": "..."
}
```

Record validation, authentication, authorization, rate limit, idempotency, timeout and streaming exceptions.

## 5. Data ownership

| Data | Authority | Tenant scope | Retention/deletion | Migration owner |
|---|---|---|---|---|
|  |  |  |  |  |

## 6. Directory/module boundaries

Document which modules may run in the browser, which are server-only, where product rules live, and where migrations/tests/evals live.

## 7. Migration rule

Framework, database, identity, hosting and model-provider migrations are separate behavior-equivalence projects. Freeze observable contracts, use a preview, and retain a rollback path.
