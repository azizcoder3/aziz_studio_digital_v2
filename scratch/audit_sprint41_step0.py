import os
import glob
import re
import json
from PIL import Image

ROOT = r"c:\Users\Aziz\Desktop\aziz_studio_digital_v2"

def get_file_size_kb(filepath):
    return round(os.path.getsize(filepath) / 1024.0, 2)

def full_audit():
    # 1. HTML Pages (compiled at root)
    compiled_htmls = glob.glob(os.path.join(ROOT, "*.html"))
    source_htmls = glob.glob(os.path.join(ROOT, "pages", "**", "*.html"), recursive=True)
    comp_htmls = glob.glob(os.path.join(ROOT, "components", "*.html"))
    
    # 2. CSS Files
    css_files = glob.glob(os.path.join(ROOT, "assets", "css", "**", "*.css"), recursive=True)
    
    # 3. JS Files
    js_files = glob.glob(os.path.join(ROOT, "assets", "js", "**", "*.js"), recursive=True)
    
    # 4. Images
    img_files = []
    img_exts = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg')
    for root, dirs, files in os.walk(os.path.join(ROOT, "assets", "images")):
        for f in files:
            if f.lower().endswith(img_exts):
                img_files.append(os.path.join(root, f))

    # Build reference map
    ref_map = {os.path.relpath(img, ROOT).replace('\\', '/'): [] for img in img_files}
    file_name_ref_map = {os.path.basename(img): [] for img in img_files}

    search_files = compiled_htmls + source_htmls + comp_htmls + css_files + js_files
    for sf in search_files:
        rel_sf = os.path.relpath(sf, ROOT).replace('\\', '/')
        try:
            with open(sf, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                for img_rel in ref_map.keys():
                    img_name = os.path.basename(img_rel)
                    if img_rel in content or img_name in content:
                        ref_map[img_rel].append(rel_sf)
                        file_name_ref_map[img_name].append(rel_sf)
        except Exception as e:
            pass

    # Process images audit
    images_detail = []
    for img_path in sorted(img_files):
        rel_p = os.path.relpath(img_path, ROOT).replace('\\', '/')
        file_name = os.path.basename(img_path)
        ext = os.path.splitext(file_name)[1].lower()
        size_kb = get_file_size_kb(img_path)
        
        width, height, has_alpha = "N/A", "N/A", "Non"
        if ext in ('.png', '.jpg', '.jpeg', '.gif', '.webp'):
            try:
                with Image.open(img_path) as im:
                    width, height = im.size
                    has_alpha = "Oui" if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info) else "Non"
            except:
                pass
                
        refs = list(set(ref_map[rel_p] + file_name_ref_map[file_name]))
        
        is_hero_or_lcp = "hero" in rel_p.lower() or "banner" in rel_p.lower() or "logo" in rel_p.lower()
        
        images_detail.append({
            'rel_path': rel_p,
            'file_name': file_name,
            'format': ext[1:].upper(),
            'size_kb': size_kb,
            'dimensions': f"{width}x{height}" if width != "N/A" else "Vector/SVG",
            'has_alpha': has_alpha,
            'ref_count': len(refs),
            'references': ", ".join(sorted(refs)) if refs else "Non référencée (Orpheline)",
            'critical': "Oui" if is_hero_or_lcp else "Non",
            'webp_convertible': "Oui" if ext in ('.png', '.jpg', '.jpeg') else "Non (Déjà WebP/SVG)"
        })

    # Process pages audit
    pages_detail = []
    for hf in sorted(compiled_htmls):
        rel_p = os.path.basename(hf)
        size_kb = get_file_size_kb(hf)
        
        with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        img_tags = re.findall(r'<img[^>]+>', content, re.IGNORECASE)
        img_srcs = re.findall(r'src=["\']([^"\']+\.(?:png|jpg|jpeg|webp|svg))["\']', content, re.IGNORECASE)
        
        css_links = re.findall(r'<link[^>]+rel=["\']stylesheet["\'][^>]+>', content, re.IGNORECASE)
        js_scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\'][^>]*>', content, re.IGNORECASE)
        
        # Calculate image weight on page
        page_img_weight = 0.0
        missing_dims = 0
        missing_alt = 0
        lazy_on_lcp = False
        
        # Determine LCP candidate
        # Usually first img in hero or main section
        hero_section = re.search(r'<(section|header|div)[^>]*class=["\'][^"\']*(hero|banner|sector-hero)[^"\']*["\'][^>]*>(.*?)</\1>', content, re.DOTALL | re.IGNORECASE)
        hero_html = hero_section.group(0) if hero_section else content[:2000]
        hero_img_srcs = re.findall(r'src=["\']([^"\']+\.(?:png|jpg|jpeg|webp|svg))["\']', hero_html, re.IGNORECASE)
        lcp_img = hero_img_srcs[0] if hero_img_srcs else (img_srcs[0] if img_srcs else "Aucune (Dashboard CSS / SVG icon)")
        
        for tag in img_tags:
            if 'width=' not in tag or 'height=' not in tag:
                missing_dims += 1
            if 'alt=' not in tag:
                missing_alt += 1
            src_m = re.search(r'src=["\']([^"\']+)["\']', tag)
            if src_m:
                s = src_m.group(1)
                full_img_p = os.path.normpath(os.path.join(ROOT, s.replace('/', os.sep)))
                if os.path.exists(full_img_p):
                    page_img_weight += get_file_size_kb(full_img_p)
                if s == lcp_img and 'loading="lazy"' in tag:
                    lazy_on_lcp = True
                    
        issues = []
        if missing_dims > 0:
            issues.append(f"{missing_dims} <img> sans width/height (Risque CLS)")
        if missing_alt > 0:
            issues.append(f"{missing_alt} <img> sans alt")
        if lazy_on_lcp:
            issues.append(f"loading='lazy' sur l'image LCP ({lcp_img})")
        if "ODN.png" in content:
            issues.append("Contient ODN.png (5.3 MB ! Image critique à optimiser)")
            
        pages_detail.append({
            'page': rel_p,
            'size_kb': size_kb,
            'img_count': len(img_srcs),
            'img_weight_kb': round(page_img_weight, 2),
            'css_count': len(css_links),
            'js_count': len(js_scripts),
            'lcp_img': lcp_img,
            'issues': "; ".join(issues) if issues else "Aucun problème critique"
        })

    result = {
        'pages_detail': pages_detail,
        'images_detail': images_detail,
        'compiled_html_count': len(compiled_htmls),
        'source_html_count': len(source_htmls),
        'css_count': len(css_files),
        'js_count': len(js_files),
        'img_count': len(img_files)
    }
    
    with open(os.path.join(ROOT, "scratch", "step0_data.json"), "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
        
    print("DONE! step0_data.json written.")

if __name__ == '__main__':
    full_audit()
