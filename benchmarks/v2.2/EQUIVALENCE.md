# Version 2.2 exact-clause equivalence ledger

Every scored fact has explicit wording in all arms. Dense expansions are reviewer aids, not extra receiver inputs. Source-fact meanings are unchanged from version 2.1; stop wording now explicitly says stop and request the rule in every arm. The exact prompts passed independent semantic review before execution. This published ledger retains all scored clauses.

## catalog

| Fact | N / canonical meaning | Exact dense D clause | Normally spaced D expansion | Exact structured S clause | Critical |
| --- | --- | --- | --- | --- | --- |
| catalog-F01 | Repair duplicate product-code detection in the hypothetical catalog validator. | Repair hypothetical catalog validator duplicateproductcode detection | Repair hypothetical catalog validator duplicate product-code detection | Goal: Repair duplicate product-code detection in hypothetical catalog validator. | False |
| catalog-F02 | The synthetic requirement note CAT-A in this handoff is authoritative. | Synthetic requirement note CAT-A here authoritative | Synthetic requirement note CAT-A here authoritative | Requirement source: Synthetic requirement note CAT-A here is authoritative. | True |
| catalog-F03 | The hypothetical catalog-cases.json fixture is authoritative test input. | Hypothetical catalog-cases.json authoritative testinput | Hypothetical catalog-cases.json authoritative test input | Fixture source: Hypothetical catalog-cases.json is authoritative test input. | True |
| catalog-F04 | Changes are limited to the validator and its tests. | Validator and tests only | Validator and tests only | Scope: Validator and its tests only. | True |
| catalog-F05 | Local edits are authorized. | Localedits authorized | Local edits authorized | Permission: Local edits authorized. | True |
| catalog-F06 | Publication is forbidden. | No publication | No publication | Prohibition: No publication. | True |
| catalog-F07 | Product-code comparisons must be case-sensitive. | Productcode comparisons case-sensitive | Product-code comparisons case-sensitive | Behavior: Product-code comparisons must be case-sensitive. | False |
| catalog-F08 | Null product codes must be preserved. | Preserve null productcodes | Preserve null product codes | Behavior: Preserve null product codes. | False |
| catalog-F09 | Whether whitespace is significant in product codes is unknown. | Productcode whitespace significance unknown | Product-code whitespace significance unknown | Uncertainty: Product-code whitespace significance unknown. | True |
| catalog-F10 | If the whitespace rule is missing, stop and request the rule before trimming product codes. | If whitespacerule missing, stop and request the rule before trimming productcodes | If whitespace rule missing, stop and request the rule before trimming product codes | Stop condition: If whitespace rule missing, stop and request the rule before trimming product codes. | True |
| catalog-F11 | After repair, run the duplicate-code regression test. | After repair run duplicatecode regression test | After repair run duplicate-code regression test | Required check: Run duplicate-code regression after repair. | False |
| catalog-F12 | After repair, run the validator test suite. | After repair run validator testsuite | After repair run validator test suite | Required check: Run validator test suite after repair. | False |
| catalog-F13 | The null-code test passed. | Nullcode test passed | Null-code test passed | Reported check: Null-code test passed. | True |
| catalog-F14 | The duplicate-code regression failed. | Duplicatecode regression failed | Duplicate-code regression failed | Reported check: Duplicate-code regression failed. | True |
| catalog-F15 | The full validator suite has not run. | Full validator suite notrun | Full validator suite not run | Reported check: Full validator suite not run. | True |
| catalog-F16 | The patch is incomplete. | Patch incomplete | Patch incomplete | Status: Patch incomplete. | False |
| catalog-F17 | Inspect the failing duplicate-code case next. | Inspect failing duplicatecode case next | Inspect failing duplicate-code case next | Next action: Inspect failing duplicate-code case next. | False |
| catalog-F18 | Repair the validator after inspecting the failing case. | After inspecting failing case repair validator | After inspecting failing case repair validator | Sequence: After inspecting failing case, repair validator. | False |

## pagination

| Fact | N / canonical meaning | Exact dense D clause | Normally spaced D expansion | Exact structured S clause | Critical |
| --- | --- | --- | --- | --- | --- |
| pagination-F01 | Repair printed page numbering in the hypothetical document renderer. | Repair hypothetical document renderer printed pagenumbering | Repair hypothetical document renderer printed page numbering | Goal: Repair printed page numbering in hypothetical document renderer. | False |
| pagination-F02 | The synthetic requirement note PAGE-B in this handoff is authoritative. | Synthetic requirement note PAGE-B here authoritative | Synthetic requirement note PAGE-B here authoritative | Requirement source: Synthetic requirement note PAGE-B here is authoritative. | True |
| pagination-F03 | The hypothetical page-cases.json fixture is authoritative test input. | Hypothetical page-cases.json authoritative testinput | Hypothetical page-cases.json authoritative test input | Fixture source: Hypothetical page-cases.json is authoritative test input. | True |
| pagination-F04 | Changes are limited to the renderer and its tests. | Renderer and tests only | Renderer and tests only | Scope: Renderer and its tests only. | True |
| pagination-F05 | Local edits are authorized. | Localedits authorized | Local edits authorized | Permission: Local edits authorized. | True |
| pagination-F06 | Distribution is forbidden. | No distribution | No distribution | Prohibition: No distribution. | True |
| pagination-F07 | Printed page numbers must start at 1. | Printed pagenumbers start at 1 | Printed page numbers start at 1 | Behavior: Printed page numbers must start at 1. | False |
| pagination-F08 | Heading anchors must be preserved. | Preserve headinganchors | Preserve heading anchors | Behavior: Preserve heading anchors. | False |
| pagination-F09 | Whether appendices participate in page numbering is unknown. | Appendix participation in pagenumbering unknown | Appendix participation in page numbering unknown | Uncertainty: Appendix participation in page numbering unknown. | True |
| pagination-F10 | If the appendix rule is missing, stop and request the rule before numbering appendices. | If appendixrule missing, stop and request the rule before numbering appendices | If appendix rule missing, stop and request the rule before numbering appendices | Stop condition: If appendix rule missing, stop and request the rule before numbering appendices. | True |
| pagination-F11 | After repair, run the page-number regression test. | After repair run pagenumber regression test | After repair run page-number regression test | Required check: Run page-number regression after repair. | False |
| pagination-F12 | After repair, run the renderer test suite. | After repair run renderer testsuite | After repair run renderer test suite | Required check: Run renderer test suite after repair. | False |
| pagination-F13 | The heading-anchor test passed. | Headinganchor test passed | Heading-anchor test passed | Reported check: Heading-anchor test passed. | True |
| pagination-F14 | The page-number regression failed. | Pagenumber regression failed | Page-number regression failed | Reported check: Page-number regression failed. | True |
| pagination-F15 | The full renderer suite has not run. | Full renderer suite notrun | Full renderer suite not run | Reported check: Full renderer suite not run. | True |
| pagination-F16 | The patch is incomplete. | Patch incomplete | Patch incomplete | Status: Patch incomplete. | False |
| pagination-F17 | Inspect the failing page-number case next. | Inspect failing pagenumber case next | Inspect failing page-number case next | Next action: Inspect failing page-number case next. | False |
| pagination-F18 | Repair the renderer after inspecting the failing case. | After inspecting failing case repair renderer | After inspecting failing case repair renderer | Sequence: After inspecting failing case, repair renderer. | False |

## time-range

| Fact | N / canonical meaning | Exact dense D clause | Normally spaced D expansion | Exact structured S clause | Critical |
| --- | --- | --- | --- | --- | --- |
| time-range-F01 | Repair reversed-range rejection in the hypothetical time-range parser. | Repair hypothetical timerange parser reversedrange rejection | Repair hypothetical time-range parser reversed-range rejection | Goal: Repair reversed-range rejection in hypothetical time-range parser. | False |
| time-range-F02 | The synthetic requirement note TIME-C in this handoff is authoritative. | Synthetic requirement note TIME-C here authoritative | Synthetic requirement note TIME-C here authoritative | Requirement source: Synthetic requirement note TIME-C here is authoritative. | True |
| time-range-F03 | The hypothetical range-cases.json fixture is authoritative test input. | Hypothetical range-cases.json authoritative testinput | Hypothetical range-cases.json authoritative test input | Fixture source: Hypothetical range-cases.json is authoritative test input. | True |
| time-range-F04 | Changes are limited to the parser and its tests. | Parser and tests only | Parser and tests only | Scope: Parser and its tests only. | True |
| time-range-F05 | Local edits are authorized. | Localedits authorized | Local edits authorized | Permission: Local edits authorized. | True |
| time-range-F06 | Deployment is forbidden. | No deployment | No deployment | Prohibition: No deployment. | True |
| time-range-F07 | A range whose end precedes its start must be rejected. | Reject range if end precedes start | Reject range if end precedes start | Behavior: Reject range whose end precedes start. | False |
| time-range-F08 | Supplied timezone offsets must be preserved. | Preserve supplied timezoneoffsets | Preserve supplied timezone offsets | Behavior: Preserve supplied timezone offsets. | False |
| time-range-F09 | How to resolve daylight-saving ambiguity is unknown. | Daylight-saving ambiguity resolution unknown | Daylight-saving ambiguity resolution unknown | Uncertainty: Daylight-saving ambiguity resolution unknown. | True |
| time-range-F10 | If the daylight-saving rule is missing, stop and request the rule before resolving ambiguous local times. | If daylight-saving rule missing, stop and request the rule before resolving ambiguous localtimes | If daylight-saving rule missing, stop and request the rule before resolving ambiguous local times | Stop condition: If daylight-saving rule missing, stop and request the rule before resolving ambiguous local times. | True |
| time-range-F11 | After repair, run the reversed-range regression test. | After repair run reversedrange regression test | After repair run reversed-range regression test | Required check: Run reversed-range regression after repair. | False |
| time-range-F12 | After repair, run the parser test suite. | After repair run parser testsuite | After repair run parser test suite | Required check: Run parser test suite after repair. | False |
| time-range-F13 | The offset-preservation test passed. | Offsetpreservation test passed | Offset-preservation test passed | Reported check: Offset-preservation test passed. | True |
| time-range-F14 | The reversed-range regression failed. | Reversedrange regression failed | Reversed-range regression failed | Reported check: Reversed-range regression failed. | True |
| time-range-F15 | The full parser suite has not run. | Full parser suite notrun | Full parser suite not run | Reported check: Full parser suite not run. | True |
| time-range-F16 | The patch is incomplete. | Patch incomplete | Patch incomplete | Status: Patch incomplete. | False |
| time-range-F17 | Inspect the failing reversed-range case next. | Inspect failing reversedrange case next | Inspect failing reversed-range case next | Next action: Inspect failing reversed-range case next. | False |
| time-range-F18 | Repair the parser after inspecting the failing case. | After inspecting failing case repair parser | After inspecting failing case repair parser | Sequence: After inspecting failing case, repair parser. | False |
