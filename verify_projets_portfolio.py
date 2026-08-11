import os
import re
import sys
from html.parser import HTMLParser

# Set stdout encoding to utf-8 if possible
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'

PROJECT_PAGES = [
    "projet-boulevard-hotel.html",
    "projet-atre-steakhouse.html",
    "projet-cabinet-maxwell.html",
    "projet-dental-glow.html",
    "projet-molato-commerce.html",
    "projet-agence-voyage.html"
]

class HTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1_count = 0
        self.h1_texts = []
        self.in_h1 = False
        self.title = None
        self.in_title = False
        self.meta_desc = None
        self.canonical = None
        self.og_title = None
        self.og_desc = None
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'h1':
            self.h1_count += 1
            self.in_h1 = True
        elif tag == 'title':
            self.in_title = True
        elif tag == 'meta':
            if attrs_dict.get('name') == 'description':
                self.meta_desc = attrs_dict.get('content')
            elif attrs_dict.get('property') == 'og:title':
                self.og_title = attrs_dict.get('content')
            elif attrs_dict.get('property') == 'og:description':
                self.og_desc = attrs_dict.get('content')
        elif tag == 'link':
            if attrs_dict.get('rel') == 'canonical':
                self.canonical = attrs_dict.get('href')
        elif tag == 'a':
            href = attrs_dict.get('href')
            if href:
                self.links.append(href)

    def handle_endtag(self, tag):
        if tag == 'h1':
            self.in_h1 = False
        elif tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_h1:
            self.h1_texts.append(data.strip())
        elif self.in_title:
            self.title = data.strip()

def verify_project_pages():
    all_ok = True
    print("==================================================")
    print("VERIFICATION DES PAGES PROJET PORTFOLIO")
    print("==================================================")

    for page_filename in PROJECT_PAGES:
        filepath = os.path.join(ROOT, page_filename)
        print(f"\n[TEST] Verification de {page_filename}...")
        
        if not os.path.exists(filepath):
            print(f"  [FAIL] ERREUR: Le fichier {page_filename} n'existe pas !")
            all_ok = False
            continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        parser = HTMLValidator()
        parser.feed(content)
        
        # 1. H1 Unicity Check
        if parser.h1_count == 1:
            print(f"  [OK] Unique <h1> trouve: '{''.join(parser.h1_texts)}'")
        else:
            print(f"  [FAIL] ERREUR: {parser.h1_count} balise(s) <h1> trouvee(s) !")
            all_ok = False

        # 2. Metadata Check
        if parser.title:
            print(f"  [OK] Balise <title> presente: '{parser.title}'")
        else:
            print("  [FAIL] ERREUR: Balise <title> manquante !")
            all_ok = False

        if parser.meta_desc:
            print(f"  [OK] Meta description presente ({len(parser.meta_desc)} car.)")
        else:
            print("  [FAIL] ERREUR: Meta description manquante !")
            all_ok = False

        if parser.canonical:
            print(f"  [OK] URL canonique presente: '{parser.canonical}'")
        else:
            print("  [FAIL] ERREUR: URL canonique manquante !")
            all_ok = False

        # 3. Check for tree structures / file paths in content text (Exclusion rule)
        tree_patterns = [r'\.opencode', r'design-system/MASTER\.md', r'assets/css/style\.css']
        found_tree_leak = False
        for pat in tree_patterns:
            if re.search(pat, content):
                found_tree_leak = True
                print(f"  [FAIL] ERREUR: Fuite d'arborescence interne detectee ({pat}) !")
                all_ok = False
        if not found_tree_leak:
            print("  [OK] Aucune arborescence interne/technique fuitee dans le contenu.")

        # 4. Check Link Integrity for internal HTML links
        broken_links = []
        for href in parser.links:
            if href.startswith(('http://', 'https://', 'mailto:', 'tel:', '#', 'javascript:')):
                continue
            clean_href = href.split('?')[0].split('#')[0]
            if clean_href:
                target_path = os.path.join(ROOT, clean_href)
                if not os.path.exists(target_path):
                    broken_links.append(href)
        
        if not broken_links:
            print("  [OK] Tous les liens internes pointent vers des fichiers existants.")
        else:
            print(f"  [FAIL] ERREUR: Liens internes casses trouves: {broken_links}")
            all_ok = False

    print("\n==================================================")
    if all_ok:
        print("TOUTES LES VERIFICATIONS SONT REUSSIES AVEC SUCCES !")
    else:
        print("CERTAINES VERIFICATIONS ONT ECHOUE.")
    print("==================================================")
    return all_ok

if __name__ == "__main__":
    verify_project_pages()
