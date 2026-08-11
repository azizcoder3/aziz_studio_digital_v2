# Sprint 23 — Page Service WordPress

## Objectif

Créer la page dédiée au service **Développement WordPress** en réutilisant intégralement le template validé au Sprint 22.

Aucun nouveau composant ne doit être créé.

Le travail consiste uniquement à adapter le contenu au service WordPress.

---

# Contexte

Le Sprint 22 a validé :

- l'architecture des pages services ;
- le template officiel ;
- les composants Premium réutilisables ;
- le document de référence :

docs/design-system-components.md

Cette documentation est désormais la source officielle du projet.

Avant toute modification, l'agent DOIT la consulter.

---

# Lecture obligatoire

Avant de commencer :

Lire intégralement :

docs/design-system-components.md

Objectif :

- identifier les composants existants ;
- vérifier si un composant répond déjà au besoin ;
- réutiliser uniquement les composants existants.

Aucun composant ne doit être recréé.

---

# Base de travail

Utiliser comme point de départ :

pages/creation-site-web.html

Cette page constitue désormais le template officiel.

La structure HTML doit être conservée à l'identique.

Même sections.

Même ordre.

Même composants.

Même architecture.

---

# Fichiers autorisés

pages/wordpress.html

assets/css/pages/wordpress.css

pages/services.html

build_index.py

docs/design-system-components.md
(seulement si un nouveau composant est réellement créé)

Aucun autre fichier.

---

# Sections obligatoires

Conserver exactement les 7 sections du template.

## 1 Hero

Adapter :

- Badge
- Breadcrumb
- H1
- texte
- CTA
- illustration HTML/CSS (contenu WordPress uniquement)

---

## 2 Pourquoi choisir WordPress

4 cartes.

Exemples :

- Gestion autonome
- Flexibilité
- Évolutivité
- Performance

---

## 3 Ce qui est inclus

6 cartes.

Par exemple :

- Installation WordPress
- Thème sur mesure
- Plugins essentiels
- Sécurité
- Optimisation SEO
- Formation

---

## 4 Notre méthode

Réutiliser EXACTEMENT :

Timeline Premium

Aucune modification structurelle.

Changer uniquement :

- les titres
- les textes

---

## 5 Pourquoi Aziz Studio Digital

Réutiliser les mêmes cartes.

Adapter uniquement :

- les arguments
- les textes

---

## 6 FAQ

Réutiliser EXACTEMENT :

FAQ Premium Accordion

Ne rien modifier.

Changer uniquement :

- les questions
- les réponses

Prévoir 5 questions spécifiques à WordPress.

---

## 7 CTA Final

Réutiliser le composant existant.

Adapter :

- titre
- texte
- boutons

Les CTA doivent être spécifiques à WordPress.

Interdiction :

"En savoir plus"

Préférer par exemple :

- Demander un devis WordPress
- Discuter de votre projet WordPress

---

# SEO

Créer :

title unique

meta description unique

H1 unique

Intégrer naturellement :

- WordPress
- développement WordPress
- création de site WordPress
- CMS WordPress
- entreprise
- Congo
- agence web
- SEO

---

# Responsive

Conserver exactement le comportement du template.

Aucune modification responsive.

---

# Accessibilité

Conserver :

- aria
- hiérarchie Hn
- contrastes
- navigation clavier

---

# Réutilisation obligatoire

Tous les composants Premium doivent être réutilisés.

Notamment :

Timeline Premium

FAQ Accordion

Cards

CTA Banner

Buttons

Badges

Grid

Section Header

Hero

Aucun composant ne doit être recréé.

---

# Mise à jour de la page Services

Mettre à jour :

pages/services.html

Le bouton de la carte WordPress doit pointer vers :

wordpress.html

---

# Documentation

Ne modifier :

docs/design-system-components.md

QUE si un nouveau composant réutilisable est créé.

Normalement :

aucune modification.

---

# Build

Mettre à jour :

build_index.py

afin de générer :

wordpress.html

à la racine du projet.

---

# Critères d'acceptation

✓ Même template que Sprint 22

✓ Aucun nouveau composant

✓ Réutilisation complète du Design System

✓ Responsive identique

✓ SEO spécifique WordPress

✓ CTA spécifiques

✓ FAQ spécifique

✓ Timeline réutilisée

✓ build fonctionnel

✓ lien Services → WordPress fonctionnel

✓ aucune régression

✓ aucun autre fichier modifié
