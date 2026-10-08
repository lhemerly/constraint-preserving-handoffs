# Constraint-Preserving Handoffs (CPH)

CPH is an experimental way to make agent handoffs compact while preserving every consequential constraint. **Use structured CPH as the default:** state the action, authoritative inputs, scope and permissions, checks and outcomes, and status plus next action.

The originally observed form was dense, single-paragraph technical prose: telegraphic clauses, compressed connectors, shared references, compact status wording and sometimes selective word fusion. The labeled structured template is a later designed variant. They share an intent; they are different formats.

## Use it

- Copy either format from [agent instructions](AGENT-INSTRUCTIONS.md); structured comes first and is recommended.
- Read the [short specification](SPEC.md) and [synthetic worked examples](EXAMPLES.md).
- Inspect [dense prose and its normally spaced expansion](DENSE-PROSE.md).
- Review the [benchmark method, results and reproduction](benchmarks/README.md) and [future evaluation plan](EVALUATION.md).

```text
Goal/action: Repair the hypothetical catalog validator's duplicate-code detection.
Inputs/provenance: Synthetic requirement note CAT-A here; hypothetical catalog-cases.json is authoritative test input.
Scope/constraints: Validator/tests only. Local edits authorized; no publication. Case-sensitive comparisons; preserve null codes. Whitespace significance unknown. If the rule is missing, stop and request it before trimming.
Checks: After repair, run duplicate-code regression and validator suite. Null-code test passed; duplicate-code regression failed; full suite not run. These are supplied claims.
Status/next: Patch incomplete. Inspect the failing case, then repair.
```

Adapt labels and fields to the task; avoid irrelevant boilerplate. Use normal spacing and explicit boundaries in structured handoffs. Never omit permissions, uncertainty, stop conditions, test outcomes or source provenance to save tokens. Do not replace a conditional permission or requirement with an unconditional rule, an added prohibition, or “if and only if.”

CPH governs agent handoffs. It does not require terse or opaque replies to users.

## What the evidence says

A small, synthetic interpretation experiment compared three two-way formats across three receiver models and three tasks: 27 answers, 18 scored facts each. The separate local review found:

| Format | Strict pass / fail / indeterminate | Facts retained | Visible token proxy |
| --- | --- | --- | --- |
| Normal prose | 7 / 2 / 0 | 162/162 | 6,099 |
| Dense composite | 6 / 2 / 1 | 162/162 | 4,340 |
| Structured fields | 8 / 0 / 1 | 161/162 | 5,457 |

Dense used 28.8% fewer visible proxy tokens than prose, with critical added constraints in two answers. Structured is the recommended default for clear review of task state; this small study does not establish universal superiority. Counts use `cl100k_base` and include protocol instructions and replies. Provider billing, reasoning usage and hidden system/tool overhead are unknown. These tasks measured interpretation, not engineering delivery. [Full limitations and evidence](benchmarks/README.md).

An earlier structured-protocol pilot had unequal task facts, a brevity confound, incomplete preregistration and unblinded grading. Its [records and corrections](benchmarks/pilot-v1/README.md) are retained separately.

We cannot trace this style to a specific training origin. We do not claim an emergent secret language or novelty over structured prompting. Selective fusion is a stylistic observation; the dense experiment tested a composite style and did not isolate whitespace causally. Real-task performance and cross-model sender-to-receiver transfer remain open questions.

## Public context

These primary sources discuss related practices, not validation of CPH:

- [OpenAI prompt engineering guidance](https://developers.openai.com/api/docs/guides/prompt-engineering)
- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)

All examples and benchmark tasks are synthetic. No private historical handoff corpus is included.
