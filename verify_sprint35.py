import os, sys, re, glob

sys.stdout.reconfigure(encoding='utf-8')
ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'

print("==================================================")
print("     VÉRIFICATION COMPLÈTE SPRINT 35 — À PROPOS    ")
print("==================================================\n")

errors = []

# 1. Compilation & File Existence
a_propos_path = os.path.join(ROOT, 'a-propos.html')
pages_a_propos_path = os.path.join(ROOT, 'pages', 'a-propos.html')
css_a_propos_path = os.path.join(ROOT, 'assets', 'css', 'pages', 'a-propos.css')

if not os.path.exists(pages_a_propos_path):
    errors.append("Fichier source 'pages/a-propos.html' introuvable.")
else:
    print("✓ Fragment source 'pages/a-propos.html' présent.")

if not os.path.exists(css_a_propos_path):
    errors.append("Fichier CSS 'assets/css/pages/a-propos.css' introuvable.")
else:
    print("✓ Feuille CSS 'assets/css/pages/a-propos.css' présente.")

if not os.path.exists(a_propos_path):
    errors.append("Fichier compilé 'a-propos.html' à la racine introuvable.")
    print("❌ Fichier compilé 'a-propos.html' absent.")
    sys.exit(1)
else:
    size_kb = os.path.getsize(a_propos_path) / 1024
    print(f"✓ Page compilée 'a-propos.html' générée avec succès ({size_kb:.1f} KB).")

content = open(a_propos_path, encoding='utf-8').read()

# 2. Validation SEO
print("\n--- 1. VALIDATION SEO ---")

# Title
t_matches = re.findall(r'<title>(.*?)</title>', content, re.DOTALL | re.IGNORECASE)
if len(t_matches) != 1:
    errors.append(f"Nombre de balises <title> incorrect: {len(t_matches)}")
else:
    title = t_matches[0].strip()
    t_len = len(title)
    pipes = title.count('|')
    print(f"Title: '{title}' ({t_len} chars, {pipes} pipe)")
    if t_len > 60:
        errors.append(f"Title trop long (>60 chars): {t_len}")
    if pipes != 1:
        errors.append(f"Title doit contenir exactement 1 pipe '|': {pipes} trouvé(s)")
    if title != "À propos | Aziz Studio Digital":
        errors.append(f"Title non conforme au cahier des charges: {title}")

# Meta description
m_matches = re.findall(r'<meta\s+name="description"\s+content="(.*?)"', content, re.DOTALL | re.IGNORECASE)
if not m_matches:
    m_matches = re.findall(r'<meta\s+content="(.*?)"\s+name="description"', content, re.DOTALL | re.IGNORECASE)

if len(m_matches) != 1:
    errors.append(f"Nombre de <meta description> incorrect: {len(m_matches)}")
else:
    meta = m_matches[0].strip()
    m_len = len(meta)
    print(f"Meta Description: '{meta}' ({m_len} chars)")
    if m_len > 160:
        errors.append(f"Meta description trop longue (>160 chars): {m_len}")
    expected_meta = "Découvrez l'histoire, les valeurs et les engagements d'Aziz Studio Digital, agence web indépendante au service de votre réussite au Congo."
    if meta != expected_meta:
        errors.append(f"Meta description non conforme au cahier des charges: {meta}")

# H1 Count & Content
h1_matches = re.findall(r'<h1[\s>](.*?)</h1\s*>', content, re.DOTALL | re.IGNORECASE)
print(f"Nombre de H1: {len(h1_matches)}")
if len(h1_matches) != 1:
    errors.append(f"Exactement 1 H1 requis, trouvé(s): {len(h1_matches)}")
else:
    h1_text = re.sub(r'<[^>]+>', '', h1_matches[0]).strip()
    print(f"H1 Content: '{h1_text}'")

# Breadcrumb aria-current
if 'aria-current="page"' in content and 'À propos' in content:
    print("✓ Breadcrumb valide avec aria-current=\"page\" sur À propos.")
else:
    errors.append("Breadcrumb invalide ou sans aria-current='page'.")

# 3. Validation Ordre CSS & Pas de @import
print("\n--- 2. VALIDATION CSS ---")

css_links = re.findall(r'href=["\'](assets/css/[^"\']+)["\']', content)
page_css = [c for c in css_links if 'assets/css/pages/' in c]
expected_css = [
    'assets/css/pages/services.css',
    'assets/css/pages/creation-site-web.css',
    'assets/css/pages/a-propos.css'
]

print("Ordre des CSS de page chargés dans a-propos.html:")
for idx, c in enumerate(page_css, 1):
    print(f"  {idx}. {c}")

if page_css == expected_css:
    print("✓ Ordre de chargement des CSS de page CONFORME.")
else:
    errors.append(f"Ordre des CSS incorrect. Attendu: {expected_css}, Trouvé: {page_css}")

# Check @import across all CSS files
css_files = glob.glob(os.path.join(ROOT, 'assets', 'css', '**', '*.css'), recursive=True)
imports_found = []
for css_f in css_files:
    rel_p = os.path.relpath(css_f, ROOT)
    txt = open(css_f, encoding='utf-8').read()
    txt_no_comments = re.sub(r'/\*.*?\*/', '', txt, flags=re.DOTALL)
    if re.search(r'@import\s+', txt_no_comments):
        imports_found.append(rel_p)

if imports_found:
    errors.append(f"@import détecté dans: {imports_found}")
else:
    print("✓ 0 directive @import dans l'ensemble des fichiers CSS.")

# 4. Composants Premium Réutilisés
print("\n--- 3. VALIDATION COMPOSANTS PREMIUM ---")

# Hero Dashboard
if 'hero-dashboard' in content and 'azizstudiodigital.cg' in content:
    print("✓ Hero Dashboard réutilisé avec succès.")
else:
    errors.append("Hero Dashboard non détecté ou mal configuré.")

# Timeline 5 étapes
timeline_steps = re.findall(r'class=["\']timeline-step["\']', content)
print(f"Nombre d'étapes Timeline: {len(timeline_steps)}")
if len(timeline_steps) == 5:
    print("✓ Timeline Premium à 5 étapes validée.")
else:
    errors.append(f"Timeline doit contenir exactement 5 étapes, trouvé: {len(timeline_steps)}")

# FAQ Accordion 5 questions
faq_items = re.findall(r'<details\s+class=["\']faq-item', content)
print(f"Nombre de questions FAQ (<details>): {len(faq_items)}")
if len(faq_items) == 5:
    print("✓ FAQ Premium Accordion à 5 questions validée.")
else:
    errors.append(f"FAQ doit contenir exactement 5 questions, trouvé: {len(faq_items)}")

# CTA Final
if 'service-cta-final-card' in content and 'Construisons ensemble votre présence en ligne.' in content:
    print("✓ CTA Final Premium validé.")
else:
    errors.append("CTA Final Premium introuvable.")

# 5. Navigation & Menu Actif
print("\n--- 4. VALIDATION MENU ACTIF ---")

active_menu = re.search(r'href=["\']a-propos\.html["\']\s+class=["\']nav-link active["\']\s+aria-current=["\']page["\']', content)
if active_menu:
    print("✓ Menu À propos actif avec class='nav-link active' et aria-current='page'.")
else:
    errors.append("Lien de navigation À propos non actif.")

# 6. Audit Liens Interne & WCAG
print("\n--- 5. VALIDATION LIENS & WCAG ---")

# Liens cassés
hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
broken = []
for href in hrefs:
    if href.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', '#')):
        continue
    target = href.split('#')[0].split('?')[0]
    if target:
        target_path = os.path.join(ROOT, target)
        if not os.path.exists(target_path):
            broken.append(href)

if broken:
    errors.append(f"Liens cassés détectés dans a-propos.html: {broken}")
else:
    print("✓ 0 lien interne cassé dans a-propos.html.")

# Alt attributes
imgs = re.findall(r'<img\s+[^>]*>', content, re.IGNORECASE)
no_alt = [img for img in imgs if 'alt=' not in img.lower()]
if no_alt:
    errors.append(f"Images sans alt: {no_alt}")
else:
    print(f"✓ 100% des images ({len(imgs)}) possèdent un attribut 'alt'.")

# RAPPORT FINAL SPRINT 35
print("\n==================================================")
if not errors:
    print("   🎉 TOUTES LES VÉRIFICATIONS SONT VALIDÉES !   ")
    print("==================================================")
else:
    print(f"❌ {len(errors)} ERREUR(S) DÉTECTÉE(S) :")
    for err in errors:
        print(f"  - {err}")
    sys.exit(1)
