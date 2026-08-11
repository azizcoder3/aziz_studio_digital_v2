# Sprint 22 — Architecture & Template des Pages Services

## Objectif

Valider l'architecture technique des futures pages Services, créer le template commun réutilisable et produire une première page modèle qui servira de référence pour tous les Sprints 23 à 28.

> ⚠️ Ce sprint **ne développe pas les six services**. Il prépare l'architecture et le template qui seront réutilisés ensuite.

---

# Contexte

Après la finalisation de la Home Page et la validation du Design System, la page **Services** (`pages/services.html`) joue désormais le rôle de page de présentation.

Les détails de chaque service seront désormais répartis sur des pages dédiées afin de renforcer :

- le référencement naturel (SEO),
- la clarté de la navigation,
- la qualité des contenus,
- la maintenance du projet.

---

# Objectifs du Sprint

À la fin de ce Sprint, le projet devra disposer :

- d'une architecture de dossiers validée,
- d'un template officiel pour toutes les pages Services,
- d'une première page modèle entièrement fonctionnelle,
- d'une base technique stable pour les Sprints 23 à 28.

---

# Étape 1 — Validation de l'architecture

Avant toute implémentation, effectuer une validation technique complète.

Comparer les deux architectures suivantes.

## Option A

```
pages/
│
├── services.html
├── creation-site-web.html
├── wordpress.html
├── seo.html
├── refonte-site.html
├── maintenance.html
└── audit-conseil.html
```

## Option B

```
pages/
│
├── services.html
│
└── services/
    ├── creation-site-web.html
    ├── wordpress.html
    ├── seo.html
    ├── refonte-site.html
    ├── maintenance.html
    └── audit-conseil.html
```

L'agent doit vérifier :

- compatibilité avec `build_index.py`,
- chemins CSS,
- chemins vers les images,
- chemins vers les icônes,
- liens Header,
- liens Footer,
- Breadcrumb,
- liens internes,
- compatibilité avec le Design System.

À l'issue de cette analyse, **retenir une seule architecture**.

Le choix devra être expliqué dans le rapport.

---

# Étape 2 — Création du template officiel

Créer uniquement la page :

```
creation-site-web.html
```

Cette page devient le **template officiel**.

Les Sprints 23 à 28 reprendront exactement cette structure.

---

# Structure obligatoire

Toutes les futures pages Services devront respecter exactement la structure suivante.

```
Hero

↓

Pourquoi ce service

↓

Ce qui est inclus

↓

Notre méthode

↓

Pourquoi Aziz Studio Digital

↓

FAQ

↓

CTA Final
```

⚠️ Cette structure ne devra plus être modifiée dans les prochains sprints.

Seul le contenu changera.

---

# Section 1 — Hero

Le Hero comprend :

- Breadcrumb
- Badge
- H1
- Description
- Deux CTA
- Illustration HTML/CSS ou image optimisée

---

# Section 2 — Pourquoi ce service

Objectif :

Expliquer :

- les problèmes rencontrés,
- les enjeux,
- les bénéfices,
- les résultats attendus.

---

# Section 3 — Ce qui est inclus

Présenter les prestations sous forme de cartes.

Chaque carte comprend :

- icône
- titre
- description
- bénéfices

---

# Section 4 — Notre méthode

Réutiliser intégralement la Timeline Premium développée sur la Home.

Même :

- Design
- Composants
- CSS
- Responsive
- Animations

Seul le texte change.

---

# Section 5 — Pourquoi Aziz Studio Digital

Bloc de réassurance.

Présenter notamment :

- expertise,
- accompagnement,
- qualité,
- support,
- transparence,
- suivi.

---

# Section 6 — FAQ

Réutiliser exactement le composant :

**FAQ Premium Accordion**

développé sur la Home.

Même :

- HTML
- CSS
- JavaScript
- Animations
- Accessibilité

Seules les questions changent.

---

# Section 7 — CTA Final

Réutiliser la philosophie du CTA final de la Home.

Contenu :

- arguments
- réassurance
- boutons CTA

---

# Contraintes techniques

Respect strict de :

- HTML5
- CSS Vanilla
- JavaScript Vanilla (uniquement pour les composants déjà existants comme le FAQ Accordion)
- zéro framework
- zéro Bootstrap
- zéro bibliothèque externe
- Design System existant
- Variables CSS uniquement
- Responsive
- SEO
- WCAG AA

---

# Validation technique obligatoire

Avant de considérer le Sprint terminé :

- vérifier les chemins CSS,
- vérifier les images,
- vérifier les liens,
- vérifier le Breadcrumb,
- vérifier Header/Footer,
- vérifier build_index.py,
- ouvrir la page dans le navigateur,
- vérifier qu'il n'y a aucune erreur 404.

---

# Livrables

Créer uniquement les fichiers nécessaires.

Exemple (selon l'architecture retenue) :

```
pages/
└── creation-site-web.html
```

ou

```
pages/
└── services/
    └── creation-site-web.html
```

Créer également :

```
assets/css/pages/creation-site-web.css
```

Aucun autre service ne doit être développé durant ce Sprint.

---

# Critères d'acceptation

- ✅ Architecture validée
- ✅ Choix de l'architecture justifié
- ✅ Chemins vérifiés
- ✅ Compatibilité avec `build_index.py`
- ✅ Template commun créé
- ✅ Une seule page modèle réalisée
- ✅ Hero complet
- ✅ Les 7 sections présentes
- ✅ Responsive
- ✅ SEO optimisé
- ✅ Accessibilité WCAG
- ✅ Réutilisation maximale du Design System
- ✅ Aucun fichier inutile modifié
- ✅ Aucune erreur 404
- ✅ Rapport complet fourni

---

# Résultat attendu

À l'issue de ce Sprint, le projet disposera d'un **template officiel unique** pour toutes les futures pages Services.

Les Sprints suivants auront uniquement pour objectif de personnaliser ce template avec le contenu spécifique de chaque service, garantissant ainsi une parfaite cohérence graphique, technique et SEO sur l'ensemble du site.
