# Independent audit amendment

This amendment preserves the original exploratory records unchanged and supplies separate audited results. The independent second review was **not blinded**. Token arithmetic and reported medians were reproduced; this is not an independently blinded benchmark.

## Confounds

Task 3 explicitly supplied “checks not run” only in the structured input while scoring that fact in all arms. The 45-fact comparison is therefore not fully input-equivalent. Arm C alone requested concise wording, confounding structure with brevity. Neither the observed dense-paragraph style nor causal efficiency was tested. The exploratory visible-token differences must not be presented as causal effects.

## Correction and critical errors

Space Bunny A changes from 42/45 to **40/45**: task 1 did not explicitly retain fixture authority and gave conflicting first-step order. Other retention scores stand. Space Bunny and LongCat C each retained 45/45; Big Pickle C retained 31/31 in its two answered cells only.

Retention is separate from critical invented constraints. Space Bunny task 1 A added a shared-branch commit prohibition; task 2 A introduced an unsupported exclusive “if and only if” stop condition. Both are critical errors even where many source facts were retained. Do not use retention totals as a permission-compliance or task-success score.

## Metadata and latency

In the original results, `body_characters` actually counted the whole attachment, including protocol text. The audited copy renames it `attachment_characters`; original data remains intact. `body_only` proxy token counts cover task text only.

Big Pickle C: three attempts, two answers and one timeout. Total wall time **613.764 seconds**, all-attempt mean **204.588 seconds**, answered-only median **6.880 seconds**, timeout **600.003 seconds**. The fast answered-only median does not represent the timeout cost. Full per-arm totals and means are in `audited-summary.json`; Space Bunny A still has one unmeasured wall time.

These corrections informed the later v2.2 equivalence ledger, equal brevity objectives and complete-attempt latency reporting. The original pilot records remain preserved separately.
