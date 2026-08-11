import json
import os

ROOT = r"c:\Users\Aziz\Desktop\aziz_studio_digital_v2"
with open(os.path.join(ROOT, "scratch", "step0_data.json"), "r", encoding="utf-8") as f:
    data = json.load(f)

pages = data['pages_detail']
images = data['images_detail']

print(f"Total Pages compilées: {data['compiled_html_count']}")
print(f"Total Pages sources: {data['source_html_count']}")
print(f"Total CSS files: {data['css_count']}")
print(f"Total JS files: {data['js_count']}")
print(f"Total Image files: {data['img_count']}")

print("\n--- TABLEAU 1: AUDIT PAR PAGE HTML (Étape 0) ---")
print("| Page | Taille HTML | Nombre d'images | Poids des images | Nb CSS | Nb JS | Image LCP potentielle | Problèmes détectés |")
print("| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |")
total_html_size = 0
total_img_weight = 0
for p in pages:
    total_html_size += p['size_kb']
    total_img_weight += p['img_weight_kb']
    print(f"| `{p['page']}` | {p['size_kb']} KB | {p['img_count']} | {p['img_weight_kb']} KB | {p['css_count']} | {p['js_count']} | `{p['lcp_img']}` | {p['issues']} |")

print(f"\nTotal Taille HTML: {round(total_html_size, 2)} KB")

print("\n--- TABLEAU 2: INVENTAIRE COMPLET DES IMAGES (Étape 0) ---")
print("| Image | Format | Dimensions | Poids | Références | Transparence | Critique / LCP | Convertible WebP |")
print("| --- | --- | ---: | ---: | ---: | --- | --- | --- |")
total_img_file_weight = 0
raster_count = 0
webp_count = 0
svg_count = 0
convertible_count = 0
convertible_weight = 0
orphans = []
heavy_imgs = []

for img in images:
    total_img_file_weight += img['size_kb']
    fmt = img['format']
    if fmt in ('PNG', 'JPG', 'JPEG', 'GIF'):
        raster_count += 1
        if img['webp_convertible'] == "Oui":
            convertible_count += 1
            convertible_weight += img['size_kb']
    elif fmt == 'WEBP':
        webp_count += 1
    elif fmt == 'SVG':
        svg_count += 1
        
    if img['ref_count'] == 0:
        orphans.append(img)
    if img['size_kb'] > 100:
        heavy_imgs.append(img)
        
    refs_short = f"{img['ref_count']} fichier(s)" if img['ref_count'] > 0 else "0 (Orpheline)"
    print(f"| `{img['rel_path']}` | {img['format']} | {img['dimensions']} | {img['size_kb']} KB | {refs_short} | {img['has_alpha']} | {img['critical']} | {img['webp_convertible']} |")

print(f"\nTotal Poids Toutes Images: {round(total_img_file_weight / 1024.0, 2)} MB ({round(total_img_file_weight, 2)} KB)")
print(f"Images Raster non-WebP: {raster_count} ({convertible_count} convertibles vers WebP pour un poids de {round(convertible_weight / 1024.0, 2)} MB)")
print(f"Images WebP existantes: {webp_count}")
print(f"Images SVG (vectorielles): {svg_count}")

print(f"\n--- IMAGES INUTILISÉES / ORPHELINES ({len(orphans)}) ---")
for o in orphans:
    print(f"- `{o['rel_path']}` ({o['format']}, {o['dimensions']}, {o['size_kb']} KB)")

print(f"\n--- IMAGES TRÈS LOURDES / SURDIMENSIONNÉES > 100 KB ({len(heavy_imgs)}) ---")
for h in heavy_imgs:
    print(f"- `{h['rel_path']}` ({h['format']}, {h['dimensions']}, {h['size_kb']} KB, Transparence: {h['has_alpha']}, Refs: {h['ref_count']})")
