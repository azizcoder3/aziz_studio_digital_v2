# Sprint 19 — Home FAQ Premium Accordion

## Objectif

Transformer la section **FAQ** actuellement composée de nombreuses cartes en un véritable accordéon premium.

Le résultat doit être plus compact, plus moderne, plus facile à parcourir et parfaitement cohérent avec l'identité visuelle Aziz Studio Digital V2.

Aucun JavaScript.

Utiliser uniquement :

- HTML5
- CSS
- balises natives `<details>` / `<summary>`

---

# Fichiers autorisés

Uniquement :

pages/home.html

assets/css/pages/home.css

Interdiction de modifier un autre fichier.

---

# Objectif UX

Aujourd'hui la FAQ occupe presque toute la hauteur de l'écran.

Le nouvel objectif :

- compacte
- élégante
- plus rapide à parcourir
- moins fatigante

---

# Structure demandée

Conserver :

- badge
- H2
- texte introductif

Puis remplacer toute la grille de cartes par :

```
Questions

▼ Combien coûte un site ?

▼ Combien de temps ?

▼ Mon site sera visible Google ?

▼ Travaillez-vous avec WordPress ?

▼ ...

▼ Comment démarrer ?
```

Chaque question est un accordéon.

---

# HTML

Utiliser uniquement

<details>

<summary>

<p>

Aucun JavaScript.

---

# Etat fermé

Chaque item affiche :

- icône FAQ

Question

chevron

Le texte est caché.

---

# Etat ouvert

Au clic :

l'accordéon s'ouvre

le texte apparaît

le chevron tourne

l'item reçoit :

border accentuée

léger glow

background plus clair

transition douce

---

# Animation

Transition CSS uniquement.

Animation fluide.

Environ :

250ms

Utiliser les transitions du Design System.

---

# Style

Réutiliser :

.card

.badge

.container

.section

.btn

Ne jamais casser le Design System.

---

# Responsive

Desktop

liste verticale centrée

largeur maximale :

900 px

Mobile

100%

padding confortable

grande zone de clic

---

# Accessibilité

Utiliser :

details

summary

focus-visible

navigation clavier

Aucun JS.

---

# SEO

Conserver toutes les questions existantes.

Conserver toutes les réponses.

Aucune suppression de contenu.

---

# Nouveaux sélecteurs CSS

Créer uniquement si nécessaire :

.faq-accordion

.faq-item

.faq-summary

.faq-question

.faq-answer

.faq-chevron

.faq-icon

---

# Effets Premium

Au hover :

bordure accent

léger glow

Au clic :

rotation du chevron

ouverture fluide

padding harmonieux

Au focus clavier :

outline visible

---

# Interdictions

Aucun JavaScript

Aucune bibliothèque

Aucune dépendance

Aucun inline style

Aucune couleur codée en dur

Ne modifier aucune autre section

Ne modifier aucun autre fichier

---

# Critères d'acceptation

✓ Toutes les cartes FAQ supprimées

✓ FAQ transformée en accordéons

✓ Utilisation de `<details>`

✓ Utilisation de `<summary>`

✓ Responsive

✓ Accessibilité

✓ SEO inchangé

✓ 0 JavaScript

✓ Design premium

✓ Respect intégral du Design System

---

# Livrable attendu

À la fin du Sprint fournir un rapport contenant :

- fichiers modifiés
- nouveaux sélecteurs CSS
- composants Design System utilisés
- vérification Responsive
- vérification WCAG
- vérification SEO
- conformité aux critères d'acceptation
