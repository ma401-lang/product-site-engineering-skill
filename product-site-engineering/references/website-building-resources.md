# Website-building skills and primary learning resources

Last link verification: 2026-10-24. “Author” below means the named creator when the source provides one; otherwise it means the repository owner or publishing organization. These links are learning inputs, not instructions to copy entire prompts, source code, branding, or copyrighted content. For stage-by-stage composition of the actual Skills, read [external-skill-integration.md](external-skill-integration.md).

## Skills and engineering workflows

| Resource | Author or publisher | What is worth learning | Boundary |
|---|---|---|---|
| [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | HKUST DIAL; initiated by Yuyu Luo (骆昱宇) | A clear repository story: why the project exists, a Guide + executable Skills dual track, a scannable capability table, and one-step quick start | Its domain is research supervision. This Skill borrows information architecture only; it does not copy its text, research methods, news feed, or community section |
| [Frontend Design plugin](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design) | Anthropic; plugin authors Prithvi Rajasekaran and Alexander Bricken | Commit to a coherent aesthetic direction and turn it into production-ready interface code instead of generic AI styling | Visual distinctiveness cannot override product scope, accessibility, performance, or evidence |
| [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills) — especially [Web Design Guidelines](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) and [React Best Practices](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) | Vercel | Prioritized interface review and performance rules; keep focused review Skills separate from the main builder | Framework-specific techniques need current verification; do not fetch mutable instructions into a trusted workflow without pinning or review |
| [UI/UX Pro Max Skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | nextlevelbuilder | Searchable design systems, product-type guidance, palettes, typography, interaction and multi-stack examples | A large style catalog can create trend mixing. Pick one benchmarked direction and validate it with users and standards |
| [Superpowers](https://github.com/obra/superpowers) — especially [brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md) and [writing-plans](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md) | obra repository | Preserve intent in a written design, plan from the spec, use small verifiable tasks, and keep execution evidence | Do not import its interaction protocol wholesale when repository or user instructions define a different workflow |
| [OpenAI Skills guide](https://developers.openai.com/api/docs/guides/tools-skills) | OpenAI | Progressive disclosure: concise discovery metadata, workflow in `SKILL.md`, background in `references/`, deterministic mechanics in `scripts/`, reusable files in `assets/` | A Skill is reusable context and tooling, not a security boundary or proof of correctness |

## Web standards and authoritative tutorials

| Resource | Author or publisher | Use it for |
|---|---|---|
| [Playwright Best Practices](https://playwright.dev/docs/best-practices) | Microsoft Playwright team | User-visible end-to-end behavior, isolated tests, resilient locators, web-first assertions, CI traces and cross-browser checks |
| [WCAG 2 overview](https://www.w3.org/WAI/standards-guidelines/wcag/) | W3C Web Accessibility Initiative and Accessibility Guidelines Working Group | Stable accessibility success criteria and conformance language; prefer the current WCAG 2.2 resources when appropriate |
| [OWASP ASVS](https://asvs.owasp.org/) | OWASP Foundation and ASVS project team | Versioned, testable web application security requirements; choose a level appropriate to the product risk |
| [Core Web Vitals](https://web.dev/explore/learn-core-web-vitals) | web.dev / Google Chrome team | Field-oriented loading, responsiveness and visual-stability quality; record actual tools, populations and dates in the benchmark |
| [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) | Google Search Central | People-first content, crawlability, descriptive structure, metadata and discoverability without promising rankings |
| [MDN Learn Web Development](https://developer.mozilla.org/en-US/docs/Learn_web_development) | Mozilla and MDN contributors | Standards-based HTML, CSS, JavaScript, forms, semantics, accessibility and web performance fundamentals |
| [TanStack Start overview](https://tanstack.com/start/latest/docs/framework/react/overview) | TanStack maintainers | Verify current framework behavior, routing, SSR, streaming and server-function boundaries when TanStack Start is actually in scope |
| [TanStack Start on Cloudflare Workers](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/) | Cloudflare Developer Documentation | Current adapter/runtime configuration, bindings, preview and deploy workflow for this specific pairing |

## How to use these sources in a benchmark

1. Pick only references comparable to the target user, task, risk, and delivery environment.
2. Record the direct URL, author or publisher, version or verification date, and the principle being learned.
3. Add at least one standard or measured baseline, not only visual inspiration.
4. State what will not be copied: brand, copyrighted content, private workflow, irrelevant architecture, or unverified claims.
5. Turn each adopted principle into a benchmark dimension and, when behavior matters, a stable acceptance ID.
6. Re-check mutable framework and hosting documentation at implementation and release time.
