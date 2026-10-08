# Earlier exploratory structured-protocol pilot

This pilot compared A: prose/prose, B: structured/prose and C: structured/structured across three synthetic tasks and three models. There were 27 attempts, 26 answers and one Big Pickle task 3 C timeout. It did not test the observed dense-paragraph style.

## Confounds

- Task 3 stated “checks not run” explicitly only in structured input, yet that fact was scored in every arm. No-draft status is not an explicit not-run statement. Inputs were not fully equivalent.
- Arm C alone requested concise wording, confounding structure with brevity.
- The final three-model list was recorded after the first call; preregistration was incomplete.
- Original manual grading and its independent second audit were unblinded. Keep original grades and audited corrections separate.

The independent audit corrected Space Bunny A from 42/45 to 40/45 for fixture authority and conflicting next-action order. Other retention scores stood. Critical invented restrictions and exclusive “if and only if” stop conditions were separate errors, not merely lost retention points.

Big Pickle C's three attempts took 613.764 seconds total, mean 204.588; answered-only median was 6.880, while the timeout took 600.003. Never hide its cost behind answered-only latency or omit its unavailable cell.

The original `body_characters` metadata counted the entire attachment; the audited copy names it `attachment_characters`. Body-only token estimates count task text, not all protocol. Original records are preserved, not silently regraded.

[Original exploratory report](REPORT.md), [original outputs](sanitized-results.json), [audited amendment](audit-amendment/README.md) and [audited outputs](audit-amendment/audited-results.json) remain available. These confounds prevent causal efficiency or controlled accuracy claims. The current [version 2.2 benchmark](../README.md) is separate.
