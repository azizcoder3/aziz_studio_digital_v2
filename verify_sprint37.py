#!/usr/bin/env python3
"""
verify_sprint37.py — Checklist de conformité automatique pour le Sprint 37 (Blog)
Aziz Studio Digital V2

Usage : python verify_sprint37.py
"""

import os
import re
import sys

ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'

PASS  = '  [PASS]'
FAIL  = '  [FAIL]'
WARN  = '  [WARN]'

errors   = 0
warnings = 0

def ok(msg):
    print(f'{PASS} — {msg}')

def fail(msg):
    global errors
    errors += 1
    print(f'{FAIL} — {msg}')

def warn(msg):
    global warnings
    warnings += 1
    print(f'{WARN} — {msg}')


# ──────────────────────────────────────────────────────────────────────────────
# FICHIERS CIBLES
# ──────────────────────────────────────────────────────────────────────────────
FILES = {
    'blog.html':              os.path.join(ROOT, 'blog.html'),
    'blog-article-seo.html':  os.path.join(ROOT, 'blog-article-seo.html'),
    'blog.css':               os.path.join(ROOT, 'assets', 'css', 'pages', 'blog.css'),
    'blog-article.css':       os.path.join(ROOT, 'assets', 'css', 'pages', 'blog-article.css'),
}

print('\n' + '='*60)
print('  SPRINT 37 -- VERIFICATION AUTOMATIQUE')
print('='*60)


# ──────────────────────────────────────────────────────────────────────────────
# 1. Présence des fichiers
# ──────────────────────────────────────────────────────────────────────────────
print('\n[1] Présence des fichiers\n')
contents = {}
for name, path in FILES.items():
    if os.path.exists(path) and os.path.getsize(path) > 0:
        ok(f'{name} existe et non vide')
        with open(path, encoding='utf-8') as fh:
            contents[name] = fh.read()
    else:
        fail(f'{name} manquant ou vide à {path}')
        contents[name] = ''


# ──────────────────────────────────────────────────────────────────────────────
# 2. SEO : <title> et <meta description> uniques
# ──────────────────────────────────────────────────────────────────────────────
print('\n[2] SEO : <title> et <meta description>\n')

for html_file in ('blog.html', 'blog-article-seo.html'):
    html = contents.get(html_file, '')
    titles = re.findall(r'<title>(.*?)</title>', html, re.DOTALL)
    descs  = re.findall(r'<meta name="description" content="([^"]+)"', html)

    if len(titles) == 1 and titles[0].strip():
        ok(f'{html_file} — <title> unique et non vide : "{titles[0].strip()[:60]}..."')
    else:
        fail(f'{html_file} — <title> manquant ou multiple (trouvé : {len(titles)})')

    if len(descs) == 1 and 30 <= len(descs[0]) <= 160:
        ok(f'{html_file} — <meta description> valide ({len(descs[0])} caractères)')
    elif len(descs) == 1:
        warn(f'{html_file} — <meta description> hors plage recommandée ({len(descs[0])} caractères)')
    else:
        fail(f'{html_file} — <meta description> manquante ou multiple (trouvé : {len(descs)})')


# ──────────────────────────────────────────────────────────────────────────────
# 3. Un seul <h1> par page
# ──────────────────────────────────────────────────────────────────────────────
print('\n[3] Hiérarchie sémantique : <h1>\n')

for html_file in ('blog.html', 'blog-article-seo.html'):
    html = contents.get(html_file, '')
    h1s  = re.findall(r'<h1[\s>]', html, re.IGNORECASE)
    if len(h1s) == 1:
        ok(f'{html_file} — exactement 1 <h1>')
    else:
        fail(f'{html_file} — {len(h1s)} balises <h1> trouvées (attendu : 1)')


# ──────────────────────────────────────────────────────────────────────────────
# 4. Absence d'@import dans les fichiers CSS
# ──────────────────────────────────────────────────────────────────────────────
print('\n[4] Absence d\'@import CSS\n')

for css_file in ('blog.css', 'blog-article.css'):
    css = contents.get(css_file, '')
    if '@import' in css:
        fail(f'{css_file} — @import détecté (interdit par les règles du projet)')
    else:
        ok(f'{css_file} — aucun @import')


# ──────────────────────────────────────────────────────────────────────────────
# 5. Ordre des CSS dans les pages compilées
# ──────────────────────────────────────────────────────────────────────────────
print('\n[5] Ordre CSS (services.css → creation-site-web.css → blog.css)\n')

EXPECTED_ORDER_BLOG = [
    'assets/css/pages/services.css',
    'assets/css/pages/creation-site-web.css',
    'assets/css/pages/blog.css',
]
EXPECTED_ORDER_ARTICLE = EXPECTED_ORDER_BLOG + ['assets/css/pages/blog-article.css']

def check_css_order(html, expected, label):
    positions = []
    for css in expected:
        idx = html.find(css)
        if idx == -1:
            fail(f'{label} — CSS manquant : {css}')
            return
        positions.append(idx)
    if positions == sorted(positions):
        ok(f'{label} — ordre CSS correct')
    else:
        fail(f'{label} — ordre CSS incorrect (attendu : {" → ".join(os.path.basename(c) for c in expected)})')

check_css_order(contents.get('blog.html', ''),              EXPECTED_ORDER_BLOG,    'blog.html')
check_css_order(contents.get('blog-article-seo.html', ''), EXPECTED_ORDER_ARTICLE, 'blog-article-seo.html')


# ──────────────────────────────────────────────────────────────────────────────
# 6. Composants Premium réutilisés
# ──────────────────────────────────────────────────────────────────────────────
print('\n[6] Composants Premium\n')

BLOG_COMPONENTS = {
    'Hero Dashboard (.hero-dashboard)':    'hero-dashboard',
    'Breadcrumb (.breadcrumb)':            'class="breadcrumb"',
    'Blog Cards (.blog-card)':             'class="blog-card"',
    'FAQ Premium (.faq-item card)':        'class="faq-item card"',
    'Badge (.badge)':                      'class="badge',
    'Section Header (.section-header)':    'class="section-header',
}

ARTICLE_COMPONENTS = {
    'Breadcrumb (.breadcrumb)':            'class="breadcrumb"',
    'Schema.org Article':                  'itemtype="https://schema.org/Article"',
    'FAQ Accordion (.faq-item)':           'class="faq-item',
    'Blog CSS article body':               'article-body',
    'Table of Contents (.article-toc)':    'article-toc',
}

blog_html         = contents.get('blog.html', '')
blog_article_html = contents.get('blog-article-seo.html', '')

for name, token in BLOG_COMPONENTS.items():
    if token in blog_html:
        ok(f'blog.html — {name}')
    else:
        fail(f'blog.html — Composant manquant : {name} ({token})')

for name, token in ARTICLE_COMPONENTS.items():
    if token in blog_article_html:
        ok(f'blog-article-seo.html — {name}')
    else:
        fail(f'blog-article-seo.html — Composant manquant : {name} ({token})')


# ──────────────────────────────────────────────────────────────────────────────
# 7. Contenu réel : 3 articles, auteur unique = Aziz
# ──────────────────────────────────────────────────────────────────────────────
print('\n[7] Contenu réel des articles\n')

REQUIRED_ARTICLES = [
    'SEO au Congo',
    'WordPress',
    'développement web',
]

for article_kw in REQUIRED_ARTICLES:
    if article_kw.lower() in blog_html.lower():
        ok(f'blog.html — Référence article trouvée : "{article_kw}"')
    else:
        fail(f'blog.html — Référence article manquante : "{article_kw}"')

# Vérifier l'auteur dans le template
if '>Aziz<' in blog_article_html or 'itemprop="name">Aziz' in blog_article_html:
    ok('blog-article-seo.html — Auteur réel "Aziz" identifié')
else:
    fail('blog-article-seo.html — Auteur "Aziz" non identifié (faux auteur interdit)')

# Vérifier l'absence de faux chiffres/témoignages inventés
FORBIDDEN_PATTERNS = ['lorem ipsum', 'john doe', 'jane doe', '999 clients', '+500 projets']
for html_file, html in [('blog.html', blog_html), ('blog-article-seo.html', blog_article_html)]:
    found_forbidden = [p for p in FORBIDDEN_PATTERNS if p.lower() in html.lower()]
    if found_forbidden:
        fail(f'{html_file} — Contenu fictif interdit trouvé : {found_forbidden}')
    else:
        ok(f'{html_file} — Aucun contenu fictif interdit')


# ──────────────────────────────────────────────────────────────────────────────
# 8. Variables CSS exclusives (aucune couleur en dur)
# ──────────────────────────────────────────────────────────────────────────────
print('\n[8] Couleurs CSS — Variables exclusives\n')

# Regex pour détecter les couleurs en dur (hsl/rgb/hex) hors contexte de variable
HARDCODED_COLOR = re.compile(
    r'(?<!var\()(?<!:)\s*(#[0-9a-fA-F]{3,8}|rgb\(|rgba\()\s*(?!.*--)',
    re.MULTILINE
)

for css_file in ('blog.css', 'blog-article.css'):
    css = contents.get(css_file, '')
    matches = HARDCODED_COLOR.findall(css)
    # Filtre les faux positifs (ex. hsl dans var definitions ou hsl() avec var())
    real_matches = [m.strip() for m in matches if not m.strip().startswith('--')]
    if real_matches:
        warn(f'{css_file} — Couleurs potentiellement en dur détectées : {real_matches[:5]}')
    else:
        ok(f'{css_file} — Toutes les couleurs utilisent des variables CSS')


# ──────────────────────────────────────────────────────────────────────────────
# 9. build_index.py contient les deux nouveaux blocs
# ──────────────────────────────────────────────────────────────────────────────
print('\n[9] build_index.py — Nouveaux blocs\n')

build_path = os.path.join(ROOT, 'build_index.py')
if os.path.exists(build_path):
    with open(build_path, encoding='utf-8') as fh:
        build_content = fh.read()

    for label, token in [
        ('blog.html compilation', 'blog.html'),
        ('blog-article-seo.html compilation', 'blog-article-seo.html'),
        ('blog.css linktag', 'pages/blog.css'),
        ('blog-article.css linktag', 'pages/blog-article.css'),
    ]:
        if token in build_content:
            ok(f'build_index.py — {label}')
        else:
            fail(f'build_index.py — {label} manquant (token: "{token}")')
else:
    fail('build_index.py introuvable')


# ──────────────────────────────────────────────────────────────────────────────
# RESUME FINAL
# ──────────────────────────────────────────────────────────────────────────────
print('\n' + '='*60)
print(f'  RESULTAT FINAL : {errors} erreur(s), {warnings} avertissement(s)')
print('='*60)

if errors == 0 and warnings == 0:
    print('\n  Sprint 37 - Conformite totale. Tous les criteres sont valides.\n')
elif errors == 0:
    print('\n  [OK] Sprint 37 - Conformite atteinte (avec avertissements mineurs).\n')
else:
    print('\n  [FAIL] Sprint 37 - Des erreurs doivent etre corrigees avant de clore le sprint.\n')

sys.exit(0 if errors == 0 else 1)
