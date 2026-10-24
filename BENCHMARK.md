# Product Site Engineering Skill benchmark

Benchmark version: `1.1`
Status: `frozen`
Owner: `ma401-lang`
Last updated: 2026-10-24

This file is the direction control for the Skill repository itself. Change it before changing the Skill's delivery philosophy, public capability scope, workbench contract, or README information architecture.

## Intent

- Target user: a product owner or engineering agent delivering a real user-facing website or web app.
- Primary outcome: turn ambiguous website work into a benchmarked, testable, observable and releasable vertical slice.
- Non-goal: become a framework starter, design-style catalog, prompt dump, community hub, or replacement for product-owner judgment.
- Non-negotiable boundaries: no private Psyche Guide prompts or user data; no invented production evidence; no copying reference branding or protected content.

## Baseline captured before v1.1 implementation

| Evidence ID | Baseline | Result |
|---|---|---|
| BASE-01 | Git tag `v1.0.0`, commit `c7443c4` | Product, acceptance, assets, frontend/backend, logs, AI safety and release were covered, but there was no benchmark-first control plane |
| BASE-02 | `README.md` at `v1.0.0` | Clear capability summary and quick start, but weaker explanation of why the project exists and how guides, execution and checks relate |
| BASE-03 | Five automated tests at `v1.0.0` | Initialization and structural validation worked; no release gate proved that the intended direction had been frozen |

## References

| ID | Reference | Author or publisher | Direct source | Principle adopted | Explicit exclusion |
|---|---|---|---|---|---|
| BMK-01 | Supervisor-Skills | HKUST DIAL; initiated by Yuyu Luo | https://github.com/HKUSTDial/Supervisor-Skills | Explain why the project exists, then show the guide/skill structure, capability table and quick start | News, community operations, research-domain content, wording and brand identity |
| BMK-02 | OpenAI Skills guide | OpenAI | https://developers.openai.com/api/docs/guides/tools-skills | Progressive disclosure across metadata, `SKILL.md`, references, scripts and assets | Hosted-API details as universal local-runtime behavior |
| BMK-03 | Vercel Agent Skills | Vercel | https://github.com/vercel-labs/agent-skills | Keep focused review knowledge modular and prioritize high-impact web quality rules | Vercel/Next.js assumptions when another stack is in scope |
| BMK-04 | Superpowers | obra repository | https://github.com/obra/superpowers | Preserve intent in a written artifact before planning and execution; verify small steps | Its interaction and subagent protocol where repository instructions differ |
| BMK-05 | Web standards baseline | W3C WAI, OWASP, Microsoft Playwright, Google/web.dev, Mozilla MDN | https://www.w3.org/WAI/standards-guidelines/wcag/ | Use attributable, testable standards and current primary documentation alongside visual references | Treating one automated score or vendor recommendation as complete product quality |

## Anti-benchmarks

| ID | Outcome to avoid | Detection |
|---|---|---|
| ANTI-01 | A large prompt that loads every guideline for every task | Root Skill stops being a concise router; unrelated references are mandatory |
| ANTI-02 | A beautiful README without executable behavior | Claims have no script, template, test or acceptance path |
| ANTI-03 | A benchmark that is rewritten after work to make the result pass | Version history does not precede implementation, or prior evidence disappears |
| ANTI-04 | A catalog of links without authors, applicability or limits | Learning-resource rows omit publisher, use case or boundary |
| ANTI-05 | Framework-specific advice presented as universal | Mutable implementation details lack scope and current primary-source verification |

## Weighted rubric

Scores use this anchor: `1` absent, `2` ad hoc, `3` documented, `4` executable and tested, `5` release-gated with traceable evidence.

| Dimension | Weight | v1.0 baseline | v1.1 target | v1.1 evidence |
|---|---:|---:|---:|---|
| Benchmark-first direction control | 25 | 1 | 5 | Workbench template, reference guide, acceptance IDs and strict `--release` audit |
| End-to-end website engineering coverage | 20 | 4 | 4 | Existing frontend/backend/logging/AI/release guides plus performance, compatibility, metadata and discoverability checks |
| Repository learnability | 15 | 3 | 4 | README follows why → workflow → capabilities → structure → quick start without a community section |
| Source attribution and learning boundaries | 15 | 2 | 4 | Website and prompting resource lists name authors/publishers, uses and limits |
| Reproducibility and verification | 15 | 4 | 5 | Six automated tests include a failing draft benchmark and passing frozen benchmark release case |
| Privacy, safety and evidence honesty | 10 | 4 | 4 | Existing data/logging/AI boundaries preserved; references cannot override non-negotiable constraints |

Weighted target: `440 / 500` (equivalent to `4.4 / 5`). This number is a compact summary; the evidence column and automated checks are authoritative.

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

