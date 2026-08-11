import json
import os

ROOT = r"c:\Users\Aziz\Desktop\aziz_studio_digital_v2"
with open(os.path.join(ROOT, "scratch", "step0_data.json"), "r", encoding="utf-8") as f:
    data = json.load(f)

pages = data['pages_detail']
images = data['images_detail']

with open(os.path.join(ROOT, "scratch", "tables_step0.md"), "w", encoding="utf-8") as f:
    f.write("# ÉTAPE 0 — TABLEAUX D'AUDIT COMPLETS (AVANT CORRECTION)\n\n")
    
    f.write("## 1. Inventaire et Audit des 39 Pages HTML Compilées\n\n")
    f.write("| Page | Format | Taille HTML | Nombre d'images | Poids des images | CSS | JS | Image LCP potentielle | Problèmes détectés |\n")
    f.write("| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- |\n")
    for p in pages:
        f.write(f"| [{p['page']}](file:///{ROOT}\\{p['page']}) | HTML5 | {p['size_kb']} KB | {p['img_count']} | {p['img_weight_kb']} KB | {p['css_count']} | {p['js_count']} | `{p['lcp_img']}` | {p['issues']} |\n")
        
    f.write("\n## 2. Inventaire et Audit des 30 Fichiers Images dans `assets/images/`\n\n")
    f.write("| Image | Format | Dimensions | Poids | Références | Transparence | Critique / LCP | Convertible WebP |\n")
    f.write("| --- | --- | ---: | ---: | ---: | --- | --- | --- |\n")
    for img in images:
        f.write(f"| `{img['rel_path']}` | {img['format']} | {img['dimensions']} | {img['size_kb']} KB | {img['references']} | {img['has_alpha']} | {img['critical']} | {img['webp_convertible']} |\n")

print("tables_step0.md written successfully.")
