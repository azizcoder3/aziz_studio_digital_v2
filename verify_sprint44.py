import os
import sys
import re
import glob

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'
EXPECTED_DOMAIN = "https://azizstudiodigital.netlify.app"

html_files = sorted(glob.glob(os.path.join(ROOT, '*.html')))
all_filenames = set(os.path.basename(f) for f in html_files)

# Sitemap & Robots check
sitemap_path = os.path.join(ROOT, 'sitemap.xml')
robots_path = os.path.join(ROOT, 'robots.txt')

errors = []
warnings = []

# 1. Sitemap check
if not os.path.exists(sitemap_path):
    errors.append("Fichier sitemap.xml manquant.")
else:
    with open(sitemap_path, encoding='utf-8') as f:
        sitemap_content = f.read()
    sitemap_urls = set(re.findall(r'<loc>(.*?)</loc>', sitemap_content))
    if EXPECTED_DOMAIN not in sitemap_content:
        errors.append(f"sitemap.xml ne contient pas le domaine attendu {EXPECTED_DOMAIN}")
    if "azizstudiodigital.com" in sitemap_content:
        errors.append("sitemap.xml contient des références au futur domaine (.com)")

# 2. Robots check
if not os.path.exists(robots_path):
    errors.append("Fichier robots.txt manquant.")
else:
    with open(robots_path, encoding='utf-8') as f:
        robots_content = f.read()
    if f"Sitemap: {EXPECTED_DOMAIN}/sitemap.xml" not in robots_content:
        errors.append("robots.txt ne référence pas correctement le sitemap.xml de production.")
    if "azizstudiodigital.com" in robots_content:
        errors.append("robots.txt référence le futur domaine (.com)")

# 3. HTML Pages audit
file_ids = {}
for filepath in html_files:
    filename = os.path.basename(filepath)
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    ids = set(re.findall(r'id=["\'](.*?)["\']', content))
    file_ids[filename] = ids

for filepath in html_files:
    filename = os.path.basename(filepath)
    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    # Title check
    m_title = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    if not m_title:
        errors.append(f"[{filename}] Balise <title> manquante.")
    else:
        title = m_title.group(1).strip()
        # count title length: unescape &amp; to & for character count if present
        clean_title_text = title.replace('&amp;', '&')
        if len(clean_title_text) > 60:
            errors.append(f"[{filename}] Titre trop long ({len(clean_title_text)} chars > 60) : '{title}'")
        if title.count('|') != 1:
            errors.append(f"[{filename}] Le titre doit contenir exactement 1 pipe '|' (trouvé {title.count('|')})")

    # Description check
    m_desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE | re.DOTALL)
    if not m_desc:
        errors.append(f"[{filename}] Meta description manquante.")
    else:
        desc = m_desc.group(1).strip()
        if len(desc) > 160:
            errors.append(f"[{filename}] Meta description trop longue ({len(desc)} chars > 160)")

    # Canonical check
    m_canon = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', content, re.IGNORECASE | re.DOTALL)
    if not m_canon:
        errors.append(f"[{filename}] Balise canonical manquante.")
    else:
        canon = m_canon.group(1).strip()
        if not canon.startswith(EXPECTED_DOMAIN):
            errors.append(f"[{filename}] Canonical ne pointe pas vers {EXPECTED_DOMAIN} (trouvé: '{canon}')")

    # OG URL check
    m_og_url = re.search(r'<meta\s+property=["\']og:url["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE | re.DOTALL)
    if not m_og_url:
        errors.append(f"[{filename}] Open Graph og:url manquant.")
    else:
        og_url = m_og_url.group(1).strip()
        if not og_url.startswith(EXPECTED_DOMAIN):
            errors.append(f"[{filename}] og:url ne pointe pas vers {EXPECTED_DOMAIN} (trouvé: '{og_url}')")

    # H1 check
    h1_count = len(re.findall(r'<h1\b', content, re.IGNORECASE))
    if h1_count != 1:
        errors.append(f"[{filename}] Doit contenir strictement 1 seul <h1> (trouvé: {h1_count})")

    # Localhost & Future Domain check
    if re.search(r'(localhost|127\.0\.0\.1)', content, re.IGNORECASE):
        errors.append(f"[{filename}] Contient une référence localhost ou 127.0.0.1")
    if re.search(r'azizstudiodigital\.com', content, re.IGNORECASE):
        errors.append(f"[{filename}] Contient une référence au futur domaine azizstudiodigital.com")

    # Schema.org check
    if 'application/ld+json' not in content:
        errors.append(f"[{filename}] Données structurées Schema.org (JSON-LD) manquantes.")

    # Sitemap registration check (except non-indexed pages)
    m_robots = re.search(r'<meta\s+name=["\']robots["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
    is_noindex = m_robots and 'noindex' in m_robots.group(1)
    if not is_noindex:
        expected_url = f"{EXPECTED_DOMAIN}/{'' if filename == 'index.html' else filename}"
        expected_url_slash = f"{EXPECTED_DOMAIN}/" if filename == 'index.html' else expected_url
        if expected_url not in sitemap_urls and expected_url_slash not in sitemap_urls:
            errors.append(f"[{filename}] Page indexable non trouvée dans sitemap.xml")

    # Internal links check
    hrefs = re.findall(r'href=["\'](.*?)["\']', content)
    for href in hrefs:
        if href.startswith(('tel:', 'mailto:', 'javascript:', 'http://', 'https://')):
            continue
        
        # Check internal link existence (removing query params and hash)
        target_file = href.split('?')[0].split('#')[0]
        if target_file and target_file not in all_filenames and not os.path.exists(os.path.join(ROOT, target_file)):
            errors.append(f"[{filename}] Lien cassé vers fichier inexistant : '{href}'")
        
        # Check hash anchor if hash exists (e.g. page.html#section or #section)
        if '#' in href:
            parts = href.split('#')
            target_page = parts[0].split('?')[0]
            target_hash = parts[1].split('?')[0] if len(parts) > 1 else ""
            if target_hash:
                page_to_check = target_page if target_page != "" else filename
                if page_to_check in file_ids and target_hash not in file_ids[page_to_check]:
                    errors.append(f"[{filename}] Ancre hachée inexistante '{href}' (ID '{target_hash}' absent de {page_to_check})")

# 4. Form and Email Function Security Check
send_autoreply_path = os.path.join(ROOT, 'netlify', 'functions', 'send-autoreply.js')
if not os.path.exists(send_autoreply_path):
    errors.append("Fonction Netlify send-autoreply.js manquante.")
else:
    with open(send_autoreply_path, encoding='utf-8') as f:
        fn_code = f.read()
    if 'process.env.GMAIL_USER' not in fn_code or 'process.env.GMAIL_APP_PASSWORD' not in fn_code:
        errors.append("send-autoreply.js n'utilise pas exclusivement process.env pour Gmail Auth.")

# Report results
print("=" * 80)
print(" VERIFY SPRINT 44 — CONTROLE DE PREPARATION A LA MISE EN PRODUCTION")
print("=" * 80)

print(f"Total pages HTML analysées : {len(html_files)}")
print(f"Erreurs détectées : {len(errors)}")
print(f"Avertissements détectés : {len(warnings)}")
print("-" * 80)

if errors:
    print("ERRORS (DOIVENT ETRE CORRIGEES) :")
    for err in errors:
        print(f"  - {err}")

if warnings:
    print("AVERTISSEMENTS :")
    for warn in warnings:
        print(f"  - {warn}")

if not errors and not warnings:
    print("SUCCES TOTAL : 0 ERREUR | 0 AVERTISSEMENT !")
    print("Le site est 100% prêt pour la mise en production sur https://azizstudiodigital.netlify.app")

print("=" * 80)
