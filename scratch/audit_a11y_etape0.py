# -*- coding: utf-8 -*-
"""
Sprint 42 - Etape 0 : Audit accessibilite WCAG 2.1 AA
Scan automatique de toutes les pages HTML compilees a la racine.
Aucune modification n'est effectuee par ce script.
"""
import os
import re
import json
from html.parser import HTMLParser

ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'

# ─── Parser HTML leger ────────────────────────────────────────────────────────
class A11yParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = {
            'lang': None,
            'title': None,
            'h1': [],
            'headings': [],          # [(level, text)]
            'images': [],            # {'src','alt','role','aria-hidden'}
            'links': [],             # {'href','text','aria-label'}
            'buttons': [],           # {'type','text','aria-label','aria-expanded','aria-controls'}
            'inputs': [],            # {'id','name','type','aria-label','required'}
            'labels': [],            # {'for','text'}
            'nav_elements': [],      # {'aria-label','role'}
            'skip_links': [],        # hrefs commencant par #
            'aria_current': [],      # elements avec aria-current
            'aria_expanded': [],
            'aria_controls': [],
            'landmarks': [],         # role=main,banner,navigation,contentinfo,search,form
            'focus_styles': [],      # outline mentions
            'forms': [],
            'details_summary': [],   # FAQ accordeons
            'has_main': False,
            'has_header': False,
            'has_footer': False,
            'has_nav': False,
        }
        self._stack = []
        self._current_text = ''
        self._in_title = False
        self._in_skip = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self._stack.append(tag)

        if tag == 'html':
            self.data['lang'] = attrs.get('lang')

        elif tag == 'title':
            self._in_title = True

        elif tag in ('h1','h2','h3','h4','h5','h6'):
            self._stack_heading = (tag, '')

        elif tag == 'img':
            self.data['images'].append({
                'src': attrs.get('src',''),
                'alt': attrs.get('alt'),  # None = absent, '' = vide explicite
                'role': attrs.get('role'),
                'aria-hidden': attrs.get('aria-hidden'),
            })

        elif tag == 'a':
            href = attrs.get('href','')
            if href.startswith('#') and 'contenu' in href.lower():
                self.data['skip_links'].append(href)
            self.data['links'].append({
                'href': href,
                'text': '',
                'aria-label': attrs.get('aria-label'),
                'aria-current': attrs.get('aria-current'),
            })
            if attrs.get('aria-current'):
                self.data['aria_current'].append(attrs.get('aria-current'))

        elif tag == 'button':
            btn = {
                'type': attrs.get('type','button'),
                'text': '',
                'aria-label': attrs.get('aria-label'),
                'aria-expanded': attrs.get('aria-expanded'),
                'aria-controls': attrs.get('aria-controls'),
                'id': attrs.get('id'),
            }
            self.data['buttons'].append(btn)
            if attrs.get('aria-expanded') is not None:
                self.data['aria_expanded'].append(attrs.get('aria-expanded'))
            if attrs.get('aria-controls'):
                self.data['aria_controls'].append(attrs.get('aria-controls'))

        elif tag == 'input':
            self.data['inputs'].append({
                'id': attrs.get('id'),
                'name': attrs.get('name'),
                'type': attrs.get('type','text'),
                'aria-label': attrs.get('aria-label'),
                'required': 'required' in attrs or attrs.get('required') is not None,
                'autocomplete': attrs.get('autocomplete'),
            })

        elif tag == 'label':
            self.data['labels'].append({
                'for': attrs.get('for'),
                'text': '',
            })

        elif tag == 'form':
            self.data['forms'].append({'id': attrs.get('id'), 'action': attrs.get('action')})

        elif tag in ('nav',):
            self.data['has_nav'] = True
            self.data['nav_elements'].append({
                'aria-label': attrs.get('aria-label'),
                'role': attrs.get('role'),
            })

        elif tag == 'main':
            self.data['has_main'] = True

        elif tag == 'header':
            self.data['has_header'] = True

        elif tag == 'footer':
            self.data['has_footer'] = True

        elif tag == 'details':
            self.data['details_summary'].append({'open': 'open' in attrs})

        role = attrs.get('role')
        if role in ('main','banner','navigation','contentinfo','search','form','complementary'):
            self.data['landmarks'].append(role)

    def handle_data(self, data):
        if self._in_title:
            self.data['title'] = (self.data['title'] or '') + data

        tag = self._stack[-1] if self._stack else ''

        if tag in ('h1','h2','h3','h4','h5','h6'):
            level = int(tag[1])
            text = data.strip()
            if text:
                self.data['headings'].append((level, text[:80]))
                if tag == 'h1':
                    self.data['h1'].append(text[:80])

        if tag == 'a' and self.data['links']:
            self.data['links'][-1]['text'] += data.strip()

        if tag == 'button' and self.data['buttons']:
            self.data['buttons'][-1]['text'] += data.strip()

        if tag == 'label' and self.data['labels']:
            self.data['labels'][-1]['text'] += data.strip()

    def handle_endtag(self, tag):
        if self._stack and self._stack[-1] == tag:
            self._stack.pop()
        if tag == 'title':
            self._in_title = False


# ─── Collecte des pages HTML ──────────────────────────────────────────────────
def get_html_pages():
    pages = []
    for fn in sorted(os.listdir(ROOT)):
        if fn.endswith('.html'):
            pages.append(fn)
    return pages


# ─── Audit d'une page ─────────────────────────────────────────────────────────
def audit_page(filename):
    filepath = os.path.join(ROOT, filename)
    content = open(filepath, encoding='utf-8', errors='replace').read()

    parser = A11yParser()
    try:
        parser.feed(content)
    except Exception as e:
        pass

    d = parser.data
    issues = []

    # 1. Lang
    if not d['lang']:
        issues.append(('CRITIQUE', '3.1.1', 'Attribut lang manquant sur <html>', 'Ajouter lang="fr"'))
    elif d['lang'] != 'fr':
        issues.append(('MOYEN', '3.1.1', f'Lang = "{d["lang"]}" (attendu "fr")', 'Verifier la valeur'))

    # 2. Title
    if not d['title']:
        issues.append(('CRITIQUE', '2.4.2', 'Title manquant', 'Ajouter un <title> descriptif'))
    elif len(d['title'].strip()) < 5:
        issues.append(('MOYEN', '2.4.2', f'Title tres court : "{d["title"].strip()}"', 'Ameliorer le title'))

    # 3. H1
    if not d['h1']:
        issues.append(('CRITIQUE', '2.4.6', 'Aucun H1 present', 'Ajouter un H1 unique'))
    elif len(d['h1']) > 1:
        issues.append(('MOYEN', '2.4.6', f'{len(d["h1"])} H1 trouves', 'Conserver un seul H1'))

    # 4. Structure Hn (sauts de niveau)
    prev_level = 1
    heading_jump = False
    for level, text in d['headings']:
        if level > prev_level + 1:
            issues.append(('MOYEN', '1.3.1', f'Saut de titre : H{prev_level} -> H{level} ("{text[:40]}")', 'Corriger la hierarchie'))
            heading_jump = True
        prev_level = level

    # 5. Images sans alt
    imgs_sans_alt = [i for i in d['images'] if i['alt'] is None and i.get('aria-hidden') != 'true']
    if imgs_sans_alt:
        for img in imgs_sans_alt:
            issues.append(('CRITIQUE', '1.1.1', f'Image sans alt : {img["src"][-60:]}', 'Ajouter alt pertinent ou alt=""'))

    # 6. Images alt vide sur image potentiellement informative (heuristique sur src)
    informative_keywords = ['hero', 'portfolio', 'secteur', 'projet', 'apercu', 'mockup']
    for img in d['images']:
        if img['alt'] == '' and any(kw in img['src'].lower() for kw in informative_keywords):
            issues.append(('MOYEN', '1.1.1', f'Image possiblement informative avec alt="" : {img["src"][-60:]}', 'Verifier si alt pertinent requis'))

    # 7. Liens vides
    for lnk in d['links']:
        if not lnk['text'].strip() and not lnk.get('aria-label'):
            href = lnk.get('href','')
            if href and not href.startswith('javascript'):
                issues.append(('CRITIQUE', '2.4.4', f'Lien sans texte ni aria-label : href="{href[:60]}"', 'Ajouter texte ou aria-label'))

    # 8. Boutons vides
    for btn in d['buttons']:
        if not btn['text'].strip() and not btn.get('aria-label'):
            issues.append(('CRITIQUE', '4.1.2', f'Bouton sans texte ni aria-label (id={btn.get("id","-")})', 'Ajouter aria-label ou texte'))

    # 9. Landmarks
    if not d['has_main']:
        issues.append(('CRITIQUE', '1.3.1', 'Pas de <main> ou role="main"', 'Ajouter <main>'))
    if not d['has_header']:
        issues.append(('MOYEN', '1.3.1', 'Pas de <header>', 'Verifier la structure'))
    if not d['has_footer']:
        issues.append(('MOYEN', '1.3.1', 'Pas de <footer>', 'Verifier la structure'))
    if not d['has_nav']:
        issues.append(('INFO', '1.3.1', 'Pas de <nav>', 'Normal si page sans navigation'))

    # 10. Skip link
    has_skip = bool(d['skip_links']) or ('#contenu' in content or '#main' in content or 'skip' in content.lower()[:2000])
    if not has_skip:
        issues.append(('MOYEN', '2.4.1', 'Skip link absent ou non detecte', 'Ajouter lien "Aller au contenu"'))

    # 11. Labels / inputs
    input_ids = {i['id'] for i in d['inputs'] if i['id']}
    label_fors = {l['for'] for l in d['labels'] if l['for']}
    for inp in d['inputs']:
        if inp['type'] in ('hidden','submit','button','image'):
            continue
        if not inp.get('aria-label') and inp.get('id') not in label_fors:
            issues.append(('CRITIQUE', '3.3.2', f'Input sans label associe (id={inp.get("id","-")}, type={inp.get("type","-")})', 'Ajouter <label for=...> ou aria-label'))

    # 12. aria-current
    if filename not in ('index.html',) and not d['aria_current']:
        # Les pages compilees devraient avoir aria-current sur le lien actif
        issues.append(('MOYEN', '4.1.2', 'Aucun aria-current detecte dans la navigation', 'Verifier aria-current="page" sur le lien actif'))

    # 13. aria-expanded sur bouton hamburger
    hamburger_found = any('hamburger' in (btn.get('id','') or '') or 'menu' in (btn.get('id','') or '') or 'nav' in (btn.get('id','') or '') for btn in d['buttons'])
    nav_toggle = 'aria-expanded' in content
    if not nav_toggle:
        issues.append(('MOYEN', '4.1.2', 'aria-expanded non detecte (bouton menu mobile ?)', 'Verifier le bouton hamburger'))

    # 14. Focus visible (heuristique CSS)
    focus_in_css = ':focus' in content or 'outline' in content
    if not focus_in_css:
        issues.append(('MOYEN', '2.4.7', ':focus ou outline non detecte dans la page', 'Verifier CSS focus'))

    # 15. Formulaire contact.html specifique
    if filename == 'contact.html':
        autocomplete_fields = [i for i in d['inputs'] if i.get('autocomplete')]
        if not autocomplete_fields and d['inputs']:
            issues.append(('INFO', '1.3.5', 'Aucun champ input avec autocomplete detecte', 'Ajouter autocomplete sur champs pertinents'))

    # 16. Verifier presence de role="dialog" sans aria-labelledby
    if 'role="dialog"' in content and 'aria-labelledby' not in content:
        issues.append(('MOYEN', '4.1.2', 'role="dialog" sans aria-labelledby', 'Ajouter aria-labelledby'))

    # Resume statut
    critique = sum(1 for i in issues if i[0] == 'CRITIQUE')
    moyen = sum(1 for i in issues if i[0] == 'MOYEN')
    info = sum(1 for i in issues if i[0] == 'INFO')

    if critique > 0:
        statut = 'ANOMALIE'
    elif moyen > 0:
        statut = 'ATTENTION'
    else:
        statut = 'OK'

    return {
        'file': filename,
        'lang': d['lang'],
        'title': (d['title'] or '').strip()[:60],
        'h1_count': len(d['h1']),
        'h1_text': d['h1'][0][:50] if d['h1'] else '-',
        'images_count': len(d['images']),
        'images_sans_alt': len(imgs_sans_alt),
        'links_count': len(d['links']),
        'buttons_count': len(d['buttons']),
        'inputs_count': len(d['inputs']),
        'labels_count': len(d['labels']),
        'has_main': d['has_main'],
        'has_header': d['has_header'],
        'has_footer': d['has_footer'],
        'has_nav': d['has_nav'],
        'has_skip': has_skip,
        'aria_current': bool(d['aria_current']),
        'aria_expanded': bool(d['aria_expanded']),
        'details_faq': len(d['details_summary']),
        'issues': issues,
        'critique': critique,
        'moyen': moyen,
        'info': info,
        'statut': statut,
    }


# ─── Main ─────────────────────────────────────────────────────────────────────
pages = get_html_pages()
print(f"Pages HTML compilees trouvees : {len(pages)}")
print("=" * 80)

results = []
for page in pages:
    r = audit_page(page)
    results.append(r)

# Tableau recapitulatif
print("\n=== TABLEAU RECAPITULATIF ===\n")
header_row = f"{'Page':<35} {'Lang':<5} {'H1':>3} {'ImgSansAlt':>10} {'Main':>5} {'Skip':>5} {'AriaCur':>8} {'AriaExp':>8} {'FAQ':>4} {'Critique':>9} {'Moyen':>6} {'Statut':<10}"
print(header_row)
print("-" * len(header_row))

for r in results:
    print(f"{r['file']:<35} {str(r['lang']):<5} {r['h1_count']:>3} {r['images_sans_alt']:>10} {str(r['has_main']):>5} {str(r['has_skip']):>5} {str(r['aria_current']):>8} {str(r['aria_expanded']):>8} {r['details_faq']:>4} {r['critique']:>9} {r['moyen']:>6} {r['statut']:<10}")

# Anomalies detaillees
print("\n\n=== ANOMALIES DETAILLEES ===\n")
all_issues = []
for r in results:
    for issue in r['issues']:
        all_issues.append((r['file'], issue[0], issue[1], issue[2], issue[3]))

critiques = [(f,g,w,p,c) for f,g,w,p,c in all_issues if g == 'CRITIQUE']
moyens = [(f,g,w,p,c) for f,g,w,p,c in all_issues if g == 'MOYEN']
infos = [(f,g,w,p,c) for f,g,w,p,c in all_issues if g == 'INFO']

print(f"TOTAL : {len(critiques)} critiques / {len(moyens)} moyens / {len(infos)} infos")
print()

print("--- CRITIQUES ---")
for f,g,w,p,c in critiques:
    print(f"  [{f}] WCAG {w} : {p}")
    print(f"    Correction : {c}")

print()
print("--- MOYENS ---")
for f,g,w,p,c in moyens:
    print(f"  [{f}] WCAG {w} : {p}")
    print(f"    Correction : {c}")

print()
print("--- INFOS ---")
for f,g,w,p,c in infos:
    print(f"  [{f}] WCAG {w} : {p}")
    print(f"    Correction : {c}")

# Stats globales
total_critique = sum(r['critique'] for r in results)
total_moyen = sum(r['moyen'] for r in results)
total_ok = sum(1 for r in results if r['statut'] == 'OK')
total_anom = sum(1 for r in results if r['statut'] == 'ANOMALIE')
total_att = sum(1 for r in results if r['statut'] == 'ATTENTION')

print(f"\n=== STATS GLOBALES ===")
print(f"Pages OK        : {total_ok}")
print(f"Pages ATTENTION : {total_att}")
print(f"Pages ANOMALIE  : {total_anom}")
print(f"Critiques total : {total_critique}")
print(f"Moyens total    : {total_moyen}")

# Sauvegarder JSON
out = os.path.join(ROOT, 'scratch', 'audit_a11y_etape0.json')
with open(out, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"\nResultats JSON sauvegardes : {out}")
