import os
import re
import subprocess
from datetime import date

def get_git_date(filename):
    try:
        res = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", filename],
            capture_output=True,
            text=True,
            check=True
        )
        val = res.stdout.strip()
        if val:
            return val
    except Exception:
        pass
    return date.today().isoformat()

def main():
    sitemap_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sitemap.xml")
    with open(sitemap_path, "r", encoding="utf-8", newline="") as f:
        content = f.read()

    url_pattern = re.compile(r"(  <url>[\s\S]*?  </url>)")
    
    urls_processed = 0
    dates_modified = 0

    def replace_url(match):
        nonlocal urls_processed, dates_modified
        block = match.group(1)
        urls_processed += 1
        
        loc_match = re.search(r"<loc>(.*?)</loc>", block)
        if not loc_match:
            return block
        
        loc = loc_match.group(1).strip()
        if loc.endswith("/"):
            filename = "index.html"
        else:
            filename = loc.split("/")[-1]
            
        git_date = get_git_date(filename)
        
        lastmod_match = re.search(r"(<lastmod>)(.*?)(</lastmod>)", block)
        if lastmod_match:
            old_date = lastmod_match.group(2)
            if old_date != git_date:
                dates_modified += 1
                start, end = lastmod_match.span(2)
                block = block[:start] + git_date + block[end:]
                
        return block

    new_content = url_pattern.sub(replace_url, content)

    with open(sitemap_path, "w", encoding="utf-8", newline="") as f:
        f.write(new_content)

    print(f"Nombre d'URLs traitées : {urls_processed}")
    print(f"Nombre de dates modifiées : {dates_modified}")

if __name__ == "__main__":
    main()
