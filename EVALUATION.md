# Evaluation plan

Status: pending. No benchmark results are claimed.

## Three-arm whole-exchange pilot

Compare A: normal prose input and reply; B: CPH handoff with ordinary reply; C: CPH handoff and CPH reply. Keep complete task facts and constraints equivalent. Count protocol instructions, both messages, corrections, and any provider-reported reasoning usage. Missing usage remains unknown; provider usage takes precedence for billing. Report body-only and complete prompt counts separately, naming the exact tokenizer encoding; local counts cannot establish hidden tool or system overhead.

The [pilot design](pilot-design.json) freezes three synthetic example inputs, reply instructions, balanced order, and source-fact oracles. This is an interpretation and constraint-retention test, not real engineering delivery. Before any calls, enumerate atomic oracle facts and freeze the provider/model/settings and scoring inventory. Use fresh bounded workspaces, concurrency one, at most nine initial calls, and a 600-second ceiling per call. Receivers must only interpret handoffs and must not execute described actions. Instruct receiver agents in arm C to use the same CPH language in their replies.

Execution limitation: the installed OpenCode CLI, version 2.0.18, returned a successful but empty result for `opencode models --standalone`. No selectable model could be verified through normal CLI discovery, so no model calls were made and model/settings selection remains pending. The [official OpenCode model pricing](https://opencode.ai/v2/docs/console/models/) listed Big Pickle and Space Bunny Free as free for input, output, and cached reads when checked on 2026-10-08; pricing alone does not establish local availability. Do not guess a model identifier, change configuration or credentials, or use a paid fallback. Once availability is established, use one verified-free model; if unavailable, try at most one distinct verified-free alternative and label failures. Do not combine different models into a claimed paired result.

Any eventual small pilot is preliminary and independent of private historical conversations. It cannot establish universal efficiency or directly describe past exchanges.

## Design

Create synthetic tasks with explicit ground-truth constraint inventories and checkable outcomes. Cover code repair, research, document editing, conditional permissions, missing references, conflicting authority, failed tests, and multi-hop transfers. Use public primary-source material where external evidence is needed. Do not use private conversations or sensitive task data.

Compare full narrative handoffs, ordinary structured handoffs, and CPH. Give every condition equivalent task facts and accessible artifacts. Include short tasks where CPH's labels may cost more than they save. Separate handoff generation from receiver execution, and score information lost at each stage.

Pre-register prompts, task selection, success criteria, retry limits, model versions/settings, sample size rationale, and scoring rules. Randomize condition order; use repeated independent trials. Blind evaluators to the condition where practical. Report uncertainty and individual failures, not just averages.

## Measures

| Measure | What to record |
| --- | --- |
| Tokens | Model-specific tokenizer counts for the complete input: labels, delimiters, schemas, instructions, references, resolved artifact content, and repeated context. Also count sender output, receiver output, tool exchanges, and retries. Report handoff-only and end-to-end totals separately. |
| Constraint retention | Recall against the original inventory; also invented constraints, altered conditions, and ambiguity. Score permissions, uncertainty, stop conditions, test outcomes, and provenance separately. |
| Task success | Objective acceptance checks plus authorization compliance. A correct artifact produced through an unauthorized action is a failure. |
| Retries | Clarification requests, missing-reference recovery, repair attempts, and total calls to success or exhaustion. |
| Cross-model transfer | Same-model and different sender/receiver model pairs, with each model's tokenizer and settings recorded; include multi-hop transfer. |

## Analysis and reporting

Compare paired tasks across conditions. Report distributions and confidence intervals for tokens, retention, success, and retries; explain the uncertainty method and handling of exhausted trials. Separate task families and model pairs to avoid hiding regressions in aggregate numbers. Track latency and monetary cost if available, without using paid services solely for this repository.

Test field merging and artifact references as separate ablations. If space removal is explored, treat it as a separate experimental condition; measure ambiguity and tokenizer-dependent behavior rather than assuming fewer characters means fewer tokens.

Publish synthetic prompts, scoring rubrics, versions, raw non-sensitive measurements, and reproducible procedures only after privacy review. Label any exploratory analysis. Claim an advantage only for the measured conditions, and report cases where ordinary prose or structured prompting performs better. Do not infer a training origin or a secret language from results.
