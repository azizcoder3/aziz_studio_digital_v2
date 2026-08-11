"""
fix_domain_email.py — Harmonisation domaine + email + hébergeur
Aziz Studio Digital V2
- Ancien domaine : https://azizstudiodigital.cg  → https://azizstudiodigital.netlify.app
- Ancien domaine (UI badge) : devis.azizstudiodigital.cg → devis.azizstudiodigital.netlify.app
- Ancien email .cg : contact@azizstudiodigital.cg → azizstudio.dev@gmail.com
- Ancien email .com : contact@azizstudiodigital.com → azizstudio.dev@gmail.com
- Hébergeur mention : "hébergé par une infrastructure cloud sécurisée..." → "hébergé par Netlify, Inc."
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"c:\Users\Aziz\Desktop\aziz_studio_digital_v2"

OLD_DOMAIN   = "https://azizstudiodigital.cg"
NEW_DOMAIN   = "https://azizstudiodigital.netlify.app"

OLD_BADGE    = "devis.azizstudiodigital.cg"
NEW_BADGE    = "devis.azizstudiodigital.netlify.app"

OLD_EMAIL_CG  = "contact@azizstudiodigital.cg"
OLD_EMAIL_COM = "contact@azizstudiodigital.com"
NEW_EMAIL     = "azizstudio.dev@gmail.com"

OLD_HOSTING  = "hébergé par une infrastructure cloud sécurisée avec certificats SSL et protection contre les attaques DDoS"
NEW_HOSTING  = "hébergé par Netlify, Inc."

# ── Fichiers à traiter ───────────────────────────────────────────────────────
# Racine : HTML compilés, sitemap, robots, build_index.py
# Composants : footer (email dans le footer)
# Pages sources : pages/ (pour email dans pages/contact.html etc.)

TARGET_FILES = []

# Tous les .html compilés à la racine
for f in os.listdir(ROOT):
    if f.endswith(".html") and os.path.isfile(os.path.join(ROOT, f)):
        TARGET_FILES.append(os.path.join(ROOT, f))

# sitemap.xml et robots.txt
TARGET_FILES.append(os.path.join(ROOT, "sitemap.xml"))
TARGET_FILES.append(os.path.join(ROOT, "robots.txt"))

# build_index.py — source principale des canonical/OG et mentions légales template
TARGET_FILES.append(os.path.join(ROOT, "build_index.py"))

# Composant footer
TARGET_FILES.append(os.path.join(ROOT, "components", "footer.html"))

# Pages sources (pour les emails dans les pages sources)
pages_dir = os.path.join(ROOT, "pages")
for f in os.listdir(pages_dir):
    if f.endswith(".html"):
        TARGET_FILES.append(os.path.join(pages_dir, f))

changed_files = []
change_log = []

for filepath in TARGET_FILES:
    if not os.path.exists(filepath):
        continue

    with open(filepath, "r", encoding="utf-8", errors="replace") as fh:
        original = fh.read()

    content = original

    # 1. Domaine principal
    if OLD_DOMAIN in content:
        content = content.replace(OLD_DOMAIN, NEW_DOMAIN)

    # 2. Badge UI "devis.azizstudiodigital.cg"
    if OLD_BADGE in content:
        content = content.replace(OLD_BADGE, NEW_BADGE)

    # 3. Email .cg
    if OLD_EMAIL_CG in content:
        content = content.replace(OLD_EMAIL_CG, NEW_EMAIL)

    # 4. Email .com
    if OLD_EMAIL_COM in content:
        content = content.replace(OLD_EMAIL_COM, NEW_EMAIL)

    # 5. Formulation hébergeur (mentions légales et build_index.py)
    if OLD_HOSTING in content:
        content = content.replace(OLD_HOSTING, NEW_HOSTING)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write(content)

        rel = os.path.relpath(filepath, ROOT)
        changed_files.append(rel)

        # Compte les remplacements par type
        log_entries = []
        if OLD_DOMAIN in original:
            n = original.count(OLD_DOMAIN)
            log_entries.append(f"{n}x domaine .cg→netlify")
        if OLD_BADGE in original:
            n = original.count(OLD_BADGE)
            log_entries.append(f"{n}x badge devis .cg→netlify")
        if OLD_EMAIL_CG in original:
            n = original.count(OLD_EMAIL_CG)
            log_entries.append(f"{n}x email .cg→gmail")
        if OLD_EMAIL_COM in original:
            n = original.count(OLD_EMAIL_COM)
            log_entries.append(f"{n}x email .com→gmail")
        if OLD_HOSTING in original:
            n = original.count(OLD_HOSTING)
            log_entries.append(f"{n}x hébergeur mention")

        change_log.append((rel, log_entries))
        print(f"✅ {rel:<55} [{', '.join(log_entries)}]")

print(f"\n{'='*70}")
print(f"  {len(changed_files)} fichier(s) modifié(s) sur {len(TARGET_FILES)} scannés.")
print(f"{'='*70}")
