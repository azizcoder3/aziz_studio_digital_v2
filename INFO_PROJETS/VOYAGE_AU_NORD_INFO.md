# 🚌 VOYAGE AU NORD (Océan du Nord v2) — Fiche Complète du Projet

> **Document de présentation officielle du projet**
> Rédigé par analyse complète du code source, de l'architecture, de la base de données et des composants.
> *Dernière mise à jour : Juillet 2026*

---

## 1. À propos du projet

**Voyage au Nord** est la **version 2, matures et durcie**, de la plateforme **Océan du Nord** : une application complète de réservation de billets de bus en ligne pour le marché congolais. Le nom du dépôt et du déploiement a évolué (`Voyage-au-nord`, hébergé sur `voyage-au-nord.vercel.app`), mais l'identité de marque affichée aux utilisateurs reste **Océan du Nord**, avec le même positionnement : **"Réservez vos billets de bus Océan du Nord en ligne. Voyagez en toute sécurité entre Brazzaville, Pointe-Noire, Ouesso et plus de 40 destinations au Congo."**

Cette version 2 conserve l'intégralité des fonctionnalités du projet d'origine (réservation, sélection de sièges, paiement Mobile Money, billetterie QR Code, assistante IA "Océane", programme de fidélité "Club ONC", services annexes) et y ajoute une **couche de maturité technique et opérationnelle significative** : migration de la base de données vers **MongoDB Atlas**, remplacement de Supabase par **Cloudinary** pour le stockage d'images, un **éditeur de texte riche** pour la gestion des actualités, un système de **campagnes newsletter** envoyées en masse, un **middleware de sécurité** dédié à la protection des routes d'administration, et un dispositif **anti-fraude renforcé** au moment du scan des billets à l'embarquement.

Le projet est accompagné d'une documentation interne étoffée (guides de sécurité, guide développeur paiement, guide d'utilisation, rapport de migration), signe d'un projet arrivé à un stade d'exploitation réelle et destiné à être audité ou transmis à un acquéreur/exploitant.

**Nom du projet :** `ocean-du-nord-v2` (dépôt `Voyage-au-nord`)
**Marque affichée :** Océan du Nord
**Secteur :** Transport interurbain de voyageurs — Compagnie de bus / Agence de voyage
**Langue :** Français
**Marché cible :** République du Congo (Brazzaville, Pointe-Noire, Dolisie et 40+ destinations)
**Devise :** FCFA / XAF (Franc CFA)
**Mode de paiement :** Mobile Money (MTN MoMo, Airtel Money) via l'agrégateur **Yabetoo**
**URL de déploiement :** `voyage-au-nord.vercel.app`

---

## 2. Aperçu du projet

### Stack technique

| Composant | Technologie |
|-----------|-------------|
| Framework | **Next.js 16.1** (App Router, Webpack) |
| Langage | **TypeScript** strict |
| Runtime UI | **React 19.2** |
| Base de données | **MongoDB Atlas** (via Prisma ORM — *migration depuis PostgreSQL/Supabase*) |
| ORM | **Prisma** v6.19 (schéma adapté au format `ObjectId` MongoDB) |
| Authentification | **NextAuth.js v5** (Auth.js beta), configuration scindée `auth.ts` / `auth.config.ts` compatible **Edge Middleware** |
| Middleware de sécurité | **`middleware.ts`** — protection RBAC de toutes les routes `/admin/*` |
| Paiement | **Yabetoo SDK** (agrégateur Mobile Money congolais, devise XAF) |
| Intelligence Artificielle | **Google Generative AI (Gemini)** — assistante "Océane" |
| Stockage d'images | **Cloudinary** (upload unsigned + transformations d'URL optimisées) |
| Éditeur de texte riche | **Tiptap** (StarterKit, Underline, Placeholder) pour la rédaction d'articles |
| SMS transactionnels | **Twilio** |
| Email transactionnels & campagnes | **Nodemailer** + **Resend** |
| Génération de billets PDF | **@react-pdf/renderer** + **jsPDF** + **html2canvas** |
| QR Code | **qrcode**, **qrcode.react** (génération) + **html5-qrcode** (scan à l'embarquement) |
| Cartographie | **@react-google-maps/api**, **Leaflet / react-leaflet** |
| PWA | **@ducanh2912/next-pwa** (installable, manifest, service worker) |
| Carrousel / Slider | **Swiper** v12 |
| Animations | **Framer Motion** v12 |
| Icônes | **lucide-react** |
| Graphiques (admin) | **Recharts** v3 |
| Notifications toast | **Sonner** |
| CSS | **TailwindCSS v4** (nouvelle syntaxe `@theme`) |
| Typographie | **Poppins** (Google Fonts) |
| Déploiement | **Vercel** (`voyage-au-nord.vercel.app`) |

### Palette de couleurs (Design Tokens — `globals.css`)

| Nom | Valeur | Usage |
|-----|--------|-------|
| `primary` | `#064e3b` | Vert foncé — couleur principale de la marque |
| `primary-light` | `#10b981` | Vert émeraude clair (accents, hover) |
| `secondary` | `#f59e0b` | Jaune Or — CTA, boutons d'action, badges |
| `accent` | `#dc2626` | Rouge — alertes, urgence |
| `bg-soft` | `#f8fafc` | Fond global gris très clair |

*(Palette identique à la v1 — l'identité visuelle n'a pas changé, seule l'infrastructure technique a évolué.)*

### Architecture des fichiers

```
ocean-du-nord-v2 (Voyage-au-nord)/
├── middleware.ts               → 🆕 Protection RBAC des routes /admin/* (Edge)
├── auth.ts                      → Configuration NextAuth (providers, Prisma)
├── auth.config.ts               → 🆕 Config NextAuth allégée compatible Edge (callbacks, JWT)
├── app/
│   ├── page.tsx                 → Page d'accueil
│   ├── booking/                  → Tunnel de réservation
│   │   ├── page.tsx              → Résultats de recherche + sélection sièges
│   │   ├── checkout/              → Paiement Mobile Money
│   │   └── success/               → Confirmation + billet
│   ├── destinations/              → Liste et détail des destinations
│   ├── ocean-du-nord/              → Pages institutionnelles (agences, tarifs, multimedia)
│   ├── services/                    → Courrier, Fret, Location
│   ├── onc/                          → Programme de fidélité "Club ONC"
│   ├── oceane/                        → Page assistante IA "Océane"
│   ├── actualites/                     → Blog / actualités (édition via Tiptap)
│   ├── contact/, login/, register/, profile/
│   ├── admin/
│   │   ├── page.tsx                    → Dashboard (revenus, statistiques)
│   │   ├── bus/, routes/, trajets/       → Gestion flotte, itinéraires, trajets programmés
│   │   ├── reservations/, utilisateurs/
│   │   ├── actualites/                    → 🆕 Éditeur riche (RichTextEditor / Tiptap)
│   │   ├── newsletter/                     → 🆕 Campagnes d'envoi + historique
│   │   │   ├── SendCampaignForm.tsx
│   │   │   ├── CampaignHistory.tsx
│   │   │   ├── NewsletterTable.tsx
│   │   │   └── actions.ts
│   │   └── scan/                            → Scanner QR Code d'embarquement (anti-fraude)
│   └── api/
│       ├── auth/, bookings/, payment/, webhooks/yabetoo/
│       ├── chat/                              → IA "Océane" (Gemini)
│       ├── articles/, newsletter/unsubscribe/
│       ├── routes/, trips/, profile/
│       └── admin/
│           ├── stats/
│           ├── manifest/[tripId]/               → Génération manifeste de bord par trajet
│           └── verify-ticket/                    → 🆕 Vérification serveur-à-serveur anti-fraude
├── components/
│   ├── layout/, home/, booking/, destination/, pdf/
│   ├── admin/
│   │   ├── DashboardChart.tsx, RevenueAreaChart.tsx
│   │   └── RichTextEditor.tsx                    → 🆕 Éditeur Tiptap pour les actualités
│   └── ui/, providers/
├── lib/
│   ├── prisma.ts, yabetoo-helper.ts, sms.ts, mail.ts, utils.ts, constants.ts
│   └── cloudinary.ts                              → 🆕 Upload et optimisation d'images (remplace Supabase)
├── prisma/
│   ├── schema.prisma                               → 🆕 Adapté MongoDB (ObjectId), champs Route étendus
│   └── seed.ts
├── fix-admin.js                                     → 🆕 Script utilitaire de réparation de compte admin
├── GUIDE_SECURITE.md                                 → 🆕 Documentation de l'architecture de sécurité
├── GUIDE_UTILISATION.md                               → 🆕 Guide d'utilisation de la plateforme
├── GUIDE_DEVELOPPEUR_PAIEMENT.md                       → 🆕 Documentation technique du flux de paiement
├── MIGRATION_MONGODB.md                                 → 🆕 Documentation de la migration PostgreSQL → MongoDB
└── rapport-walkthrough-migration-supabase-vers-mongodb-atlas.md → 🆕 Rapport de migration Supabase → MongoDB Atlas
```

### Modèle de données (Prisma — MongoDB)

| Entité | Description |
|--------|--------------|
| `User` | Utilisateurs (rôles USER, ADMIN, AGENT — désormais stockés en `String` plutôt qu'en `enum`, contrainte du provider MongoDB), identifiés par téléphone, avec points fidélité |
| `Bus` | Flotte de véhicules (nom, immatriculation, capacité, type VIP/Standard, équipements) |
| `Route` | Itinéraires — 🆕 enrichis avec `via` (route nationale empruntée : N1, N2, N3, RN1...) et `days` (jours de circulation) |
| `Trip` | Trajets programmés (date, statut, bus assigné, agence de départ) |
| `Booking` | Réservations (référence unique, prix total, statut, méthode et ID de paiement) |
| `Passenger` | Passagers rattachés à une réservation (nom, type adulte/enfant, numéro de siège) |
| `Article` | Articles du blog (contenu HTML riche généré par l'éditeur Tiptap) |
| `NewsletterSubscriber` | Abonnés à la newsletter |
| `NewsletterCampaign` | 🆕 Historique des campagnes d'emailing envoyées (sujet, contenu, date d'envoi, nombre de destinataires, statut) |

*(Les `enum` Prisma classiques — `Role`, `TripStatus`, `BookingStatus`, `PassengerType` — ont été convertis en champs `String` avec valeurs documentées en commentaire, MongoDB/Prisma ne supportant pas les enums natifs de la même manière que PostgreSQL.)*

---

## 3. Pages principales

*(Le périmètre fonctionnel des pages publiques est identique à la v1 — la fiche se concentre ici sur les évolutions majeures ; se référer à la fiche Océan du Nord v1 pour le détail complet des pages inchangées.)*

### 🏠 Page d'accueil, Réservation, Destinations, Institutionnel, Fidélité, Assistante IA, Services, Actualités, Espace client, Contact

Toutes ces sections sont **reprises à l'identique** de la version 1 (Hero avec recherche de trajet, sélection de sièges, paiement Mobile Money, page Club ONC, page Océane, services Courrier/Fret/Location, etc.).

### 📰 Actualités — enrichies d'un éditeur riche

La rédaction des articles dans l'administration s'appuie désormais sur un **éditeur de texte riche (Tiptap)** avec barre d'outils (gras, italique, souligné, titres H2/H3, listes à puces/numérotées, citations, bloc de code) et un mode "source" pour éditer le HTML brut directement — une nette évolution par rapport à un simple champ texte.

### 🗺️ Itinéraires enrichis

Les itinéraires (`Route`) intègrent désormais deux nouvelles informations exploitables côté admin et potentiellement côté public : la **route nationale empruntée** (`via` — ex. "N1", "RN1") et les **jours de circulation** (`days`), permettant de préciser qu'un trajet ne circule pas tous les jours de la semaine.

---

## 4. Pages utilitaires et système

### 🔐 Authentification & Middleware de sécurité — 🆕 évolution majeure

- **`middleware.ts`** intercepte toute requête vers `/admin/:path*` **avant même le rendu de la page**, au niveau Edge, et bloque l'accès si l'utilisateur n'est pas connecté ou n'a pas le rôle `ADMIN`.
- **`auth.config.ts`** sépare la configuration NextAuth compatible Edge (callbacks JWT/session, page de connexion) de `auth.ts` qui contient les providers dépendants de Prisma — une bonne pratique qui évite d'exposer le client Prisma (non compatible Edge Runtime) au middleware.
- Chaque route API sensible (ex. `/api/admin/verify-ticket`) revérifie indépendamment le rôle de session (`ADMIN` ou `AGENT`) côté serveur, en plus du filtrage du middleware — défense en profondeur.

### 🛠️ Dashboard Admin — `/admin`

Conserve l'ensemble des sections de la v1 (Tableau de bord, Bus, Itinéraires, Trajets, Réservations, Utilisateurs, Scan) avec deux évolutions notables :

| Section | Évolution |
|---------|-----------|
| **Actualités** | Édition via `RichTextEditor` (Tiptap) au lieu d'un champ texte brut |
| **Newsletter** | Passe d'une simple liste d'abonnés à un véritable **outil de campagne d'emailing** : `SendCampaignForm` (rédaction avec éditeur riche + envoi), `CampaignHistory` (historique des envois avec statut et nombre de destinataires), `NewsletterTable` (gestion des abonnés) |

### 🎫 Sécurisation renforcée du scan de billets (anti-fraude)

Le système de contrôle d'embarquement a été durci avec une logique de vérification **intelligente et serveur-à-serveur**, décrite dans `GUIDE_SECURITE.md` et implémentée dans `/api/admin/verify-ticket` :

- **Anti-replay strict** : dès qu'un billet passe de `PAID` à `USED`, tout nouveau scan du même billet est rejeté avec un message explicite ("Billet déjà utilisé").
- **Vérification directe du paiement** : si une réservation est encore au statut `PENDING` au moment du scan, le serveur interroge en direct l'API Yabetoo (`api.yabetoopay.com/api/v1/sessions/{paymentId}`) avec la clé secrète serveur pour confirmer ou infirmer le paiement avant d'autoriser l'embarquement — empêchant la fabrication de faux billets.
- **Contrôle de rôle** : seuls les comptes `ADMIN` et `AGENT` peuvent appeler cette route.

### 📄 Manifeste de bord par trajet

Nouvelle route dédiée `/api/admin/manifest/[tripId]` pour générer le manifeste PDF des passagers **directement associé à un trajet précis**, en complément du composant `ManifestPDF` existant.

### 🖼️ Gestion des images — migration vers Cloudinary

`lib/cloudinary.ts` remplace l'intégration Supabase Storage de la v1 :
- Upload *unsigned* côté client vers un dossier structuré `odn-media/{folder}` (ex. `odn-media/actualites`, `odn-media/routes`)
- Génération d'URLs optimisées à la volée (redimensionnement, qualité et format automatiques `w_{width},q_{quality},f_{format}`)
- Fonction `getResponsiveUrls()` fournissant des variantes mobile/tablette/desktop pour l'affichage responsive

### 🗄️ Migration de base de données PostgreSQL → MongoDB Atlas

Documentée dans `MIGRATION_MONGODB.md` et le rapport de walkthrough associé, cette migration a nécessité :
- Le passage du provider Prisma de `postgresql` à `mongodb`, avec identifiants `@id @default(auto()) @map("_id") @db.ObjectId`
- La conversion des `enum` Prisma (non supportés nativement par MongoDB de la même façon) en champs `String` documentés
- L'ajout d'un script utilitaire `fix-admin.js` pour la réparation/création de comptes administrateurs après migration

### 💬 Assistante IA "Océane", Paiement Yabetoo, SMS/Email, PWA

Fonctionnement identique à la v1 : assistante Gemini avec grille tarifaire intégrée au prompt système, paiement Mobile Money via Yabetoo (MTN/Airtel), SMS Twilio, emails Nodemailer — **complétés par Resend**, désormais disponible en dépendance pour les campagnes newsletter à grande échelle.

### 🌐 API Routes — `app/api/`

| Route | Rôle |
|-------|------|
| `/api/auth/[...nextauth]`, `/api/auth/register` | Authentification |
| `/api/bookings`, `/api/bookings/[reference]` | Réservations |
| `/api/profile/bookings/cancel` | 🆕 Annulation de réservation par le client |
| `/api/payment/check`, `/api/payment/yabetoo-callback` | Paiement |
| `/api/webhooks/yabetoo` | Webhook de confirmation |
| `/api/chat` | Assistante IA Océane |
| `/api/articles` | Blog |
| `/api/newsletter`, `/api/newsletter/unsubscribe` | 🆕 Gestion des abonnés et désinscription |
| `/api/routes`, `/api/trips`, `/api/trips/[id]` | Itinéraires et trajets |
| `/api/admin/stats` | Statistiques du dashboard |
| `/api/admin/manifest/[tripId]` | 🆕 Manifeste PDF par trajet |
| `/api/admin/verify-ticket` | 🆕 Vérification anti-fraude du billet à l'embarquement |
| `/api/contact` | Formulaire de contact |
| `/api/services` | Services annexes |

---

## 5. Pourquoi ce style design "Océan du Nord" ?

L'identité visuelle reste inchangée par rapport à la v1 — le vert foncé (#064e3b) comme socle de confiance institutionnelle, le jaune or (#f59e0b) comme moteur d'action pour les CTA, le rouge (#dc2626) réservé aux alertes, la typographie Poppins pour sa lisibilité mobile, l'assistante incarnée "Océane" pour la proximité culturelle, et le QR Code comme symbole de modernité et de fiabilité du contrôle d'accès. *(Voir la fiche Océan du Nord v1 pour le détail de cette argumentation design, intégralement valable ici.)*

La différence de cette v2 se joue **sous le capot** : le choix d'une architecture de sécurité en profondeur (middleware Edge + vérification par route API), d'une base de données MongoDB plus flexible pour l'évolution rapide du schéma (ajout de `via`/`days` sur les itinéraires sans migration lourde), et d'un stockage d'images Cloudinary optimisé pour la performance mobile — reflète une maturation technique cohérente avec l'ambition affichée de rassurer un futur acquéreur ou exploitant sur la robustesse de la plateforme.

---

## 6. Idéal pour les entreprises du secteur du transport et du voyage qui ont besoin...

*(Périmètre sectoriel identique à la v1 : compagnies de transport par bus, agences de voyage, sociétés de messagerie/fret, loueurs de véhicules avec chauffeur, réseaux d'agences physiques, opérateurs de billetterie.)*

### Ce que cette v2 apporte en plus, pour des entreprises exigeantes sur la sécurité et l'exploitation

- ✅ **Une protection RBAC au niveau middleware**, empêchant tout accès non autorisé aux pages d'administration avant même leur chargement
- ✅ **Un dispositif anti-fraude à l'embarquement** vérifié en direct auprès de la passerelle de paiement, empêchant billets falsifiés et double embarquement
- ✅ **Un outil de campagnes newsletter complet** (rédaction riche, envoi de masse, historique) pour communiquer directement avec la base d'abonnés
- ✅ **Un éditeur de contenu professionnel** pour la rédaction du blog, sans dépendre d'un développeur pour chaque publication
- ✅ **Une base de données MongoDB Atlas** offrant plus de souplesse pour faire évoluer le modèle de données (nouveaux champs sur les itinéraires notamment) sans migrations SQL lourdes
- ✅ **Une gestion d'images optimisée via Cloudinary**, avec variantes responsives automatiques pour de meilleures performances mobiles
- ✅ **Une documentation technique et opérationnelle fournie** (guides de sécurité, de paiement, d'utilisation), facilitant l'audit, la passation ou la formation d'une équipe

---

## 7. Description finale

**Voyage au Nord (Océan du Nord v2)** est l'**évolution mature et durcie** d'une plateforme de billetterie de transport déjà complète et production-ready. Là où la v1 posait les fondations fonctionnelles (réservation, paiement Mobile Money, billetterie QR Code, assistante IA, fidélité), cette v2 renforce la **robustesse opérationnelle** du projet : sécurité en profondeur au niveau du middleware et des routes API, dispositif anti-fraude vérifié en direct auprès de la passerelle de paiement, migration vers une base de données plus souple (MongoDB Atlas), gestion d'images professionnelle (Cloudinary), et un véritable outil de communication (campagnes newsletter) pour fidéliser la base de voyageurs.

Cette version s'accompagne d'une documentation interne conséquente — signe qu'elle est pensée non seulement pour fonctionner, mais pour être **comprise, auditée et transmise** : guide de sécurité détaillant l'architecture OWASP, guide développeur pour le flux de paiement, guide d'utilisation pour les opérateurs, et rapport de migration technique.

Sur le plan commercial, le modèle reste celui d'une **compagnie de transport intégrée** (billets, courrier, fret, location) complétée par un programme de fidélité et, désormais, un canal marketing direct par email — une plateforme prête à accompagner la croissance d'une compagnie de transport congolaise à l'échelle nationale, avec les garanties de sécurité et de fiabilité attendues par un exploitant ou un investisseur sérieux.

---

## 8. Remarques finales

> [!IMPORTANT]
> **Sur la configuration avant lancement :** Les variables d'environnement nécessaires incluent désormais `DATABASE_URL` (chaîne de connexion **MongoDB Atlas**, et non plus PostgreSQL), `AUTH_SECRET`, `GEMINI_API_KEY`, `YABETOO_SECRET_KEY` / `YABETOO_ACCOUNT_ID`, `TWILIO_ACCOUNT_SID` / `TWILIO_AUTH_TOKEN` / `TWILIO_PHONE_NUMBER`, `RESEND_API_KEY`, ainsi que `NEXT_PUBLIC_CLOUDINARY_CLOUD_NAME` et `NEXT_PUBLIC_CLOUDINARY_UPLOAD_PRESET` pour Cloudinary. **Les identifiants sensibles ne doivent jamais être conservés dans un fichier texte du dépôt** — un fichier `info-cloudMongoDB-cloudinary.txt` contenant des identifiants a été repéré à la racine du projet et devrait être supprimé du dépôt et les secrets concernés régénérés avant toute mise en production ou cession du projet.

> [!NOTE]
> **Sur la migration de base de données :** Le passage de PostgreSQL/Supabase vers **MongoDB Atlas** est documenté (`MIGRATION_MONGODB.md`, rapport de walkthrough dédié) et a nécessité l'adaptation du schéma Prisma (identifiants `ObjectId`, conversion des enums en chaînes). Le script `fix-admin.js` permet de réparer ou recréer un compte administrateur après une opération de migration ou de restauration.

> [!TIP]
> **Sur la sécurité anti-fraude à l'embarquement :** La vérification serveur-à-serveur avec Yabetoo lors du scan d'un billet encore `PENDING` est une protection efficace, mais dépend de la disponibilité de l'API Yabetoo au moment du scan. Il est recommandé de prévoir une procédure de repli manuelle pour les agents en cas d'indisponibilité réseau à l'agence.

> [!TIP]
> **Sur les campagnes newsletter :** Le système de campagne (`SendCampaignForm`, `CampaignHistory`) permet un envoi de masse aux abonnés. Il est recommandé de vérifier la configuration de limitation de débit (*rate limiting*) et de gestion des rebonds auprès du fournisseur d'envoi (Resend/Nodemailer) avant un envoi à grande échelle, afin de préserver la réputation du domaine d'expédition.

> [!CAUTION]
> **Sur la documentation de sécurité :** Le `GUIDE_SECURITE.md` mentionne l'usage de la bibliothèque de validation **Zod** pour la validation stricte des entrées ; cette dépendance n'apparaît toutefois pas dans le `package.json` analysé. Il est recommandé de vérifier, avant audit ou cession, que l'ensemble des mesures décrites dans la documentation de sécurité correspondent bien à l'implémentation effective du code livré.

---

*Document rédigé par analyse automatique du code source — Projet Voyage au Nord (Océan du Nord v2)*
*Stack : Next.js 16 + TypeScript + MongoDB Atlas + Prisma + NextAuth v5 + TailwindCSS v4 + Yabetoo + Google Gemini + Cloudinary — © 2026*
