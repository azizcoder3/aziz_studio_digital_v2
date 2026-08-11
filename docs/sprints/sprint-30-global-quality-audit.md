# Sprint 30 — Audit qualité global du projet

**Projet :** Aziz Studio Digital V2  
**Sprint :** 30  
**Statut :** À exécuter  
**Priorité :** Haute  
**Dépendance :** Sprint 29 validé (Documentation de l'architecture)

---

# 1. Contexte

Le module **Services** est désormais entièrement terminé, harmonisé et documenté.

Le projet dispose également de deux documents de référence :

- `docs/design-system-components.md`
- `docs/project-architecture.md`

Avant de poursuivre les prochains développements (Portfolio, Blog, Contact, SEO avancé, optimisations...), une dernière étape de contrôle qualité global est nécessaire.

L'objectif n'est **pas** d'ajouter de nouvelles fonctionnalités.

Il s'agit uniquement de vérifier que l'ensemble du projet respecte les standards définis depuis le début du développement.

---

# 2. Objectif

Réaliser un audit qualité complet de l'ensemble du projet afin de :

- détecter les incohérences restantes ;
- corriger uniquement les anomalies réelles ;
- harmoniser les éléments encore divergents ;
- garantir un socle technique propre avant les prochains développements.

Le Sprint doit produire un projet cohérent, stable et homogène.

---

# 3. Documents de référence obligatoires

Avant toute intervention, l'agent doit lire intégralement :

```
docs/project-architecture.md
```

puis

```
docs/design-system-components.md
```

Ces documents constituent les références officielles du projet.

Aucune décision ne doit entrer en contradiction avec ces documents.

---

# 4. Périmètre

Le Sprint concerne l'ensemble du projet.

Sont notamment concernés :

- index.html
- services.html
- portfolio.html
- a-propos.html
- contact.html
- toutes les pages Services
- pages légales
- composants communs
- build_index.py
- assets/
- components/
- pages/

---

# 5. Hors périmètre

Ne pas :

- créer une nouvelle page ;
- développer une nouvelle fonctionnalité ;
- modifier l'architecture ;
- modifier le Design System ;
- modifier les animations ;
- modifier le responsive sans nécessité ;
- créer un composant HTML/CSS/JS.

---

# 6. Contrôles SEO

Pour chaque page :

Vérifier :

- présence d'un seul `<title>`;
- présence d'une seule meta description ;
- présence d'un seul H1 ;
- hiérarchie correcte H1 → H2 → H3 ;
- titles uniques ;
- meta descriptions uniques ;
- aucune duplication.

Mesurer automatiquement :

- longueur exacte du title ;
- longueur exacte de la meta description.

Produire un tableau récapitulatif.

---

# 7. Contrôles HTML

Vérifier :

- HTML valide ;
- balises fermées ;
- structure sémantique ;
- `<main>`;
- `<header>`;
- `<footer>`;
- `<section>`;
- `<article>` lorsque nécessaire.

Aucune structure incohérente.

---

# 8. Contrôles WCAG 2.1 AA

Contrôler :

- aria-label ;
- aria-hidden ;
- aria-current ;
- alt des images ;
- boutons ;
- liens ;
- navigation clavier ;
- composants `<details>/<summary>`;
- ordre logique des titres.

Corriger uniquement les erreurs réelles.

---

# 9. Contrôles Responsive

Tester :

- 375 px
- 768 px
- 1024 px
- 1440 px

Vérifier :

- aucune barre horizontale ;
- aucune carte cassée ;
- aucune image débordante ;
- aucun Hero cassé ;
- aucune Timeline cassée ;
- aucune FAQ cassée.

---

# 10. Contrôles CSS

Contrôler :

absence de :

- @import
- duplication
- règles inutilisées
- règles orphelines

Vérifier l'ordre des feuilles CSS.

Les pages Services doivent toujours charger :

```
services.css
```

↓

```
creation-site-web.css
```

↓

```
page.css
```

dans cet ordre uniquement.

---

# 11. Contrôles du Design System

Comparer tous les composants utilisés avec :

```
docs/design-system-components.md
```

Vérifier :

- Hero Premium
- Dashboard
- Timeline Premium
- FAQ Premium
- CTA Final
- Cards
- Badges
- Buttons
- Grid
- Container
- Sections

Aucun composant ne doit avoir été recréé.

---

# 12. Contrôles de l'architecture

Comparer le projet avec :

```
docs/project-architecture.md
```

Vérifier :

- organisation des dossiers ;
- workflow ;
- build ;
- conventions ;
- architecture CSS ;
- architecture HTML.

Le projet doit respecter la documentation officielle.

---

# 13. Contrôles des liens

Tester tous les liens internes.

Contrôler notamment :

- Header
- Footer
- CTA
- Portfolio
- Contact
- Services
- Mentions légales
- Politique de confidentialité
- Conditions d'utilisation
- Breadcrumb

Objectif :

Aucun lien cassé.

---

# 14. Contrôles du Build

Exécuter :

```bash
python build_index.py
```

Le build doit :

- terminer sans erreur ;
- générer toutes les pages ;
- ne produire aucun avertissement bloquant.

---

# 15. Contrôles JavaScript

Contrôler :

- header.js
- footer.js

Vérifier :

- absence d'erreur console ;
- comportement identique sur toutes les pages ;
- aucun code mort évident.

Ne développer aucune nouvelle fonctionnalité JavaScript.

---

# 16. Contrôles des performances

Vérifier :

- absence de CSS inutile ;
- absence de chargement redondant ;
- absence de fichiers inutilisés introduits récemment.

Le Sprint ne demande pas une optimisation Lighthouse.

Simple contrôle de cohérence.

---

# 17. Corrections autorisées

L'agent peut uniquement corriger :

- incohérence SEO ;
- lien cassé ;
- erreur HTML ;
- erreur WCAG ;
- ordre CSS ;
- doublon CSS ;
- oubli de compilation ;
- oubli de build.

Tout le reste est interdit.

---

# 18. Corrections interdites

Ne jamais :

- modifier le design ;
- modifier les couleurs ;
- modifier la typographie ;
- modifier les espacements ;
- modifier les composants ;
- modifier les animations ;
- modifier les templates ;
- modifier l'architecture.

---

# 19. Livrables

Produire :

## Rapport complet

Le rapport devra contenir :

### 1.

Liste des fichiers vérifiés.

---

### 2.

Liste des fichiers modifiés.

---

### 3.

Résultat SEO.

Avec tableau complet :

- page ;
- title ;
- longueur ;
- meta ;
- longueur.

---

### 4.

Résultat WCAG.

---

### 5.

Résultat HTML.

---

### 6.

Résultat CSS.

---

### 7.

Résultat Responsive.

---

### 8.

Résultat Build.

---

### 9.

Résultat des liens.

---

### 10.

Liste précise des corrections effectuées.

---

### 11.

Confirmation finale :

- aucun nouveau composant ;
- Design System inchangé ;
- Architecture inchangée ;
- Responsive inchangé ;
- Build validé ;
- Documentation inchangée.

---

# 20. Critères d'acceptation

Le Sprint est validé uniquement si :

✅ aucun lien cassé

✅ aucun @import

✅ aucun composant recréé

✅ aucun changement d'architecture

✅ aucun changement visuel involontaire

✅ un seul H1 par page

✅ titles uniques

✅ meta descriptions uniques

✅ HTML cohérent

✅ WCAG conforme

✅ Responsive conforme

✅ Build exécuté avec succès

✅ `docs/design-system-components.md` inchangé

✅ `docs/project-architecture.md` inchangé

---

# 21. Résultat attendu

À la fin du Sprint, le projet doit être considéré comme :

- techniquement propre ;
- cohérent ;
- homogène ;
- documenté ;
- prêt pour la prochaine phase de développement.

Aucune fonctionnalité nouvelle ne doit avoir été ajoutée.

---

# Fin du Sprint 30
