# Sprint 20 — Services Foundation & Hero

## Objectif

Créer les fondations de la page **Services** (`services.html`) ainsi que son Hero.

Cette page doit immédiatement expliquer :

- ce que fait Aziz Studio Digital,
- pour qui,
- quels bénéfices,
- et orienter vers les différents services.

Cette première version ne contient que :

- Hero
- Breadcrumb
- Introduction

Les autres sections arriveront dans les prochains sprints.

---

# Fichiers autorisés

Modifier uniquement :

pages/services.html

assets/css/pages/services.css

Aucun autre fichier.

---

# Design System

Réutiliser exclusivement :

.section

.container

.grid

.card

.badge

.btn

Aucun nouveau composant générique.

---

# Structure

La page doit commencer par :

```
Accueil
    >
Services
```

(Breadcrumb)

Puis

Hero Services

---

# Hero

Le Hero doit contenir :

Badge

🛠️ Nos Services

H1

Des solutions web pensées
pour développer votre entreprise.

Texte

Présentation de l'agence et de son approche.

Le texte doit intégrer naturellement :

création de site web

développement web

SEO

WordPress

entreprise

Congo

Deux boutons

Demander un devis

Voir nos réalisations

---

# Layout

Desktop

2 colonnes

gauche :

texte

droite :

illustration

Mobile

1 colonne

illustration sous le texte

---

# Illustration

Créer un visuel HTML/CSS premium.

Ne pas utiliser d'image.

Le visuel peut représenter :

ordinateur

dashboard

cartes

wireframe

interface

Le style doit rester cohérent avec le Hero de la Home.

---

# Cartes d'introduction

Sous le Hero

Créer une grille

3 cartes

Chaque carte présente :

Création de sites web

SEO & visibilité Google

Maintenance & évolution

Chaque carte contient :

petite icône SVG

H3

court texte

lien

Découvrir →

---

# Responsive

Desktop

3 colonnes

Tablette

2 colonnes

Mobile

1 colonne

---

# Accessibilité

Hiérarchie

H1

H2

H3

SVG décoratifs

aria-hidden="true"

Boutons accessibles

---

# SEO

Le Hero doit intégrer naturellement :

création de site web

agence web

développement web

SEO

WordPress

entreprise

Congo

visibilité Google

Sans sur-optimisation.

---

# Nouveaux sélecteurs CSS

Créer uniquement ceux nécessaires.

Exemple :

.services-hero

.services-hero-grid

.services-hero-content

.services-hero-visual

.services-intro-grid

.service-intro-card

.service-icon

.hero-dashboard

.hero-dashboard-header

.hero-dashboard-body

---

# Style

Respecter l'identité Aziz Studio Digital :

fond sombre

surfaces premium

bordures discrètes

violet principal

ombres légères

coins arrondis

aucune couleur codée en dur

uniquement les variables CSS existantes.

---

# Interdictions

Aucun JavaScript

Aucune librairie

Aucun framework

Aucun style inline

Aucune image externe

Aucune modification hors des fichiers autorisés

---

# Critères d'acceptation

✓ Hero complet

✓ Breadcrumb

✓ H1 unique

✓ Illustration HTML/CSS

✓ Deux CTA

✓ Trois cartes d'introduction

✓ Responsive

✓ Accessibilité

✓ SEO

✓ Design System respecté

✓ Aucun JavaScript

---

# Livrable attendu

À la fin fournir un rapport contenant :

- fichiers modifiés
- nouveaux sélecteurs CSS
- composants Design System utilisés
- choix techniques
- responsive
- SEO
- accessibilité
- validation des critères d'acceptation
