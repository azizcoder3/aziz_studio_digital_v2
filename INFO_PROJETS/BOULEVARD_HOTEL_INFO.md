# 📋 Fiche Projet — Boulevard-Hôtel

> *Application web hôtelière full-stack moderne, conçue pour l'Hôtel Boulevard à Loutété, République du Congo.*

---

## 1. 🏨 À propos du projet

**Boulevard-Hôtel** est une application web hôtelière complète, développée avec les technologies les plus modernes du développement web. Le projet couvre l'intégralité du parcours client : de la découverte de l'établissement jusqu'à la confirmation de réservation en ligne, en passant par la consultation des chambres, des services et des équipements.

L'objectif principal est de doter l'Hôtel Boulevard — établissement de luxe situé à **Loutété, en République du Congo** — d'une présence numérique à la hauteur de son positionnement haut de gamme. Le site reflète l'âme de l'hôtel : un mariage subtil entre la chaleur de l'hospitalité congolaise et le standard d'un établissement international.

Le projet est entièrement **bilingue (Français / Anglais)**, avec gestion des devises et système d'authentification membres intégré.

**Stack technique :**
| Technologie | Usage |
|---|---|
| **Next.js 16** (App Router) | Framework React full-stack |
| **React 19** | Interface utilisateur |
| **TypeScript** | Typage statique |
| **TailwindCSS v4** | Styling utilitaire |
| **Framer Motion** | Animations & transitions |
| **Prisma ORM** | Accès base de données |
| **MongoDB** | Base de données NoSQL |
| **Resend** | Envoi d'emails transactionnels |
| **bcryptjs** | Hashage des mots de passe |
| **Iconify / Solar Icons** | Bibliothèque d'icônes |
| **Vercel** | Hébergement & déploiement |

---

## 2. 🖼 Aperçu du projet

Boulevard-Hôtel est une plateforme web professionnelle pensée autour de trois axes :

### 🛎 Expérience client
Le visiteur arrive sur une **page d'accueil immersive** avec un hero cinématique (image plein écran arrondie), une barre de recherche intelligente permettant de filtrer les chambres par dates, type et nombre de voyageurs. Il navigue ensuite naturellement à travers les sections : présentation de l'hôtel, services exclusifs, catalogue de chambres, équipements, galerie photos et vidéo de présentation.

### 🛏 Catalogue de chambres intelligent
La page `/chambres` propose un système de **filtrage avancé et en temps réel** : par dates de disponibilité, type de chambre (Standard, Deluxe Royale, Suite Senior, Présidentielle), nombre de voyageurs et nombre de chambres. Chaque chambre dispose d'une page de détail dédiée avec galerie photo, description complète, équipements, et formulaire de réservation en ligne multi-étapes.

### 🔐 Espace administration sécurisé
Un back-office complet permet à l'équipe de l'hôtel de gérer en temps réel les chambres (création, modification, suppression, gestion des promotions saisonnières) et les réservations (suivi des statuts : en attente, confirmée, annulée), avec un tableau de bord affichant les statistiques clés.

### Caractéristiques fonctionnelles principales :
- ✅ Barre de recherche avec filtres URL (check-in, check-out, type, voyageurs)
- ✅ Système de réservation en ligne multi-étapes avec récapitulatif
- ✅ Gestion des disponibilités par dates bloquées
- ✅ Offres promotionnelles saisonnières avec réduction automatique (%)
- ✅ Programme membre avec **-10% de réduction** sur tous les séjours
- ✅ Confirmation de réservation par email (Resend)
- ✅ Galerie photos avec modal plein écran
- ✅ Section vidéo cinématique
- ✅ Formulaire de contact avec sélection de sujet et réponse par email
- ✅ Interface bilingue FR / EN avec contexte de langue global
- ✅ Gestion multi-devises
- ✅ SEO optimisé (métadonnées, structure sémantique)
- ✅ Design entièrement responsive (mobile, tablette, desktop)

---

## 3. 📄 Pages principales

### 🏠 Page d'accueil — `/`
La vitrine complète de l'hôtel, construite en sections successives :

| Section | Description |
|---|---|
| **Hero** | Image cinématique plein écran avec barre de recherche intégrée (check-in, check-out, type de chambre, adultes, enfants) |
| **À Propos** | Présentation de l'hôtel en grille 3 colonnes : texte + image centrale + image latérale — style éditorial |
| **Services** | Grille des 10 équipements principaux + slider auto-animé des 4 services phares (Restaurant, Spa, Conférences, Piscine) |
| **Chambres** | Aperçu des chambres disponibles tirées de la base de données, avec prix et liens vers les détails |
| **Équipements** | Section dédiée aux commodités : Wi-Fi, Piscine, Parking, Spa, Gym, Restaurant, Conférences, Navette, Service 24h/24 |
| **Vidéo** | Section cinématique avec lecteur vidéo de présentation de l'hôtel |
| **Galerie** | Grille photos avec modal d'ouverture en plein écran |
| **Footer** | Liens rapides, coordonnées (Avenue de l'Indépendance, Loutété), réseaux sociaux, témoignage client |

### 🛏 Page Chambres — `/chambres`
Catalogue complet avec filtres avancés en temps réel : dates, type de chambre, capacité, nombre de chambres. Affichage dynamique des disponibilités. Résultats mis à jour instantanément.

### 🚪 Page Détail Chambre — `/chambres/[slug]`
Page individuelle par chambre avec galerie photo, informations complètes (superficie, étage, vue, capacité, équipements inclus), services en supplément, avis clients, et widget de réservation latéral. Chambres similaires suggérées en bas de page.

### ℹ Page À propos — `/a-propos`
Histoire et philosophie de l'hôtel, statistiques (années d'expérience, clients heureux, chambres & suites), timeline du parcours, présentation du cadre naturel de Loutété, valeurs, équipe et distinctions.

### 🍽 Page Services — `/services`
Présentation détaillée des services premium : gastronomie congolaise & internationale, espace spa & bien-être, salles de conférence modulables, piscine & loisirs. Packages tout-inclus (Évasion Romantique, Détente Totale, Séminaire Pro) et FAQ.

### 📞 Page Contact — `/contact`
Formulaire de contact avec sélection de sujet (réservation, événement, spa, groupe, etc.), coordonnées complètes, horaires de réception/restaurant/spa, accès carte, FAQ, et lien WhatsApp.

---

## 4. ⚙ Pages utilitaires et système

### 🔐 Administration — `/admin`
Espace protégé par authentification, accessible uniquement à l'équipe de l'hôtel.

| Page Admin | URL | Description |
|---|---|---|
| **Connexion Admin** | `/admin/login` | Page de connexion sécurisée (mot de passe hashé bcrypt) |
| **Tableau de bord** | `/admin` | Vue d'ensemble : total réservations, revenus estimés (XAF), nombre de chambres, réservations récentes |
| **Gestion des chambres** | `/admin/chambres` | Liste, création, modification, suppression des chambres + gestion des promotions saisonnières |
| **Gestion des réservations** | `/admin/reservations` | Suivi et mise à jour des statuts (en attente / confirmé / annulé) |

### 👤 Authentification membre — Modal `/`
Les visiteurs peuvent créer un compte membre (nom, téléphone, email optionnel, mot de passe) ou se connecter directement depuis la barre de navigation. Les membres bénéficient d'un **rabais automatique de -10%** sur toutes les réservations.

### 📡 API Routes — `/api`
Routes API internes pour la gestion des opérations serveur :
- Authentification (connexion / inscription)
- Réservations (création, envoi email de confirmation)
- Gestion des chambres (CRUD admin)

### 🌐 Système de langue — `LanguageContext`
Contexte global gérant le basculement FR ↔ EN sur l'ensemble du site, avec dictionnaires JSON complets (`fr.json`, `en.json`) pour tous les textes de l'interface.

### 💱 Système de devises — `CurrencyContext`
Contexte global permettant l'affichage des prix dans différentes devises.

### 🗄 Base de données — Prisma + MongoDB
Trois modèles principaux :
- **`Room`** : slug, nom, type, prix, galerie, équipements, capacité, lits, superficie, vue, dates bloquées, stock, promotion (start/end/discount%)
- **`User`** : nom, email (optionnel), téléphone, mot de passe hashé, statut membre
- **`Booking`** : chambre, utilisateur (optionnel), informations client, dates, prix total, statut

---

## 5. 🎨 Pourquoi ce style design « Max Well » ?

Le style **Max Well** — *Maximalisme bien calibré, épuré jusqu'à l'essentiel* — a été choisi pour Boulevard-Hôtel pour les raisons suivantes :

### 🖤 Noir & Or : La dualité du luxe
La palette chromatique repose sur un contraste fort entre **le noir profond** (autorité, sophistication) et **les tons ambrés/dorés** (`amber-700`, `#C5A08D`) qui évoquent la chaleur de l'Afrique centrale et le confort d'un établissement premium. Ce duo crée une identité visuelle immédiatement reconnaissable.

### ⬭ Formes organiques & grands rayons
Les coins très arrondis (`rounded-[45px]`, `rounded-[40px]`, `rounded-full`) confèrent une douceur et une modernité au design. Ils tranchent avec la rigidité des sites institutionnels et renforcent le sentiment de confort et de bien-être — valeurs centrales de l'hôtellerie.

### 🔤 Typographie Geist : clarté et technologie
L'utilisation des polices **Geist Sans** et **Geist Mono** (conçues par Vercel) garantit une lisibilité maximale sur tous les écrans, tout en apportant une touche contemporaine qui positionne l'hôtel comme un acteur moderne et tourné vers l'avenir.

### 🎞 Animations Framer Motion : le mouvement comme valeur
Chaque section s'anime à l'entrée dans le viewport grâce au composant `MotionReveal`. Les transitions fluides (fade-in, slide-up/left/right) créent une expérience narrative : le site se raconte au rythme de la lecture. Le slider auto-animé des services, les hover effects sur les images, les rotations d'icônes — tout concourt à une interface vivante et premium.

### 🪟 Glassmorphism & profondeur
L'usage du `backdrop-blur`, des fonds semi-transparents (`bg-white/95`, `bg-black/20`) et des ombres portées (`shadow-2xl`) crée de la profondeur visuelle. La barre de recherche flottante sur le hero en est l'illustration parfaite : un objet UI qui semble "posé" sur l'image.

### 📐 Grille éditoriale asymétrique
Les mises en page à 12 colonnes avec des répartitions non uniformes (3-6-3, 1-2) évitent la symétrie mécanique et rapprochent l'interface d'une mise en page de magazine de luxe.

---

## 6. 🎯 Idéal pour les entreprises du secteur de l'hôtellerie & tourisme haut de gamme qui ont besoin…

Boulevard-Hôtel est une solution clé en main idéale pour les établissements du **secteur de l'hospitalité, du tourisme et de l'hébergement de luxe** en Afrique et dans le monde, qui ont besoin de :

- **Une présence digitale professionnelle** reflétant leur positionnement premium, sans recourir à des solutions génériques type Booking.com
- **Un système de réservation propriétaire** sans commissions tierces — le client réserve directement, le paiement se règle sur place
- **Une gestion autonome de leur catalogue** : ajouter, modifier ou supprimer des chambres, gérer les photos, les prix et les offres promotionnelles sans compétences techniques
- **Un programme de fidélité simple** : système de membres avec avantage tarifaire intégré (-10%)
- **Une communication multicanale** : formulaire de contact, email automatique de confirmation, lien WhatsApp pour le suivi
- **Une interface administrative complète** : suivi des réservations en temps réel, statistiques de revenus, gestion des statuts
- **Un site bilingue** pour accueillir une clientèle internationale (Français & Anglais natif)
- **Des performances optimales** grâce au rendu serveur Next.js (SSR / RSC) pour un chargement rapide et un excellent référencement naturel

> 💡 Ce template convient particulièrement aux : hôtels boutique, lodges, écolodges, résidences de standing, maisons d'hôtes de luxe, centres de conférence avec hébergement, et complexes hôteliers en Afrique subsaharienne.

---

## 7. 📝 Description finale

**Boulevard-Hôtel** est bien plus qu'un simple site vitrine. C'est une **plateforme hôtelière full-stack** entièrement opérationnelle, construite avec les meilleures pratiques du développement web moderne.

Du côté client, l'application offre une expérience utilisateur soignée et fluide, guidant le visiteur de la découverte de l'hôtel jusqu'à la confirmation de sa réservation en quelques clics. La navigation est intuitive, les animations renforcent la perception de qualité, et chaque détail — du wording au moindre effet de hover — a été pensé pour inspirer confiance et désir de séjour.

Du côté administrateur, l'équipe de l'hôtel dispose d'un back-office puissant mais accessible : sans connaissance technique, un responsable peut mettre à jour l'offre de chambres, suivre les réservations, consulter les revenus estimés et gérer les promotions saisonnières.

Du côté technique, le projet repose sur une architecture robuste et scalable : Next.js App Router pour le rendu hybride (SSR + RSC), MongoDB pour la flexibilité des données hôtelières, Prisma pour la sécurité et la clarté des requêtes, et Vercel pour un déploiement continu sans friction.

**Boulevard-Hôtel** est le premier établissement hôtelier digital de Loutété — un projet qui place l'hospitalité congolaise sur la carte du numérique, avec ambition et élégance.

---

## 8. 💬 Remarque finale

> Ce projet a été conçu et développé avec une attention particulière portée à **l'identité locale** : le nom "Boulevard", les références à Loutété et à la République du Congo, les couleurs chaudes évoquant l'Afrique centrale, le système de paiement sur place adapté aux réalités du marché local — tout rappelle que la technologie doit être **au service des hommes et des territoires**, et non l'inverse.

Le code source est propre, modulaire et bien commenté, permettant une maintenance aisée et une évolution future sans refonte. Chaque composant est réutilisable, chaque contexte est découplé, et la structure de l'App Router Next.js garantit une montée en charge progressive.

**Ce projet est une fondation solide.** Il peut être enrichi de fonctionnalités additionnelles : paiement en ligne (Stripe / CinetPay), avis clients authentifiés, programme de points fidélité, gestion multi-établissements, dashboard analytique, notifications push — les bases sont posées pour aller aussi loin que l'ambition le dicte.

---

*Rédigé le 10 juin 2026 — Documentation générée à partir du code source du projet `boulevard-hotel`.*
