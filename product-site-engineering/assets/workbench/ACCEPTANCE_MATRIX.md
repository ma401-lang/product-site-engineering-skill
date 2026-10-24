# {{PROJECT_NAME}} acceptance matrix

Initialized: {{DATE}}

Evidence states: `not_started`, `implemented_unverified`, `locally_passed`, `preview_passed`, `production_passed`, `user_validated`, `blocked`.

| ID | Priority | Scenario | Pass condition | Evidence | Status |
|---|---|---|---|---|---|
| FLOW-01 | P0 | A new user starts the primary flow | Reaches the first useful action without a fake control or internal jargon | Browser test | not_started |
| UI-01 | P0 | Primary async action is slow or fails | Loading, timeout, retry and duplicate prevention are visible and truthful | Component + browser test | not_started |
| API-01 | P0 | API receives empty, malformed, oversized or unauthorized input | Request is rejected before side effects with a stable public error and request ID | Unit + integration test | not_started |
| DATA-01 | P0 | Public bundle, storage and network are inspected | No secret, private prompt, admin credential or raw internal error is exposed | Build scan + browser inspection | not_started |
| OBS-01 | P0 | A production request succeeds or fails | Frontend and backend can correlate it without logging user content | Schema test + preview logs | not_started |
| REL-01 | P0 | A release is deployed and then rolled back | Previous release is restored and declared durable data remains readable | Rehearsal on preview | not_started |
| A11Y-01 | P1 | User completes the primary flow with keyboard and 360 px viewport | Focus, labels, errors, status and layout remain usable | Manual + automated checks | not_started |

## Product-specific cases

Add the smallest scenarios that distinguish this product. Include forbidden outcomes for AI or high-stakes behavior.

| ID | Priority | Scenario | Pass condition | Evidence | Status |
|---|---|---|---|---|---|
| DOMAIN-01 | P0 |  |  |  | not_started |
