import os
import re
import sys

# Ensure UTF-8 stdout encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Use relative directory path (no hardcoded Windows absolute path)
ROOT = os.path.dirname(os.path.abspath(__file__))

print("=================================================================")
print("  VERIFY SPRINT 49 — NETTOYAGE RESIDUS UNICODE POST-SPRINT 48   ")
print("=================================================================")

errors = []

# Table of base emojis from Sprint 48 specification
EMOJIS_MAPPING = [
    '⚡', '✓', '❓', '📦', '💡', '🚀', '⚙', '🛠', '📍', '💎',
    '📋', '🎯', '⭐', '🌟', '🤝', '👁', '🔍', '💬', '🏠', '🏢',
    '✨', '📊', '🎨', '📱', '🦷', '📝', '🎞', '💼', '📈', '💖',
    '💻', '🔄', '🛡', '🏨', '🛏', '📚', '📖', '📰', '⚖', '🏛',
    '🍖', '🍽', '🥩', '🛒', '🗂', '📂', '🏪', '🏗', '🗄', '👋',
    '🚌', '🏆', '🔐', '🔒', '📧', '✉', '💊', '🩺', '🔲', '🎬',
    '♿', '🎉', '💳', '🔔', '👗', '💰', '🧩', '🎓', '✕', '💉',
    '🤖', '🎫', '🌱', '🖼', '🏥', '📞', '👤', '🌐', '🌍', '✈',
    '🔷', '📡', '⚠'
]

emoji_regex = re.compile('|'.join(re.escape(e) for e in EMOJIS_MAPPING))

# Collect all HTML files (root pages and pages/ directory)
html_files = []

for item in os.listdir(ROOT):
    if item.endswith('.html'):
        html_files.append(os.path.join(ROOT, item))

pages_dir = os.path.join(ROOT, 'pages')
if os.path.exists(pages_dir):
    for root_dir, dirs, files in os.walk(pages_dir):
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root_dir, f))

components_dir = os.path.join(ROOT, 'components')
if os.path.exists(components_dir):
    for root_dir, dirs, files in os.walk(components_dir):
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root_dir, f))

html_files = sorted(list(set(html_files)))

# ─── CHECK 1 : Scan d'absence de résidus Unicode (\uFE0F / \uFE0E) ───────────
print(f"\n[1/4] Scan d'absence des sélecteurs de variation Unicode (U+FE0F et U+FE0E) sur {len(html_files)} fichiers...")

total_residus = 0
files_with_residus = []

for fpath in html_files:
    rel_path = os.path.relpath(fpath, ROOT)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    c_fe0f = content.count('\uFE0F')
    c_fe0e = content.count('\uFE0E')
    
    if c_fe0f > 0 or c_fe0e > 0:
        total_residus += (c_fe0f + c_fe0e)
        files_with_residus.append((rel_path, c_fe0f, c_fe0e))

if total_residus > 0:
    errors.append(f"{total_residus} résidu(s) Unicode U+FE0F/U+FE0E trouvé(s) dans {len(files_with_residus)} fichier(s)")
    for rel_path, c16, c15 in files_with_residus:
        print(f"  [FAIL] {rel_path} : U+FE0F = {c16}, U+FE0E = {c15}")
else:
    print(f"  [OK] Aucun résidu Unicode U+FE0F / U+FE0E restant sur les {len(html_files)} fichiers HTML !")

# ─── CHECK 2 : Scan d'absence des emojis de base (Sprint 48) ───────────────
print(f"\n[2/4] Scan d'absence des emojis de base sur {len(html_files)} fichiers HTML...")

total_emojis = 0
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    matches = emoji_regex.findall(content)
    if matches:
        total_emojis += len(matches)

if total_emojis > 0:
    errors.append(f"{total_emojis} emoji(s) de base restant(s) décelé(s)")
else:
    print(f"  [OK] Aucun emoji Unicode de base restant sur l'ensemble des pages !")

# ─── CHECK 3 : Présence et conformité des icônes SVG inline ─────────────────
print("\n[3/4] Vérification des icônes SVG inline et de l'attribut aria-hidden='true'...")

total_svg_count = 0
total_lucide_svgs = 0
svg_without_aria_hidden = 0

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    svg_tags = re.findall(r'<svg[^>]*>', content)
    lucide_svgs = re.findall(r'<svg[^>]*class="[^"]*lucide-icon[^"]*"[^>]*>', content)
    
    total_svg_count += len(svg_tags)
    total_lucide_svgs += len(lucide_svgs)
    
    for tag in svg_tags:
        if 'aria-hidden="true"' not in tag and 'aria-hidden=\'true\'' not in tag:
            svg_without_aria_hidden += 1

print(f"  [OK] Total de balises <svg> détectées : {total_svg_count}")
print(f"  [OK] Balises <svg class=\"lucide-icon...\"> détectées : {total_lucide_svgs}")

if svg_without_aria_hidden > 0:
    errors.append(f"{svg_without_aria_hidden} balise(s) <svg> sans attribut aria-hidden='true'")
else:
    print("  [OK] Toutes les balises <svg> possèdent bien aria-hidden='true' !")

# ─── CHECK 4 : Vérification du fichier CSS global ───────────────────────────
print("\n[4/4] Vérification de la classe CSS .lucide-icon dans base.css...")

base_css_path = os.path.join(ROOT, 'assets', 'css', 'base', 'base.css')
if not os.path.exists(base_css_path):
    errors.append("assets/css/base/base.css introuvable")
else:
    with open(base_css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    if '.lucide-icon' not in css_content and '.icon-inline' not in css_content:
        errors.append("Règle CSS .lucide-icon / .icon-inline absente de base.css")
    else:
        print("  [OK] Styles CSS globaux .lucide-icon présents dans base.css")

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
    print("\n[OK] VÉRIFICATION RÉUSSIE — SPRINT 49 VALIDÉ !")
    sys.exit(0)
