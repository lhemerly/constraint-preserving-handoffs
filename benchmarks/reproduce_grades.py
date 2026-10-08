"""Verify aggregates from locked grades; never regrade or call a model."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent / 'v2.2'
def read(name):
    return json.loads((ROOT / name).read_text())

def main():
    mapping = {x['answer_id']: x for x in read('mapping.json')}
    grades = read('grades/adjudication.json')['grades']
    responses = [json.loads(line) for line in (ROOT / 'responses.jsonl').read_text().splitlines()]
    assert len(mapping) == len(grades) == len(responses) == 27
    assert set(mapping) == {x['answer_id'] for x in grades} == {x['answer_id'] for x in responses}
    oracle = read('oracle.json')
    for g in grades:
        assert g['task_id'] == mapping[g['answer_id']]['task']
        assert len(g['facts']) == 18
        assert {f['fact_id'] for f in g['facts']} == {f['id'] for f in oracle[g['task_id']]}
    summary = read('summary.json')
    groups = [(summary['summary'], grades)]
    for field, key in [('by_format', 'arm'), ('by_model', 'model')]:
        groups.extend((s, [g for g in grades if mapping[g['answer_id']][key] == s['group']]) for s in summary[field])
    groups.extend((s, [g for g in grades if mapping[g['answer_id']]['model'] + ' / ' + mapping[g['answer_id']]['arm'] == s['group']]) for s in summary['by_model_format'])
    for expected, rows in groups:
        strict = Counter('indeterminate' if g['strict_fidelity'] == 'ambiguous' else g['strict_fidelity'] for g in rows)
        facts = Counter(f['decision'] for g in rows for f in g['facts'])
        additions = Counter(a['severity'] for g in rows for a in g['unsupported_additions'])
        actual = dict(answers=len(rows), strict={k: strict[k] for k in expected['strict']}, facts={k: facts[k] for k in expected['facts']}, fact_denominator=sum(len(g['facts']) for g in rows), critical_errors=sum(g['critical_error_count'] for g in rows), unsupported_additions={k: additions[k] for k in expected['unsupported_additions']}, actual_clarification_requests=sum(g['actual_clarification_request'] for g in rows), interpretation_only_violations=sum(g['interpretation_only_violation'] for g in rows))
        for k,v in actual.items():
            assert v == expected[k], (expected['group'], k, v, expected[k])
        print(expected['group'], actual['strict'], f"facts {facts['retained']}/{actual['fact_denominator']}", 'critical', actual['critical_errors'])
    print('All 16 group aggregates match locked grades; no grades changed.')

if __name__ == '__main__':
    main()
