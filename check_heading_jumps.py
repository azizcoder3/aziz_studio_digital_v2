import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'

pages = [
    'creation-site-web.html',
    'wordpress.html',
    'seo.html',
    'refonte-site.html',
    'maintenance.html',
    'audit-conseil.html'
]

print("=== CHECKING HEADING HIERARCHY JUMPS ACROSS ALL 6 PAGES ===\n")

for p in pages:
    file_path = os.path.join(ROOT, p)
    content = open(file_path, encoding='utf-8').read()
    
    headings = re.findall(r'<(h[1-6])[^>]*>', content)
    levels = [int(h[1]) for h in headings]
    
    jumps = []
    for i in range(len(levels) - 1):
        if levels[i+1] > levels[i] + 1:
            jumps.append((levels[i], levels[i+1]))
            
    print(f"[{p}] Headings sequence: {levels[:15]}...")
    if jumps:
        print(f"  ⚠️ Heading jumps found: {jumps}")
    else:
        print("  ✅ Perfect heading hierarchy (no skipped levels).")
    print()
