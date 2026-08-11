# Documentation du Projet : DentalGlow

> Template de site web premium pour cabinet dentaire — Design système Max Well
> Version 1.0.0 · © 2025 DentalGlow

---

## 1. À propos du projet

**DentalGlow** est un template de site web professionnel conçu spécifiquement pour les cabinets dentaires modernes. Il s'agit d'une solution clé en main, construite autour d'un design haut de gamme, alliant esthétique médicale sérieuse et expérience utilisateur irréprochable. Le projet repose sur une architecture modulaire basée sur **Vite**, **TailwindCSS v3** et du **JavaScript natif** enrichi par les bibliothèques d'animation **GSAP** et **Motion**.

La page d'accueil est construite dynamiquement à partir de fragments HTML indépendants (situés dans `src/sections/`), ce qui facilite grandement la personnalisation et la maintenance. Chaque section peut être modifiée, réordonnée ou supprimée sans impact sur le reste du site. Le projet est pensé pour être déployé rapidement sur des plateformes modernes comme **Vercel** ou **Netlify** en un seul clic.

**Caractéristiques techniques clés :**
- Bundler : Vite 6
- Styles : TailwindCSS 3 + CSS personnalisé (`custom.css`)
- Animations : GSAP 3 & Motion 12 (animations d'entrée, flottement, compteurs animés)
- Polices : Google Fonts — *Playfair Display* (titres) & *Plus Jakarta Sans* (corps de texte)
- Palette : Navy `#0d1b4b` / Navy-light `#1a3a8f` / Surface `#e8eaf0`
- Déploiement : Build vers `/dist` via `npm run build`

---

## 2. Aperçu du projet

DentalGlow se démarque par une approche visuelle **éditoriale et magazine**, inspirée des grandes marques de luxe et de santé haut de gamme. L'interface adopte une mise en page en grille 12 colonnes, avec une alternance savamment orchestrée de blocs blancs, de fonds doux (`#F7F8FC`) et d'images plein cadre aux bords arrondis (`rounded-3xl`, `rounded-[3rem]`).

**Points visuels distinctifs :**
- **Hero en split-screen** : la moitié gauche affiche le contenu textuel et la navigation, la moitié droite est occupée par une photographie plein format avec une carte produit flottante et animée.
- **Typographie contrastée** : alternance entre *Playfair Display* en italique pour les mots-clés émotionnels et *Plus Jakarta Sans* en gras pour la lisibilité.
- **Dégradé de texte** : les mots à fort impact (ex : *sourire*, *cabinet*) utilisent un dégradé `navy → bleu clair` via la classe `.text-gradient`.
- **Animations d'entrée séquentielles** : chaque élément de page s'anime avec un décalage progressif (`animate-enter-1` à `animate-enter-5`) pour un rendu dynamique et vivant.
- **Badge tournant** : un badge de confiance animé en rotation lente (`animate-spin-slow`, 15s) positionné en bordure de la section "À propos".
- **Défilement de partenaires** : bande de logos partenaires en défilement horizontal automatique et infini avec effet de fondu sur les bords.

---

## 3. Pages principales

Le projet comprend **trois pages HTML** principales, chacune avec son propre point d'entrée :

### 🏠 `index.html` — Page d'accueil
La page centrale du site. Elle charge dynamiquement, via JavaScript, l'ensemble des sections du dossier `src/sections/` :

| # | Section | Fichier | Contenu |
|---|---------|---------|---------|
| 01 | **Hero** | `01-hero.html` | Split-screen avec logo, titre principal, CTA "Prendre rendez-vous", carte produit flottante et défilement de partenaires |
| 02 | **À propos** | `02-about.html` | Titre éditorial avec image intégrée, compteurs animés (98% satisfaction, 500+ vies, 4.9★), photo avec badge tournant |
| 03 | **Expertises** | `03-service.html` | Accordéon de 4 spécialités dentaires, image centrale, carte descriptive avec équipe de médecins |
| 04 | **Témoignages** | `04-testimonial.html` | Slider de 4 témoignages patients avec photos, citations et notes individuelles |
| 05 | **CTA** | `05-cta.html` | Bandeau d'appel à l'action, champ de capture e-mail, coordonnées et horaires |
| 06 | **Contact** | `06-contact.html` | Formulaire complet (nom, e-mail, sujet, message) avec informations du cabinet |
| 07 | **Footer** | `07-footer.html` | Pied de page complet avec navigation, colonnes ressources, newsletter et liens légaux |

### 🦷 `about.html` — Page À propos
Page dédiée à la présentation approfondie du cabinet, de l'équipe et de la philosophie de soin. Chargée via le script `src/js/about.js`.

### ⚕️ `service.html` — Page Services / Expertises
Page de détail des spécialités et traitements proposés par le cabinet. Chargée via `src/js/service.js`.

---

## 4. Pages utilitaires et système

En plus des pages visibles, DentalGlow intègre plusieurs **composants système** transversaux qui enrichissent l'expérience sur toutes les pages :

### 📋 Sidebar de réservation — `booking-sidebar.html`
Un panneau latéral (drawer) coulissant depuis la droite de l'écran, déclenché par le bouton "Prendre rendez-vous". Il contient un formulaire avec :
- Champ : Nom complet
- Champ : Adresse e-mail
- Sélecteur : Service souhaité (Esthétique, Orthodontie, Implants, Soins préventifs)
- Champ : Message optionnel
- Bouton de confirmation avec feedback visuel

Le panneau dispose d'un **backdrop flouté** (`backdrop-blur-sm`) et d'une animation de glissement (`translate-x-full → translate-x-0`). La fermeture se fait via le bouton ✕ ou en cliquant sur le fond.

### 🗂️ Menu plein écran — `full-menu.html`
Un overlay de navigation plein écran en fond blanc, déclenché par le bouton hamburger. Il affiche :
- Les liens principaux du site en très grande typographie Playfair Display italique (*Accueil, L'Équipe, Expertises, Témoignages, Contact*)
- Chaque lien s'anime au survol avec un glissement vers la droite (`translate-x-4`)
- En bas de l'overlay : numéro de téléphone pour prendre RDV et liens réseaux sociaux
- Fermeture via un bouton ✕ avec rotation à 90° au survol

### 🎨 Styles système — `src/styles/custom.css`
Fichier CSS complémentaire à TailwindCSS contenant :
- `.text-gradient` : dégradé bleu sur les mots-clés
- `.partners-scroll` + animation `scroll-horizontal` : défilement automatique infini
- `.animate-spin-slow` : rotation continue du badge de confiance
- `.cta-btn` : micro-interaction lift au survol du bouton principal
- Animations : `floatIn`, `floatBob` pour la carte produit flottante dans le hero
- Illustration CSS de la brosse à dents dans la carte produit (`.brush-body`, `.brush-head`)

### ⚙️ JavaScript principal — `src/js/main.js`
Fichier de 14 Ko orchestrant toute la logique interactive :
- Chargement dynamique des sections HTML par injection dans `#app`
- Initialisation des animations d'entrée (GSAP / Motion)
- Gestion de l'accordéon des services
- Contrôle du slider de témoignages (navigation Précédent / Suivant + compteur)
- Animation des compteurs statistiques au scroll (`IntersectionObserver`)
- Ouverture/fermeture du menu plein écran et de la sidebar de réservation
- Simulation de soumission de formulaires avec loader et message de confirmation

---

## 5. Pourquoi ce style design Max Well ?

Le style **Max Well** est un système de design éditorial haut de gamme, pensé pour des marques qui veulent projeter à la fois **crédibilité, modernité et émotion**. Il repose sur trois piliers fondamentaux :

### ① La typographie comme architecture
Max Well s'appuie sur la **dualité typographique** : une police Serif italique (*Playfair Display*) pour les mots à charge émotionnelle (sourire, excellence, confiance, unique) et une police Sans-Serif robuste (*Plus Jakarta Sans*) pour la lisibilité du texte courant. Cette tension entre classicisme et modernité génère une hiérarchie visuelle immédiatement lisible et perçue comme premium.

### ② La palette Navy comme signature d'autorité
Le bleu marine profond (`#0d1b4b`) est associé universellement à la confiance, la compétence et le sérieux dans le secteur médical. Contrasté avec du blanc pur et des fonds gris très doux (`#F7F8FC`), il évite toute agressivité visuelle tout en affirmant l'autorité du cabinet. L'accent `navy-light` (`#1a3a8f`) apporte la subtile variation nécessaire pour les éléments interactifs.

### ③ L'animation comme signe de vie
Un site médical statique transmet de la froideur. Max Well contrebalance cela avec des **micro-animations très contrôlées** : entrées séquentielles au chargement, flottement de la carte produit, rotation lente du badge de confiance, compteurs animés au scroll. Ces animations ne distraient jamais : elles rythment la découverte du contenu et renforcent la sensation de soin apporté à chaque détail.

### ④ La mise en page magazine pour valoriser l'expertise
La grille en 12 colonnes, les images aux coins très arrondis, les éléments flottants positionnés en absolu et les blocs qui se chevauchent subtilement créent une **composition éditoriale** digne d'un magazine de santé haut de gamme. Ce choix positionne le cabinet dentaire non plus comme un simple prestataire, mais comme un acteur de référence dans son domaine.

---

## 6. Idéal pour les entreprises du secteur de la santé et du bien-être qui ont besoin de :

- **Projeter une image premium** et se différencier de la concurrence sur leur marché local
- **Convertir les visiteurs en patients** grâce à des CTA clairs (bouton "Prendre rendez-vous", formulaire de contact, sidebar de réservation)
- **Rassurer et fidéliser** grâce aux témoignages patients, aux statistiques clés (98% de satisfaction, 4.9★, 500+ vies transformées) et au badge de confiance
- **Afficher leur spécialisation** de manière structurée et visuellement attractive (accordéon des expertises : Orthodontie Invisible, Esthétique Dentaire, Implants & Prothèses, Soins Préventifs)
- **Gérer facilement leurs rendez-vous** via une interface de réservation intégrée et personnalisable
- **Mettre en valeur leur équipe** avec des photos des praticiens et une communication humaine
- **Être présents en ligne** rapidement sans développement sur mesure long et coûteux
- **Déployer et maintenir sans compétences techniques avancées**, grâce à une architecture en sections HTML indépendantes et une documentation claire

> **Secteurs directement concernés :** Cabinet dentaire, orthodontie, chirurgie orale, implantologie, clinique esthétique, cabinet de stomatologie, centre de soins bucco-dentaires.

---

## 7. Description finale

**DentalGlow** est bien plus qu'un simple template : c'est une identité numérique complète pour le cabinet dentaire du XXIe siècle. À travers une interface visuellement irréprochable, il communique instantanément les valeurs essentielles que recherche tout patient potentiel — confiance, excellence, humanité et modernité — avant même d'avoir lu une seule ligne de texte.

Chaque décision de design a été prise dans une logique de conversion et de réassurance : le hero capture l'attention et incite à l'action, la section "À propos" légitime l'expertise par les chiffres, l'accordéon des services facilite la projection du patient dans son parcours de soin, et les témoignages apportent la preuve sociale indispensable à la prise de décision. La sidebar de réservation, accessible depuis n'importe quel point de la page, raccourcit au maximum le chemin entre l'intention et l'acte.

Techniquement, le projet est construit sur des fondations solides et évolutives. La séparation du contenu (sections HTML) de la logique (JavaScript) et des styles (TailwindCSS + CSS personnalisé) garantit une maintenabilité à long terme. La compatibilité avec les services de formulaires tiers (Web3Forms, Formspree) et les plateformes de déploiement modernes (Vercel, Netlify) en fait une solution immédiatement opérationnelle.

---

## 8. Remarque finale

> **⚠️ À noter pour la mise en production :**
>
> Les formulaires de contact et de réservation intégrés fonctionnent actuellement en mode **simulation** (feedback visuel sans envoi réel d'e-mail). Pour activer l'envoi réel des messages, il est nécessaire d'intégrer un service tiers comme **Web3Forms** ou **Formspree** dans le fichier `src/js/main.js` (fonctions `initBookingSidebar` et `initContactForm`). Cette intégration est documentée dans le `README.md` et ne nécessite pas de compétences en développement back-end.
>
> Par ailleurs, les noms de partenaires affichés dans le bandeau défilant (Basecamp, DocuSign, Hopin, Attentive) sont des **données de démonstration** à remplacer par les véritables partenaires ou accréditations du cabinet. Il en va de même pour les coordonnées, les photos et les contenus textuels, tous facilement modifiables directement dans les fichiers HTML de chaque section.
>
> Ce projet constitue une **base de départ robuste et professionnelle** ; son architecture modulaire invite à le faire évoluer sereinement au rythme du développement du cabinet.

---

*Documentation rédigée le 10 juin 2026 — Projet DentalGlow v1.0.0*
