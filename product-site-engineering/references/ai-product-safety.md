# AI product engineering and safety

Use this reference only when the website calls a model, retrieves knowledge, stores memory, or makes claims in a high-stakes domain.

## Pipeline, not prompt

Treat production behavior as a pipeline:

```text
validated input -> authorization and rate control -> risk/state classification
-> approved context retrieval -> model call -> deterministic output checks
-> optional bounded retry -> safe fallback -> user-visible result -> eval signal
```

A longer system prompt cannot replace missing authentication, data boundaries, source governance, output enforcement, or evaluation.

## Server-only boundary

Keep prompts, provider credentials, routing, safety policies, private knowledge, raw dependency errors, and privileged memory writes on the server. Send the browser only what the current interface needs.

Make provider and model selection configurable. Compare candidates against the same eval cases; do not bind public product language to a vendor that may change.

## Prompt lifecycle

- Store prompts in named, version-controlled modules.
- Build dynamic parts through typed, validated arguments.
- Keep stable behavioral instructions separate from untrusted user content and retrieved text.
- Review prompt changes with the code and acceptance cases they affect.
- Record prompt/eval version in restricted operational metadata, not public UI.
- Prefer concise instructions plus representative examples over an unbounded rule dump.

## Failure-driven evaluation

1. Capture a real failure with identity removed.
2. Label the failure type before changing the system.
3. Write observable pass and forbidden conditions.
4. Fix the smallest responsible layer: state, retrieval, prompt, tool contract, guard, or interface.
5. Run deterministic tests.
6. Run repeated production-model checks for nondeterministic behavior.
7. Use calibrated human review for tone, safety, and domain judgment.
8. Release narrowly and track first-pass, retry, and fallback separately.

Do not let an LLM judge be the only safety gate. Calibrate it against human-labeled cases and retain deterministic checks for hard boundaries.

## Knowledge and citations

Separate source text, user notes, human summaries, and AI explanations. Each production record should include provenance, rights, review status, last verification, and intended/forbidden use. Only approved records enter retrieval.

When evidence is absent, say so. Never invent quotations, page numbers, cases, diagnoses, or source support. Retrieval relevance does not prove a claim is true.

## Memory

Use layers:

- current-turn context;
- recent session context;
- temporary, disclosed memory with an expiry;
- long-term memory explicitly approved by the user.

Long-term memory must be viewable, correctable, deletable, and scoped to the correct user. Keep user-stated facts separate from model hypotheses. Do not save sensitive inferences as facts.

## Injection and output safety

- Treat user input, web pages, files, retrieved passages, and tool output as untrusted data.
- Delimit instructions from data and restrict tools by least privilege.
- Validate tool arguments and re-authorize the resulting action.
- Inspect the complete candidate output before releasing sensitive content.
- Do not echo internal rules, hidden context, file paths, environment names, or provider errors.
- Bound retries; after repeated failure, return a deterministic, non-deceptive fallback.

## High-stakes domains

For health, mental health, legal, finance, safety, children, or other regulated contexts:

- define what the product is and is not;
- separate education or reflection from diagnosis and professional advice;
- stop deeper exploration when immediate danger is plausible;
- do not rely on raw keyword matching alone;
- test negation, quotation, third-person discussion, historical events, misspellings, and indirect language;
- obtain qualified human review before expanding use;
- never claim continuous monitoring or third-party intervention unless it truly exists.

Human review and local legal analysis are release inputs, not optional polish.
