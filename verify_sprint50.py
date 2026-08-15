import os
import re
import sys

# Ensure UTF-8 stdout encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Use relative directory path (no hardcoded Windows absolute path)
ROOT = os.path.dirname(os.path.abspath(__file__))

print("=================================================================")
print("      VERIFY SPRINT 50 — TRANSITIONS FLUIDES ENTRE PAGES        ")
print("=================================================================")

errors = []

# ─── CHECK 1 : Présence centralisée de @view-transition dans base.css ───────
print("\n[1/4] Vérification de l'intégration centralisée de @view-transition dans base.css...")

base_css_path = os.path.join(ROOT, 'assets', 'css', 'base', 'base.css')
if not os.path.exists(base_css_path):
    errors.append("assets/css/base/base.css introuvable")
    css_content = ""
else:
    with open(base_css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()

    if '@view-transition' not in css_content:
        errors.append("@view-transition absente de base.css")
    else:
        print("  [OK] Règle @view-transition { navigation: auto; } présente dans base.css")

    if '::view-transition-old' not in css_content or '::view-transition-new' not in css_content:
        errors.append("Animations ::view-transition-old / ::view-transition-new manquantes dans base.css")
    else:
        print("  [OK] Pseudo-éléments ::view-transition-old et ::view-transition-new configurés")

# ─── CHECK 2 : Respect de prefers-reduced-motion ──────────────────────────────
print("\n[2/4] Vérification de l'accessibilité (prefers-reduced-motion)...")

if css_content:
    if 'prefers-reduced-motion' not in css_content:
        errors.append("Media query prefers-reduced-motion manquante dans base.css")
    else:
        print("  [OK] Media query @media (prefers-reduced-motion: reduce) configurée dans base.css")

# ─── CHECK 3 : Vérification de la non-duplication du code dans les HTML ──────
print("\n[3/4] Vérification de la centralisation (absence de duplication par page)...")

html_files = [os.path.join(ROOT, f) for f in os.listdir(ROOT) if f.endswith('.html')]

duplicated_in_html = 0
base_css_linked = 0

for fpath in html_files:
    rel_path = os.path.relpath(fpath, ROOT)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if '@view-transition' in content:
        duplicated_in_html += 1
    
    if 'assets/css/base/base.css' in content:
        base_css_linked += 1

if duplicated_in_html > 0:
    errors.append(f"@view-transition est dupliqué directement dans {duplicated_in_html} fichier(s) HTML")
else:
    print(f"  [OK] Aucune duplication de code de transition dans les {len(html_files)} fichiers HTML !")

if base_css_linked != len(html_files):
    errors.append(f"base.css lié à {base_css_linked}/{len(html_files)} pages HTML")
else:
    print(f"  [OK] base.css est correctement lié sur l'intégralité des {len(html_files)} pages compilées !")

# ─── CHECK 4 : Structure HTML et intégrité globale ────────────────────────────
print("\n[4/4] Vérification de l'intégrité de la structure HTML...")

required_elements = [
    ('Navigation principale', r'<nav\s+class="primary-navigation"'),
    ('Footer', r'<footer\s+class="site-footer"'),
    ('Header', r'<header\s+class="site-header"')
]

index_path = os.path.join(ROOT, 'index.html')
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        idx_content = f.read()
    for label, pattern in required_elements:
        if not re.search(pattern, idx_content):
            errors.append(f"Structure altérée : {label} non trouvé dans index.html")
        else:
            print(f"  [OK] {label} conservé sans régression")

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
    print("\n[OK] VÉRIFICATION RÉUSSIE — SPRINT 50 VALIDÉ !")
    sys.exit(0)
