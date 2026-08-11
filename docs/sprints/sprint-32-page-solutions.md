# Sprint 32 — Construction de la page Solutions

## Objectif

Créer la page **Solutions** du site Aziz Studio Digital.

Cette page devient la porte d'entrée principale vers l'ensemble des expertises de l'agence. Contrairement à la page **Services**, qui présente les prestations individuellement, la page **Solutions** doit guider les visiteurs vers la solution la plus adaptée à leur besoin.

Cette page servira également de page de maillage interne vers :

- Création de site web
- Développement WordPress
- SEO & Référencement
- Refonte de site
- Maintenance & Support
- Audit & Conseil digital
- Contact
- Portfolio

Elle devra respecter intégralement l'architecture du projet définie dans :

- docs/project-architecture.md
- docs/design-system-components.md
- docs/contributing.md

---

# Documents obligatoires à consulter

Avant toute modification, lire intégralement :

- docs/project-architecture.md
- docs/design-system-components.md
- docs/contributing.md

Ne créer aucun composant déjà documenté.

---

# Travail demandé

Créer :

pages/solutions.html

Créer :

assets/css/pages/solutions.css

Mettre à jour :

build_index.py

pour générer :

solutions.html

Mettre à jour :

header.html

afin que le menu "Solutions" pointe vers la nouvelle page.

---

# Architecture de la page

La structure devra reprendre l'organisation générale des pages Services tout en étant adaptée à une page de navigation.

La page comportera **8 sections**.

---

# Section 1 — Hero

Réutiliser le Hero Premium existant.

Contenu attendu :

Badge :

Nos solutions digitales

H1 :

Des solutions web conçues pour développer votre activité au Congo

Texte :

Présenter Aziz Studio Digital comme partenaire capable d'accompagner une entreprise à chaque étape de sa transformation digitale grâce à une gamme complète de solutions.

CTA primaire :

Parler de votre projet

CTA secondaire :

Voir nos réalisations

Hero Dashboard :

Réutiliser le Hero Dashboard Premium.

Adapter uniquement les métriques.

Exemple :

+250 projets

99 % satisfaction

6 expertises

---

# Section 2 — Choisissez votre solution

Créer une grille présentant les 6 solutions principales.

Réutiliser uniquement les cartes existantes.

Une carte par solution :

- Création de site web
- Développement WordPress
- SEO & Référencement
- Refonte
- Maintenance
- Audit digital

Chaque carte doit contenir :

- icône
- titre
- court texte
- bouton

Libellés :

Découvrir cette solution

Chaque carte doit pointer vers la page correspondante.

---

# Section 3 — Pourquoi choisir Aziz Studio Digital

Réutiliser les cartes de réassurance.

4 cartes.

Exemples :

Expertise

Accompagnement

Performance

Résultats

---

# Section 4 — Notre méthode

Réutiliser exactement la Timeline Premium.

Adapter le contenu.

4 étapes :

Découverte

Analyse

Réalisation

Suivi

---

# Section 5 — Nos secteurs d'activité

Créer une grille.

Réutiliser les cartes existantes.

Exemples :

PME

Artisans

Commerçants

Associations

Institutions

Entreprises

Chaque carte contient :

titre

description

---

# Section 6 — Questions fréquentes

Réutiliser la FAQ Premium.

5 questions.

Exemples :

Comment choisir la bonne solution ?

Puis-je commencer petit ?

Peut-on faire évoluer mon site ?

Travaillez-vous uniquement au Congo ?

Comment démarrer ?

---

# Section 7 — CTA final

Réutiliser le CTA Premium.

Badge :

Parlons de votre projet

Titre :

Trouvons ensemble la solution adaptée à votre activité

Bouton principal :

Parler de votre projet

Bouton secondaire :

Voir nos réalisations

---

# Section 8 — Maillage interne

Créer une section dédiée aux liens internes.

Objectif :

Renforcer le SEO.

Présenter :

- les Services
- le Portfolio
- les Tarifs
- le Blog (préparer le lien)
- Contact

Réutiliser les cartes existantes.

---

# SEO

Respecter strictement :

Title :

≤60 caractères

1 seul séparateur |

Proposition :

Solutions digitales au Congo | Aziz Studio Digital

Meta description :

≤160 caractères

Unique.

H1 unique.

Hiérarchie H2/H3.

Breadcrumb :

Accueil

>

Solutions

aria-current obligatoire.

---

# Accessibilité

Respecter WCAG 2.1 AA.

Navigation clavier.

Focus visibles.

ARIA.

details/summary pour la FAQ.

alt sur toutes les illustrations.

---

# CSS

Créer :

assets/css/pages/solutions.css

Ordre de chargement :

services.css

↓

creation-site-web.css

↓

solutions.css

Aucun @import.

Aucune duplication.

Utiliser exclusivement les tokens existants.

---

# Build

Mettre à jour build_index.py.

Compiler :

solutions.html

Aucune régression.

---

# Contraintes

Réutiliser exclusivement les composants existants.

Ne créer aucun composant Premium.

Ne modifier ni le Design System ni l'architecture.

Respecter :

project-architecture.md

design-system-components.md

contributing.md

---

# Critères d'acceptation

✓ pages/solutions.html créé

✓ assets/css/pages/solutions.css créé

✓ build_index.py mis à jour

✓ solutions.html compilé

✓ lien du menu mis à jour

✓ Hero Premium réutilisé

✓ Hero Dashboard réutilisé

✓ Timeline Premium réutilisée

✓ FAQ Premium réutilisée

✓ CTA Premium réutilisé

✓ Aucun nouveau composant

✓ SEO conforme

✓ WCAG conforme

✓ Responsive validé

✓ Aucun @import

✓ Documentation respectée

✓ Rapport complet fourni
