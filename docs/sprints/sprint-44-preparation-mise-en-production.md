# Sprint 44 — Préparation à la mise en production

**Projet :** Aziz Studio Digital V2  
**Sprint :** 44  
**Thème :** Préparation finale à la mise en production  
**Domaine de production actuel :** `azizstudiodigital.netlify.app`

---

# 0. Cadre stratégique du Sprint

Le Sprint 43 — Automatisation des emails avec Netlify Functions + Gmail SMTP — est déjà terminé et fonctionnel en production sur Netlify.

Le Sprint 44 constitue donc la dernière phase de vérification avant de considérer le site comme prêt à être utilisé publiquement.

## Domaine de production officiel

Pour ce sprint, le domaine officiel est exclusivement :

`https://azizstudiodigital.netlify.app`

### IMPORTANT

Aucune migration de domaine ne doit être effectuée pendant ce sprint.

Ne pas :

- migrer vers `azizstudiodigital.com` ;
- configurer Hostinger ;
- modifier le DNS ;
- modifier les nameservers ;
- préparer une redirection vers un domaine futur ;
- remplacer le domaine Netlify par un domaine qui n'existe pas encore ;
- ajouter une configuration liée à un futur hébergement.

La migration vers :

`azizstudiodigital.com`

ou vers Hostinger fera l'objet d'un sprint distinct ultérieur lorsque les moyens seront disponibles.

---

# 1. Objectif principal

Effectuer une revue finale et globale du site après les Sprints 39 à 43 afin de vérifier que le projet est réellement prêt pour une utilisation publique.

Le sprint doit notamment vérifier :

- tous les liens ;
- tous les parcours utilisateurs ;
- tous les formulaires ;
- l'automatisation des emails ;
- les données de test ;
- les URLs de production ;
- canonical ;
- Open Graph ;
- sitemap ;
- robots.txt ;
- variables d'environnement ;
- pages légales ;
- navigation ;
- CTA ;
- responsive ;
- SEO ;
- accessibilité ;
- performances ;
- cohérence globale ;
- absence de régression.

---

# 2. Étape 0 — Audit complet avant toute correction

⚠ Aucune modification ne doit être effectuée avant cet audit.

L'agent doit commencer par établir l'état réel du projet.

Scanner automatiquement toutes les pages HTML compilées présentes à la racine.

Le nombre de pages ne doit pas être codé en dur : détecter les fichiers `.html` présents.

Pour chaque page, contrôler au minimum :

| Page | HTTP/URL | Header | Footer | Liens | CTA | Formulaire | SEO | Canonical | OG  | Sitemap | Robots | Responsive | Accessibilité | Statut |
| ---- | -------- | ------ | ------ | ----- | --- | ---------- | --- | --------- | --- | ------- | ------ | ---------- | ------------- | ------ |

L'agent doit ensuite produire une liste des anomalies trouvées avant toute correction.

---

# 3. Vérification du domaine de production

Toutes les références absolues destinées à la production doivent être analysées.

Le domaine attendu est :

`https://azizstudiodigital.netlify.app`

Rechercher notamment :

- `azizstudiodigital.netlify.app`
- `azizstudiodigital.com`
- `www.azizstudiodigital.com`
- anciennes URLs ;
- localhost ;
- `127.0.0.1` ;
- URLs de staging ;
- chemins de développement ;
- URLs temporaires Netlify.

### Règle

Une référence de production vers un domaine futur inexistant est une anomalie.

Le domaine futur `.com` ne doit pas apparaître dans :

- canonical ;
- Open Graph ;
- sitemap ;
- robots ;
- JSON-LD ;
- liens absolus ;
- configuration de production.

---

# 4. Audit complet des liens

Scanner tous les liens internes :

```html
<a href="..."></a>
```
