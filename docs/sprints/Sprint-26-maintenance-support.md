# Sprint 26 — Page Service : Maintenance & Support

## Objectif

Créer la page détaillée **Maintenance & Support** en réutilisant intégralement le template officiel validé au Sprint 22 (`creation-site-web.html`), sans modifier son architecture ni recréer de composants existants.

Cette page doit présenter l'offre de maintenance de sites web d'Aziz Studio Digital, rassurer les visiteurs sur la sécurité et la continuité de leur site, et générer des demandes de devis.

---

# Contexte

Les pages suivantes sont déjà terminées :

- ✅ Création de site web
- ✅ Développement WordPress
- ✅ SEO & Référencement
- ✅ Refonte de site web

Toutes utilisent exactement le même template.

La page Maintenance doit suivre cette logique afin de conserver une parfaite cohérence visuelle et technique.

---

# Étape 0 — Lecture obligatoire

Avant toute modification :

Lire intégralement :

```
docs/design-system-components.md
```

Aucun composant existant ne doit être recréé.

Toutes les sections doivent réutiliser les composants déjà documentés.

---

# Architecture obligatoire

Conserver exactement les 7 sections du template :

1. Hero
2. Pourquoi ce service
3. Ce qui est inclus
4. Notre méthode
5. Pourquoi Aziz Studio Digital
6. FAQ
7. CTA Final

Aucune section supplémentaire.

Aucune suppression.

Aucune modification de structure HTML.

---

# 1. Création des fichiers

Créer :

```
pages/maintenance.html
```

Créer :

```
assets/css/pages/maintenance.css
```

Compiler ensuite :

```
maintenance.html
```

à la racine via :

```
build_index.py
```

---

# 2. Chargement CSS

Ne jamais utiliser :

```css
@import;
```

Le build doit charger séparément :

```html
<link rel="stylesheet" href="assets/css/pages/services.css" />
<link rel="stylesheet" href="assets/css/pages/creation-site-web.css" />
<link rel="stylesheet" href="assets/css/pages/maintenance.css" />
```

Vérifier explicitement que :

- services.css est bien chargé
- creation-site-web.css est chargé
- maintenance.css est chargé

Le Hero Dashboard dépend notamment de services.css.

---

# 3. Hero

Adapter uniquement le contenu.

Badge :

```
🛠 Maintenance & Support
```

H1 :

```
Maintenance de site web pour un site toujours rapide, sécurisé et disponible
```

Texte :

Mettre l'accent sur :

- sécurité
- disponibilité
- sérénité
- performances
- accompagnement continu

Dashboard :

Conserver exactement celui du template.

Adapter uniquement quelques métriques :

Exemple :

```
Disponibilité : 99,9 %

Temps de réponse

Sauvegarde OK

Sécurité active
```

---

# CTA Hero

Premier bouton :

```
Demander un devis Maintenance
```

Deuxième bouton :

```
Parler de votre projet
```

---

# 4. Pourquoi ce service

Créer 4 cartes.

Thèmes :

• éviter les pannes

• protéger contre les failles de sécurité

• garder un site rapide

• éviter les pertes de trafic et de clients

---

# 5. Ce qui est inclus

Créer 6 cartes.

Exemples :

- Sauvegardes automatiques
- Mises à jour WordPress
- Mises à jour plugins
- Monitoring du site
- Corrections de bugs
- Rapports mensuels

Ne pas copier le contenu des autres pages.

---

# 6. Notre méthode

Réutiliser exactement :

Timeline Premium

Aucune modification HTML.

Adapter uniquement les étapes.

Exemple :

Étape 1

Audit du site

Étape 2

Mise en sécurité

Étape 3

Maintenance continue

Étape 4

Suivi & assistance

---

# 7. Pourquoi Aziz Studio Digital

Créer 4 cartes spécifiques.

Exemples :

- intervention rapide
- suivi humain
- surveillance continue
- transparence

---

# 8. FAQ

Réutiliser exactement :

FAQ Premium Accordion

Créer 5 questions propres à la maintenance.

Exemples :

- À quelle fréquence effectuez-vous les sauvegardes ?
- Que comprend le contrat de maintenance ?
- Intervenez-vous en cas de panne urgente ?
- Puis-je souscrire même si mon site n'a pas été créé par vous ?
- Les mises à jour sont-elles incluses ?

Conserver les mêmes icônes SVG.

Ne recréer aucun composant.

---

# 9. CTA Final

Respecter la règle éditoriale.

Bouton principal :

```
Demander un devis Maintenance
```

Bouton secondaire :

```
Parler de votre projet
```

---

# 10. SEO

Créer un title unique.

Contraintes :

- maximum 60 caractères
- un seul séparateur |

Exemple :

```
Maintenance de site web au Congo | Aziz Studio Digital
```

Meta description :

Maximum :

```
160 caractères
```

Contenu :

Maintenance, sécurité, sauvegardes, mises à jour, support technique au Congo.

Le comptage exact n'est pas obligatoire tant que la limite est respectée.

---

# 11. Accessibilité

Conserver :

- hiérarchie H1 → H2 → H3
- aria-hidden
- alt
- breadcrumb
- détails FAQ
- navigation clavier

Aucune régression WCAG.

---

# 12. Responsive

Identique au template :

Mobile

Tablette

Desktop

Aucune nouvelle règle responsive.

---

# 13. Mise à jour des liens

Dans :

```
pages/services.html
```

Modifier la carte :

```
Maintenance & Hébergement
```

pour pointer vers :

```
maintenance.html
```

---

# 14. Build

Mettre à jour :

```
build_index.py
```

afin qu'il génère automatiquement :

```
maintenance.html
```

à la racine.

---

# 15. Documentation

Aucun nouveau composant ne doit être créé.

Par conséquent :

```
docs/design-system-components.md
```

ne doit normalement pas être modifié.

Seulement si un composant réutilisable inédit apparaît.

---

# Critères d'acceptation

✅ Template Sprint 22 conservé

✅ Aucun composant recréé

✅ services.css + creation-site-web.css + maintenance.css chargés

✅ Hero Dashboard fonctionnel

✅ Contenu 100 % spécifique Maintenance

✅ FAQ spécifique Maintenance

✅ Timeline Premium réutilisée

✅ CTA conformes à la règle éditoriale

✅ Title ≤ 60 caractères

✅ Meta description ≤ 160 caractères

✅ Responsive identique au template

✅ Lien mis à jour dans services.html

✅ build_index.py mis à jour

✅ Aucun nouveau composant Design System
