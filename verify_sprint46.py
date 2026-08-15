import os
import re
import sys

# Ensure UTF-8 stdout encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'

print("=================================================================")
print("     VERIFY SPRINT 46 — CORRECTIF CSS CONTACT + DOC COQUILLE    ")
print("=================================================================")

errors = []

# ─── CHECK 1 : Ordre CSS de contact.html ─────────────────────────────────────
print("\n[1/3] Vérification de l'ordre CSS de contact.html (Base → Composants → Pages)...")

contact_path = os.path.join(ROOT, 'contact.html')
if not os.path.exists(contact_path):
    errors.append("contact.html introuvable")
else:
    content = open(contact_path, 'r', encoding='utf-8').read()
    css_links = re.findall(r'<link rel="stylesheet" href="([^"]+)">', content)

    base_indices  = [i for i, c in enumerate(css_links) if '/base/' in c]
    comp_indices  = [i for i, c in enumerate(css_links) if '/components/' in c]
    page_indices  = [i for i, c in enumerate(css_links) if '/pages/' in c]

    if not base_indices or not comp_indices or not page_indices:
        errors.append("contact.html : couche CSS manquante (base, composants ou pages)")
    elif max(base_indices) > min(comp_indices):
        errors.append("contact.html : Layer Base doit précéder Layer Composants")
    elif max(comp_indices) > min(page_indices):
        errors.append(
            f"contact.html : Layer Composants ({max(comp_indices)}) "
            f"dépasse Layer Pages ({min(page_indices)}) — ordre invalide"
        )
    else:
        print(f"  [OK] Ordre CSS strict Base → Composants → Pages respecté sur contact.html")
        print(f"       Liens CSS détectés : {css_links}")

# ─── CHECK 2 : Absence de services.css et creation-site-web.css sur contact.html ─
print("\n[2/3] Vérification de l'absence de services.css / creation-site-web.css sur contact.html...")

if os.path.exists(contact_path):
    content = open(contact_path, 'r', encoding='utf-8').read()
    if 'assets/css/pages/services.css' in content:
        errors.append("contact.html référence encore assets/css/pages/services.css (doit être absent)")
    else:
        print("  [OK] services.css absent de contact.html")

    if 'assets/css/pages/creation-site-web.css' in content:
        errors.append("contact.html référence encore assets/css/pages/creation-site-web.css (doit être absent)")
    else:
        print("  [OK] creation-site-web.css absent de contact.html")

# ─── CHECK 3 : Documentation "36 URLs indexables" ────────────────────────────
print("\n[3/3] Vérification de la documentation finale (36 URLs indexables)...")

doc_path = os.path.join(ROOT, 'docs', 'final-project-documentation.md')
if not os.path.exists(doc_path):
    errors.append("docs/final-project-documentation.md introuvable")
else:
    doc_content = open(doc_path, 'r', encoding='utf-8').read()

    if '35 URLs indexables' in doc_content:
        errors.append("docs/final-project-documentation.md contient encore '35 URLs indexables' (coquille non corrigée)")
    else:
        print("  [OK] Aucune occurrence de '35 URLs indexables' dans final-project-documentation.md")

    if '36 URLs indexables' in doc_content:
        print("  [OK] '36 URLs indexables' présent dans final-project-documentation.md")
    else:
        errors.append("docs/final-project-documentation.md ne contient pas '36 URLs indexables'")

# ─── RÉSULTATS ────────────────────────────────────────────────────────────────
print("\n=================================================================")
print(f"RÉSULTATS : {len(errors)} erreur(s)")
print("=================================================================")

if errors:
    print("\n[FAIL] VÉRIFICATION ÉCHOUÉE :")
    for err in errors:
        print(f"  - {err}")
    sys.exit(1)
else:
    print("\n[OK] VÉRIFICATION RÉUSSIE — SPRINT 46 VALIDÉ !")
    sys.exit(0)
