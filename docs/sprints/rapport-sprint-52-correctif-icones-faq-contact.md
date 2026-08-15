# Rapport Sprint 52 — Correctif CSS des icônes FAQ sur contact.html & Audit SVG Renforcé

**Projet :** Aziz Studio Digital V2  
**Sprint :** 52  
**Type :** Correctif CSS & Fiabilisation de l'audit automatisé  
**Date :** 2026-08-12  
**Statut :** ✅ Clos — tous les critères de clôture validés (Validation conjointe des Sprints 50, 51 et 52)

---

## 1. Contexte & Diagnostic du problème

### 1.1. Cause du bug d'affichage sur `contact.html`
Sur la page `contact.html`, les icônes de la section FAQ (`#faq-contact`) — notamment `.faq-icon-wrapper`, `.faq-icon` et `.faq-chevron` — s'affichaient à taille géante non stylisée.
- Au **Sprint 46**, les fichiers CSS externes (`home.css`, `creation-site-web.css`, `solutions.css`) avaient été retirés du `<head>` de `contact.html` pour des raisons d'isolation de la couche Layer 3.
- Au **Sprint 48**, la section accordéon FAQ avait été déclinée sur `contact.html`, mais les règles CSS `.faq-icon-wrapper`, `.faq-icon`, `.faq-chevron` résidaient uniquement dans `home.css`.

### 1.2. Diagnostic de la faille de l'audit (`verify_sprint51.py`)
Pourquoi `verify_sprint51.py` avait-il rapporté un faux positif ("0 erreur") lors du Sprint 51 ?
- Le script `verify_sprint51.py` testait si la balise HTML `<svg>` possédait un attribut `width=` inline via `'width=' in svg_attrs`.
- Or, toutes les icônes Lucide/Feather possèdent l'attribut d'épaisseur de trait **`stroke-width="2"`**.
- La recherche naïve du sous-texte `'width='` correspondait dans la sous-chaîne `stroke-width="2"`. Le script considérait à tort que chaque balise `<svg>` possédait une largeur inline HTML et annulait la vérification des classes CSS !

---

## 2. Correctifs apportés

### 2.1. Refonte du Moteur d'Audit SVG
L'algorithme de détection du moteur d'audit a été corrigé avec une expression rationnelle à recherche arrière négative (negative lookbehind) et limite de mot :
```python
has_inline_width = bool(re.search(r'(?<!stroke-)\bwidth\s*=', svg_attrs, re.I))
has_inline_height = bool(re.search(r'\bheight\s*=', svg_attrs, re.I))
```
Grâce à cette correction, `stroke-width="2"` n'est plus confondu avec l'attribut HTML `width="..."`.

### 2.2. Portage des règles CSS dans `assets/css/pages/contact.css`
Les règles de l'accordéon FAQ et de ses icônes ont été copiées/adaptées de `home.css` vers `assets/css/pages/contact.css` (Layer 3) :

```css
/* ==========================================================================
   FAQ ACCORDION & ICONS (CONTACT FIX - SPRINT 52)
   ========================================================================== */

.faq-accordion-wrapper {
    max-width: 860px;
    margin: 0 auto;
}

.faq-accordion {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-16px);
    width: 100%;
}

.faq-item {
    border-radius: var(--radius-large);
    background-color: var(--color-surface);
    border: 1px solid var(--color-border);
    transition: background-color var(--transition-normal), border-color var(--transition-normal), box-shadow var(--transition-normal);
    overflow: hidden;
}

.faq-item:hover {
    border-color: hsla(var(--color-accent-h), var(--color-accent-s), var(--color-accent-l), 0.3);
    box-shadow: var(--shadow-md);
}

.faq-item[open] {
    border-color: hsla(var(--color-accent-h), var(--color-accent-s), var(--color-accent-l), 0.45);
    box-shadow: 0 4px 20px hsla(var(--color-accent-h), var(--color-accent-s), var(--color-accent-l), 0.12);
    background-color: hsla(var(--color-accent-h), var(--color-accent-s), var(--color-accent-l), 0.02);
}

.faq-summary {
    list-style: none;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: var(--spacing-16px);
    padding: var(--spacing-20px) var(--spacing-24px);
    cursor: pointer;
    user-select: none;
    transition: background-color var(--transition-fast);
}

.faq-summary::-webkit-details-marker {
    display: none;
}

.faq-summary:focus-visible {
    outline: 2px solid var(--color-accent);
    outline-offset: -2px;
    border-radius: var(--radius-large);
}

.faq-question {
    display: flex;
    align-items: center;
    gap: var(--spacing-16px);
    flex-grow: 1;
}

.faq-icon-wrapper {
    flex-shrink: 0;
    width: 40px;
    height: 40px;
    border-radius: var(--radius-medium);
    background-color: hsla(var(--color-accent-h), var(--color-accent-s), var(--color-accent-l), 0.1);
    color: var(--color-accent);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background-color var(--transition-fast), color var(--transition-fast);
}

.faq-item:hover .faq-icon-wrapper,
.faq-item[open] .faq-icon-wrapper {
    background-color: var(--color-accent);
    color: hsl(var(--color-surface-h), var(--color-surface-s), var(--color-surface-l));
}

.faq-icon {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}

.faq-question-title {
    font-family: var(--font-heading);
    font-size: var(--font-size-base);
    font-weight: var(--font-weight-700);
    color: var(--color-text-primary);
    line-height: 1.4;
    margin: 0;
}

@media (min-width: 768px) {
    .faq-question-title {
        font-size: var(--font-size-lg);
    }
}

.faq-chevron {
    width: 20px;
    height: 20px;
    color: var(--color-text-secondary);
    flex-shrink: 0;
    transition: transform var(--transition-normal) ease, color var(--transition-fast);
}

.faq-summary:hover .faq-chevron,
.faq-item[open] .faq-chevron {
    color: var(--color-accent);
}

.faq-item[open] .faq-chevron {
    transform: rotate(180deg);
}

.faq-answer {
    padding: 0 var(--spacing-24px) var(--spacing-24px) calc(var(--spacing-24px) + 40px + var(--spacing-16px));
}

.faq-answer-text {
    font-size: var(--font-size-sm);
    color: var(--color-text-secondary);
    line-height: 1.65;
    margin: 0;
}

@media (max-width: 575px) {
    .faq-summary {
        padding: var(--spacing-16px);
        gap: var(--spacing-12px);
    }

    .faq-question {
        gap: var(--spacing-12px);
    }

    .faq-icon-wrapper {
        width: 36px;
        height: 36px;
    }

    .faq-icon {
        width: 18px;
        height: 18px;
    }

    .faq-answer {
        padding: 0 var(--spacing-16px) var(--spacing-16px) var(--spacing-16px);
    }
}
```

---

## 3. Description visuelle de la page Contact après correctif

L'inspection de la page `contact.html` confirme un rendu visuel conforme au Design System du studio :
- **Section FAQ (`#faq-contact`)** : Chaque question est présentée dans une carte accordéon `<details class="faq-item card">` bordée d'un trait fin violet au survol et à l'ouverture.
- **Icône de question (`.faq-icon-wrapper` / `.faq-icon`)** : Logée dans un container carré à coins arrondis (40x40px en desktop, 36x36px sur mobile), fond violet translucide `hsla(var(--color-accent-h)..., 0.1)`. Au survol ou à l'ouverture, le fond bascule en violet plein (`var(--color-accent)`) et l'icône SVG (20x20px) passe en blanc.
- **Chevron d'accordéon (`.faq-chevron`)** : Positionné à droite (20x20px), couleur text-secondary qui s'illumine en violet au survol et pivote de 180° de manière fluide (`transform: rotate(180deg)`) lors de l'ouverture du volet.
- **Section Processus (Sprint 51)** : Les 5 cartes de déroulement de prise de contact s'affichent avec des icônes numérotées parfaitement dimensionnées (42x42px wrapper, 20x20px icône principale, 14x14px coches d'outcomes et horloges).

---

## 4. Script de vérification & Résultats (`verify_sprint52.py`)

Le script `verify_sprint52.py` inclut une auto-évaluation obligatoire pour prouver qu'il attrape les réelles erreurs (test sur un élément HTML SVG fictif non stylisé `<svg class="dummy-broken-icon" stroke-width="2">`).

### Résultat de l'exécution de `verify_sprint52.py`

```
=================================================================
  VERIFY SPRINT 52 — CORRECTIF CSS ICONES FAQ ET AUDIT REFORCE   
=================================================================

[1/5] Preuve de détection du moteur d'audit SVG (test sur cas délibérément cassé)...
  [OK] Preuve de détection réussie : le moteur a correctement attrapé l'icône cassée fictive (1/1 décelée) !

[2/5] Audit automatisé du dimensionnement CSS des balises <svg> sur les 38 pages du projet...
  [OK] 100% des balises <svg> sur les 38 pages possèdent une règle de taille CSS valide !

[3/5] Vérification explicite des règles FAQ dans contact.css et de l'isolation CSS...
  [OK] contact.html charge uniquement assets/css/pages/contact.css en Layer 3 (pas de home.css / creation-site-web.css)
  [OK] Les règles FAQ CSS (.faq-icon-wrapper, .faq-icon, .faq-chevron, et états open/hover) sont toutes présentes dans contact.css

[4/5] Vérification de non-régression sur les View Transitions (Sprint 50)...
  [OK] Transitions de page @view-transition et prefers-reduced-motion intactes dans base.css

[5/5] Vérification de l'absence de résidus Unicode et emojis de base...
  [OK] Aucun résidu Unicode U+FE0F / U+FE0E décelé sur l'ensemble du site !

=================================================================
RÉSULTATS : 0 erreur(s)
=================================================================

[OK] VÉRIFICATION RÉUSSIE — SPRINT 52 VALIDÉ !
```

---

## 5. Non-régression globale (Sprints 46 à 52)

Tous les scripts de test du projet ont été ré-exécutés avec le moteur d'audit corrigé :

| Script de test | Statut | Résultat |
|---|---|---|
| `verify_sprint46.py` | ✅ PASS | 0 erreur |
| `verify_sprint47.py` | ✅ PASS | 0 erreur |
| `verify_sprint48.py` | ✅ PASS | 0 erreur |
| `verify_sprint49.py` | ✅ PASS | 0 erreur |
| `verify_sprint50.py` | ✅ PASS | 0 erreur |
| `verify_sprint51.py` (mis à jour) | ✅ PASS | 0 erreur |
| `verify_sprint52.py` | ✅ PASS | 0 erreur |

---

## Critères de clôture

- [x] Correction de la faille du moteur d'audit SVG (`stroke-width="2"` exclu des attributs de largeur HTML)
- [x] Auto-test d'intégrité du moteur d'audit validé sur un cas de test cassé fictif
- [x] Portage de 100% des règles CSS d'accordéon et d'icônes FAQ dans `assets/css/pages/contact.css`
- [x] Maintien strict de l'isolation CSS de `contact.html` (Layer 3 autonome sans `home.css`)
- [x] Recompilation avec `python build_index.py` sans aucune erreur
- [x] Passage à 0 erreur des scripts `verify_sprint46.py` à `verify_sprint52.py`
- [x] Clôture simultanée officielle du **Sprint 50** (transitions), du **Sprint 51** et du **Sprint 52**
- [x] Rédaction du rapport dans `docs/sprints/rapport-sprint-52-correctif-icones-faq-contact.md`

**Les Sprints 50, 51 et 52 sont officiellement clos et validés.**
