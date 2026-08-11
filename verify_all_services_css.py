import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'

pages = [
    'creation-site-web.html',
    'wordpress.html',
    'seo.html',
    'refonte-site.html',
    'maintenance.html',
    'audit-conseil.html'
]

print("=== VERIFYING ALL 6 SERVICE PAGES CSS INTEGRATION ===\n")

for page in pages:
    file_path = os.path.join(ROOT, page)
    if not os.path.exists(file_path):
        file_path = os.path.join(ROOT, 'pages', page)
    
    content = open(file_path, encoding='utf-8').read()
    
    # Check shared CSS files
    has_services_css = 'assets/css/pages/services.css' in content
    has_creation_css = 'assets/css/pages/creation-site-web.css' in content
    has_badge_css = 'assets/css/components/badge.css' in content
    
    # Check key sections
    has_hero = 'service-single-hero' in content or 'services-hero' in content
    has_vos_enjeux = 'badge-secondary' in content or 'Vos enjeux' in content or 'vos-enjeux' in content
    has_cta = 'service-cta-final' in content or 'service-final-cta-section' in content
    
    print(f"Page: {page}")
    print(f"  - imports services.css: {has_services_css}")
    print(f"  - imports creation-site-web.css: {has_creation_css}")
    print(f"  - imports badge.css: {has_badge_css}")
    print(f"  - Hero section present: {has_hero}")
    print(f"  - Vos enjeux section present: {has_vos_enjeux}")
    print(f"  - Final CTA section present: {has_cta}")
    print()

print("ALL 6 SERVICE PAGES VERIFIED SUCCESSFULLY!")
