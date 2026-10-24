# Delivery loop and evidence model

Use this reference when starting a product module, planning a release, or deciding whether work is complete.

## 1. Separate four kinds of statements

| Kind | Meaning | Evidence |
|---|---|---|
| Fact | True in the current code, deployed system, data, or contract | File, command output, deployed check, or authoritative source |
| Decision | An approved product or engineering choice | Decision log with owner and date |
| Hypothesis | A belief to test with users or production evidence | Metric, interview question, or experiment |
| Idea | Possible future work | Backlog only; not public capability |

Do not present a decision as already implemented, a test as user validation, or an idea as a roadmap commitment.

## 2. Trace an idea into a product decision

Do not begin with a polished requirement when the original idea is still uncertain. Keep the chain visible:

```text
owner's idea
  -> what we know / what we are guessing
  -> research questions and methods
  -> findings with sources and confidence
  -> requirement decision
  -> design hypothesis or prototype
  -> acceptance scenario
  -> implementation and release evidence
```

Research should answer a decision, not create a large report. Use interviews, existing support evidence, analytics, competitor walkthroughs, standards, technical spikes, or a small prototype according to the uncertainty. Record discarded options and why they lost; otherwise the same debate returns later without its evidence.

## 3. Minimum sources of truth

A non-trivial product should have one authoritative place for each concern. Existing equivalent documents are fine.

| Concern | Minimum contents |
|---|---|
| Product system spec | Outcome, target user, primary loop, non-goals, scope, safety and data boundaries |
| Benchmark | Idea thesis, research evidence, requirement/design trace, current baseline, attributed references, anti-benchmarks, targets and acceptance mappings |
| Acceptance matrix | Stable ID, priority, scenario, passing evidence, status |
| Engineering boundaries | Current stack, directory/API/data boundaries, reuse decisions, migration rules |
| Asset register | Routes, capabilities, saved data, discoverability and compatibility requirements |
| Delivery roadmap | Ordered slices, exit criteria, known blockers |
| Observability plan | Event schemas, redaction, retention, dashboards and alerts |
| Runbook | Detection, triage, mitigation, rollback and follow-up |
| Bad-case register | De-identified failures and rejected results, responsible layer, regression check, prevention evidence and recurrence history |

When older documents conflict, record the conflict and defer to the explicitly designated source of truth. Do not silently rewrite history.

Freeze the benchmark after the minimal product intent is clear and before task splitting or implementation. If direction changes, update and re-freeze the benchmark before changing code. See [benchmark-first.md](benchmark-first.md).

## 4. Requirement to acceptance ID

Good acceptance criteria describe a user-observable scenario, including the failure path.

```text
ID: FORM-03
Priority: P0
Scenario: A user submits the form twice while the first request is pending.
Pass: Only one durable write occurs; the button is disabled; timeout and retry are visible.
Evidence: Unit test for idempotency + browser test against preview.
Status: locally passed / preview pending
```

Avoid criteria such as “looks professional,” “uses best practices,” or “API completed.” Translate them into navigation, latency, error recovery, accessibility, persistence, or visual-consistency observations.

Use statuses that expose evidence, for example:

- `not_started`
- `implemented_unverified`
- `locally_passed`
- `preview_passed`
- `production_passed`
- `user_validated`
- `blocked`

## 5. Vertical slice task split

Split by user outcome, not by layer ownership alone.

```text
Entry -> UI state -> validated request -> authorization -> business rule
      -> persistence -> response -> user feedback -> telemetry -> recovery
```

A slice can use multiple commits, but its review should show the surrounding flow. Avoid declaring the frontend complete while its real write path, error state, or monitoring remains fictional.

## 6. Definition of done

A module is complete only when:

1. The idea, unknowns, research evidence, requirement choice and design hypothesis are traceable.
2. The benchmark is frozen, versioned, attributed, and mapped to acceptance IDs before implementation.
3. The main action is real and the public UI has no fake controls.
4. Empty, loading, failure, timeout, retry, and duplicate paths are handled where relevant.
5. Product-specific logic has automated tests.
6. Data, privacy, security, accessibility, and content rights were reviewed in proportion to risk.
7. Build and relevant quality commands pass.
8. Operational signals and a rollback path exist for released behavior.
9. Any judgment that still requires a real user is marked as unverified.
10. Every meaningful failed or rejected result is present in `BAD_CASES.md`, with a regression ID and current prevention evidence.

## 7. Feedback and bad-case loop

Capture feedback without raw private content when possible:

1. Record the situation and user-observable failure.
2. Remove identity and unnecessary content.
3. Classify the cause: positioning, information architecture, UI state, API, data, model behavior, knowledge, safety, deployment, or misunderstanding.
4. If the result is unsatisfactory, create or update a bad case before fixing it.
5. Add or update an acceptance/eval case and name the prevention guard.
6. Change the smallest responsible layer.
7. Re-run the original scenario and the surrounding regression set.
8. Record resolution evidence. If it recurs, increment the recurrence count and explain why the previous guard missed it.
9. Release narrowly and compare the original scenario.

Do not redesign the whole product in response to one unexplained anecdote.
