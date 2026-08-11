import os
import re
import sys
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"c:\Users\Aziz\Desktop\aziz_studio_digital_v2"


class HeadParser(HTMLParser):
    """Lightweight parser to extract <head> tag attributes."""
    def __init__(self):
        super().__init__()
        self.metas = []        # list of dict {name, property, content}
        self.links = []        # list of dict {rel, href, type}
        self.title = ""
        self.lang = ""
        self._in_title = False
        self._in_head = True
        self.html_attrs = {}
        self.schema_types = []
        self.ld_json_found = False
        self.headings = []     # ['h1','h2','h3',...]

    def handle_starttag(self, tag, attrs):
        attrs_d = dict(attrs)
        if tag == "html":
            self.lang = attrs_d.get("lang", "")
        if tag == "meta":
            self.metas.append(attrs_d)
        if tag == "link":
            self.links.append(attrs_d)
        if tag == "title":
            self._in_title = True
        if tag in ("h1","h2","h3","h4","h5","h6"):
            self.headings.append(tag)
        if "itemtype" in attrs_d:
            schema_url = attrs_d["itemtype"]
            m = re.search(r"schema\.org/(\w+)", schema_url)
            if m:
                t = m.group(1)
                if t not in self.schema_types:
                    self.schema_types.append(t)
        if tag == "script":
            if attrs_d.get("type","") == "application/ld+json":
                self.ld_json_found = True

    def handle_data(self, data):
        if self._in_title:
            self.title += data

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def get_meta(self, name_or_prop, value):
        """Return content of meta by name or property."""
        for m in self.metas:
            if m.get("name","").lower() == value.lower() or m.get("property","").lower() == value.lower():
                return m.get("content","")
        return ""

    def get_link(self, rel_value):
        for l in self.links:
            rel = l.get("rel","").lower()
            if rel == rel_value.lower():
                return l.get("href","")
        return ""


def parse_page(file_path):
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    parser = HeadParser()
    try:
        parser.feed(content)
    except Exception:
        pass

    return parser, content


def audit_pages():
    html_files = sorted([f for f in os.listdir(ROOT_DIR)
                         if f.endswith(".html") and os.path.isfile(os.path.join(ROOT_DIR, f))])

    # Check sitemap.xml and robots.txt
    sitemap_path = os.path.join(ROOT_DIR, "sitemap.xml")
    sitemap_exists = os.path.exists(sitemap_path)
    sitemap_urls = []
    if sitemap_exists:
        with open(sitemap_path, "r", encoding="utf-8") as f:
            sitemap_content = f.read()
            sitemap_urls = re.findall(r"<loc>(.*?)</loc>", sitemap_content)

    robots_path = os.path.join(ROOT_DIR, "robots.txt")
    robots_exists = os.path.exists(robots_path)
    robots_content = ""
    if robots_exists:
        with open(robots_path, "r", encoding="utf-8") as f:
            robots_content = f.read()

    results = []

    for file_name in html_files:
        file_path = os.path.join(ROOT_DIR, file_name)
        parser, raw_content = parse_page(file_path)

        # 1. Title
        title_clean = re.sub(r"\s+", " ", parser.title).strip()
        title_clean = title_clean.replace("&amp;", "&").replace("&quot;", '"').replace("&#039;", "'")
        title_len = len(title_clean)
        nb_pipes = title_clean.count("|")
        nb_titles = len(re.findall(r"<title[^>]*>", raw_content, re.IGNORECASE))

        # 2. Meta description
        desc_text = parser.get_meta("name", "description")
        desc_clean = desc_text.replace("&amp;", "&").replace("&quot;", '"').replace("&#039;", "'")
        desc_len = len(desc_clean)

        # 3. Canonical
        canonical_href = parser.get_link("canonical")
        canonical_status = canonical_href if canonical_href else "Absent"

        # 4. Open Graph
        og_props = ["og:title", "og:description", "og:type", "og:url", "og:image"]
        og_missing = [p for p in og_props if not parser.get_meta("property", p)]
        og_status = "Complet" if not og_missing else f"Manque: {', '.join(og_missing)}"

        # 5. Twitter Cards
        tw_names = ["twitter:card", "twitter:title", "twitter:description", "twitter:image"]
        tw_missing = [n for n in tw_names if not parser.get_meta("name", n)]
        tw_status = "Complet" if not tw_missing else f"Manque: {', '.join(tw_missing)}"

        # 6. Schema.org
        schemas = list(parser.schema_types)
        if parser.ld_json_found and "JSON-LD" not in schemas:
            schemas.append("JSON-LD")
        schema_status = ", ".join(schemas) if schemas else "Aucun"

        # 7. Favicon
        fav_href = parser.get_link("icon")
        if not fav_href:
            fav_href = parser.get_link("shortcut icon")
        fav_status = fav_href if fav_href else "Absent"

        # 8. Lang HTML
        lang = parser.lang if parser.lang else "Absent"

        # 9. Robots Meta
        robots_meta = parser.get_meta("name", "robots")
        robots_status = robots_meta if robots_meta else "Absent"

        # 10. Sitemap status
        in_sitemap = False
        if sitemap_exists:
            in_sitemap = (any(file_name in url for url in sitemap_urls) or
                          (file_name == "index.html" and any(url.endswith("/") for url in sitemap_urls)))
        if file_name == "404.html":
            sitemap_status = "Exclus (Normale)"
        else:
            sitemap_status = "Présent" if in_sitemap else "Absent"

        # 12. H1 count (from content, to include all page headings)
        h1_count = len(re.findall(r"<h1\b[^>]*>", raw_content, re.IGNORECASE))

        # 13. Hn Hierarchy check
        levels = [int(h[1]) for h in parser.headings]
        hn_coherent = True
        for i in range(len(levels) - 1):
            if levels[i+1] > levels[i] + 1:
                hn_coherent = False
                break
        hn_status = "OK" if hn_coherent else "Saut détecté"

        # Overall Status
        issues = []
        if nb_titles != 1:
            issues.append(f"Nb title ({nb_titles})")
        if title_len > 60:
            issues.append(f"Title trop long ({title_len} car.)")
        if nb_pipes != 1:
            issues.append(f"Pipes title ({nb_pipes})")
        if desc_len > 160:
            issues.append(f"Meta desc trop longue ({desc_len} car.)")
        if desc_len == 0:
            issues.append("Meta desc absente")
        if desc_len < 70 and desc_len > 0 and file_name not in ("404.html","mentions-legales.html","conditions-utilisation.html","politique-confidentialite.html"):
            issues.append(f"Meta desc très courte ({desc_len} car. < 70)")
        if canonical_status == "Absent":
            issues.append("Canonical absent")
        if og_missing:
            issues.append(f"OG incomplet ({len(og_missing)} manquant(s))")
        if tw_missing:
            issues.append(f"Twitter Card incomplet ({len(tw_missing)} manquant(s))")
        if fav_status == "Absent":
            issues.append("Favicon absent")
        if lang != "fr":
            issues.append(f"Lang HTML ({lang})")
        if robots_status == "Absent":
            issues.append("Robots meta absent")
        if sitemap_status == "Absent":
            issues.append("Absent du sitemap")
        if h1_count != 1:
            issues.append(f"H1 count ({h1_count})")
        if not hn_coherent:
            issues.append("Hiérarchie Hn (saut)")

        status_final = "CONFORME" if not issues else "NON CONFORME"

        results.append({
            "page": file_name,
            "title": title_clean,
            "title_len": title_len,
            "nb_pipes": nb_pipes,
            "desc": desc_clean,
            "desc_len": desc_len,
            "canonical": canonical_status,
            "og": og_status,
            "twitter": tw_status,
            "schema": schema_status,
            "favicon": fav_status,
            "lang": lang,
            "robots": robots_status,
            "sitemap": sitemap_status,
            "h1_count": h1_count,
            "hn": hn_status,
            "issues": issues,
            "status": status_final
        })

    # Print markdown table
    print("| Page | Title | Longueur | Nb | | Meta description | Longueur | Canonical | Open Graph | Twitter Cards | Schema.org | Favicon | Lang HTML | Robots meta | Sitemap | Statut |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for r in results:
        t_trunc = (r["title"][:28] + "...") if len(r["title"]) > 28 else r["title"]
        d_trunc = (r["desc"][:35] + "...") if len(r["desc"]) > 35 else r["desc"]
        print(f'| `{r["page"]}` | {t_trunc} | {r["title_len"]} | {r["nb_pipes"]} | {d_trunc} | {r["desc_len"]} | {r["canonical"]} | {r["og"]} | {r["twitter"]} | {r["schema"]} | {r["favicon"]} | {r["lang"]} | {r["robots"]} | {r["sitemap"]} | **{r["status"]}** |')

    print("\n--- ANOMALIES DÉTECTÉES PAR PAGE ---")
    non_conforme_count = 0
    for r in results:
        if r["issues"]:
            non_conforme_count += 1
            print(f"\n❌ `{r['page']}` ({len(r['issues'])} anomalie(s)) :")
            for issue in r["issues"]:
                print(f"  - {issue}")
        else:
            print(f"\n✅ `{r['page']}` : Conforme")

    print(f"\nRésumé : {len(results) - non_conforme_count}/{len(results)} pages conformes. {non_conforme_count} pages avec anomalies.")
    print(f"sitemap.xml : {'✅ Existe' if sitemap_exists else '❌ Absent'}")
    print(f"robots.txt : {'✅ Existe' if robots_exists else '❌ Absent'}")
    
    if robots_exists:
        has_sitemap_ref = "sitemap" in robots_content.lower()
        print(f"robots.txt contient ref sitemap : {'✅' if has_sitemap_ref else '❌ Manquant'}")
    
    if sitemap_exists:
        print(f"\nPages dans sitemap.xml :")
        for url in sitemap_urls:
            print(f"  {url}")

    return results


if __name__ == "__main__":
    audit_pages()
