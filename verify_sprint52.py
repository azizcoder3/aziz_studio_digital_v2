import os
import re
import sys

# Ensure UTF-8 stdout encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Use relative directory path (no hardcoded Windows absolute path)
ROOT = os.path.dirname(os.path.abspath(__file__))

print("=================================================================")
print("  VERIFY SPRINT 52 — CORRECTIF CSS ICONES FAQ ET AUDIT REFORCE   ")
print("=================================================================")

errors = []

# ─── FUNCTION: SVG Audit Engine ───────────────────────────────────────────────
def audit_svg_in_content(html_content, combined_css):
    """
    Scans html_content for <svg> tags and verifies if each SVG is styled either:
    1) Via inline HTML width="..." or height="..." attributes (excluding stroke-width="...")
    2) Via a CSS rule in combined_css defining width, height, or max-width for at least one of its classes.
    Returns a list of unstyled SVG details: (classes, tag_snippet)
    """
    unstyled = []
    svg_matches = re.finditer(r'<svg([^>]*)>', html_content)
    for m in svg_matches:
        svg_attrs = m.group(1)
        
        # Sprint 52 Fix: Exclude stroke-width="2" using negative lookbehind and word boundary
        has_inline_width = bool(re.search(r'(?<!stroke-)\bwidth\s*=', svg_attrs, re.I))
        has_inline_height = bool(re.search(r'\bheight\s*=', svg_attrs, re.I))
        has_inline_size = (has_inline_width or has_inline_height)
        
        class_match = re.search(r'class="([^"]+)"', svg_attrs)
        classes = class_match.group(1).split() if class_match else []
        
        has_css_size = False
        for cls in classes:
            if re.search(r'\.' + re.escape(cls) + r'\b', combined_css):
                for block in re.finditer(r'\.' + re.escape(cls) + r'\b[^{]*\{([^}]+)\}', combined_css):
                    if re.search(r'\b(width|height|max-width)\b', block.group(1), re.I):
                        has_css_size = True
                        break
        
        if not has_inline_size and not has_css_size:
            unstyled.append((classes, m.group(0)[:70]))
            
    return unstyled

# ─── CHECK 1 : Preuve de fonctionnement du moteur d'audit (Test de Faux Positif) ─
print("\n[1/5] Preuve de détection du moteur d'audit SVG (test sur cas délibérément cassé)...")

mock_html_broken = '<svg class="dummy-broken-icon" stroke-width="2" aria-hidden="true"><circle cx="10" cy="10" r="5"></circle></svg>'
mock_css_dummy = '.dummy-broken-icon { color: red; }' # missing width/height

detected_mock = audit_svg_in_content(mock_html_broken, mock_css_dummy)
if len(detected_mock) == 1:
    print("  [OK] Preuve de détection réussie : le moteur a correctement attrapé l'icône cassée fictive (1/1 décelée) !")
else:
    errors.append("Le moteur d'audit SVG n'a pas détecté le cas de test fictif cassé !")

# ─── CHECK 2 : Audit sur les 38 pages HTML du projet ──────────────────────────
print("\n[2/5] Audit automatisé du dimensionnement CSS des balises <svg> sur les 38 pages du projet...")

html_files = [os.path.join(ROOT, f) for f in os.listdir(ROOT) if f.endswith('.html')]

total_unstyled = 0
unstyled_by_file = {}

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
    
    un_list = audit_svg_in_content(content, combined_css)
    if un_list:
        total_unstyled += len(un_list)
        unstyled_by_file[fname] = un_list

if total_unstyled > 0:
    errors.append(f"{total_unstyled} balise(s) <svg> non stylisée(s) décelée(s) dans le projet")
    for fname, details in unstyled_by_file.items():
        print(f"  [FAIL] {fname} -> {len(details)} icône(s) non stylisée(s) : {details}")
else:
    print(f"  [OK] 100% des balises <svg> sur les {len(html_files)} pages possèdent une règle de taille CSS valide !")

# ─── CHECK 3 : Vérification explicite de contact.html et contact.css ──────────
print("\n[3/5] Vérification explicite des règles FAQ dans contact.css et de l'isolation CSS...")

contact_html_path = os.path.join(ROOT, 'contact.html')
if not os.path.exists(contact_html_path):
    errors.append("contact.html introuvable à la racine")
else:
    with open(contact_html_path, 'r', encoding='utf-8') as f:
        c_html = f.read()
    
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
    
    faq_rules = [
        '.faq-icon-wrapper',
        '.faq-icon',
        '.faq-chevron',
        '.faq-item:hover .faq-icon-wrapper',
        '.faq-item[open] .faq-icon-wrapper',
        '.faq-summary:hover .faq-chevron',
        '.faq-item[open] .faq-chevron'
    ]
    missing_faq_rules = [r for r in faq_rules if r not in c_css]
    
    if missing_faq_rules:
        errors.append(f"Règles FAQ CSS manquantes dans contact.css : {missing_faq_rules}")
    else:
        print("  [OK] Les règles FAQ CSS (.faq-icon-wrapper, .faq-icon, .faq-chevron, et états open/hover) sont toutes présentes dans contact.css")

# ─── CHECK 4 : Non-régression sur Transitions (Sprint 50) ─────────────────────
print("\n[4/5] Vérification de non-régression sur les View Transitions (Sprint 50)...")

base_css_path = os.path.join(ROOT, 'assets', 'css', 'base', 'base.css')
if os.path.exists(base_css_path):
    with open(base_css_path, 'r', encoding='utf-8') as f:
        base_css = f.read()
    if '@view-transition' not in base_css or 'prefers-reduced-motion' not in base_css:
        errors.append("Règles @view-transition / prefers-reduced-motion altérées dans base.css")
    else:
        print("  [OK] Transitions de page @view-transition et prefers-reduced-motion intactes dans base.css")

# ─── CHECK 5 : Non-régression sur les Emojis (Sprints 48 & 49) ─────────────────
print("\n[5/5] Vérification de l'absence de résidus Unicode et emojis de base...")

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
    print("\n[OK] VÉRIFICATION RÉUSSIE — SPRINT 52 VALIDÉ !")
    sys.exit(0)
