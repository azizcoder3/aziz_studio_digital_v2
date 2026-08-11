import os
import glob

# Revert "24h à 72h" back to "24h à 48h" in all HTML files in pages/
pages_dir = 'pages'
html_files = glob.glob(os.path.join(pages_dir, '*.html'))

modified_files = []

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('24h à 72h', '24h à 48h')
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        modified_files.append(file_path)

print("Modified files:")
for m in modified_files:
    print(m)
