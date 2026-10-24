# {{PROJECT_NAME}} bad-case register

Initialized: {{DATE}}

This file is the product's durable memory of results that failed, felt wrong, confused a user, violated a boundary, or returned after an earlier fix. Record the case before changing the product, while the triggering scenario is still reproducible.

Do not paste raw conversations, names, contacts, credentials, private prompts, production payloads, or screenshots containing personal data. Use a restricted evidence reference when the source must remain private.

## Intake rule

Create or update a case when any of these happens:

- an automated, manual, accessibility, security or usability test fails meaningfully;
- the product owner or a user says the result is unsatisfactory;
- an AI output violates an explicit or newly discovered boundary;
- a production incident exposes a user-visible failure;
- a problem already marked prevented or verified appears again.

Before fixing it, capture the triggering situation, expected result, observed result, severity, responsible layer and a regression/eval ID. Name the prevention guard. After fixing it, attach evidence from the original scenario. On recurrence, increment the count and explain why the earlier guard did not catch it.

Statuses: `observed`, `reproduced`, `prevented`, `verified`, `accepted`, `blocked`.

## Cases

| Bad case ID | Date | Source ref | Triggering scenario | Expected | Observed | Severity | Responsible layer | Regression/eval ID | Prevention guard | Owner | Status | Resolution evidence | Recurrence count and analysis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Review rule

- P0 cases block release until `verified`, or until the product owner records an explicit `accepted` risk and expiry/review date in the decision log.
- `prevented` means a guard exists; `verified` means the original scenario and surrounding regression set passed against the intended release.
- A repeated case never receives a new unrelated ID. Update the existing row, increment recurrence and improve the prevention guard.
- Link user feedback with `FB-*`, acceptance checks with stable IDs, AI evaluations with `EVAL-*`, and incidents with their sanitized reference.
