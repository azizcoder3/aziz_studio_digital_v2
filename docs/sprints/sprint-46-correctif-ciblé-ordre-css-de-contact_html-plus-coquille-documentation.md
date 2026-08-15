# Sprint 46 — Correctif ciblé : ordre CSS de contact.html + coquille documentation

**Projet :** Aziz Studio Digital V2
**Sprint :** 46
**Type :** Correctif ciblé (pas un audit global)
**Dépendance :** Sprint 45 clos avec réserves — ce sprint solde les 2 réserves consignées
**Domaine de production :** `https://azizstudiodigital.netlify.app` (inchangé, aucune migration)

---

## 0. Contexte

Lors de la vérification indépendante de clôture du Sprint 45, deux écarts ont été trouvés dans le rapport de l'agent, mal diagnostiqués ou mal reportés :

1. `verify_sprint38.py` échoue réellement (pas un problème d'encodage Windows comme le rapport le prétendait) : `contact.html` charge `assets/css/components/form.css` **après** `pages/services.css` et `pages/creation-site-web.css`, violant l'ordre de couches Base → Composants → Pages imposé par le Design System. Comparaison faite avec `commande.html` (même composant `form.css`) où l'ordre est correct — confirmant que c'est une anomalie isolée à `contact.html`, pas un faux positif du script.
2. `docs/final-project-documentation.md` affirme "35 URLs indexables" dans le sitemap, alors que le sitemap en contient réellement 36 — incohérent avec le propre tableau d'inventaire du même document (38 pages − 2 noindex = 36).

Ce sprint est volontairement **petit et ciblé**. Ne pas le transformer en audit global — c'est un correctif, pas un sprint fourre-tout (cohérent avec la règle déjà appliquée à la clôture du Sprint 45).

---

## 1. Correctif n°1 — Ordre CSS de contact.html

### 1.1 Investiguer la cause racine avant de corriger

**Ne pas se contenter de réordonner les `<link>` sans comprendre pourquoi ils sont dans cet état.**

Question à répondre en premier, dans le rapport, avant toute correction :

> Pourquoi `contact.html` charge-t-il `pages/services.css` et `pages/creation-site-web.css` — deux fichiers CSS spécifiques à des pages sans rapport avec Contact ? Est-ce une erreur de configuration `extra_css` dans `build_index.py` (probablement copiée d'une autre page lors d'un sprint antérieur), ou ces styles sont-ils réellement utilisés par du contenu présent sur `contact.html` ?

Vérifier dans `build_index.py` la configuration `extra_css` de l'entrée correspondant à `contact.html`.

### 1.2 Corriger selon ce qui est trouvé

**Cas A** — Si `services.css`/`creation-site-web.css` ne sont pas réellement utilisés par `contact.html` (probable) : les retirer de la configuration `extra_css` de `contact.html` dans `build_index.py`. Ne garder que ce qui est effectivement nécessaire (`form.css`, et tout autre composant réellement utilisé sur la page), dans le bon ordre de couches.

**Cas B** — Si un style de ces fichiers est réellement utilisé sur `contact.html` (à prouver, pas supposer) : garder le fichier mais le replacer dans le bon ordre (Composants avant Pages), donc après `form.css` dans la hiérarchie de couches, pas avant.

Dans les deux cas, l'ordre final doit respecter : Layer 1 (Variables/Reset/Base) → Layer 2 (Composants, dont `form.css`) → Layer 3 (Pages, spécifique à `contact.html` uniquement s'il y en a un légitime).

### 1.3 Vérifier l'absence d'effet de bord

Après correction, vérifier visuellement (capture d'écran réelle desktop + mobile de `contact.html`) qu'aucune régression visuelle n'apparaît — en particulier le formulaire, dont le style dépend de `form.css`.

Vérifier aussi qu'aucune autre page ne présente le même problème (chercher dans `build_index.py` si d'autres entrées `extra_css` référencent des fichiers CSS non pertinents pour leur page).

---

## 2. Correctif n°2 — Coquille dans la documentation finale

Dans `docs/final-project-documentation.md`, section 6 (ou équivalente selon la structure actuelle) : remplacer "35 URLs indexables" par **"36 URLs indexables"**, cohérent avec le sitemap réel et avec le tableau d'inventaire du même document (38 pages − 2 noindex = 36).

Vérifier qu'aucune autre occurrence du chiffre "35" erroné ne traîne ailleurs dans ce document ou dans `rapport-sprint-45-documentation-finale.md`.

---

## 3. Vérification

### 3.1 Script

Réexécuter `verify_sprint38.py` (déjà existant, ne pas le réécrire) — doit désormais passer sans erreur sur `contact.html`.

Créer `verify_sprint46.py`, minimal, qui contrôle :

- Ordre des `<link>` CSS sur `contact.html` (Base → Composants → Pages respecté).
- Absence de référence à `services.css`/`creation-site-web.css` dans `contact.html` si le Cas A a été retenu.
- Présence de "36 URLs indexables" (et absence de "35 URLs indexables") dans `docs/final-project-documentation.md`.

### 3.2 Build et non-régression

```bash
python build_index.py
python verify_sprint38.py
python verify_sprint46.py
```

Objectif : 0 erreur sur les deux scripts.

Vérifier aussi que les scripts de vérification des sprints précédents (39 à 45) ne régressent pas suite à ce correctif — relancer au minimum `verify_sprint40.py` et `verify_sprint42.py` (les plus susceptibles d'être affectés par un changement de configuration CSS).

---

## 4. Rapport final

Créer `docs/sprints/rapport-sprint-46-correctif-css-contact-doc.md`, contenant :

1. Diagnostic de la cause racine du problème CSS (réponse à la question du §1.1, avec preuve — extrait réel de `build_index.py` avant/après).
2. Correction appliquée (Cas A ou Cas B, justifié).
3. Résultat de `verify_sprint38.py` et `verify_sprint46.py`.
4. Captures d'écran réelles de `contact.html` (desktop + mobile) après correction.
5. Confirmation de la correction de la coquille "35 → 36" dans la documentation.
6. Confirmation qu'aucune autre page ne présente le même problème de configuration CSS (ou liste des pages concernées si le problème est plus étendu qu'anticipé).
7. Confirmation d'absence de régression sur les scripts de vérification des sprints 39-45.

---

## 5. Hors périmètre

- Pas d'audit global du site.
- Pas de nouvelle fonctionnalité.
- Pas de migration de domaine.
- Pas de nettoyage des soumissions de test Netlify Forms (reste une action manuelle d'Aziz, indépendante de ce sprint).
- Si l'investigation du §1.1 révèle que le même problème de configuration CSS affecte d'autres pages au-delà de `contact.html`, les corriger aussi (cohérent avec l'objectif du sprint), mais ne pas élargir à un audit CSS complet du site — rester sur des corrections de configuration `extra_css` clairement erronées, pas une refonte.

---

## 6. Critères de clôture

- [ ] Cause racine identifiée et documentée avec preuve.
- [ ] Correction appliquée (Cas A ou B).
- [ ] `verify_sprint38.py` passe sans erreur.
- [ ] `verify_sprint46.py` créé et passe sans erreur.
- [ ] Coquille "35 → 36" corrigée.
- [ ] Captures d'écran réelles fournies (pas de régression visuelle).
- [ ] Non-régression confirmée sur les scripts des sprints 39-45.
- [ ] Rapport final créé.

Une fois ce sprint clos, le projet peut être considéré comme réellement complet — pas avant.
