import os
import re
import sys

# Ensure UTF-8 stdout encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Use relative directory path (no hardcoded Windows absolute path)
ROOT = os.path.dirname(os.path.abspath(__file__))

print("=================================================================")
print("      VERIFY SPRINT 48 — REMPLACEMENT EMOJIS PAR ICONES LUCIDE    ")
print("=================================================================")

errors = []

# Table of emojis from Sprint 48 specification
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

print(f"\n[1/3] Scan automatisé d'absence d'emojis sur {len(html_files)} fichiers HTML...")

total_remaining_emojis = 0
files_with_emojis = []

for fpath in html_files:
    rel_path = os.path.relpath(fpath, ROOT)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    matches = emoji_regex.findall(content)
    if matches:
        total_remaining_emojis += len(matches)
        files_with_emojis.append((rel_path, len(matches), set(matches)))

if total_remaining_emojis > 0:
    errors.append(f"{total_remaining_emojis} emoji(s) restant(s) décelé(s) dans {len(files_with_emojis)} fichier(s)")
    for rel_path, count, emojis_set in files_with_emojis:
        print(f"  [FAIL] {rel_path} : {count} emoji(s) {emojis_set}")
else:
    print(f"  [OK] Aucun emoji Unicode restant sur les {len(html_files)} fichiers scannés !")

# ─── CHECK 2 : Présence et conformité des icônes SVG inline ─────────────────
print("\n[2/3] Vérification des icônes SVG inline et de l'attribut aria-hidden='true'...")

total_svg_count = 0
total_lucide_svgs = 0
svg_without_aria_hidden = 0

for fpath in html_files:
    rel_path = os.path.relpath(fpath, ROOT)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    svg_tags = re.findall(r'<svg[^>]*>', content)
    lucide_svgs = re.findall(r'<svg[^>]*class="[^"]*lucide-icon[^"]*"[^>]*>', content)
    
    total_svg_count += len(svg_tags)
    total_lucide_svgs += len(lucide_svgs)
    
    for tag in svg_tags:
        if 'aria-hidden="true"' not in tag and 'aria-hidden=\'true\'' not in tag:
            # check if it's a decorative icon tag without aria-hidden
            svg_without_aria_hidden += 1

print(f"  [OK] Total de balises <svg> détectées : {total_svg_count}")
print(f"  [OK] Balises <svg class=\"lucide-icon...\"> détectées : {total_lucide_svgs}")

if svg_without_aria_hidden > 0:
    errors.append(f"{svg_without_aria_hidden} balise(s) <svg> sans attribut aria-hidden='true'")
else:
    print("  [OK] Toutes les balises <svg> possèdent bien aria-hidden='true' !")

# ─── CHECK 3 : Vérification du fichier CSS global ───────────────────────────
print("\n[3/3] Vérification de la classe CSS .lucide-icon / .icon-inline dans base.css...")

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
    print("\n[OK] VÉRIFICATION RÉUSSIE — SPRINT 48 VALIDÉ !")
    sys.exit(0)
