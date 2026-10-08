# Evaluation plan

The [completed synthetic study](benchmarks/README.md) is a small interpretation experiment. Real-task delivery, retries in production and model-generated sender-to-receiver transfer remain pending.

## Future design

Create public-safe synthetic tasks with a clause-by-clause equivalence ledger and objective acceptance criteria. Compare ordinary prose, dense paragraph shorthand and structured fields. Preserve complete facts, permissions, stop conditions, provenance, uncertainty and requested outputs across every arm; use identical brevity objectives. Freeze tasks, atomic oracles, contradiction/addition rules, model list, settings, balanced order, tokenizer encodings and timeout/missing-cell rules before calls.

Blind two independent semantic graders to model identity, order, usage and timings; style may reveal format. Use an independent third adjudicator for disagreements, or explicitly disclose any departure. Preserve original grades and indeterminate outcomes. Score strict fidelity (all source facts retained, zero critical errors) alongside recall, critical additions and format compliance.

For real task delivery, add independently checkable artifacts and tests. An unauthorized action is failure even if the artifact is correct. Restating supplied facts is interpretation fidelity, not engineering success. Include missing references, conditional permissions, failed checks, ambiguous boundaries and multi-hop transfers.

## Measures

| Measure | Record |
| --- | --- |
| Tokens | Body-only, complete protocol/schema/instruction overhead, both messages, resolved artifacts, tools, reasoning if reported, corrections and retries. Name encoding for estimates; provider usage controls billing. Missing usage is unknown. |
| Constraint retention | Per-fact retained/omitted/contradicted/ambiguous decisions; invented constraints separately. Audit permissions, uncertainty, stop conditions, outcomes and provenance. |
| Task success | Acceptance tests, authority compliance and delivery status, independently of response length. |
| Retries | Actual clarification requests, recovery/repair attempts and total calls through success or exhaustion. |
| Cross-model transfer | Explicit sender/receiver model pairs plus multi-hop cases; handcrafted inputs across receiver models do not establish model-generated transfer. |
| Availability/latency | Coverage, errors, timeouts, total/mean/median all-attempt latency and answered-only latency; queue/generation split only if evidenced. |

Repeat independent trials, choose sample size before results, report uncertainty and failures by task family/model pair, and avoid pooling away missing cells. Test space removal separately only if seeking a causal whitespace claim; the current dense arm is composite. Publish synthetic prompts, exact counts, grading evidence and versions after privacy review. Claim advantages only for measured conditions; do not infer training origin or universal superiority.
