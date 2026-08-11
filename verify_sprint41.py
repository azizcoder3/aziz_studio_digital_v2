# -*- coding: utf-8 -*-
"""
verify_sprint41.py - Verification Sprint 41 : Conversion WebP globale
Verifie l'etat reel du disque :
  - presence de tous les .webp attendus
  - absence de references .png/.jpg d'images raster dans les HTML
  - coherence build_index.py (og:image par defaut)
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
errors = []
warnings = []

print("=" * 60)
print("VERIFY SPRINT 41 - Conversion WebP globale")
print("=" * 60)

# ------------------------------------------------------------------
# 1. Fichiers WebP attendus sur disque
# ------------------------------------------------------------------
EXPECTED_WEBP = [
    os.path.join('assets', 'images', 'home', 'hero-illustration.webp'),
    os.path.join('assets', 'images', 'home', 'portfolio-boulevard-hotel.webp'),
    os.path.join('assets', 'images', 'home', 'portfolio-atre-steakhouse.webp'),
    os.path.join('assets', 'images', 'home', 'portfolio-cabinet-maxwell.webp'),
    os.path.join('assets', 'images', 'home', 'portfolio-dental-glow.webp'),
    os.path.join('assets', 'images', 'home', 'portfolio-molato-commerce.webp'),
    os.path.join('assets', 'images', 'home', 'agence-voyage.webp'),
    os.path.join('assets', 'images', 'portfolio', 'ODN.webp'),
    # secteurs (deja presents avant sprint 41)
    os.path.join('assets', 'images', 'secteurs', 'cabinet-dentaire.webp'),
    os.path.join('assets', 'images', 'secteurs', 'cabinet-medical.webp'),
    os.path.join('assets', 'images', 'secteurs', 'clinique.webp'),
    os.path.join('assets', 'images', 'secteurs', 'hotel.webp'),
    os.path.join('assets', 'images', 'secteurs', 'immobilier.webp'),
    os.path.join('assets', 'images', 'secteurs', 'pharmacie.webp'),
    os.path.join('assets', 'images', 'secteurs', 'restaurant.webp'),
    os.path.join('assets', 'images', 'secteurs', 'salon-beaute.webp'),
    os.path.join('assets', 'images', 'secteurs', 'voyage.webp'),
    # portfolio (deja presents avant sprint 41)
    os.path.join('assets', 'images', 'portfolio', 'atre-steakhouse.webp'),
    os.path.join('assets', 'images', 'portfolio', 'boulevard-hotel.webp'),
    os.path.join('assets', 'images', 'portfolio', 'cabinet-avocat-maxWell.webp'),
    os.path.join('assets', 'images', 'portfolio', 'dantal-glow-landingPage.webp'),
    os.path.join('assets', 'images', 'portfolio', 'designFlow-template.webp'),
    os.path.join('assets', 'images', 'portfolio', 'molato-ecommerce.webp'),
]

print("\n[1] Fichiers WebP sur disque")
all_ok = True
for rel in EXPECTED_WEBP:
    full = os.path.join(ROOT, rel)
    if os.path.exists(full):
        size = os.path.getsize(full)
        print(f"  OK  {rel} ({size:,} o)")
    else:
        print(f"  MANQUANT  {rel}")
        errors.append(f"Fichier WebP manquant : {rel}")
        all_ok = False

# ------------------------------------------------------------------
# 2. References raster residuelles dans les HTML
# ------------------------------------------------------------------
print("\n[2] References .png/.jpg d'images raster dans les HTML")
raster_refs_found = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    for skip in ['__pycache__', 'scratch', '.git']:
        if skip in dirnames:
            dirnames.remove(skip)
    for fn in filenames:
        if not fn.endswith('.html'):
            continue
        fp = os.path.join(dirpath, fn)
        try:
            content = open(fp, encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        for i, line in enumerate(content.splitlines(), 1):
            # Ignorer favicon SVG, og:image absolue webp, etc.
            if 'assets/images' not in line:
                continue
            if 'favicon' in line:
                continue
            if '.png' in line or '.jpg' in line or '.jpeg' in line:
                raster_refs_found.append((os.path.relpath(fp, ROOT), i, line.strip()[:120]))

if raster_refs_found:
    for f, ln, l in raster_refs_found:
        print(f"  WARN  {f}:{ln}  {l}")
        warnings.append(f"Ref raster residuelle dans {f}:{ln}")
else:
    print("  OK  Aucune reference raster residuelle.")

# ------------------------------------------------------------------
# 3. build_index.py : og:image par defaut
# ------------------------------------------------------------------
print("\n[3] build_index.py - og:image par defaut")
build_py = os.path.join(ROOT, 'build_index.py')
if os.path.exists(build_py):
    content = open(build_py, encoding='utf-8', errors='replace').read()
    if 'hero-illustration.png' in content:
        print("  WARN  build_index.py contient encore hero-illustration.png")
        warnings.append("build_index.py : og:image par defaut non mise a jour")
    elif 'hero-illustration.webp' in content:
        print("  OK  build_index.py utilise hero-illustration.webp")
    else:
        print("  INFO  build_index.py : aucune reference hero-illustration trouvee")
else:
    print("  INFO  build_index.py introuvable")

# ------------------------------------------------------------------
# Bilan
# ------------------------------------------------------------------
print("\n" + "=" * 60)
print("BILAN")
print(f"  Erreurs   : {len(errors)}")
print(f"  Avertiss. : {len(warnings)}")
if errors:
    print("\nERREURS :")
    for e in errors:
        print(f"  - {e}")
if warnings:
    print("\nAVERTISSEMENTS :")
    for w in warnings:
        print(f"  - {w}")
if not errors and not warnings:
    print("\n  SPRINT 41 : TOUTES LES VERIFICATIONS PASSENT.")
print("=" * 60)

sys.exit(1 if errors else 0)
