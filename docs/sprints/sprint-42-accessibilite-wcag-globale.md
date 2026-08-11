# Sprint 42 — Audit & conformité Accessibilité WCAG globale

**Projet :** Aziz Studio Digital V2  
**Sprint :** 42  
**Thème :** Audit, correction et harmonisation de l'accessibilité WCAG globale  
**Objectif principal :** Auditer puis améliorer l'accessibilité de l'ensemble du site sans dégrader le Design System, le SEO, les performances, le responsive ou les fonctionnalités existantes.

---

## 0. Étape 0 — Audit complet de l'existant avant toute correction

⚠️ **OBLIGATOIRE : aucune correction ne doit être appliquée avant la réalisation et la présentation de cet audit.**

Le site a été construit et modifié progressivement sur de nombreux sprints. L'accessibilité a été traitée page par page, ce qui peut avoir créé des divergences.

L'agent doit donc commencer par auditer **toutes les pages HTML compilées du site**, et non uniquement quelques pages représentatives.

### Pages à contrôler

Scanner automatiquement toutes les pages `.html` compilées présentes à la racine du projet, notamment :

- `index.html`
- `services.html`
- `creation-site-web.html`
- `wordpress.html`
- `seo.html`
- `refonte-site.html`
- `maintenance.html`
- `audit-conseil.html`
- `solutions.html`
- `portfolio.html`
- `tarifs.html`
- `a-propos.html`
- `contact.html`
- `blog.html`
- les pages/articles individuels du Blog
- les éventuelles autres pages HTML compilées découvertes automatiquement

### L'audit initial doit produire un tableau comprenant au minimum

| Page | Langue HTML | H1  | Images alt | Navigation clavier | Focus visible | Labels formulaires | ARIA | Contraste potentiel | Headings | Liens | Boutons | FAQ/accordéon | Menu mobile | Skip link | Statut |
| ---- | ----------- | --- | ---------- | ------------------ | ------------- | ------------------ | ---- | ------------------- | -------- | ----- | ------- | ------------- | ----------- | --------- | ------ |

Pour chaque anomalie, préciser :

- page concernée ;
- élément concerné ;
- problème constaté ;
- niveau de gravité ;
- règle WCAG potentiellement concernée ;
- correction envisagée.

### Référentiel

L'audit doit principalement viser **WCAG 2.1 AA**, avec prise en compte des bonnes pratiques WCAG 2.2 lorsqu'elles sont pertinentes sans modifier inutilement l'architecture du projet.

Les critères prioritaires comprennent notamment :

- 1.1.1 — Contenu non textuel
- 1.3.1 — Informations et relations
- 1.3.2 — Ordre séquentiel
- 1.3.3 — Caractéristiques sensorielles
- 1.4.3 — Contraste minimum
- 1.4.4 — Redimensionnement du texte
- 1.4.10 — Reflow
- 1.4.11 — Contraste du contenu non textuel
- 2.1.1 — Clavier
- 2.1.2 — Pas de piège au clavier
- 2.4.1 — Contourner les blocs
- 2.4.2 — Titre de page
- 2.4.3 — Ordre du focus
- 2.4.4 — Fonction du lien
- 2.4.6 — En-têtes et étiquettes
- 2.4.7 — Focus visible
- 2.4.11 — Focus non masqué, lorsque pertinent
- 3.1.1 — Langue de la page
- 3.2.1 — Au focus
- 3.2.2 — À la saisie
- 3.3.1 — Identification des erreurs
- 3.3.2 — Étiquettes ou instructions
- 4.1.2 — Nom, rôle, valeur
- 4.1.3 — Messages d'état

---

# 1. Objectifs du Sprint

Le Sprint 42 doit permettre de :

1. détecter les problèmes d'accessibilité communs à l'ensemble du site ;
2. détecter les divergences entre les pages ;
3. corriger les problèmes réellement présents ;
4. harmoniser les comportements du Header, Footer, navigation mobile, formulaires, FAQ et CTA ;
5. garantir une navigation clavier cohérente ;
6. garantir des états `:focus` clairement visibles ;
7. vérifier les textes alternatifs des images ;
8. vérifier les labels et messages d'erreur des formulaires ;
9. vérifier la structure sémantique HTML ;
10. vérifier les attributs ARIA uniquement lorsqu'ils sont nécessaires ;
11. préserver le Design System existant ;
12. éviter toute régression visuelle ou fonctionnelle.

---

# 2. Règle absolue — Réutilisation du Design System

Avant de créer ou modifier un composant :

1. consulter `docs/design-system-components.md` ;
2. identifier le composant existant ;
3. utiliser ses classes et variantes existantes ;
4. ne pas recréer un composant déjà documenté.

Les composants concernés peuvent notamment être :

- Header Premium ;
- Navigation mobile ;
- Footer Premium ;
- Hero Dashboard ;
- Breadcrumb ;
- Cards ;
- Timeline Premium ;
- FAQ Accordion ;
- CTA Final ;
- formulaires ;
- boutons ;
- badges.

### Interdiction

Ne pas créer un nouveau composant HTML/CSS simplement parce qu'une page présente une anomalie.

Si une correction globale est nécessaire, privilégier :

- le composant source partagé ;
- le CSS global ;
- le script `build_index.py`.

---

# 3. Audit du Header et de la navigation

Vérifier sur toutes les pages :

### Navigation desktop

- structure sémantique correcte ;
- `nav` correctement identifié ;
- liens compréhensibles hors contexte ;
- état actif correctement annoncé ;
- `aria-current="page"` présent sur la page courante ;
- ordre du focus cohérent ;
- aucun élément interactif inaccessible au clavier.

### Navigation mobile

Vérifier :

- bouton hamburger accessible ;
- nom accessible du bouton ;
- `aria-expanded` correctement mis à jour ;
- `aria-controls` cohérent ;
- ouverture/fermeture au clavier ;
- fermeture avec `Escape` si prévue par le composant ;
- focus correctement géré ;
- absence de piège au clavier ;
- éléments masqués réellement inaccessibles lorsqu'ils sont fermés.

### Skip link

Vérifier si le projet possède déjà un mécanisme permettant de contourner la navigation.

Si absent :

- vérifier d'abord le Design System et l'architecture ;
- si nécessaire, ajouter un skip link global réutilisable ;
- ne pas créer une solution différente page par page.

---

# 4. Audit du Footer

Vérifier :

- `footer` sémantique ;
- liens accessibles ;
- intitulés explicites ;
- ordre logique ;
- navigation clavier ;
- focus visible ;
- contraste ;
- liens légaux ;
- liens vers Contact, Blog, Solutions, Portfolio, Tarifs, À propos et Services ;
- cohérence avec le Footer Premium validé au Sprint 38.

Aucun lien ne doit être supprimé simplement pour résoudre un problème d'accessibilité.

---

# 5. Images et contenus non textuels

Scanner toutes les images du site.

Pour chaque image :

### Image informative

Elle doit disposer d'un `alt` pertinent.

### Image décorative

Elle doit utiliser :

```html
alt=""
```
