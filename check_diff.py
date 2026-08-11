import difflib

def get_hero(path):
    content = open(path, encoding='utf-8').read()
    start = content.find('<div class="hero-dashboard">')
    end = content.find('<!-- 2.')
    return content[start:end].splitlines()

seo_hero = get_hero('pages/seo.html')
refonte_hero = get_hero('pages/refonte-site.html')
creation_hero = get_hero('pages/creation-site-web.html')

print("=== DIFF SEO VS REFONTE ===")
for line in difflib.unified_diff(seo_hero, refonte_hero, fromfile='seo', tofile='refonte'):
    print(line)

print("\n=== DIFF CREATION VS REFONTE ===")
for line in difflib.unified_diff(creation_hero, refonte_hero, fromfile='creation', tofile='refonte'):
    print(line)
