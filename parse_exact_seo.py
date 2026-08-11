import os
from html.parser import HTMLParser

class HeadParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.title = ""
        self.meta_desc = ""
        self.h1_count = 0
        self.in_h1 = False
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'title':
            self.in_title = True
        elif tag == 'meta' and attrs_dict.get('name', '').lower() == 'description':
            self.meta_desc = attrs_dict.get('content', '')
        elif tag == 'h1':
            self.h1_count += 1

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data

ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'
pages = [f for f in os.listdir(ROOT) if f.endswith('.html')]

print("=== EXACT SEO MEASUREMENTS (HTML PARSER STDLIB) ===\n")

for p in sorted(pages):
    fp = os.path.join(ROOT, p)
    raw = open(fp, encoding='utf-8').read()
    
    if len(raw.strip()) == 0:
        print(f"Page: {p} (Fichier 0-octet non encore développé)")
        continue
        
    parser = HeadParser()
    parser.feed(raw)
    
    title = parser.title.strip()
    meta = parser.meta_desc.strip()
    
    print(f"Page: {p}")
    print(f"  Title ({len(title)} chars, {title.count('|')} pipe) : \"{title}\"")
    print(f"  Meta Description ({len(meta)} chars) : \"{meta}\"")
    print(f"  Nombre H1 : {parser.h1_count}")
    print()
