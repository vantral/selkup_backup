from pathlib import Path
import json

for file in Path('./hillmari_multimedia').iterdir():
    if not file.name.endswith('.json'):
        continue
    doc = json.load(file.open(encoding='utf-8'))
    for sent in doc['sentences']:
        for word in sent['words']:
            if 'ana' in word:
                for ana in word['ana']:
                    ana.update({'gloss_index': ana.get('gloss_index_ru', '')})
    json.dump(doc, file.open('w', encoding='utf-8'), ensure_ascii=False, indent=2)
