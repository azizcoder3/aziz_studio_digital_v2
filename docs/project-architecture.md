# Architecture du projet — Aziz Studio Digital V2

> **Document officiel d'architecture** — Version 1.0 — Sprint 29  
> Ce document décrit fidèlement l'état stabilisé du projet après le Sprint 28.  
> Il complète `docs/design-system-components.md` sans le remplacer.

---

## Table des matières

1. [Présentation du projet](#1-présentation-du-projet)
2. [Arborescence complète](#2-arborescence-complète)
3. [Organisation des pages](#3-organisation-des-pages)
4. [Build — `build_index.py`](#4-build--build_indexpy)
5. [Architecture CSS](#5-architecture-css)
6. [Architecture HTML](#6-architecture-html)
7. [JavaScript](#7-javascript)
8. [Design System](#8-design-system)
9. [Pages Services](#9-pages-services)
10. [Conventions](#10-conventions)
11. [Workflow officiel de création d'une nouvelle page](#11-workflow-officiel-de-création-dune-nouvelle-page)
12. [Bonnes pratiques](#12-bonnes-pratiques)
13. [Historique des sprints](#13-historique-des-sprints)

---

## 1. Présentation du projet

**Aziz Studio Digital V2** est le site vitrine officiel de l'agence web Aziz Studio Digital, basée en République du Congo (Brazzaville / Pointe-Noire).

### Objectifs du site

- Présenter l'offre de services : création de site web, WordPress, SEO, refonte, maintenance, audit & conseil digital.
- Générer des demandes de devis et de contact qualifiées.
- Positionner l'agence sur Google avec une architecture SEO technique rigoureuse.
- Garantir une expérience utilisateur premium sur mobile, tablette et desktop.

### Principes techniques fondateurs

| Principe | Choix |
|---|---|
| **Framework** | Aucun — HTML, CSS Vanilla, JavaScript natif |
| **Build** | Script Python (`build_index.py`) — assemblage statique |
| **CSS** | Variables CSS custom properties — aucun framework externe |
| **Accessibilité** | WCAG 2.1 AA — ARIA, navigation clavier, contrastes conformes |
| **Performance** | Pas de dépendances, pas de bundler, code minimal optimisé |
| **Typographie** | Google Fonts : `Inter` (corps) + `Outfit` (titres) |
| **Mode sombre** | Surcharge automatique via `@media (prefers-color-scheme: dark)` |

---

## 2. Arborescence complète

```
aziz_studio_digital_v2/           ← Racine du projet
│
├── index.html                     ← Page d'accueil compilée
├── services.html                  ← Page Services compilée
├── creation-site-web.html         ← Page Service compilée
├── wordpress.html                 ← Page Service compilée
├── seo.html                       ← Page Service compilée
├── refonte-site.html              ← Page Service compilée
├── maintenance.html               ← Page Service compilée
├── audit-conseil.html             ← Page Service compilée
├── portfolio.html                 ← Page Portfolio (statique)
├── blog.html                      ← Page Blog (statique)
├── tarifs.html                    ← Page Tarifs (statique)
├── a-propos.html                  ← Page À propos (statique)
├── contact.html                   ← Page Contact (statique)
├── solutions.html                 ← Page Solutions (statique)
├── mentions-legales.html          ← Page légale
├── politique-confidentialite.html ← Page légale
├── conditions-utilisation.html    ← Page légale
├── 404.html                       ← Page d'erreur
│
├── build_index.py                 ← Script de build (assemblage des pages compilées)
├── netlify.toml                   ← Configuration Netlify (déploiement)
├── manifest.webmanifest           ← Manifeste PWA
├── robots.txt                     ← Directive crawlers
├── sitemap.xml                    ← Plan du site XML
│
├── assets/                        ← Ressources statiques
│   ├── css/
│   │   ├── base/
│   │   │   ├── variables.css      ← Tokens du Design System (couleurs, typo, espacements…)
│   │   │   ├── reset.css          ← Normalisation navigateur
│   │   │   ├── typography.css     ← Styles de base des titres et corps de texte
│   │   │   └── base.css           ← Styles globaux (body, liens, focus)
│   │   ├── components/
│   │   │   ├── container.css      ← Gabarit centré et responsive
│   │   │   ├── grid.css           ← Système de grille CSS Grid
│   │   │   ├── section.css        ← Espacement et variation des sections
│   │   │   ├── card.css           ← Composant carte de base
│   │   │   ├── badge.css          ← Étiquettes / tags / chips
│   │   │   ├── button.css         ← Styles de tous les boutons
│   │   │   ├── header.css         ← Navigation principale fixe
│   │   │   ├── footer.css         ← Pied de page global
│   │   │   ├── form.css           ← Champs de formulaire
│   │   │   ├── faq.css            ← (réservé — vide)
│   │   │   ├── hero.css           ← (réservé — vide)
│   │   │   ├── modal.css          ← (réservé — vide)
│   │   │   └── pricing.css        ← (réservé — vide)
│   │   ├── layout/                ← (réservé — vide, rôles couverts par components/)
│   │   ├── pages/
│   │   │   ├── home.css           ← Styles page d'accueil + composants Premium
│   │   │   ├── services.css       ← Styles page Services + styles partagés services
│   │   │   ├── creation-site-web.css ← Template CSS officiel des 6 pages Service
│   │   │   ├── wordpress.css      ← Surcharges spécifiques WordPress (vide actuellement)
│   │   │   ├── seo.css            ← Surcharges spécifiques SEO (vide actuellement)
│   │   │   ├── refonte-site.css   ← Surcharges spécifiques Refonte (vide actuellement)
│   │   │   ├── maintenance.css    ← Surcharges spécifiques Maintenance (vide actuellement)
│   │   │   ├── audit-conseil.css  ← Surcharges spécifiques Audit (vide actuellement)
│   │   │   ├── blog.css           ← (réservé)
│   │   │   ├── contact.css        ← (réservé)
│   │   │   └── portfolio.css      ← (réservé)
│   │   └── utilities/             ← (réservé — animations.css, helpers.css, spacing.css)
│   ├── js/
│   │   ├── core/
│   │   │   ├── app.js             ← Point d'entrée JS (réservé)
│   │   │   └── config.js          ← Configuration globale (réservé)
│   │   ├── modules/
│   │   │   ├── header.js          ← Navigation sticky, menu mobile, trap focus clavier
│   │   │   ├── footer.js          ← Année dynamique du footer
│   │   │   ├── contact.js         ← (réservé)
│   │   │   ├── faq.js             ← (réservé — FAQ gérée nativement par <details>)
│   │   │   ├── hero.js            ← (réservé)
│   │   │   ├── portfolio.js       ← (réservé)
│   │   │   └── pricing.js         ← (réservé)
│   │   └── utils/                 ← (réservé)
│   ├── images/                    ← Images du projet
│   ├── fonts/                     ← (réservé — polices locales si nécessaire)
│   └── icons/                     ← (réservé — icônes SVG locales)
│
├── components/                    ← Fragments HTML réutilisables (partiels)
│   ├── header.html                ← Fragment navigation principale
│   ├── footer.html                ← Fragment pied de page
│   ├── faq.html                   ← (réservé)
│   ├── hero.html                  ← (réservé)
│   ├── pricing.html               ← (réservé)
│   └── testimonials.html          ← (réservé)
│
├── pages/                         ← Fragments HTML sources (contenu des pages)
│   ├── home.html                  ← Contenu de la page d'accueil
│   ├── services.html              ← Contenu de la page Services
│   ├── creation-site-web.html     ← Contenu de la page Création de site web
│   ├── wordpress.html             ← Contenu de la page WordPress
│   ├── seo.html                   ← Contenu de la page SEO
│   ├── refonte-site.html          ← Contenu de la page Refonte
│   ├── maintenance.html           ← Contenu de la page Maintenance
│   ├── audit-conseil.html         ← Contenu de la page Audit & Conseil
│   └── [secteur]/                 ← Dossiers réservés aux pages Solutions par secteur
│       ├── clinique/
│       ├── hotel/
│       ├── immobilier/
│       ├── pharmacie/
│       ├── restaurant/
│       └── voyage/
│
├── data/                          ← (réservé — données structurées JSON)
├── config/                        ← Configuration JS du site
│   ├── site.js                    ← Paramètres globaux (nom, URL, langue…)
│   ├── seo.js                     ← Configuration SEO globale
│   └── theme.js                   ← Configuration thème / couleurs
├── public/                        ← Ressources publiques statiques
├── blog/                          ← Articles de blog
├── seo/                           ← Ressources SEO additionnelles
└── docs/                          ← Documentation du projet
    ├── design-system-components.md ← Référence officielle du Design System
    ├── project-architecture.md     ← Ce document
    ├── PRD.md                      ← Product Requirements Document
    ├── ROADMAP.md                  ← Feuille de route
    ├── CHANGELOG.md                ← Journal des changements
    ├── SEO.md                      ← Stratégie SEO
    └── sprints/                    ← Documentation de chaque sprint
```

---

## 3. Organisation des pages

### 3.1 Pages sources (fragments)

Les pages sources sont situées dans `pages/`. Ce sont des **fragments HTML purs** : ils contiennent uniquement le contenu `<main>` de la page, sans `<html>`, sans `<head>`, sans `<header>` ni `<footer>`.

```
pages/
├── home.html               ← contenu de l'accueil
├── services.html           ← contenu de la page Services
├── creation-site-web.html  ← contenu de la page Création de site
└── …
```

### 3.2 Pages compilées (pages racine)

Les pages compilées sont situées à la **racine du projet**. Elles sont générées automatiquement par `build_index.py` à partir des fragments sources. Elles incluent `<html>`, `<head>`, les `<link>` CSS, le `<header>` et le `<footer>`.

```
creation-site-web.html   ← assemblée par build_index.py depuis :
                            - components/header.html
                            - pages/creation-site-web.html
                            - components/footer.html
```

> ⚠️ **Ne jamais modifier les pages racine directement.** Toute modification de contenu doit être faite dans `pages/[page].html` puis recompilée via `python build_index.py`.

### 3.3 Pages légales

Les pages légales sont des pages simples autonomes, non gérées par `build_index.py` :

- `mentions-legales.html`
- `politique-confidentialite.html`
- `conditions-utilisation.html`

### 3.4 Pages statiques autonomes

Ces pages ont un contenu propre et ne passent pas par le système de template :

- `portfolio.html`
- `blog.html`
- `tarifs.html`
- `a-propos.html`
- `contact.html`
- `solutions.html`
- `404.html`

---

## 4. Build — `build_index.py`

### 4.1 Rôle

`build_index.py` est le **script de build officiel** du projet. Il assemble les pages compilées en combinant :

1. Un bloc `<head>` complet avec les balises SEO (`<title>`, `<meta description>`) et les `<link>` CSS dans l'ordre exact.
2. Le fragment `components/header.html` (navigation).
3. Le fragment `pages/[page].html` (contenu de la page).
4. Le fragment `components/footer.html` (pied de page).

Le tout est écrit dans le fichier HTML racine correspondant.

### 4.2 Fonctionnement

```python
# Chargement des fragments
header = open('components/header.html').read()
footer = open('components/footer.html').read()
content = open('pages/creation-site-web.html').read()

# Assemblage
html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <title>Création de site web au Congo | Aziz Studio Digital</title>
    …
    <link rel="stylesheet" href="assets/css/pages/services.css">
    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">
    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">
</head>
<body>
{header}
{content}
{footer}
</body>
</html>"""

# Écriture
open('creation-site-web.html', 'w').write(html)
```

### 4.3 Pages compilées par le script

| N° | Page compilée | Fragment source | CSS spécifique |
|---|---|---|---|
| 1 | `index.html` | `pages/home.html` | `home.css` |
| 2 | `services.html` | `pages/services.html` | `services.css` |
| 3 | `creation-site-web.html` | `pages/creation-site-web.html` | `services.css` + `creation-site-web.css` |
| 4 | `wordpress.html` | `pages/wordpress.html` | `services.css` + `creation-site-web.css` + `wordpress.css` |
| 5 | `seo.html` | `pages/seo.html` | `services.css` + `creation-site-web.css` + `seo.css` |
| 6 | `refonte-site.html` | `pages/refonte-site.html` | `services.css` + `creation-site-web.css` + `refonte-site.css` |
| 7 | `maintenance.html` | `pages/maintenance.html` | `services.css` + `creation-site-web.css` + `maintenance.css` |
| 8 | `audit-conseil.html` | `pages/audit-conseil.html` | `services.css` + `creation-site-web.css` + `audit-conseil.css` |

### 4.4 Particularité du header dans les pages Service

Pour les 6 pages Service, le header injecté est une variante du header standard avec le lien "Services" marqué actif :

```python
header_services = header.replace(
    'href="services.html" class="nav-link"',
    'href="services.html" class="nav-link active" aria-current="page"'
)
```

### 4.5 Exécution

```bash
# À la racine du projet
python build_index.py
```

---

## 5. Architecture CSS

### 5.1 Vue d'ensemble

L'architecture CSS suit une structure en 4 couches chargées dans un ordre strict :

```
Layer 1 — BASE        → variables.css, reset.css, typography.css, base.css
Layer 2 — COMPONENTS  → container.css, grid.css, section.css, card.css, badge.css, button.css, header.css, footer.css
Layer 3 — PAGES       → [page].css (styles spécifiques à la page)
Layer 4 — INLINE      → <style> dans le <head> (overrides body padding uniquement)
```

> ⚠️ **Règle absolue :** Ne jamais coder de valeur en dur dans le CSS. Toujours utiliser les variables CSS définies dans `variables.css`.

### 5.2 Ordre de chargement obligatoire pour toutes les pages

```html
<!-- Layer 1: Base -->
<link rel="stylesheet" href="assets/css/base/variables.css">
<link rel="stylesheet" href="assets/css/base/reset.css">
<link rel="stylesheet" href="assets/css/base/typography.css">
<link rel="stylesheet" href="assets/css/base/base.css">

<!-- Layer 2: Components -->
<link rel="stylesheet" href="assets/css/components/container.css">
<link rel="stylesheet" href="assets/css/components/grid.css">
<link rel="stylesheet" href="assets/css/components/section.css">
<link rel="stylesheet" href="assets/css/components/card.css">
<link rel="stylesheet" href="assets/css/components/badge.css">
<link rel="stylesheet" href="assets/css/components/button.css">
<link rel="stylesheet" href="assets/css/components/header.css">
<link rel="stylesheet" href="assets/css/components/footer.css">

<!-- Layer 3: Page-specific (exemple pour une page Service) -->
<link rel="stylesheet" href="assets/css/pages/services.css">
<link rel="stylesheet" href="assets/css/pages/creation-site-web.css">
<link rel="stylesheet" href="assets/css/pages/[page].css">
```

### 5.3 Ordre des feuilles de style des pages Service

Pour les 6 pages Service, les 3 feuilles s'appliquent dans cet ordre précis :

| Ordre | Fichier | Rôle |
|---|---|---|
| 1er | `services.css` | Styles partagés de la page Services générale (hero, dashboard, bannière, composants partagés entre les pages Service) |
| 2e | `creation-site-web.css` | Template CSS officiel des pages Service : hero, timeline, FAQ accordion, CTA final, espacement badge/titre |
| 3e | `[page].css` | Surcharges spécifiques à la page (actuellement vides pour les 5 pages dérivées) |

**Pourquoi cet ordre ?**

- `services.css` pose les fondations visuelles communes héritées de la page Services (Sprint 20/21).
- `creation-site-web.css` introduit le template complet de la page Service (Sprint 22), avec ses composants Premium.
- `[page].css` permet des surcharges propres à une page sans polluer les autres.

### 5.4 Variables CSS (tokens)

Toutes les valeurs de design sont définies dans `assets/css/base/variables.css` :

| Catégorie | Exemples de variables |
|---|---|
| **Couleurs** | `--color-accent`, `--color-background`, `--color-surface`, `--color-border`, `--color-text-primary` |
| **Typographie** | `--font-primary` (Inter), `--font-heading` (Outfit), `--font-size-xs` à `--font-size-4xl` |
| **Espacements** | `--spacing-4px` à `--spacing-128px` |
| **Rayons** | `--radius-small`, `--radius-large`, `--radius-pill`, `--radius-circle` |
| **Ombres** | `--shadow-sm`, `--shadow-md`, `--shadow-lg`, `--shadow-xl` |
| **Transitions** | `--transition-fast`, `--transition-normal`, `--transition-slow` |
| **Z-index** | `--z-index-header`, `--z-index-modal`, `--z-index-overlay` |
| **Breakpoints** | `--breakpoint-mobile` (320px) à `--breakpoint-wide` (1440px) |

Le mode sombre est automatique via `@media (prefers-color-scheme: dark)` dans le même fichier.

### 5.5 Interdictions CSS

- ❌ Aucun `@import` dans les fichiers CSS
- ❌ Aucune valeur en dur (couleurs hexadécimales, px codés en dur sans variable)
- ❌ Aucune duplication de règles entre fichiers
- ❌ Aucun framework CSS externe (pas de Tailwind, Bootstrap…)

---

## 6. Architecture HTML

### 6.1 Fragments partiels (`components/`)

Les fragments de `components/` sont des morceaux de HTML réutilisés sur toutes les pages compilées. Ils ne contiennent que leur propre balisage sémantique, sans `<html>`, `<head>` ni `<body>`.

| Fragment | Fichier | Injecté dans |
|---|---|---|
| Navigation principale | `components/header.html` | Toutes les pages compilées |
| Pied de page | `components/footer.html` | Toutes les pages compilées |

### 6.2 Fragments de contenu (`pages/`)

Les fragments de `pages/` contiennent uniquement le `<main>` de la page. Ils sont assemblés par `build_index.py` avec le header et le footer.

### 6.3 Structure HTML type d'une page Service

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <!-- SEO -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Titre ≤ 60 chars | Aziz Studio Digital]</title>
    <meta name="description" content="[Description ≤ 160 chars]">
    <!-- Fonts -->
    …
    <!-- CSS (dans l'ordre strict) -->
    …
</head>
<body>
    <!-- [HEADER injecté] -->
    <header class="site-header" …> … </header>

    <!-- [CONTENU DE LA PAGE] -->
    <main class="main-content" id="main-content" role="main">
        <!-- 1. Breadcrumb -->
        <div class="services-breadcrumb-wrapper"> … </div>

        <!-- 2. Hero avec Dashboard Premium -->
        <section class="section service-single-hero" id="hero-service-detail"> … </section>

        <!-- 3. Vos enjeux (Pourquoi ce service) -->
        <section class="section section-surface" id="pourquoi-ce-service"> … </section>

        <!-- 4. Ce qui est inclus -->
        <section class="section" id="ce-qui-est-inclus"> … </section>

        <!-- 5. Notre méthode (Timeline Premium) -->
        <section class="section section-surface" id="notre-methode"> … </section>

        <!-- 6. Pourquoi nous choisir -->
        <section class="section" id="pourquoi-nous-choisir"> … </section>

        <!-- 6bis. FAQ Accordion Premium -->
        <section class="section section-surface" id="faq-service"> … </section>

        <!-- 7. CTA Final -->
        <section class="section service-final-cta-section" id="cta-final-service"> … </section>
    </main>

    <!-- [FOOTER injecté] -->
    <footer class="site-footer" …> … </footer>
</body>
</html>
```

### 6.4 Structure du Breadcrumb (obligatoire)

```html
<nav class="breadcrumb" aria-label="Fil d'Ariane">
    <ol class="breadcrumb-list" role="list">
        <li class="breadcrumb-item">
            <a href="index.html" class="breadcrumb-link">Accueil</a>
        </li>
        <li class="breadcrumb-separator" aria-hidden="true">…</li>
        <li class="breadcrumb-item">
            <a href="services.html" class="breadcrumb-link">Services</a>
        </li>
        <li class="breadcrumb-separator" aria-hidden="true">…</li>
        <li class="breadcrumb-item breadcrumb-item-active" aria-current="page">
            <span>Nom du service</span>
        </li>
    </ol>
</nav>
```

### 6.5 Composants Premium réutilisés dans les pages Service

| Composant | Classe racine | Description |
|---|---|---|
| **Hero Dashboard** | `service-single-hero` | Hero avec maquette dashboard animée, métriques, badge flottant |
| **Timeline Premium** | `processus-timeline` | 4 étapes numérotées avec nœuds et ligne de connexion |
| **FAQ Accordion** | `faq-accordion` | Accordéon natif HTML `<details>/<summary>`, 4 questions |
| **CTA Final** | `service-cta-final-card` | Bandeau de conversion avec badge, titre, texte et 2 boutons |
| **Section Header** | `section-header` | En-tête de section avec badge, titre H2 et sous-titre |
| **Cards** | `card service-reason-card` | Cartes réutilisables pour raisons, fonctionnalités, atouts |

---

## 7. JavaScript

### 7.1 Modules actifs

| Module | Fichier | Rôle |
|---|---|---|
| **Navigation** | `assets/js/modules/header.js` | Header sticky au scroll, menu mobile hamburger, trap focus clavier, détection du lien actif |
| **Footer** | `assets/js/modules/footer.js` | Mise à jour dynamique de l'année dans le copyright |

### 7.2 Modules réservés (vides)

Les fichiers `contact.js`, `faq.js`, `hero.js`, `portfolio.js`, `pricing.js` sont créés mais non remplis. Ils serviront lors des sprints futurs correspondants.

### 7.3 Chargement des scripts

Les scripts sont chargés directement dans les pages HTML sans bundler ni transpileur. Aucune dépendance externe (pas de jQuery, pas de React).

---

## 8. Design System

### 8.1 Relation avec `docs/design-system-components.md`

| Document | Rôle |
|---|---|
| **`docs/design-system-components.md`** | Référence des **composants** : comment les utiliser, leurs classes CSS, leurs variantes, leurs exemples HTML |
| **`docs/project-architecture.md`** (ce document) | Référence de l'**architecture** : comment le projet est organisé, comment le build fonctionne, comment ajouter une page |

> Ces deux documents sont complémentaires et doivent être lus ensemble.

### 8.2 Périmètre du Design System

Le Design System couvre :

- Les **tokens** de design (couleurs, typographie, espacements, radii, ombres, transitions) définis dans `variables.css`
- Les **composants atomiques** (Badge, Button, Card, Grid, Container, Section, Header, Footer)
- Les **composants Premium** (Timeline, FAQ Accordion, Hero Dashboard, CTA Final)
- Les **règles d'usage** (aucun code en dur, réutilisation stricte, aucune duplication)

### 8.3 Règle fondamentale

> Aucun composant ne doit jamais être créé en dehors du Design System.  
> Si un composant réutilisable nouveau est identifié, `docs/design-system-components.md` doit être mis à jour.

---

## 9. Pages Services

Les 6 pages Service partagent toutes le même template HTML et CSS (Sprint 22), avec un contenu éditorial entièrement différent et unique.

| Page | Fichier source | Fichier compilé | CSS partagé | CSS spécifique |
|---|---|---|---|---|
| **Création de site web** | `pages/creation-site-web.html` | `creation-site-web.html` | `services.css` + `creation-site-web.css` | — |
| **Développement WordPress** | `pages/wordpress.html` | `wordpress.html` | `services.css` + `creation-site-web.css` | `wordpress.css` |
| **Référencement SEO** | `pages/seo.html` | `seo.html` | `services.css` + `creation-site-web.css` | `seo.css` |
| **Refonte de site web** | `pages/refonte-site.html` | `refonte-site.html` | `services.css` + `creation-site-web.css` | `refonte-site.css` |
| **Maintenance & Support** | `pages/maintenance.html` | `maintenance.html` | `services.css` + `creation-site-web.css` | `maintenance.css` |
| **Audit & Conseil Digital** | `pages/audit-conseil.html` | `audit-conseil.html` | `services.css` + `creation-site-web.css` | `audit-conseil.css` |

### 9.1 Données SEO des 6 pages (mesurées par script Python — Sprint 28)

| Page | Title | Chars | Meta Description | Chars |
|---|---|:---:|---|:---:|
| Création de site web | `Création de site web au Congo | Aziz Studio Digital` | 51 | `Conception de sites vitrines et sur-mesure modernes, rapides et optimisés pour le SEO au Congo par Aziz Studio Digital.` | 119 |
| WordPress | `Développement WordPress au Congo | Aziz Studio Digital` | 54 | `Création et développement de sites WordPress professionnels, autonomes, sécurisés et optimisés pour le SEO au Congo par Aziz Studio Digital.` | 140 |
| SEO | `Référencement Naturel SEO au Congo | Aziz Studio Digital` | 56 | `Optimisation SEO et référencement naturel au Congo par Aziz Studio Digital. Dominez la 1ère page Google, générez du trafic qualifié et attirez plus de clients.` | 159 |
| Refonte | `Refonte de site web au Congo | Aziz Studio Digital` | 50 | `Modernisez votre site web au Congo avec Aziz Studio Digital : redesign UI/UX moderne, refonte technique sans perte SEO et gain de performance mobile.` | 149 |
| Maintenance | `Maintenance de site web au Congo | Aziz Studio Digital` | 54 | `Maintenance et support technique de sites web au Congo par Aziz Studio Digital : sauvegardes automatiques, sécurité, mises à jour et dépannage rapide.` | 150 |
| Audit & Conseil | `Audit digital au Congo | Aziz Studio Digital` | 44 | `Audit digital au Congo par Aziz Studio Digital : analyse SEO, technique, UX et stratégie pour améliorer les performances de votre site web.` | 139 |

---

## 10. Conventions

### 10.1 Nomenclature des classes CSS

| Type | Convention | Exemple |
|---|---|---|
| Composant | kebab-case descriptif | `.service-hero-badge-wrapper` |
| Modificateur | suffixe d'état ou variante | `.section-header-center`, `.btn-primary` |
| Élément JS ciblé | préfixe `js-` (non utilisé actuellement) | `.js-menu-toggle` |
| ID HTML | kebab-case, unique par page | `id="hero-service-detail"` |

### 10.2 Conventions HTML

- **Un seul `<h1>`** par page
- Hiérarchie stricte : `H1` → `H2` → `H3` sans saut de niveau
- `role="main"` sur `<main>`
- `role="banner"` sur `<header>`
- `role="contentinfo"` sur `<footer>`
- `lang="fr"` sur `<html>`
- `aria-hidden="true"` sur tous les SVG et éléments purement décoratifs
- `aria-label` sur tous les éléments interactifs sans texte visible

### 10.3 Conventions SEO

| Élément | Règle |
|---|---|
| `<title>` | Unique, ≤ 60 caractères, exactement 1 séparateur `\|` |
| `<meta description>` | Unique, ≤ 160 caractères |
| Breadcrumb | Structure `Accueil > Services > Nom` avec `aria-current="page"` sur le dernier élément |
| URL des pages | kebab-case, descriptive, sans paramètre |

### 10.4 Conventions éditoriales — CTA

| Type de CTA | Formulation obligatoire |
|---|---|
| Demande de devis | `Demander un devis [Service]` |
| Demande d'audit | `Demander un audit [Service] gratuit` |
| Contact | `Parler de votre projet` |
| Portfolio | `Voir nos réalisations` |

### 10.5 Responsive — Breakpoints

| Nom | Valeur CSS | Utilisation |
|---|---|---|
| Mobile | < 768px | Mobile-first, affichage colonne unique |
| Tablette | ≥ 768px | `@media (min-width: 768px)` |
| Laptop | ≥ 1024px | `@media (min-width: 1024px)` |
| Desktop | ≥ 1200px | `@media (min-width: 1200px)` |
| Wide | ≥ 1440px | `@media (min-width: 1440px)` |

### 10.6 Accessibilité (WCAG 2.1 AA)

- Navigation clavier complète (Tab, Shift+Tab, Escape sur le menu mobile)
- Trap focus dans le menu mobile ouvert
- FAQ Accordion via `<details>/<summary>` natif (accessible sans JavaScript)
- Contrastes de couleur conformes aux ratios WCAG 1.4.3 et 1.4.11
- Tous les liens et boutons ont un état `:focus-visible` visible

---

## 11. Workflow officiel de création d'une nouvelle page

Voici le workflow complet à suivre pour créer une nouvelle page, en respectant l'architecture du projet.

### Étape 1 — Créer le fragment HTML source

```
pages/[nom-page].html
```

Le fragment contient uniquement le `<main>` de la page, sans `<html>`, `<head>`, `<header>` ni `<footer>`.

Pour une page Service, utiliser le template officiel des 6 pages existantes comme référence structurelle.

### Étape 2 — Créer le fichier CSS spécifique

```
assets/css/pages/[nom-page].css
```

Ce fichier ne contient que les surcharges propres à la page. S'il n'y a pas de surcharge, laisser le fichier vide avec un commentaire d'en-tête.

### Étape 3 — Ajouter la page dans `build_index.py`

Ajouter un bloc de compilation en suivant le modèle existant :

```python
# N. Build [nom-page].html
[nom_page]_content = open(os.path.join(ROOT, 'pages', '[nom-page].html'), encoding='utf-8').read()

html_[nom_page] = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    …
    <title>[Titre ≤ 60 chars | Aziz Studio Digital]</title>
    <meta name="description" content="[Description ≤ 160 chars]">
    …
    <link rel="stylesheet" href="assets/css/pages/services.css">
    <link rel="stylesheet" href="assets/css/pages/creation-site-web.css">
    <link rel="stylesheet" href="assets/css/pages/[nom-page].css">
    …
</head>
<body>
{header_services}
{[nom_page]_content}
{footer}
</body>
</html>
"""

out = os.path.join(ROOT, '[nom-page].html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(html_[nom_page])
print('[nom-page].html rebuilt OK!')
```

### Étape 4 — Compiler

```bash
python build_index.py
```

Vérifier la sortie console : chaque page doit afficher `rebuilt OK!`.

### Étape 5 — Vérifier

Ouvrir la page dans un navigateur (via un serveur local) et contrôler :

- [ ] Title et meta description conformes (≤ 60 / ≤ 160 chars, 1 pipe)
- [ ] H1 unique et hiérarchie H1 → H2 → H3 correcte
- [ ] Breadcrumb avec `aria-current="page"` sur le dernier élément
- [ ] CTA conformes à la règle éditoriale officielle
- [ ] Aucun lien cassé
- [ ] Responsive mobile, tablette, desktop
- [ ] Aucun `@import` dans le CSS
- [ ] Design System respecté (aucun nouveau composant créé sans documentation)

### Étape 6 — Documenter

Si un nouveau composant réutilisable a été créé, mettre à jour :

```
docs/design-system-components.md
```

---

## 11. Formulaires — Netlify Forms

Le site utilise la solution native **Netlify Forms** pour la collecte des formulaires de contact (`contact.html`) et de commande (`commande.html`), sans backend ni serveur à maintenir.

### 11.1 Configuration requise dans les formulaires HTML
1. **Attribut `data-netlify="true"`** sur la balise `<form>`.
2. **Attribut `name` unique** (`name="contact"` ou `name="commande"`).
3. **Champ caché `form-name`** : `<input type="hidden" name="form-name" value="contact">`.
4. **Piège anti-spam honeypot** : `<p class="hidden" data-netlify-honeypot="bot-field" style="display:none;"><label>Ne pas remplir : <input name="bot-field"></label></p>`.
5. **Redirection de confirmation** : `action="merci.html"`.

Lors du build et du déploiement statique, Netlify analyse le HTML compilé et active automatiquement les endpoints de soumission de formulaires.

### 11.2 Emails automatiques — Netlify Functions

Lorsqu'un formulaire est soumis, Netlify Forms déclenche un **Outgoing Webhook** vers la fonction backend serverless située dans `netlify/functions/send-autoreply.js`.

**Flux technique :**
1. Le visiteur soumet le formulaire (`contact` ou `commande`).
2. Netlify Forms enregistre la donnée.
3. Un webhook est envoyé à `/.netlify/functions/send-autoreply?secret=VOTRE_WEBHOOK_SECRET`.
4. La fonction vérifie la validité du secret (`process.env.WEBHOOK_SECRET`) transmis via l'en-tête `x-webhook-secret` ou le paramètre `?secret=`.
5. La fonction vérifie le honeypot (`bot-field`).
6. La fonction sélectionne le template HTML correspondant.
7. La fonction utilise Nodemailer pour envoyer l'email de confirmation via SMTP (Gmail).

> ⚠️ **Sécurité absolue :** Aucun identifiant SMTP (email expéditeur, mot de passe d'application) ni secret webhook ne doit jamais être codé en dur dans les fichiers du projet. La fonction lit exclusivement les variables d'environnement `process.env.GMAIL_USER`, `process.env.GMAIL_APP_PASSWORD` et `process.env.WEBHOOK_SECRET`. Ces secrets doivent être configurés manuellement dans l'interface de Netlify (Site settings → Environment variables).


---

## 12. Bonnes pratiques

### À toujours faire

- ✅ Consulter `docs/design-system-components.md` avant d'écrire du HTML ou du CSS
- ✅ Réutiliser les composants existants sans les modifier
- ✅ Utiliser exclusivement les variables CSS de `variables.css`
- ✅ Compiler via `python build_index.py` après toute modification de contenu
- ✅ Respecter l'ordre strict des feuilles de style CSS
- ✅ Tester sur mobile avant desktop (mobile-first)
- ✅ Vérifier l'accessibilité clavier après chaque modification interactive

### À ne jamais faire

- ❌ Modifier directement les pages HTML compilées à la racine (elles seront écrasées au prochain build)
- ❌ Créer un nouveau composant sans le documenter dans le Design System
- ❌ Utiliser `@import` dans le CSS
- ❌ Dupliquer des règles CSS entre fichiers
- ❌ Coder des valeurs en dur dans le CSS (couleurs, tailles, espacements)
- ❌ Modifier le template (`creation-site-web.css`, `services.css`) sans validation
- ❌ Ajouter des dépendances externes (framework, librairie) sans décision collective

---

## 13. Historique des sprints

| Version | Sprint | Description |
|---|---|---|
| — | **Sprint DS-01** | Création du Design System officiel — variables CSS, composants atomiques (Badge, Button, Card, Grid, Container, Section, Header, Footer), documentation dans `docs/design-system-components.md` |
| — | **Sprints 01–04** | Fondations : variables, reset, typographie, base CSS, composants atomiques |
| — | **Sprints 05–17** | Construction de la page d'accueil section par section (Hero, Secteurs, Pourquoi Aziz Studio, Services, Portfolio, Processus, Technologies, Témoignages, FAQ, Blog, CTA) |
| — | **Sprint 18** | Timeline Premium — composant de processus en 4 étapes avec nœuds numérotés et ligne de connexion |
| — | **Sprint 19** | FAQ Premium Accordion — composant accordéon natif HTML `<details>/<summary>` |
| — | **Sprint 20–21** | Page Services générale — hero, grille de services, bannière CTA |
| — | **Sprint 22** | Template officiel des pages Service — création du template complet réutilisé par les 5 pages suivantes. Création de `pages/creation-site-web.html` et `assets/css/pages/creation-site-web.css` |
| — | **Sprint 23** | Page WordPress (`pages/wordpress.html`) |
| — | **Sprint 24** | Page SEO & Référencement (`pages/seo.html`) |
| — | **Sprint 25** | Page Refonte de site web (`pages/refonte-site.html`) |
| — | **Sprint 26** | Page Maintenance & Support (`pages/maintenance.html`) |
| — | **Sprint 27** | Page Audit & Conseil Digital (`pages/audit-conseil.html`) |
| **v1.0** | **Sprint 28** | Harmonisation finale des 6 pages Services — audit SEO, CTA, breadcrumbs, liens, responsive, accessibilité. Architecture considérée **stabilisée** |
| — | **Sprint 29** | Documentation de l'architecture — création de ce document (`docs/project-architecture.md`) |

---

## Historique du document

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-07-23 | Version initiale — architecture stabilisée après Sprint 28 |

---

*Document maintenu par Aziz Studio Digital.*  
*Pour toute question sur les composants, consulter `docs/design-system-components.md`.*  
*Pour toute question sur l'architecture, consulter ce document.*
