# Benchmark-first delivery

Use this reference from the moment a non-trivial website idea is being shaped. A benchmark is the product's versioned reasoning trail and comparison frame: why the idea matters, what research found, which requirement and design were chosen, what good means, what must not drift, and what evidence will show improvement.

It is not a mood board, a list of fashionable sites, or permission to copy another product.

## Why the benchmark comes first

Without a frozen benchmark, teams often change direction through scattered comments, optimize whichever detail is most visible, and move the quality bar after implementation. A benchmark prevents that by turning taste and intent into a versioned decision artifact before code changes begin.

The benchmark complements, rather than replaces, the other sources of truth:

| Artifact | Question it answers |
|---|---|
| Product system spec | What product and user outcome are we responsible for? |
| Benchmark | What quality direction and comparison frame will keep the work from drifting? |
| Acceptance matrix | Which concrete scenarios must pass, and with what evidence? |
| Engineering boundaries | Which technical constraints and interfaces must the solution respect? |

## Required sequence

1. **Preserve the original idea.** Record it in the owner's language, why it matters now, the target situation, current alternatives, known facts, assumptions, unknowns, and the riskiest belief.
2. **Plan the research.** Turn unknowns into decision questions. For each question choose the smallest useful method, owner, source population or material, stopping rule, and privacy boundary.
3. **Record evidence.** Keep the source or method, author/publisher where relevant, date, finding, confidence, limitation, and decision impact. Separate what a user said, what analytics showed, what a standard requires, and what the team inferred.
4. **Choose requirements and design hypotheses.** Link each material requirement and design direction to idea/evidence IDs. Record discarded options and what future evidence would reopen the decision.
5. **Capture the current baseline.** Measure the existing flow or substitute before changing it: screenshots, route inventory, task completion, error behavior, accessibility, performance, logs, or other relevant evidence.
6. **Select references deliberately.** Use two to five strong examples, standards, or current product baselines. For each one record its author or publisher, URL or local evidence, verification date, useful principle, and what must not be copied.
7. **Distill principles, not pixels.** Translate references into observable dimensions such as information hierarchy, task completion, recovery, accessibility, visual coherence, performance, privacy, and operability.
8. **Define anti-benchmarks.** Name tempting but harmful outcomes: decorative complexity, hidden protected features, generic AI styling, misleading controls, overcollection, fragile animation, skipped research, or repeated known failures.
9. **Score and set targets.** Give each relevant dimension a weight, current score or baseline, target, measurement method, and acceptance IDs. Omit irrelevant dimensions rather than pretending every product needs the same rubric.
10. **Freeze the benchmark.** Set `Status: frozen`, assign a version, owner, and date, then record the decision. Only then split tasks or implement.
11. **Evaluate and learn.** Use the same scenarios and methods for baseline and candidate. Send every meaningful failed or rejected result to `BAD_CASES.md`, then attach a regression check and resolution evidence.

## Default quality dimensions

Use only the dimensions that affect the product outcome. A useful starting set is:

| Dimension | Example evidence |
|---|---|
| User outcome | First useful action, task completion, abandonment, user confirmation |
| Information architecture | Route and entry-point map, findability task, protected-asset map |
| Interaction completeness | Empty/loading/error/timeout/retry/duplicate/offline behavior |
| Content clarity | Comprehension check, terminology audit, action-label specificity |
| Accessibility | Keyboard flow, focus, semantic names, announcements, WCAG checks |
| Visual system | Token consistency, hierarchy, responsive screenshots, long-content stress test |
| Performance | Field or lab measures, request waterfalls, bundle or server timings |
| Security and privacy | Threat scenarios, data inventory, secret scan, ASVS-derived checks |
| Reliability and operations | Request correlation, alerts, deploy and rollback rehearsal |
| Discoverability | Metadata, crawl/index behavior, share previews, internal navigation |

Weights should total 100 for a scored benchmark. Scores are useful only when the scoring anchors are written down; a bare “8/10” is not evidence.

## Direction-change rule

When the product owner changes the intended direction:

1. edit the benchmark first;
2. increment its version and return its status to `draft`;
3. record why the old frame is no longer sufficient;
4. update affected research conclusions, product facts, acceptance IDs, protected-asset mappings, bad cases, and roadmap items;
5. re-freeze the benchmark;
6. then change implementation.

Do not rewrite old evidence or retroactively lower a target to make the current build pass. Preserve the decision history so a reviewer can tell whether the product improved or the ruler changed.

## Benchmark review checklist

- The references solve a comparable user or engineering problem, not merely share a visual style.
- The original idea, important unknowns, research methods, findings and confidence are visible.
- Material requirements and design hypotheses trace to evidence or are clearly marked as assumptions.
- Every external reference has an author or publisher, a direct URL, and a verification date.
- Current-state evidence was captured before implementation.
- Useful principles and excluded copying are both explicit.
- Anti-benchmarks name likely drift, not vague dislikes.
- Targets map to stable acceptance IDs and executable or inspectable evidence.
- Product safety, data boundaries, rights, and protected assets cannot be traded away by a weighted score.
- A change in direction updates the benchmark before the code.
- Failed tests, rejected outputs and repeated complaints are captured in the bad-case register rather than left in transient conversation memory.
