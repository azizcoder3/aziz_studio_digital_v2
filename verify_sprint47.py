import os
import re
import sys

# Ensure UTF-8 stdout encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Use relative directory path (no hardcoded Windows absolute path)
ROOT = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(ROOT, 'index.html')

print("=================================================================")
print("   VERIFY SPRINT 47 — RECENTAGE SECTION SERVICES (HOME PAGE)   ")
print("=================================================================")

errors = []

if not os.path.exists(INDEX_PATH):
    print(f"[FAIL] {INDEX_PATH} introuvable.")
    sys.exit(1)

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# ─── CHECK 1 : Isolement de la section services ──────────────────────────────
print("\n[1/4] Extraction et vérification de la section services (#services)...")

services_match = re.search(r'<section\s+class="[^"]*section[^"]*"\s+id="services">(.*?)</section>', content, re.DOTALL)
if not services_match:
    errors.append("Section #services introuvable dans index.html")
    services_section = ""
else:
    services_section = services_match.group(1)
    print("  [OK] Section #services extraite avec succès.")

# ─── CHECK 2 : Nombre et ordre exact des 4 cartes ────────────────────────────
print("\n[2/4] Vérification des 4 cartes de services transversaux...")

if services_section:
    # Extraire les titres h3.card-title de la section services
    titles = re.findall(r'<h3\s+class="card-title">(.*?)</h3>', services_section)
    # Nettoyer HTML entities pour comparaison
    clean_titles = [t.replace('&amp;', '&').strip() for t in titles]

    expected_titles = [
        "Création de sites web",
        "SEO & Référencement",
        "Maintenance & Hébergement",
        "Audit & Optimisation"
    ]

    print(f"  Titres trouvés ({len(clean_titles)}) : {clean_titles}")

    if len(clean_titles) != 4:
        errors.append(f"La section services doit contenir exactement 4 cartes (trouvé {len(clean_titles)})")

    if clean_titles != expected_titles:
        errors.append(f"L'ordre ou l'intitulé des cartes est incorrect.\n    Attendu : {expected_titles}\n    Obtenu  : {clean_titles}")
    else:
        print("  [OK] Les 4 cartes attendues sont bien présentes dans l'ordre exact :")
        for idx, title in enumerate(clean_titles, 1):
            print(f"       {idx}. {title}")

# ─── CHECK 3 : Absence des cartes sectorielles dans #services ─────────────────
print("\n[3/4] Vérification de l'absence des offres sectorielles dans #services...")

forbidden_labels = [
    "Sites pour hôtels & restaurants",
    "Sites pour agences de voyage",
    "hôtels & restaurants",
    "agences de voyage",
    "Intégration IA"
]

if services_section:
    for forbidden in forbidden_labels:
        if forbidden.lower() in services_section.lower():
            errors.append(f"La section services contient encore l'élément interdit '{forbidden}'")
        else:
            print(f"  [OK] '{forbidden}' absent de la section services")

# ─── CHECK 4 : Non-altération du reste de la page (nav, secteurs, footer, etc.) ─
print("\n[4/4] Vérification de l'intégrité globale de index.html...")

# Vérifier la présence des autres sections clés
required_elements = [
    ('Navigation principale', r'<nav\s+class="primary-navigation"'),
    ('Section Hero', r'id="hero"'),
    ('Section Nos secteurs d\'activité', r'id="secteurs"'),
    ('Section Pourquoi nous', r'id="pourquoi-nous"'),
    ('Footer', r'<footer\s+class="site-footer"')
]

for label, pattern in required_elements:
    if not re.search(pattern, content):
        errors.append(f"Structure altérée : {label} non trouvé dans index.html")
    else:
        print(f"  [OK] {label} conservé")

# Vérification taille de fichier (> 130 KB, index.html fait typiquement ~145 KB)
file_size_kb = os.path.getsize(INDEX_PATH) / 1024
print(f"  Taille de index.html : {file_size_kb:.1f} KB")

if file_size_kb < 130.0 or file_size_kb > 165.0:
    errors.append(f"Taille suspecte de index.html ({file_size_kb:.1f} KB) - régression possible")
else:
    print("  [OK] Taille de fichier conforme")

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
    print("\n[OK] VÉRIFICATION RÉUSSIE — SPRINT 47 VALIDÉ !")
    sys.exit(0)
