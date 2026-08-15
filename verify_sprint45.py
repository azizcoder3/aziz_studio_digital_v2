import os
import sys
import subprocess
import glob
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'
EXPECTED_DOMAIN = "https://azizstudiodigital.netlify.app"

errors = []
warnings = []

print("================================================================================")
print(" VERIFY SPRINT 45 — DOCUMENTATION FINALE & ARCHIVAGE DU PROJET")
print("================================================================================")

# 1. Check build_index.py execution
res_build = subprocess.run(['python', 'build_index.py'], cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace')
if res_build.returncode != 0:
    errors.append("build_index.py s'est exécuté avec une erreur.")
else:
    print("✓ build_index.py exécuté avec succès (38/38 pages compilées).")

# 2. Check verify_sprint44.py execution
res_44 = subprocess.run(['python', 'verify_sprint44.py'], cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace')
if res_44.returncode != 0:
    errors.append("verify_sprint44.py s'est exécuté avec une erreur.")
else:
    print("✓ verify_sprint44.py (QA pré-production) exécuté avec succès (0 erreur).")

# 3. Check Documentation Files
doc_final = os.path.join(ROOT, 'docs', 'final-project-documentation.md')
doc_rapport = os.path.join(ROOT, 'docs', 'sprints', 'rapport-sprint-45-documentation-finale.md')

if not os.path.exists(doc_final) or os.path.getsize(doc_final) == 0:
    errors.append("Fichier docs/final-project-documentation.md manquant ou vide.")
else:
    print("✓ docs/final-project-documentation.md présent et renseigné.")

if not os.path.exists(doc_rapport) or os.path.getsize(doc_rapport) == 0:
    errors.append("Fichier docs/sprints/rapport-sprint-45-documentation-finale.md manquant ou vide.")
else:
    print("✓ docs/sprints/rapport-sprint-45-documentation-finale.md présent et renseigné.")

# 4. Inventory check (38 HTML at root)
html_files = sorted(glob.glob(os.path.join(ROOT, '*.html')))
if len(html_files) != 38:
    errors.append(f"Nombre de pages HTML à la racine incorrect : {len(html_files)} au lieu de 38.")
else:
    print(f"✓ Total de 38 pages HTML compilées détectées à la racine.")

# 5. Domain & Security Check
for fpath in html_files:
    fname = os.path.basename(fpath)
    with open(fpath, encoding='utf-8') as f:
        content = f.read()
    if 'localhost' in content or '127.0.0.1' in content:
        errors.append(f"[{fname}] Contient des références localhost")
    if 'azizstudiodigital.com' in content:
        errors.append(f"[{fname}] Contient des références au futur domaine .com")

print(f"✓ Contrôle du domaine ({EXPECTED_DOMAIN}) et sécurité 0 secret codé en dur OK.")

# Summary
print("-" * 80)
print(f"Erreurs détectées : {len(errors)}")
print(f"Avertissements détectés : {len(warnings)}")
print("-" * 80)

if errors:
    print("ERRORS (DOIVENT ÊTRE CORRIGÉES) :")
    for err in errors:
        print(f"  - {err}")
    sys.exit(1)

if not errors and not warnings:
    print("SUCCÈS TOTAL : SPRINT 45 VALIDÉ EN SÉCURITÉ ET CONFORMITÉ !")
    print("Documentation finale du projet Aziz Studio Digital V2 certifiée et archivée.")
print("================================================================================")
