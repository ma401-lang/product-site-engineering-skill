# {{PROJECT_NAME}} benchmark

Initialized: {{DATE}}

Benchmark version: `0.1`
Status: `draft`
Owner: `unassigned`
Last updated: {{DATE}}

Change rule: update this file, affected acceptance IDs, and the decision log before implementation changes direction. Re-freeze the benchmark after review; never rewrite old evidence to make a result pass.

## 1. Original idea and uncertainty

- Idea in the product owner's own words:
- Why this matters now:
- Target user and triggering situation:
- Current workaround or alternative:
- Facts already known:
- Assumptions still unverified:
- Most expensive or risky assumption:
- Questions that could change whether or what we build:

## 2. Product research plan and evidence

Use only enough research to make the next decision. Keep source observations separate from team interpretation, and remove personal data from this workbench.

| Research ID | Decision question | Method or source | Participant/source boundary | Finding or evidence reference | Confidence and limitation | Decision impact |
|---|---|---|---|---|---|---|
| RSH-01 |  |  |  |  |  |  |

## 3. Requirement and design trace

Link every material choice to the idea or research evidence that supports it. Mark an unsupported choice as a hypothesis and say how it will be tested.

| Decision ID | Idea/research IDs | Requirement or product decision | Design hypothesis/prototype | Rejected alternative and reason | Validation/acceptance IDs |
|---|---|---|---|---|---|
| DEC-01 |  |  |  |  |  |

## 4. Intent and comparison boundary

- Target user:
- Primary outcome:
- Scope of this benchmark:
- Explicit non-goals:
- Protected assets and non-negotiable safety/data/content boundaries:

## 5. Current baseline captured before implementation

| Evidence ID | Scenario or surface | Method | Result or artifact path | Captured on |
|---|---|---|---|---|
| BASE-01 | Primary flow | Browser walkthrough |  | {{DATE}} |

## 6. References

Use two to five comparable products, standards, or local baselines. Record the creator or publisher and a direct source. Learn principles; do not copy protected content, brand identity, or interaction without checking rights and fit.

| ID | Reference | Author or publisher | URL or local evidence | Principle to learn | What not to copy |
|---|---|---|---|---|---|
| BMK-01 | Replace with a relevant reference | Replace with author or publisher | — |  |  |
| BMK-02 | Replace with a relevant reference | Replace with author or publisher | — |  |  |

## 7. Anti-benchmarks

| ID | Outcome to avoid | Why it would harm this product | Detection evidence |
|---|---|---|---|
| ANTI-01 | A polished shell with fake or dead controls | Breaks trust and hides incomplete behavior | Public-control inventory + browser test |
| ANTI-02 | A redesign that hides a protected capability | Reduces product value while appearing simpler | Before/after asset map |
| ANTI-03 | A known unsatisfactory result returns | Failure knowledge was left in chat or a test report instead of a durable bad case and regression guard | `BAD_CASES.md` recurrence history + regression test |

## 8. Weighted quality rubric

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

## 9. Decision and change history

| Benchmark version | Date | Status | Decision or change | Affected acceptance IDs | Owner |
|---|---|---|---|---|---|
| 0.1 | {{DATE}} | draft | Initial benchmark scaffold | BENCH-01, BENCH-02 | unassigned |

## 10. Freeze checklist

- [ ] The original idea, assumptions, unknowns and riskiest belief are recorded.
- [ ] Research questions are tied to decisions, and findings include method/source, confidence and limitations.
- [ ] Material requirements and design hypotheses trace to idea/research IDs or are marked for validation.
- [ ] Current-state evidence was captured before implementation.
- [ ] Each external reference has an author or publisher and a direct verified URL.
- [ ] Useful principles and excluded copying are explicit.
- [ ] Anti-benchmarks cover the most likely drift.
- [ ] Relevant rubric weights total 100 and scoring anchors are observable.
- [ ] Targets map to acceptance IDs.
- [ ] Safety, data, content rights, and protected assets remain non-negotiable.
- [ ] Existing bad cases were reviewed and relevant prevention guards are mapped to acceptance/eval IDs.
- [ ] Owner approved this version and changed `Status` to `frozen`.
