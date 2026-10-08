# CPH specification, version 0.2

CPH names the intent of compact, constraint-preserving agent handoffs. Structured CPH is the recommended default and a designed variant; dense paragraph shorthand reflects the originally observed form. Neither is an authorization protocol or guarantee of compliance.

## Information contract

| Information | Preserve when relevant |
| --- | --- |
| Goal/action | Concrete result and requested action. |
| Inputs/provenance | Authoritative sources and accessible, specific artifact references; facts versus assumptions and untrusted material. |
| Scope/constraints | Boundaries, permissions, prohibitions, uncertainty, dependencies and exact stop/clarification conditions. |
| Checks | Acceptance criteria, required validation, actual or supplied outcomes, failures and checks not run. |
| Status/next | Completed work, blockers, remaining work and the next executable action in the required order. |

Labels are adaptable. Remove irrelevant boilerplate, not consequential information. References avoid repeated history but do not replace critical constraints needed immediately. Say unknown when a relevant value is unknown.

## Sender

1. Extract every fact or constraint whose loss or alteration could change action, result, authority or interpretation.
2. Preserve negation, quantities, conditions and order. Do not compress a conditional permission into an unconditional command, add a prohibition or introduce “if and only if.”
3. Use structured fields with normal spacing by default. Dense shorthand is optional; keep explicit clause boundaries and readable critical instructions.
4. Cite provenance accurately; do not invent accessible files, versions, results or authorization. Distinguish supplied test claims from tests you ran.
5. Never omit permissions, uncertainty, stop conditions, test outcomes or provenance to save tokens.
6. Compare the final handoff with the source for omissions, additions and ambiguity. Expand wording when needed.

## Receiver

Resolve required references and distinguish source data from instructions. Follow applicable instruction precedence. Check permission before acting. Stop and request the missing information if a required artifact is unavailable, authority conflicts or a stated stop condition applies. Do not guess. Report actual results and failures in the next handoff.

## Experimental limits

Inaccessible references, stale artifacts, invented restrictions, hidden failed checks and altered conditions can make a short handoff unreliable. Benchmark retention is not sufficient by itself: an answer can retain every source fact and still add a critical restriction. [The benchmark](benchmarks/README.md) measures synthetic interpretation, not real task delivery. Training origin, universal efficiency and novelty over structured prompting are unestablished.
