"""
verify_sprint40.py — Script de vérification automatisée Sprint 40
Aziz Studio Digital V2
"""

import os
import sys
import re
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = r"c:\Users\Aziz\Desktop\aziz_studio_digital_v2"

# 11 nouvelles pages à vérifier
NEW_PAGES = [
    "hotel.html",
    "restaurant.html",
    "immobilier.html",
    "clinique.html",
    "cabinet-medical.html",
    "cabinet-dentaire.html",
    "pharmacie.html",
    "salon-beaute.html",
    "voyage.html",
    "commande.html",
    "merci.html"
]

SECTOR_SLUGS = [
    "hotel", "restaurant", "immobilier", "clinique",
    "cabinet-medical", "cabinet-dentaire", "pharmacie",
    "salon-beaute", "voyage"
]

class HTMLInspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.description = ""
        self._in_title = False
        self.forms = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            if attr_dict.get("name", "").lower() == "description":
                self.description = attr_dict.get("content", "")
        elif tag == "form":
            self.forms.append(attr_dict)
        elif tag == "a":
            href = attr_dict.get("href", "")
            if href:
                self.links.append(href)

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data

def verify_sprint40():
    print("=== DÉBUT DES VÉRIFICATIONS SPRINT 40 ===")
    errors = []
    warnings = []

    # 1. Vérification de l'existence des 11 pages compilées
    print("\n--- 1. Contrôle d'existence des 11 nouvelles pages ---")
    for page in NEW_PAGES:
        path = os.path.join(ROOT_DIR, page)
        if not os.path.exists(path):
            errors.append(f"Fichier manquant : {page}")
        else:
            size_kb = os.path.getsize(path) / 1024
            print(f"  [✓] {page} présent ({size_kb:.1f} KB)")

    # 2. Vérification des 9 images sectorielles
    print("\n--- 2. Contrôle des 9 images sectorielles ---")
    sect_dir = os.path.join(ROOT_DIR, "assets", "images", "secteurs")
    for slug in SECTOR_SLUGS:
        img_name = f"{slug}.webp"
        img_path = os.path.join(sect_dir, img_name)
        if not os.path.exists(img_path):
            errors.append(f"Image sectorielle manquante : assets/images/secteurs/{img_name}")
        else:
            size_kb = os.path.getsize(img_path) / 1024
            print(f"  [✓] {img_name} présent ({size_kb:.1f} KB)")

    # 3. Vérification SEO (Title <= 60 & Meta Description <= 160)
    print("\n--- 3. Contrôle des contraintes SEO (Title <= 60, Meta Desc <= 160) ---")
    for page in NEW_PAGES:
        path = os.path.join(ROOT_DIR, page)
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        inspector = HTMLInspector()
        inspector.feed(content)
        
        t_len = len(inspector.title)
        d_len = len(inspector.description)

        if t_len == 0:
            errors.append(f"{page} : Balise <title> manquante")
        elif t_len > 60:
            errors.append(f"{page} : <title> trop long ({t_len} car. > 60) -> '{inspector.title}'")
        else:
            print(f"  [✓] {page} Title ({t_len} car.) : '{inspector.title}'")

        if d_len == 0:
            errors.append(f"{page} : <meta description> manquante")
        elif d_len > 160:
            errors.append(f"{page} : <meta description> trop longue ({d_len} car. > 160)")
        else:
            print(f"  [✓] {page} Meta Desc ({d_len} car.)")

    # 4. Vérification de l'absence de liens cassés vers pages/[secteur]/ ou contact.html?type=...
    print("\n--- 4. Contrôle de l'absence de liens cassés/obsolètes ---")
    legacy_patterns = [
        r"pages/hotel/", r"pages/restaurant/", r"pages/immobilier/", r"pages/clinique/",
        r"pages/pharmacie/", r"pages/voyage/",
        r"contact\.html\?type=cabinet-medical", r"contact\.html\?type=cabinet-dentaire", r"contact\.html\?type=salon-beaute",
        r"services\.html#hotel", r"services\.html#restaurant"
    ]

    all_html_files = [f for f in os.listdir(ROOT_DIR) if f.endswith(".html")]
    for hf in all_html_files:
        path = os.path.join(ROOT_DIR, hf)
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            code = f.read()
        for pat in legacy_patterns:
            matches = re.findall(pat, code)
            if matches:
                errors.append(f"{hf} contient encore {len(matches)} occurrence(s) du lien obsolète '{pat}'")

    if not any("contient encore" in e for e in errors):
        print("  [✓] Aucun lien obsolète détecté dans l'ensemble des pages HTML racine.")

    # 5. Vérification de Netlify Forms sur contact.html et commande.html
    print("\n--- 5. Contrôle de l'intégration Netlify Forms ---")
    for form_page in ["contact.html", "commande.html"]:
        path = os.path.join(ROOT_DIR, form_page)
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            code = f.read()
        
        if 'data-netlify="true"' not in code:
            errors.append(f"{form_page} : Attribut data-netlify=\"true\" absent sur le formulaire")
        else:
            print(f"  [✓] {form_page} contient data-netlify=\"true\"")
            
        if f'name="{form_page.replace(".html", "")}"' not in code and 'name="contact"' not in code and 'name="commande"' not in code:
            errors.append(f"{form_page} : Attribut name de formulaire manquant")
        else:
            print(f"  [✓] {form_page} nom de formulaire valide")

        if 'name="form-name"' not in code:
            errors.append(f"{form_page} : Champ caché input name=\"form-name\" manquant")
        else:
            print(f"  [✓] {form_page} champ caché form-name présent")

        if 'data-netlify-honeypot' not in code:
            errors.append(f"{form_page} : Piège anti-spam honeypot manquant")
        else:
            print(f"  [✓] {form_page} honeypot anti-spam présent")

    # Bilan final
    print("\n=== BILAN DU SPRINT 40 ===")
    if errors:
        print(f"❌ {len(errors)} ERREUR(S) DÉTECTÉE(S) :")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("✅ TOUTES LES VÉRIFICATIONS AUTOMATIQUES DU SPRINT 40 SONT VALIDES !")
        return True

if __name__ == "__main__":
    success = verify_sprint40()
    sys.exit(0 if success else 1)
