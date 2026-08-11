# Sprint 04 — UI Components System (Foundation)

Version : 1.0

Projet : Aziz Studio Digital V2

Type : Design System

Priorité : Très Haute

Dépendances :

- Sprint 01 — Foundation ✅
- Sprint 02 — Header System ✅
- Sprint 03 — Footer System ✅

---

# Objectif

Créer les composants universels qui seront utilisés dans l'ensemble du projet.

Ces composants constituent le Design System officiel d'Aziz Studio Digital V2.

Ils devront être réutilisables, accessibles, responsives et faciles à maintenir.

Ils ne doivent contenir aucune logique métier spécifique à une page.

---

# Architecture

Créer uniquement les fichiers suivants :

assets/css/components/

- button.css
- card.css
- badge.css
- section.css
- container.css
- grid.css
- form.css

Ne modifier aucun autre composant.

---

# Composant 1 — Button

Créer un système de boutons.

Prévoir les variantes suivantes :

- Primary
- Secondary
- Outline
- Ghost
- Text

États :

- Normal
- Hover
- Focus
- Active
- Disabled

Les boutons doivent utiliser exclusivement les variables CSS du Sprint 01.

---

# Composant 2 — Card

Créer un composant Card générique.

Prévoir :

- Image (optionnelle)
- Titre
- Description
- Contenu libre
- Pied de carte (optionnel)

États :

- Normal
- Hover

Le composant doit être réutilisable pour :

- Portfolio
- Blog
- Services
- Témoignages
- Tarifs

---

# Composant 3 — Badge

Créer un composant Badge.

Prévoir plusieurs variantes :

- Primary
- Secondary
- Success
- Warning
- Danger

Le badge doit pouvoir être utilisé sur toutes les pages.

---

# Composant 4 — Section

Créer une classe utilitaire pour les sections.

Prévoir :

- Espacement vertical
- Largeur maximale
- Alignement
- Variantes si nécessaire

Toutes les sections du site utiliseront ce composant.

---

# Composant 5 — Container

Créer le conteneur principal du site.

Prévoir :

- Largeur maximale
- Marges automatiques
- Padding responsive

Toutes les pages devront utiliser ce conteneur.

---

# Composant 6 — Grid

Créer un système de grille flexible.

Prévoir :

- 2 colonnes
- 3 colonnes
- 4 colonnes

Le système doit être responsive.

Desktop

Tablet

Mobile

---

# Composant 7 — Form

Créer les styles communs pour :

- Input
- Textarea
- Select
- Label
- Checkbox
- Radio
- Boutons de formulaire

États :

- Focus
- Disabled
- Error
- Success

---

# Responsive

Tous les composants doivent fonctionner sur :

- Mobile
- Tablet
- Desktop

Approche Mobile First obligatoire.

---

# Accessibilité

Tous les composants doivent respecter :

- Focus visible
- Contrastes suffisants
- Navigation clavier
- États accessibles

---

# Performance

- Aucun framework CSS
- Aucun plugin
- Aucun code inutile
- CSS optimisé
- Réutilisation maximale

---

# Contraintes

Ne pas développer :

- Hero
- Home
- Portfolio
- Contact
- Blog
- Footer
- Header

Créer uniquement les composants CSS demandés.

---

# Livrables

Créer uniquement :

assets/css/components/

- button.css
- card.css
- badge.css
- section.css
- container.css
- grid.css
- form.css

---

# Critères d'acceptation

Le Sprint est terminé lorsque :

✔ Tous les composants existent

✔ Tous utilisent les variables CSS

✔ Tous sont responsives

✔ Tous sont accessibles

✔ Aucun code dupliqué

✔ Aucun style spécifique à une page

✔ Aucun composant métier

---

# Résultat attendu

À la fin de ce Sprint, Aziz Studio Digital V2 dispose d'un Design System CSS complet permettant de construire toutes les pages du site avec des composants réutilisables.

Fin du Sprint 04 — UI Components System (Foundation).
