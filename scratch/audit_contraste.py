# -*- coding: utf-8 -*-
"""
Sprint 42 - Complement Etape 0 : Audit contraste WCAG 1.4.3 / 1.4.11
Calcul des ratios de contraste reels a partir des variables CSS du Design System.
Objectif : 4.5:1 texte normal, 3:1 texte large (>= 18px normal ou >= 14px bold).
"""
import math
import colorsys

def hsl_to_rgb(h, s, l):
    """Convertit HSL (en degres, %) en tuple RGB (0-255)."""
    h /= 360
    s /= 100
    l /= 100
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return int(r * 255), int(g * 255), int(b * 255)

def luminance(r, g, b):
    """Calcule la luminance relative WCAG (sRGB)."""
    def c(val):
        v = val / 255
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * c(r) + 0.7152 * c(g) + 0.0722 * c(b)

def contrast_ratio(color1_hsl, color2_hsl):
    """Calcule le ratio de contraste entre deux couleurs HSL."""
    r1, g1, b1 = hsl_to_rgb(*color1_hsl)
    r2, g2, b2 = hsl_to_rgb(*color2_hsl)
    l1 = luminance(r1, g1, b1)
    l2 = luminance(r2, g2, b2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

def check_wcag(ratio, size_type):
    """Verifie la conformite WCAG AA selon le type de texte."""
    if size_type == 'normal':
        threshold_aa = 4.5
        threshold_aaa = 7.0
    else:  # large (>= 18px ou >= 14px bold)
        threshold_aa = 3.0
        threshold_aaa = 4.5

    if ratio >= threshold_aaa:
        return f"PASS AAA ({ratio:.2f}:1)"
    elif ratio >= threshold_aa:
        return f"PASS AA ({ratio:.2f}:1)"
    else:
        return f"FAIL ({ratio:.2f}:1 - requis {threshold_aa}:1)"

# ─── Variables CSS du Design System (Light Mode) ──────────────────────────────
# Format: (H, S, L)
colors = {
    'text_primary':   (224, 71, 4),    # hsl(224, 71%, 4%)   - quasi noir
    'text_secondary': (220,  9, 30),   # hsl(220, 9%, 30%)   - gris fonce
    'accent':         (262, 83, 58),   # hsl(262, 83%, 58%)  - violet
    'primary':        (224, 64, 23),   # hsl(224, 64%, 23%)  - bleu nuit
    'background':     (210, 40, 98),   # hsl(210, 40%, 98%)  - fond gris tres clair
    'surface':        (  0,  0, 100),  # hsl(0, 0%, 100%)    - blanc pur
    'danger':         (  0, 84, 50),   # hsl(0, 84%, 50%)    - rouge
    'success':        (142, 72, 29),   # hsl(142, 72%, 29%)  - vert fonce
    'warning':        ( 38, 92, 42),   # hsl(38, 92%, 42%)   - ambre
    'border':         (220, 13, 91),   # hsl(220, 13%, 91%)  - bordure gris clair
    # Accent Hero (texte blanc sur fond accent)
    'white':          (0, 0, 100),
    # Dark mode background approximatif
    'dark_bg':        (224, 71, 4),    # hsl(224, 71%, 4%)
    'dark_surface':   (224, 71, 8),    # hsl(224, 71%, 8%)
    'dark_text':      (210, 40, 98),   # hsl(210, 40%, 98%)
    'dark_accent':    (262, 83, 68),   # hsl(262, 83%, 68%)
}

print("=" * 75)
print("AUDIT CONTRASTE WCAG 1.4.3 & 1.4.11 — Design System Aziz Studio Digital V2")
print("=" * 75)

# ─── Combinaisons a auditer (Light Mode) ─────────────────────────────────────
light_mode_pairs = [
    # (label, couleur_texte, couleur_fond, type_texte, contexte)
    ("Texte principal sur fond page",       'text_primary',   'background', 'normal', "Tous les corps de texte"),
    ("Texte secondaire sur fond page",      'text_secondary', 'background', 'normal', "Sous-titres, descriptions"),
    ("Texte secondaire sur fond surface",   'text_secondary', 'surface',    'normal', "Texte dans les cartes"),
    ("Texte principal sur fond surface",    'text_primary',   'surface',    'normal', "Titres dans les cartes"),
    ("Accent sur fond page (liens)",        'accent',         'background', 'normal', "Liens accentuation"),
    ("Accent sur fond surface (liens)",     'accent',         'surface',    'normal', "Liens dans cartes"),
    ("Blanc sur fond accent (btn CTA)",     'white',          'accent',     'large',  "Texte bouton CTA violet"),
    ("Blanc sur fond primary (btn header)", 'white',          'primary',    'large',  "Texte bouton nav bleu"),
    ("Primary sur fond background",         'primary',        'background', 'normal', "Titres H2/H3 couleur primaire"),
    ("Danger sur fond surface (erreurs)",   'danger',         'surface',    'normal', "Messages d'erreur formulaire"),
    ("Success sur fond surface (succes)",   'success',        'surface',    'normal', "Messages de succes"),
    ("Warning sur fond surface (icones)",   'warning',        'surface',    'large',  "Icones etoiles rating (non-text)"),
    ("Texte principal sur fond surface",    'text_primary',   'surface',    'large',  "Titres H1/H2 (grands)"),
]

print("\n--- MODE CLAIR (Light Mode) ---\n")
print(f"{'Combinaison':<42} {'Type':<8} {'Ratio':<20} {'Contexte'}")
print("-" * 95)

fails_light = []
for label, txt_key, bg_key, size, context in light_mode_pairs:
    ratio = contrast_ratio(colors[txt_key], colors[bg_key])
    result = check_wcag(ratio, size)
    if 'FAIL' in result:
        fails_light.append((label, result, context))
    icon = "OK" if 'PASS' in result else "!!"
    print(f"[{icon}] {label:<42} {size:<8} {result:<25} {context}")

# ─── Dark Mode ───────────────────────────────────────────────────────────────
dark_mode_pairs = [
    ("Texte primaire dark sur fond dark",   'dark_text',   'dark_bg',      'normal', "Corps de texte dark mode"),
    ("Texte primaire dark sur fond surface",'dark_text',   'dark_surface',  'normal', "Texte dans cartes dark"),
    ("Accent dark sur fond dark bg",        'dark_accent', 'dark_bg',      'normal', "Liens accent dark"),
]

print("\n--- MODE SOMBRE (Dark Mode - overrides) ---\n")
print(f"{'Combinaison':<42} {'Type':<8} {'Ratio':<20} {'Contexte'}")
print("-" * 95)

fails_dark = []
for label, txt_key, bg_key, size, context in dark_mode_pairs:
    ratio = contrast_ratio(colors[txt_key], colors[bg_key])
    result = check_wcag(ratio, size)
    if 'FAIL' in result:
        fails_dark.append((label, result, context))
    icon = "OK" if 'PASS' in result else "!!"
    print(f"[{icon}] {label:<42} {size:<8} {result:<25} {context}")

# ─── Bilan ────────────────────────────────────────────────────────────────────
print("\n" + "=" * 75)
print(f"BILAN CONTRASTE")
print(f"  Light Mode — combinaisons verifiees : {len(light_mode_pairs)}")
print(f"  Light Mode — echecs WCAG AA         : {len(fails_light)}")
print(f"  Dark Mode  — combinaisons verifiees : {len(dark_mode_pairs)}")
print(f"  Dark Mode  — echecs WCAG AA         : {len(fails_dark)}")
print("=" * 75)

all_fails = fails_light + fails_dark
if all_fails:
    print("\nCOMBINAISONS EN ECHEC :")
    for label, result, context in all_fails:
        print(f"  !! {label}")
        print(f"     Ratio : {result}")
        print(f"     Contexte : {context}")
else:
    print("\n  Toutes les combinaisons passent WCAG 2.1 AA.")

# ─── Valeurs RGB references ────────────────────────────────────────────────────
print("\n--- Valeurs RGB des tokens cles ---")
for name, hsl in colors.items():
    r, g, b = hsl_to_rgb(*hsl)
    lum = luminance(r, g, b)
    print(f"  {name:<22}: hsl({hsl[0]},{hsl[1]}%,{hsl[2]}%) -> rgb({r},{g},{b}) -> luminance={lum:.4f}")
