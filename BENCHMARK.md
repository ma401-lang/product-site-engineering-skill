# Product Site Engineering Skill benchmark

Benchmark version: `1.2`
Status: `draft`
Owner: `ma401-lang`
Last updated: 2026-10-24

This file is the direction control for the Skill repository itself. Change it before changing the Skill's delivery philosophy, public capability scope, workbench contract, or README information architecture.

## Intent

- Target user: a product owner or engineering agent delivering a real user-facing website or web app.
- Primary outcome: carry a website from an early idea through product research, requirements, design, implementation, testing, release and evidence-led improvement without losing known failures.
- Non-goal: become a framework starter, design-style catalog, prompt dump, community hub, or replacement for product-owner judgment.
- Non-negotiable boundaries: no private Psyche Guide prompts or user data; no invented production evidence; no copying reference branding or protected content.

## Baseline captured before v1.1 implementation

| Evidence ID | Baseline | Result |
|---|---|---|
| BASE-01 | Git tag `v1.0.0`, commit `c7443c4` | Product, acceptance, assets, frontend/backend, logs, AI safety and release were covered, but there was no benchmark-first control plane |
| BASE-02 | `README.md` at `v1.0.0` | Clear capability summary and quick start, but weaker explanation of why the project exists and how guides, execution and checks relate |
| BASE-03 | Five automated tests at `v1.0.0` | Initialization and structural validation worked; no release gate proved that the intended direction had been frozen |
| BASE-04 | Product-owner review of `v1.1.0` on 2026-10-24 | The public README felt fragmented and impersonal, did not quickly explain what the Skill helps someone accomplish, hid external website-building Skills in a reference file, began the benchmark too late in the product process, and had no durable bad-case memory for unsatisfactory tests |

## References

| ID | Reference | Author or publisher | Direct source | Principle adopted | Explicit exclusion |
|---|---|---|---|---|---|
| BMK-01 | Supervisor-Skills | HKUST DIAL; initiated by Yuyu Luo | https://github.com/HKUSTDial/Supervisor-Skills | Explain why the project exists, then show the guide/skill structure, capability table and quick start | News, community operations, research-domain content, wording and brand identity |
| BMK-02 | OpenAI Skills guide | OpenAI | https://developers.openai.com/api/docs/guides/tools-skills | Progressive disclosure across metadata, `SKILL.md`, references, scripts and assets | Hosted-API details as universal local-runtime behavior |
| BMK-03 | Vercel Agent Skills | Vercel | https://github.com/vercel-labs/agent-skills | Keep focused review knowledge modular and prioritize high-impact web quality rules | Vercel/Next.js assumptions when another stack is in scope |
| BMK-04 | Superpowers | obra repository | https://github.com/obra/superpowers | Preserve intent in a written artifact before planning and execution; verify small steps | Its interaction and subagent protocol where repository instructions differ |
| BMK-05 | Web standards baseline | W3C WAI, OWASP, Microsoft Playwright, Google/web.dev, Mozilla MDN | https://www.w3.org/WAI/standards-guidelines/wcag/ | Use attributable, testable standards and current primary documentation alongside visual references | Treating one automated score or vendor recommendation as complete product quality |
| BMK-06 | v1.2 product-owner review | Repository owner | Product-owner feedback recorded in `BASE-04` | Start the benchmark at idea discovery, make research and design decisions traceable, keep failed or disliked results as durable bad cases, and explain the product in connected ordinary language | Treating the feedback as a copy-only edit while leaving the workflow unchanged |

## Anti-benchmarks

| ID | Outcome to avoid | Detection |
|---|---|---|
| ANTI-01 | A large prompt that loads every guideline for every task | Root Skill stops being a concise router; unrelated references are mandatory |
| ANTI-02 | A beautiful README without executable behavior | Claims have no script, template, test or acceptance path |
| ANTI-03 | A benchmark that is rewritten after work to make the result pass | Version history does not precede implementation, or prior evidence disappears |
| ANTI-04 | A catalog of links without authors, applicability or limits | Learning-resource rows omit publisher, use case or boundary |
| ANTI-05 | Framework-specific advice presented as universal | Mutable implementation details lack scope and current primary-source verification |
| ANTI-06 | Product work begins with a pre-decided requirement and skips discovery | There is no traceable path from the original idea through user/problem evidence to the chosen requirement and design |
| ANTI-07 | The same unsatisfactory AI or product behavior returns after it was already found | Feedback exists only in chat or a transient test report; no bad-case record, regression check, owner, or resolution evidence exists |
| ANTI-08 | The homepage sounds complete but readers still cannot tell what they can do next | Capability nouns dominate; there is no concrete end-to-end example, visible external Skill stack, or plain-language outcome |

## Weighted rubric

Scores use this anchor: `1` absent, `2` ad hoc, `3` documented, `4` executable and tested, `5` release-gated with traceable evidence.

| Dimension | Weight | v1.0 baseline | v1.1 target | v1.1 evidence |
|---|---:|---:|---:|---|
| Idea-to-product continuity | 20 | 2 | 5 | Benchmark and workbench trace idea thesis, research evidence, requirement decisions, design hypotheses and delivery evidence |
| Durable bad-case learning | 20 | 1 | 5 | Every unsatisfactory test or user-reported failure has a structured record, responsible layer, prevention check, status and recurrence history |
| End-to-end website engineering coverage | 15 | 4 | 4 | Frontend, backend, logs, AI, deployment, rollback and feedback remain connected to the expanded discovery loop |
| Repository learnability and human clarity | 15 | 2 | 4 | README leads with concrete outcomes and one connected example, uses ordinary sentences, and avoids slogan-heavy contrast writing |
| External website-Skill usability | 10 | 2 | 4 | The README names the actual Skills, authors, direct paths, use cases and composition boundaries instead of hiding them behind a resource summary |
| Reproducibility and release gates | 10 | 5 | 5 | Tests cover benchmark completeness and bad-case persistence; strict audit blocks incomplete release evidence |
| Privacy, safety and evidence honesty | 10 | 4 | 4 | Existing data/logging/AI boundaries remain non-negotiable; bad cases are de-identified before storage |

Weighted target: `450 / 500` (equivalent to `4.5 / 5`). This number is a compact summary; the evidence column and automated checks are authoritative.

## Direction-change protocol

1. Set status back to `draft` and increment the version.
2. Record new evidence or the user decision that invalidates the old direction.
3. Update references, anti-benchmarks, rubric, affected acceptance cases and tests.
4. Review the diff against the non-goals and privacy/safety boundaries.
5. Re-freeze the benchmark before implementation of the new direction.

## Freeze record

| Version | Date | Decision |
|---|---|---|
| 1.0 | 2026-10-24 | Initial reusable website product engineering Skill released locally |
| 1.1 | 2026-10-24 | Adopt benchmark-first delivery, attributed web-learning sources, README information hierarchy and an executable release gate |
| 1.2 | 2026-10-24 | Draft direction: extend benchmark control from idea and research through design and delivery; add durable bad-case learning; rewrite the public explanation around concrete use |
