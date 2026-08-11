# Sprint 02 — Header System (Foundation)

Version : 1.0

Projet : Aziz Studio Digital V2

---

# Objectif

Concevoir et développer le Header officiel d'Aziz Studio Digital.

Ce Header sera utilisé sur toutes les pages du site.

Il doit être moderne, rapide, responsive, accessible et facilement maintenable.

Le Header est un composant système.

Il ne doit jamais être redéveloppé dans une autre page.

---

# Architecture

Le composant devra être créé dans :

components/header.html

Les styles devront être créés dans :

assets/css/components/header.css

Le JavaScript devra être créé dans :

assets/js/modules/header.js

---

# Fonctionnalités

Le Header doit contenir :

- Logo Aziz Studio Digital
- Navigation principale
- Bouton "Demander un devis"
- Bouton menu mobile
- Menu responsive
- Header Sticky
- Animation au scroll
- État actif du menu
- Accessibilité clavier
- Compatible Mobile First

---

# Navigation

La navigation principale doit contenir :

- Accueil
- Services
- Solutions
- Portfolio
- Blog
- Tarifs
- À propos
- Contact

Le lien correspondant à la page active devra être identifiable visuellement.

---

# Logo

Le logo doit :

- être cliquable
- rediriger vers l'accueil
- posséder un texte alternatif
- rester lisible sur toutes les tailles d'écran

---

# Bouton principal (CTA)

Créer un bouton principal :

Texte :

"Demander un devis"

Il devra être clairement mis en avant.

---

# Responsive

Desktop

- Logo à gauche
- Navigation centrée ou légèrement décalée
- CTA à droite

Tablet

- Navigation simplifiée si nécessaire

Mobile

- Logo
- Bouton Menu
- Navigation dans un panneau mobile

---

# Header Sticky

Au défilement :

- le Header reste visible
- la hauteur peut être légèrement réduite
- une ombre discrète apparaît
- la transition doit être fluide

---

# Accessibilité

Respecter les bonnes pratiques :

- navigation clavier
- aria-label
- aria-expanded
- aria-controls
- contraste suffisant
- focus visible

---

# SEO

Utiliser :

<header>

<nav>

<ul>

<li>

<a>

Le Header doit être entièrement sémantique.

---

# Performance

- Aucun framework
- Aucun plugin
- JavaScript minimal
- Animation optimisée
- Pas de bibliothèque externe

---

# Design

Le Header doit reprendre l'identité visuelle d'Aziz Studio Digital.

Il doit inspirer :

- professionnalisme
- modernité
- confiance

---

# Contraintes

Ne pas développer :

- Footer
- Hero
- Home
- Sections

Ne développer que le Header.

---

# Livrables

Créer uniquement :

components/header.html

assets/css/components/header.css

assets/js/modules/header.js

Ne modifier aucun autre composant.

---

# Critères d'acceptation

Le Sprint est terminé lorsque :

✔ Header responsive

✔ Navigation fonctionnelle

✔ Menu mobile fonctionnel

✔ Sticky Header opérationnel

✔ Bouton CTA visible

✔ Accessibilité respectée

✔ SEO respecté

✔ Aucun bug JavaScript

Fin du Sprint 02 Foundation.
