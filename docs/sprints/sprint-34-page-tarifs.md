# Sprint 34 — Construction de la page Tarifs

## Objectif

Créer la page **Tarifs** (`tarifs.html`) d'Aziz Studio Digital V2.

Cette page doit permettre aux visiteurs de comprendre rapidement les prestations proposées, les fourchettes de prix, le fonctionnement des devis et les services inclus, sans transformer le site en boutique e-commerce.

La page doit rester parfaitement cohérente avec :

- docs/design-system-components.md
- docs/project-architecture.md
- docs/contributing.md

Aucun nouveau composant ne devra être créé.

---

# Contexte

Les pages suivantes existent déjà :

- Accueil
- Solutions
- Services
- Création Site Web
- WordPress
- SEO
- Refonte
- Maintenance
- Audit & Conseil
- Portfolio

La page Tarifs doit naturellement compléter ce parcours.

---

# Architecture

Créer :

pages/tarifs.html

Créer :

assets/css/pages/tarifs.css

Compiler ensuite :

tarifs.html

à la racine du projet via build_index.py.

---

# Contraintes

Réutiliser exclusivement les composants du Design System.

Interdiction de créer :

- nouveaux composants HTML
- nouveaux composants CSS
- nouveaux layouts

Uniquement des variantes.

---

# SEO

Title :

Tarifs création de site web au Congo | Aziz Studio Digital

≤ 60 caractères.

1 seul |

Meta description :

Découvrez les tarifs de création de site web, WordPress, référencement SEO, maintenance et audit proposés par Aziz Studio Digital au Congo.

≤160 caractères.

Un seul H1.

---

# Breadcrumb

Accueil

>

Tarifs

avec

aria-current="page"

---

# Sections à créer

## 1 Hero Premium

Réutiliser exactement :

service-single-hero

avec Hero Dashboard.

Dashboard :

Devis personnalisés

↓

48h

Budget adapté

100%

Accompagnement

Projet sur mesure

CTA principal

Demander un devis

CTA secondaire

Voir nos réalisations

---

## 2 Introduction

Pourquoi nos tarifs sont-ils personnalisés ?

Expliquer :

- chaque projet est unique
- pas de prix cachés
- devis gratuit
- accompagnement

---

## 3 Nos prestations

Créer une grille de cartes présentant :

Création de site vitrine

Développement WordPress

Référencement SEO

Refonte

Maintenance

Audit digital

Chaque carte contient :

icône

titre

description

à partir de...

CTA

Découvrir le service

Utiliser les cartes Premium existantes.

---

## 4 Packs indicatifs

Créer une grille de trois cartes.

Pack Essentiel

Pack Business

Pack Premium

Chaque carte contient :

badge

titre

prix indicatif

liste d'éléments inclus

CTA

Demander un devis

IMPORTANT

Bien préciser :

Tarifs indicatifs

Chaque projet fait l'objet d'un devis personnalisé.

---

## 5 Ce qui est inclus

Réutiliser les cartes existantes.

Présenter :

analyse

UX

responsive

SEO technique

sécurité

performance

support

formation

---

## 6 Notre processus

Réutiliser Timeline Premium.

Étapes :

Découverte

Analyse

Proposition

Production

Livraison

Suivi

---

## 7 FAQ

Réutiliser FAQ Premium.

Créer 6 questions.

Exemples :

Pourquoi les prix ne sont-ils pas fixes ?

Le devis est-il gratuit ?

Quels sont les délais ?

Peut-on payer en plusieurs fois ?

Proposez-vous la maintenance ?

Travaillez-vous uniquement au Congo ?

---

## 8 CTA Final

Réutiliser :

service-cta-final-card

Titre :

Parlons de votre projet

Texte :

Chaque entreprise possède des besoins spécifiques.

Nous réalisons un devis personnalisé gratuitement.

CTA principal

Demander un devis

CTA secondaire

Nous contacter

---

# Navigation

Le menu Tarifs doit devenir actif.

Modifier build_index.py.

Compiler :

tarifs.html

---

# CSS

Créer :

assets/css/pages/tarifs.css

Ne jamais utiliser :

@import

Respecter l'ordre :

services.css

↓

creation-site-web.css

↓

tarifs.css

---

# Responsive

Tester :

375px

768px

1024px

1440px

Aucun débordement.

---

# WCAG

Respecter :

HTML5

H1 unique

Contrastes

Navigation clavier

details/summary

aria-current

aria-hidden

Focus visible

---

# Vérifications

Créer un script Python :

verify_sprint34.py

Vérifier :

SEO

Title

Meta

H1

Breadcrumb

CSS

ordre des feuilles

Responsive

Timeline

FAQ

CTA

Menu actif

Compilation

Liens

Aucun @import

---

# Critères d'acceptation

✓ Page compilée

✓ Aucun composant créé

✓ Hero Dashboard réutilisé

✓ Timeline Premium

✓ FAQ Premium

✓ Cards Premium

✓ CTA Final Premium

✓ SEO validé

✓ Responsive validé

✓ WCAG validé

✓ Build réussi

✓ Aucun @import

✓ Documentation inchangée

---

# Rapport final

Présenter :

## Fichiers créés

## Fichiers modifiés

## Composants réutilisés

## Validation SEO

## Validation WCAG

## Validation Responsive

## Validation Build

## Vérification CSS

## Vérification Python

## Critères d'acceptation

Ne jamais répondre avant :

python build_index.py

python verify_sprint34.py

Le rapport devra confirmer explicitement que tous les contrôles ont été exécutés avec succès.
