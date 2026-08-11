import json, sys
sys.stdout.reconfigure(encoding='utf-8')

log_path = r'C:\Users\Aziz\.gemini\antigravity-ide\brain\4e2a2b99-c14c-4766-88c9-540feca256d6\.system_generated\logs\transcript.jsonl'
with open(log_path, encoding='utf-8') as f:
    lines = f.readlines()

for idx in [321, 322, 323, 324, 325]:
    if idx < len(lines):
        step = json.loads(lines[idx])
        stype = step.get('type', '')
        source = step.get('source', '')
        content = str(step.get('content', ''))[:800]
        print('=== Step', idx, 'type=', stype, 'source=', source, '===')
        print(content)
        print()
