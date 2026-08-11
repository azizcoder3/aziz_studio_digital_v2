# Sprint 39 — Audit SEO global & Harmonisation technique

## Objectif

Réaliser un audit SEO complet de l'ensemble du projet **Aziz Studio Digital V2** afin de vérifier la conformité de toutes les pages HTML compilées avec les bonnes pratiques SEO techniques et les conventions du projet.

Ce Sprint est un **Sprint d'audit et d'harmonisation**, pas un Sprint de création de contenu.

Aucune nouvelle page ne doit être créée.

---

# Étape 0 — Audit complet avant toute correction (OBLIGATOIRE)

Avant toute modification, l'agent doit scanner **l'ensemble des pages HTML compilées** du projet.

Le but est de produire un état des lieux exhaustif de la situation actuelle.

Aucune correction ne doit être réalisée tant que cet audit n'est pas terminé.

---

## Pages à auditer

Toutes les pages HTML compilées doivent être incluses :

- index.html
- services.html
- creation-site-web.html
- wordpress.html
- seo.html
- refonte-site.html
- maintenance.html
- audit-conseil.html
- solutions.html
- portfolio.html
- tarifs.html
- a-propos.html
- contact.html
- blog.html
- blog-article-seo.html
- blog-article-wordpress.html
- blog-article-developpement-web.html

ainsi que toute autre page HTML compilée présente à la racine du projet.

---

# Tableau d'audit SEO obligatoire

Pour chaque page, produire un tableau contenant exactement les colonnes suivantes :

| Page | Title | Longueur | Nb " | "   | Meta description | Longueur | Canonical | Open Graph | Twitter Cards | Schema.org | Favicon | Lang HTML | Robots meta | Sitemap | Statut |
| ---- | ----- | -------- | ---- | --- | ---------------- | -------- | --------- | ---------- | ------------- | ---------- | ------- | --------- | ----------- | ------- | ------ |

Le tableau doit être rempli automatiquement.

Les longueurs doivent être mesurées par script Python.

Aucune estimation manuelle.

---

# Vérifications obligatoires

## 1. Balise `<title>`

Vérifier :

- exactement une balise
- ≤ 60 caractères
- exactement un séparateur "|"
- mot-clé principal placé avant la marque
- marque à la fin
- unicité

---

## 2. Meta description

Vérifier :

- exactement une
- ≤160 caractères
- unique
- pertinente

---

## 3. Canonical

Vérifier :

présence ou absence

si présente :

- URL correcte
- cohérente

---

## 4. Open Graph

Vérifier :

- og:title
- og:description
- og:type
- og:url
- og:image

Indiquer les balises manquantes.

---

## 5. Twitter Cards

Vérifier :

- twitter:card
- twitter:title
- twitter:description
- twitter:image

---

## 6. Schema.org

Identifier précisément :

Aucun

ou

Article

FAQPage

BreadcrumbList

Organization

WebSite

LocalBusiness

etc.

---

## 7. Favicon

Vérifier :

présence

type

chemin

---

## 8. Langue

Vérifier :

```html
<html lang="fr"></html>
```

---

## 9. Robots Meta

Présence ou absence de :

```html
<meta name="robots" ... />
```

---

## 10. Sitemap

Vérifier :

- sitemap.xml existe
- toutes les pages y figurent
- aucune page inexistante

Si sitemap.xml n'existe pas :

le signaler

sans le créer immédiatement.

---

## 11. robots.txt

Vérifier :

- existe
- contient sitemap
- directives correctes

Si absent :

le signaler

sans le créer immédiatement.

---

## 12. H1

Vérifier :

- exactement un H1

---

## 13. Hiérarchie Hn

Vérifier :

H1

↓

H2

↓

H3

↓

H4

sans saut.

---

## 14. Liens internes

Détecter :

- liens cassés
- pages orphelines
- ancres invalides

---

## 15. Images

Vérifier :

- alt présent
- images décoratives avec aria-hidden

---

# Étape 1 — Présentation de l'audit

Une fois l'audit terminé, produire un rapport listant :

## Conforme

Tout ce qui respecte déjà les règles.

## À corriger

Chaque problème détecté.

Aucune correction ne doit être masquée.

---

# Étape 2 — Corrections

Corriger uniquement les points réellement non conformes.

Ne jamais modifier un élément déjà conforme.

---

# Étape 3 — Recompilation

Exécuter :

python build_index.py

---

# Étape 4 — Vérification automatique

Créer :

verify_sprint39.py

Le script doit contrôler automatiquement :

- Titles
- Meta descriptions
- Canonical
- Open Graph
- Twitter Cards
- Schema
- H1
- Hn
- favicon
- lang
- robots meta
- liens internes
- sitemap
- robots.txt

Le script doit afficher :

PASS

ou

FAIL

pour chaque critère.

---

# Étape 5 — Captures

Captures réelles :

Desktop :

- Home
- Service
- Solutions
- Portfolio
- Blog
- Contact

montrant :

- favicon
- title
- navigation
- footer

---

# Rapport final obligatoire

Le rapport doit comporter :

## 1. Résumé exécutif

## 2. Tableau complet de l'audit SEO initial

## 3. Liste détaillée des anomalies

## 4. Corrections réalisées

## 5. Résultats de verify_sprint39.py

## 6. Vérification sitemap

## 7. Vérification robots.txt

## 8. Vérification Open Graph

## 9. Vérification Schema.org

## 10. Vérification Canonical

## 11. Vérification Hn

## 12. Vérification des liens

## 13. Captures d'écran

Chaque affirmation doit être appuyée par une capture réelle.

## 14. Conformité stratégique

✓ Aucun faux témoignage

✓ Aucun faux chiffre

✓ Aucun composant recréé

✓ Réutilisation stricte du Design System

✓ Respect de project-architecture.md

✓ Respect de contributing.md

✓ Aucun @import

✓ Build compilé

✓ Responsive

✓ WCAG

✓ SEO

✓ Aucune régression détectée

✓ Capture d'écran fournie et cohérente avec le rapport

## 15. Conclusion

Validation globale du Sprint.

---

# Contraintes absolues

Interdictions :

- créer un nouveau composant
- modifier le Design System
- modifier la structure HTML sans nécessité
- changer le contenu éditorial sans justification SEO
- modifier les CTA
- modifier les textes métier

Le Sprint est exclusivement consacré à l'audit et à l'harmonisation SEO technique.
