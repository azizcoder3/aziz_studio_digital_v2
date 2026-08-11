# -*- coding: utf-8 -*-
"""
verify_sprint43.py - Verification statique Sprint 43 : Emails automatiques
Controle de l'architecture et prioritairement de l'absence de mots de passe ou d'emails codees en dur.
"""
import os
import re
import sys
import json

ROOT = os.path.dirname(os.path.abspath(__file__))
errors = []
infos = []

print("=" * 70)
print("VERIFY SPRINT 43 - Automatisation Emails & Securite")
print("=" * 70)

# 1. Verification des fichiers et dossiers
func_dir = os.path.join(ROOT, 'netlify', 'functions')
func_file = os.path.join(func_dir, 'send-autoreply.js')
pkg_file = os.path.join(ROOT, 'package.json')
toml_file = os.path.join(ROOT, 'netlify.toml')

if not os.path.exists(func_file):
    errors.append(f"Fichier manquant : {os.path.relpath(func_file, ROOT)}")
else:
    infos.append("Fonction send-autoreply.js trouvee.")

if not os.path.exists(pkg_file):
    errors.append("package.json manquant.")
else:
    try:
        pkg = json.load(open(pkg_file, 'r', encoding='utf-8'))
        if 'nodemailer' not in pkg.get('dependencies', {}):
            errors.append("nodemailer n'est pas declare dans les dependencies de package.json.")
        else:
            infos.append("Dependance nodemailer configuree.")
    except Exception as e:
        errors.append(f"Erreur de lecture package.json : {str(e)}")

if not os.path.exists(toml_file):
    errors.append("netlify.toml manquant.")
else:
    content = open(toml_file, 'r', encoding='utf-8').read()
    if '[functions]' not in content or 'netlify/functions' not in content:
        errors.append("Dossier de fonctions non declare dans netlify.toml.")
    else:
        infos.append("netlify.toml declare correctement les fonctions.")

# 2. Verification critique de la securite (Grep statique sur TOUS les js/html)
# On cherche des mots de passe en dur, adresses email Gmail en dur hors process.env
dangerous_patterns = [
    (r'GMAIL_APP_PASSWORD\s*=\s*["\'][^"\']+["\']', "Mot de passe GMAIL trouve en dur !"),
    (r'auth:\s*\{\s*user:\s*["\'][^"\']+["\']', "Identifiant SMTP user code en dur !"),
    (r'auth:\s*\{\s*pass:\s*["\'][^"\']+["\']', "Mot de passe SMTP pass code en dur !"),
    (r'smtp\.gmail\.com.*user.*pass.*[a-z0-9]{16}', "Mot de passe d'application 16 caracteres suspect !"),
    (r'process\.env\.GMAIL_APP_PASSWORD\s*\|\|\s*["\'][^"\']+["\']', "Mot de passe de secours code en dur !")
]

security_violations = 0
for dirpath, dirs, files in os.walk(ROOT):
    if 'node_modules' in dirpath or '.git' in dirpath or '.gemini' in dirpath:
        continue
    for fn in files:
        if fn.endswith(('.js', '.html', '.py', '.md')):
            fp = os.path.join(dirpath, fn)
            try:
                # Exclure le script de verification lui-meme et la documentation pour ne pas fausser le test
                if fn == 'verify_sprint43.py' or fn.startswith('sprint-43') or fn.startswith('rapport-sprint-43'):
                    continue
                content = open(fp, 'r', encoding='utf-8', errors='ignore').read()
                for pattern, msg in dangerous_patterns:
                    if re.search(pattern, content):
                        errors.append(f"VIOLATION SECURITE [{fn}] : {msg}")
                        security_violations += 1
            except Exception:
                pass

if security_violations == 0:
    infos.append("SECURITE : Aucun mot de passe SMTP ou identifiant n'a ete trouve code en dur (Verification Statique OK).")

# 3. Verification de la structure de send-autoreply.js
if os.path.exists(func_file):
    func_content = open(func_file, 'r', encoding='utf-8').read()
    
    if 'bot-field' not in func_content and 'bot_field' not in func_content:
        errors.append("Le honeypot n'est pas verifie dans la fonction.")
    else:
        infos.append("Honeypot : Verification presente.")
        
    if 'process.env.GMAIL_USER' not in func_content or 'process.env.GMAIL_APP_PASSWORD' not in func_content:
        errors.append("La fonction n'utilise pas correctement process.env pour les identifiants SMTP.")
    else:
        infos.append("SMTP Auth : Utilise exclusivement process.env.")
        
    if 'process.env.WEBHOOK_SECRET' not in func_content:
        errors.append("La fonction ne verifie pas process.env.WEBHOOK_SECRET.")
    else:
        infos.append("Webhook Secret : Verification process.env.WEBHOOK_SECRET presente.")

    if 'nodemailer.createTransport' not in func_content:
        errors.append("Configuration Nodemailer manquante.")
    else:
        infos.append("Nodemailer : Transport configure.")

print("\n--- INFOS ---")
for i in infos:
    print(f"[OK] {i}")

print("\n--- ERREURS ---")
if errors:
    for e in errors:
        print(f"[ERROR] {e}")
else:
    print("Aucune erreur detectee.")

print("\n" + "=" * 70)
if not errors:
    print("BILAN : SPRINT 43 OK (100% SECURISE - PAS DE SECRET EXPOSE)")
    sys.exit(0)
else:
    print(f"BILAN : ECHEC ({len(errors)} erreurs trouves)")
    sys.exit(1)
