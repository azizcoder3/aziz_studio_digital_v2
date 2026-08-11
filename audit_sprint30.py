import os, sys, re, glob
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding='utf-8')
ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'

html_files = sorted([f for f in os.listdir(ROOT) if f.endswith('.html')])

print(f"=== SPRINT 30 GLOBAL QUALITY AUDIT ===")
print(f"Total HTML files found in root: {len(html_files)}\n")

# 1. SEO & Headings Audit
print("--- 1. SEO & HEADING HIERARCHY AUDIT ---")
titles = {}
metas = {}
seo_results = []

for page in html_files:
    filepath = os.path.join(ROOT, page)
    content = open(filepath, encoding='utf-8').read()
    
    # Title
    t_matches = re.findall(r'<title>(.*?)</title>', content, re.DOTALL | re.IGNORECASE)
    t_count = len(t_matches)
    t_text = t_matches[0].strip() if t_count > 0 else ""
    t_len = len(t_text)
    
    # Meta description
    m_matches = re.findall(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.DOTALL | re.IGNORECASE)
    if not m_matches:
        m_matches = re.findall(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']', content, re.DOTALL | re.IGNORECASE)
    m_count = len(m_matches)
    m_text = m_matches[0].strip() if m_count > 0 else ""
    m_len = len(m_text)
    
    # H1 count
    h1_matches = re.findall(r'<h1[\s>](.*?)</h1>', content, re.DOTALL | re.IGNORECASE)
    h1_count = len(h1_matches)
    
    # Headings hierarchy
    headings = re.findall(r'<h([1-6])[\s>](.*?)</h\1>', content, re.DOTALL | re.IGNORECASE)
    hierarchy_errors = []
    prev_level = 0
    for level_str, h_content in headings:
        level = int(level_str)
        if prev_level > 0 and level > prev_level + 1:
            hierarchy_errors.append(f"Jump H{prev_level} -> H{level}")
        prev_level = level
        
    seo_results.append({
        'page': page,
        't_count': t_count,
        'title': t_text,
        't_len': t_len,
        'm_count': m_count,
        'meta': m_text,
        'm_len': m_len,
        'h1_count': h1_count,
        'hierarchy_ok': len(hierarchy_errors) == 0,
        'hierarchy_errors': hierarchy_errors
    })
    
    if t_text:
        titles.setdefault(t_text, []).append(page)
    if m_text:
        metas.setdefault(m_text, []).append(page)

# Print SEO Table
print(f"{'Page':<28} | {'Title Chars':<11} | {'Meta Chars':<10} | {'H1 Count':<8} | {'Hierarchy'}")
print("-" * 75)
for res in seo_results:
    h_status = "OK" if res['hierarchy_ok'] else f"ERR ({', '.join(res['hierarchy_errors'])})"
    print(f"{res['page']:<28} | {res['t_len']:<11} | {res['m_len']:<10} | {res['h1_count']:<8} | {h_status}")

print("\n--- UNICITY CHECKS ---")
dup_titles = {k: v for k, v in titles.items() if len(v) > 1}
dup_metas = {k: v for k, v in metas.items() if len(v) > 1}

if dup_titles:
    print(f"DUPLICATE TITLES FOUND ({len(dup_titles)}):")
    for t, pages in dup_titles.items():
        print(f"  - '{t}': {pages}")
else:
    print("✓ All page titles are unique.")

if dup_metas:
    print(f"DUPLICATE META DESCRIPTIONS FOUND ({len(dup_metas)}):")
    for m, pages in dup_metas.items():
        print(f"  - '{m}': {pages}")
else:
    print("✓ All meta descriptions are unique.")


# 2. CSS AUDIT
print("\n--- 2. CSS AUDIT ---")
css_files = glob.glob(os.path.join(ROOT, 'assets', 'css', '**', '*.css'), recursive=True)
imports_found = []

for css_f in css_files:
    rel_p = os.path.relpath(css_f, ROOT)
    txt = open(css_f, encoding='utf-8').read()
    if '@import' in txt:
        imports_found.append(rel_p)

if imports_found:
    print(f"❌ @import found in: {imports_found}")
else:
    print("✓ 0 @import statements found in any CSS file.")

# Services pages CSS order check
services_pages = ['creation-site-web.html', 'wordpress.html', 'seo.html', 'refonte-site.html', 'maintenance.html', 'audit-conseil.html']
print("\nServices CSS order check:")
for sp in services_pages:
    content = open(os.path.join(ROOT, sp), encoding='utf-8').read()
    css_links = re.findall(r'href=["\'](assets/css/[^"\']+)["\']', content)
    
    # Filter page-level css
    page_css = [c for c in css_links if 'assets/css/pages/' in c]
    print(f"  - {sp}: {page_css}")


# 3. LINK CHECKER
print("\n--- 3. INTERNAL LINK AUDIT ---")
broken_links = []
all_hrefs = []

for page in html_files:
    content = open(os.path.join(ROOT, page), encoding='utf-8').read()
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
    
    for href in hrefs:
        all_hrefs.append((page, href))
        # Ignore external, mailto, tel, javascript, pure anchor
        if href.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', '#')):
            continue
            
        target = href.split('#')[0].split('?')[0]
        if target:
            target_path = os.path.join(ROOT, target)
            if not os.path.exists(target_path):
                broken_links.append((page, href, target_path))

if broken_links:
    print(f"❌ BROKEN LINKS DETECTED ({len(broken_links)}):")
    for src, href, path in broken_links:
        print(f"  - In {src}: href='{href}' -> file not found: {path}")
else:
    print("✓ 0 broken internal links detected across all HTML files.")


# 4. WCAG & ACCESSIBILITY QUICK CHECK
print("\n--- 4. WCAG ACCESSIBILITY QUICK AUDIT ---")
img_no_alt = []
for page in html_files:
    content = open(os.path.join(ROOT, page), encoding='utf-8').read()
    # Check <img> without alt
    imgs = re.findall(r'<img\s+[^>]*>', content, re.IGNORECASE)
    for img in imgs:
        if 'alt=' not in img.lower():
            img_no_alt.append((page, img))

if img_no_alt:
    print(f"❌ <img> missing alt attribute ({len(img_no_alt)}):")
    for page, img in img_no_alt:
        print(f"  - In {page}: {img}")
else:
    print("✓ 100% of <img> tags have an 'alt' attribute.")

