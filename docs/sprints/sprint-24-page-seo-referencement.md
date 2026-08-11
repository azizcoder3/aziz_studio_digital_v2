# Sprint 24 — Page Service SEO & Référencement

## Objectif

Créer la page **SEO & Référencement Naturel** en réutilisant intégralement le template officiel validé au Sprint 22 (`creation-site-web.html`).

⚠️ Ce sprint est un sprint de **contenu**, pas de conception.

Aucun nouveau composant, aucune nouvelle structure HTML et aucun nouveau Design System ne doivent être créés.

---

# Contexte

Les composants Premium du projet sont désormais documentés dans :

`docs/design-system-components.md`

Ce document devient la référence officielle du projet.

Avant toute modification, il doit être consulté afin de réutiliser exactement les composants existants.

---

# Étape 0 — Lecture obligatoire

Avant de commencer :

Lire entièrement :

`docs/design-system-components.md`

Puis vérifier notamment :

- Section 4 → composants du Design System
- Section 5 → composants Premium
- Section 6 → Règle absolue de réutilisation

Aucun composant documenté ne doit être recréé.

---

# Architecture

Créer :

pages/
└── seo.html

Créer :

assets/css/pages/
└── seo.css

Compiler ensuite :

seo.html

à la racine via :

build_index.py

comme pour :

- creation-site-web.html
- wordpress.html

---

# Base obligatoire

Copier la structure de :

pages/creation-site-web.html

La structure des 7 sections doit rester STRICTEMENT identique.

Aucun changement de structure.

Ordre obligatoire :

1. Hero
2. Pourquoi ce service
3. Ce qui est inclus
4. Notre méthode
5. Pourquoi Aziz Studio Digital
6. FAQ
7. CTA final

---

# CSS

Ne jamais utiliser :

@import

Le build doit charger :

```html
<link rel="stylesheet" href="assets/css/pages/creation-site-web.css" />
<link rel="stylesheet" href="assets/css/pages/seo.css" />
```

comme cela a été corrigé sur WordPress.

Le fichier :

seo.css

ne contient que les éventuelles adaptations propres au SEO.

Le template reste dans :

creation-site-web.css

---

# Section 1 — Hero

Adapter uniquement le contenu.

Badge :

SEO & Référencement

H1 :

Référencement naturel SEO au Congo pour attirer plus de clients

Texte :

adapter entièrement au SEO.

Mettre en avant :

- visibilité Google
- trafic qualifié
- référencement local
- optimisation continue
- acquisition de prospects

CTA principaux :

Bouton 1

Demander un audit SEO gratuit

Bouton 2

Découvrir notre méthode SEO

Conserver exactement :

- le Hero Premium
- le Dashboard HTML/CSS
- les composants existants

---

# Section 2 — Pourquoi investir dans le SEO

Remplacer les cartes.

Créer 4 cartes :

• Plus de visibilité sur Google

• Attirer des visiteurs qualifiés

• Générer des demandes sans publicité

• Construire une visibilité durable

Conserver exactement les mêmes cartes Premium.

---

# Section 3 — Ce qui est inclus

Créer 6 cartes.

Exemple :

- Audit SEO complet
- Recherche de mots-clés
- Optimisation technique
- SEO local (Google Business Profile)
- Optimisation des contenus
- Reporting mensuel

Ne modifier que les textes.

---

# Section 4 — Notre méthode

Réutiliser exactement :

Timeline Premium

Ne modifier que le contenu.

4 étapes :

1.

Audit & Analyse

2.

Stratégie SEO

3.

Optimisations & Déploiement

4.

Suivi & Amélioration continue

Aucune modification HTML/CSS.

---

# Section 5 — Pourquoi Aziz Studio Digital

Réutiliser exactement les cartes existantes.

Adapter le contenu SEO.

Exemple :

- expertise locale
- suivi transparent
- optimisation durable
- accompagnement personnalisé

---

# Section 6 — FAQ

Réutiliser exactement :

FAQ Premium Accordion

Créer 5 questions spécifiques au référencement.

Exemples :

- Combien de temps faut-il pour voir les résultats SEO ?
- Travaillez-vous le référencement local à Brazzaville ?
- Optimisez-vous Google Business Profile ?
- Comment choisissez-vous les mots-clés ?
- Fournissez-vous un suivi de positionnement ?

Conserver :

- mêmes classes
- même structure HTML
- mêmes icônes
- même comportement

---

# Section 7 — CTA Final

Adapter au SEO.

Titre :

Prêt à améliorer votre visibilité sur Google ?

Texte :

inciter à demander un audit.

CTA principal :

Demander un audit SEO gratuit

CTA secondaire :

Parler de votre projet

---

# SEO

Créer :

Title unique

Meta description unique

Le title n'a pas besoin d'être optimisé à 100 %.

Nous harmoniserons les 6 pages dans un sprint SEO dédié.

---

# Accessibilité

Conserver exactement :

- aria-hidden
- hiérarchie H1/H2/H3
- breadcrumb
- focus
- détails FAQ

---

# Responsive

Ne modifier aucun comportement responsive.

Le rendu doit rester identique au template.

---

# Mise à jour des liens

Modifier :

pages/services.html

Carte :

SEO & Référencement

Lien :

seo.html

---

# build_index.py

Ajouter :

seo.html

au build automatique.

---

# Documentation

Ne modifier

docs/design-system-components.md

QUE si un nouveau composant réutilisable est créé.

Normalement :

aucune modification.

---

# Interdictions

Ne pas :

- créer un nouveau composant
- modifier le template
- modifier Timeline Premium
- modifier FAQ Premium
- modifier le Hero Premium
- modifier les Cards Premium
- utiliser @import
- modifier le Design System
- toucher aux autres pages

---

# Critères d'acceptation

✅ Template Sprint 22 réutilisé à 100 %

✅ Architecture des 7 sections inchangée

✅ Aucun composant recréé

✅ Hero SEO personnalisé

✅ 4 cartes "Pourquoi ce service"

✅ 6 cartes "Ce qui est inclus"

✅ Timeline Premium réutilisée

✅ FAQ Premium réutilisée

✅ CTA SEO personnalisés

✅ Title et Meta uniques

✅ CSS chargé avec deux `<link>`

✅ Lien SEO de `services.html` mis à jour

✅ build_index.py mis à jour

✅ Responsive identique

✅ Aucun nouveau composant ajouté au Design System
