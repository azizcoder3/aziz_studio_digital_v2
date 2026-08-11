# Sprint 28 — Harmonisation finale des pages Services

## Objectif

Finaliser définitivement le module **Services** en réalisant un audit complet des six pages créées lors des Sprints 22 à 27 afin de garantir une cohérence parfaite du point de vue :

- éditorial
- SEO
- UX
- responsive
- accessibilité
- architecture
- Design System

**Aucune nouvelle fonctionnalité ne doit être créée.**

Ce sprint est exclusivement un sprint de contrôle qualité, d'harmonisation et de correction.

---

# Contexte

Les pages suivantes existent désormais :

- creation-site-web.html
- wordpress.html
- seo.html
- refonte-site.html
- maintenance.html
- audit-conseil.html

Toutes utilisent le template officiel créé au Sprint 22.

Le Design System est documenté dans :

```
docs/design-system-components.md
```

Ce document constitue désormais la référence officielle.

---

# Consigne absolue

Aucun nouveau composant HTML ou CSS ne doit être créé.

Aucune nouvelle classe CSS.

Aucune modification de l'architecture du template.

Uniquement des corrections de cohérence.

---

# Travaux à effectuer

---

# 1. Audit SEO

Vérifier les 6 pages.

Pour chacune contrôler :

- title présent
- title unique
- ≤60 caractères
- un seul séparateur "|"

Vérifier également :

- meta description présente
- meta description unique
- ≤160 caractères

Vérifier :

- un seul H1

Vérifier :

hiérarchie logique

```
H1
H2
H3
```

sans saut.

---

# 2. Audit éditorial

Vérifier que chaque page possède un contenu réellement spécifique.

Aucun paragraphe ne doit être copié mot pour mot depuis une autre page.

Contrôler notamment :

Hero

Pourquoi ce service

Prestations incluses

Méthode

FAQ

CTA final

Si une duplication est trouvée :

la reformuler.

---

# 3. Harmonisation des CTA

Contrôler les CTA selon la règle éditoriale officielle.

## Devis

Toujours :

```
Demander un devis [Service]
```

Exemples :

```
Demander un devis WordPress

Demander un devis Refonte

Demander un devis Maintenance
```

---

## Audit

Toujours :

```
Demander un audit [Service] gratuit
```

Exemple :

```
Demander un audit SEO gratuit

Demander un audit digital gratuit
```

---

## Contact

Toujours :

```
Parler de votre projet
```

---

## Portfolio

Toujours :

```
Voir nos réalisations
```

---

Aucun autre libellé ne doit subsister.

---

# 4. Vérification des Breadcrumbs

Toutes les pages doivent suivre exactement :

```
Accueil

>

Services

>

Nom du service
```

Le dernier élément doit posséder :

```
aria-current="page"
```

---

# 5. Vérification des liens

Contrôler :

Header

Footer

CTA

Portfolio

Contact

Services

Retour vers Services

Aucun lien cassé.

Aucun href incorrect.

---

# 6. Vérification du Hero Dashboard

Contrôler sur les six pages :

présence du Hero Dashboard Premium

présence des deux métriques

badge flottant

URL Badge

cartes Dashboard

Aucune structure différente.

---

# 7. Vérification des composants Premium

Comparer chaque page avec

```
docs/design-system-components.md
```

Contrôler :

Timeline Premium

FAQ Accordion

Cards

Hero

CTA Final

Dashboard

Aucun composant ne doit avoir été modifié.

---

# 8. Vérification CSS

Contrôler que chaque page compile avec exactement :

```
services.css

creation-site-web.css

CSS spécifique
```

Ordre obligatoire :

```html
<link rel="stylesheet" href="assets/css/pages/services.css" />

<link rel="stylesheet" href="assets/css/pages/creation-site-web.css" />

<link rel="stylesheet" href="assets/css/pages/xxx.css" />
```

Interdictions :

- @import

- CSS dupliqué

- feuille CSS oubliée

---

# 9. Responsive

Contrôler :

mobile

tablette

desktop

Vérifier notamment :

Hero

Timeline

FAQ

Cards

CTA

Dashboard

Grilles

---

# 10. Accessibilité WCAG

Contrôler :

navigation clavier

FAQ

Breadcrumb

aria-hidden

aria-current

alt

structure HTML5

Aucune régression.

---

# 11. Build

Contrôler :

```
build_index.py
```

Toutes les pages doivent être compilées.

Vérifier :

aucun doublon

aucune omission

aucune erreur.

Puis exécuter :

```
python build_index.py
```

---

# 12. Documentation

Ne modifier

```
docs/design-system-components.md
```

QUE

si un composant réutilisable nouveau apparaît.

Normalement :

Aucune modification.

---

# Livrables attendus

Pages vérifiées :

- creation-site-web.html
- wordpress.html
- seo.html
- refonte-site.html
- maintenance.html
- audit-conseil.html

Build exécuté.

Rapport complet.

---

# Critères d'acceptation

| Critère                                  | Statut attendu |
| ---------------------------------------- | -------------- |
| 6 pages auditées                         | ✅             |
| Titles conformes                         | ✅             |
| Meta descriptions conformes              | ✅             |
| CTA harmonisés                           | ✅             |
| Breadcrumbs conformes                    | ✅             |
| Hero Dashboard identique                 | ✅             |
| Timeline Premium conforme                | ✅             |
| FAQ Premium conforme                     | ✅             |
| Aucun nouveau composant                  | ✅             |
| Aucun @import                            | ✅             |
| Trois `<link>` CSS                       | ✅             |
| Responsive validé                        | ✅             |
| WCAG validé                              | ✅             |
| build_index.py validé                    | ✅             |
| Build exécuté                            | ✅             |
| Documentation inchangée (sauf nécessité) | ✅             |
