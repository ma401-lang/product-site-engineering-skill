# {{PROJECT_NAME}} product system specification

Status: draft

Initialized: {{DATE}}

## 0. Discovery handoff

- Benchmark version that supports this specification:
- Original idea/research IDs:
- Requirement/design decision IDs:
- Assumptions still awaiting user or production evidence:
- Bad cases this version must prevent:

## 1. Product contract

- One-sentence outcome:
- Target user and triggering situation:
- Primary user loop:
- Why this product should exist now:

## 2. Non-goals

- The product is not:
- The beta will not promise:
- Features explicitly deferred:

## 3. Success and failure

- First useful outcome:
- Evidence that a user received value:
- Evidence that the product is confusing or harmful:
- Beta size and duration:
- Bad-case triggers that must be recorded even if no metric moves:

## 4. Information architecture

| Route/surface | User purpose | Primary action | Saved data | Release status |
|---|---|---|---|---|
| `/` |  |  |  | draft |

## 5. Primary flow

```text
entry -> first useful action -> durable result -> recovery/revisit -> feedback
```

Document optional branches separately. Do not make every future feature part of the primary loop.

## 6. Data and privacy

| Data category | Why needed | Authoritative storage | Retention | User control | May enter logs/AI? |
|---|---|---|---|---|---|
|  |  |  |  |  | no by default |

## 7. Safety and content boundaries

- Regulated or high-stakes claims:
- Required human review:
- Content rights/source rules:
- Abuse and crisis boundaries, if applicable:

## 8. Commercial boundary

- Current paid state:
- Capabilities that truly exist:
- Capabilities that must not be advertised yet:

## 9. Decisions requiring product-owner approval

List only decisions that change positioning, billing, data boundaries, content rights, safety scope, or irreversible external state.

## 10. Source-of-truth precedence

When documents conflict, this specification and `ACCEPTANCE_MATRIX.md` govern current behavior. Historical documents remain history and must not silently restore old assumptions.
