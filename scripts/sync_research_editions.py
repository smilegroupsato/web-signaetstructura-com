#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'publishing/publications.json'
OVERLAY = ROOT / 'publishing/research-editions.json'


def main():
    base_doc = json.loads(BASE.read_text(encoding='utf-8'))
    if not OVERLAY.exists():
        print('No research edition overlay; nothing to sync')
        return
    overlay_doc = json.loads(OVERLAY.read_text(encoding='utf-8'))
    overlay = overlay_doc.get('publications', [])
    by_key = {(x['publication_id'], x['language']): x for x in overlay}
    merged = []
    seen = set()
    for item in base_doc.get('publications', []):
        key = (item['publication_id'], item['language'])
        if key in by_key:
            merged.append(by_key[key])
            seen.add(key)
        else:
            merged.append(item)
    for item in overlay:
        key = (item['publication_id'], item['language'])
        if key not in seen and not any((x['publication_id'], x['language']) == key for x in merged):
            merged.append(item)
    base_doc['publications'] = merged
    if overlay_doc.get('updated_at_jst'):
        base_doc['updated_at_jst'] = overlay_doc['updated_at_jst']
    BASE.write_text(json.dumps(base_doc, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Synced {len(overlay)} research edition override(s); registry now has {len(merged)} edition(s)')


if __name__ == '__main__':
    main()
