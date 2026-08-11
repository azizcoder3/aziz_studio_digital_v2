# Sprint 33 — Construction de la page Portfolio

## Objectif

Construire la page **Portfolio** d'Aziz Studio Digital V2.

Cette page constitue la vitrine officielle des réalisations de l'agence.

Elle doit permettre :

- de présenter les projets réalisés ;
- de renforcer la crédibilité de l'agence ;
- d'améliorer le maillage interne du site ;
- d'alimenter les CTA présents sur les pages Services ;
- de préparer les futures fiches projets (Sprint ultérieur).

Cette page doit respecter intégralement :

- docs/design-system-components.md
- docs/project-architecture.md
- docs/contributing.md

Aucun nouveau composant ne doit être créé.

---

# Objectifs fonctionnels

Créer une page Portfolio moderne comprenant :

- Hero Premium
- Hero Dashboard
- présentation des réalisations
- grille de projets
- statistiques
- méthodologie
- témoignages
- FAQ
- CTA final
- navigation rapide

Le visiteur doit comprendre immédiatement :

- le niveau de qualité des réalisations
- les domaines d'expertise
- les résultats obtenus
- pourquoi faire confiance à Aziz Studio Digital

---

# Architecture de la page

La page doit comporter exactement les sections suivantes.

---

## Section 1

Hero Premium

Réutiliser intégralement :

service-single-hero

service-hero-grid

service-hero-content

Hero Dashboard Premium

Adapter uniquement le contenu.

Ne jamais modifier le composant.

---

Contenu :

Badge

```
Notre portfolio
```

H1

```
Découvrez quelques réalisations conçues pour développer les entreprises au Congo
```

Texte

Présentation du portfolio.

Deux boutons :

```
Parler de votre projet
```

```
Voir nos services
```

---

Dashboard :

Exemple :

```
+120

Projets réalisés
```

```
98%

Clients satisfaits
```

```
12

Secteurs accompagnés
```

Badge flottant

```
Portfolio Premium

Réalisations vérifiées
```

---

## Section 2

Nos réalisations

Réutiliser :

service-reason-card

Créer une grille responsive.

6 cartes.

Chaque carte comporte :

- image placeholder
- catégorie
- titre
- description
- technologies
- bouton

Texte bouton :

```
Voir le projet
```

---

Catégories :

Création Web

WordPress

SEO

Refonte

Maintenance

Audit Digital

---

## Section 3

Nos résultats

Réutiliser :

cards

Créer une grille de statistiques.

Exemples :

```
120+

Projets réalisés
```

```
98%

Clients satisfaits
```

```
35%

Croissance moyenne
```

```
24h

Support
```

---

## Section 4

Pourquoi nos clients nous choisissent

Réutiliser :

service-reason-card

Créer 4 cartes.

---

## Section 5

Notre processus

Réutiliser intégralement :

Timeline Premium

4 étapes.

Découverte

Conception

Développement

Suivi

Aucune modification du composant.

---

## Section 6

FAQ

Réutiliser intégralement :

FAQ Premium

5 questions.

Aucun JavaScript supplémentaire.

Utiliser uniquement :

details

summary

---

## Section 7

CTA Final

Réutiliser :

service-final-cta-section

Deux boutons.

```
Parler de votre projet
```

```
Découvrir nos services
```

---

## Section 8

Navigation rapide

Même structure que Solutions.

4 cartes :

Services

Tarifs

Contact

À propos

---

# Breadcrumb

Accueil

>

Portfolio

Respecter :

aria-current="page"

---

# SEO

Title

Maximum :

60 caractères

Exactement :

1 pipe |

Meta description

Maximum :

160 caractères

Unique.

1 seul H1.

---

# Responsive

Tester :

375 px

768 px

1024 px

1440 px

Aucun débordement.

---

# WCAG

Respecter :

WCAG 2.1 AA

Navigation clavier

Contrastes

Focus visible

aria-current

aria-hidden

details

summary

---

# CSS

Créer :

assets/css/pages/portfolio.css

Sans :

@import

Ordre :

services.css

↓

creation-site-web.css

↓

portfolio.css

---

# Build

Créer :

pages/portfolio.html

Ajouter :

portfolio.html

dans :

build_index.py

La page compilée doit être générée à la racine.

---

# Header

Le menu :

Portfolio

doit devenir actif.

---

# Footer

Tous les liens doivent fonctionner.

Aucun lien cassé.

---

# Documentation

Ne modifier aucun des fichiers suivants :

docs/design-system-components.md

docs/project-architecture.md

docs/contributing.md

---

# Interdictions

Ne jamais créer :

nouveau composant

nouvelle architecture

nouvelle grille

nouveau Hero

nouvelle Timeline

nouvelle FAQ

nouveau CTA

Ne jamais modifier les composants Premium.

Ils doivent être réutilisés.

---

# Critères d'acceptation

✓ Hero Premium identique aux pages Services

✓ Hero Dashboard réutilisé

✓ 8 sections présentes

✓ 6 cartes Portfolio

✓ Timeline Premium conforme

✓ FAQ Premium conforme

✓ CTA Final conforme

✓ Navigation rapide conforme

✓ Responsive validé

✓ WCAG validé

✓ SEO validé

✓ build_index.py compilé

✓ portfolio.html généré

✓ Aucun @import

✓ Aucun nouveau composant

✓ Documentation inchangée

---

# Livrables attendus

Créer :

pages/portfolio.html

assets/css/pages/portfolio.css

Modifier :

build_index.py

Générer :

portfolio.html

Produire un rapport final indiquant :

- fichiers créés
- fichiers modifiés
- validation SEO
- validation WCAG
- validation Responsive
- validation Build
- composants réutilisés
- confirmation qu'aucun nouveau composant n'a été créé.
