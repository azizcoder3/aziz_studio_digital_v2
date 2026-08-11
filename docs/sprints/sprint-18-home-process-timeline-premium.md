# Sprint 18 — Home Process Timeline Premium

## Contexte

La page d'accueil est entièrement développée et validée.

La section **"Notre méthode"** fonctionne correctement mais son rendu actuel, basé sur des cartes indépendantes, ne met pas suffisamment en valeur la progression naturelle d'un projet.

L'objectif est de transformer cette section en une véritable **timeline premium**, inspirée des meilleures agences web et plateformes SaaS modernes, tout en restant fidèle à l'identité visuelle d'Aziz Studio Digital.

Cette refonte concerne uniquement cette section.

---

# Objectif

Créer une timeline élégante illustrant les différentes étapes d'un projet.

Le visiteur doit comprendre instantanément qu'il s'agit d'un processus clair, structuré et maîtrisé.

Le rendu doit évoquer :

- professionnalisme
- confiance
- méthode
- accompagnement

sans perdre l'identité graphique actuelle.

---

# Inspiration

S'inspirer de la maquette fournie.

Le rendu ne doit pas être copié pixel par pixel.

Il doit simplement reprendre les principes UX :

- ligne de progression
- étapes reliées
- lecture fluide
- design minimaliste
- forte hiérarchie visuelle

Tout en conservant l'univers Aziz Studio Digital.

---

# Fichiers autorisés

Modifier uniquement :

- pages/home.html
- assets/css/pages/home.css

Aucun autre fichier.

---

# Contenu

Conserver :

- le badge
- le titre H2
- le sous-titre
- les textes des étapes
- les liens éventuels
- les mots-clés SEO

Ne modifier aucun contenu rédactionnel.

---

# Structure Desktop

Créer une timeline horizontale.

Disposition :

○────────○────────○────────○────────○────────○

01 02 03 04 05 06

Titre

Description

Chaque étape comprend :

- un cercle numéroté
- un titre
- une description

Les étapes sont reliées par une ligne continue.

La ligne traverse uniquement les cercles.

Elle ne passe jamais sur les textes.

---

# Apparence

Chaque cercle :

- parfaitement rond
- centré
- bordure utilisant les couleurs du Design System
- numéro centré

La ligne :

- fine
- élégante
- discrète

Les titres :

- parfaitement alignés

Les descriptions :

- largeur uniforme

Toutes les étapes doivent avoir exactement la même largeur.

---

# Responsive

## Desktop

Timeline horizontale.

6 étapes alignées.

---

## Tablette

Timeline horizontale si l'espace le permet.

Sinon retour automatique sur deux lignes.

Les connexions doivent rester cohérentes.

---

## Mobile

Transformation complète.

Timeline verticale.

Exemple :

○

01

Découverte

Description

│

○

02

Proposition

Description

│

○

03

...

Chaque étape reste reliée.

Lecture naturelle du haut vers le bas.

---

# Design System

Utiliser exclusivement :

- var(--color-primary)
- var(--color-accent)
- var(--color-border)
- var(--color-text-primary)
- var(--color-text-secondary)
- var(--spacing-\*)
- var(--radius-\*)
- var(--shadow-\*)
- var(--transition-\*)

Interdiction absolue :

- couleurs codées en dur
- tailles fixes incohérentes
- nouvelles variables

---

# Technique

Autorisé :

- Flexbox
- Grid
- ::before
- ::after
- position:absolute
- z-index

Interdit :

- JavaScript
- Canvas
- SVG supplémentaires
- bibliothèque externe

---

# Micro-interactions

Au survol d'une étape :

- légère élévation
- bordure accentuée
- transition douce

Aucune animation excessive.

---

# Accessibilité

Respect WCAG AA.

La ligne est décorative.

Ne pas modifier :

- la hiérarchie H2/H3
- la navigation clavier
- les lecteurs d'écran

---

# SEO

Aucun changement.

Conserver tous les contenus existants.

---

# Contraintes

Respecter l'identité Aziz Studio Digital :

- ambiance premium
- moderne
- élégante
- minimaliste
- professionnelle

La section doit sembler appartenir naturellement au reste du site.

Le visiteur ne doit pas avoir l'impression qu'elle provient d'un autre template.

---

# Critères d'acceptation

✓ Timeline horizontale Desktop

✓ Timeline verticale Mobile

✓ Étapes parfaitement alignées

✓ Ligne de progression visible

✓ Cercles numérotés

✓ Design cohérent avec Aziz Studio Digital

✓ Aucun changement SEO

✓ Aucun JavaScript

✓ Aucun autre fichier modifié

✓ Responsive validé

✓ Accessibilité préservée

✓ Utilisation exclusive du Design System

---

# Livrables

Modifier uniquement :

- pages/home.html
- assets/css/pages/home.css

Puis fournir un rapport comprenant :

- fichiers modifiés
- structure HTML retenue
- nouvelles classes CSS
- responsive
- accessibilité
- choix UX
- conformité Design System
- validation complète des critères d'acceptation
