# Sprint 35 — Page À propos (`sprint-35-page-a-propos.md`)

---

# Objectif

Créer la page **À propos** (`a-propos.html`) d'Aziz Studio Digital V2.

Cette page doit renforcer la confiance en présentant :

- l'histoire du studio ;
- la vision ;
- les valeurs ;
- la méthode de travail ;
- le parcours du fondateur ;
- les engagements qualité ;
- une FAQ orientée agence ;
- un CTA final.

Cette page ne doit contenir **aucun faux chiffre**, **aucun faux témoignage**, **aucune promesse invérifiable**.

---

# Documents de référence (obligatoires)

Lire intégralement avant toute modification :

- docs/design-system-components.md
- docs/project-architecture.md
- docs/contributing.md

Ces documents sont la référence absolue.

---

# Fichiers à créer

pages/a-propos.html

assets/css/pages/a-propos.css

---

# Fichiers à modifier

build_index.py

---

# Interdictions

Ne jamais :

- créer un nouveau composant
- créer un nouveau système CSS
- utiliser @import
- casser build_index.py
- modifier les autres pages
- modifier les composants existants

Tout doit être réutilisé.

---

# Structure de la page

La page doit être composée des sections suivantes.

---

# 1 Hero Premium

Réutiliser exactement le Hero Premium des pages Services.

Dashboard Premium réutilisé.

Adapter uniquement le contenu.

Titre :

# Aziz Studio Digital, un studio web indépendant au service de votre réussite digitale

Texte :

Créer un site web est simple.
Créer un site qui inspire confiance, qui performe et qui génère des opportunités demande une vraie méthode.

Chez Aziz Studio Digital, chaque projet est conçu avec exigence, transparence et une attention particulière portée à l'expérience utilisateur, au référencement naturel et aux performances.

CTA principal

Découvrir nos solutions

→ solutions.html

CTA secondaire

Parler de votre projet

→ contact.html

Dashboard :

Badge URL

azizstudiodigital.cg

Statistiques honnêtes :

50+ sites web conçus

6 expertises maîtrisées

Approche SEO dès la conception

Floating badge

Conçu avec passion

---

# 2 Notre histoire

Section Header Premium

Titre

Une aventure née de la passion du web

Texte

Expliquer :

- découverte du développement web
- apprentissage autodidacte
- nombreux projets personnels
- volonté de créer un studio professionnel
- ambition d'aider les entreprises congolaises

3 cartes :

Passion

Apprentissage continu

Vision long terme

---

# 3 Nos valeurs

Section Header Premium

4 cartes

Transparence

Qualité

Performance

Accompagnement

Réutiliser service-feature-card.

---

# 4 Notre méthode

Réutiliser Timeline Premium.

5 étapes :

Découverte

Analyse

Conception

Développement

Suivi

---

# 5 Pourquoi Aziz Studio Digital

Réutiliser service-reason-card.

6 cartes.

Exemples :

Approche personnalisée

Code propre

SEO intégré

Responsive

Performance

Maintenance évolutive

---

# 6 Nos engagements

Section Premium.

4 cartes :

Communication claire

Délais réalistes

Documentation

Amélioration continue

---

# 7 FAQ

Réutiliser FAQ Premium.

5 questions.

Exemples :

Pourquoi avoir créé Aziz Studio Digital ?

Travaillez-vous uniquement au Congo ?

Pourquoi choisir un studio indépendant ?

Combien de temps dure un projet ?

Comment démarrer ?

---

# 8 CTA final

Réutiliser CTA Premium.

Badge

Prêt à concrétiser votre projet ?

Titre

Construisons ensemble votre présence en ligne.

Bouton primaire

Parler de votre projet

Bouton secondaire

Découvrir nos services

---

# SEO

<title>

À propos | Aziz Studio Digital

≤60 caractères.

Meta description

≤160 caractères.

H1 unique.

---

# CSS

Créer

assets/css/pages/a-propos.css

Uniquement pour les ajustements spécifiques.

Ordre :

services.css

creation-site-web.css

a-propos.css

Aucun @import.

---

# Build

Modifier build_index.py.

Compiler :

a-propos.html

---

# Vérifications

Créer

verify_sprint35.py

Contrôler :

✓ title

✓ meta

✓ H1

✓ breadcrumb

✓ FAQ

✓ Timeline

✓ Hero

✓ CTA

✓ CSS

✓ build

---

# Critères d'acceptation

✓ Aucun composant créé

✓ Hero Premium réutilisé

✓ Dashboard Premium réutilisé

✓ Timeline Premium

✓ FAQ Premium

✓ CTA Premium

✓ SEO conforme

✓ WCAG conforme

✓ Responsive

✓ build_index.py compilé

✓ Documentation inchangée

✓ Aucun faux témoignage

✓ Aucun faux chiffre

✓ Ton professionnel et humain

---

Fin du Sprint 35
