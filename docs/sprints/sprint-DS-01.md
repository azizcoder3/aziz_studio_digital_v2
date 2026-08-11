Exécute le Sprint DS-01 — Documentation du Design System.

Objectif :

Créer un document unique de référence nommé :

docs/design-system-components.md

IMPORTANT :

Il s'agit d'une documentation uniquement.

AUCUN fichier HTML

AUCUN fichier CSS

AUCUN composant

AUCUNE modification du projet

AUCUN build

AUCUNE correction

Le document doit uniquement décrire le Design System réellement existant.

Ne pas inventer de composants.

Ne documenter QUE ce qui existe actuellement dans le projet.

---

Le document devra contenir :

# Design System — Aziz Studio Digital V2

## 1. Présentation

Expliquer les objectifs du Design System :

- cohérence visuelle
- réutilisabilité
- maintenance
- responsive
- accessibilité
- performances

---

## 2. Architecture CSS

Lister les dossiers :

assets/css/base/

assets/css/components/

assets/css/pages/

avec le rôle de chacun.

---

## 3. Variables CSS

Documenter les grandes familles de variables :

- couleurs
- typographie
- spacing
- radius
- shadow
- transition
- z-index

Ne pas recopier le contenu de variables.css.

Faire une documentation claire et pédagogique.

---

## 4. Composants du Design System

Créer une fiche pour chaque composant réellement existant.

Pour chacun, documenter :

- rôle
- classes principales
- structure HTML
- responsive
- règles d'utilisation
- exemple HTML minimal

Exemples :

### Container

.container

---

### Grid

.grid

.grid-2

.grid-md-2

.grid-lg-2

.grid-lg-3

.grid-lg-4

avec un petit schéma de fonctionnement.

---

### Section

.section

.section-surface

.section-header

.section-header-center

---

### Card

.card

.card-body

.card-title

.card-description

.card-image-wrapper

.card-image

etc.

---

### Badge

---

### Button

---

### Header

---

### Footer

---

## 5. Composants Premium créés

Documenter tous les composants développés pendant les différents Sprints.

Par exemple :

- Hero Premium
- Services Cards
- Portfolio Cards
- Process Timeline Premium
- FAQ Premium Accordion
- Blog Cards
- CTA Banner
- Dashboard HTML/CSS
- etc.

Pour chacun, documenter :

- objectif
- structure HTML
- classes CSS utilisées
- comportement responsive
- où il est utilisé dans le projet

### IMPORTANT

Pour CHAQUE composant Premium, ajouter obligatoirement une section :

### Localisation du code source

avec :

- fichier HTML exact
- section concernée
- fichier CSS exact
- localisation (plage de lignes si possible)

Exemple attendu :

Timeline Premium

HTML :

pages/home.html

section #processus

CSS :

assets/css/pages/home.css

lignes 750–940

FAQ Premium Accordion

HTML :

pages/home.html

section #faq

CSS :

assets/css/pages/home.css

lignes XXXX–XXXX

L'objectif est qu'un futur développeur ou un futur agent puisse ouvrir directement le vrai composant dans le code sans avoir à le reconstruire.

Ne jamais se contenter d'une description textuelle lorsqu'une référence précise au code peut être donnée.

---

## 6. Règles de développement

Commencer IMPÉRATIVEMENT cette section par la règle suivante, mise en évidence.

# RÈGLE ABSOLUE

Avant de créer un nouveau sélecteur CSS ou une nouvelle structure HTML pour répondre à un besoin visuel (timeline, accordéon, carte, bannière, dashboard, CTA, etc.), vérifier d'abord dans les sections 4 et 5 de ce document si un composant équivalent existe déjà.

Si un composant existe :

- il DOIT être réutilisé à l'identique ;
- mêmes classes CSS ;
- même structure HTML ;
- même logique responsive ;
- aucune réécriture partielle ;
- aucune réinterprétation.

La création d'un nouveau composant n'est autorisée que si aucun composant existant ne répond réellement au besoin.

Puis documenter les autres règles :

- utiliser exclusivement les variables CSS
- ne jamais coder une couleur en dur
- réutiliser les composants existants
- HTML sémantique
- responsive mobile-first
- accessibilité WCAG
- SEO
- aucun JavaScript inutile
- respecter le Design System

---

## 7. Checklist avant chaque Sprint

Créer une checklist de validation.

Exemple :

□ le composant existe-t-il déjà ?

□ une classe existante peut-elle être réutilisée ?

□ de nouveaux sélecteurs sont-ils réellement nécessaires ?

□ responsive vérifié ?

□ accessibilité vérifiée ?

□ SEO vérifié ?

□ Design System respecté ?

□ build exécuté ?

---

## 8. Historique des composants

Créer un tableau récapitulatif.

Exemple :

Sprint | Composant | Statut

Sprint 05 | Hero | ✅

Sprint 06 | Services Cards | ✅

...

jusqu'au Sprint 22.

---

## 9. Maintenance du document

Ajouter une dernière section intitulée :

# Mise à jour continue du Design System

Préciser que ce document constitue la référence officielle du projet.

À chaque fois qu'un nouveau composant réutilisable est créé dans le projet (Services, Portfolio, Blog, Contact, À propos, etc.), ce document doit être mis à jour immédiatement.

Pour chaque nouveau composant, il faudra ajouter :

- son nom ;
- son objectif ;
- ses classes CSS ;
- sa structure HTML ;
- son comportement responsive ;
- son fichier HTML de référence ;
- son fichier CSS de référence ;
- sa localisation exacte dans le code (plage de lignes si possible).

Ainsi, ce document restera la source unique de vérité du Design System et évitera la recréation inutile de composants déjà existants.

---

Contraintes :

Ne modifier AUCUN autre fichier.

Ne pas corriger le projet.

Ne pas créer de CSS.

Ne pas créer de HTML.

Ne pas lancer le build.

Créer uniquement :

docs/design-system-components.md

---

À la fin, fournir un rapport indiquant :

- le fichier créé ;
- le nombre de composants documentés ;
- la liste des composants recensés ;
- la confirmation que les références HTML/CSS ont été ajoutées pour chaque composant Premium ;
- la confirmation qu'aucun autre fichier du projet n'a été modifié.
