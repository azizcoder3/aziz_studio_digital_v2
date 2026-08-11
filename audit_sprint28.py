import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'

pages_info = [
    {
        'file': 'creation-site-web.html',
        'name': 'Création de site web',
        'page_css': 'creation-site-web.css',
        'devis_cta': 'Demander un devis Création Web', # Or Demander un devis site web / Demander un devis gratuit ? Let's check rule
    },
    {
        'file': 'wordpress.html',
        'name': 'Développement WordPress',
        'page_css': 'wordpress.css',
        'devis_cta': 'Demander un devis WordPress',
    },
    {
        'file': 'seo.html',
        'name': 'SEO & Référencement',
        'page_css': 'seo.css',
        'audit_cta': 'Demander un audit SEO gratuit',
    },
    {
        'file': 'refonte-site.html',
        'name': 'Refonte de site web',
        'page_css': 'refonte-site.css',
        'devis_cta': 'Demander un devis Refonte',
    },
    {
        'file': 'maintenance.html',
        'name': 'Maintenance & Support',
        'page_css': 'maintenance.css',
        'devis_cta': 'Demander un devis Maintenance',
    },
    {
        'file': 'audit-conseil.html',
        'name': 'Audit & Conseil Digital',
        'page_css': 'audit-conseil.css',
        'audit_cta': 'Demander un audit digital gratuit',
    }
]

print("==================================================")
print("       SPRINT 28 — COMPREHENSIVE AUDIT SCRIPT")
print("==================================================\n")

# 1. Check build_index.py definitions & root html files
build_file = os.path.join(ROOT, 'build_index.py')
build_content = open(build_file, encoding='utf-8').read()

print("--- 1. SEO AUDIT (Titles & Meta Descriptions in build_index.py & compiled pages) ---")
titles = {}
metas = {}

for p in pages_info:
    filename = p['file']
    root_path = os.path.join(ROOT, filename)
    content = open(root_path, encoding='utf-8').read()
    
    # Title
    t_match = re.search(r'<title>(.*?)</title>', content)
    title = t_match.group(1) if t_match else "MISSING"
    t_len = len(title)
    t_pipes = title.count('|')
    
    # Meta desc
    m_match = re.search(r'<meta name="description" content="(.*?)"', content)
    meta = m_match.group(1) if m_match else "MISSING"
    m_len = len(meta)
    
    titles[filename] = title
    metas[filename] = meta
    
    print(f"[{filename}]")
    print(f"  Title ({t_len} chars, {t_pipes} pipe): \"{title}\"")
    print(f"    - Unique: {'PENDING'}")
    print(f"    - Length <= 60: {'YES' if t_len <= 60 else 'NO (' + str(t_len) + ')'}")
    print(f"    - Single pipe: {'YES' if t_pipes == 1 else 'NO (' + str(t_pipes) + ')'}")
    print(f"  Meta Description ({m_len} chars): \"{meta}\"")
    print(f"    - Length <= 160: {'YES' if m_len <= 160 else 'NO (' + str(m_len) + ')'}")
    print()

# Check uniqueness
unique_titles = len(set(titles.values())) == len(titles)
unique_metas = len(set(metas.values())) == len(metas)
print(f"All Titles Unique: {'YES' if unique_titles else 'NO'}")
print(f"All Metas Unique: {'YES' if unique_metas else 'NO'}\n")

print("--- 2. HEADINGS & HIERARCHY AUDIT ---")
for p in pages_info:
    filename = p['file']
    content = open(os.path.join(ROOT, filename), encoding='utf-8').read()
    h1s = re.findall(r'<h1.*?>(.*?)</h1>', content, re.DOTALL)
    h2s = re.findall(r'<h2.*?>(.*?)</h2>', content, re.DOTALL)
    h3s = re.findall(r'<h3.*?>(.*?)</h3>', content, re.DOTALL)
    h4s = re.findall(r'<h4.*?>(.*?)</h4>', content, re.DOTALL)
    
    print(f"[{filename}] H1 count: {len(h1s)} | H2 count: {len(h2s)} | H3 count: {len(h3s)} | H4 count: {len(h4s)}")
    if len(h1s) != 1:
        print(f"  ⚠️  WARNING: H1 count is {len(h1s)}")
print()

print("--- 3. CTA WORDING AUDIT ---")
# Official CTA rules:
# Devis: "Demander un devis [Service]"
# Audit: "Demander un audit [Service] gratuit"
# Contact: "Parler de votre projet"
# Portfolio: "Voir nos réalisations"

for p in pages_info:
    filename = p['file']
    content = open(os.path.join(ROOT, filename), encoding='utf-8').read()
    print(f"[{filename}] CTA Links & Buttons:")
    # Find all <a> and <button> tags with class btn or cta
    ctas = re.findall(r'<(?:a|button)[^>]*class="[^"]*btn[^"]*"[^>]*>(.*?)</(?:a|button)>', content, re.DOTALL)
    for cta in ctas:
        clean_text = re.sub(r'<[^>]+>', '', cta).strip()
        print(f"   -> \"{clean_text}\"")
print()

print("--- 4. BREADCRUMBS & ACCESSIBILITY AUDIT ---")
for p in pages_info:
    filename = p['file']
    content = open(os.path.join(ROOT, filename), encoding='utf-8').read()
    has_crumb = 'aria-label="Fil d\'Ariane"' in content or 'class="breadcrumb"' in content
    has_aria_current = 'aria-current="page"' in content
    print(f"[{filename}] Breadcrumb present: {has_crumb} | aria-current=\"page\" on last item: {has_aria_current}")
print()

print("--- 5. CSS LINKS AUDIT ---")
for p in pages_info:
    filename = p['file']
    content = open(os.path.join(ROOT, filename), encoding='utf-8').read()
    stylesheets = re.findall(r'<link rel="stylesheet" href="(.*?)">', content)
    page_sheets = [s for s in stylesheets if 'pages/' in s]
    print(f"[{filename}] Page stylesheets: {page_sheets}")
print()

print("--- 6. HERO DASHBOARD & COMPONENTS REUSE AUDIT ---")
for p in pages_info:
    filename = p['file']
    content = open(os.path.join(ROOT, filename), encoding='utf-8').read()
    has_hero_dash = 'hero-dashboard' in content
    has_sparkline = 'dash-card' in content
    has_timeline = 'processus-timeline' in content or 'timeline-step' in content
    has_faq = 'faq-accordion' in content or 'faq-item' in content
    has_cta_final = 'service-cta-final-card' in content or 'service-final-cta-section' in content
    
    print(f"[{filename}] Hero Dashboard: {has_hero_dash} | Timeline: {has_timeline} | FAQ: {has_faq} | CTA Final: {has_cta_final}")

print("\nAUDIT SCRIPT COMPLETED.")
