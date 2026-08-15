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

print("=== CHECKING EDITORIAL CONTENT UNIQUENESS ACROSS 6 SERVICE PAGES ===\n")

paragraphs = {}

for p in pages:
    file_path = os.path.join(ROOT, 'pages', p)
    content = open(file_path, encoding='utf-8').read()
    
    # Extract all <p> text content
    p_texts = re.findall(r'<p[^>]*>(.*?)</p>', content, re.DOTALL)
    cleaned = []
    for text in p_texts:
        t = re.sub(r'<[^>]+>', '', text).strip()
        if len(t) > 30: # Ignore very short labels
            cleaned.append(t)
    paragraphs[p] = cleaned

# Compare paragraphs between pairs of pages
duplicates_found = False
for i in range(len(pages)):
    for j in range(i + 1, len(pages)):
        p1, p2 = pages[i], pages[j]
        set1, set2 = set(paragraphs[p1]), set(paragraphs[p2])
        common = set1.intersection(set2)
        if common:
            duplicates_found = True
            print(f"⚠ Duplicate paragraphs between {p1} and {p2} ({len(common)} matches):")
            for dup in common:
                print(f"   - \"{dup[:100]}...\"")

if not duplicates_found:
    print("✅ PERFECT! Zero duplicate paragraphs found across all 6 service pages.")
