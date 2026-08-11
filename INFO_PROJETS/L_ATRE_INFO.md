# 🔥 L'ÂTRE — Fiche Complète du Projet

> **Document de présentation officielle du projet**
> Rédigé par analyse complète du code source, du design system et des composants.
> *Dernière mise à jour : Juillet 2026*

---

## 1. À propos du projet

**L'ÂTRE** est un **site vitrine one-page haut de gamme** pour une steakhouse d'exception à Paris et Monaco. Le nom "L'ÂTRE" (le foyer, la cheminée, en vieux français) porte à lui seul tout le concept de la marque : une maison qui célèbre l'art du feu et de la viande, où chaque pièce est sélectionnée, maturée avec patience, et grillée au bois de chêne.

La direction artistique retenue est **"Dark & Moody"** — un noir profond chaleureux, des accents or, une ambiance tamisée et des animations subtiles au scroll — directement inspirée des plus grandes maisons européennes et américaines de la gastronomie carnée : **Hawksmoor** (Londres), **Cut** (Beverly Hills), **L'Atelier de Joël Robuchon**, **Septime** (Paris). Le projet est explicitement positionné comme une **pièce de portfolio à haute valeur perçue**, avec une valeur de production cible affichée de **10 000 $** et un temps de développement estimé de 40 à 60 heures.

Contrairement aux précédents projets analysés (applications full-stack avec base de données), L'ÂTRE est un **site 100% frontend, sans backend ni base de données** : aucune persistance de données, aucune authentification, aucun système de réservation connecté à un vrai système de gestion — un choix assumé et cohérent avec sa nature de site vitrine premium destiné à démontrer un savoir-faire de direction artistique et de développement front-end.

**Nom du projet :** `resto-steakhouse` (dépôt), marque affichée **L'ÂTRE**
**Secteur :** Restauration gastronomique — Steakhouse haut de gamme / Site vitrine premium
**Langue :** Français
**Marché cible :** Clientèle gastronomique aisée, France (Paris) et Principauté de Monaco
**Devise :** EUR (prix affichés en euros, taxes et service compris)
**Type de projet :** Site statique, sans build step, aucune base de données

---

## 2. Aperçu du projet

### Stack technique

| Composant | Technologie | Pourquoi |
|-----------|--------------|----------|
| Structure | **HTML5 sémantique** | Pas de framework lourd, pas d'étape de build |
| Style | **Tailwind CSS** (via Play CDN) | Développement rapide, configuration custom inline |
| Interactivité | **Alpine.js** (~15 Ko) | Léger, déclaratif, adapté au périmètre du site |
| Polices | **Playfair Display** + **Cormorant Garamond** + **Inter** | Trio élégant : serif de luxe + italique + sans-serif moderne |
| Icônes | **Lucide Icons** (SVG inline) | Cohérence visuelle, contrôle du stroke, accessibilité |
| Médias | Images et **vidéo** custom (`assets/publics/`) | Photographies et vidéo d'ambiance déjà intégrées au projet |
| Animations | **CSS + IntersectionObserver** natif | Scroll-triggered reveals, performance optimale sans librairie tierce |
| Curseur personnalisé | JavaScript natif | Curseur custom pour renforcer l'expérience premium au survol |

**Aucune étape de build.** Le site peut être servi par n'importe quel serveur statique (Python `http.server`, `npx serve`, ou hébergement statique classique type Netlify — un fichier `_redirects` est d'ailleurs déjà présent à la racine).

### Palette de couleurs (Design Tokens — `design-system/MASTER.md`)

**Palette principale**

| Token | Hex | Usage |
|-------|-----|-------|
| `--bg-base` | `#0C0A09` | Fond principal (noir profond chaleureux) |
| `--bg-elevated` | `#1C1917` | Cartes, surfaces surélevées |
| `--bg-overlay` | `#292524` | Overlays, modales |
| `--border-subtle` | `#44403C` | Bordures discrètes |
| `--border-strong` | `#57534E` | Bordures marquées |
| `--text-primary` | `#FAFAF9` | Texte principal (blanc chaud) |
| `--text-secondary` | `#A8A29E` | Texte secondaire |
| `--text-muted` | `#78716C` | Texte muté / métadonnées |

**Palette d'accent**

| Token | Hex | Usage |
|-------|-----|-------|
| `--accent-gold` | `#D4AF37` | Or — CTA primaire, titres d'accent |
| `--accent-gold-bright` | `#EAB308` | Or vif (état hover) |
| `--accent-gold-dark` | `#CA8A04` | Or foncé (état pressed) |
| `--accent-ember` | `#B45309` | Braise (glow au survol, marqueurs) |
| `--accent-wine` | `#7F1D1D` | Vin (badges, étiquettes) |

**Contrastes validés WCAG** : texte principal sur fond de base 19.5:1 (AAA), texte secondaire 8.9:1 (AAA), or sur fond de base 9.2:1 (AAA) — avec la consigne explicite de n'utiliser l'or que sur fond sombre (2.1:1 sur texte clair, insuffisant).

### Typographie

| Rôle | Police | Graisses | Usage |
|------|--------|----------|-------|
| Display / Logo | **Playfair Display** | 400 à 800 | Titres hero, H1, logo |
| Display italique | **Cormorant Garamond** | 400/500 italique | Citations, accents |
| Corps de texte | **Inter** | 300 à 700 | Paragraphes, navigation |
| Petites majuscules | Inter | 500, tracking 0.2em | "Eyebrows" (labels de section) |

Le titre du Hero va de 48px (mobile) jusqu'à 128px (desktop, via `clamp()`), et la règle explicite du design system est de **ne jamais utiliser plus de deux familles de police sur un même écran**.

### Architecture des fichiers

```
resto-steakhouse-main/
├── index.html                      → Page principale (one-pager complet, ~1060 lignes)
├── design-system/
│   └── MASTER.md                    → Design system persisté (source de vérité)
├── assets/
│   ├── css/
│   │   └── style.css                 → Styles custom (animations, composants, ~1310 lignes)
│   ├── js/
│   │   └── app.js                     → Alpine.js + logique interactive (~780 lignes)
│   └── publics/
│       ├── images/                     → 11 visuels custom (chef, salle, façades, plats...)
│       └── video/
│           └── steak-chef.mp4           → Vidéo d'ambiance en fond du Hero
├── .opencode/
│   └── skills/ui-ux-pro-max/            → Skill de design utilisé pendant le développement
│       └── SKILL.md                       (base de 67 styles, 96 palettes, 57 pairings typographiques)
├── scratch/
│   ├── check_html.py                    → Script de vérification HTML
│   └── count_tags.py                     → Script utilitaire de comptage de balises
├── _redirects                            → Configuration de redirections (hébergement statique type Netlify)
├── README.md                              → Documentation complète du projet
└── .gitignore
```

---

## 3. Pages / Sections principales

Le site est un **one-pager** structuré en **9 sections** ancrées, navigables via un menu fixe et un menu mobile en panneau latéral.

### 🎬 Hero — `#hero`

Section plein écran avec **vidéo de fond en boucle** (`steak-chef.mp4`, effet "sticky scroll") plutôt qu'une simple image statique, filtre sombre léger et texture de grain pour l'ambiance. Contenu :
- Eyebrow : *"Paris · Monaco · Depuis 2008"*
- Titre : **L'ÂTRE** (jusqu'à 128px sur desktop)
- Accroche italique : *"La maison de la braise"*
- Texte d'intention : présentation de l'art du feu et de la maturation
- Double appel à l'action : "Découvrir la carte" (bouton or plein) et "Réserver une table" (bouton fantôme)
- Indicateur de scroll animé en bas de section

### 🏠 Notre Maison — `#maison`

Section manifeste avec photo de la salle principale (parallax léger) et texte de présentation :
- Histoire : maison fondée en 2008, viandes sélectionnées auprès des meilleurs élevages français, européens et japonais, maturées entre 28 et 90 jours
- Philosophie : cuisson au bois de chêne et de vigne
- **Statistiques clés animées** (compteurs incrémentaux au scroll) : 15 années d'expérience, 2 adresses d'exception, 3 étoiles Michelin (Paris & Monaco)

### 🍖 La Carte — `#carte`

Le cœur fonctionnel du site : un **menu interactif piloté par Alpine.js**, avec :
- **5 catégories** : Pour Commencer, La Braise, Maturé, Les Côtés, Desserts
- **23 plats au total**, chacun avec nom, description, origine/méta-donnée, prix en euros
- Un **toggle "Accords mets-vins"** qui révèle, pour chaque plat, une suggestion de vin associée
- Exemples de plats signature : *Côte de Bœuf Salers maturée 35 jours (140€, pour 2)*, *Wagyu A5 Japonais de Kagoshima (95€)*, *T-Bone vieilli 60 jours (180€, pour 2)*, *Côte de Bœuf maturée 90 jours de Galice (220€, pour 2)*
- Animation d'apparition échelonnée (stagger) des plats à chaque changement de catégorie

### 👨‍🍳 Le Chef — `#chef`

Portrait et biographie du **Chef Exécutif Antoine Beaumont** :
- Formation chez Alain Ducasse, Pierre Gagnaire, et trois ans à l'Eleven Madison Park (New York)
- Citation signature : *"Le feu ne ment pas. Soit on respecte la matière, soit on la trahit. Il n'y a pas de troisième voie."*
- **Frise chronologique animée** : 2008 (ouverture L'ÂTRE Paris), 2014 (première étoile Michelin), 2017 (ouverture L'ÂTRE Monaco), 2022 (seconde étoile Michelin)

### 📍 Nos Adresses — `#adresses`

Deux adresses présentées en cartes asymétriques (Paris en avant, Monaco en complément) :

| | Paris (adresse principale) | Monaco |
|---|---|---|
| **Adresse** | 14 rue du Faubourg Saint-Honoré, 75008 Paris | Avenue de la Costa, 7, 98000 Monaco |
| **Téléphone** | +33 1 42 68 15 30 | +377 97 70 30 30 |
| **Horaires** | Lun–Sam 19h–22h30, Dim 12h–14h30 | Mar–Sam 19h30–22h30 |

### 🖼️ Galerie — `#galerie`

Mosaïque de **9 photographies** (grille sur desktop, défilement horizontal tactile sur mobile) avec légendes au survol : le grill au bois de chêne, plats signature, ambiance de salle, cave à vin, gros plan Wagyu, etc.

### 📅 Réservation — `#reservation`

Formulaire de réservation complet : nom, email, téléphone, nombre de couverts (1 à "plus de 8, privatisation"), date, heure (créneaux déjeuner et dîner prédéfinis), adresse souhaitée (Paris ou Monaco), et champ libre pour allergies/occasions spéciales. Labels flottants animés, validation côté client (champs requis, format email).

### 📧 Newsletter — section dédiée

Bandeau d'inscription à la newsletter ("L'ÂTRE en privé") pour recevoir actualités, cartes saisonnières et invitations aux soirées exclusives des deux maisons.

### 🦶 Footer

Identité de marque, liens sociaux (Instagram, Facebook, TripAdvisor), coordonnées des deux adresses, horaires, mentions légales.

---

## 4. Fonctionnement technique et système

### 🍽️ Système de menu dynamique (Alpine.js)

Le menu n'est pas codé en dur dans le HTML : il repose sur un objet de données JavaScript (`window.carteData()`), qui centralise les 5 catégories et les 23 plats (nom, description, origine, prix, accord vin). Cette architecture permet de faire évoluer la carte facilement sans toucher au HTML — un choix pragmatique malgré l'absence de backend.

### 🎞️ Animations et micro-interactions

Le fichier `assets/js/app.js` orchestre une interactivité front-end riche, entièrement en JavaScript natif (sans librairie d'animation tierce) :

| Fonction | Rôle |
|----------|------|
| `initRevealOnScroll` | Animations de révélation au scroll (fade-up) via `IntersectionObserver` |
| `initScrollVideo` | Effet vidéo "sticky" en fond du Hero, lié au scroll |
| `initNavScroll` / `initActiveNavLink` | Barre de navigation qui réagit au scroll, mise en évidence du lien actif |
| `initMobileMenu` | Panneau de navigation mobile accessible |
| `initReservationForm` | Validation et simulation d'envoi du formulaire de réservation |
| `initCustomCursor` | Curseur personnalisé, renforçant l'ambiance premium |
| `initCounterAnimation` | Compteurs animés (15 ans, 2 adresses, années clés du Chef) déclenchés au scroll |
| `initParallaxImages` | Effet de parallaxe léger sur certaines images |
| `initMagneticButtons` | Effet "magnétique" sur les boutons au survol de la souris |
| `initDrawLines` | Lignes dorées qui se dessinent progressivement au scroll |
| `initGalleryMobileScroll` | Défilement horizontal tactile optimisé pour la galerie sur mobile |

### 📩 Formulaire de réservation — simulation côté client

Le formulaire de réservation effectue une **validation front-end** (champs requis, format d'email) puis affiche un message de confirmation stylisé — **il ne transmet aucune donnée à un serveur réel**. Le README documente explicitement ce point dans sa checklist de pré-livraison : *"Connecter le formulaire de réservation (backend, OpenTable, TheFork)"* reste une tâche à réaliser avant une mise en production commerciale réelle.

### 🎨 Design System persisté

Le fichier `design-system/MASTER.md` fait office de **source de vérité unique** pour l'ensemble des décisions visuelles du projet : tokens de couleur, échelle typographique, règles d'espacement, composants récurrents (boutons primaire/secondaire, cartes, champs de formulaire), spécifications d'animation, règles d'accessibilité et **liste explicite d'anti-patterns à éviter** (emojis comme icônes, dégradés "IA violet/rose", scroll-jacking, oranges saturés, etc.) — une discipline de conception rare et particulièrement soignée pour un site vitrine.

### ♿ Accessibilité (WCAG 2.1 AA)

Le site revendique une conformité **WCAG 2.1 AA validée**, avec plusieurs mesures concrètes vérifiées dans le code :
- Lien d'évitement ("skip link") en premier élément focusable
- Landmarks ARIA (`<header>`, `<main>`, `<nav>`, `<section aria-labelledby>`, `<footer>`)
- Focus visible (anneau or 2px avec décalage)
- Textes alternatifs descriptifs sur toutes les images
- Labels de formulaire explicites (jamais de placeholder seul comme label)
- Respect de `prefers-reduced-motion` pour désactiver les animations
- Cibles tactiles ≥ 44×44px
- Contrastes ≥ 4.5:1 (texte) et 3:1 (éléments d'interface)

### ⚡ Performance ciblée

Le projet fixe des objectifs Core Web Vitals précis (LCP < 2.5s, CLS < 0.1, INP < 200ms) et un score Lighthouse cible de 95+ en performance, 100 en accessibilité et en SEO — cohérent avec le choix technique de n'embarquer qu'Alpine.js (~15 Ko) et un fichier JS custom léger (~3 Ko gzip), sans framework JavaScript lourd.

---

## 5. Pourquoi ce style design "L'ÂTRE" ?

Le style visuel de L'ÂTRE est un **"Dark & Moody"** assumé et rigoureusement documenté — un parti pris esthétique fort, pensé pour transmettre le luxe sobre et intemporel d'une steakhouse gastronomique, à l'opposé des codes visuels criards ou "cheap" que le design system lui-même liste explicitement comme anti-patterns à bannir.

### 🖤 Le noir chaud (#0C0A09) comme toile de fond du luxe

Plutôt qu'un noir pur ou froid, L'ÂTRE choisit un noir "chaud" (warm deep black) qui évoque la braise et l'intimité d'un foyer — un écho direct au nom de la maison. Ce fond sombre est aussi un choix fonctionnel : il met en valeur la photographie culinaire et crée un cadre presque théâtral pour chaque plat présenté.

### ✨ L'or comme unique signature chromatique

Contrairement à des palettes multicolores, L'ÂTRE limite volontairement sa signature à une seule couleur d'accent — l'or (#D4AF37) — complétée par la braise (#B45309) en second plan. Cette discipline chromatique, associée à la règle stricte "jamais plus de deux familles de police", produit une identité visuelle immédiatement reconnaissable et évite toute dilution du message de luxe.

### ✍️ Playfair Display + Cormorant Garamond : l'élégance de l'imprimé

Le choix de deux polices serif distinctes — Playfair Display pour les titres structurants, Cormorant Garamond en italique pour les citations et accents — évoque directement les cartes de restaurants gastronomiques imprimées, ancrant le site dans les codes visuels de la haute gastronomie plutôt que dans ceux du web générique.

### 🎥 Une vidéo en Hero plutôt qu'une simple image

Le choix d'une vidéo d'ambiance en fond de Hero (plutôt qu'une image statique comme le suggérait initialement le concept) renforce l'immersion sensorielle dès la première seconde — un choix coûteux en performance mais assumé pour l'impact émotionnel recherché, contrebalancé par des optimisations techniques (préchargement, format optimisé).

### 🍷 Le toggle "Accords mets-vins" : le détail qui distingue

Cette fonctionnalité, discrète mais non triviale à développer, illustre une attention portée à l'expérience du convive averti : plutôt que d'imposer les suggestions de vin, le site laisse le visiteur choisir de les révéler — un geste d'interface qui respecte l'autonomie du client tout en valorisant l'expertise de la maison en matière d'accords.

### 📜 Une frise chronologique plutôt qu'une simple biographie

La présentation du parcours du Chef sous forme de dates clés animées (2008, 2014, 2017, 2022) transforme une biographie classique en récit de légitimité gastronomique, où chaque étoile Michelin et chaque ouverture devient un jalon visuel — un procédé narratif emprunté aux maisons de luxe établies.

### 🧭 Un design system documenté comme un vrai livrable

La présence d'un fichier `MASTER.md` complet — avec tokens, composants types, règles de contraste chiffrées et liste d'anti-patterns — dépasse largement ce qu'on attend d'un simple site vitrine. Ce niveau de documentation traduit une volonté de livrer non seulement un site, mais un véritable **système de marque réutilisable et évolutif**.

---

## 6. Idéal pour les établissements de restauration qui ont besoin...

L'ÂTRE est la base idéale pour tout restaurant gastronomique ou établissement haut de gamme souhaitant une **présence en ligne à la hauteur de son positionnement premium**.

### Secteurs concernés

- 🥩 **Steakhouses et restaurants de viande gastronomiques**
- 🍽️ **Restaurants étoilés ou aspirant à l'être**
- 🏛️ **Maisons multi-sites** (plusieurs adresses, identité de marque unifiée)
- 🍷 **Établissements avec une forte identité autour du vin et des accords mets-vins**
- 🎉 **Lieux proposant privatisations et événements exclusifs**
- 🎨 **Marques de restauration cherchant une direction artistique sur-mesure plutôt qu'un template générique**

### Ce dont ces établissements ont besoin — et que L'ÂTRE fournit

- ✅ **Une identité visuelle "Dark & Moody" mémorable**, cohérente du Hero au footer
- ✅ **Une carte interactive et filtrable par catégorie**, facile à maintenir (données centralisées en JS)
- ✅ **Un système de suggestions d'accords mets-vins** activable/désactivable par le visiteur
- ✅ **Un formulaire de réservation complet et accessible**, prêt à être connecté à un vrai système (OpenTable, TheFork, ou back-office sur-mesure)
- ✅ **Une mise en récit forte du chef et de l'histoire de la maison**, via une frise chronologique
- ✅ **Une présentation soignée du réseau d'adresses** (principale/secondaire), avec horaires et contacts
- ✅ **Une galerie immersive** pensée aussi bien pour le desktop que pour le mobile (scroll tactile)
- ✅ **Un design system documenté et réutilisable**, facilitant toute évolution future du site par une autre équipe
- ✅ **Une accessibilité et une performance pensées dès la conception**, pas ajoutées après coup
- ✅ **Un socle technique simple à héberger**, sans base de données ni serveur applicatif à maintenir

---

## 7. Description finale

**L'ÂTRE** est un site vitrine **soigné jusqu'au moindre détail**, qui démontre qu'un projet purement front-end — sans base de données, sans backend, sans framework JavaScript lourd — peut atteindre un niveau de finition et de sophistication comparable à une application complexe. Sa force ne réside pas dans la profondeur fonctionnelle (il n'y a ni compte client, ni gestion de commandes, ni back-office), mais dans la **rigueur de sa direction artistique** et la **densité de ses micro-interactions** : curseur personnalisé, boutons magnétiques, lignes dorées qui se dessinent au scroll, compteurs animés, vidéo immersive en Hero, toggle d'accords mets-vins.

Son ambition est claire : **incarner numériquement le positionnement d'une steakhouse gastronomique deux étoiles**, où chaque détail visuel — du choix des polices à la palette de couleurs, en passant par la présence d'un design system documenté — participe à raconter une histoire de patience, de feu et de matière première d'exception.

Sur le plan architectural, L'ÂTRE illustre une approche délibérément minimaliste : HTML sémantique, Tailwind via CDN, Alpine.js pour l'interactivité déclarative, et JavaScript natif pour les animations avancées — un choix qui privilégie la performance, la simplicité de maintenance et l'absence totale de dépendance à un processus de build, au prix d'une évolutivité fonctionnelle volontairement limitée (pas de CMS, pas de gestion dynamique de contenu côté serveur).

Livré avec une documentation exceptionnellement complète (README détaillé, design system `MASTER.md`, checklist de pré-livraison), le projet est prêt à être présenté comme une **pièce de portfolio haut de gamme**, ou à servir de base solide pour un restaurant réel une fois le formulaire de réservation connecté à un système réel et les dernières étapes de la checklist de livraison complétées.

---

## 8. Remarques finales

> [!NOTE]
> **Sur la nature du projet :** L'ÂTRE est un site **entièrement statique et frontend**. Aucune base de données, aucune authentification et aucun paiement ne sont implémentés — un choix cohérent avec son usage de site vitrine, mais à garder à l'esprit si le projet doit évoluer vers une plateforme de réservation transactionnelle réelle.

> [!IMPORTANT]
> **Sur le formulaire de réservation :** Le formulaire valide les champs côté client et affiche un message de confirmation, mais **n'envoie aucune donnée à un serveur réel** — c'est une simulation assumée et documentée dans le README. Avant toute mise en production commerciale, il est nécessaire de le connecter à un vrai système (email transactionnel, plateforme tierce type OpenTable/TheFork, ou back-office dédié).

> [!TIP]
> **Sur les visuels :** Contrairement à ce que suggère la checklist de pré-livraison du README ("Remplacer les images Unsplash par les photos officielles"), le projet contient déjà un jeu complet de **visuels et d'une vidéo personnalisés** (`assets/publics/images/`, `steak-chef.mp4`) plutôt que des images de stock génériques — un signe que le projet a progressé au-delà de l'étape de placeholder initialement prévue. Il reste néanmoins pertinent de vérifier les droits d'usage de chaque média avant une mise en ligne commerciale.

> [!TIP]
> **Sur le "Nombre fictif" du restaurant :** Le README précise explicitement que **L'ÂTRE est un restaurant fictif**, conçu comme démonstration de savoir-faire en direction artistique et développement front-end. Toute utilisation commerciale réelle nécessitera l'adaptation des informations (adresses, numéros de téléphone, distinctions Michelin, identité du chef) à un établissement réellement existant.

> [!TIP]
> **Sur le potentiel d'évolution :** La structure en données centralisées pour le menu (`window.carteData()`) facilite une migration future vers un CMS léger ou un fichier de configuration externe (JSON) si la carte doit être mise à jour fréquemment sans intervention d'un développeur. De même, l'ajout d'un système de réservation réel, d'un module de commande à emporter, ou d'une déclinaison multilingue (le site n'existe aujourd'hui qu'en français) constituent des extensions naturelles cohérentes avec le positionnement international de la marque (Paris/Monaco).

---

*Document rédigé par analyse automatique du code source — Projet L'ÂTRE*
*Stack : HTML5 sémantique + Tailwind CSS (Play CDN) + Alpine.js — site statique sans backend — © 2026*
