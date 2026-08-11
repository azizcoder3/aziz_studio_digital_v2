import re, os
ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'
files = ['blog.html', 'blog-article-seo.html', 'blog-article-wordpress.html', 'blog-article-developpement-web.html']
for f in files:
    path = os.path.join(ROOT, f)
    c = open(path, encoding='utf-8').read()
    h1 = len(re.findall(r'<h1[\s>]', c))
    t = re.findall(r'<title>(.*?)</title>', c, re.DOTALL)
    d = re.findall(r'<meta name="description" content="([^"]+)"', c)
    sz = round(os.path.getsize(path)/1024, 1)
    title_len = len(t[0].strip()) if t else 0
    desc_len = len(d[0]) if d else 0
    print(f'{f}: H1={h1}, title={title_len}ch, desc={desc_len}ch, size={sz}KB')

# Check @import in CSS
print()
css_files = ['blog.css', 'blog-article.css']
for css in css_files:
    path = os.path.join(ROOT, 'assets', 'css', 'pages', css)
    c = open(path, encoding='utf-8').read()
    has_import = '@import' in c
    has_hard_color = bool(re.search(r'(?<!var\()(?<!:)\s*(#[0-9a-fA-F]{3,8}|rgb\(|rgba\()', c))
    lines = len(c.split('\n'))
    print(f'{css}: @import={has_import}, hard_colors={has_hard_color}, lines={lines}')

# Check components
print()
checks = {
    'blog.html': ['hero-dashboard', 'class="breadcrumb"', 'class="blog-card"', 'class="faq-item card"', 'class="badge', 'class="section-header'],
    'blog-article-seo.html': ['class="breadcrumb"', 'itemtype="https://schema.org/Article"', 'class="faq-item card"', 'article-body', 'article-toc', 'card service-cta-final-card', 'service-cta-final-actions'],
    'blog-article-wordpress.html': ['class="breadcrumb"', 'itemtype="https://schema.org/Article"', 'class="faq-item card"', 'card service-cta-final-card', 'service-cta-final-actions'],
    'blog-article-developpement-web.html': ['class="breadcrumb"', 'itemtype="https://schema.org/Article"', 'class="faq-item card"', 'card service-cta-final-card', 'service-cta-final-actions'],
}
for f, tokens in checks.items():
    path = os.path.join(ROOT, f)
    c = open(path, encoding='utf-8').read()
    for tok in tokens:
        ok = tok in c
        status = 'OK' if ok else 'MISSING'
        print(f'  [{status}] {f}: {tok}')
