# -*- coding: utf-8 -*-
"""
Sprint 41 - Mise a jour des references d'images vers WebP.
Remplace dans tous les fichiers HTML et build_index.py les refs restantes :
  - hero-illustration.png -> hero-illustration.webp
  - portfolio-*.jpg -> portfolio-*.webp
  - agence-voyage.jpg -> agence-voyage.webp
  - ODN.png -> ODN.webp
  - og:image hero-illustration.png -> hero-illustration.webp
"""
import os
import re

ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'

# Liste des substitutions (old, new)
SUBSTITUTIONS = [
    ('assets/images/home/hero-illustration.png', 'assets/images/home/hero-illustration.webp'),
    ('assets/images/home/portfolio-boulevard-hotel.jpg', 'assets/images/home/portfolio-boulevard-hotel.webp'),
    ('assets/images/home/portfolio-atre-steakhouse.jpg', 'assets/images/home/portfolio-atre-steakhouse.webp'),
    ('assets/images/home/portfolio-cabinet-maxwell.jpg', 'assets/images/home/portfolio-cabinet-maxwell.webp'),
    ('assets/images/home/portfolio-dental-glow.jpg', 'assets/images/home/portfolio-dental-glow.webp'),
    ('assets/images/home/portfolio-molato-commerce.jpg', 'assets/images/home/portfolio-molato-commerce.webp'),
    ('assets/images/home/agence-voyage.jpg', 'assets/images/home/agence-voyage.webp'),
    ('assets/images/portfolio/ODN.png', 'assets/images/portfolio/ODN.webp'),
    # OG image absolue
    ('assets/images/home/hero-illustration.png', 'assets/images/home/hero-illustration.webp'),
]

# Fichiers cibles
html_files = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    # Exclure les dossiers non pertinents
    for skip in ['__pycache__', '.git', 'scratch', 'node_modules']:
        if skip in dirnames:
            dirnames.remove(skip)
    for fn in filenames:
        if fn.endswith('.html') or fn.endswith('.py'):
            html_files.append(os.path.join(dirpath, fn))

total_files_changed = 0
total_replacements = 0

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(filepath, 'r', encoding='cp1252') as f:
                content = f.read()
        except Exception as e:
            print(f"SKIP (erreur lecture) : {filepath} - {e}")
            continue

    original = content
    count = 0

    for old, new in SUBSTITUTIONS:
        if old in content:
            new_content = content.replace(old, new)
            count += new_content.count(new) - content.count(new)
            content = new_content

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        total_files_changed += 1
        print(f"  MODIFIE : {os.path.relpath(filepath, ROOT)}")

print(f"\n{total_files_changed} fichiers mis a jour.")
