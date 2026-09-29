import os

ROOT = os.path.dirname(os.path.abspath(__file__))

header = open(os.path.join(ROOT, 'components', 'header.html'), encoding='utf-8').read()
footer = open(os.path.join(ROOT, 'components', 'footer.html'), encoding='utf-8').read()

google_fonts = (
    'https://fonts.googleapis.com/css2'
    '?family=Inter:wght@300;400;500;600;700;800'
    '&family=Outfit:wght@400;500;600;700;800'
    '&display=swap'
)

def render_head(title, description, canonical_url, og_type="website", og_image="https://azizstudiodigital.netlify.app/assets/images/home/hero-illustration.webp", extra_css="", robots="index, follow", verification_tag=""):
    verif_str = f"\n\n    {verification_tag}" if verification_tag else ""
    return f"""<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="robots" content="{robots}">
    <link rel="canonical" href="{canonical_url}">

    <!-- Favicon -->
    <link rel="icon" type="image/png" href="assets/images/favicon.png">

    <!-- Open Graph -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="{og_type}">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:image" content="{og_image}">
    <meta property="og:locale" content="fr_FR">

    <!-- Twitter Cards -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{og_image}">{verif_str}

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="{google_fonts}" rel="stylesheet">

    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-F0Q3GG2XE4"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-F0Q3GG2XE4');
    </script>

    <!-- CSS Base -->
    <link rel="stylesheet" href="assets/css/base/variables.css">
    <link rel="stylesheet" href="assets/css/base/reset.css">
    <link rel="stylesheet" href="assets/css/base/typography.css">
    <link rel="stylesheet" href="assets/css/base/base.css">

    <!-- CSS Composants -->
    <link rel="stylesheet" href="assets/css/components/container.css">
    <link rel="stylesheet" href="assets/css/components/grid.css">
    <link rel="stylesheet" href="assets/css/components/section.css">
    <link rel="stylesheet" href="assets/css/components/card.css">
    <link rel="stylesheet" href="assets/css/components/badge.css">
    <link rel="stylesheet" href="assets/css/components/button.css">
    <link rel="stylesheet" href="assets/css/components/header.css">
    <link rel="stylesheet" href="assets/css/components/footer.css">

    <!-- Schema.org JSON-LD Structured Data -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "ProfessionalService",
      "name": "Aziz Studio Digital",
      "url": "https://azizstudiodigital.netlify.app/",
      "logo": "https://azizstudiodigital.netlify.app/assets/images/aziz_logo.png",
      "image": "https://azizstudiodigital.netlify.app/assets/images/home/hero-illustration.webp",
      "description": "Aziz Studio Digital accompagne les entreprises au Congo avec des sites web rapides, modernes, optimisés pour Google et pensés pour générer des contacts.",
      "address": {{
        "@type": "PostalAddress",
        "addressCountry": "CG",
        "addressLocality": "Brazzaville",
        "addressRegion": "République du Congo"
      }},
      "telephone": "+242066257433",
      "email": "azizstudio.dev@gmail.com",
      "areaServed": [
        {{
          "@type": "City",
          "name": "Brazzaville"
        }},
        {{
          "@type": "City",
          "name": "Pointe-Noire"
        }}
      ]
    }}
    </script>

    {extra_css}

    <style>
        body {{
            padding-top: 73px;
        }}
        @media (min-width: 1024px) {{
            body {{
                padding-top: 90px;
            }}
        }}

        .nav-list,
        .nav-list li {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}

        .footer-links,
        .footer-contact-info,
        .hero-arguments,
        .cta-benefits-list,
        .cta-outcomes-list {{
            list-style: none;
            padding-left: 0;
        }}
    </style>
</head>"""

def render_breadcrumb_schema(page_label, page_url):
    return f"""
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{
          "@type": "ListItem",
          "position": 1,
          "name": "Accueil",
          "item": "https://azizstudiodigital.netlify.app/"
        }},
        {{
          "@type": "ListItem",
          "position": 2,
          "name": "Solutions",
          "item": "https://azizstudiodigital.netlify.app/solutions.html"
        }},
        {{
          "@type": "ListItem",
          "position": 3,
          "name": "{page_label}",
          "item": "{page_url}"
        }}
      ]
    }}
    </script>"""

pages_config = [
    {
        "filename": "index.html",
        "source": os.path.join(ROOT, "pages", "home.html"),
        "title": "Agence web &amp; Création site au Congo – Brazzaville &amp; Pointe-Noire | Aziz Studio Digital",
        "description": "Aziz Studio Digital accompagne les entreprises au Congo avec des sites web rapides, modernes, optimisés pour Google et pensés pour générer des contacts.",
        "canonical": "https://azizstudiodigital.netlify.app/",
        "active_nav": "index.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/home.css">',
        "verification_tag": '<meta name="google-site-verification" content="zH8TtuFb_aDGFspBaykSrhITE8X0Qb011kxqHStp2E4" />'
    },
    {
        "filename": "services.html",
        "source": os.path.join(ROOT, "pages", "services.html"),
        "title": "Nos Services web &amp; SEO au Congo – Brazzaville &amp; Pointe-Noire | Aziz Studio Digital",
        "description": "Découvrez tous les services d'Aziz Studio Digital au Congo : création de site web, WordPress, SEO, refonte, maintenance et audit digital.",
        "canonical": "https://azizstudiodigital.netlify.app/services.html",
        "active_nav": "services.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">'
    },
    {
        "filename": "creation-site-web.html",
        "source": os.path.join(ROOT, "pages", "creation-site-web.html"),
        "title": "Création de site web au Congo | Aziz Studio Digital",
        "description": "Conception de sites vitrines et sur-mesure modernes, rapides et optimisés pour le SEO au Congo par Aziz Studio Digital.",
        "canonical": "https://azizstudiodigital.netlify.app/creation-site-web.html",
        "active_nav": "services.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">'
    },
    {
        "filename": "wordpress.html",
        "source": os.path.join(ROOT, "pages", "wordpress.html"),
        "title": "Développement WordPress au Congo | Aziz Studio Digital",
        "description": "Création et développement de sites WordPress professionnels, autonomes, sécurisés et optimisés pour le SEO au Congo par Aziz Studio Digital.",
        "canonical": "https://azizstudiodigital.netlify.app/wordpress.html",
        "active_nav": "services.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/wordpress.css">'
    },
    {
        "filename": "seo.html",
        "source": os.path.join(ROOT, "pages", "seo.html"),
        "title": "Référencement Naturel SEO au Congo | Aziz Studio Digital",
        "description": "Optimisation SEO et référencement naturel au Congo par Aziz Studio Digital. Dominez la 1ère page Google, générez du trafic qualifié et attirez plus de clients.",
        "canonical": "https://azizstudiodigital.netlify.app/seo.html",
        "active_nav": "services.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/seo.css">'
    },
    {
        "filename": "refonte-site.html",
        "source": os.path.join(ROOT, "pages", "refonte-site.html"),
        "title": "Refonte de site web au Congo | Aziz Studio Digital",
        "description": "Modernisez votre site web au Congo avec Aziz Studio Digital : redesign UI/UX moderne, refonte technique sans perte SEO et gain de performance mobile.",
        "canonical": "https://azizstudiodigital.netlify.app/refonte-site.html",
        "active_nav": "services.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/refonte-site.css">'
    },
    {
        "filename": "maintenance.html",
        "source": os.path.join(ROOT, "pages", "maintenance.html"),
        "title": "Maintenance de site web au Congo | Aziz Studio Digital",
        "description": "Maintenance et support technique de sites web au Congo par Aziz Studio Digital : sauvegardes automatiques, sécurité, mises à jour et dépannage rapide.",
        "canonical": "https://azizstudiodigital.netlify.app/maintenance.html",
        "active_nav": "services.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/maintenance.css">'
    },
    {
        "filename": "audit-conseil.html",
        "source": os.path.join(ROOT, "pages", "audit-conseil.html"),
        "title": "Audit digital au Congo | Aziz Studio Digital",
        "description": "Audit digital au Congo par Aziz Studio Digital : analyse SEO, technique, UX et stratégie pour améliorer les performances de votre site web.",
        "canonical": "https://azizstudiodigital.netlify.app/audit-conseil.html",
        "active_nav": "services.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/audit-conseil.css">'
    },
    {
        "filename": "solutions.html",
        "source": os.path.join(ROOT, "pages", "solutions.html"),
        "title": "Solutions web par secteur au Congo | Aziz Studio Digital",
        "description": "Découvrez nos solutions web sur-mesure adaptées à votre secteur au Congo : PME, artisans, commerçants, ONG, institutions et grandes entreprises.",
        "canonical": "https://azizstudiodigital.netlify.app/solutions.html",
        "active_nav": "solutions.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/solutions.css">'
    },
    {
        "filename": "portfolio.html",
        "source": os.path.join(ROOT, "pages", "portfolio.html"),
        "title": "Portfolio &amp; Réalisations web Congo | Aziz Studio Digital",
        "description": "Découvrez le portfolio des réalisations web d'Aziz Studio Digital au Congo : sites vitrines, WordPress, refontes et optimisations SEO.",
        "canonical": "https://azizstudiodigital.netlify.app/portfolio.html",
        "active_nav": "portfolio.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/portfolio.css">'
    },
    {
        "filename": "tarifs.html",
        "source": os.path.join(ROOT, "pages", "tarifs.html"),
        "title": "Tarifs création de site web au Congo – Brazzaville &amp; Pointe-Noire | Aziz Studio Digital",
        "description": "Découvrez les tarifs de création de site web, WordPress, référencement SEO, maintenance et audit proposés par Aziz Studio Digital au Congo.",
        "canonical": "https://azizstudiodigital.netlify.app/tarifs.html",
        "active_nav": "tarifs.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/tarifs.css">'
    },
    {
        "filename": "a-propos.html",
        "source": os.path.join(ROOT, "pages", "a-propos.html"),
        "title": "Agence web indépendante au Congo | Aziz Studio Digital",
        "description": "Découvrez l'histoire, les valeurs et les engagements d'Aziz Studio Digital, agence web indépendante au service de votre réussite au Congo.",
        "canonical": "https://azizstudiodigital.netlify.app/a-propos.html",
        "active_nav": "a-propos.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/a-propos.css">'
    },
    {
        "filename": "contact.html",
        "source": os.path.join(ROOT, "pages", "contact.html"),
        "title": "Contact &amp; Devis gratuit au Congo – Brazzaville &amp; Pointe-Noire | Aziz Studio Digital",
        "description": "Contactez Aziz Studio Digital au Congo. Devis gratuit, accompagnement personnalisé et étude de votre projet web avec réponse sous 72 heures.",
        "canonical": "https://azizstudiodigital.netlify.app/contact.html",
        "active_nav": "contact.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/components/form.css">\n    <link rel="stylesheet" href="assets/css/pages/contact.css">'
    },
    {
        "filename": "blog.html",
        "source": os.path.join(ROOT, "pages", "blog.html"),
        "title": "Blog, SEO &amp; WordPress au Congo | Aziz Studio Digital",
        "description": "Conseils, guides pratiques et articles d'experts sur la création de site web, le SEO et WordPress au Congo par Aziz Studio Digital.",
        "canonical": "https://azizstudiodigital.netlify.app/blog.html",
        "active_nav": "blog.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/blog.css">'
    },
    {
        "filename": "blog-article-seo.html",
        "source": os.path.join(ROOT, "pages", "blog-article-seo.html"),
        "title": "SEO au Congo : apparaître sur Google | Aziz Studio Digital",
        "description": "Guide complet pour apparaître sur Google au Congo en 2026 : mots-clés locaux, Google Business Profile, SEO technique et plan d'action sur 90 jours.",
        "canonical": "https://azizstudiodigital.netlify.app/blog-article-seo.html",
        "active_nav": "blog.html",
        "og_type": "article",
        "og_image": "https://images.unsplash.com/photo-1562577309-4932fdd64cd1?w=800&q=80",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/blog.css">\n    <link rel="stylesheet" href="assets/css/pages/blog-article.css">'
    },
    {
        "filename": "blog-article-wordpress.html",
        "source": os.path.join(ROOT, "pages", "blog-article-wordpress.html"),
        "title": "WordPress pour votre site d'entreprise | Aziz Studio Digital",
        "description": "WordPress est-il le bon choix pour votre entreprise au Congo ? Avantages, limites et cas d'usage expliqués clairement par Aziz Studio Digital.",
        "canonical": "https://azizstudiodigital.netlify.app/blog-article-wordpress.html",
        "active_nav": "blog.html",
        "og_type": "article",
        "og_image": "https://images.unsplash.com/photo-1547658719-da2b51169166?w=800&q=80",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/blog.css">\n    <link rel="stylesheet" href="assets/css/pages/blog-article.css">'
    },
    {
        "filename": "blog-article-developpement-web.html",
        "source": os.path.join(ROOT, "pages", "blog-article-developpement-web.html"),
        "title": "Développement web : les étapes clés | Aziz Studio Digital",
        "description": "Découvrez les 6 étapes concrètes qui jalonnent un projet web professionnel : découverte, proposition, design, développement, validation et mise en ligne.",
        "canonical": "https://azizstudiodigital.netlify.app/blog-article-developpement-web.html",
        "active_nav": "blog.html",
        "og_type": "article",
        "og_image": "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=800&q=80",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/blog.css">\n    <link rel="stylesheet" href="assets/css/pages/blog-article.css">'
    },
    {
        "filename": "404.html",
        "source_content": """<main class="main-content" id="main-content" role="main">
    <section class="section service-single-hero" id="hero-404">
        <div class="container" style="text-align: center; padding: var(--spacing-64px) var(--spacing-16px);">
            <span class="badge badge-secondary" style="margin-bottom: var(--spacing-16px);"><svg class="lucide-icon lucide-alert-triangle" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg> Erreur 404</span>
            <h1 class="service-hero-title" style="font-size: var(--font-size-4xl); margin-bottom: var(--spacing-16px);">Page non trouvée</h1>
            <h2 class="service-hero-description" style="font-size: var(--font-size-lg); font-weight: var(--font-weight-400); max-width: 600px; margin: 0 auto var(--spacing-32px) auto;">
                La page que vous recherchez n'existe pas ou a été déplacée. Nous vous invitons à retourner sur la page d'accueil ou à consulter nos services.
            </h2>
            <div style="display: flex; gap: var(--spacing-16px); justify-content: center; flex-wrap: wrap;">
                <a href="index.html" class="btn btn-primary">Retour à l'accueil</a>
                <a href="services.html" class="btn btn-outline">Voir nos services</a>
            </div>
        </div>
    </section>
</main>""",
        "title": "Page non trouvée | Aziz Studio Digital",
        "description": "La page que vous recherchez n'existe pas ou a été déplacée. Retournez à l'accueil d'Aziz Studio Digital.",
        "canonical": "https://azizstudiodigital.netlify.app/404.html",
        "robots": "noindex, follow",
        "active_nav": "",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">'
    },
    {
        "filename": "mentions-legales.html",
        "source_content": """<main class="main-content" id="main-content" role="main">
    <div class="services-breadcrumb-wrapper">
        <div class="container">
            <nav class="breadcrumb" aria-label="Fil d'Ariane">
                <ol class="breadcrumb-list" role="list">
                    <li class="breadcrumb-item"><a href="index.html" class="breadcrumb-link">Accueil</a></li>
                    <li class="breadcrumb-separator" aria-hidden="true">/</li>
                    <li class="breadcrumb-item breadcrumb-item-active" aria-current="page"><span>Mentions légales</span></li>
                </ol>
            </nav>
        </div>
    </div>
    <section class="section" id="mentions-legales">
        <div class="container" style="max-width: 800px; margin: 0 auto;">
            <h1 class="service-hero-title" style="margin-bottom: var(--spacing-32px);">Mentions légales</h1>
            <div class="article-body">
                <h2>1. Éditeur du site</h2>
                <p>Le site internet <strong>Aziz Studio Digital</strong> est édité par Aziz Studio Digital, agence web et SEO basée au Congo (Brazzaville &amp; Pointe-Noire).</p>
                <p><strong>Fondateur &amp; Directeur de publication :</strong> Aziz</p>
                <p><strong>Contact :</strong> azizstudio.dev@gmail.com</p>

                <h2>2. Hébergement</h2>
                <p>Le site est hébergé par Netlify, Inc.</p>

                <h2>3. Propriété intellectuelle</h2>
                <p>L'ensemble des contenus (textes, graphismes, logos, éléments visuels) présents sur ce site est la propriété exclusive d'Aziz Studio Digital, sauf mention contraire. Toute reproduction ou représentation sans autorisation expresse est interdite.</p>
            </div>
        </div>
    </section>
</main>""",
        "title": "Mentions légales | Aziz Studio Digital",
        "description": "Consultez les mentions légales d'Aziz Studio Digital, agence de création de sites web et SEO au Congo.",
        "canonical": "https://azizstudiodigital.netlify.app/mentions-legales.html",
        "active_nav": "",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">'
    },
    {
        "filename": "politique-confidentialite.html",
        "source_content": """<main class="main-content" id="main-content" role="main">
    <div class="services-breadcrumb-wrapper">
        <div class="container">
            <nav class="breadcrumb" aria-label="Fil d'Ariane">
                <ol class="breadcrumb-list" role="list">
                    <li class="breadcrumb-item"><a href="index.html" class="breadcrumb-link">Accueil</a></li>
                    <li class="breadcrumb-separator" aria-hidden="true">/</li>
                    <li class="breadcrumb-item breadcrumb-item-active" aria-current="page"><span>Politique de confidentialité</span></li>
                </ol>
            </nav>
        </div>
    </div>
    <section class="section" id="politique-confidentialite">
        <div class="container" style="max-width: 800px; margin: 0 auto;">
            <h1 class="service-hero-title" style="margin-bottom: var(--spacing-32px);">Politique de confidentialité</h1>
            <div class="article-body">
                <h2>1. Collecte des données</h2>
                <p>Aziz Studio Digital s'engage à protéger la vie privée des utilisateurs de son site web. Les informations collectées via le formulaire de contact (nom, adresse email, téléphone, détails du projet) sont utilisées exclusivement pour répondre à vos demandes d'information ou de devis.</p>

                <h2>2. Utilisation des données</h2>
                <p>Vos données personnelles ne sont jamais vendues, louées ou transmises à des tiers sans votre consentement préalable.</p>

                <h2>3. Vos droits</h2>
                <p>Conformément à la réglementation sur la protection des données, vous disposez d'un droit d'accès, de rectification et de suppression de vos données personnelles sur simple demande par email à azizstudio.dev@gmail.com.</p>
            </div>
        </div>
    </section>
</main>""",
        "title": "Politique de confidentialité | Aziz Studio Digital",
        "description": "Consultez la politique de confidentialité d'Aziz Studio Digital concernant le traitement et la protection de vos données.",
        "canonical": "https://azizstudiodigital.netlify.app/politique-confidentialite.html",
        "active_nav": "",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">'
    },
    {
        "filename": "conditions-utilisation.html",
        "source_content": """<main class="main-content" id="main-content" role="main">
    <div class="services-breadcrumb-wrapper">
        <div class="container">
            <nav class="breadcrumb" aria-label="Fil d'Ariane">
                <ol class="breadcrumb-list" role="list">
                    <li class="breadcrumb-item"><a href="index.html" class="breadcrumb-link">Accueil</a></li>
                    <li class="breadcrumb-separator" aria-hidden="true">/</li>
                    <li class="breadcrumb-item breadcrumb-item-active" aria-current="page"><span>Conditions d'utilisation</span></li>
                </ol>
            </nav>
        </div>
    </div>
    <section class="section" id="conditions-utilisation">
        <div class="container" style="max-width: 800px; margin: 0 auto;">
            <h1 class="service-hero-title" style="margin-bottom: var(--spacing-32px);">Conditions d'utilisation</h1>
            <div class="article-body">
                <h2>1. Objet</h2>
                <p>Les présentes conditions d'utilisation régissent l'accès et l'utilisation du site officiel d'Aziz Studio Digital.</p>

                <h2>2. Responsabilité</h2>
                <p>Aziz Studio Digital s'efforce de fournir des informations exactes et à jour sur son site. Toutefois, l'agence ne saurait être tenue responsable des erreurs ou omissions involontaires.</p>
            </div>
        </div>
    </section>
</main>""",
        "title": "Conditions d'utilisation | Aziz Studio Digital",
        "description": "Consultez les conditions d'utilisation du site officiel d'Aziz Studio Digital, agence web et SEO au Congo.",
        "canonical": "https://azizstudiodigital.netlify.app/conditions-utilisation.html",
        "active_nav": "",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">'
    },
    # ----------------------------------------------------------------
    # Pages projet individuelles du portfolio — Sprint 40
    # ----------------------------------------------------------------
    {
        "filename": "projet-boulevard-hotel.html",
        "source": os.path.join(ROOT, "pages", "projet-boulevard-hotel.html"),
        "title": "Boulevard Hôtel — Projet web hôtelier | Aziz Studio Digital",
        "description": "Application hôtelière full-stack pour l'Hôtel Boulevard à Loutété (Congo). Next.js 16, React 19, TypeScript, Prisma, MongoDB, interface bilingue FR/EN.",
        "canonical": "https://azizstudiodigital.netlify.app/projet-boulevard-hotel.html",
        "active_nav": "portfolio.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/projet-template.css">'
    },
    {
        "filename": "projet-atre-steakhouse.html",
        "source": os.path.join(ROOT, "pages", "projet-atre-steakhouse.html"),
        "title": "L'Âtre Steakhouse — Site Vitrine | Aziz Studio Digital",
        "description": "Site vitrine one-page Dark & Moody pour steakhouse gastronomique à Paris et Monaco. HTML5, TailwindCSS, Alpine.js, animations JavaScript natif.",
        "canonical": "https://azizstudiodigital.netlify.app/projet-atre-steakhouse.html",
        "active_nav": "portfolio.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/projet-template.css">'
    },
    {
        "filename": "projet-cabinet-maxwell.html",
        "source": os.path.join(ROOT, "pages", "projet-cabinet-maxwell.html"),
        "title": "Cabinet Maxwell — Site Avocat Congo | Aziz Studio Digital",
        "description": "Landing page SPA premium pour cabinet d'avocats. React 19, Vite 8, TailwindCSS v4, Framer Motion. Design Gold × Dark, 12 sections animées, 2 modals plein écran.",
        "canonical": "https://azizstudiodigital.netlify.app/projet-cabinet-maxwell.html",
        "active_nav": "portfolio.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/projet-template.css">'
    },
    {
        "filename": "projet-dental-glow.html",
        "source": os.path.join(ROOT, "pages", "projet-dental-glow.html"),
        "title": "Dental Glow — Site Cabinet Dentaire | Aziz Studio Digital",
        "description": "Template professionnel pour cabinet dentaire moderne. Vite 6, TailwindCSS 3, GSAP 3, Motion 12. Architecture modulaire en sections HTML indépendantes.",
        "canonical": "https://azizstudiodigital.netlify.app/projet-dental-glow.html",
        "active_nav": "portfolio.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/projet-template.css">'
    },
    {
        "filename": "projet-molato-commerce.html",
        "source": os.path.join(ROOT, "pages", "projet-molato-commerce.html"),
        "title": "Molato Commerce — Marketplace Congo | Aziz Studio Digital",
        "description": "Plateforme marketplace multi-vendeurs pour le marché congolais. Next.js 16, TypeScript, PostgreSQL, Prisma, paiement Mobile Money MTN MoMo et Airtel Money.",
        "canonical": "https://azizstudiodigital.netlify.app/projet-molato-commerce.html",
        "active_nav": "portfolio.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/projet-template.css">'
    },
    {
        "filename": "projet-sante-plus.html",
        "source": os.path.join(ROOT, "pages", "projet-sante-plus.html"),
        "title": "Santé Plus – Plateforme médicale en ligne | Aziz Studio Digital",
        "description": "Plateforme médicale full-stack construite avec Next.js 15 pour la République du Congo : prise de RDV en ligne, espace patient/médecin/admin, notifications SMS et email, gestion des dossiers médicaux.",
        "canonical": "https://azizstudiodigital.netlify.app/projet-sante-plus.html",
        "active_nav": "portfolio.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">\n    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">\n    <link rel="stylesheet" href="assets/css/pages/projet-template.css">'
    },
    {
        "filename": "hotel.html",
        "source": os.path.join(ROOT, "pages", "hotel", "offre.html"),
        "title": "Site web pour hôtel au Congo | Aziz Studio Digital",
        "description": "Création de site web pour hôtels au Congo : réservation en ligne, présentation des chambres et galeries photos. Devis gratuit en 72h.",
        "canonical": "https://azizstudiodigital.netlify.app/hotel.html",
        "breadcrumb_label": "Site web pour hôtels",
        "active_nav": "index.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/components/hero.css">\n    <link rel="stylesheet" href="assets/css/components/pricing.css">\n    <link rel="stylesheet" href="assets/css/components/faq.css">\n    <link rel="stylesheet" href="assets/css/pages/secteurs.css">'
    },
    {
        "filename": "restaurant.html",
        "source": os.path.join(ROOT, "pages", "restaurant", "offre.html"),
        "title": "Site web pour restaurant au Congo | Aziz Studio Digital",
        "description": "Création de site web pour restaurants au Congo : menus interactifs, réservation de table et visibilité Google local. Devis gratuit en 72h.",
        "canonical": "https://azizstudiodigital.netlify.app/restaurant.html",
        "breadcrumb_label": "Site web pour restaurants",
        "active_nav": "index.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/components/hero.css">\n    <link rel="stylesheet" href="assets/css/components/pricing.css">\n    <link rel="stylesheet" href="assets/css/components/faq.css">\n    <link rel="stylesheet" href="assets/css/pages/secteurs.css">'
    },
    {
        "filename": "immobilier.html",
        "source": os.path.join(ROOT, "pages", "immobilier", "offre.html"),
        "title": "Site web pour l'immobilier au Congo | Aziz Studio Digital",
        "description": "Création de site web pour agences immobilières au Congo : catalogue de biens, filtres de recherche et demandes de visite. Devis gratuit en 72h.",
        "canonical": "https://azizstudiodigital.netlify.app/immobilier.html",
        "breadcrumb_label": "Site web pour l'immobilier",
        "active_nav": "index.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/components/hero.css">\n    <link rel="stylesheet" href="assets/css/components/pricing.css">\n    <link rel="stylesheet" href="assets/css/components/faq.css">\n    <link rel="stylesheet" href="assets/css/pages/secteurs.css">'
    },
    {
        "filename": "clinique.html",
        "source": os.path.join(ROOT, "pages", "clinique", "offre.html"),
        "title": "Site web pour clinique au Congo | Aziz Studio Digital",
        "description": "Création de site web pour cliniques au Congo : présentation des pôles médicaux, prise de RDV et informations d'urgence. Devis gratuit en 72h.",
        "canonical": "https://azizstudiodigital.netlify.app/clinique.html",
        "breadcrumb_label": "Site web pour cliniques",
        "active_nav": "index.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/components/hero.css">\n    <link rel="stylesheet" href="assets/css/components/pricing.css">\n    <link rel="stylesheet" href="assets/css/components/faq.css">\n    <link rel="stylesheet" href="assets/css/pages/secteurs.css">'
    },
    {
        "filename": "cabinet-medical.html",
        "source": os.path.join(ROOT, "pages", "cabinet-medical", "offre.html"),
        "title": "Site web cabinet médical au Congo | Aziz Studio Digital",
        "description": "Création de site web pour cabinets médicaux au Congo : fiches praticiens, prise de rendez-vous et horaires d'ouverture. Devis gratuit en 72h.",
        "canonical": "https://azizstudiodigital.netlify.app/cabinet-medical.html",
        "breadcrumb_label": "Site web pour cabinets médicaux",
        "active_nav": "index.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/components/hero.css">\n    <link rel="stylesheet" href="assets/css/components/pricing.css">\n    <link rel="stylesheet" href="assets/css/components/faq.css">\n    <link rel="stylesheet" href="assets/css/pages/secteurs.css">'
    },
    {
        "filename": "cabinet-dentaire.html",
        "source": os.path.join(ROOT, "pages", "cabinet-dentaire", "offre.html"),
        "title": "Site web cabinet dentaire au Congo | Aziz Studio Digital",
        "description": "Création de site web pour cabinets dentaires au Congo : fiches de soins, présentation de l'équipe et prise de rendez-vous. Devis gratuit en 72h.",
        "canonical": "https://azizstudiodigital.netlify.app/cabinet-dentaire.html",
        "breadcrumb_label": "Site web pour cabinets dentaires",
        "active_nav": "index.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/components/hero.css">\n    <link rel="stylesheet" href="assets/css/components/pricing.css">\n    <link rel="stylesheet" href="assets/css/components/faq.css">\n    <link rel="stylesheet" href="assets/css/pages/secteurs.css">'
    },
    {
        "filename": "pharmacie.html",
        "source": os.path.join(ROOT, "pages", "pharmacie", "offre.html"),
        "title": "Site web pour pharmacie au Congo | Aziz Studio Digital",
        "description": "Création de site web pour pharmacies au Congo : plannings de garde, parapharmacie et envoi d'ordonnance sécurisé. Devis gratuit en 72h.",
        "canonical": "https://azizstudiodigital.netlify.app/pharmacie.html",
        "breadcrumb_label": "Site web pour pharmacies",
        "active_nav": "index.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/components/hero.css">\n    <link rel="stylesheet" href="assets/css/components/pricing.css">\n    <link rel="stylesheet" href="assets/css/components/faq.css">\n    <link rel="stylesheet" href="assets/css/pages/secteurs.css">'
    },
    {
        "filename": "salon-beaute.html",
        "source": os.path.join(ROOT, "pages", "salon-beaute", "offre.html"),
        "title": "Site web salon de beauté au Congo | Aziz Studio Digital",
        "description": "Création de site web pour salons de beauté et spas au Congo : carte des soins, réservation en ligne et contact WhatsApp. Devis gratuit en 72h.",
        "canonical": "https://azizstudiodigital.netlify.app/salon-beaute.html",
        "breadcrumb_label": "Site web pour salons de beauté",
        "active_nav": "index.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/components/hero.css">\n    <link rel="stylesheet" href="assets/css/components/pricing.css">\n    <link rel="stylesheet" href="assets/css/components/faq.css">\n    <link rel="stylesheet" href="assets/css/pages/secteurs.css">'
    },
    {
        "filename": "voyage.html",
        "source": os.path.join(ROOT, "pages", "voyage", "offre.html"),
        "title": "Site web agence de voyage au Congo | Aziz Studio Digital",
        "description": "Création de site web pour agences de voyage au Congo : catalogue de séjours, circuits et formulaires de devis sur mesure. Devis gratuit en 72h.",
        "canonical": "https://azizstudiodigital.netlify.app/voyage.html",
        "breadcrumb_label": "Site web pour agences de voyage",
        "active_nav": "index.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/components/hero.css">\n    <link rel="stylesheet" href="assets/css/components/pricing.css">\n    <link rel="stylesheet" href="assets/css/components/faq.css">\n    <link rel="stylesheet" href="assets/css/pages/secteurs.css">'
    },
    {
        "filename": "commande.html",
        "source": os.path.join(ROOT, "pages", "commande.html"),
        "title": "Commander une offre web au Congo | Aziz Studio Digital",
        "description": "Finalisez votre demande d'offre sectorielle pour la création de votre site web au Congo. Réponse et devis détaillé sous 72h.",
        "canonical": "https://azizstudiodigital.netlify.app/commande.html",
        "active_nav": "index.html",
        "extra_css": '<link rel="stylesheet" href="assets/css/components/hero.css">\n    <link rel="stylesheet" href="assets/css/components/pricing.css">\n    <link rel="stylesheet" href="assets/css/components/form.css">\n    <link rel="stylesheet" href="assets/css/pages/commande.css">'
    },
    {
        "filename": "merci.html",
        "source": os.path.join(ROOT, "pages", "merci.html"),
        "title": "Demande de projet transmise | Aziz Studio Digital",
        "description": "Votre demande de devis ou de commande a été bien transmise à notre équipe. Nous vous recontacterons sous 72 heures.",
        "canonical": "https://azizstudiodigital.netlify.app/merci.html",
        "active_nav": "index.html",
        "robots": "noindex, follow",
        "extra_css": '<link rel="stylesheet" href="assets/css/pages/services.css">'
    }
]

for pcfg in pages_config:
    active_nav = pcfg.get("active_nav", "")
    page_header = header
    if active_nav:
        page_header = header.replace(
            f'href="{active_nav}" class="nav-link"',
            f'href="{active_nav}" class="nav-link active" aria-current="page"'
        )
    
    if "source" in pcfg:
        content = open(pcfg["source"], encoding='utf-8').read()
    else:
        content = pcfg["source_content"]
    
    head_html = render_head(
        title=pcfg["title"],
        description=pcfg["description"],
        canonical_url=pcfg["canonical"],
        og_type=pcfg.get("og_type", "website"),
        og_image=pcfg.get("og_image", "https://azizstudiodigital.netlify.app/assets/images/home/hero-illustration.webp"),
        extra_css=pcfg.get("extra_css", ""),
        robots=pcfg.get("robots", "index, follow"),
        verification_tag=pcfg.get("verification_tag", "")
    )
    
    breadcrumb_html = ""
    if pcfg.get("breadcrumb_label"):
        breadcrumb_html = render_breadcrumb_schema(
            page_label=pcfg["breadcrumb_label"],
            page_url=pcfg["canonical"]
        )

    full_html = f"""<!DOCTYPE html>
<html lang="fr">
{head_html}
{breadcrumb_html}
<body>

{page_header}

{content}

{footer}

</body>
</html>
"""
    out_path = os.path.join(ROOT, pcfg["filename"])
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    size_kb = os.path.getsize(out_path) / 1024
    print(f'{pcfg["filename"]} rebuilt OK! {size_kb:.1f} KB')
