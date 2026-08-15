import os
import re
import sys

# Ensure UTF-8 stdout encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Use relative directory path (no hardcoded Windows absolute path)
ROOT = os.path.dirname(os.path.abspath(__file__))

print("=================================================================")
print("  VERIFY SPRINT 51 — CORRECTIF CSS DES ICONES SUR CONTACT.HTML   ")
print("=================================================================")

errors = []

# ─── CHECK 1 : Audit automatisé du dimensionnement de toutes les balises <svg> ─
print("\n[1/4] Audit automatisé du dimensionnement CSS de toutes les balises <svg> sur les pages...")

html_files = [os.path.join(ROOT, f) for f in os.listdir(ROOT) if f.endswith('.html')]

unstyled_svg_count = 0
unstyled_details = []

for fpath in html_files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    css_links = re.findall(r'<link\s+rel="stylesheet"\s+href="([^"]+)"', content)
    combined_css = ""
    for css_rel in css_links:
        css_full = os.path.join(ROOT, css_rel.replace('/', os.sep))
        if os.path.exists(css_full):
            with open(css_full, 'r', encoding='utf-8', errors='ignore') as f:
                combined_css += f.read() + "\n"
    
    svg_matches = re.finditer(r'<svg([^>]*)>', content)
    for m in svg_matches:
        svg_attrs = m.group(1)
        # Fix Sprint 52: Exclude stroke-width="2" by checking word boundary and negative lookbehind
        has_inline_width = bool(re.search(r'(?<!stroke-)\bwidth\s*=', svg_attrs, re.I))
        has_inline_height = bool(re.search(r'\bheight\s*=', svg_attrs, re.I))
        has_inline_size = (has_inline_width or has_inline_height)
        
        class_match = re.search(r'class="([^"]+)"', svg_attrs)
        classes = class_match.group(1).split() if class_match else []
        
        has_css_size = False
        for cls in classes:
            pattern = r'\.' + re.escape(cls) + r'\b[^}]*\{[^}]*(width|height|max-width)'
            if re.search(r'\.' + re.escape(cls) + r'\b', combined_css):
                for block in re.finditer(r'\.' + re.escape(cls) + r'\b[^{]*\{([^}]+)\}', combined_css):
                    if re.search(r'\b(width|height|max-width)\b', block.group(1), re.I):
                        has_css_size = True
                        break
        
        if not has_inline_size and not has_css_size:
            unstyled_svg_count += 1
            unstyled_details.append((fname, classes, m.group(0)[:60]))

if unstyled_svg_count > 0:
    errors.append(f"{unstyled_svg_count} balise(s) <svg> sans règle de dimensionnement CSS décelée(s)")
    for fname, classes, snippet in unstyled_details[:10]:
        print(f"  [FAIL] {fname} -> classes: {classes} | {snippet}")
else:
    print(f"  [OK] 100% des balises <svg> sur les {len(html_files)} pages possèdent une règle de dimensionnement valides !")

# ─── CHECK 2 : Vérification spécifique de contact.html et contact.css ─────────
print("\n[2/4] Vérification de l'indépendance CSS et des règles d'icônes dans contact.css...")

contact_html_path = os.path.join(ROOT, 'contact.html')
if not os.path.exists(contact_html_path):
    errors.append("contact.html introuvable à la racine")
else:
    with open(contact_html_path, 'r', encoding='utf-8') as f:
        c_html = f.read()
    
    # Check Layer 3 stylesheet
    page_css_links = [m for m in re.findall(r'<link\s+rel="stylesheet"\s+href="([^"]+)"', c_html) if 'assets/css/pages/' in m]
    if page_css_links != ['assets/css/pages/contact.css']:
        errors.append(f"contact.html charge des CSS de pages incorrects : {page_css_links}")
    else:
        print("  [OK] contact.html charge uniquement assets/css/pages/contact.css en Layer 3 (pas de home.css / creation-site-web.css)")

contact_css_path = os.path.join(ROOT, 'assets', 'css', 'pages', 'contact.css')
if not os.path.exists(contact_css_path):
    errors.append("assets/css/pages/contact.css introuvable")
else:
    with open(contact_css_path, 'r', encoding='utf-8') as f:
        c_css = f.read()
    
    required_rules = ['.processus-icon-wrapper', '.processus-icon', '.outcome-check', '.clock-icon']
    missing_rules = [r for r in required_rules if r not in c_css]
    
    if missing_rules:
        errors.append(f"Règles CSS manquantes dans contact.css : {missing_rules}")
    else:
        print("  [OK] Les règles CSS d'icônes (.processus-icon-wrapper, .processus-icon, .outcome-check, .clock-icon) sont toutes présentes dans contact.css")

# ─── CHECK 3 : Vérification de non-régression (Transitions & Emojis) ──────────
print("\n[3/4] Vérification de non-régression (Transitions Sprint 50 & Emojis Sprint 48-49)...")

base_css_path = os.path.join(ROOT, 'assets', 'css', 'base', 'base.css')
if os.path.exists(base_css_path):
    with open(base_css_path, 'r', encoding='utf-8') as f:
        base_css = f.read()
    if '@view-transition' not in base_css or 'prefers-reduced-motion' not in base_css:
        errors.append("Règles @view-transition / prefers-reduced-motion altérées dans base.css")
    else:
        print("  [OK] Transitions de page @view-transition et prefers-reduced-motion intactes dans base.css")

# ─── CHECK 4 : Absence de résidus Unicode ─────────────────────────────────────
print("\n[4/4] Vérification de l'absence de résidus Unicode (U+FE0F / U+FE0E)...")

total_residus = 0
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    total_residus += content.count('\uFE0F') + content.count('\uFE0E')

if total_residus > 0:
    errors.append(f"{total_residus} résidu(s) Unicode U+FE0F/U+FE0E décelé(s)")
else:
    print("  [OK] Aucun résidu Unicode U+FE0F / U+FE0E décelé sur l'ensemble du site !")

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
    print("\n[OK] VÉRIFICATION RÉUSSIE — SPRINT 51 VALIDÉ !")
    sys.exit(0)
