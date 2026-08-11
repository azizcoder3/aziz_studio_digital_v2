# Sprint 29 — Documentation de l'architecture du projet

**Projet :** Aziz Studio Digital v2  
**Sprint :** 29  
**Statut :** À exécuter  
**Priorité :** Haute  
**Dépendance :** Sprint 28 validé (harmonisation finale des pages Services)

---

# 1. Contexte

Les six pages du module **Services** sont désormais terminées, harmonisées et validées.

Conformément à la décision prise après le Sprint DS-01, la documentation de l'architecture n'a pas été réalisée au début du projet afin d'éviter de documenter une architecture encore instable.

Après le Sprint 28, l'architecture est désormais considérée comme stabilisée.

L'objectif de ce sprint est donc de produire une documentation technique de référence décrivant fidèlement l'organisation actuelle du projet, sans modifier le code existant.

Aucune évolution fonctionnelle n'est attendue.

---

# 2. Objectif

Créer le document :

```
docs/project-architecture.md
```

Ce document deviendra la documentation officielle de l'architecture du projet.

Il devra être suffisamment précis pour permettre à un nouveau développeur de comprendre immédiatement :

- la structure du projet ;
- le fonctionnement du build ;
- l'organisation HTML/CSS ;
- les composants réutilisables ;
- les conventions utilisées.

---

# 3. Sources obligatoires

Avant de commencer, l'agent doit analyser :

- build_index.py
- docs/design-system-components.md
- l'arborescence complète du projet
- les pages créées jusqu'au Sprint 28

La documentation doit décrire exclusivement l'architecture réellement présente dans le projet.

Aucune partie ne doit être inventée.

---

# 4. Contenu attendu

Le document devra être structuré exactement comme suit.

---

# Architecture du projet

Présentation générale du projet.

Objectifs.

Organisation générale.

---

# Arborescence

Documenter l'arborescence complète du projet.

Exemple :

```
/
assets/
css/
components/
pages/
docs/
```

Présenter l'organisation sous forme d'arbre.

---

# Organisation des pages

Décrire :

- pages source
- pages compilées
- pages légales
- page d'accueil
- pages services

Expliquer la logique.

---

# Build

Décrire précisément :

- build_index.py

Son rôle.

Son fonctionnement.

Les étapes de compilation.

Les fichiers générés.

---

# Architecture CSS

Documenter :

assets/css/

Organisation des dossiers.

CSS global.

CSS composants.

CSS pages.

Expliquer les dépendances.

Expliquer pourquoi :

services.css

est chargé avant

creation-site-web.css

puis

page.css

---

# Architecture HTML

Décrire :

partials

templates

pages

structure HTML

organisation des sections.

---

# Design System

Faire un résumé du document :

docs/design-system-components.md

Ne pas recopier le document.

Expliquer uniquement son rôle dans le projet.

---

# Pages Services

Lister les pages :

- Création de site web
- WordPress
- SEO
- Refonte
- Maintenance
- Audit & Conseil

Pour chacune :

- nom du fichier
- CSS associé
- template utilisé

---

# Conventions

Documenter :

nomenclature

classes CSS

organisation

responsive

accessibilité

SEO

CTA

---

# Workflow

Expliquer le workflow officiel :

Création d'une nouvelle page

↓

création du fragment HTML

↓

création du CSS

↓

ajout dans build_index.py

↓

compilation

↓

tests

↓

validation

---

# Bonnes pratiques

Documenter :

- ne jamais dupliquer un composant
- toujours consulter design-system-components.md
- ne jamais modifier le template sans validation
- toujours compiler avec build_index.py
- respecter le Design System

---

# Historique

Ajouter une section résumant les étapes majeures :

DS-01

Sprint 22

Sprint 23

Sprint 24

Sprint 25

Sprint 26

Sprint 27

Sprint 28

sans entrer dans le détail des développements.

---

# 5. Contraintes

Le document doit être :

- entièrement en Markdown ;
- structuré avec des titres cohérents ;
- facilement lisible ;
- orienté documentation technique.

Ne pas documenter du code inexistant.

Ne pas ajouter de fonctionnalités futures.

Ne pas faire de spéculation.

---

# 6. Hors périmètre

Ne pas modifier :

- build_index.py
- HTML
- CSS
- JavaScript
- Design System

Aucun fichier du projet ne doit être modifié.

Seul le document :

```
docs/project-architecture.md
```

doit être créé.

---

# 7. Livrables attendus

Créer uniquement :

```
docs/project-architecture.md
```

Aucun autre document.

Aucune modification du projet.

---

# 8. Critères d'acceptation

✅ architecture fidèle au projet

✅ aucune invention

✅ build correctement documenté

✅ structure CSS expliquée

✅ structure HTML expliquée

✅ workflow documenté

✅ pages Services documentées

✅ conventions documentées

✅ Design System référencé

✅ document clair

✅ document maintenable

✅ aucun autre fichier modifié

---

# Fin du Sprint 29
