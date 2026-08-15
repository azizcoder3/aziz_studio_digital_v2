# Documentation Technique Finale — Aziz Studio Digital V2

**Projet :** Aziz Studio Digital V2  
**Domaine Officiel et Unique de Production :** `https://azizstudiodigital.netlify.app`  
**Version :** 2.0.0  
**Statut :** Livré & Certifié en Production (0 erreur QA)  

---

## Table des Matières
1. [Présentation Générales & Périmètre](#1-présentation-générales--périmètre)
2. [Architecture du Projet & Arborescence Réelle](#2-architecture-du-projet--arborescence-réelle)
3. [Inventaire Exhaustif des 38 Pages HTML](#3-inventaire-exhaustif-des-38-pages-html)
4. [Système de Build (`build_index.py`)](#4-système-de-build-build_indexpy)
5. [Design System & Composants UI](#5-design-system--composants-ui)
6. [Stratégie SEO & Données Structurées](#6-stratégie-seo--données-structurées)
7. [Netlify Functions & Système d'Email Autoreply](#7-netlify-functions--système-demail-autoreply)
8. [Performance & Accessibilité WCAG 2.1 AA](#8-performance--accessibilité-wcag-21-aa)
9. [Synthèse de l'Historique des Sprints](#9-synthèse-de-lhistorique-des-sprints)
10. [Guide de Maintenance & Procédures Pas à Pas](#10-guide-de-maintenance--procédures-pas-à-pas)

---

## 1. Présentation Générales & Périmètre

**Aziz Studio Digital V2** est la plateforme web officielle de l'agence web spécialisée dans la création de sites internet professionnels, l'optimisation SEO, le développement WordPress et les solutions digitales sur mesure pour les entreprises en République du Congo (Brazzaville et Pointe-Noire).

### Technologies Clés
- **Structure :** HTML5 sémantique, architecture par fragments et compilation Python.
- **Styling :** CSS Vanilla modulaire respectant la méthodologie BEM, sans processeur et sans aucune directive `@import`.
- **Logic & Interactions :** JavaScript ES6+ modulaire et natif.
- **Compilateur :** Script Python sur mesure (`build_index.py`) gérant le templating, l'injection de composants et le SEO.
- **Serverless & Emails :** Netlify Functions (`send-autoreply.js`), Nodemailer, Netlify Forms et Webhook Outgoing.
- **Hébergement & Production :** Netlify sur le domaine officiel `https://azizstudiodigital.netlify.app`.

---

## 2. Architecture du Projet & Arborescence Réelle

Le projet est structuré autour d'une séparation stricte entre les fragments sources (`pages/`), les composants partagés (`components/`), les ressources statiques (`assets/`), la configuration du serveur (`netlify/`) et la racine compilée.

```text
aziz_studio_digital_v2/
├── 38 fichiers HTML compilés à la racine (index.html, services.html, etc.)
├── build_index.py                    # Compilateur principal du site
├── sitemap.xml                       # Sitemap XML complet (35 pages indexables)
├── robots.txt                        # Directives pour les robots d'indexation
├── netlify.toml                      # Configuration Netlify & Functions
├── verify_sprint44.py                # Script QA de contrôle pré-production
├── verify_sprint45.py                # Script QA de validation documentaire finale
│
├── pages/                            # Source des fragments HTML (36 fragments)
│   ├── home.html
│   ├── services.html
│   ├── creation-site-web.html
│   ├── wordpress.html
│   ├── seo.html
│   ├── refonte-site.html
│   ├── maintenance.html
│   ├── audit-conseil.html
│   ├── solutions.html
│   ├── portfolio.html
│   ├── tarifs.html
│   ├── a-propos.html
│   ├── contact.html
│   ├── blog.html
│   ├── blog-article-seo.html
│   ├── blog-article-wordpress.html
│   ├── blog-article-developpement-web.html
│   ├── commande.html
│   ├── merci.html
│   ├── projet-boulevard-hotel.html
│   ├── projet-atre-steakhouse.html
│   ├── projet-cabinet-maxwell.html
│   ├── projet-dental-glow.html
│   ├── projet-molato-commerce.html
│   ├── projet-agence-voyage.html
│   └── [secteurs]/
│       ├── hotel/offre.html
│       ├── restaurant/offre.html
│       ├── immobilier/offre.html
│       ├── clinique/offre.html
│       ├── cabinet-medical/offre.html
│       ├── cabinet-dentaire/offre.html
│       ├── pharmacie/offre.html
│       ├── salon-beaute/offre.html
│       └── voyage/offre.html
│
├── components/                       # Composants HTML globaux
│   ├── header.html                   # En-tête et navigation principale
│   ├── footer.html                   # Pied de page Premium global
│   ├── hero.html                     # Hero générique
│   ├── pricing.html                  # Grille de tarifs réutilisable
│   ├── faq.html                      # FAQ réutilisable
│   └── testimonials.html             # Avis clients & preuves réutilisables
│
├── assets/
│   ├── css/                          # Styles CSS modulaires sans @import
│   │   ├── base/                     # Reset, variables, typographie
│   │   ├── components/               # Styles des composants (buttons, cards, badges...)
│   │   ├── layout/                   # Layouts, containers, header, footer
│   │   ├── pages/                    # Styles spécifiques par page
│   │   └── utilities/                # Spacing, helpers, animations
│   ├── js/                           # Scripts JavaScript ES6+
│   │   ├── core/                     # Initialisation & configuration
│   │   ├── modules/                  # Modules fonctionnels (header, faq, etc.)
│   │   └── utils/                    # Dom helpers, animations
│   └── images/                       # Assets visuels et WebP optimisés
│       ├── favicon.svg
│       ├── home/                     # Visuels de l'accueil en WebP
│       ├── portfolio/                # Visuels des projets en WebP
│       └── secteurs/                 # Visuels des offres sectorielles en WebP
│
├── netlify/
│   └── functions/
│       └── send-autoreply.js         # Fonction serverless d'envoi d'emails d'autoreply
│
└── docs/                             # Documentation technique et rapports
    ├── final-project-documentation.md # Ce document
    ├── design-system-components.md    # Documentation du Design System
    ├── project-architecture.md       # Architecture technique
    ├── contributing.md               # Directives de contribution
    └── sprints/                      # Rapports des Sprints 01 à 45
```

---

## 3. Inventaire Exhaustif des 38 Pages HTML

L'ensemble des 38 pages HTML figurant à la racine du projet est catalogué ci-dessous :

| N° | Fichier `.html` | Rôle de la page | URL Canonique | Type | Statut |
|---|---|---|---|---|---|
| 1 | `index.html` | Page d'accueil officielle | `https://azizstudiodigital.netlify.app/` | Principale | Indexable |
| 2 | `services.html` | Hub général des services | `https://azizstudiodigital.netlify.app/services.html` | Service | Indexable |
| 3 | `creation-site-web.html` | Service Création de site web | `https://azizstudiodigital.netlify.app/creation-site-web.html` | Service | Indexable |
| 4 | `wordpress.html` | Service Développement WordPress | `https://azizstudiodigital.netlify.app/wordpress.html` | Service | Indexable |
| 5 | `seo.html` | Service Référencement SEO | `https://azizstudiodigital.netlify.app/seo.html` | Service | Indexable |
| 6 | `refonte-site.html` | Service Refonte de site web | `https://azizstudiodigital.netlify.app/refonte-site.html` | Service | Indexable |
| 7 | `maintenance.html` | Service Maintenance & Hébergement | `https://azizstudiodigital.netlify.app/maintenance.html` | Service | Indexable |
| 8 | `audit-conseil.html` | Service Audit & Conseil digital | `https://azizstudiodigital.netlify.app/audit-conseil.html` | Service | Indexable |
| 9 | `solutions.html` | Hub des solutions sur mesure | `https://azizstudiodigital.netlify.app/solutions.html` | Solution | Indexable |
| 10 | `portfolio.html` | Hub du portfolio et réalisations | `https://azizstudiodigital.netlify.app/portfolio.html` | Portfolio | Indexable |
| 11 | `tarifs.html` | Grille tarifaire des prestations | `https://azizstudiodigital.netlify.app/tarifs.html` | Prestation | Indexable |
| 12 | `a-propos.html` | Présentation du studio et équipe | `https://azizstudiodigital.netlify.app/a-propos.html` | Institutionnel | Indexable |
| 13 | `contact.html` | Page de contact & devis | `https://azizstudiodigital.netlify.app/contact.html` | Conversion | Indexable |
| 14 | `blog.html` | Hub des articles du blog | `https://azizstudiodigital.netlify.app/blog.html` | Blog | Indexable |
| 15 | `blog-article-seo.html` | Article Blog : Stratégie SEO Congo | `https://azizstudiodigital.netlify.app/blog-article-seo.html` | Article | Indexable |
| 16 | `blog-article-wordpress.html` | Article Blog : WordPress au Congo | `https://azizstudiodigital.netlify.app/blog-article-wordpress.html` | Article | Indexable |
| 17 | `blog-article-developpement-web.html` | Article Blog : Création site web | `https://azizstudiodigital.netlify.app/blog-article-developpement-web.html` | Article | Indexable |
| 18 | `projet-boulevard-hotel.html` | Fiche Projet : Boulevard Hôtel | `https://azizstudiodigital.netlify.app/projet-boulevard-hotel.html` | Projet | Indexable |
| 19 | `projet-atre-steakhouse.html` | Fiche Projet : L'Âtre Steakhouse | `https://azizstudiodigital.netlify.app/projet-atre-steakhouse.html` | Projet | Indexable |
| 20 | `projet-cabinet-maxwell.html` | Fiche Projet : Cabinet Maxwell | `https://azizstudiodigital.netlify.app/projet-cabinet-maxwell.html` | Projet | Indexable |
| 21 | `projet-dental-glow.html` | Fiche Projet : Dental Glow | `https://azizstudiodigital.netlify.app/projet-dental-glow.html` | Projet | Indexable |
| 22 | `projet-molato-commerce.html` | Fiche Projet : Molato Commerce | `https://azizstudiodigital.netlify.app/projet-molato-commerce.html` | Projet | Indexable |
| 23 | `projet-agence-voyage.html` | Fiche Projet : Agence de Voyage | `https://azizstudiodigital.netlify.app/projet-agence-voyage.html` | Projet | Indexable |
| 24 | `hotel.html` | Offre Sectorielle : Hôtels | `https://azizstudiodigital.netlify.app/hotel.html` | Secteur | Indexable |
| 25 | `restaurant.html` | Offre Sectorielle : Restaurants | `https://azizstudiodigital.netlify.app/restaurant.html` | Secteur | Indexable |
| 26 | `immobilier.html` | Offre Sectorielle : Immobilier | `https://azizstudiodigital.netlify.app/immobilier.html` | Secteur | Indexable |
| 27 | `clinique.html` | Offre Sectorielle : Cliniques | `https://azizstudiodigital.netlify.app/clinique.html` | Secteur | Indexable |
| 28 | `cabinet-medical.html` | Offre Sectorielle : Cabinets Médicaux | `https://azizstudiodigital.netlify.app/cabinet-medical.html` | Secteur | Indexable |
| 29 | `cabinet-dentaire.html` | Offre Sectorielle : Dentistes | `https://azizstudiodigital.netlify.app/cabinet-dentaire.html` | Secteur | Indexable |
| 30 | `pharmacie.html` | Offre Sectorielle : Pharmacies | `https://azizstudiodigital.netlify.app/pharmacie.html` | Secteur | Indexable |
| 31 | `salon-beaute.html` | Offre Sectorielle : Salons de Beauté | `https://azizstudiodigital.netlify.app/salon-beaute.html` | Secteur | Indexable |
| 32 | `voyage.html` | Offre Sectorielle : Agences de Voyage | `https://azizstudiodigital.netlify.app/voyage.html` | Secteur | Indexable |
| 33 | `commande.html` | Formulaire de commande directe | `https://azizstudiodigital.netlify.app/commande.html` | Conversion | Indexable |
| 34 | `merci.html` | Page de confirmation de soumission | `https://azizstudiodigital.netlify.app/merci.html` | Confirmation | Noindex |
| 35 | `404.html` | Page d'erreur 404 sur mesure | `https://azizstudiodigital.netlify.app/404.html` | Erreur | Noindex |
| 36 | `mentions-legales.html` | Page juridique : Mentions légales | `https://azizstudiodigital.netlify.app/mentions-legales.html` | Juridique | Indexable |
| 37 | `politique-confidentialite.html` | Page juridique : Confidentialité | `https://azizstudiodigital.netlify.app/politique-confidentialite.html` | Juridique | Indexable |
| 38 | `conditions-utilisation.html` | Page juridique : Conditions d'utilisation | `https://azizstudiodigital.netlify.app/conditions-utilisation.html` | Juridique | Indexable |

---

## 4. Système de Build (`build_index.py`)

### Rôle et Mécanisme
Le fichier `build_index.py` est le script Python central en charge de l'assemblage et de la compilation statique de l'ensemble du site web.

1. **Extraction des Composants Globaux :**  
   Lit `components/header.html` et `components/footer.html`.
2. **Configuration par Page (`pages_config`) :**  
   Pour chacune des 28 configurations définies, `build_index.py` spécifie :
   - Le fragment HTML source dans `pages/` (ou le code source inline pour les pages juridiques/404).
   - Le fichier de sortie `.html` à la racine.
   - Le titre SEO `<title>` (strictement $\le 60$ chars avec 1 seul pipe `|`).
   - La méta description (strictement $\le 160$ chars).
   - L'URL canonique (avec le domaine `https://azizstudiodigital.netlify.app`).
   - Les feuilles de style CSS spécifiques à charger (respectant l'ordre Base $\rightarrow$ Components $\rightarrow$ Page).
   - L'onglet actif de la navigation (`nav_active`), injectant `class="nav-link active"` et `aria-current="page"`.
3. **Injection En-tête & Pied de Page :**
   - Injecte le composant `components/header.html` en marquant dynamiquement le lien actif.
   - Injecte le composant `components/footer.html`.
   - Injecte la balise globale Schema.org JSON-LD (`ProfessionalService`).
4. **Fichiers Générés :**  
   Écrit les 38 fichiers `.html` directement à la racine.

### Commande de Compilation
```bash
python build_index.py
```

---

## 5. Design System & Composants UI

Le Design System repose sur une architecture CSS Vanilla stricte sans processeur (Sass/Less) et sans aucune directive `@import` (garantissant 0 blocage de rendu CSS critique).

### Règles d'Or du Design System
- **Règle n° 1 :** NE JAMAIS recréer un composant déjà existant. Toujours réutiliser les classes BEM du Design System (`.btn`, `.card`, `.badge`, `.timeline`, `.faq-accordion`, etc.).
- **Règle n° 2 :** Aucun `@import` dans aucun fichier CSS. Les CSS sont déclarés explicitement dans l'en-tête HTML via des balises `<link rel="stylesheet">`.
- **Règle n° 3 :** Respecter l'ordre des couches CSS :
  1. Base & Variables (`variables.css`, `reset.css`, `base.css`, `typography.css`)
  2. Structure & Layout (`container.css`, `grid.css`, `header.css`, `footer.css`)
  3. Composants réutilisables (`button.css`, `card.css`, `badge.css`, `faq.css`, `pricing.css`, `hero.css`)
  4. Styles spécifiques de la page (`pages/[nom-page].css`)
  5. Utilitaires (`spacing.css`, `helpers.css`, `animations.css`)

### Composants Majeurs Disponibles
- **Navigation (Header & Mobile Menu) :** Responsive, logo SVG, menu hamburger accessible avec aria-expanded.
- **Footer Premium :** Navigation à 4 colonnes, badges de confiance, copyright, coordonnées d'agence.
- **Boutons (`.btn`) :** `.btn-primary`, `.btn-secondary`, `.btn-outline`, `.btn-glow`, tailles `.btn-sm`, `.btn-lg`.
- **Cartes (`.card`) :** Cartes de services, cartes de tarifs, cartes de réalisations du portfolio, cartes de blog.
- **Timeline Processus (`.timeline`) :** Étapes numérotées chronologiques avec connecteurs visuels.
- **FAQ Accordion (`.faq-accordion`) :** Balises nativement accessibles `<details>` et `<summary>`.

---

## 6. Stratégie SEO & Données Structurées

### Normes Strictes
- **Balise `<title>` :** Longueur unescaped $\le 60$ caractères. Exactement 1 seul séparateur `|`. Format : `[Titre de la Page] | Aziz Studio Digital`.
- **Meta Description :** Longueur $\le 160$ caractères, orientée conversion et locale (Congo / Brazzaville / Pointe-Noire).
- **H1 Unique :** Exactement 1 seul `<h1>` par page.
- **Canonical Absolue :** `https://azizstudiodigital.netlify.app/[page].html`.
- **Open Graph & Twitter Cards :** Renseignés sur 100% des pages (`og:title`, `og:description`, `og:url`, `og:image`, `twitter:card`).

### Données Structurées Schema.org JSON-LD
Injecté dynamiquement sur les 38 pages du site dans la fonction `render_head()` de `build_index.py` :
```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Aziz Studio Digital",
  "url": "https://azizstudiodigital.netlify.app/",
  "logo": "https://azizstudiodigital.netlify.app/assets/images/favicon.svg",
  "image": "https://azizstudiodigital.netlify.app/assets/images/home/hero-illustration.webp",
  "description": "Aziz Studio Digital accompagne les entreprises au Congo avec des sites web rapides, modernes, optimisés pour Google et pensés pour générer des contacts.",
  "address": {
    "@type": "PostalAddress",
    "addressCountry": "CG",
    "addressLocality": "Brazzaville / Pointe-Noire",
    "addressRegion": "République du Congo"
  },
  "email": "azizstudio.dev@gmail.com",
  "areaServed": "République du Congo"
}
```

### Sitemap & Robots
- **`sitemap.xml` :** Contient les 36 URLs indexables du domaine `https://azizstudiodigital.netlify.app`.
- **`robots.txt` :** Référence l'URL absolue du sitemap et exclut la page 404.

---

## 7. Netlify Functions & Système d'Email Autoreply

### Formulaires Netlify Forms
Les formulaires de contact (`contact.html`) et de commande (`commande.html`) fonctionnent en natif avec Netlify Forms :
- Attributs requis : `data-netlify="true"`, `method="POST"`, `name="contact"` (ou `name="commande"`).
- Sécurité anti-spam : Champ Honeypot invisible `<input type="hidden" name="bot-field">`.

### Fonction Serverless (`netlify/functions/send-autoreply.js`)
- Déclenchée via un Outgoing Webhook de Netlify Forms.
- Utilise **Nodemailer** pour envoyer un email de confirmation personnalisé au client au format HTML réactif.
- Choix du template automatique selon le nom du formulaire (`contact` vs `commande`).

### Variables d'Environnement (Configurees dans Netlify UI)
1. `GMAIL_USER` : Adresse Gmail de l'expéditeur d'agence (`azizstudio.dev@gmail.com`).
2. `GMAIL_APP_PASSWORD` : Mot de passe d'application SMTP sécurisé Gmail (16 caractères).
3. `WEBHOOK_SECRET` : Clé secrète partagée de signature du Webhook Netlify.

> [!CAUTION]
> Aucun identifiant SMTP ni secret n'est écrit dans le code source. Toutes les variables sont lues exclusivement via `process.env`.

---

## 8. Performance & Accessibilité WCAG 2.1 AA

### Performance & Images WebP
- 100% des visuels sont au format WebP optimisé.
- Attributs de dimensions `width` et `height` systématiques pour éviter tout déplacement de mise en page (CLS).
- Attribut `loading="lazy"` présent sur toutes les images sous la ligne de flottaison.

### Accessibilité (WCAG 2.1 AA)
- Navigation active marquée via `aria-current="page"`.
- Menu hamburger accessible au clavier avec attribut `aria-expanded`.
- Fil d'Ariane sémantique (`<nav aria-label="Fil d'Ariane">`).
- Styles de focus clavier très visibles via `:focus-visible`.
- Pas de saut de niveau de titre (H1 $\rightarrow$ H2 $\rightarrow$ H3).

---

## 9. Synthèse de l'Historique des Sprints

| Sprints | Périmètre et Livrables Clés | Statut |
|---|---|---|
| **01 – 19** | Fondations, Design System v1, structure de la page d'accueil, composants UI basiques. | Achèvement v1 |
| **20 – 28** | Création et harmonisation des pages de Services (WordPress, SEO, Refonte, Maintenance, Audit). | Achèvement v1 |
| **29 – 33** | Architecture des templates, pages Solutions et Portfolio. | Achèvement v1 |
| **34 – 38** | Pages Tarifs, À propos, Contact, Blog et refonte du Footer Premium global. | Achèvement v1 |
| **39** | Audit SEO global & Harmonisation technique des titres et métadonnées. | Validé (38/38) |
| **40** | Création des 9 offres sectorielles et de la page Commande directe. | Validé (11/11) |
| **41** | Optimisation Performance Core Web Vitals & Conversion WebP globale. | Validé (0 JPG/PNG) |
| **42** | Audit et mise en conformité Accessibilité WCAG 2.1 AA globale. | Validé (0 erreur) |
| **43** | Automatisation des emails d'autoreply via Netlify Serverless Functions. | Validé (0 secret hardcodé) |
| **44** | Préparation finale pré-production & Script QA `verify_sprint44.py`. | Validé (0 erreur) |
| **45** | Documentation finale, archivage du projet & Script `verify_sprint45.py`. | Certifié Livraison |

---

## 10. Guide de Maintenance & Procédures Pas à Pas

### Procédure 1 : Ajouter une Nouvelle Page HTML
1. Créer le fragment HTML source dans `pages/votre-nouvelle-page.html`.
2. Ouvrir `build_index.py` et ajouter une nouvelle entrée dans le dictionnaire `pages_config` :
   ```python
   {
       "source": "pages/votre-nouvelle-page.html",
       "output": "votre-nouvelle-page.html",
       "title": "Titre explicite de la page | Aziz Studio Digital",  # max 60 chars
       "meta_desc": "Description concise et captivante pour les utilisateurs au Congo.", # max 160 chars
       "canonical": "https://azizstudiodigital.netlify.app/votre-nouvelle-page.html",
       "css_list": ["assets/css/pages/services.css", "assets/css/pages/votre-page.css"],
       "nav_active": "services" # ou la clé nav correspondante
   }
   ```
3. Exécuter la compilation : `python build_index.py`.
4. Si la page doit être indexée, l'ajouter dans `sitemap.xml`.

### Procédure 2 : Ajouter un Nouvel Article de Blog
1. Dupliquer un article existant dans `pages/blog-article-[nom-sujet].html`.
2. Mettre à jour l'en-tête de l'article, le titre H1, la table des matières (`<a href="#section-1">`) et le contenu textuel.
3. Déclarer la nouvelle page dans `pages_config` dans `build_index.py`.
4. Ajouter une carte résumée vers l'article dans `pages/blog.html`.
5. Compiler (`python build_index.py`) et ajouter l'URL au `sitemap.xml`.

### Procédure 3 : Modifier le Header ou le Footer Global
1. Pour modifier le Header : éditer `components/header.html`.
2. Pour modifier le Footer : éditer `components/footer.html`.
3. Ré-exécuter `python build_index.py` pour propager automatiquement la modification sur l'ensemble des 38 pages du site.

### Procédure 4 : Compiler et Tester le Projet
```bash
# 1. Compilation de toutes les pages HTML
python build_index.py

# 2. Lancement des contrôles qualité automatisés
python verify_sprint44.py
python verify_sprint45.py
```

### Procédure 5 : Déployer en Production sur Netlify
1. Effectuer le push des modifications sur la branche principale Git (`git push origin main`).
2. Netlify détecte automatiquement le push et déploie les fichiers statiques de la racine.
3. Vérifier l'affichage sur `https://azizstudiodigital.netlify.app`.
