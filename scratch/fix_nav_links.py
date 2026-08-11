import os
import re

ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'
PAGES_DIR = os.path.join(ROOT, 'pages')

sector_nav_pattern = re.compile(
    r'<a\s+href="([^"]+)"\s+class="sector-nav-link"([^>]*)>(.*?<div class="sector-nav-title">([^<]+)</div>.*?)</a>',
    re.DOTALL
)

projet_nav_pattern = re.compile(
    r'<a\s+href="([^"]+)"\s+class="projet-nav-card\s+(nav-prev|nav-next)"([^>]*)>(.*?<span class="projet-nav-name">([^<]+)</span>.*?)</a>',
    re.DOTALL
)

count = 0

for root, _, files in os.walk(PAGES_DIR):
    for filename in files:
        if filename.endswith('.html'):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = content
            
            # Replace sector links
            def repl_sector(m):
                href = m.group(1)
                other_attrs = m.group(2)
                inner_html = m.group(3)
                target_name = m.group(4).strip()
                
                # Check if it already has aria-label
                if 'aria-label=' in other_attrs:
                    return m.group(0)
                
                # Determine direction
                direction = "précédent" if "Secteur précédent" in inner_html else "suivant"
                new_aria = f' aria-label="Secteur {direction} : {target_name}"'
                
                global count
                count += 1
                return f'<a href="{href}" class="sector-nav-link"{other_attrs}{new_aria}>{inner_html}</a>'

            new_content = sector_nav_pattern.sub(repl_sector, new_content)

            # Replace project links
            def repl_projet(m):
                href = m.group(1)
                direction_class = m.group(2) # nav-prev or nav-next
                other_attrs = m.group(3)
                inner_html = m.group(4)
                target_name = m.group(5).strip()
                
                if 'aria-label=' in other_attrs:
                    return m.group(0)
                
                direction = "précédent" if direction_class == "nav-prev" else "suivant"
                new_aria = f' aria-label="Projet {direction} : {target_name}"'
                
                global count
                count += 1
                return f'<a href="{href}" class="projet-nav-card {direction_class}"{other_attrs}{new_aria}>{inner_html}</a>'

            new_content = projet_nav_pattern.sub(repl_projet, new_content)

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")

print(f"Total links updated: {count}")
