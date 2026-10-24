# Prompt engineering and evaluation resources

Last link verification: 2026-10-24. These are learning references, not text to copy wholesale. Model-specific advice changes; always pair a prompt change with representative tests.

## Official guides

| Resource | Author or publisher | Best use | Important limit |
|---|---|---|---|
| [OpenAI: Prompting](https://developers.openai.com/api/docs/guides/prompting) | OpenAI | Production prompt organization, versioning, examples, and release tests | OpenAI-specific API details can change |
| [OpenAI: Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering) | OpenAI | Clear instructions, message roles, context, examples, and current model guidance | Read the model-specific guide as well as general patterns |
| [OpenAI: ChatGPT Enterprise Prompting Guide](https://developers.openai.com/cookbook/examples/chatgpt/chatgpt_prompt_guide/chatgpt_prompt_guide) | OpenAI | Accessible, example-led prompting and meta-prompting | A good starting guide, not a substitute for product evals |
| [OpenAI: Skills](https://developers.openai.com/api/docs/guides/tools-skills) | OpenAI | Packaging repeatable instructions, scripts, references, and assets | A Skill is workflow context, not privileged code or a security boundary |
| [Anthropic: Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) | Anthropic | Start from success criteria and empirical evaluation before tuning prompts | Techniques and model names are Claude-specific |
| [Google: Prompt design strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies) | Google | Clear structure, few-shot examples, iteration, long-context organization | Sampling and model behavior differ across Gemini versions |

## Community and tooling references

| Resource | Author or publisher | Best use | Important limit |
|---|---|---|---|
| [DAIR.AI Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | DAIR.AI and project contributors | Broad map of prompting techniques, papers, lectures, and notebooks | Community-curated; verify claims against primary sources and current model docs |
| [Promptfoo](https://github.com/promptfoo/promptfoo) | Promptfoo maintainers and contributors | Comparing prompts/models and adding deterministic or rubric assertions | Evaluation output can contain sensitive prompts/responses; configure storage and redaction deliberately |
| [OpenAI Evals](https://github.com/openai/evals) | OpenAI and project contributors | Learning eval structure and reproducible task cases | Do not adopt a framework before the case volume justifies it |
| [OpenAI Cookbook](https://github.com/openai/openai-cookbook) | OpenAI and project contributors | Runnable examples and evaluation patterns | Examples may target a particular API generation; check current docs |

## Engineering references used in the underlying workflow

These public projects informed the general engineering lessons, without copying their product code:

- [Vercel AI Chatbot](https://github.com/vercel/chatbot) — Vercel: typed request contracts, UI/provider separation, and end-to-end interaction testing.
- [Mem0](https://github.com/mem0ai/mem0) and [Memory Benchmarks](https://github.com/mem0ai/memory-benchmarks) — Mem0 maintainers: separating user/session memory, retrieval, generation, and evaluation.
- [Promptfoo](https://github.com/promptfoo/promptfoo) — Promptfoo maintainers, and [OpenAI Evals](https://github.com/openai/evals) — OpenAI: turning real failures into repeatable cases and distinguishing deterministic checks from semantic grading.

## Recommended learning order

1. Define success and forbidden outcomes.
2. Create a small, representative eval set.
3. Write the shortest prompt that communicates the task, context, constraints, and output contract.
4. Add varied examples for the failures the model actually makes.
5. Fix state, retrieval, tools, or deterministic guards when the prompt is not the responsible layer.
6. Run repeated checks on the production model and record first-pass, retry, and fallback separately.
7. Revisit the prompt when the model, API, product boundary, or user population changes.

The core lesson is not “find the perfect template.” It is to treat prompt behavior as versioned application behavior with evidence and rollback.
