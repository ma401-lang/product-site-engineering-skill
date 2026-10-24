# External website Skills: when and how to compose them

Use this reference when a product needs specialized help beyond the core delivery workflow. These are real external Skills or Skill collections. Link to their maintained source, review the current license and instructions, and install them separately when the target agent supports them. Do not copy mutable third-party content into this Skill or silently let it override repository rules.

## Recommended stack

| Stage | Skill | Author or publisher | Direct source | What it contributes | Composition boundary |
|---|---|---|---|---|---|
| Idea and discovery | `brainstorming` | Jesse Vincent / obra and Prime Radiant contributors | https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md | Questions that expose intent, prior attempts, disliked outcomes and unresolved decisions before building | Keep this repository's authority and approval rules; do not import mandatory subagent or interaction policies automatically |
| Planning | `writing-plans` | Jesse Vincent / obra and Prime Radiant contributors | https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md | Small implementation tasks with explicit files, tests and verification | Run only after the local benchmark, requirements and design direction are approved |
| Visual direction | `frontend-design` | Anthropic; Prithvi Rajasekaran and Alexander Bricken | https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md | Deliberate typography, layout, motion and subject-specific visual choices | Aesthetic ambition cannot weaken usability, accessibility, protected assets, performance or product evidence |
| Design-system exploration | `ui-ux-pro-max` | nextlevelbuilder | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | Searchable product patterns, palettes, typography and multi-stack UI guidance | Use it to compare options, then select one benchmarked direction; do not mix catalog trends into one interface |
| UI review | `web-design-guidelines` | Vercel | https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md | Focused review of interface and accessibility rules | Pin or review fetched mutable guidance before trusting it in a release gate |
| React performance | `react-best-practices` | Vercel | https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices | React and Next.js performance review ordered by likely impact | Apply only when the stack matches; verify framework details against current official documentation |

## Composition recipes

### A rough idea with no validated product direction

1. Use `brainstorming` for the conversation and prototype questions.
2. Record the result in the local benchmark's idea, research and decision sections.
3. Freeze the chosen direction and acceptance IDs.
4. Use `writing-plans` to turn that approved direction into implementation tasks.
5. Keep delivery, logs, deployment, feedback and bad-case memory under `product-site-engineering`.

### A product direction that needs a stronger interface

1. Give `frontend-design` or `ui-ux-pro-max` the product's audience, real content, constraints, protected assets and anti-benchmarks.
2. Save the selected visual direction as a design hypothesis with reasons and rejected options.
3. Implement one coherent path.
4. Review it with `web-design-guidelines`, then run the product's accessibility, responsive, performance and browser tests.
5. Put every rejected or failing result into `BAD_CASES.md` before revising.

### A React site that is already visually complete

1. Run `react-best-practices` only on the relevant React surface.
2. Translate findings into local acceptance IDs; do not treat the external report as implementation.
3. Measure the same performance scenario before and after.
4. Preserve any regression as a bad case and keep the prevention test.

## Installation and trust rule

Installation commands differ between Codex, Claude Code and other Agent Skills-compatible tools. Follow each tool's current official installer and the external repository's README. Review the exact files and license before installation, prefer a pinned release or commit for repeatable work, and keep third-party updates out of a release until their effect has been re-evaluated against the local benchmark.
