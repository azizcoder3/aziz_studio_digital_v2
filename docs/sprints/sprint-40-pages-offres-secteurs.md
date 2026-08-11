# Sprint 40 — Pages Offres Sectorielles + Page Commande

> Document de cadrage à exécuter par l'agent de développement.
> Projet : Aziz Studio Digital V2 — architecture statique (`build_index.py`).
> **Rappel non négociable du projet** : aucune métrique commerciale inventée (pas de faux avis, pas de faux compteur de commandes, pas de fausse urgence). Toute preuve sociale doit être omise tant qu'elle n'est pas réelle.

---

## 1. Contexte et objectif

La section "Nos secteurs d'activité" de la Home (`pages/home.html`) contient 9 boutons vers des offres sectorielles (Hôtellerie, Restauration, Immobilier, Cliniques, Cabinets médicaux, Cabinets dentaires, Pharmacies, Salons de beauté, Agences de voyage). Actuellement :
- 6 boutons pointent vers des dossiers vides (`pages/hotel/`, `pages/restaurant/`, `pages/immobilier/`, `pages/clinique/`, `pages/pharmacie/`, `pages/voyage/`) → lien cassé, listing de dossier brut.
- 3 boutons (Cabinet médical, Cabinet dentaire, Salon de beauté) redirigent vers `contact.html?type=...` → à remplacer par le même système que les 6 autres pour homogénéité.
- 2 liens du footer (`components/footer.html`) — "Site hôtel", "Site restaurant" — pointent vers `services.html#hotel` et `services.html#restaurant`, des ancres qui n'existent pas dans `services.html` → à corriger dans le même sprint.

**Objectif** : créer 9 pages offre sectorielles + 1 page de commande unique, reliées par un tunnel simple : page offre → bouton "Continuer avec cette offre" → page commande pré-remplie → email de demande.

---

## 2. Portée — Les 9 secteurs

| Secteur | Dossier source | Fichier compilé (racine) |
|---|---|---|
| Hôtellerie | `pages/hotel/offre.html` | `hotel.html` |
| Restauration | `pages/restaurant/offre.html` | `restaurant.html` |
| Immobilier | `pages/immobilier/offre.html` | `immobilier.html` |
| Cliniques | `pages/clinique/offre.html` | `clinique.html` |
| Cabinets médicaux | `pages/cabinet-medical/offre.html` | `cabinet-medical.html` |
| Cabinets dentaires | `pages/cabinet-dentaire/offre.html` | `cabinet-dentaire.html` |
| Pharmacies | `pages/pharmacie/offre.html` | `pharmacie.html` |
| Salons de beauté | `pages/salon-beaute/offre.html` | `salon-beaute.html` |
| Agences de voyage | `pages/voyage/offre.html` | `voyage.html` |

> Note : conserver les dossiers `pages/[secteur]/` déjà réservés dans l'architecture (cf. `docs/project-architecture.md`), y ajouter `offre.html` comme fragment source. Créer les 2 dossiers manquants (`pages/cabinet-medical/`, `pages/cabinet-dentaire/`, `pages/salon-beaute/`).

---

## 3. Structure de chaque page offre

Réutiliser exclusivement les composants existants du Design System (`docs/design-system-components.md`) et le gabarit visuel déjà validé sur les pages projet portfolio (`pages/projet-template.html`) pour la cohérence Hero/breadcrumb/CTA. **Ne recréer aucun composant existant** — vérifier `docs/design-system-components.md` avant toute création de classe CSS.

### 3.1 Breadcrumb
Même composant que sur les pages projet (`Accueil > Secteurs > [Nom du secteur]`).

### 3.2 Hero
- Titre : "Site web pour [secteur]" (ex. "Site web pour hôtels")
- Sous-titre : une phrase reprenant la description déjà rédigée sur la carte secteur de la Home (`pages/home.html`, section `#secteurs`) — ne pas dupliquer un texte différent, réutiliser le même angle.
- Visuel : réutiliser les assets existants si disponibles dans `assets/images/`, sinon icône du secteur déjà utilisée dans la carte Home (SVG inline présent dans `pages/home.html`).

### 3.3 "Ce que vous obtenez"
Liste à puces des livrables inclus, rédigée spécifiquement par secteur (pas de texte générique copié-collé entre les 9 pages). S'inspirer du fond (pas de la forme marketing) des pages service existantes (`pages/creation-site-web.html` etc.) pour le niveau de détail attendu.
**Contrainte stricte** : aucun chiffre commercial inventé (pas de "+40% de réservations", pas de nombre de clients).

### 3.4 "Comment ça marche"
4 à 5 étapes du processus, cohérentes avec le processus déjà décrit ailleurs sur le site (page Contact : réponse sous 72h ; page Services : méthode de travail).

### 3.5 Bloc résumé (sticky, colonne latérale sur desktop / empilé sur mobile)
- Nom de l'offre
- **"À partir de [X] FCFA"** — reprendre les fourchettes déjà indiquées sur `tarifs.html` (section `#packs-indicatifs` et fourchettes par domaine d'expertise) comme référence, à adapter par secteur. Ne pas inventer un chiffre non cohérent avec les tarifs déjà publiés.
- Bouton "Continuer avec cette offre" → lien vers `commande.html?secteur=[slug]&offre=[Nom lisible encodé]&prix=[X FCFA]`
- **Aucun bloc avis clients, aucun compteur de commandes, aucune preuve sociale fabriquée.**

### 3.6 FAQ
3 à 5 questions spécifiques au secteur, format `<details>` natif (cf. `assets/js/modules/faq.js` réservé — la FAQ est actuellement gérée nativement, ne pas introduire de JS superflu).

### 3.7 Navigation entre secteurs (optionnel mais recommandé)
Reprendre le pattern "prev/next" déjà en place sur les pages projet portfolio, adapté aux 9 secteurs, pour le maillage interne SEO.

---

## 4. Page Commande (`commande.html`)

Page unique, distincte de `contact.html` (qui reste pour les demandes générales).

### 4.1 Réception des paramètres
Lit les paramètres d'URL (`secteur`, `offre`, `prix`) en JavaScript natif au chargement (`assets/js/modules/` — créer `commande.js` si nécessaire, dans le dossier réservé) pour :
- Afficher un résumé en haut de page : nom de l'offre + "À partir de [X] FCFA"
- Pré-remplir un champ caché du formulaire (`secteur_origine`) pour que l'email reçu indique clairement l'offre d'origine

### 4.2 Formulaire
Mêmes champs que `contact.html` (nom, prénom, email, téléphone optionnel, message, checkbox RGPD), **sans** le `<select>` "Type de projet" — celui-ci est déjà déterminé par la page d'origine et transmis via le champ caché.
Réutiliser le composant `form.css` existant, aucune nouvelle classe de champ.

### 4.3 Pas de code fictif
Ne pas reprendre le concept "Résumé de commande / Sous-total / Extras" du site de référence externe consulté pour l'inspiration — le modèle retenu est **devis sur mesure**, pas de grille de prix à cocher. Le seul chiffre affiché est le "À partir de X FCFA" hérité de la page offre.

---

## 5. Envoi réel du formulaire — Netlify Forms

Le formulaire de `contact.html` a actuellement `action="#"` (aucun envoi réel). À corriger dans ce même sprint, pour `commande.html` ET `contact.html` par cohérence, via **Netlify Forms** (le site est hébergé sur Netlify — solution native, sans backend à écrire) :

1. Ajouter `data-netlify="true"` et `name="commande"` (resp. `name="contact"`) à la balise `<form>`.
2. Ajouter un champ caché `<input type="hidden" name="form-name" value="commande">` (resp. `"contact"`) dans chaque formulaire.
3. Créer un fichier statique `commande.html`-only nécessaire pour Netlify au build : Netlify a besoin de détecter le formulaire au build time. Comme le site est en HTML statique compilé, s'assurer que le formulaire final compilé (pas seulement le fragment source dans `pages/`) contient bien `data-netlify="true"` — vérifier avec `netlify.toml` si un traitement particulier est nécessaire, sinon Netlify détecte automatiquement les formulaires dans le HTML statique déployé.
4. Ajouter un honeypot anti-spam simple : `<p class="hidden" data-netlify-honeypot="bot-field"><label>Ne pas remplir : <input name="bot-field"></label></p>`.
5. Rediriger après envoi vers une page de remerciement simple (`merci.html`, à créer, reprenant le header/footer standard, message de confirmation + délai de réponse 72h).
6. Documenter cette intégration dans `docs/project-architecture.md` (nouvelle section "Formulaires — Netlify Forms").

---

## 6. Mise à jour des liens existants

### 6.1 Home (`pages/home.html`)
Les 9 boutons `sector-cta` (actuellement `pages/hotel/`, `pages/restaurant/`, `pages/immobilier/`, `pages/clinique/`, `contact.html?type=cabinet-medical`, `contact.html?type=cabinet-dentaire`, `pages/pharmacie/`, `contact.html?type=salon-beaute`, `pages/voyage/`) → remplacer tous par les 9 nouvelles pages compilées (`hotel.html`, `restaurant.html`, `immobilier.html`, `clinique.html`, `cabinet-medical.html`, `cabinet-dentaire.html`, `pharmacie.html`, `salon-beaute.html`, `voyage.html`).
Les 3 liens FAQ de la Home (lignes ~1428, 1447, 1466 : "Voir nos solutions pour hôtels/restaurants/l'immobilier") pointent aussi vers `pages/hotel/` etc. → mettre à jour de la même façon.

### 6.2 Footer (`components/footer.html`)
"Site hôtel" (`services.html#hotel`) → `hotel.html`
"Site restaurant" (`services.html#restaurant`) → `restaurant.html`

### 6.3 `build_index.py`
Ajouter les 9 pages offre + `commande.html` + `merci.html` dans `pages_config`, en suivant exactement le pattern déjà utilisé (filename, source, title, description, canonical, active_nav, extra_css). Respecter le format des balises `<title>` (≤60 caractères) et meta description (≤160 caractères) déjà validé au Sprint 39 (audit SEO).

### 6.4 Sitemap
Ajouter les 11 nouvelles URLs (9 offres + commande + merci — la page merci peut être exclue du sitemap et mise en `noindex`) à `sitemap.xml`.

---

## 7. Vérification obligatoire avant validation

Conformément à la méthode établie du projet : **jamais se fier à un rapport texte seul**.
1. Script de vérification Python (sur le modèle de `verify_sprint39.py`) contrôlant : présence des 9 pages compilées, absence de lien cassé vers `pages/[secteur]/` nu, présence de `data-netlify="true"` sur les 2 formulaires, cohérence des title/meta.
2. Capture d'écran réelle d'au moins 2 pages offre différentes (desktop + mobile) et de la page `commande.html` avec paramètres pré-remplis, à fournir avant validation finale.
3. Test manuel du tunnel complet : clic sur un bouton secteur depuis la Home → page offre → "Continuer" → `commande.html` affichant le bon résumé.

---

## 8. Hors périmètre de ce sprint

- Sprint 41 (Performance / Core Web Vitals, conversion WebP)
- Sprint 42 (Accessibilité WCAG globale)
- Sprint 43 (Préparation mise en production)
- Sprint 44 (Documentation finale)
- Migration éventuelle des 3 anciens liens `contact.html?type=...` : à supprimer une fois les 9 pages en place, ne pas les laisser en doublon.
