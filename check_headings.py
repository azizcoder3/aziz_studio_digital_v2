import os, re

ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'
pages = ['index.html', 'services.html', 'creation-site-web.html', 'wordpress.html', 'seo.html', 'refonte-site.html', 'maintenance.html', 'audit-conseil.html', 'mentions-legales.html', 'politique-confidentialite.html', 'conditions-utilisation.html']

for page in pages:
    filepath = os.path.join(ROOT, page)
    content = open(filepath, encoding='utf-8').read()
    
    headings = re.findall(r'<(h[1-6])[\s>](.*?)</\1>', content, re.IGNORECASE | re.DOTALL)
    print(f"=== {page} ===")
    prev = 0
    h1_count = 0
    for tag, text in headings:
        level = int(tag[1])
        if level == 1:
            h1_count += 1
        clean_text = re.sub(r'<[^>]+>', '', text).strip()
        clean_text = ' '.join(clean_text.split())[:40]
        jump = ""
        if prev > 0 and level > prev + 1:
            jump = f"  <-- JUMP DETECTED from H{prev} to H{level}!"
        print(f"  <{tag}> {clean_text}{jump}")
        prev = level
    print(f"Total H1: {h1_count}\n")
