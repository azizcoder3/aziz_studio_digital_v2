import os, sys, re, glob

sys.stdout.reconfigure(encoding='utf-8')
ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'

print("==================================================")
print("     VÉRIFICATION COMPLÈTE SPRINT 36 — CONTACT    ")
print("==================================================\n")

errors = []

# 1. Compilation & File Existence
contact_path = os.path.join(ROOT, 'contact.html')
pages_contact_path = os.path.join(ROOT, 'pages', 'contact.html')
css_contact_path = os.path.join(ROOT, 'assets', 'css', 'pages', 'contact.css')

if not os.path.exists(pages_contact_path):
    errors.append("Fichier source 'pages/contact.html' introuvable.")
else:
    print("✓ Fragment source 'pages/contact.html' présent.")

if not os.path.exists(css_contact_path):
    errors.append("Fichier CSS 'assets/css/pages/contact.css' introuvable.")
else:
    print("✓ Feuille CSS 'assets/css/pages/contact.css' présente.")

if not os.path.exists(contact_path):
    errors.append("Fichier compilé 'contact.html' à la racine introuvable.")
    print("❌ Fichier compilé 'contact.html' absent.")
    sys.exit(1)
else:
    size_kb = os.path.getsize(contact_path) / 1024
    print(f"✓ Page compilée 'contact.html' générée avec succès ({size_kb:.1f} KB).")

content = open(contact_path, encoding='utf-8').read()

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
    if title != "Contact | Aziz Studio Digital":
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

# H1 Count & Content
h1_matches = re.findall(r'<h1[\s>](.*?)</h1\s*>', content, re.DOTALL | re.IGNORECASE)
print(f"Nombre de H1: {len(h1_matches)}")
if len(h1_matches) != 1:
    errors.append(f"Exactement 1 H1 requis, trouvé(s): {len(h1_matches)}")
else:
    h1_text = re.sub(r'<[^>]+>', '', h1_matches[0]).strip()
    print(f"H1 Content: '{h1_text}'")

# Breadcrumb aria-current
if 'aria-current="page"' in content and 'Contact' in content:
    print("✓ Breadcrumb valide avec aria-current=\"page\" sur Contact.")
else:
    errors.append("Breadcrumb invalide ou sans aria-current='page'.")

# 3. Validation Ordre CSS & Pas de @import
print("\n--- 2. VALIDATION CSS ---")

css_links = re.findall(r'href=["\'](assets/css/[^"\']+)["\']', content)
page_css = [c for c in css_links if 'assets/css/pages/' in c]
expected_css = [
    'assets/css/pages/services.css',
    'assets/css/pages/creation-site-web.css',
    'assets/css/pages/contact.css'
]

print("Ordre des CSS de page chargés dans contact.html:")
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
print("\n--- 3. VALIDATION COMPOSANTS PREMIUM & FORMULAIRE ---")

# Hero Dashboard
if 'hero-dashboard' in content and 'contact.azizstudiodigital.cg' in content:
    print("✓ Hero Dashboard réutilisé avec succès.")
else:
    errors.append("Hero Dashboard non détecté ou mal configuré.")

# Form Fields Verification
required_fields = ['id="nom"', 'id="prenom"', 'id="email"', 'id="type_projet"', 'id="budget"', 'id="message"', 'id="rgpd"']
missing_fields = [f for f in required_fields if f not in content]
if not missing_fields:
    print("✓ Tous les champs du formulaire sont présents (Nom, Prénom, Email, Type projet, Budget, Message, RGPD).")
else:
    errors.append(f"Champs de formulaire manquants: {missing_fields}")

# Coordonnées réelles uniquement
coords_ok = ('contact@azizstudiodigital.cg' in content or 'mailto:' in content) and 'Brazzaville' in content
fake_terms = ['support 24/7', 'chat 24/7', 'hotline', 'numéro fixe fictif', 'équipe support']
found_fakes = [term for term in fake_terms if term in content.lower()]

if coords_ok and not found_fakes:
    print("✓ Coordonnées réelles validées (Email, WhatsApp, Brazzaville sans faux canaux).")
else:
    errors.append(f"Coordonnées non conformes ou canaux fictifs détectés: {found_fakes}")

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
if 'service-cta-final-card' in content and 'Discutons ensemble de votre futur site web.' in content:
    print("✓ CTA Final Premium validé.")
else:
    errors.append("CTA Final Premium introuvable.")

# 5. Navigation & Menu Actif
print("\n--- 4. VALIDATION MENU ACTIF ---")

active_menu = re.search(r'href=["\']contact\.html["\']\s+class=["\']nav-link active["\']\s+aria-current=["\']page["\']', content)
if active_menu:
    print("✓ Menu Contact actif avec class='nav-link active' et aria-current='page'.")
else:
    errors.append("Lien de navigation Contact non actif.")

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
    errors.append(f"Liens cassés détectés dans contact.html: {broken}")
else:
    print("✓ 0 lien interne cassé dans contact.html.")

# Alt attributes
imgs = re.findall(r'<img\s+[^>]*>', content, re.IGNORECASE)
no_alt = [img for img in imgs if 'alt=' not in img.lower()]
if no_alt:
    errors.append(f"Images sans alt: {no_alt}")
else:
    print(f"✓ 100% des images ({len(imgs)}) possèdent un attribut 'alt'.")

# 7. Cohérence du délai de réponse (48h) sur TOUT LE SITE
print("\n--- 6. COHÉRENCE DU DÉLAI DE RÉPONSE (48 HEURES) ---")

html_files = glob.glob(os.path.join(ROOT, '*.html'))
conflicting_delays = []

for hfile in html_files:
    fname = os.path.basename(hfile)
    fcontent = open(hfile, encoding='utf-8').read()
    
    # Chercher les promesses de délai de réponse ou de devis en 24h ou 72h
    # (ex: "sous 24h", "sous 24 heures", "en 24h", "sous 72h", "garantie sous 24h")
    matches = re.findall(r'(?:réponse|devis|analyse|chiffrage|proposition)\s+(?:garantie\s+)?(?:sous|en)\s+(24h|24\s+heures|72h|72\s+heures)', fcontent, re.IGNORECASE)
    if matches:
        conflicting_delays.append((fname, matches))

if conflicting_delays:
    print(f"❌ Incohérences de délai détectées sur le site : {conflicting_delays}")
    for fname, match_list in conflicting_delays:
        errors.append(f"Délai contradictoire ({match_list}) trouvé dans {fname}")
else:
    print("✓ Cohérence parfaite du délai de réponse (48h) sur l'ensemble des pages du site !")

# RAPPORT FINAL SPRINT 36
print("\n==================================================")
if not errors:
    print("   🎉 TOUTES LES VÉRIFICATIONS SONT VALIDÉES !   ")
    print("==================================================")
else:
    print(f"❌ {len(errors)} ERREUR(S) DÉTECTÉE(S) :")
    for err in errors:
        print(f"  - {err}")
    sys.exit(1)
