# Sprint 36 — Page Contact (`sprint-36-page-contact.md`)

---

# Objectif

Créer la page **Contact** (`contact.html`) d'Aziz Studio Digital V2.

Cette page constitue le principal point de conversion du site.

Son objectif est de permettre à un prospect de prendre contact facilement, de comprendre le déroulement de la prise en charge de son projet et d'être rassuré sur les délais de réponse.

La page doit reprendre intégralement le Design System existant sans créer de nouveaux composants.

---

# Documents de référence (obligatoires)

Lire intégralement avant toute modification :

- docs/design-system-components.md
- docs/project-architecture.md
- docs/contributing.md

Ces documents sont la référence absolue.

---

# Fichiers à créer

pages/contact.html

assets/css/pages/contact.css

verify_sprint36.py

---

# Fichiers à modifier

build_index.py

---

# Interdictions

Ne jamais :

- créer un nouveau composant
- créer un nouveau système CSS
- modifier un composant Premium existant
- utiliser @import
- modifier une autre page
- modifier les documents du dossier docs

Tout doit être construit exclusivement avec les composants existants.

---

# Structure de la page

La page comporte exactement les sections suivantes.

---

# 1. Hero Premium

Réutiliser exactement le Hero Premium des pages Services.

Dashboard Premium réutilisé.

Titre

# Parlons de votre projet web

Texte

Vous avez un projet de création de site web, de référencement naturel, de refonte ou de maintenance ?

Décrivez votre besoin et échangeons ensemble sur la meilleure solution pour atteindre vos objectifs.

CTA principal

Envoyer une demande

(ancre vers le formulaire)

CTA secondaire

Découvrir nos solutions

→ solutions.html

Dashboard

Badge URL

contact.azizstudiodigital.cg

Statistiques honnêtes

Réponse personnalisée

Étude gratuite

Retour sous 48 heures

Floating badge

Disponible pour échanger

---

# 2. Pourquoi nous contacter

Section Header Premium.

4 cartes.

Exemples :

Conseil personnalisé

Analyse gratuite

Accompagnement

Solutions adaptées

Réutiliser service-feature-card.

---

# 3. Formulaire de contact

Utiliser exclusivement les composants existants.

Champs :

Nom

Prénom

Entreprise (facultatif)

Adresse e-mail

Téléphone (facultatif)

Type de projet

Budget indicatif

Message

Checkbox RGPD

Bouton :

Envoyer ma demande

Le formulaire reste statique (pas de backend).

Prévoir les attributs HTML5 :

required

autocomplete

type=email

type=tel

maxlength

labels

fieldset si pertinent

WCAG AA.

---

# 4. Nos coordonnées

Réutiliser les Cards Premium.

Présenter uniquement des informations réalistes.

Canaux autorisés :

Email

WhatsApp

Localisation :

Brazzaville

Ne pas ajouter :

chat en direct

support 24/7

hotline

numéro fixe fictif

équipe support

réseaux inventés

Le studio est géré par une seule personne.

Les moyens de contact doivent rester cohérents avec cette réalité.

---

# 5. Comment se déroule la prise de contact ?

Réutiliser Timeline Premium.

5 étapes :

Prise de contact

Analyse du besoin

Échange

Proposition

Lancement du projet

---

# 6. Questions fréquentes

Réutiliser FAQ Premium.

5 questions.

Exemples :

Quel est votre délai de réponse ?

Travaillez-vous à distance ?

Comment obtenir un devis ?

Faut-il déjà avoir un cahier des charges ?

Quels projets acceptez-vous ?

---

# 7. CTA Final

Réutiliser CTA Premium.

Badge

Prêt à lancer votre projet ?

Titre

Discutons ensemble de votre futur site web.

Bouton principal

Envoyer une demande

Bouton secondaire

Découvrir nos services

---

# Cohérence des engagements

Cette section est obligatoire.

Le Sprint doit vérifier automatiquement que le délai annoncé est identique sur toutes les pages.

Le délai retenu est :

48 heures

Le script de vérification doit contrôler que :

- À propos annonce 48 heures.
- Contact annonce exactement 48 heures.
- Aucune autre page ne promet un délai différent (24h, immédiat, quelques heures, etc.).

Si une incohérence est détectée :

le Sprint échoue.

---

# SEO

<title>

Contact | Aziz Studio Digital

≤60 caractères.

Meta description

≤160 caractères.

H1 unique.

Breadcrumb conforme.

---

# CSS

Créer :

assets/css/pages/contact.css

Uniquement pour les ajustements spécifiques.

Ordre obligatoire :

services.css

creation-site-web.css

contact.css

Aucun @import.

---

# Build

Modifier build_index.py.

Compiler :

contact.html

---

# Vérifications automatiques

Créer :

verify_sprint36.py

Contrôler :

✓ title

✓ meta

✓ H1

✓ breadcrumb

✓ Hero

✓ Timeline

✓ FAQ

✓ CTA

✓ CSS

✓ build

✓ ordre des feuilles CSS

✓ absence de @import

✓ cohérence du délai de réponse (48h)

✓ absence de liens cassés

---

# Captures d'écran obligatoires

Le rapport devra inclure de vraies captures d'écran.

Minimum :

Hero

Formulaire

Timeline

FAQ

CTA Final

Les captures doivent permettre de vérifier visuellement les affirmations du rapport.

---

# Rapport final

Le rapport doit contenir :

1. Fichiers créés

2. Fichiers modifiés

3. Composants réutilisés

4. SEO mesuré

5. WCAG

6. Responsive

7. Build

8. Vérifications automatiques

9. Conformité Design System

10. Conformité Architecture

11. Conformité Contributing

12. Confirmation qu'aucun nouveau composant n'a été créé

13. Confirmation qu'aucun faux chiffre n'a été utilisé

14. Confirmation qu'aucun faux témoignage n'a été utilisé

15. Vérification de la cohérence du délai de réponse

16. Captures d'écran

17. Conformité stratégique

---

# Conformité stratégique (obligatoire)

Le rapport doit contenir cette checklist :

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

Les captures d'écran doivent appuyer les affirmations du rapport.

Une simple case cochée n'est pas suffisante.

---

# Critères d'acceptation

✓ Hero Premium réutilisé

✓ Dashboard Premium réutilisé

✓ Timeline Premium

✓ FAQ Premium

✓ CTA Premium

✓ Aucun composant créé

✓ SEO conforme

✓ WCAG conforme

✓ Responsive

✓ Build compilé

✓ Aucun faux chiffre

✓ Aucun faux témoignage

✓ Cohérence du délai de réponse (48 heures)

✓ Rapport complet

---

Fin du Sprint 36
