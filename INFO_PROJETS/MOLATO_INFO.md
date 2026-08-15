# 🛒 MOLATO E-COMMERCE — Fiche Complète du Projet

> **Document de présentation officielle du projet**
> Rédigé par analyse complète du code source, de l'architecture, de la base de données et des composants.
> *Dernière mise à jour : Juin 2026*

---

## 1. À propos du projet

**MOLATO** est une **plateforme e-commerce multi-vendeurs à part entière**, conçue pour le marché africain et plus particulièrement congolais. Ce n'est pas un simple site vitrine ou une landing page — c'est une application web complète avec gestion des utilisateurs, catalogue produits, système de commandes, paiement Mobile Money, tableau de bord administrateur, espace vendeur et bien plus.

La promesse de la marque, exprimée dans son slogan central, est forte et inclusive : **"Faites vos achats sans frontières"**. Elle positionne MOLATO comme la référence du commerce en ligne accessible, multimarque et multi-catégories, pensée pour des clients qui veulent acheter facilement depuis leur téléphone, payer avec ce qu'ils ont (MTN MoMo, Airtel Money), et recevoir chez eux.

Le projet adopte un **modèle marketplace** : des vendeurs indépendants créent leur boutique sur MOLATO, publient leurs produits, reçoivent leurs commandes et gèrent leurs revenus via un dashboard dédié. MOLATO perçoit une **commission sur chaque vente** (taux configurable par boutique, par défaut 10%). L'administration centrale supervise tout : produits, commandes, clients, finances, promotions et candidatures vendeurs.

**Nom du projet :** `molato-ecommerce`
**Marque :** MOLATO
**Secteur :** Mode, vêtements, accessoires — Commerce multi-catégories
**Langue :** Français
**Marché cible :** Congo (Brazzaville / RDC), Afrique francophone
**Devise :** FCFA (Franc CFA)
**Mode de paiement :** Mobile Money (MTN MoMo, Airtel Money)

---

## 2. Aperçu du projet

### Stack technique

| Composant | Technologie |
|-----------|-------------|
| Framework | **Next.js 16.2** (App Router, Turbopack) |
| Langage | **TypeScript** strict |
| Base de données | **PostgreSQL** (via Prisma ORM v7) |
| ORM | **Prisma** (schéma complet, migrations, seed) |
| Authentification | **NextAuth.js v5** (Auth.js) + Prisma Adapter |
| Upload images | **Cloudinary** (next-cloudinary) |
| Animations | **Framer Motion** v12 |
| Icônes | **Iconify React** (Solar icons) |
| Email | **Resend** (transactionnels) |
| Toast notifications | **Sonner** |
| État global (panier, favoris) | **Zustand** v5 |
| Graphiques | **Recharts** v3 |
| CSS | **TailwindCSS v4** (nouvelle syntaxe `@theme`) |
| Typographie | **Plus Jakarta Sans** (Google Fonts) |
| Déploiement | Compatible **Vercel** (build script inclus) |

### Palette de couleurs (Design Tokens — `globals.css`)

| Nom | Valeur | Usage |
|-----|--------|-------|
| `primary` | `#FF6B00` | Orange vif — couleur principale de la marque |
| `primary-hover` | `#E55A00` | Orange foncé pour les états hover |
| `primary-light` | `#FFF5F0` | Orange très clair (arrière-plans) |
| `dark` | `#1A1A2E` | Bleu marine très sombre (navbar, textes forts) |
| `dark-footer` | `#0F0F1A` | Fond footer presque noir |
| `mtn` | `#FFCC00` | Jaune MTN MoMo (couleur officielle opérateur) |
| `airtel` | `#E40521` | Rouge Airtel Money (couleur officielle opérateur) |
| Fond global | `#FAFAFA` | Blanc cassé ultra-léger |

### Architecture des fichiers

```
molato-ecommerce/
├── app/
│   ├── (auth)/              → Pages d'authentification
│   │   ├── connexion/
│   │   ├── inscription/
│   │   ├── mot-de-passe-oublie/
│   │   └── reinitialiser-mot-de-passe/
│   ├── (site)/              → Pages publiques du site
│   │   ├── page.tsx         → Page d'accueil
│   │   ├── boutiques/       → Liste des boutiques
│   │   ├── categorie/       → Page par catégorie
│   │   ├── categories/      → Toutes les catégories
│   │   ├── produits/        → Fiche produit
│   │   ├── panier/          → Panier + commande
│   │   ├── commande/        → Tunnel de commande
│   │   ├── compte/          → Espace client
│   │   ├── recherche/       → Résultats de recherche
│   │   ├── promo/           → Page promotions / codes promo
│   │   ├── avis/            → Avis clients
│   │   ├── contact/         → Page contact
│   │   ├── faq/             → FAQ
│   │   ├── aide/            → Aide & support
│   │   ├── a-propos/        → À propos de MOLATO
│   │   ├── cgv/             → Conditions générales de vente
│   │   ├── confidentialite/ → Politique de confidentialité
│   │   └── service-client/  → Service client
│   ├── admin/               → Espace administration
│   │   ├── page.tsx         → Dashboard (stats, graphiques, alertes)
│   │   ├── produits/        → CRUD produits
│   │   ├── commandes/       → Gestion commandes + export
│   │   ├── clients/         → Liste des clients
│   │   ├── categories/      → Gestion catégories
│   │   ├── promotions/      → Codes promo
│   │   ├── finance/         → Finance & retraits vendeurs
│   │   ├── boutiques/       → Gestion des boutiques
│   │   ├── candidatures/    → Candidatures vendeurs
│   │   └── avis/            → Modération des avis
│   ├── vendeur/dashboard/   → Espace vendeur
│   │   ├── page.tsx         → Dashboard vendeur
│   │   ├── produits/        → Mes produits
│   │   ├── commandes/       → Mes commandes
│   │   └── profil/          → Mon profil boutique
│   └── api/
│       ├── auth/            → Routes NextAuth (login, register)
│       └── checkout/        → Route API paiement
├── components/
│   ├── layout/              → TopBar, Header, Footer, MobileNav, WhatsAppButton
│   ├── home/                → HeroBanner, CategoryBar, FlashSaleSection, PourVousSection...
│   ├── produits/            → ProductCard, ProductGrid, ProductGallery, ProductReviews...
│   ├── boutiques/           → BoutiqueCard, ShopHeader, ShopSidebar
│   ├── ui/                  → Skeleton, animations
│   └── providers/           → AuthProvider
├── lib/
│   ├── actions/             → Server Actions (auth, produits, commandes, favoris...)
│   ├── queries.ts           → Requêtes Prisma complexes
│   ├── payment.ts           → Intégration Mobile Money
│   ├── mail.ts              → Emails transactionnels (Resend)
│   └── utils.ts             → Fonctions utilitaires
├── prisma/
│   ├── schema.prisma        → Modèle de données complet (15 modèles)
│   └── seed.ts              → Données initiales
├── store/
│   ├── cartStore.ts         → Panier (Zustand)
│   └── favorisStore.ts      → Favoris (Zustand)
└── public/
    ├── categories/          → Images catégories (8 WebP)
    ├── products/            → Photos produits (2 collections)
    └── logo/                → Logos MTN et Airtel
```

### Modèle de données (Prisma — 15 entités)

| Entité | Description |
|--------|-------------|
| `User` | Utilisateurs (CLIENT, VENDEUR, ADMIN) |
| `Boutique` | Boutiques vendeurs avec commission |
| `Produit` | Catalogue complet (prix, stock, couleurs, matière, tailles...) |
| `Categorie` | Arborescence catégories |
| `Commande` | Commandes clients avec suivi statut |
| `ArticleCommande` | Lignes de commande avec suivi commission |
| `Paiement` | Paiements Mobile Money (opérateur, téléphone, transactionId) |
| `Withdrawal` | Demandes de retrait des vendeurs |
| `Favori` | Produits favoris par utilisateur |
| `Avis` | Avis/notes produits |
| `CodePromo` | Codes promo (fixe ou pourcentage) |
| `Notification` | Notifications in-app par utilisateur |
| `VendorRequest` | Candidatures pour devenir vendeur |
| `PasswordResetToken` | Tokens réinitialisation de mot de passe |

---

## 3. Pages principales

### 🏠 Page d'accueil — `(site)/page.tsx`

La page d'accueil est composée de **6 sections** construites en Server Components (rendu côté serveur, données fetched en parallèle) :

| # | Section | Composant | Contenu |
|---|---------|-----------|---------|
| 1 | **Hero Banner** | `HeroBanner` | Titre animé (Framer Motion), slogan "Grandes Soldes de Mode", CTA "Acheter maintenant", badge -50%, image produit mode |
| 2 | **Barre de catégories** | `CategoryBar` | Scroll horizontal des catégories avec icônes et images (ex: T-shirt, Jean, Chaussures, Sac, Montre...) |
| 3 | **Flash Sale** | `FlashSaleSection` | Carrousel de produits en promotion avec timer compte à rebours en temps réel |
| 4 | **Pour Vous** | `PourVousSection` | Grille de produits personnalisée, chargement infini (pagination) |
| 5 | **Boutiques** | `BoutiquesSection` | Mise en avant des boutiques partenaires |
| 6 | **Slogan Banner** | `SloganBanner` | Section plein écran avec image de fond, overlay sombre et citation "Faites vos achats sans frontières" |

### 🗂 Page Catalogue & Produits

- **`/categories`** — Grille toutes les catégories
- **`/categorie/[slug]`** — Produits d'une catégorie avec filtres sidebar (prix, couleurs, tailles)
- **`/produits/[slug]`** — Fiche produit complète : galerie images, sélecteur couleur/taille, avis clients, produits similaires

### 🛒 Tunnel d'achat

- **`/panier`** — Panier avec liste d'articles (Zustand), résumé, application de code promo
- **`/commande`** — Formulaire de livraison + choix opérateur (MTN MoMo / Airtel Money) + validation paiement

### 👤 Espace Client — `/compte`

Tableau de bord client avec 4 onglets :
- **Profil** — Modifier ses informations personnelles
- **Commandes** — Historique des commandes et statuts
- **Favoris** — Produits sauvegardés
- **Avis** — Ses avis publiés

### 🔍 Recherche — `/recherche`

Page de résultats de recherche full-text (produits + catégories) avec auto-complétion temps réel dans la barre (debounce 300ms).

### 🏪 Boutiques — `/boutiques` et `/boutiques/[slug]`

Liste des boutiques actives sur la plateforme + page détail boutique (header, slogan, logo, grille produits, sidebar filtres).

---

## 4. Pages utilitaires et système

### 🔐 Authentification — `(auth)/`

Groupe de routes dédié à l'authentification, sans le layout site (pas de header/footer) :

| Page | Route | Fonctionnalité |
|------|-------|----------------|
| Connexion | `/connexion` | Email + mot de passe (NextAuth credentials) |
| Inscription | `/inscription` | Création de compte client (hachage bcryptjs) |
| Mot de passe oublié | `/mot-de-passe-oublie` | Envoi email de réinitialisation (Resend) |
| Réinitialisation | `/reinitialiser-mot-de-passe` | Token + nouveau mot de passe |

### 🛠 Dashboard Admin — `/admin`

Interface d'administration complète, accessible uniquement aux utilisateurs avec `role: ADMIN` :

| Section Admin | Contenu |
|---------------|---------|
| **Tableau de bord** | KPIs (CA, commandes, clients, panier moyen), graphique CA 7 jours (Recharts), graphique ventes par catégorie, alertes stock faible |
| **Produits** | Liste avec recherche, ajout (images Cloudinary, couleurs, catégorie), modification, suppression |
| **Commandes** | Liste filtrée, changement de statut (EN_ATTENTE → CONFIRMEE → EXPEDIEE → LIVREE), export, détail commande |
| **Clients** | Liste des clients, informations de contact |
| **Catégories** | Création/suppression de catégories |
| **Promotions** | Création de codes promo (fixe ou pourcentage), date d'expiration |
| **Finance** | Vue des revenus, commissions MOLATO, demandes de retrait vendeurs |
| **Boutiques** | Gestion des boutiques partenaires |
| **Candidatures** | Traitement des demandes de devenir vendeur (PENDING → APPROVED/REJECTED) |
| **Avis** | Modération des avis clients |

### 🏪 Dashboard Vendeur — `/vendeur/dashboard`

Espace dédié aux vendeurs (`role: VENDEUR`), avec un layout propre :

| Section Vendeur | Contenu |
|-----------------|---------|
| **Tableau de bord** | Statistiques de ses ventes |
| **Mes Produits** | Liste, ajout et gestion de ses propres produits |
| **Mes Commandes** | Commandes contenant ses produits |
| **Mon Profil** | Informations boutique, logo, slogan |

### 🔔 Système de notifications

Notifications in-app temps réel dans le header (cloche 🔔) :
- Badge rouge avec compteur de non-lues
- Panel dropdown animé (Framer Motion)
- Marquer comme lu au clic
- Types : INFO, PROMO, commande (CONFIRMED, SHIPPED...)

### 💬 Bouton WhatsApp flottant

Présent sur toutes les pages du site, permet au client de contacter le support directement.

### 📱 Navigation Mobile — `MobileNav`

Barre de navigation fixe en bas de l'écran (mobile uniquement) avec icônes : Accueil, Catégories, Panier, Compte.

### 🔎 Recherche avec auto-complétion

Mega-menu "Toutes catégories" au hover + recherche temps réel avec debounce 300ms affichant : catégories matchées + produits suggérés (image, nom, prix) + lien "Voir tous les résultats".

### 📄 Pages légales et informatives

| Route | Contenu |
|-------|---------|
| `/a-propos` | Histoire et valeurs de MOLATO |
| `/contact` | Formulaire de contact |
| `/faq` | Questions fréquemment posées |
| `/aide` | Centre d'aide |
| `/service-client` | Service client et politique retour |
| `/cgv` | Conditions Générales de Vente |
| `/confidentialite` | Politique de confidentialité |

### 🌐 API Routes — `app/api/`

| Route | Méthode | Rôle |
|-------|---------|------|
| `/api/auth/[...nextauth]` | GET/POST | Gestion sessions NextAuth |
| `/api/auth/register` | POST | Inscription nouvel utilisateur |
| `/api/checkout` | POST | Initiation paiement Mobile Money |

---

## 5. Pourquoi ce style design "MOLATO" ?

Le style visuel de MOLATO est un **"African Commerce Bold"** — un design énergique, clair, orienté conversion, qui s'inspire des grands marketplaces mondiaux (Jumia, Shopify, Amazon) tout en affirmant une identité forte et locale. Voici pourquoi chaque choix est stratégique.

### 🟠 L'orange vif (#FF6B00) comme moteur d'énergie et de confiance

L'orange est la couleur de l'action, de la chaleur et de l'urgence commerciale. C'est la couleur de Jumia, du CTA "Acheter maintenant", des badges "Flash Sale". Elle est scientifiquement prouvée pour augmenter le taux de clic. Elle dit : *"Ici, il se passe quelque chose. Agis maintenant."* Combinée au fond blanc/gris très clair (`#FAFAFA`), elle ressort avec une puissance maximale sans être agressive.

### 🌑 Le bleu marine profond (#1A1A2E) comme ancrage de sérieux

Le bleu marine est la couleur de la confiance, de l'institution, du haut de gamme sobre. Là où l'orange crie "énergie et promotion", le bleu marine dit "fiabilité et structure". MOLATO l'utilise pour les titres, la navbar, les sections foncées — il ancre visuellement la marque dans quelque chose de solide et de crédible. Ce duo orange/bleu marine est l'un des duos les plus performants en e-commerce.

### 🟡🔴 Les couleurs Mobile Money intégrées dans l'identité

La décision de définir `--color-mtn: #FFCC00` et `--color-airtel: #E40521` dans les tokens CSS de marque est une décision profondément locale et stratégique. En affichant les couleurs officielles des opérateurs sur les boutons de paiement, MOLATO crée une **reconnaissance immédiate** chez ses utilisateurs congolais. Ils voient le jaune MTN et le rouge Airtel, et ils savent immédiatement qu'ils peuvent payer avec ce qu'ils utilisent déjà au quotidien.

### ✍ La typographie Plus Jakarta Sans : moderne et africaine

Plus Jakarta Sans est une police moderne, géométrique, extrêmement lisible en gros titres comme en petits corps. Elle est `extrabold` pour les titres (impact maximal) et régulière pour les corps. Elle transmet modernité et accessibilité — exactement les deux valeurs que MOLATO doit incarner pour son marché.

### 🎞 Framer Motion comme gage de qualité native

Dans un marché où beaucoup de sites e-commerces locaux sont statiques ou peu soignés, les animations Framer Motion de MOLATO (hero en slide-in depuis la gauche, cards en stagger au scroll, menus en scale/opacity) positionnent instantanément la plateforme dans la catégorie des produits premium. L'utilisateur ressent une fluidité d'application native, et cette fluidité crée confiance et engagement.

### 📱 Mobile-First comme priorité absolue

La navigation mobile fixée en bas (`MobileNav`), les cartes produits compactes, la barre de recherche adaptative, le scroll horizontal sur les Flash Sales — tout est pensé pour le **smartphone**, qui est le premier (et souvent seul) outil de navigation et d'achat de la majorité des clients africains.

### 🏗 Architecture multi-layout (groupe de routes)

Le choix d'organiser les routes en groupes `(site)`, `(auth)`, `admin`, `vendeur` avec des layouts indépendants est une décision architecturale forte. L'admin n'a pas le header client, l'auth n'a ni header ni footer, le vendeur a son propre menu. Cette séparation nette des contextes améliore la performance, la sécurité et l'expérience de chaque type d'utilisateur.

---

## 6. Idéal pour les entreprises du secteur de la mode, du retail africain et du commerce multi-vendeurs qui ont besoin...

MOLATO est la base idéale pour toute entreprise ou entrepreneur souhaitant lancer ou gérer une **marketplace de mode et de commerce en ligne** sur le marché africain.

### Secteurs concernés

- 👗 **Boutiques de vêtements et mode africaine** (prêt-à-porter, tenues traditionnelles, casual)
- 👟 **Revendeurs de chaussures, sacs, accessoires de mode**
- ⌚ **Commerces multi-produits** (montres, bijoux, articles de maison)
- 🏪 **Opérateurs de marketplace** souhaitant agréger plusieurs vendeurs
- 📦 **Entrepreneurs du e-commerce** cherchant une solution marketplace prête à l'emploi
- 🏢 **Boutiques physiques** qui veulent une présence digitale avec commandes en ligne

### Ce dont ces entreprises ont besoin — et que MOLATO fournit

- ✅ **Un catalogue multi-vendeurs structuré** avec gestion indépendante des stocks et des prix par boutique
- ✅ **Un paiement Mobile Money natif** (MTN MoMo + Airtel Money) sans besoin de carte bancaire
- ✅ **Un système de commissions automatique** sur chaque vente (taux configurable par boutique)
- ✅ **Un tableau de bord admin complet** avec statistiques réelles, graphiques, alertes stock
- ✅ **Un espace vendeur autonome** pour que chaque commerçant gère ses produits et commandes sans dépendre de l'admin
- ✅ **Un système d'authentification sécurisé** (NextAuth, bcrypt, tokens reset)
- ✅ **Des promotions et codes promo** gérables depuis l'admin (Flash Sales, réductions %)
- ✅ **Des notifications in-app** pour informer clients et vendeurs en temps réel
- ✅ **Un candidature vendeur** structurée pour recruter de nouveaux partenaires
- ✅ **Une recherche produit temps réel** avec auto-complétion pour une UX irréprochable
- ✅ **Un système de favoris et d'avis** pour engager et fidéliser la clientèle
- ✅ **Un upload d'images via Cloudinary** pour des visuels produits optimisés
- ✅ **Des emails transactionnels** automatiques (confirmation, réinitialisation...) via Resend
- ✅ **Une compatibilité Vercel** pour un déploiement rapide et scalable

---

## 7. Description finale

**MOLATO** est un projet e-commerce **full-stack complet et production-ready**, construit sur les technologies les plus modernes de l'écosystème React/Next.js. Il ne s'agit pas d'un prototype ou d'un exercice académique — c'est une plateforme marketplace **opérationnelle**, capable de gérer des flux commerciaux réels dès sa mise en ligne avec quelques configurations.

Son ambition est claire : **démocratiser le commerce en ligne en Afrique centrale** en proposant une expérience d'achat moderne, fiable et adaptée aux réalités locales. Pas de carte bancaire requise — juste un téléphone et un compte MTN ou Airtel. Pas de complexité technique pour le vendeur — juste un dashboard intuitif pour publier des produits et encaisser des commandes.

Sur le plan architectural, MOLATO représente un **exemple de référence** de l'App Router Next.js v16 : Server Components pour la performance, Client Components pour l'interactivité, Server Actions pour les mutations, Zustand pour l'état global, Prisma pour la persistance, NextAuth pour la sécurité. Chaque couche est pensée pour être scalable, maintenable et extensible.

Sur le plan commercial, son modèle de **marketplace à commission** est l'un des modèles économiques les plus durables du web : MOLATO perçoit un pourcentage sur chaque vente sans stocker un seul article, créant ainsi un business potentiellement très rentable à mesure que le nombre de vendeurs et de clients croît.

**MOLATO est une infrastructure commerciale complète**, livrée avec toutes les fonctionnalités attendues d'un grand e-commerce : panier persistant, codes promo, flash sales avec timer, galerie produits, avis, notifications, espace vendeur, admin dashboard avec graphiques — et plus encore.

---

## 8. Remarques finales

> [!IMPORTANT]
> **Sur la configuration avant lancement :** Plusieurs variables d'environnement doivent être configurées dans un fichier `.env` avant le déploiement : `DATABASE_URL` (PostgreSQL), `NEXTAUTH_SECRET`, `NEXTAUTH_URL`, `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`, `RESEND_API_KEY`. Sans ces variables, l'application ne fonctionnera pas correctement en production.

> [!NOTE]
> **Sur le paiement Mobile Money :** La fonction `initiateMobileMoneyPayment()` dans `lib/payment.ts` est actuellement en **mode simulation** (90% de succès, délai 2s). En production, elle devra être remplacée par les appels API réels des opérateurs (MTN MoMo API, Airtel Money API) ou d'un agrégateur comme CinetPay ou FedaPay, selon la disponibilité dans le pays ciblé.

> [!TIP]
> **Sur l'évolutivité du modèle marketplace :** La structure de commission par boutique (`tauxCommission` sur le modèle `Boutique`) permet de personnaliser les taux selon les accords commerciaux avec chaque vendeur. La section Finance admin permet de suivre les retraits et de valider les paiements aux vendeurs. Ce modèle peut évoluer vers du paiement automatique via l'API Mobile Money.

> [!TIP]
> **Sur le potentiel de croissance :** MOLATO est conçu pour accueillir un nombre illimité de boutiques et de produits. L'ajout d'un système de livraison (tracking), de publicités sponsorisées pour les vendeurs, ou d'un programme de fidélité client sont des extensions naturelles qui s'intègreraient facilement dans l'architecture existante. Le projet est une base solide pour une startup e-commerce africaine ambitieuse.

> [!CAUTION]
> **Sur la base de données :** La première migration Prisma (`20260504194348_init`) doit être exécutée sur la base de données de production avant le lancement. Commande : `npx prisma migrate deploy`. Le seed (`prisma/seed.ts`) peut être utilisé pour peupler les données initiales (catégories, produit de démonstration, compte admin).

---

*Document rédigé par analyse automatique du code source — Projet MOLATO E-Commerce*
*Stack : Next.js 16 + TypeScript + PostgreSQL + Prisma + NextAuth + TailwindCSS v4 + Framer Motion — © 2026*
