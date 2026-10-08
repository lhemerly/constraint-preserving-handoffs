# Synthetic benchmark: method, results and reproduction

The dense composite format used 4,340 visible proxy tokens versus 6,099 for normal prose (28.8% fewer). Strict fidelity was 6/9 passes for dense, 7/9 for prose and 8/9 for structured fields. Smaller responses did not guarantee constraint-safe interpretation. Structured CPH is the recommended default; this small study does not establish universal superiority or provider billing savings.

## Version 2.2 method

Three fresh synthetic tasks × three two-way formats × three receiver models = 27 answers. N: normal prose in/out. D: one dense technical paragraph with compressed connectors and selective fusion in/out. S: structured fields in/out. All arms shared the same brevity objective and requested interpretation output. All 54 task facts (18 per task) had explicit clauses in every arm and passed independent semantic equivalence review before receiver calls. The frozen design retains its pre-execution status text as an immutable snapshot; the completed run is recorded in the responses and summary. The [frozen design](v2.2/design.json), [ledger](v2.2/EQUIVALENCE.md), [dense expansions](v2.2/DENSE-EXPANSIONS.md) and [exact prompts](v2.2/prompts/catalog-D.txt) are public.

Models: opencode/space-bunny-free, opencode/big-pickle, opencode/longcat-2.5-preview-free. OpenCode 2.0.18; explicit model IDs, fixed title, CLI defaults without overrides (internal sampling values unknown), fresh empty contexts, concurrency one, 600-second cap, frozen balanced order, one trial per cell. All 27 returned text; no errors, timeouts, correction/retry turns or actual clarification requests. Receivers interpreted hypothetical tasks; no real engineering delivery was tested.

Zero input/output prices were checked at execution on 2026-10-08 against [official OpenCode pricing](https://opencode.ai/v2/docs/console/models/) and [models.dev](https://models.dev/api.json). That does not establish future availability or billing totals.

## Separate local review

Two new local model-blind semantic reviews graded the already generated responses. This is a separate local review, not a reproduction of an earlier adjudication. Style could reveal format, so blinding was partial. Reviewer one reconciled disagreements after both reviews were locked; there was no independent third grader, a departure from the frozen review plan. No grades changed after unblinding.

Original [review one](v2.2/grades/review-one.json), [review two](v2.2/grades/review-two.json) and [locked reconciliation](v2.2/grades/adjudication.json) preserve grade payloads unchanged. Private location metadata was removed. Original reviewer totals differ: one reported 486/486 retained, 22/5/0 pass/fail/indeterminate; two reported 485/486, 21/4/2. Reconciliation preserved one ambiguous fact and two indeterminate answers. Three strict-outcome disagreements and one fact-decision disagreement are recorded.

Strict pass requires all 18 facts retained and zero critical errors. Critical invented permissions, prohibitions, attribution or exclusive conditions fail even with perfect recall. Indeterminate is neither a pass nor a confirmed failure. Format labels identify assigned arms; reviewers deferred independent format-compliance grading.

## Per-format results

| Format | Answers | Pass / fail / indeterminate | Retained facts | Critical errors | Visible exchange proxy |
| --- | --- | --- | --- | --- | --- |
| N: normal | 9 | 7 / 2 / 0 | 162/162 | 2 | 6,099 |
| D: dense | 9 | 6 / 2 / 1 | 162/162 | 2 | 4,340 |
| S: structured | 9 | 8 / 0 / 1 | 161/162 | 0 | 5,457 |

Overall: 21 passes, four failures, two indeterminate; 485/486 facts retained. Confirmed additions: four critical and 20 noncritical; three further additions were ambiguous. One failed answer also had an ambiguous addition, so three ambiguous additions do not imply three indeterminate answers. Clarification requests and interpretation-only violations were zero in the locked review.

Pass-fraction ambiguity bounds: overall 21/27 to 23/27; dense 6/9 to 7/9; structured 8/9 to 9/9. These are not confidence intervals. Every format has nine answered cells and 162 fact decisions; each model-format cell has three answers and 54 facts. No missing cells were imputed.

## Model × format

| Model | Format | Pass / fail / indeterminate | Retained facts | Critical errors | Visible exchange | Reduction vs own prose | Median seconds |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Space Bunny | N | 1 / 2 / 0 | 54/54 | 2 | 2,622 | 0.0% | 13.298 |
| Space Bunny | D | 2 / 1 / 0 | 54/54 | 1 | 1,594 | 39.2% | 6.180 |
| Space Bunny | S | 2 / 0 / 1 | 53/54 | 0 | 2,133 | 18.6% | 6.280 |
| Big Pickle | N | 3 / 0 / 0 | 54/54 | 0 | 1,839 | 0.0% | 19.658 |
| Big Pickle | D | 1 / 1 / 1 | 54/54 | 1 | 1,451 | 21.1% | 13.645 |
| Big Pickle | S | 3 / 0 / 0 | 54/54 | 0 | 1,698 | 7.7% | 22.671 |
| LongCat | N | 3 / 0 / 0 | 54/54 | 0 | 1,638 | 0.0% | 40.468 |
| LongCat | D | 3 / 0 / 0 | 54/54 | 0 | 1,295 | 20.9% | 24.926 |
| LongCat | S | 3 / 0 / 0 | 54/54 | 0 | 1,626 | 0.7% | 13.645 |

Per-model totals: Space Bunny 5/3/1, 161/162 retained, three critical errors; Big Pickle 7/1/1, 162/162, one critical error; LongCat 9/0/0, 162/162, no confirmed critical errors.

## Failure and ambiguity evidence

Confirmed failures were added restrictions: Space Bunny N introduced a local-only repair limitation and broadened a deployment ban to every release/rollout; Space Bunny D forbade treating null codes as duplicates; Big Pickle D changed rejection to “if and only if.” The source tasks did not establish those restrictions.

Space Bunny S catalog remained indeterminate because a correctly stated conditional was later described as an active block, allowing two readings of whether the whitespace rule was actually missing. Big Pickle D catalog remained indeterminate because calling required test completion a stop condition could add a halt obligation. An additional source-attribution reading in a failed prose answer remains ambiguous. All evidence and reasons remain in [locked grades](v2.2/grades/adjudication.json).

## Token and latency limitations

Proxy encoding cl100k_base, tiktoken 0.14.0. Full literal prompts include common protocol, identical brevity objectives, format instructions and delimiters; each exact emitted answer segment is counted separately. Provider input/output/cache/reasoning usage, native model tokenization, hidden system/tool/schema overhead and billing remain unknown. CLI exposed step_start and text events, not usage totals.

| Format | Body-only tokens | Full visible prompt | Answers | Visible exchange | Median wall seconds | Total wall seconds |
| --- | --- | --- | --- | --- | --- | --- |
| N | 1,458 | 2,736 | 3,363 | 6,099 | 22.265 | 218.859 |
| D | 1,167 | 2,733 | 1,607 | 4,340 | 13.645 | 162.074 |
| S | 1,617 | 2,958 | 2,499 | 5,457 | 13.147 | 120.371 |

Dense instructions cost more than prose instructions, so full input totals were almost equal. Most observed exchange reduction came from replies. Totals include failed and indeterminate answers; production retry costs are unmeasured. Wall time totaled 501.304 seconds; queue versus generation delay is unknown. Detailed all-attempt means, ranges and totals are in [summary.json](v2.2/summary.json).

This is a composite style treatment, not a causal whitespace experiment. Three task families, three models, one trial per cell, handcrafted senders, interpretation-only outputs and partial blinding limit inference. No statistical significance, universal superiority, billing savings, training origin or secret language is claimed.

## Reproduce existing counts locally

No model calls are required:

```bash
python3 benchmarks/reproduce_grades.py
python3 -m pip install -r benchmarks/requirements.txt
python3 benchmarks/reproduce_tokens.py
```

The optional tokenizer dependency is needed only for counts; an existing matching environment works. Encoding data may be fetched by tiktoken on first use. These scripts only read published files and verify existing data; they cannot call models. They check expected totals against exact public prompts, emitted text, locked grades and mapping.

[v2.2 responses](v2.2/responses.jsonl) retain exact synthetic answer segments and token/timing evidence. [Sanitized CLI events](v2.2/cli-events.sanitized.jsonl) preserve text and event timing while omitting session/message/part identifiers. [Provenance](v2.2/PROVENANCE.json) and the integrity manifest document the transformation. Benchmark-only anonymous IDs are not private task identifiers.

To collect a new independent trial, preserve these records, version the new trial, verify current pricing/access and use the frozen order and literal prompts. The recorded invocation was `opencode run --standalone --model <explicit-model-id> --format json --title 'Synthetic CPH v2 interpretation' <exact-literal-prompt>` in a fresh empty context with a 600-second process timeout. Pass the prompt as a literal argument, not shell-interpolated code. CLI defaults and provider behavior can change, so a new run cannot guarantee identical responses. No rerun was performed for this publication.

## Earlier pilot

[Version 1 records and confounds](pilot-v1/README.md) are exploratory and separate. It tested structured CPH, not the observed dense style. Do not pool it with version 2.2 or treat its unequal inputs as a controlled fidelity comparison.
