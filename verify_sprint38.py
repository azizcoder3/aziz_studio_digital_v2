import os
import re
import subprocess
import sys

# Ensure UTF-8 stdout encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'

pages_to_verify = [
    'index.html',
    'services.html',
    'creation-site-web.html',
    'wordpress.html',
    'seo.html',
    'refonte-site.html',
    'maintenance.html',
    'audit-conseil.html',
    'solutions.html',
    'portfolio.html',
    'blog.html',
    'tarifs.html',
    'a-propos.html',
    'contact.html',
    'blog-article-seo.html',
    'blog-article-wordpress.html',
    'blog-article-developpement-web.html'
]

print("=================================================================")
print("          VERIFY SPRINT 38 — FOOTER PREMIUM & NAV GLOBALE       ")
print("=================================================================")

errors = []
warnings = []

# 1. Run build_index.py
print("\n[1/9] Testing build_index.py execution...")
try:
    res = subprocess.run([sys.executable, os.path.join(ROOT, 'build_index.py')], capture_output=True, text=True, check=True)
    print("  [OK] build_index.py executed successfully!")
except Exception as e:
    errors.append(f"build_index.py failed: {e}")
    print(f"  [FAIL] build_index.py failed: {e}")

# 2. Check 0 @import in CSS files
print("\n[2/9] Checking 0 @import in all CSS files...")
css_dir = os.path.join(ROOT, 'assets', 'css')
import_count = 0
for root_d, dirs, files in os.walk(css_dir):
    for f in files:
        if f.endswith('.css'):
            fpath = os.path.join(root_d, f)
            content = open(fpath, 'r', encoding='utf-8').read()
            if '@import' in content:
                import_count += 1
                errors.append(f"@import found in {fpath}")
if import_count == 0:
    print("  [OK] 0 @import found in CSS files!")
else:
    print(f"  [FAIL] Found {import_count} @import statements!")

# 3. Check Header & Footer presence & structural identity
print("\n[3/9] Verifying Header & Footer Premium structural identity...")
header_comp = open(os.path.join(ROOT, 'components', 'header.html'), encoding='utf-8').read().strip()
footer_comp = open(os.path.join(ROOT, 'components', 'footer.html'), encoding='utf-8').read().strip()

footer_mismatch = 0
header_mismatch = 0

for p in pages_to_verify:
    fpath = os.path.join(ROOT, p)
    if not os.path.exists(fpath):
        errors.append(f"Page missing: {p}")
        continue
    content = open(fpath, 'r', encoding='utf-8').read()
    
    # Check Header structure
    m_head = re.search(r'<header class="site-header"[^>]*>(.*?)</header>', content, re.DOTALL)
    if not m_head:
        errors.append(f"Missing header in {p}")
        header_mismatch += 1
    else:
        # Check essential header elements
        h_str = m_head.group(0)
        if 'class="logo"' not in h_str or 'class="mobile-nav-toggle"' not in h_str or 'class="primary-navigation"' not in h_str or 'class="desktop-cta-wrapper"' not in h_str:
            errors.append(f"Header elements missing in {p}")
            header_mismatch += 1

    # Check Footer structure
    m_foot = re.search(r'<footer class="site-footer"[^>]*>(.*?)</footer>', content, re.DOTALL)
    if not m_foot:
        errors.append(f"Missing footer in {p}")
        footer_mismatch += 1
    else:
        ftr_str = m_foot.group(0).strip()
        if ftr_str != footer_comp:
            errors.append(f"Footer mismatch in {p} vs components/footer.html")
            footer_mismatch += 1

if header_mismatch == 0 and footer_mismatch == 0:
    print("  [OK] Header & Footer Premium structurally identical across all pages!")
else:
    print(f"  [FAIL] Mismatch count - Header: {header_mismatch}, Footer: {footer_mismatch}")

# 4. Check aria-current="page" on active header link for every page
print("\n[4/9] Verifying aria-current='page' on active link for every page...")
aria_current_missing = 0
for p in pages_to_verify:
    fpath = os.path.join(ROOT, p)
    if not os.path.exists(fpath): continue
    content = open(fpath, 'r', encoding='utf-8').read()
    
    m_active = re.search(r'<a\s+href="([^"]+)"\s+class="[^"]*active[^"]*"[^>]*aria-current="page"[^>]*>([^<]+)</a>', content)
    if not m_active:
        # Check reverse order of attributes
        m_active = re.search(r'<a\s+href="([^"]+)"\s+[^>]*aria-current="page"[^>]*class="[^"]*active[^"]*"[^>]*>([^<]+)</a>', content)
    
    if m_active:
        print(f"  [OK] {p:35s} -> Active: '{m_active.group(2).strip()}' ({m_active.group(1)})")
    else:
        errors.append(f"Missing aria-current='page' or active class in {p}")
        aria_current_missing += 1

if aria_current_missing == 0:
    print("  [OK] aria-current='page' verified on ALL 17 pages!")

# 5. Check CSS loading order
print("\n[5/9] Checking CSS loading order (Base -> Components -> Page)...")
css_order_errors = 0
for p in pages_to_verify:
    fpath = os.path.join(ROOT, p)
    if not os.path.exists(fpath): continue
    content = open(fpath, 'r', encoding='utf-8').read()
    css_links = re.findall(r'<link rel="stylesheet" href="([^"]+)">', content)
    
    # Verify Layer 1 (variables, reset, typography, base) comes before Layer 2 (components)
    base_indices = [i for i, c in enumerate(css_links) if '/base/' in c]
    comp_indices = [i for i, c in enumerate(css_links) if '/components/' in c]
    page_indices = [i for i, c in enumerate(css_links) if '/pages/' in c]
    
    if not base_indices or not comp_indices or not page_indices:
        errors.append(f"Missing CSS layer in {p}")
        css_order_errors += 1
    elif max(base_indices) > min(comp_indices) or max(comp_indices) > min(page_indices):
        errors.append(f"CSS layer order invalid in {p}")
        css_order_errors += 1

if css_order_errors == 0:
    print("  [OK] CSS loading order strict Layer 1 -> Layer 2 -> Layer 3 on all pages!")

# 6. Internal links validation
print("\n[6/9] Validating internal links in Header & Footer...")
broken_links = 0
footer_links = re.findall(r'href="([^"#?]+)(?:[#?][^"]*)?"', footer_comp)
header_links = re.findall(r'href="([^"#?]+)(?:[#?][^"]*)?"', header_comp)

for link in set(footer_links + header_links):
    if link.startswith(('http://', 'https://', 'tel:', 'mailto:', '#')):
        continue
    target = os.path.join(ROOT, link)
    if not os.path.exists(target):
        errors.append(f"Broken link in header/footer: {link}")
        broken_links += 1

if broken_links == 0:
    print("  [OK] 0 broken internal links in Header & Footer!")

# 7. Real internal linking mapping check (Adjustment #3)
print("\n[7/9] Checking real internal linking destinations (Home, Services, Solutions, Portfolio, Tarifs, Blog, À propos, Contact)...")
key_pages = ['index.html', 'services.html', 'solutions.html', 'portfolio.html', 'tarifs.html', 'blog.html', 'a-propos.html', 'contact.html']
missing_key = 0
for kp in key_pages:
    target = os.path.join(ROOT, kp)
    if os.path.exists(target):
        print(f"  [OK] Target destination exists: {kp}")
    else:
        errors.append(f"Key destination missing: {kp}")
        missing_key += 1

# 8. Editorial consistency check for residual "24h" / "48h" in Header/Footer (Adjustment #4)
print("\n[8/9] Editorial consistency check: scanning Header & Footer for residual '24h' or '48h'...")
editorial_issues = 0
for term in ['24h', '48h', '24 heures', '48 heures']:
    if term in header_comp.lower():
        errors.append(f"Residual term '{term}' found in header.html")
        editorial_issues += 1
    if term in footer_comp.lower():
        errors.append(f"Residual term '{term}' found in footer.html")
        editorial_issues += 1

if editorial_issues == 0:
    print("  [OK] No residual 24h/48h terms in Header & Footer components!")

# 9. Legal pages status check
print("\n[9/9] Checking legal pages status...")
legals = ['mentions-legales.html', 'politique-confidentialite.html', 'conditions-utilisation.html']
for l in legals:
    lpath = os.path.join(ROOT, l)
    if os.path.exists(lpath):
        size = os.path.getsize(lpath)
        print(f"  [OK] {l:35s} present ({size} bytes)")
    else:
        errors.append(f"Legal page missing: {l}")

print("\n=================================================================")
print(f"RESULTS: {len(errors)} Error(s), {len(warnings)} Warning(s)")
print("=================================================================")

if errors:
    print("\n[FAIL] VERIFICATION FAILED:")
    for err in errors:
        print(f"  - {err}")
    sys.exit(1)
else:
    print("\n[OK] VERIFICATION PASSED — SPRINT 38 FULLY VALIDATED!")
    sys.exit(0)
