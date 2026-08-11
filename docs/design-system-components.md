# Design System — Aziz Studio Digital V2

> **Document de référence officiel** — Version 1.0 — Sprint DS-01  
> Ce document constitue la source unique de vérité du Design System.  
> Il doit être mis à jour à chaque nouveau composant créé.

---

## 1. Présentation

Le Design System d'Aziz Studio Digital V2 est un ensemble de règles, de variables et de composants réutilisables qui garantissent la cohérence visuelle, la maintenabilité et la performance de l'ensemble du projet.

### Objectifs

| Objectif | Description |
|---|---|
| **Cohérence visuelle** | Une seule palette de couleurs, une seule typographie et un seul jeu de composants sur toutes les pages |
| **Réutilisabilité** | Chaque composant est conçu une seule fois et réutilisé sans réécriture |
| **Maintenance** | Modifier une variable CSS (`--color-accent`, `--spacing-24px`) répercute le changement sur l'ensemble du projet |
| **Responsive** | Architecture mobile-first : les breakpoints sont définis une seule fois dans les variables |
| **Accessibilité WCAG 2.1 AA** | Contrastes de couleur conformes, attributs ARIA, navigation clavier |
| **Performances** | Aucun framework CSS externe, aucune librairie, code minimal et optimisé |

---

## 2. Architecture CSS

```
assets/css/
├── base/               ← Fondations — chargées en premier sur toutes les pages
│   ├── variables.css   ← Tous les tokens du Design System (couleurs, typo, spacing…)
│   ├── reset.css       ← Normalisation du comportement navigateur
│   ├── typography.css  ← Styles de base des titres et corps de texte
│   └── base.css        ← Styles globaux de body, liens, focus
│
├── components/         ← Composants atomiques réutilisables (chargés sur toutes les pages)
│   ├── container.css   ← Gabarit centré et responsive
│   ├── grid.css        ← Système de grille CSS Grid
│   ├── section.css     ← Structure et espacement des sections
│   ├── card.css        ← Composant carte de base
│   ├── badge.css       ← Étiquettes / tags / chips
│   ├── button.css      ← Tous les styles de boutons
│   ├── header.css      ← Navigation principale fixe
│   ├── footer.css      ← Pied de page global
│   ├── form.css        ← Champs de formulaire
│   ├── hero.css        ← Hero sectoriel + breadcrumb (Sprint 40)
│   ├── pricing.css     ← Bloc résumé sticky sectoriel (Sprint 40)
│   └── faq.css         ← Accordéon FAQ sectoriel <details>/<summary> (Sprint 40)
│
└── pages/              ← Styles spécifiques à chaque page
    ├── home.css              ← Page d'accueil (2177 lignes — contient tous les composants Premium)
    ├── services.css          ← Page Services (588 lignes)
    └── creation-site-web.css ← Template Page Service (615 lignes)
```

### Ordre de chargement

Chaque page HTML compilée (via `build_index.py`) charge dans cet ordre :

1. `assets/css/base/variables.css`
2. `assets/css/base/reset.css`
3. `assets/css/base/typography.css`
4. `assets/css/base/base.css`
5. `assets/css/components/container.css`
6. `assets/css/components/grid.css`
7. `assets/css/components/section.css`
8. `assets/css/components/card.css`
9. `assets/css/components/badge.css`
10. `assets/css/components/button.css`
11. `assets/css/components/header.css`
12. `assets/css/components/footer.css`
13. `assets/css/pages/<page>.css` (spécifique à la page)

---

## 3. Variables CSS

Toutes les variables sont définies dans `assets/css/base/variables.css` sous la règle `:root {}`.  
Un jeu de surcharge `@media (prefers-color-scheme: dark)` fournit le mode sombre automatique.

> ⚠️ **Règle absolue** : Ne jamais coder une valeur en dur dans le CSS de composant. Utiliser exclusivement les variables ci-dessous.

### 3.1 Couleurs

Chaque couleur est décomposée en 3 variables H/S/L + 1 variable de synthèse pour permettre des transparences via `hsla()`.

| Variable | Rôle | Valeur Light Mode |
|---|---|---|
| `--color-primary` | Couleur principale (texte sombre, survol bouton) | `hsl(224, 64%, 23%)` |
| `--color-secondary` | Couleur secondaire | `hsl(220, 14%, 46%)` |
| `--color-accent` | Couleur d'accentuation (violet) — CTA, badges, liens actifs | `hsl(262, 83%, 58%)` |
| `--color-background` | Fond de page (gris très clair) | `hsl(210, 40%, 98%)` |
| `--color-surface` | Fond des cartes, header, footer (blanc) | `hsl(0, 0%, 100%)` |
| `--color-border` | Couleur des bordures | `hsl(220, 13%, 91%)` |
| `--color-text-primary` | Texte principal (quasi noir) | `hsl(224, 71%, 4%)` |
| `--color-text-secondary` | Texte secondaire (gris) | `hsl(220, 9%, 30%)` |
| `--color-success` | Succès (vert) | `hsl(142, 72%, 29%)` |
| `--color-warning` | Avertissement (ambre) | `hsl(38, 92%, 42%)` |
| `--color-danger` | Erreur (rouge) | `hsl(0, 84%, 50%)` |

**Utilisation des transparences (correct) :**
```css
background-color: hsla(var(--color-accent-h), var(--color-accent-s), var(--color-accent-l), 0.1);
/* NE PAS utiliser : background-color: rgba(120, 60, 220, 0.1); */
```

### 3.2 Typographie

| Variable | Valeur | Usage |
|---|---|---|
| `--font-primary` | `'Inter'` + system fonts | Corps de texte |
| `--font-heading` | `'Outfit'` + fallback | Titres H1–H4, badges, stats |
| `--font-size-xs` | `0.75rem` / 12px | Labels, métadonnées |
| `--font-size-sm` | `0.875rem` / 14px | Texte secondaire, descriptions |
| `--font-size-base` | `1rem` / 16px | Corps de texte standard |
| `--font-size-lg` | `1.125rem` / 18px | Sous-titres, texte mis en avant |
| `--font-size-xl` | `1.25rem` / 20px | Titres de cartes |
| `--font-size-2xl` | `1.5rem` / 24px | Titres de sections (mobile) |
| `--font-size-3xl` | `1.875rem` / 30px | Titres de sections (desktop) |
| `--font-size-4xl` | `3rem` / 48px | H1 Hero (desktop) |

**Weights disponibles :** `--font-weight-300`, `400`, `500`, `600`, `700`, `800`

### 3.3 Espacements

> ⛔ Seules ces valeurs existent. Ne jamais inventer `--spacing-40px` ou similaire.

| Variable | Valeur rem |
|---|---|
| `--spacing-4px` | `0.25rem` |
| `--spacing-6px` | `0.375rem` |
| `--spacing-8px` | `0.5rem` |
| `--spacing-10px` | `0.625rem` |
| `--spacing-12px` | `0.75rem` |
| `--spacing-16px` | `1rem` |
| `--spacing-20px` | `1.25rem` |
| `--spacing-24px` | `1.5rem` |
| `--spacing-32px` | `2rem` |
| `--spacing-48px` | `3rem` |
| `--spacing-64px` | `4rem` |
| `--spacing-80px` | `5rem` |
| `--spacing-96px` | `6rem` |
| `--spacing-128px` | `8rem` |

### 3.4 Border Radius

| Variable | Valeur | Usage |
|---|---|---|
| `--radius-small` | `4px` | Petits éléments (tags) |
| `--radius-medium` | `8px` | Boutons, icônes |
| `--radius-large` | `12px` | Cartes, panels |
| `--radius-xl` | `20px` | Grandes surfaces |
| `--radius-pill` | `9999px` | Badges, progress bars |
| `--radius-circle` | `50%` | Avatars, cercles de numérotation |

### 3.5 Ombres

| Variable | Usage |
|---|---|
| `--shadow-sm` | Ombres très légères (boutons au repos) |
| `--shadow-md` | Cartes au repos, dropdowns |
| `--shadow-lg` | Cartes au survol |
| `--shadow-xl` | Modales, éléments flottants |

### 3.6 Transitions

| Variable | Valeur | Usage |
|---|---|---|
| `--transition-fast` | `150ms cubic-bezier(0.4, 0, 0.2, 1)` | Hover, focus |
| `--transition-normal` | `300ms cubic-bezier(0.4, 0, 0.2, 1)` | Animations UI |
| `--transition-slow` | `500ms cubic-bezier(0.4, 0, 0.2, 1)` | Zoom images |

### 3.7 Z-index

| Variable | Valeur | Usage |
|---|---|---|
| `--z-index-header` | `100` | Barre de navigation fixe |
| `--z-index-dropdown` | `500` | Menus déroulants |
| `--z-index-modal` | `800` | Fenêtres modales |
| `--z-index-overlay` | `900` | Fonds opaques |
| `--z-index-tooltip` | `1000` | Infobulles |

### 3.8 Breakpoints (référence)

| Variable | Valeur |
|---|---|
| `--breakpoint-mobile` | `320px` |
| `--breakpoint-tablet` | `768px` |
| `--breakpoint-laptop` | `1024px` |
| `--breakpoint-desktop` | `1200px` |
| `--breakpoint-wide` | `1440px` |

---

## 4. Composants du Design System

> Ces composants sont chargés sur **toutes les pages** via les fichiers `assets/css/components/`.

---

### 4.1 Container

**Rôle :** Gabarit centré horizontalement avec padding latéral responsive. Enveloppe le contenu de chaque section.

**Fichier CSS :** `assets/css/components/container.css`

**Classes disponibles :** `.container` (seul sélecteur)

**Comportement responsive :**

| Breakpoint | max-width | padding horizontal |
|---|---|---|
| < 576px | 100% | `--spacing-16px` |
| ≥ 576px | 540px | `--spacing-16px` |
| ≥ 768px | 720px | `--spacing-24px` |
| ≥ 1024px | 960px | `--spacing-24px` |
| ≥ 1200px | 1140px | `--spacing-24px` |
| ≥ 1440px | 1280px | `--spacing-24px` |

**Exemple HTML minimal :**
```html
<section class="section">
  <div class="container">
    <!-- Contenu ici -->
  </div>
</section>
```

> **Règle :** Toujours placer `.container` à l'intérieur d'une `.section`, jamais inversé.

---

### 4.2 Grid

**Rôle :** Système de grille CSS Grid responsive mobile-first.

**Fichier CSS :** `assets/css/components/grid.css`

**Classes disponibles :**

```
.grid           → 1 colonne par défaut (mobile)
.grid-2         → 2 colonnes fixes (sans breakpoint)

.grid-md-2      → 2 colonnes dès 768px
.grid-md-3      → 3 colonnes dès 768px
.grid-md-4      → 4 colonnes dès 768px

.grid-lg-2      → 2 colonnes dès 1024px
.grid-lg-3      → 3 colonnes dès 1024px
.grid-lg-4      → 4 colonnes dès 1024px

.col-span-md-2  → s'étend sur 2 col dès 768px
.col-span-lg-2  → s'étend sur 2 col dès 1024px
.col-span-lg-3  → s'étend sur 3 col dès 1024px
.col-span-lg-4  → s'étend sur 4 col dès 1024px
```

**Schéma de fonctionnement :**
```
Mobile (<768px)      Tablette (≥768px)      Desktop (≥1024px)
┌──────────────┐     ┌───────┬───────┐      ┌────┬────┬────┐
│    Item 1    │     │  I 1  │  I 2  │      │ 1  │ 2  │ 3  │
├──────────────┤     ├───────┼───────┤      ├────┼────┼────┤
│    Item 2    │     │  I 3  │  I 4  │      │ 4  │ 5  │ 6  │
└──────────────┘     └───────┴───────┘      └────┴────┴────┘
   .grid              .grid.grid-md-2         .grid.grid-lg-3
```

**Gap par défaut :** `--spacing-24px`

**Exemple HTML :**
```html
<div class="grid grid-md-2 grid-lg-3">
  <article class="card">...</article>
  <article class="card">...</article>
  <article class="card">...</article>
</div>
```

---

### 4.3 Section

**Rôle :** Définit le rythme vertical des sections de page et leur fond.

**Fichier CSS :** `assets/css/components/section.css`

| Classe | Rôle |
|---|---|
| `.section` | Padding `64px` vertical mobile, `96px` ≥ 768px |
| `.section-surface` | Fond `--color-surface` (blanc) — alterne avec fond de page |
| `.section-alt` | Fond légèrement coloré (primaire clair) |
| `.section-header` | Wraps titre + sous-titre, max-width 680px |
| `.section-header-center` | Centre le header |
| `.section-title` | H2 — `font-heading`, `font-weight-800` |
| `.section-subtitle` | Sous-titre — `font-size-lg`, `color-text-secondary` |

**Exemple HTML minimal :**
```html
<section class="section section-surface" id="ma-section">
  <div class="container">
    <div class="section-header section-header-center">
      <span class="badge badge-primary">🏷️ Label</span>
      <h2 class="section-title">Titre</h2>
      <p class="section-subtitle">Description.</p>
    </div>
  </div>
</section>
```

---

### 4.4 Card

**Rôle :** Conteneur de contenu universel avec fond, bordure, radius et hover animé.

**Fichier CSS :** `assets/css/components/card.css`

| Classe | Rôle |
|---|---|
| `.card` | Fond surface, bordure, radius-large, flex colonne, height 100% |
| `.card-body` | Zone de contenu — padding `24px`, flex-grow |
| `.card-title` | `font-heading`, `font-size-xl`, `font-weight-700` |
| `.card-description` | `font-size-sm`, `color-text-secondary`, line-height 1.6 |
| `.card-content` | Zone de contenu flexible (flex-grow: 1) |
| `.card-footer` | Pied de carte — border-top, bg-background |
| `.card-image-wrapper` | Zone image 16:9 avec overflow hidden |
| `.card-image` | `object-fit: cover` + zoom au survol |

**Hover par défaut :** `translateY(-4px)` + `shadow-lg`

**Exemple HTML minimal :**
```html
<article class="card">
  <div class="card-image-wrapper">
    <img class="card-image" src="..." alt="Description">
  </div>
  <div class="card-body">
    <h3 class="card-title">Titre</h3>
    <p class="card-description">Description courte.</p>
  </div>
  <div class="card-footer">
    <a href="#" class="btn btn-primary">Action</a>
  </div>
</article>
```

> **Règle :** Ne jamais redéfinir `background-color`, `border-radius` ou `border` d'une `.card` dans une CSS de page. Utiliser des classes modificatrices.

---

### 4.5 Badge

**Rôle :** Étiquette compacte pour qualifier une section, un statut ou une catégorie.

**Fichier CSS :** `assets/css/components/badge.css`

| Classe | Couleur | Usage typique |
|---|---|---|
| `.badge-primary` | Violet (accent) | Sections Hero, labels principaux |
| `.badge-secondary` | Gris (secondary) | Sections de contenu standard |
| `.badge-success` | Vert | Statuts positifs |
| `.badge-warning` | Ambre | Alertes |
| `.badge-danger` | Rouge | Erreurs |

**Exemple HTML :**
```html
<span class="badge badge-primary">🚀 Création de site web</span>
<span class="badge badge-secondary">💡 Vos enjeux</span>
```

> **Règle :** Toujours associer `.badge` + un modificateur de couleur. Ne jamais utiliser `.badge` seul.

---

### 4.6 Button

**Rôle :** Boutons d'appel à l'action. Couvre tous les états (survol, focus, désactivé).

**Fichier CSS :** `assets/css/components/button.css`

**Classes de base :**

| Classe | Rôle |
|---|---|
| `.btn` | Base obligatoire — padding, font, border, transition |
| `.btn-sm` | Variante petite |
| `.btn-lg` | Variante grande |

**Variantes :**

| Classe | Usage |
|---|---|
| `.btn-primary` | CTA principal (violet accent) |
| `.btn-secondary` | CTA secondaire (bleu) |
| `.btn-outline` | Alternative (bordure, fond transparent) |
| `.btn-ghost` | Action discrète (fond transparent) |
| `.btn-text` | Lien textuel avec flèche, padding 0 |

**Exemple HTML :**
```html
<a href="contact.html" class="btn btn-primary">Demander un devis</a>
<a href="portfolio.html" class="btn btn-outline">Nos réalisations</a>
<a href="services.html" class="btn btn-text">Découvrir →</a>
```

**États :** `:focus-visible` avec ring violet 3px ; `:disabled` opacité 0.6.

---

### 4.7 Header

**Rôle :** Barre de navigation principale, fixe en haut de page sur toutes les pages compilées.

**Fichier CSS :** `assets/css/components/header.css` (289 lignes)  
**Fichier HTML :** `components/header.html`

| Classe | Rôle |
|---|---|
| `.site-header` | Position fixed, z-index 100, fond surface, border-bottom |
| `.header-container` | Flex row — logo gauche, nav centre, CTA droite |
| `.logo` | Wordmark — `font-heading`, `font-weight-800` + `.text-accent` violet |
| `.primary-navigation` | Panel mobile (overlay fullscreen) / inline desktop |
| `.primary-navigation.is-open` | État menu ouvert |
| `.nav-list` | Liste des liens |
| `.nav-link` | Lien standard |
| `.nav-link.active` | Page courante (injecté par `build_index.py`) |

**Responsive :**
- Mobile : hamburger + overlay fullscreen
- ≥ 1024px : navigation horizontale inline

**Ajustement body** (injecté par `build_index.py`) :
```css
body { padding-top: 73px; }
@media (min-width: 1024px) { body { padding-top: 90px; } }
```

---

### 4.8 Footer

**Rôle :** Pied de page global, présent sur toutes les pages compilées.

**Fichier CSS :** `assets/css/components/footer.css` (333 lignes)  
**Fichier HTML :** `components/footer.html`

| Classe | Rôle |
|---|---|
| `.site-footer` | Fond surface, border-top |
| `.footer-container` | Flex colonne avec gap |
| `.footer-top` | Logo + description + réseaux sociaux |
| `.footer-brand` | Bloc logo + texte agence |
| `.social-links` / `.social-link` | Liens réseaux sociaux |
| `.footer-nav-grid` | Grille des colonnes de liens |
| `.footer-nav-title` | Titre de colonne |
| `.footer-links` | Liste de liens de colonne |
| `.footer-contact-info` | Informations de contact |
| `.footer-bottom` | Copyright + mentions légales |

---

## 5. Composants Premium créés

> Ces composants ont été développés durant les Sprints.  
> Chaque composant est **documenté avec sa localisation exacte** dans le code source.

---

### 5.1 Hero Premium (Sprint 06)

**Objectif :** Section héros de la page d'accueil avec blobs animés CSS, grille 2 colonnes, statistiques et illustration HTML/CSS.

**Classes CSS clés :** `.hero-section`, `.hero-grid`, `.hero-content`, `.hero-badge-wrapper`, `.hero-title`, `.hero-subtitle`, `.hero-arguments`, `.hero-argument-item`, `.argument-icon`, `.hero-actions`, `.hero-cta-primary`, `.hero-cta-secondary`, `.hero-stats`, `.stat-item`, `.stat-number`, `.stat-label`, `.hero-illustration`, `.illustration-placeholder`, `.placeholder-graphic`, `.graphic-window`, `.window-header`, `.window-body`, `.dot`, `.dot-red`, `.dot-yellow`, `.dot-green`, `.graphic-line`, `.graphic-cards`, `.card-box`

**Animations :** `@keyframes heroBlobFloat` et `@keyframes heroBlobPulse` (pseudo-éléments `::before` / `::after` de `.hero-section`)

**Responsive :**
- Mobile : 1 colonne
- ≥ 768px : 2 colonnes côte à côte

**Structure HTML (résumée) :**
```html
<section class="section hero-section" id="hero">
  <div class="container">
    <div class="grid grid-md-2 hero-grid">
      <div class="hero-content">
        <div class="hero-badge-wrapper"><span class="badge badge-primary">...</span></div>
        <h1 class="hero-title">...</h1>
        <p class="hero-subtitle">...</p>
        <ul class="hero-arguments"><li class="hero-argument-item">...</li></ul>
        <div class="hero-actions">
          <a class="btn btn-primary hero-cta-primary">...</a>
          <a class="btn btn-outline hero-cta-secondary">...</a>
        </div>
        <div class="hero-stats">
          <div class="stat-item">
            <span class="stat-number">X+</span>
            <span class="stat-label">label</span>
          </div>
        </div>
      </div>
      <div class="hero-illustration">
        <div class="illustration-placeholder">
          <div class="placeholder-graphic"><div class="graphic-window">...</div></div>
        </div>
      </div>
    </div>
  </div>
</section>
```

### Localisation du code source

| | Fichier | Localisation |
|---|---|---|
| **HTML** | `pages/home.html` | section `#hero` |
| **CSS** | `assets/css/pages/home.css` | lignes **1 à 370** |

---

### 5.2 Secteurs Section (Sprint 07)

**Objectif :** Grille de cartes présentant les secteurs d'activité couverts (BTP, Restauration, Hôtellerie, etc.).

**Classes CSS clés :** `.secteurs-badge-wrapper`, `.secteurs-grid`, `.secteur-card`, `.secteur-icon-wrapper`, `.secteur-icon`

**Responsive :** `.grid .grid-md-2 .grid-lg-3`

### Localisation du code source

| | Fichier | Localisation |
|---|---|---|
| **HTML** | `pages/home.html` | section `#secteurs` |
| **CSS** | `assets/css/pages/home.css` | lignes **371 à 429** |

---

### 5.3 Bloc Réassurance — Pourquoi Aziz Studio Digital (Sprint 08)

**Objectif :** Grille de 4 cartes présentant les valeurs différenciatrices de l'agence.

**Classes CSS clés :** `.pourquoi-badge-wrapper`, `.pourquoi-grid`, `.pourquoi-card`, `.pourquoi-icon-wrapper`, `.pourquoi-icon`, `.pourquoi-card-title`, `.pourquoi-card-description`

**Responsive :** `.grid .grid-md-2 .grid-lg-4`

### Localisation du code source

| | Fichier | Localisation |
|---|---|---|
| **HTML** | `pages/home.html` | section `#pourquoi` |
| **CSS** | `assets/css/pages/home.css` | lignes **430 à 539** |

---

### 5.4 Services Home Cards (Sprint 09)

**Objectif :** Aperçu des services principaux sur la Home avec icône, titre, description et CTA.

**Classes CSS clés :** `.services-badge-wrapper`, `.services-home-grid`, `.service-home-card`, `.service-home-icon-wrapper`, `.service-home-icon`

**Responsive :** `.grid .grid-md-2 .grid-lg-3`

### Localisation du code source

| | Fichier | Localisation |
|---|---|---|
| **HTML** | `pages/home.html` | section `#services` |
| **CSS** | `assets/css/pages/home.css` | lignes **540 à 668** |

---

### 5.5 Réalisations / Portfolio Cards (Sprint 10)

**Objectif :** Grille de cartes portfolio avec image, tag, titre, description et lien.

**Classes CSS clés :** `.realisations-badge-wrapper`, `.realisations-grid`, `.realisation-card`, `.realisation-image-wrapper`, `.realisation-tag`, `.realisation-title`

**Responsive :** `.grid .grid-md-2 .grid-lg-3`

### Localisation du code source

| | Fichier | Localisation |
|---|---|---|
| **HTML** | `pages/home.html` | section `#realisations` |
| **CSS** | `assets/css/pages/home.css` | lignes **669 à 807** |

---

### 5.6 Timeline Premium — Processus de travail (Sprint 18)

**Objectif :** Visualisation du processus en 6 étapes (Home) ou 4 étapes (pages service) avec cercles numérotés reliés par une ligne continue, cartes détaillées avec icône, outcomes et durée.

**Classes CSS clés :** `.processus-timeline`, `.timeline-track`, `.processus-steps-grid`, `.timeline-step`, `.timeline-node`, `.step-number`, `.processus-card`, `.processus-card-header`, `.processus-icon-wrapper`, `.processus-icon`, `.processus-outcomes`, `.outcomes-title`, `.outcomes-list`, `.outcome-check`, `.processus-duration`, `.clock-icon`

**Comportement responsive :**

| Breakpoint | Layout |
|---|---|
| Mobile (< 768px) | Colonne verticale + ligne gauche via `.timeline-track` absolu |
| 768–1023px | Grille 3×2 (Home) ou 2×2 (Service) + lignes via `::before` |
| ≥ 1024px | Grille 6 colonnes (Home) ou 4 colonnes (Service) + ligne continue `.timeline-track` |

**Structure HTML (résumée) :**
```html
<div class="processus-timeline" aria-label="Processus en X étapes">
  <div class="timeline-track" aria-hidden="true"></div>
  <div class="processus-steps-grid">
    <div class="timeline-step">
      <div class="timeline-node">
        <span class="step-number" aria-label="Étape 01">01</span>
      </div>
      <article class="card processus-card">
        <div class="card-body">
          <div class="processus-card-header">
            <div class="processus-icon-wrapper" aria-hidden="true">
              <svg class="processus-icon">...</svg>
            </div>
          </div>
          <h3 class="card-title">Titre étape</h3>
          <p class="card-description">...</p>
          <div class="processus-outcomes">
            <h4 class="outcomes-title">Vous obtenez :</h4>
            <ul class="outcomes-list">
              <li><svg class="outcome-check" aria-hidden="true">...</svg> Résultat</li>
            </ul>
          </div>
          <div class="processus-duration">
            <svg class="clock-icon" aria-hidden="true">...</svg>
            <span>Durée : X jours</span>
          </div>
        </div>
      </article>
    </div>
    <!-- Répéter par étape -->
  </div>
</div>
```

**Utilisé dans :**
- `pages/home.html` — 6 étapes (version complète)
- `pages/creation-site-web.html` — 4 étapes (avec classe `.grid-4-steps`)

### Localisation du code source

| | Fichier | Localisation |
|---|---|---|
| **HTML (6 étapes)** | `pages/home.html` | section `#processus` |
| **CSS (Home)** | `assets/css/pages/home.css` | lignes **808 à 1165** |
| **HTML (4 étapes)** | `pages/creation-site-web.html` | section `#notre-methode` |
| **CSS (Service)** | `assets/css/pages/creation-site-web.css` | section "Timeline Premium" |

---

### 5.7 Technologies Cards (Sprint 12)

**Objectif :** Grille de cartes présentant les technologies maîtrisées (HTML/CSS, WordPress, SEO, etc.).

**Classes CSS clés :** `.tech-badge-wrapper`, `.tech-grid`, `.tech-card`, `.tech-icon-wrapper`, `.tech-card-header`

**Responsive :** `.grid .grid-md-3 .grid-lg-4`

### Localisation du code source

| | Fichier | Localisation |
|---|---|---|
| **HTML** | `pages/home.html` | section `#technologies` |
| **CSS** | `assets/css/pages/home.css` | lignes **1166 à 1302** |

---

### 5.8 Témoignages Cards + Stats Banner (Sprint 13)

**Objectif :** Grille de cartes témoignages avec étoiles, citation, auteur, entreprise ; plus un bandeau de statistiques chiffrées.

**Classes CSS clés :** `.testimonial-card`, `.testimonial-header`, `.testimonial-stars`, `.star-icon`, `.testimonial-meta`, `.testimonial-company`, `.testimonial-quote`, `.testimonial-footer`, `.testimonial-author`, `.author-name`, `.author-role`, `.testimonial-stats-banner`, `.testimonial-stat-item`, `.testimonial-stat-value`, `.testimonial-stat-label`

**Responsive :** `.grid .grid-md-2 .grid-lg-3`

### Localisation du code source

| | Fichier | Localisation |
|---|---|---|
| **HTML** | `pages/home.html` | section `#temoignages` |
| **CSS** | `assets/css/pages/home.css` | lignes **1303 à 1521** |

---

### 5.9 FAQ Premium Accordion (Sprint 19)

**Objectif :** Accordéon de questions/réponses avec icône SVG dans cercle violet à gauche de chaque question, chevron animé à droite. Fonctionne sans JavaScript via `<details>/<summary>` HTML5.

**Classes CSS clés :** `.faq-badge-wrapper`, `.faq-accordion-wrapper`, `.faq-accordion`, `.faq-item`, `.faq-summary`, `.faq-question`, `.faq-icon-wrapper`, `.faq-icon`, `.faq-question-title`, `.faq-chevron`, `.faq-answer`, `.faq-answer-text`, `.faq-footer`, `.faq-link`

**Comportement :**
- `.faq-item[open]` → `border-color` accent + `shadow-md`
- `.faq-item[open] .faq-chevron` → `rotate(180deg)`
- Survol ou `[open]` de `.faq-icon-wrapper` → fond violet, icône blanche

**Structure HTML :**
```html
<div class="faq-accordion-wrapper">
  <div class="faq-accordion">
    <details class="faq-item card" open>
      <summary class="faq-summary">
        <div class="faq-question">
          <div class="faq-icon-wrapper" aria-hidden="true">
            <svg class="faq-icon"><!-- icône spécifique --></svg>
          </div>
          <h3 class="faq-question-title">Question ?</h3>
        </div>
        <svg class="faq-chevron" aria-hidden="true"><!-- chevron ˅ --></svg>
      </summary>
      <div class="faq-answer">
        <p class="faq-answer-text">Réponse.</p>
        <!-- Optionnel sur Home : -->
        <div class="faq-footer">
          <a href="#" class="faq-link">Lien contextuel</a>
        </div>
      </div>
    </details>
  </div>
</div>
```

**Icônes recommandées par type de question :**

| Type de question | Icône SVG à utiliser |
|---|---|
| Durée / délai | Horloge — `<circle cx="12" cy="12" r="10">` + `<polyline points="12 6 12 12 16 14">` |
| Coût / tarif | Carte bancaire — `<rect x="1" y="4" width="22" height="16">` + ligne |
| Modification contenu | Crayon — `<path d="M11 4H4a2 2...">` |
| Référencement Google | Loupe — `<circle cx="11" cy="11" r="8">` + `<line x1="21" y1="21">` |
| Hébergement / domaine | Serveur — `<rect x="2" y="2" width="20" height="8">` double |
| Question générale | Point d'interrogation — `<circle cx="12" cy="12" r="10">` + `<path d="M9.09 9...">` |

**Utilisé dans :**
- `pages/home.html` section `#faq` — version complète avec `.faq-toggle-checkbox`
- `pages/creation-site-web.html` section `#faq-service` — version simplifiée

### Localisation du code source

| | Fichier | Localisation |
|---|---|---|
| **HTML (Home)** | `pages/home.html` | section `#faq` |
| **CSS (Home)** | `assets/css/pages/home.css` | lignes **1522 à 1810** |
| **HTML (Service)** | `pages/creation-site-web.html` | section `#faq-service` |
| **CSS (Service)** | `assets/css/pages/creation-site-web.css` | section "FAQ Premium Accordion" |

---

### 5.10 Blog Cards (Sprint 15)

**Objectif :** Grille d'articles de blog avec image placeholder HTML/CSS, métadonnées (date, durée de lecture), titre, extrait et CTA.

**Classes CSS clés :** `.blog-grid`, `.blog-card`, `.blog-image-placeholder`, `.blog-placeholder-content`, `.blog-placeholder-icon`, `.blog-placeholder-tag`, `.blog-card-meta`, `.blog-meta-details`, `.blog-date`, `.blog-read-time`, `.meta-icon`, `.blog-title`, `.blog-excerpt`, `.blog-cta`, `.blog-cta-banner`

**Responsive :** `.grid .grid-md-2 .grid-lg-3`

### Localisation du code source

| | Fichier | Localisation |
|---|---|---|
| **HTML** | `pages/home.html` | section `#blog` |
| **CSS** | `assets/css/pages/home.css` | lignes **1811 à 1981** |

---

### 5.11 Final CTA Section (Sprint 16)

**Objectif :** Section de conversion finale avec carte 2 colonnes (bénéfices + réassurance) et bandeau de confiance (stats chiffrées).

**Classes CSS clés :** `.main-cta-card`, `.cta-main-grid`, `.cta-left-col`, `.cta-col-title`, `.cta-col-description`, `.cta-benefits-list`, `.benefit-check-icon`, `.cta-reassurance-card`, `.reassurance-title`, `.cta-outcomes-list`, `.outcome-dot-icon`, `.cta-actions-group`, `.cta-trust-banner`, `.cta-trust-item`, `.cta-trust-value`, `.cta-trust-label`

**Responsive :** 1 colonne mobile → 2 colonnes tablette/desktop

### Localisation du code source

| | Fichier | Localisation |
|---|---|---|
| **HTML** | `pages/home.html` | section `#cta` |
| **CSS** | `assets/css/pages/home.css` | lignes **1982 à 2177** |

---

### 5.12 Dashboard HTML/CSS — Illustration Hero Services (Sprint 20)

**Objectif :** Illustration de navigateur/dashboard codée entièrement en HTML/CSS sans aucune image externe, utilisée dans les heroes des pages de service.

**Classes CSS clés :** `.hero-dashboard`, `.hero-dashboard-header`, `.hero-dashboard-dots`, `.hero-dashboard-title-bar`, `.dashboard-url-badge`, `.hero-dashboard-body`, `.dashboard-sidebar`, `.sidebar-item`, `.dashboard-main`, `.dashboard-stats-row`, `.dash-card`, `.dash-card-header`, `.dash-label`, `.dash-value`, `.dash-progress-bar`, `.dash-progress-fill`, `.dash-sparkline`, `.spark-bar`, `.floating-feature-card`, `.feature-badge-icon`, `.feature-card-text`, `.feature-title`, `.feature-sub`, `.code-preview-card`, `.code-line`

**Structure HTML (résumée) :**
```html
<div class="hero-dashboard">
  <div class="hero-dashboard-header">
    <div class="hero-dashboard-dots">
      <span class="dot dot-red"></span>
      <span class="dot dot-yellow"></span>
      <span class="dot dot-green"></span>
    </div>
    <div class="hero-dashboard-title-bar">
      <span class="dashboard-url-badge">votre-entreprise.cg</span>
    </div>
  </div>
  <div class="hero-dashboard-body">
    <div class="dashboard-sidebar">
      <div class="sidebar-item active"></div>
    </div>
    <div class="dashboard-main">
      <div class="dashboard-stats-row">
        <div class="dash-card">
          <div class="dash-card-header">
            <span class="dash-label">Score Vitesse</span>
            <span class="dash-value">98/100</span>
          </div>
          <div class="dash-progress-bar">
            <div class="dash-progress-fill p-99"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```

**Utilisé dans :**
- `pages/services.html` — Hero (Sprint 20)
- `pages/creation-site-web.html` — Hero (Sprint 22)

### Localisation du code source

| | Fichier | Localisation |
|---|---|---|
| **HTML (Services)** | `pages/services.html` | section `.services-hero` |
| **CSS (Services)** | `assets/css/pages/services.css` | section "Dashboard Illustration" |
| **HTML (Création)** | `pages/creation-site-web.html` | section `#hero-service-detail` |
| **CSS (Création)** | `assets/css/pages/creation-site-web.css` | section "Hero Section" |

---

### 5.13 Services Grid — 6 Cartes Expertises (Sprint 21)

**Objectif :** Grille de 6 cartes de services avec icône SVG, titre, description, liste de 3 features avec checkmark, et CTA textuel pointant vers la page dédiée du service.

**Classes CSS clés :** `.services-expertise-section`, `.services-grid`, `.service-card`, `.service-card-title`, `.service-card-desc`, `.service-icon`, `.service-features`, `.service-feature-item`, `.feature-check-icon`, `.service-cta-wrapper`, `.service-cta`

**Bannière CTA sous la grille :** `.services-banner-card`, `.services-banner-body`, `.services-banner-title`, `.services-banner-text`, `.services-banner-actions`

**Responsive :** `.grid .grid-md-2 .grid-lg-3`

**Liens des 6 cartes :**
- Carte 1 → `creation-site-web.html` ✅ (Sprint 22)
- Carte 2 → `wordpress.html` (Sprint 24)
- Carte 3 → `seo.html` (Sprint 25)
- Carte 4 → `refonte-site.html` (Sprint 26)
- Carte 5 → `maintenance.html` (Sprint 27)
- Carte 6 → `audit-conseil.html` (Sprint 28)

### Localisation du code source

| | Fichier | Localisation |
|---|---|---|
| **HTML** | `pages/services.html` | section `#nos-expertises` |
| **CSS** | `assets/css/pages/services.css` | lignes **358 à 588** |

---

### 5.14 Breadcrumb Component (Sprint 20 / 22)

**Objectif :** Fil d'Ariane horizontal indiquant la position dans la hiérarchie du site.

**Classes CSS clés :** `.services-breadcrumb-wrapper`, `.breadcrumb-list`, `.breadcrumb-item`, `.breadcrumb-link`, `.breadcrumb-separator`, `.breadcrumb-item-active`

**Structure HTML :**
```html
<div class="services-breadcrumb-wrapper">
  <div class="container">
    <nav class="breadcrumb" aria-label="Fil d'Ariane">
      <ol class="breadcrumb-list" role="list">
        <li class="breadcrumb-item">
          <a href="index.html" class="breadcrumb-link">Accueil</a>
        </li>
        <li class="breadcrumb-separator" aria-hidden="true"><svg>...</svg></li>
        <li class="breadcrumb-item">
          <a href="services.html" class="breadcrumb-link">Services</a>
        </li>
        <li class="breadcrumb-separator" aria-hidden="true"><svg>...</svg></li>
        <li class="breadcrumb-item breadcrumb-item-active" aria-current="page">
          <span>Création de site web</span>
        </li>
      </ol>
    </nav>
  </div>
</div>
```

> ⚠️ Ces styles existent dans `services.css` ET dans `creation-site-web.css`. Chaque nouvelle page service doit copier ces styles dans sa propre feuille de style — ils n'existent pas dans un fichier composant partagé.

### Localisation du code source

| | Fichier | Localisation |
|---|---|---|
| **CSS (Services)** | `assets/css/pages/services.css` | lignes **1 à 47** |
| **CSS (Création)** | `assets/css/pages/creation-site-web.css` | lignes **1 à 50** |

---

### 5.15 Template Page Service (Sprint 22)

**Objectif :** Template de page de service en 7 sections obligatoires, servant de modèle officiel pour les Sprints 23 à 28.

**7 sections canoniques :**

| # | Section | `id` HTML | Composants utilisés |
|---|---|---|---|
| 1 | Hero | `#hero-service-detail` | Badge, H1, Dashboard Illustration |
| 2 | Pourquoi ce service | `#pourquoi-ce-service` | Section, Grid 4 cartes |
| 3 | Ce qui est inclus | `#ce-qui-est-inclus` | Section, Grid 6 cartes |
| 4 | Notre méthode | `#notre-methode` | Timeline Premium 4 étapes |
| 5 | Pourquoi Aziz Studio | `#pourquoi-aziz-studio` | Section, Grid 4 cartes réassurance |
| 6 | FAQ | `#faq-service` | FAQ Premium Accordion |
| 7 | CTA Final | `#cta-final-service` | Card avec accent strip vertical |

**Classes CSS spécifiques :** `.service-single-hero`, `.service-hero-grid`, `.service-hero-content`, `.service-hero-title`, `.service-hero-description`, `.service-hero-actions`, `.service-hero-visual`, `.service-reason-card`, `.service-feature-card`, `.service-trust-card`, `.service-final-cta-section`, `.service-cta-final-card`, `.service-cta-final-body`, `.service-cta-final-content`, `.service-cta-final-title`, `.service-cta-final-text`, `.service-cta-final-actions`

### Localisation du code source

| | Fichier | Localisation |
|---|---|---|
| **HTML** | `pages/creation-site-web.html` | fichier complet |
| **CSS** | `assets/css/pages/creation-site-web.css` | fichier complet |

---

## 6. Règles de développement

---

> ## ⛔ RÈGLE ABSOLUE
>
> **Avant de créer un nouveau sélecteur CSS ou une nouvelle structure HTML** pour répondre à un besoin visuel (timeline, accordéon, carte, bannière, dashboard, CTA, etc.), **vérifier d'abord dans les sections 4 et 5 de ce document** si un composant équivalent existe déjà.
>
> **Si un composant existe :**
> - il **DOIT** être réutilisé à l'identique
> - mêmes classes CSS, même structure HTML, même logique responsive
> - aucune réécriture partielle, aucune réinterprétation
>
> La création d'un nouveau composant n'est autorisée que si aucun composant existant ne répond au besoin.

---

### 6.1 Variables CSS

- ✅ Utiliser exclusivement les variables de la section 3
- ❌ Ne jamais coder une couleur en dur (`#7c3aed`, `rgba(120,60,220)`)
- ❌ Ne jamais inventer une variable (`--spacing-40px`, `--color-violet`)
- ✅ Transparences : `hsla(var(--color-accent-h), var(--color-accent-s), var(--color-accent-l), 0.1)`

### 6.2 Composants

- ✅ Utiliser `.card`, `.badge`, `.btn`, `.section`, `.grid`, `.container` comme base
- ✅ Étendre par des classes modificatrices sans redéfinir les propriétés de base
- ❌ Ne jamais reconstruire from scratch un composant déjà existant

### 6.3 HTML sémantique

- `<section>` pour les grandes zones, `<article>` pour les cartes répétées, `<nav>` pour la navigation, `<main>` pour le contenu principal
- **Une seule `<h1>` par page**, ensuite `<h2>` pour les sections, `<h3>` pour les cartes
- Attributs ARIA : `aria-label`, `aria-current="page"`, `aria-hidden="true"` sur les éléments décoratifs

### 6.4 Responsive mobile-first

- Styles mobile écrits sans media query
- Extension avec `@media (min-width: 768px)` et `@media (min-width: 1024px)`
- Ne jamais utiliser `@media (max-width: ...)` sauf exception documentée

### 6.5 Accessibilité WCAG 2.1 AA

- Contraste minimum 4.5:1 texte normal, 3:1 grand texte
- Tous les liens ont un libellé explicite ou un `aria-label`
- Images décoratives : `alt=""` ou `aria-hidden="true"`
- Éléments interactifs : `:focus-visible` stylé (ring violet 3px)

### 6.6 SEO

- Chaque page compilée : `<title>` et `<meta name="description">` uniques
- `<h1>` contient le mot-clé principal de la page
- URLs descriptives : `creation-site-web.html`, pas `page1.html`

### 6.7 Performance

- Aucun JavaScript inutile (accordéons via `<details>`, menus via CSS/JS minimal)
- Aucune image externe non nécessaire — utiliser les illustrations HTML/CSS
- Aucune bibliothèque externe (pas de Bootstrap, Tailwind, jQuery)

---

## 7. Checklist avant chaque Sprint

```
□ Ai-je lu les sections 4 et 5 de ce document ?
□ Le composant dont j'ai besoin existe-t-il déjà ?
□ Puis-je réutiliser une classe existante sans en créer une nouvelle ?
□ Les nouveaux sélecteurs CSS sont-ils vraiment nécessaires ?
□ J'utilise uniquement les variables CSS de la section 3 ?
□ La structure HTML respecte-t-elle la hiérarchie sémantique (h1 → h2 → h3) ?
□ L'approche est-elle mobile-first ?
□ Les éléments décoratifs ont-ils aria-hidden="true" ?
□ Les liens ont-ils des libellés accessibles ?
□ Le responsive a-t-il été vérifié sur mobile, tablette et desktop ?
□ Le build a-t-il été exécuté avec python build_index.py ?
□ Le Design System est-il respecté (aucune couleur en dur) ?
```

---

## 8. Historique des composants

| Sprint | Composant | Fichier HTML source | Fichier CSS | Réutilisé dans | Statut |
|---|---|---|---|---|---|
| Sprint 06 | Hero Premium | `pages/home.html` | `home.css` L.1–370 | `home.html` | ✅ |
| Sprint 07 | Secteurs Cards | `pages/home.html` | `home.css` L.371–429 | `home.html` | ✅ |
| Sprint 08 | Bloc Réassurance | `pages/home.html` | `home.css` L.430–539 | `home.html`, `creation-site-web.html` | ✅ |
| Sprint 09 | Services Home Cards | `pages/home.html` | `home.css` L.540–668 | `home.html` | ✅ |
| Sprint 10 | Portfolio / Réalisations Cards | `pages/home.html` | `home.css` L.669–807 | `home.html` | ✅ |
| Sprint 12 | Technologies Cards | `pages/home.html` | `home.css` L.1166–1302 | `home.html` | ✅ |
| Sprint 13 | Témoignages Cards + Stats | `pages/home.html` | `home.css` L.1303–1521 | `home.html` | ✅ |
| Sprint 15 | Blog Cards | `pages/home.html` | `home.css` L.1811–1981 | `home.html` | ✅ |
| Sprint 16 | Final CTA Section | `pages/home.html` | `home.css` L.1982–2177 | `home.html`, `creation-site-web.html` | ✅ |
| Sprint 18 | Timeline Premium (6/4 étapes) | `pages/home.html` | `home.css` L.808–1165 | `home.html`, `creation-site-web.html` | ✅ |
| Sprint 19 | FAQ Premium Accordion | `pages/home.html` | `home.css` L.1522–1810 | `home.html`, `creation-site-web.html` | ✅ |
| Sprint 20 | Hero Services + Dashboard + Breadcrumb | `pages/services.html` | `services.css` L.1–357 | `services.html`, `creation-site-web.html` | ✅ |
| Sprint 21 | Services Grid 6 cartes + Bannière | `pages/services.html` | `services.css` L.358–588 | `services.html` | ✅ |
| Sprint 22 | Template Page Service (7 sections) | `pages/creation-site-web.html` | `creation-site-web.css` | `creation-site-web.html` (Template Sprints 23–28) | ✅ |
| Sprint 40 | Hero Sectoriel | `pages/[secteur]/offre.html` | `components/hero.css` L.1–105 | 9 pages d'offres sectorielles | ✅ |
| Sprint 40 | Pricing / Bloc résumé Sticky | `pages/[secteur]/offre.html` | `components/pricing.css` L.1–110 | 9 pages d'offres sectorielles | ✅ |

---

### 5.13 Hero Sectoriel (Sprint 40)

**Objectif :** Section Hero des pages d'offres sectorielles avec badge, titre, sous-titre, description, CTAs et visuel image réel (`assets/images/secteurs/*.webp`) dans un cadre responsive.

**Classes CSS clés :** `.sector-hero`, `.sector-hero-grid`, `.sector-hero-content`, `.sector-hero-badge-wrapper`, `.sector-hero-title`, `.sector-hero-subtitle`, `.sector-hero-description`, `.sector-hero-actions`, `.sector-hero-visual`, `.sector-hero-image-frame`, `.sector-hero-img`

**Localisation du code source :** `assets/css/components/hero.css`

---

### 5.14 Pricing / Bloc résumé Sticky (Sprint 40)

**Objectif :** Carte de résumé d'offre avec tarif à partir de (250k / 500k FCFA), points forts et bouton d'action vers la page commande. Sticky sur desktop.

**Classes CSS clés :** `.sector-pricing-card`, `.sector-pricing-sticky`, `.sector-pricing-header`, `.sector-pricing-badge`, `.sector-pricing-title`, `.sector-pricing-amount-block`, `.sector-pricing-label`, `.sector-pricing-amount`, `.sector-pricing-features`, `.sector-pricing-feature-item`, `.sector-pricing-cta`, `.sector-pricing-note`

**Localisation du code source :** `assets/css/components/pricing.css`

---

### 5.15 FAQ Sectorielle Accordion (Sprint 40)

**Objectif :** Accordéon de questions/réponses sans JavaScript, basé sur `<details>/<summary>` HTML5 natif. Version allégée du composant FAQ Premium (5.9) : pas d'icône SVG dans un cercle, uniquement un chevron rotatif. Utilisé sur les 9 pages d'offres sectorielles.

**Fichier CSS :** `assets/css/components/faq.css` (120 lignes)

**Classes CSS clés :**

| Classe | Rôle |
|---|---|
| `.faq-section` | Wrapper de section avec padding-top |
| `.faq-accordion-wrapper` | Conteneur de l'accordéon avec margin-top |
| `.faq-accordion` | Flex column, gap entre items |
| `.faq-item` | `<details>` — card avec bordure, radius, transition |
| `.faq-item:hover` | Bordure accent semi-transparente |
| `.faq-item[open]` | Bordure accent + glow doux violet |
| `.faq-summary` | `<summary>` — flex row, padding, cursor pointer |
| `.faq-question` | Zone texte (flex: 1) |
| `.faq-question-title` | H3 — font-heading, weight-700, couleur accent si `[open]` |
| `.faq-chevron` | SVG chevron — rotate(180deg) si `[open]` |
| `.faq-answer` | Zone réponse — border-top, padding bottom |
| `.faq-answer-text` | Texte réponse — font-size-base, color-text-secondary |

**Différence avec le composant FAQ Premium (5.9) :**
- Pas d'icône SVG dans un cercle à gauche de la question
- Pas de `.faq-link` en pied de réponse
- Structure HTML plus légère, adaptée aux pages secondaires

**Structure HTML minimale :**
```html
<div class="faq-section">
  <div class="section-header">
    <span class="badge badge-secondary">❓ Questions fréquentes</span>
    <h2 class="section-title">Foire aux questions — {Secteur}</h2>
  </div>
  <div class="faq-accordion-wrapper">
    <div class="faq-accordion">
      <details class="faq-item card" open>
        <summary class="faq-summary">
          <div class="faq-question">
            <h3 class="faq-question-title">Question ?</h3>
          </div>
          <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor"
               stroke-width="2" aria-hidden="true">
            <polyline points="6 9 12 15 18 9"></polyline>
          </svg>
        </summary>
        <div class="faq-answer">
          <p class="faq-answer-text">Réponse.</p>
        </div>
      </details>
    </div>
  </div>
</div>
```

**Chargement :** Via `extra_css` dans `build_index.py`, entre `pricing.css` et `secteurs.css`.

**Pages utilisant ce composant :**
- `hotel.html`, `restaurant.html`, `immobilier.html`, `clinique.html`
- `cabinet-medical.html`, `cabinet-dentaire.html`, `pharmacie.html`
- `salon-beaute.html`, `voyage.html`

---

## 9. Dette technique connue

> [!WARNING]
> **Duplication CSS : `.blog-card` (Sprint 37)**  
> Les styles des cartes de blog existent en double dans :
> - `assets/css/pages/home.css` (lignes 1811-1981)
> - `assets/css/pages/blog.css` (copie exacte effectuée lors du Sprint 37)
> 
> *Action requise :* Lors d'un futur sprint de refactoring, extraire ces règles dans un fichier partagé `assets/css/components/card-blog.css` et nettoyer `home.css` et `blog.css`.

---

## 10. Mise à jour continue du Design System

# Ce document est la source unique de vérité du projet

À chaque fois qu'un nouveau composant réutilisable est créé (Sprints 23–28 et au-delà), **ce document doit être mis à jour immédiatement**, avant que le Sprint ne soit considéré comme terminé.

### Pour chaque nouveau composant, ajouter en section 5 :

- Nom du composant
- Objectif fonctionnel
- Classes CSS principales (liste exhaustive)
- Structure HTML minimale annotée
- Comportement responsive (tableau des breakpoints)
- Fichier HTML de référence avec numéro de section
- Fichier CSS de référence avec plage de lignes
- Liste des pages où il est utilisé

### Pour chaque nouveau Sprint, mettre à jour :

- Le tableau de la **section 8** (historique)
- La **checklist section 7** si de nouvelles règles émergent
- La **section 3** si de nouvelles variables CSS sont créées (à ajouter d'abord dans `assets/css/base/variables.css`)

> Ce document évite la recréation inutile de composants déjà existants et garantit la cohérence visuelle sur l'ensemble des pages présentes et futures du projet Aziz Studio Digital V2.
