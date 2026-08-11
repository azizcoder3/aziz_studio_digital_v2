# Sprint 38 — Footer Premium & Navigation globale

## Objectif

Harmoniser définitivement le **Footer Premium** et la **navigation globale** sur l'ensemble du projet **Aziz Studio Digital V2**.

Ce Sprint est un Sprint de **consolidation** : aucune nouvelle fonctionnalité n'est développée. L'objectif est d'éliminer les divergences accumulées au fil des précédents Sprints et d'assurer une cohérence parfaite sur l'ensemble des pages.

---

# Étape 0 — Audit de l'existant avant correction (OBLIGATOIRE)

Le footer et la navigation ont été construits progressivement au fil des Sprints précédents.

Certaines pages ont été créées à différentes périodes du projet.

Il est donc possible que des différences se soient introduites progressivement.

**Avant toute modification**, l'agent doit réaliser un audit complet.

## Pages minimales à comparer

Comparer au minimum les pages suivantes :

- index.html
- wordpress.html
- solutions.html
- portfolio.html
- a-propos.html
- blog.html

L'agent peut en comparer davantage si nécessaire.

---

## Vérifications obligatoires

Comparer précisément :

### Navigation principale

- ordre des liens
- intitulés
- URLs
- classes CSS
- aria-current
- aria-label
- structure HTML

---

### Footer

Comparer :

- structure HTML
- colonnes
- titres
- ordre des sections
- liens
- coordonnées
- CTA
- copyright
- réseaux sociaux
- liens légaux
- boutons
- icônes
- attributs ARIA

---

### Design System

Comparer également :

- classes CSS utilisées
- composants réutilisés
- wrappers
- containers
- spacing
- variables CSS

---

## Rapport d'audit obligatoire

Avant toute correction, produire un tableau listant :

| Élément | Pages concernées | Divergence détectée | Gravité |
| ------- | ---------------- | ------------------- | ------- |

Exemples :

- lien manquant
- ordre différent
- texte différent
- structure HTML différente
- composant différent
- classe CSS différente
- accessibilité différente

---

## Choix de la version de référence

L'agent **ne doit pas supposer** que la Home est la référence.

Il doit identifier quelle version est :

- la plus récente
- la plus complète
- la plus conforme au Design System
- la plus conforme à project-architecture.md
- la plus conforme à contributing.md

Puis expliquer pourquoi cette version sera utilisée comme référence.

Seulement après cette étape, les corrections peuvent commencer.

---

# Livrables

Créer ou mettre à jour uniquement si nécessaire :

- footer.html
- header.html
- build_index.py (uniquement si indispensable)
- verify_sprint38.py
- rapport_sprint38.md
- walkthrough.md

---

# Objectifs du Sprint

## 1. Harmonisation complète du Footer Premium

Le footer doit être strictement identique sur toutes les pages.

Vérifier notamment :

- ordre des colonnes
- titres
- liens
- CTA
- coordonnées
- copyright
- liens légaux

---

## 2. Navigation globale

Contrôler :

- menu principal
- liens actifs
- aria-current
- breadcrumb
- cohérence des intitulés

---

## 3. Maillage interne

Vérifier tous les liens vers :

- Accueil
- Services
- les 6 pages Services
- Solutions
- Portfolio
- Tarifs
- À propos
- Blog
- Contact

Aucun lien cassé.

---

## 4. Mentions légales

Contrôler :

- Mentions légales
- Politique de confidentialité

Si ces pages n'existent pas encore :

- conserver les liens
- documenter leur statut
- ne pas créer leur contenu durant ce Sprint.

---

## 5. Responsive

Vérifier :

Desktop

Tablet

Mobile

Aucun débordement.

---

## 6. Accessibilité

Contrôler :

WCAG 2.1 AA

navigation clavier

focus visible

ordre logique

contrastes

ARIA

landmarks

---

## 7. Design System

Réutilisation stricte.

Aucun composant recréé.

Avant de créer quoi que ce soit :

consulter obligatoirement

docs/design-system-components.md

---

## 8. Architecture

Respect strict de

docs/project-architecture.md

---

## 9. Contributing

Respect strict de

docs/contributing.md

---

## 10. CSS

Ordre inchangé.

Aucun

@import

Variables CSS uniquement.

---

## 11. SEO

Vérifier :

Footer

Header

navigation

liens

---

## 12. Build

Compiler avec

python build_index.py

---

## 13. Vérifications automatiques

Créer

verify_sprint38.py

Le script doit contrôler :

- Footer identique sur toutes les pages
- Header identique
- Aucun lien cassé
- aria-current correct
- Footer Premium présent
- Header Premium présent
- ordre CSS
- 0 @import
- build OK

---

# Captures obligatoires

Le rapport devra contenir de vraies captures d'écran montrant :

- Home
- une page Service
- Solutions
- Portfolio
- À propos
- Blog
- Contact

Les captures devront démontrer :

- Footer identique
- Header identique
- Navigation correcte
- Responsive
- Aucun débordement

Les captures devront être cohérentes avec les affirmations du rapport.

---

# Rapport final

Le rapport devra contenir :

## 1. Résumé exécutif

## 2. Audit de l'existant

(tableau des divergences)

## 3. Version de référence retenue

(explication)

## 4. Corrections réalisées

## 5. Audit Header

## 6. Audit Footer

## 7. Audit Navigation

## 8. Audit Responsive

## 9. Audit WCAG

## 10. Audit SEO

## 11. Vérification automatique

(sortie complète de verify_sprint38.py)

## 12. Captures d'écran

## 13. Conformité stratégique

### Checklist

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

✓ Capture d'écran fournie et cohérente avec les affirmations du rapport

## 14. Conclusion

Validation finale du Sprint.
