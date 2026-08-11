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

print("=== CHECKING ALL LINKS & HREF DESTINATIONS ACROSS 6 PAGES ===\n")

broken_count = 0
for p in pages:
    file_path = os.path.join(ROOT, p)
    content = open(file_path, encoding='utf-8').read()
    
    hrefs = re.findall(r'href="([^"#]+)(?:#[^"]*)?"', content)
    print(f"[{p}] {len(hrefs)} external/internal page links found.")
    for href in set(hrefs):
        if href.startswith('http') or href.startswith('https') or href.startswith('mailto:') or href.startswith('tel:'):
            continue
        
        # Clean query string if present
        clean_href = href.split('?')[0]
        target_path = os.path.join(ROOT, clean_href)
        if not os.path.exists(target_path):
            print(f"  ❌ BROKEN LINK: href=\"{href}\" -> target file {clean_href} does NOT exist!")
            broken_count += 1

if broken_count == 0:
    print("\n✅ PERFECT! Zero broken links found across all 6 service pages.")
