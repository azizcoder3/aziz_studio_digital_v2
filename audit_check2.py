import re, os
ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'

# Check CSS vars usage
for css in ['blog.css', 'blog-article.css']:
    c = open(os.path.join(ROOT, 'assets', 'css', 'pages', css), encoding='utf-8').read()
    var_matches = len(re.findall(r'var\(--', c))
    print(css + ': var() usages=' + str(var_matches))

# Check old faq-icon-plus/minus
for f in ['pages/blog-article-template.html', 'blog-article-seo.html']:
    c = open(os.path.join(ROOT, f), encoding='utf-8').read()
    old_faq = ('faq-icon-plus' in c) or ('faq-icon-minus' in c)
    has_cta_card = ('card service-cta-final-card' in c)
    has_chevron = ('faq-chevron' in c)
    print(f + ': old_faq_icons=' + str(old_faq) + ', cta_card_ok=' + str(has_cta_card) + ', chevron=' + str(has_chevron))
