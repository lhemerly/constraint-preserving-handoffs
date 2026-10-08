# Constraint-Preserving Handoffs (CPH)

CPH is an experimental way to hand a task from one agent to another: state the action, point to authoritative inputs, preserve consequential constraints, name required checks, and report status plus the next action.

Use short, direct wording and shared artifact references to avoid repeating history. Keep normal spacing and explicit field boundaries. Brevity is useful only when the receiving agent can still act correctly.

## Start here

- Read the [short specification](SPEC.md).
- Copy the [agent instruction template](AGENT-INSTRUCTIONS.md) into the appropriate agent configuration.
- Compare the [synthetic examples](EXAMPLES.md).
- Use the [evaluation plan](EVALUATION.md) before making efficiency claims.

```text
Goal/action: Fix the documented CSV export defect.
Inputs/provenance: Synthetic issue in EXAMPLES.md, example 1; referenced fixtures are hypothetical.
Scope/constraints: Exporter only. Local edits authorized; no push or deployment. Preserve column order.
Checks: Add a regression test; run exporter tests. Report actual outcomes.
Status/next: No work started. Inspect the exporter; stop if the fixture is unavailable.
```

Adapt fields to the task. Merge fields when that improves clarity; omit only irrelevant boilerplate. Never omit permissions, uncertainty, stop conditions, test outcomes, or source provenance to save tokens. References must be accessible and specific enough to resolve; they are not substitutes for constraints the receiver needs immediately.

CPH applies to agent handoffs. It does not require terse or opaque replies to users. User-facing explanations should remain clear and appropriately detailed.

## Evidence and limits

Evaluation is pending. We have not measured token or performance superiority. Selective removal of spaces was an observed style, not a proven optimization, and is not part of this specification. We cannot trace the technique to a specific training origin. We do not claim an emergent secret language or novelty over structured prompting.

This repository contains original documentation and synthetic examples only. It contains no private conversation corpus or benchmark results. The name describes the intended behavior, not a demonstrated guarantee.

## Public context

These primary sources describe related practices; they do not validate CPH:

- [OpenAI prompt engineering guidance](https://platform.openai.com/docs/guides/prompt-engineering) discusses explicit instructions and context.
- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) discusses agent workflows and orchestration.

