# Sprint 25 — Page Service Refonte de Site Web

## Objectif

Créer la page **Refonte de Site Web** en réutilisant intégralement le template officiel validé au Sprint 22 (`creation-site-web.html`).

⚠ Ce sprint est un sprint de contenu.

Aucun nouveau composant ne doit être créé.

Toute la structure HTML du template doit être conservée.

---

# Contexte

Le Design System officiel est documenté dans :

docs/design-system-components.md

Avant toute modification :

- lire le document ;
- consulter les sections 4, 5 et 6 ;
- appliquer la règle absolue de réutilisation.

Aucun composant existant ne peut être recréé.

---

# Architecture

Créer :

pages/
└── refonte-site.html

Créer :

assets/css/pages/
└── refonte-site.css

Compiler ensuite :

refonte-site.html

à la racine via :

build_index.py

---

# Base obligatoire

Copier :

pages/creation-site-web.html

Conserver exactement les 7 sections :

1. Hero
2. Pourquoi ce service
3. Ce qui est inclus
4. Notre méthode
5. Pourquoi Aziz Studio Digital
6. FAQ
7. CTA Final

Aucune modification de structure.

---

# CSS

Ne jamais utiliser :

@import

Le build doit charger :

```html
<link rel="stylesheet" href="assets/css/pages/creation-site-web.css" />
<link rel="stylesheet" href="assets/css/pages/refonte-site.css" />
```

Le fichier :

refonte-site.css

contient uniquement les adaptations spécifiques.

---

# Section 1 — Hero

Badge :

Refonte de Site Web

H1 :

Modernisez votre site web pour gagner en performance et en crédibilité

Texte :

Adapter entièrement au service de refonte.

Mettre en avant :

- modernisation
- expérience utilisateur
- performances
- responsive
- SEO
- image professionnelle

CTA principaux

Bouton 1 :

Demander un devis Refonte

Bouton 2 :

Voir nos réalisations

Conserver exactement :

- Hero Premium
- Dashboard HTML/CSS
- mêmes composants

---

# Section 2 — Pourquoi refaire son site ?

Créer 4 cartes :

• Site devenu obsolète

• Faible taux de conversion

• Mauvaise expérience mobile

• Performances insuffisantes

Réutiliser exactement les cartes Premium.

---

# Section 3 — Ce qui est inclus

Créer 6 cartes :

- Audit complet de l'existant
- Nouveau design UX/UI
- Migration des contenus
- Redirections SEO
- Optimisation des performances
- Tests & mise en ligne

Modifier uniquement les textes.

---

# Section 4 — Notre méthode

Réutiliser exactement :

Timeline Premium

4 étapes :

1.

Audit de l'existant

2.

Conception de la nouvelle interface

3.

Migration & Développement

4.

Mise en ligne sans perte de trafic

Aucune modification HTML/CSS.

---

# Section 5 — Pourquoi Aziz Studio Digital

Adapter les 4 cartes :

- analyse approfondie
- accompagnement personnalisé
- conservation du référencement
- support après mise en ligne

Réutiliser les mêmes composants.

---

# Section 6 — FAQ

Réutiliser exactement :

FAQ Premium Accordion

Créer 5 questions spécifiques :

- Vais-je perdre mon référencement pendant la refonte ?
- Combien de temps dure une refonte ?
- Puis-je conserver mon contenu actuel ?
- Dois-je changer de nom de domaine ?
- Mon site restera-t-il accessible pendant les travaux ?

Même structure.

Même HTML.

Même composants.

---

# Section 7 — CTA Final

Titre :

Votre site mérite une nouvelle génération.

Texte :

Inciter à moderniser son site.

CTA principal :

Demander un devis Refonte

CTA secondaire :

Parler de votre projet

---

# SEO

Créer :

Title unique

Meta description unique

Orientés :

- refonte de site web
- modernisation de site
- refonte site Congo

---

# Accessibilité

Conserver :

- aria-hidden
- breadcrumb
- H1/H2/H3
- focus
- FAQ accessible

---

# Responsive

Conserver exactement le comportement du template.

---

# Règle éditoriale des CTA

Appliquer les règles officielles :

| Type      | Structure                             |
| --------- | ------------------------------------- |
| Devis     | Demander un devis + Service           |
| Audit     | Demander un audit + Service + gratuit |
| Contact   | Parler de votre projet                |
| Portfolio | Voir nos réalisations                 |

Pour cette page :

- Demander un devis Refonte
- Voir nos réalisations
- Parler de votre projet

---

# Mise à jour des liens

Modifier :

pages/services.html

Carte :

Refonte de Site Web

Lien :

refonte-site.html

---

# build_index.py

Ajouter :

refonte-site.html

au build automatique.

---

# Documentation

Ne modifier :

docs/design-system-components.md

que si un nouveau composant est créé.

Normalement :

aucune modification.

---

# Interdictions

Ne pas :

- créer un composant
- modifier le template
- modifier Timeline Premium
- modifier FAQ Premium
- modifier Hero Premium
- utiliser @import
- modifier le Design System

---

# Critères d'acceptation

✅ Template Sprint 22 réutilisé

✅ Architecture inchangée

✅ Hero personnalisé

✅ 4 cartes "Pourquoi refaire son site"

✅ 6 prestations spécifiques

✅ Timeline Premium réutilisée

✅ FAQ Premium réutilisée

✅ CTA conformes à la règle éditoriale

✅ CSS chargé via deux `<link>`

✅ SEO unique

✅ Responsive identique

✅ Lien de `services.html` mis à jour

✅ build_index.py mis à jour

✅ Aucun nouveau composant
