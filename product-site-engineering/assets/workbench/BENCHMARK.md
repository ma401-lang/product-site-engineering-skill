# {{PROJECT_NAME}} benchmark

Initialized: {{DATE}}

Benchmark version: `0.1`
Status: `draft`
Owner: `unassigned`
Last updated: {{DATE}}

Change rule: update this file, affected acceptance IDs, and the decision log before implementation changes direction. Re-freeze the benchmark after review; never rewrite old evidence to make a result pass.

## Intent and comparison boundary

- Target user:
- Primary outcome:
- Scope of this benchmark:
- Explicit non-goals:
- Protected assets and non-negotiable safety/data/content boundaries:

## Current baseline captured before implementation

| Evidence ID | Scenario or surface | Method | Result or artifact path | Captured on |
|---|---|---|---|---|
| BASE-01 | Primary flow | Browser walkthrough |  | {{DATE}} |

## References

Use two to five comparable products, standards, or local baselines. Record the creator or publisher and a direct source. Learn principles; do not copy protected content, brand identity, or interaction without checking rights and fit.

| ID | Reference | Author or publisher | URL or local evidence | Principle to learn | What not to copy |
|---|---|---|---|---|---|
| BMK-01 | Replace with a relevant reference | Replace with author or publisher | — |  |  |
| BMK-02 | Replace with a relevant reference | Replace with author or publisher | — |  |  |

## Anti-benchmarks

| ID | Outcome to avoid | Why it would harm this product | Detection evidence |
|---|---|---|---|
| ANTI-01 | A polished shell with fake or dead controls | Breaks trust and hides incomplete behavior | Public-control inventory + browser test |
| ANTI-02 | A redesign that hides a protected capability | Reduces product value while appearing simpler | Before/after asset map |

## Weighted quality rubric

Use only relevant dimensions. Weights must total 100 before freezing. Define scoring anchors in the measurement column instead of relying on an unexplained subjective score.

| Dimension | Weight | Current baseline | Target | Measurement and scoring anchors | Acceptance IDs |
|---|---:|---|---|---|---|
| User outcome and primary flow | 25 |  |  |  | FLOW-01 |
| Information architecture and protected assets | 15 |  |  |  | ASSET-01 |
| Interaction states and recovery | 15 |  |  |  | UI-01 |
| Accessibility and responsive behavior | 10 |  |  |  | A11Y-01 |
| Performance and reliability | 10 |  |  |  | REL-01 |
| Security, privacy, and data boundaries | 15 |  |  |  | DATA-01 |
| Observability and operations | 10 |  |  |  | OBS-01 |

## Decision and change history

| Benchmark version | Date | Status | Decision or change | Affected acceptance IDs | Owner |
|---|---|---|---|---|---|
| 0.1 | {{DATE}} | draft | Initial benchmark scaffold | BENCH-01, BENCH-02 | unassigned |

## Freeze checklist

- [ ] Current-state evidence was captured before implementation.
- [ ] Each external reference has an author or publisher and a direct verified URL.
- [ ] Useful principles and excluded copying are explicit.
- [ ] Anti-benchmarks cover the most likely drift.
- [ ] Relevant rubric weights total 100 and scoring anchors are observable.
- [ ] Targets map to acceptance IDs.
- [ ] Safety, data, content rights, and protected assets remain non-negotiable.
- [ ] Owner approved this version and changed `Status` to `frozen`.
