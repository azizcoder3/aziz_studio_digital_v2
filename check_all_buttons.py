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

print("=== DETAILED BUTTON & LINK SEARCH ACROSS PAGES/ ===\n")

for p in pages:
    file_path = os.path.join(ROOT, 'pages', p)
    content = open(file_path, encoding='utf-8').read()
    
    # Find all btn elements
    matches = re.findall(r'<(?:a|button)[^>]*class="[^"]*btn[^"]*"[^>]*>(.*?)</(?:a|button)>', content, re.DOTALL)
    print(f"[{p}] ({len(matches)} buttons/links found):")
    for m in matches:
        clean = re.sub(r'<[^>]+>', '', m).strip()
        print(f"   - \"{clean}\"")
    print()
