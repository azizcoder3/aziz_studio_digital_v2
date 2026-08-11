# Sprint 43 — Automatisation des emails de confirmation (Netlify Functions + Gmail SMTP)

**Projet :** Aziz Studio Digital V2
**Sprint :** 43
**Type :** Fonctionnalité backend (première brique serveur du projet)
**Dépendances :** Sprint 40 (Netlify Forms déjà configuré sur `contact.html` et `commande.html`)

> **Renumérotation de la roadmap** : ce sprint s'insère avant les sprints de préparation. Le sprint "Préparation mise en production" devient le **Sprint 44**, et "Documentation finale" devient le **Sprint 45**.

---

## 0. Contexte et objectif

Actuellement, `contact.html` et `commande.html` envoient leurs soumissions via Netlify Forms (Sprint 40) : Aziz reçoit la donnée brute dans son tableau de bord Netlify. Il n'existe **aucune confirmation automatique** envoyée à la personne qui a rempli le formulaire.

**Objectif** : dès qu'un visiteur soumet `contact.html` ou `commande.html`, il reçoit automatiquement un email de confirmation personnalisé, envoyé depuis `azizstudio.dev@gmail.com` via SMTP.

**Hébergement** : le site reste sur **Netlify** pour ce sprint. Une éventuelle migration future vers Hostinger (pas avant plusieurs mois, pas encore planifiée) nécessitera une réécriture de cette fonctionnalité en PHP à ce moment-là — **ne pas anticiper cette migration dans ce sprint**, elle sera traitée comme un sprint dédié le moment venu.

---

## 1. Règle de sécurité absolue — Non négociable

**Aucun identifiant (mot de passe d'application Gmail, adresse email d'envoi) ne doit jamais apparaître :**

- dans un fichier HTML, CSS ou JavaScript servi au navigateur (code client) ;
- dans un fichier commité sur Git, même dans un commentaire ou un exemple ;
- dans les logs de la fonction serveur (pas de `console.log` affichant le mot de passe) ;
- dans le rapport final du sprint ou toute capture d'écran.

Les identifiants vivent **exclusivement** dans les variables d'environnement du tableau de bord Netlify (Site settings → Environment variables), configurées manuellement par Aziz — **l'agent ne doit jamais demander le mot de passe d'application en clair et ne doit jamais le coder en dur, même temporairement pour tester.**

Si l'agent a besoin de tester l'envoi, il doit le faire en lisant les variables d'environnement (`process.env.GMAIL_USER`, `process.env.GMAIL_APP_PASSWORD`) déjà configurées côté Netlify, jamais en les saisissant dans le code.

---

## 2. Architecture retenue

```
Visiteur soumet contact.html ou commande.html
  ↓  (POST natif du formulaire, data-netlify="true" — inchangé du Sprint 40)
Netlify Forms capture la soumission (tableau de bord Aziz intact)
  ↓  (notification sortante configurée dans Netlify UI, PAS dans le code)
Netlify Function : netlify/functions/send-autoreply.js
  ↓  (Nodemailer + SMTP Gmail)
Email de confirmation envoyé à l'adresse du visiteur
```

Le formulaire HTML existant n'est **pas modifié** dans sa structure ni son `action`. Seul un déclencheur de notification est ajouté côté configuration Netlify.

---

## 3. Configuration Netlify (à faire par Aziz, pas par l'agent)

Cette étape se fait dans l'interface web Netlify, pas dans le code. L'agent doit uniquement **documenter** la procédure dans le rapport, pas la réaliser lui-même (il n'a pas accès au compte Netlify d'Aziz).

1. Site settings → Environment variables → ajouter :
   - `GMAIL_USER` = `azizstudio.dev@gmail.com`
   - `GMAIL_APP_PASSWORD` = (le code à 16 caractères, déjà généré par Aziz)
2. Site settings → Forms → Form notifications → Add notification → **Outgoing webhook** :
   - Pour le formulaire `contact` : URL = `/.netlify/functions/send-autoreply`
   - Pour le formulaire `commande` : même URL (la fonction distingue les deux via le champ `form-name`)

L'agent doit rédiger cette procédure noir sur blanc dans le rapport final, avec des captures si possible, pour qu'Aziz puisse la suivre ou la vérifier lui-même.

---

## 4. La Netlify Function

### 4.1 Fichier à créer

`netlify/functions/send-autoreply.js`

### 4.2 Dépendances

Ajouter `nodemailer` au `package.json` du projet (le créer à la racine s'il n'existe pas déjà). Configurer `netlify.toml` pour déclarer le dossier de fonctions si ce n'est pas déjà fait :

```toml
[functions]
  directory = "netlify/functions"
```

### 4.3 Logique de la fonction

1. Recevoir le payload JSON envoyé par le webhook Netlify Forms (contient tous les champs soumis + `form-name`).
2. **Vérifier le honeypot** (`bot-field`) : si non vide, ne rien envoyer et retourner directement (c'est un bot).
3. Extraire les champs pertinents selon le formulaire :
   - `contact` : nom, prénom, email, type de projet, message.
   - `commande` : nom, prénom, email, secteur d'origine, offre, prix.
4. Valider qu'un email valide est présent — si absent ou malformé, ne pas planter, juste ne pas envoyer (et logger l'anomalie sans exposer de données sensibles).
5. Sélectionner le bon template HTML selon `form-name`.
6. Envoyer via Nodemailer (transport SMTP Gmail, `smtp.gmail.com`, port 465, `secure: true`, auth via les variables d'environnement).
7. Retourner un statut HTTP 200 même en cas d'échec d'envoi (pour ne jamais faire échouer la soumission Netlify Forms elle-même côté visiteur) — logger l'erreur côté fonction pour diagnostic.

---

## 5. Templates d'emails

Deux templates HTML distincts, **honnêtes et sobres**, cohérents avec le principe fondateur du projet (aucune métrique inventée, aucune promesse non tenue).

### 5.1 Template `contact`

- Objet : "Votre message a bien été reçu — Aziz Studio Digital"
- Corps : remerciement, rappel du délai de réponse (**72h**, cohérent avec `contact.html`), résumé du message envoyé (nom, type de projet), coordonnées de contact (`azizstudio.dev@gmail.com`, WhatsApp).
- Ne pas promettre un canal ou un délai différent de ce qui existe déjà sur le site.

### 5.2 Template `commande`

- Objet : "Votre demande d'offre [Nom de l'offre] — Aziz Studio Digital"
- Corps : remerciement, rappel de l'offre sélectionnée et du tarif de départ affiché, rappel du délai de réponse (72h), coordonnées de contact.

### 5.3 Charte visuelle des emails

Reprendre a minima : logo texte "Aziz **Studio** Digital" (avec le mot "Studio" en violet accent si le client email le permet), couleur d'accent violette cohérente avec le site, pied de page avec les coordonnées réelles (`azizstudio.dev@gmail.com`, République du Congo). Rester sobre — un email HTML simple, pas un design surchargé.

---

## 6. Sécurité et anti-abus

- Le honeypot existant (`bot-field`) doit être vérifié dans la fonction, pas seulement côté Netlify Forms.
- La fonction ne doit jamais renvoyer dans sa réponse HTTP un message d'erreur détaillé pouvant révéler des informations internes (config SMTP, stack trace).
- Aucune donnée personnelle (email du visiteur, message) ne doit être loggée en clair dans les logs Netlify au-delà de ce qui est strictement nécessaire au diagnostic.

---

## 7. Vérification

### 7.1 Vérification statique (script)

Créer `verify_sprint43.py` qui contrôle, **sans envoyer de vrai email** :

- Présence de `netlify/functions/send-autoreply.js`.
- Présence de `nodemailer` dans `package.json`.
- Présence de `[functions]` dans `netlify.toml`.
- **Absence totale** de toute chaîne ressemblant à un mot de passe, une adresse Gmail en dur, ou une clé API dans l'ensemble du code source (grep sur des patterns suspects : `smtp`, `password`, `@gmail.com` codés en dur hors `process.env`).
- Présence de la vérification du honeypot dans le code de la fonction.
- Confirmation que la fonction utilise bien `process.env.GMAIL_USER` et `process.env.GMAIL_APP_PASSWORD`, jamais de valeur en dur.

### 7.2 Vérification réelle (obligatoire, ne peut pas être automatisée par un script)

L'agent ne peut pas tester l'envoi réel sans accès aux variables d'environnement Netlify (qu'il n'a pas). **C'est Aziz qui doit faire ce test après déploiement** :

1. Soumettre `contact.html` avec une vraie adresse email de test.
2. Vérifier que l'email de confirmation arrive (regarder aussi les spams).
3. Répéter pour `commande.html`.
4. Vérifier dans le tableau de bord Netlify Functions que l'exécution ne montre aucune erreur.

L'agent doit clairement indiquer dans son rapport que **cette étape reste à faire par Aziz**, ne jamais prétendre l'avoir testée lui-même sans accès aux vraies clés.

---

## 8. Documentation

Mettre à jour `docs/project-architecture.md` avec une nouvelle section "Emails automatiques — Netlify Functions", décrivant l'architecture, l'emplacement du code, et un rappel explicite de la règle de sécurité (identifiants uniquement en variables d'environnement).

---

## 9. Rapport final attendu

Le rapport doit contenir :

1. Résumé de l'architecture mise en place.
2. Liste des fichiers créés/modifiés.
3. La procédure de configuration Netlify (variables d'environnement + notification webhook), rédigée pour qu'Aziz puisse la suivre.
4. Résultat de `verify_sprint43.py`.
5. **Rappel explicite que le test d'envoi réel reste à faire par Aziz**, avec les étapes précises à suivre.
6. Confirmation qu'aucun identifiant n'apparaît nulle part dans le code (preuve : résultat du grep de sécurité du script de vérification).
7. Aperçu texte du contenu des deux templates (pas juste "template créé" — montrer le texte réel envoyé).
