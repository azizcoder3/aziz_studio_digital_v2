# Sprint 27 — Page Service Audit & Conseil Digital

## Objectif du Sprint

Créer la page **Audit & Conseil Digital** en s'appuyant **strictement** sur le template officiel validé au **Sprint 22** (`creation-site-web.html`) et en réutilisant **100 % des composants existants** documentés dans `docs/design-system-components.md`.

Aucune modification de l'architecture du template n'est autorisée. Seul le contenu est adapté au service **Audit & Conseil Digital**.

---

# Contexte

Les pages suivantes sont déjà terminées :

- ✅ Création de site web
- ✅ Développement WordPress
- ✅ SEO & Référencement
- ✅ Refonte de site web
- ✅ Maintenance & Support

Cette page clôture la série des pages Services.

---

# Fichiers à créer

Créer les fichiers suivants :

```text
pages/
└── audit-conseil.html
```

```text
assets/css/pages/
└── audit-conseil.css
```

Le build devra générer :

```text
audit-conseil.html
```

à la racine du projet via `build_index.py`.

---

# Règles obligatoires

## 1. Lecture obligatoire du Design System

Avant toute modification, consulter impérativement :

```text
docs/design-system-components.md
```

Tous les composants existants doivent être réutilisés.

Aucun composant HTML ou CSS ne doit être recréé.

---

## 2. Copier le template officiel

Utiliser comme base :

```text
pages/creation-site-web.html
```

Conserver exactement les **7 sections** :

1. Hero
2. Pourquoi ce service
3. Ce qui est inclus
4. Notre méthode
5. Pourquoi Aziz Studio Digital
6. FAQ
7. CTA Final

Aucune section ne doit être ajoutée, supprimée ou déplacée.

---

# Structure détaillée

## Section 1 — Hero

Adapter entièrement le contenu.

### Badge

```
📊 Audit & Conseil Digital
```

### H1

Exemple :

> Audit digital au Congo pour identifier les opportunités de croissance de votre entreprise

### Texte

Mettre en avant :

- analyse complète
- performance
- visibilité
- stratégie digitale
- amélioration des conversions
- accompagnement personnalisé

### CTA

Bouton principal

```
Demander un audit digital gratuit
```

Lien :

```text
contact.html?type=audit&service=audit
```

Bouton secondaire

```
Parler de votre projet
```

---

## Hero Dashboard

Réutiliser exactement le composant Premium.

Adapter les données.

Exemple :

### URL

```
audit-digital.cg
```

### Statistiques

```
Opportunités détectées
+18
```

```
Performance globale
82/100
```

### Badge flottant

```
📈 Diagnostic complet
```

Sous-titre

```
Analyse • Conseils • Priorités
```

---

# Section 2 — Pourquoi réaliser un audit digital ?

Créer **4 cartes**.

Exemples :

### Votre site ne génère pas assez de clients

Identifier les blocages empêchant la conversion.

---

### Votre visibilité Google est insuffisante

Repérer les opportunités SEO.

---

### Vos performances sont faibles

Analyser vitesse, UX et expérience mobile.

---

### Vous manquez de stratégie

Définir un plan d'action clair et priorisé.

---

# Section 3 — Ce qui est inclus

Créer **6 cartes**.

Exemples :

- Audit SEO complet
- Audit technique
- Analyse UX/UI
- Analyse concurrentielle
- Recommandations prioritaires
- Plan d'action personnalisé

---

# Section 4 — Notre méthode

Réutiliser la **Timeline Premium**.

Les 4 étapes deviennent :

### Étape 01

Découverte & objectifs

---

### Étape 02

Audit complet

- SEO
- Technique
- UX
- Performance

---

### Étape 03

Analyse & recommandations

Classement des priorités.

---

### Étape 04

Présentation du plan d'action

Accompagnement stratégique.

---

# Section 5 — Pourquoi Aziz Studio Digital

Créer **4 cartes**.

Exemples :

### Vision globale

Nous analysons tous les aspects de votre présence digitale.

---

### Recommandations concrètes

Des actions classées par priorité.

---

### Expertise locale

Solutions adaptées au marché congolais.

---

### Accompagnement

Nous pouvons également mettre en œuvre les recommandations.

---

# Section 6 — FAQ

Créer **5 questions spécifiques**.

Exemples :

### Combien de temps dure un audit digital ?

---

### Vais-je recevoir un rapport détaillé ?

---

### L'audit comprend-il le référencement SEO ?

---

### Puis-je demander uniquement un audit sans prestation complémentaire ?

---

### Que se passe-t-il après l'audit ?

---

Réutiliser exactement le composant **FAQ Premium**.

---

# Section 7 — CTA Final

Titre :

```
Découvrez les points qui freinent réellement votre croissance digitale
```

Texte :

Inviter à demander un audit personnalisé.

Boutons :

```
Demander un audit digital gratuit
```

```
Parler de votre projet
```

---

# SEO

Créer des métadonnées uniques.

## Title

- Maximum **60 caractères**
- Un seul séparateur **|**

Exemple :

```
Audit digital au Congo | Aziz Studio Digital
```

---

## Meta description

Maximum **160 caractères**.

Exemple :

```
Audit digital au Congo par Aziz Studio Digital : analyse SEO, technique, UX et stratégie pour améliorer les performances de votre site web.
```

---

# Chargement CSS

Ne jamais utiliser :

```css
@import;
```

Le `<head>` doit contenir exactement :

```html
<link rel="stylesheet" href="assets/css/pages/services.css" />
<link rel="stylesheet" href="assets/css/pages/creation-site-web.css" />
<link rel="stylesheet" href="assets/css/pages/audit-conseil.css" />
```

---

# Mise à jour de services.html

Mettre à jour la carte :

```
Audit & Conseil Digital
```

pour pointer vers :

```text
audit-conseil.html
```

---

# Mise à jour de build_index.py

Ajouter la compilation automatique de :

```text
pages/audit-conseil.html
```

vers :

```text
audit-conseil.html
```

---

# Documentation

Puisqu'aucun nouveau composant ne doit être créé :

```
docs/design-system-components.md
```

ne doit **pas être modifié**.

---

# Critères d'acceptation

- ✅ Template officiel du Sprint 22 réutilisé sans modification.
- ✅ Les 7 sections obligatoires sont conservées.
- ✅ Aucun composant HTML/CSS recréé.
- ✅ Tous les composants proviennent du Design System.
- ✅ Hero Dashboard réutilisé.
- ✅ Timeline Premium réutilisée.
- ✅ FAQ Premium réutilisée.
- ✅ Contenu entièrement spécifique à l'Audit & Conseil Digital.
- ✅ Title ≤ 60 caractères avec un seul séparateur `|`.
- ✅ Meta description ≤ 160 caractères.
- ✅ Trois feuilles CSS chargées (`services.css`, `creation-site-web.css`, `audit-conseil.css`).
- ✅ Aucun `@import`.
- ✅ CTA conformes à la règle éditoriale :
  - **Demander un audit digital gratuit**
  - **Parler de votre projet**
- ✅ Carte "Audit & Conseil Digital" de `services.html` reliée à `audit-conseil.html`.
- ✅ `build_index.py` mis à jour.
- ✅ Génération de `audit-conseil.html` à la racine.
- ✅ Aucun nouveau composant ajouté au Design System.

---

# Prompt d'exécution pour l'agent

```text
Exécute le Sprint 27 — Page Service Audit & Conseil Digital.

Avant toute modification :

1. Lire obligatoirement docs/design-system-components.md.
2. Réutiliser exclusivement les composants existants.
3. Ne recréer aucun composant HTML ou CSS.

Créer :

- pages/audit-conseil.html
- assets/css/pages/audit-conseil.css

en copiant le template officiel pages/creation-site-web.html sans modifier son architecture.

Conserver exactement les 7 sections :

1. Hero
2. Pourquoi ce service
3. Ce qui est inclus
4. Notre méthode
5. Pourquoi Aziz Studio Digital
6. FAQ
7. CTA Final

Adapter uniquement le contenu au service Audit & Conseil Digital.

Le Hero Dashboard doit être réutilisé avec de nouvelles métriques adaptées à l'audit.

Créer un contenu totalement original comprenant :

- Hero
- 4 raisons
- 6 prestations incluses
- Timeline en 4 étapes
- 4 cartes de réassurance
- 5 questions FAQ
- CTA Final

Créer un Title unique (≤60 caractères) avec un seul séparateur "|".

Créer une Meta description unique (≤160 caractères).

Ne jamais utiliser @import.

Le build doit charger exactement :

- assets/css/pages/services.css
- assets/css/pages/creation-site-web.css
- assets/css/pages/audit-conseil.css

Mettre à jour pages/services.html afin que la carte "Audit & Conseil Digital" pointe vers audit-conseil.html.

Mettre à jour build_index.py pour compiler automatiquement audit-conseil.html.

Ne pas modifier docs/design-system-components.md puisqu'aucun nouveau composant n'est créé.

À la fin :

1. Exécuter python build_index.py.
2. Vérifier que audit-conseil.html est générée correctement.
3. Fournir un rapport comprenant :

- Fichiers créés
- Fichiers modifiés
- Composants Design System réutilisés
- Validation SEO (Title, Meta, H1)
- Validation WCAG
- Validation Responsive
- Validation Build
- Nouveaux composants créés (normalement : Aucun)
- Documentation mise à jour (normalement : Non)
```
