import sys, re
sys.stdout.reconfigure(encoding='utf-8')

content = open('solutions.html', encoding='utf-8').read()
css_links = re.findall(r'href=["\'](assets/css/[^"\']+)["\']', content)
page_css = [c for c in css_links if 'assets/css/pages/' in c]

print("=== SPRINT 32 VERIFICATION ===")
print("CSS Pages links loaded in solutions.html:")
for idx, c in enumerate(page_css, 1):
    print(f"  {idx}. {c}")

expected = [
    'assets/css/pages/services.css',
    'assets/css/pages/creation-site-web.css',
    'assets/css/pages/solutions.css'
]

if page_css == expected:
    print("\n✓ CSS loading order matches requirement EXACTLY!")
else:
    print(f"\n❌ CSS loading order mismatch! Expected: {expected}")
