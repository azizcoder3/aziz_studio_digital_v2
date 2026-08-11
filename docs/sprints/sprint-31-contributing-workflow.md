# Sprint 31 — Guide de contribution & Workflow de développement

## Objectif

Créer le document officiel **`docs/contributing.md`** afin de formaliser le workflow de développement du projet **Aziz Studio Digital V2**.

Après la stabilisation de l'architecture (Sprint 29) et l'audit qualité global (Sprint 30), ce document devient la référence pour tous les futurs développements, qu'ils soient réalisés par un développeur humain ou par un agent IA.

L'objectif est que chaque nouveau Sprint applique exactement les mêmes règles de qualité, de structure et de validation.

---

# Documents à consulter obligatoirement avant toute modification

Avant de commencer, consulter impérativement :

- `docs/project-architecture.md`
- `docs/design-system-components.md`

Le nouveau document devra être parfaitement cohérent avec ces deux références.

---

# Travail demandé

Créer :

```
docs/contributing.md
```

Aucun autre document de référence ne doit être modifié.

---

# Structure attendue

Le document doit être organisé avec les sections suivantes.

---

# 1. Présentation

Expliquer le rôle du document :

- guide officiel de contribution
- workflow de développement
- règles communes
- conventions du projet

Préciser que ce document complète :

- project-architecture.md
- design-system-components.md

---

# 2. Philosophie du projet

Documenter les principes fondateurs :

- HTML statique
- CSS Vanilla
- JavaScript natif
- Build Python
- Mobile First
- Responsive
- SEO First
- WCAG 2.1 AA
- Performance
- Réutilisation maximale des composants

---

# 3. Workflow officiel d'un Sprint

Décrire précisément les étapes.

Exemple :

1. Lecture de la documentation
2. Analyse de l'existant
3. Réutilisation des composants
4. Développement
5. Compilation
6. Contrôle qualité
7. Documentation
8. Rapport

---

# 4. Création d'une nouvelle page

Décrire le workflow officiel.

Ordre obligatoire :

Création du fragment :

```
pages/
```

↓

Création CSS :

```
assets/css/pages/
```

↓

Compilation :

```
build_index.py
```

↓

Génération page racine

↓

Validation

---

# 5. Création d'un nouveau composant

Documenter précisément :

Quand créer un composant

Quand ne PAS créer un composant

Obligation :

Toujours vérifier auparavant :

```
docs/design-system-components.md
```

Si composant inexistant :

- créer le composant
- documenter immédiatement
- respecter les conventions

---

# 6. Conventions HTML

Documenter :

HTML5 sémantique

Hiérarchie :

H1

↓

H2

↓

H3

Présence obligatoire :

- breadcrumb
- main
- section
- article
- nav

Accessibilité

ARIA

---

# 7. Conventions CSS

Documenter :

Architecture :

Base

↓

Components

↓

Pages

↓

Inline

Interdictions :

❌ @import

❌ duplication

❌ valeurs magiques

Utilisation obligatoire :

variables CSS

tokens

responsive mobile-first

---

# 8. Conventions JavaScript

Documenter :

JavaScript natif

Modules indépendants

Aucune dépendance inutile

Progressive enhancement

---

# 9. Conventions Python

Documenter :

build_index.py

Compilation

Aucune modification du build sans justification

Commentaires

Lisibilité

---

# 10. Convention SEO

Documenter :

Title

≤60 caractères

1 seul |

Meta Description

≤160 caractères

H1 unique

Breadcrumb

Liens internes

Canonical si nécessaire

---

# 11. Convention WCAG

Documenter :

Navigation clavier

Contraste

Focus

aria-hidden

aria-current

details/summary

alt

Hiérarchie

---

# 12. Règles éditoriales

Documenter officiellement :

CTA Devis

Demander un devis [Service]

CTA Audit

Demander un audit [Service] gratuit

CTA Contact

Parler de votre projet

CTA Portfolio

Voir nos réalisations

---

# 13. Checklist avant compilation

Créer une checklist.

Exemple :

□ HTML valide

□ CSS valide

□ Responsive

□ Aucun @import

□ SEO

□ WCAG

□ CTA

□ Breadcrumb

□ Build

□ Documentation

---

# 14. Checklist avant livraison

Créer une checklist.

Exemple :

□ build_index.py exécuté

□ pages générées

□ liens

□ responsive

□ Lighthouse

□ SEO

□ Documentation

□ Rapport

---

# 15. Format officiel d'un rapport de Sprint

Documenter la structure utilisée depuis les précédents Sprints.

Exemple :

Résumé

Fichiers créés

Fichiers modifiés

Composants réutilisés

SEO

WCAG

Responsive

Validation

Conclusion

---

# 16. Bonnes pratiques

Créer deux sections.

Toujours faire

Ne jamais faire

Sous forme de listes.

---

# 17. Historique

Ajouter une section rappelant :

DS-01

Sprint 23

Sprint 24

Sprint 25

Sprint 26

Sprint 27

Sprint 28

Sprint 29

Sprint 30

Puis :

Version actuelle du projet.

---

# Contraintes

Créer uniquement :

```
docs/contributing.md
```

Ne modifier aucun autre document.

Ne modifier aucun HTML.

Ne modifier aucun CSS.

Ne modifier aucun JS.

Ne modifier aucun Python.

Ne modifier aucun composant.

Ne modifier aucun build.

Aucun changement fonctionnel.

Documentation uniquement.

---

# Critères d'acceptation

✓ Un seul nouveau document

✓ Structure claire

✓ Cohérent avec project-architecture.md

✓ Cohérent avec design-system-components.md

✓ Workflow complet

✓ Checklists complètes

✓ Aucune modification du projet

✓ Aucune régression

✓ Documentation prête pour les futurs Sprints
