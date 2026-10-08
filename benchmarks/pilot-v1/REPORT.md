# Structured-protocol synthetic pilot, version 1

Completed 27 attempts with three officially verified-free model IDs through OpenCode CLI 2.0.18; 26 answers, one timeout. The observed dense-paragraph style was not an arm in this frozen pilot. Its separately versioned follow-up has not run.

| Model | Attempts | Answers | Timeouts | Retained oracle facts in answered cells | Measured call seconds, range |
| --- | --- | --- | --- | --- | --- |
| opencode/space-bunny-free | 9 | 9 | 0 | 131/135 | 4.32–11.94 |
| opencode/big-pickle | 9 | 8 | 1 | 117/121 | 6.53–600.00 |
| opencode/longcat-2.5-preview-free | 9 | 9 | 0 | 135/135 | 7.63–17.61 |

Provider billing and full model input remain unknown. The already-installed ttok environment supplied tiktoken with named proxy encoding cl100k_base after loading public encoding data. Exact visible UTF-8 segments were counted separately: the literal CLI message, attachment text including protocol instructions, and returned answer. Counts below are the sum of segment counts; unknown system/tool/schema/attachment serialization and reasoning overhead is excluded. These are proxy estimates, not native model tokens or provider billing. Failed response/exchange counts remain unknown, not zero.

| Model / arm | Answers / attempts | Retained facts | Clarifications | Answer wall median, seconds | Body-only tokens, 3 inputs | Visible sent tokens, 3 attempts | Answer tokens | Visible exchange tokens, answered cells |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| opencode/space-bunny-free / A | 3/3 | 42/45 | 0 | 10.41 | 331 | 574 | 1804 | 2378 |
| opencode/space-bunny-free / B | 3/3 | 44/45 | 0 | 7.83 | 310 | 556 | 1353 | 1909 |
| opencode/space-bunny-free / C | 3/3 | 45/45 | 0 | 5.53 | 310 | 607 | 902 | 1509 |
| opencode/big-pickle / A | 3/3 | 43/45 | 0 | 10.09 | 331 | 574 | 784 | 1358 |
| opencode/big-pickle / B | 3/3 | 43/45 | 0 | 21.31 | 310 | 556 | 748 | 1304 |
| opencode/big-pickle / C | 2/3 | 31/31 | 0 | 6.88 | 310 | 607 | 471 | 898 |
| opencode/longcat-2.5-preview-free / A | 3/3 | 45/45 | 0 | 14.55 | 331 | 574 | 688 | 1262 |
| opencode/longcat-2.5-preview-free / B | 3/3 | 45/45 | 0 | 13.00 | 310 | 556 | 743 | 1299 |
| opencode/longcat-2.5-preview-free / C | 3/3 | 45/45 | 0 | 12.79 | 310 | 607 | 412 | 1019 |

A = ordinary prose input/reply; B = structured CPH input/ordinary reply; C = structured CPH input/reply. Big Pickle C has only two answers; its exchange total covers those two cells only, while its sent total includes all three attempts. Its task 3 C timeout lasted 600.00 seconds; the two answered C calls lasted 6.53 and 7.23 seconds. Space Bunny A median uses only two measured calls; the first wall time is unknown. All other arms have three measured answered calls. Per-cell timings and the all-attempt medians are in summary.json. Queue versus generation delay is unknown.

Visible exchange totals were lower in C than A for complete Space Bunny cells (1509 versus 2378) and complete LongCat cells (1019 versus 1262). This is a small structured-only interpretation pilot with a proxy tokenizer; it does not establish provider usage reductions, universal efficiency, engineering-delivery performance, or an advantage for the untested observed dense-paragraph style. No clarifications or correction/retry calls occurred: conditional requests restated inside interpretations were not counted as actual clarification interactions.


The retained/total scores apply only to answered cells. The timed-out Big Pickle task 3 C cell is absent from its denominator, not an accuracy zero or an inferred pass. These are non-blinded manual interpretation scores from one reviewer, not statistically reliable model rankings. Inferences and invented claims are noted separately; high retention can coexist with additions or ambiguity.

Observed defects include Space Bunny dropping/contradicting the fixture path in task 1 B, adding a shared-branch commit restriction in task 1 A, and softening 150 words to roughly 150 in task 3 A. Big Pickle softened the word requirement in task 3 A/B and omitted hypothetical-fixture status in task 1 B. LongCat retained the oracle facts in the reviewed answers but sometimes overinterpreted a passing regression as general proof.

Prompts, oracle and order are in frozen-settings.json and task-*.txt. The actual literal CLI message was: “Interpret the attached synthetic task only; do not use tools or execute actions.” It was supplied with --file pointing to the matching prompt, --standalone, explicit --model, --format json, and a fixed title to avoid a separate title-generation request. CLI defaults were used without configuration overrides; their internal sampling values are unknown. The first Space Bunny cell ran before the final three-model list was recorded; its task, arm, model and scoring were unchanged. This run was not a fully preregistered experiment. Fresh empty directory per call; timeout 600 seconds; concurrency one. The timeout reports orchestration elapsed time only; queue versus generation delay cannot be inferred.

Zero pricing checked on 2026-10-08 against https://models.dev/api.json and official https://opencode.ai/v2/docs/console/models/: opencode/space-bunny-free, opencode/big-pickle, opencode/longcat-2.5-preview-free had zero input/output pricing. Actual returned answers establish availability for those successful cells only. No paid fallback, new credentials, configuration changes or private corpus were used.

Sanitized outputs and per-cell timings, unknown usage fields, coverage and review notes are in sanitized-results.json. Raw local logs are excluded from any publication candidate because they contain runtime session identifiers. This exploratory record is retained for transparency; its confounds and separate audited amendment must accompany any interpretation.
