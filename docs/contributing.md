# Guide de contribution & Workflow de développement — Aziz Studio Digital V2

> **Document officiel du projet** — Version 1.0 — Sprint 31  
> Ce document définit le workflow de développement, les règles de qualité et les conventions officielles pour la contribution sur **Aziz Studio Digital V2**.  
> Il complète et s'appuie sur [`docs/project-architecture.md`](file:///c:/Users/Aziz/Desktop/aziz_studio_digital_v2/docs/project-architecture.md) et [`docs/design-system-components.md`](file:///c:/Users/Aziz/Desktop/aziz_studio_digital_v2/docs/design-system-components.md).

---

## Table des matières

1. [Présentation](#1-présentation)
2. [Philosophie du projet](#2-philosophie-du-projet)
3. [Workflow officiel d'un Sprint](#3-workflow-officiel-dun-sprint)
4. [Création d'une nouvelle page](#4-création-dune-nouvelle-page)
5. [Gestion et création de composants](#5-gestion-et-création-de-composants)
6. [Conventions HTML](#6-conventions-html)
7. [Conventions CSS](#7-conventions-css)
8. [Conventions JavaScript](#8-conventions-javascript)
9. [Conventions Python & Build](#9-conventions-python--build)
10. [Conventions SEO](#10-conventions-seo)
11. [Conventions WCAG & Accessibilité](#11-conventions-wcag--accessibilité)
12. [Règles éditoriales des CTA](#12-règles-éditoriales-des-cta)
13. [Checklist avant compilation](#13-checklist-avant-compilation)
14. [Checklist avant livraison](#14-checklist-avant-livraison)
15. [Format officiel d'un rapport de Sprint](#15-format-officiel-dun-rapport-de-sprint)
16. [Bonnes pratiques](#16-bonnes-pratiques)
17. [Historique du projet](#17-historique-du-projet)

---

## 1. Présentation

Le présent guide est le **manuel de référence pour toute contribution** (développeur humain ou agent IA) sur le projet **Aziz Studio Digital V2**.

Il formalise la méthode de travail et garantit qu'au fil des Sprints, la codebase conserve :
- une homogénéité parfaite de structure et de style ;
- un haut niveau d'exigence technique et SEO ;
- une stabilité architecturale totale.

### Dépendances et documentation de référence

Ce document doit être utilisé conjointement avec les deux piliers documentaires du projet :
- **[`docs/project-architecture.md`](file:///c:/Users/Aziz/Desktop/aziz_studio_digital_v2/docs/project-architecture.md)** : Décrit l'arborescence, la mécanique de compilation Python, l'ordre des feuilles CSS et la répartition des fichiers.
- **[`docs/design-system-components.md`](file:///c:/Users/Aziz/Desktop/aziz_studio_digital_v2/docs/design-system-components.md)** : Définit les tokens visuels, les composants atomiques et les composants Premium réutilisables.

---

## 2. Philosophie du projet

Les principes techniques fondateurs d'Aziz Studio Digital V2 sont intangibles :

| Principe | Choix technique | Justification |
|---|---|---|
| **Structure** | HTML5 Statique Sémantique | Zéro overhead, SEO maximal, durabilité |
| **Styles** | CSS Vanilla Custom Properties | Zéro framework (Tailwind/Bootstrap), contrôle total, légèreté |
| **Logique** | JavaScript ES6+ Natif | Zéro librairie lourde (React/jQuery), chargement instantané |
| **Build** | Python Script (`build_index.py`) | Assemblage statique fiable sans bundler complexe (npm/webpack) |
| **Responsive** | Mobile-First | Conception d'abord pour mobile (<768px) puis enrichment desktop |
| **SEO** | Technical SEO First | Titres stricts (≤60 chars), meta (≤160 chars), H1 unique, breadcrumbs |
| **Accessibilité** | WCAG 2.1 AA | Navigation clavier complète, contrastes validés, attributs ARIA |
| **Composants** | Réutilisation stricte | Interdiction de recréer du code existant dans le Design System |

---

## 3. Workflow officiel d'un Sprint

Tout Sprint (fonctionnel, correctif ou documentaire) doit respecter l'enchaînement strict des **8 étapes** suivantes :

```
Step 1 : Lecture documentaire
   └── Consulter project-architecture.md et design-system-components.md

Step 2 : Analyse de l'existant
   └── Vérifier si des fragments ou composants répondent au besoin

Step 3 : Réutilisation maximale
   └── Ne recréer aucun composant ni style déjà disponible

Step 4 : Développement
   └── Écrire le HTML/CSS/JS selon les conventions strictes

Step 5 : Compilation
   └── Exécuter python build_index.py pour régénérer les pages

Step 6 : Contrôle Qualité (QA)
   └── Valider le SEO, le responsive, l'accessibilité et les liens

Step 7 : Documentation
   └── Mettre à jour design-system-components.md si un composant est créé

Step 8 : Rapport de Sprint
   └── Produire un rapport complet au format officiel
```

---

## 4. Création d'une nouvelle page

La création d'une page respecte un découpage obligatoire en **6 phases** :

1. **Création du fragment HTML source** dans `pages/[nom-page].html` :
   - Contient uniquement le bloc `<main role="main">` de la page.
   - Ne doit contenir ni `<html>`, ni `<head>`, ni `<header>`, ni `<footer>`.
2. **Création du fichier CSS spécifique** dans `assets/css/pages/[nom-page].css` :
   - Contient exclusivement les règles propres à cette page.
3. **Ajout de la page dans `build_index.py`** :
   - Configurer le titre (≤60 chars, 1 pipe `|`), la description (≤160 chars) et la liste ordonnée des feuilles CSS.
4. **Compilation** :
   - Lancer `python build_index.py` depuis la racine.
5. **Génération de la page racine** :
   - La page compilée finale est produite à la racine `[nom-page].html`.
6. **Validation** :
   - Contrôler l'affichage mobile, tablette, desktop et la conformité des balises.

---

## 5. Gestion et création de composants

### Quand utiliser un composant existant ? (Cas par défaut)
Avant tout développement visuel, consulter [`docs/design-system-components.md`](file:///c:/Users/Aziz/Desktop/aziz_studio_digital_v2/docs/design-system-components.md). Tous les blocs types (Hero Dashboard, Cards, Timeline, FAQ Accordion, CTA Final, Badges, Boutons) doivent être réutilisés sans réécriture.

### Quand créer un nouveau composant ?
Un composant ne peut être créé que si :
1. Aucun composant existant ne peut répondre au besoin fonctionnel.
2. Le besoin est générique et réutilisable sur plusieurs pages.

### Obligation lors de la création d'un composant
- Utiliser la nomenclature BEM/kebab-case officielle.
- Ne faire référence qu'aux tokens de `variables.css`.
- Documenter immédiatement le composant avec ses exemples de code dans `docs/design-system-components.md`.

---

## 6. Conventions HTML

- **Unicité du `<h1>`** : Strictement **1 seul `<h1>`** par page.
- **Hiérarchie stricte** : $H1 \rightarrow H2 \rightarrow H3 \rightarrow H4$. Aucun saut de niveau (ex: $H1 \rightarrow H3$ est interdit).
- **Structure sémantique HTML5** :
  - `<main id="main-content" role="main">` pour le contenu principal.
  - `<header class="site-header" role="banner">` pour la navigation.
  - `<footer class="site-footer" role="contentinfo">` pour le pied de page.
  - `<section class="section">` pour les découpages horizontaux.
- **Fil d'Ariane (Breadcrumb)** : Obligatoire sur les pages secondaires sous la forme :
  ```html
  <nav class="breadcrumb" aria-label="Fil d'Ariane">
      <ol class="breadcrumb-list" role="list">
          <li class="breadcrumb-item"><a href="index.html" class="breadcrumb-link">Accueil</a></li>
          <li class="breadcrumb-separator" aria-hidden="true">…</li>
          <li class="breadcrumb-item breadcrumb-item-active" aria-current="page"><span>Page Active</span></li>
      </ol>
  </nav>
  ```

---

## 7. Conventions CSS

### Architecture en 4 couches
Les feuilles de style sont chargées selon l'ordre strict suivant :

```
Layer 1 : BASE       (variables.css → reset.css → typography.css → base.css)
Layer 2 : COMPONENTS (container.css → grid.css → section.css → card.css → badge.css → button.css → header.css → footer.css)
Layer 3 : PAGES      (services.css → creation-site-web.css → [page].css)
Layer 4 : INLINE     (<style> en head pour padding-top du body)
```

### Ordre obligatoire sur les pages Services
```html
<link rel="stylesheet" href="assets/css/pages/services.css">
<link rel="stylesheet" href="assets/css/pages/creation-site-web.css">
<link rel="stylesheet" href="assets/css/pages/[page].css">
```

### Interdictions formelles
- ❌ **Aucun `@import`** dans les fichiers CSS.
- ❌ **Aucune valeur magique** ou codée en dur (couleurs `#hex`, marges `px` hors variables).
- ❌ **Aucune duplication** de règles entre composants.

### Utilisation obligatoire des tokens
Toujours utiliser `var(--color-primary)`, `var(--spacing-16px)`, `var(--radius-medium)`, etc.

---

## 8. Conventions JavaScript

- **Vanilla JS natif** : Écrire du code ES6+ clair, sans aucun transpileur ni bundler.
- **Architecture modulaire** : Tout code JS doit être isolé dans `assets/js/modules/[module].js`.
- **Zéro dépendance externe** : Ne jamais inclure de CDN ou de librairie externe (pas de jQuery, Lodash, React).
- **Progressive Enhancement** : La page doit rester fonctionnelle et lisible même si JavaScript est désactivé (ex: accordéons FAQ natifs en `<details>/<summary>`).

---

## 9. Conventions Python & Build

- **Script unique** : `build_index.py` à la racine est le seul script de build autorisé pour la génération des pages.
- **Encodage UTF-8** : Tout fichier HTML ou Python doit être lu et écrit en UTF-8 (`encoding='utf-8'`).
- **Indépendance des fragments** : `build_index.py` combine `components/header.html`, `pages/[page].html` et `components/footer.html`.
- **Règle de modification** : Ne jamais modifier les règles d'assemblage du build sans raison technique majeure validée.

---

## 10. Conventions SEO

| Élément | Règle stricte |
|---|---|
| **`<title>`** | Unique par page, **$\le$ 60 caractères**, exactement **1 seul séparateur `\|`** |
| **`<meta description>`** | Unique par page, **$\le$ 160 caractères**, phrase complète |
| **`<h1>`** | Unicité absolue (1 seul H1 par page) |
| **Liage interne** | Liens relatifs propres (`index.html`, `services.html`), aucun lien cassé |
| **Canonical** | Présence des balises canonical sur les pages d'atterrissage |

---

## 11. Conventions WCAG & Accessibilité

- **Clavier** : Navigation accessible via `Tab` / `Shift+Tab`. Menu mobile fermable via `Escape` avec piège à focus (trap focus).
- **Visibilité du focus** : Toujours conserver un contour `:focus-visible` net.
- **Contrastes** : Respecter un ratio minimal de 4.5:1 pour le texte standard et 3:1 pour le texte large/composants.
- **Attributs ARIA** :
  - `aria-label` sur tous les boutons/icônes sans texte explicite.
  - `aria-hidden="true"` sur les SVG et éléments visuels décoratifs.
  - `aria-current="page"` sur l'élément actif du menu et du breadcrumb.
- **Alternative textuelle** : 100% des balises `<img>` doivent posséder un attribut `alt` renseigné.

---

## 12. Règles éditoriales des CTA

Pour garantir une cohérence de conversion sur tout le site, la formulation des boutons d'action (CTA) est strictement réglementée :

- **CTA Devis** : `"Demander un devis [Service]"` *(ex: "Demander un devis WordPress")*
- **CTA Audit** : `"Demander un audit [Service] gratuit"` *(ex: "Demander un audit SEO gratuit")*
- **CTA Contact** : `"Parler de votre projet"`
- **CTA Portfolio** : `"Voir nos réalisations"`

---

## 13. Checklist avant compilation

Avant d'exécuter le script `build_index.py`, vérifier :

- [ ] Fragment HTML valide créé dans `pages/` sans balises d'en-tête global (`<head>`, `<body>`).
- [ ] Titre SEO préparé ($\le$ 60 chars, 1 pipe `|`).
- [ ] Meta description préparée ($\le$ 160 chars).
- [ ] Feuille CSS créée dans `assets/css/pages/` sans aucun `@import`.
- [ ] Variables CSS custom properties utilisées à 100%.
- [ ] Règle éditoriale du CTA respectée.
- [ ] 1 seul `<h1>` présent dans le fragment.

---

## 14. Checklist avant livraison

Avant de déclarer un Sprint terminé, valider :

- [ ] `python build_index.py` exécuté avec succès (0 erreur).
- [ ] Toutes les pages générées à la racine sont à jour.
- [ ] 0 lien interne cassé.
- [ ] Responsive vérifié sur 375px, 768px, 1024px et 1440px.
- [ ] Contrastes et navigation clavier validés (WCAG 2.1 AA).
- [ ] `docs/design-system-components.md` mis à jour si un nouveau composant réutilisable a été créé.
- [ ] Rapport de Sprint rédigé selon le format officiel.

---

## 15. Format officiel d'un rapport de Sprint

Chaque Sprint doit se conclure par un rapport structuré comme suit :

```markdown
# Sprint [N°] — [Nom du Sprint]

### 📁 Fichiers modifiés / créés
- Fichiers créés : …
- Fichiers modifiés : …

### 📊 Mesures & Contrôles SEO
- Tableau récapitulatif des Titles, Meta descriptions et H1.

### 🎨 Design System & CSS
- Validation du non-usage d'import et de la réutilisation des composants.

### ♿ Accessibilité (WCAG) & Responsive
- Résultats des tests clavier, contrastes et breakpoints.

### ⚙️ Build & Liens
- Validation de l'exécution de build_index.py et résultat du contrôle des liens.

### ✅ Confirmations finales
- Confirmation du respect des règles et de l'absence de régression.
```

---

## 16. Bonnes pratiques

### À toujours faire
- ✅ Consulter la documentation officielle avant toute écriture de code.
- ✅ Utiliser `python build_index.py` pour compiler la racine.
- ✅ Tester le rendu sur mobile (375px) en premier lieu.
- ✅ Conserver des noms de classes explicites en kebab-case.
- ✅ Exécuter les scripts Python de contrôle qualité SEO et liens.

### À ne jamais faire
- ❌ Ne jamais modifier directement les fichiers HTML compilés à la racine.
- ❌ Ne jamais utiliser `@import` dans les fichiers CSS.
- ❌ Ne jamais installer de framework CSS ou de librairie JS externe.
- ❌ Ne jamais utiliser d'images ou d'icônes sans attribut `alt` ou `aria-hidden`.
- ❌ Ne jamais sauter de niveau dans la hiérarchie des titres.

---

## 17. Historique du projet

| Version | Sprint | Description |
|---|---|---|
| — | **Sprint DS-01** | Création du Design System officiel (variables CSS, composants atomiques). |
| — | **Sprints 01–04** | Mise en place des fondations CSS (variables, reset, typography, base). |
| — | **Sprints 05–17** | Construction progressive des sections de la page d'accueil. |
| — | **Sprint 18** | Composant Timeline Premium. |
| — | **Sprint 19** | Composant FAQ Accordion Premium. |
| — | **Sprints 20–21** | Page Services générale. |
| — | **Sprints 22–27** | Création du template officiel des pages Services et déclinaison des 6 services. |
| — | **Sprint 28** | Harmonisation finale des pages Services. |
| — | **Sprint 29** | Documentation officielle de l'architecture (`docs/project-architecture.md`). |
| — | **Sprint 30** | Audit qualité global du projet (0 erreur SEO, HTML, CSS, links, WCAG). |
| **v1.0** | **Sprint 31** | Guide de contribution officiel & workflow (`docs/contributing.md`). |

---

*Document maintenu par Aziz Studio Digital.*  
*Pour toute question sur l'architecture : `docs/project-architecture.md`.*  
*Pour toute question sur les composants : `docs/design-system-components.md`.*
