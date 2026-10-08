"""Recount exact published text with a proxy tokenizer; no model calls."""
import json
from pathlib import Path
import tiktoken

ROOT = Path(__file__).resolve().parent / 'v2.2'
def read(name):
    return json.loads((ROOT / name).read_text())

def main():
    enc = tiktoken.get_encoding('cl100k_base')
    count = lambda s: len(enc.encode(s))
    tasks = {t['id']: t for t in read('design.json')['tasks']}
    rows = [json.loads(line) for line in (ROOT / 'responses.jsonl').read_text().splitlines()]
    for r in rows:
        t, arm = tasks[r['task']], r['arm']
        published = (ROOT / 'prompts' / f"{r['task']}-{arm}.txt").read_text()
        assert published == t['prompts'][arm]
        measured = dict(body_only=count(t['bodies'][arm]), complete_literal_prompt=count(t['prompts'][arm]), answer=sum(count(s) for s in r['answer_segments']))
        measured['visible_exchange'] = measured['complete_literal_prompt'] + measured['answer']
        for k,v in measured.items():
            assert r['tokens'][k] == v, (r['answer_id'], k, v, r['tokens'][k])
    summary = read('summary.json')
    groups = [(summary['summary'], rows)]
    for field,key in [('by_format','arm'), ('by_model','model')]:
        groups.extend((s,[r for r in rows if r[key] == s['group']]) for s in summary[field])
    groups.extend((s,[r for r in rows if r['model']+' / '+r['arm'] == s['group']]) for s in summary['by_model_format'])
    fields = dict(body_tokens='body_only', complete_visible_prompt_tokens='complete_literal_prompt', answer_tokens='answer', visible_exchange_tokens='visible_exchange')
    for expected, selected in groups:
        totals = {out:sum(r['tokens'][key] for r in selected) for out,key in fields.items()}
        for k,v in totals.items():
            assert v == expected[k], (expected['group'], k)
        print(expected['group'], totals)
    print('All exact-text and aggregate counts match. Proxy only: provider/schema/system/reasoning usage unknown.')

if __name__ == '__main__':
    main()
