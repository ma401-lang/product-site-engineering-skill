# {{PROJECT_NAME}} acceptance matrix

Initialized: {{DATE}}

Evidence states: `not_started`, `implemented_unverified`, `locally_passed`, `preview_passed`, `production_passed`, `user_validated`, `blocked`.

| ID | Priority | Scenario | Pass condition | Evidence | Status |
|---|---|---|---|---|---|
| BENCH-01 | P0 | A non-trivial build, redesign, migration or release begins | Current-state evidence is captured and a versioned benchmark with attributed references, anti-benchmarks, targets and mapped IDs is frozen before implementation | Benchmark review + decision log | not_started |
| BENCH-02 | P1 | Product direction changes after the benchmark was frozen | Benchmark version and affected facts, acceptance IDs and roadmap are updated and re-frozen before implementation changes | Diff history + decision log | not_started |
| BENCH-03 | P0 | An idea is being turned into a new product or material feature | Original idea, unknowns, research method/evidence, requirement choice and design hypothesis are traceable before implementation | Benchmark research and decision trace | not_started |
| BADCASE-01 | P0 | A test fails meaningfully or a user/product owner rejects a result | A de-identified bad case records the original scenario, expected/observed result, severity, responsible layer, regression/eval ID, prevention guard, owner and status before the fix is declared complete | Bad-case register + regression evidence | not_started |
| BADCASE-02 | P0 | A known bad case happens again | The existing case's recurrence count and analysis are updated; the failed prevention guard is strengthened and the release remains blocked until verified or explicitly risk-accepted | Recurrence record + decision log + release test | not_started |
| FLOW-01 | P0 | A new user starts the primary flow | Reaches the first useful action without a fake control or internal jargon | Browser test | not_started |
| ASSET-01 | P0 | Navigation or visual structure changes | Every protected route, capability and saved-data contract remains discoverable and compatible, or owner approval is recorded | Before/after asset map + regression test | not_started |
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
