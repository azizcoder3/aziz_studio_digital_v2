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

print("=== EXACT CHAR COUNT MEASUREMENT SCRIPT ===\n")

for p in pages:
    filepath = os.path.join(ROOT, p)
    content = open(filepath, encoding='utf-8').read()
    
    t_match = re.search(r'<title>(.*?)</title>', content)
    title = t_match.group(1) if t_match else ""
    
    m_match = re.search(r'<meta name="description" content="(.*?)"', content)
    meta = m_match.group(1) if m_match else ""
    
    print(f"Page: {p}")
    print(f"  Title ({len(title)} chars, {title.count('|')} pipe): \"{title}\"")
    print(f"  Meta Description ({len(meta)} chars): \"{meta}\"")
    print()
