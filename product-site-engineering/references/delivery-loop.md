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

## 2. Minimum sources of truth

A non-trivial product should have one authoritative place for each concern. Existing equivalent documents are fine.

| Concern | Minimum contents |
|---|---|
| Product system spec | Outcome, target user, primary loop, non-goals, scope, safety and data boundaries |
| Acceptance matrix | Stable ID, priority, scenario, passing evidence, status |
| Engineering boundaries | Current stack, directory/API/data boundaries, reuse decisions, migration rules |
| Asset register | Routes, capabilities, saved data, discoverability and compatibility requirements |
| Delivery roadmap | Ordered slices, exit criteria, known blockers |
| Observability plan | Event schemas, redaction, retention, dashboards and alerts |
| Runbook | Detection, triage, mitigation, rollback and follow-up |

When older documents conflict, record the conflict and defer to the explicitly designated source of truth. Do not silently rewrite history.

## 3. Requirement to acceptance ID

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

## 4. Vertical slice task split

Split by user outcome, not by layer ownership alone.

```text
Entry -> UI state -> validated request -> authorization -> business rule
      -> persistence -> response -> user feedback -> telemetry -> recovery
```

A slice can use multiple commits, but its review should show the surrounding flow. Avoid declaring the frontend complete while its real write path, error state, or monitoring remains fictional.

## 5. Definition of done

A module is complete only when:

1. The goal, boundary, and acceptance IDs are recorded.
2. The main action is real and the public UI has no fake controls.
3. Empty, loading, failure, timeout, retry, and duplicate paths are handled where relevant.
4. Product-specific logic has automated tests.
5. Data, privacy, security, accessibility, and content rights were reviewed in proportion to risk.
6. Build and relevant quality commands pass.
7. Operational signals and a rollback path exist for released behavior.
8. Any judgment that still requires a real user is marked as unverified.

## 6. Feedback loop

Capture feedback without raw private content when possible:

1. Record the situation and user-observable failure.
2. Remove identity and unnecessary content.
3. Classify the cause: positioning, information architecture, UI state, API, data, model behavior, knowledge, safety, deployment, or misunderstanding.
4. Add or update an acceptance/eval case before fixing.
5. Change the smallest responsible layer.
6. Re-run the affected slice and regression set.
7. Release narrowly and compare the original scenario.

Do not redesign the whole product in response to one unexplained anecdote.
