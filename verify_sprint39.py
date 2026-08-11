"""
verify_sprint39.py — Vérification automatique Sprint 39 : Audit SEO global
Aziz Studio Digital V2
"""
import os
import re
import sys
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = r"c:\Users\Aziz\Desktop\aziz_studio_digital_v2"

# ── Pages indexables (celles qui doivent figurer dans le sitemap) ───────────
INDEXED_PAGES = [
    "index.html",
    "services.html",
    "creation-site-web.html",
    "wordpress.html",
    "seo.html",
    "refonte-site.html",
    "maintenance.html",
    "audit-conseil.html",
    "solutions.html",
    "portfolio.html",
    "tarifs.html",
    "a-propos.html",
    "contact.html",
    "blog.html",
    "blog-article-seo.html",
    "blog-article-wordpress.html",
    "blog-article-developpement-web.html",
    "mentions-legales.html",
    "politique-confidentialite.html",
    "conditions-utilisation.html",
]

TITLE_MAX = 60
DESC_MAX  = 160
DESC_MIN  = 70   # recommandation minimale (hors pages légales/404)
LEGAL_PAGES = {"404.html", "mentions-legales.html", "politique-confidentialite.html", "conditions-utilisation.html"}

# ── HTML parser léger ────────────────────────────────────────────────────────
class HeadParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.metas   = []
        self.links   = []
        self.title   = ""
        self.lang    = ""
        self._in_title = False
        self.headings = []
        self.schema_types = []
        self.ld_json_found = False

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "html":
            self.lang = d.get("lang", "")
        if tag == "meta":
            self.metas.append(d)
        if tag == "link":
            self.links.append(d)
        if tag == "title":
            self._in_title = True
        if tag in ("h1","h2","h3","h4","h5","h6"):
            self.headings.append(tag)
        if "itemtype" in d:
            m = re.search(r"schema\.org/(\w+)", d["itemtype"])
            if m and m.group(1) not in self.schema_types:
                self.schema_types.append(m.group(1))
        if tag == "script" and d.get("type","") == "application/ld+json":
            self.ld_json_found = True

    def handle_data(self, data):
        if self._in_title:
            self.title += data

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def get_meta(self, attr, value):
        for m in self.metas:
            if m.get(attr,"").lower() == value.lower():
                return m.get("content","")
        return ""

    def get_link(self, rel):
        for l in self.links:
            if l.get("rel","").lower() == rel.lower():
                return l.get("href","")
        return ""


def parse(filepath):
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        raw = f.read()
    p = HeadParser()
    try:
        p.feed(raw)
    except Exception:
        pass
    return p, raw


# ── Helpers ──────────────────────────────────────────────────────────────────
PASS = "PASS"
FAIL = "FAIL"

def ok(cond):
    return PASS if cond else FAIL

def check_title(parser, raw):
    t = re.sub(r"\s+", " ", parser.title).strip().replace("&amp;","&").replace("&quot;",'"')
    nb = len(re.findall(r"<title[^>]*>", raw, re.IGNORECASE))
    issues = []
    if nb != 1:
        issues.append(f"Nombre de <title> = {nb} (attendu: 1)")
    if not t:
        issues.append("Title vide")
    elif len(t) > TITLE_MAX:
        issues.append(f"Title trop long : {len(t)} car. > {TITLE_MAX}")
    if t.count("|") != 1:
        issues.append(f"Séparateur '|' : {t.count('|')} (attendu: 1)")
    return t, issues

def check_desc(parser, page):
    d = parser.get_meta("name","description").replace("&amp;","&").replace("&quot;",'"')
    issues = []
    if not d:
        issues.append("Meta description absente")
    elif len(d) > DESC_MAX:
        issues.append(f"Meta desc trop longue : {len(d)} car. > {DESC_MAX}")
    elif len(d) < DESC_MIN and page not in LEGAL_PAGES:
        issues.append(f"Meta desc trop courte : {len(d)} car. < {DESC_MIN}")
    return d, issues

def check_og(parser):
    props = ["og:title","og:description","og:type","og:url","og:image"]
    missing = [p for p in props if not parser.get_meta("property", p)]
    return missing

def check_twitter(parser):
    names = ["twitter:card","twitter:title","twitter:description","twitter:image"]
    missing = [n for n in names if not parser.get_meta("name", n)]
    return missing

def check_hn(parser):
    levels = [int(h[1]) for h in parser.headings]
    for i in range(len(levels)-1):
        if levels[i+1] > levels[i]+1:
            return False, f"Saut H{levels[i]}→H{levels[i+1]}"
    return True, "OK"

def check_internal_links(raw, page):
    """Detect href to .html files that don't exist in the root dir."""
    links = re.findall(r'href=["\']([^"\'#?]+\.html)["\']', raw, re.IGNORECASE)
    broken = []
    for lnk in links:
        if lnk.startswith("http"):
            continue
        target = os.path.join(ROOT_DIR, lnk)
        if not os.path.exists(target):
            if lnk not in broken:
                broken.append(lnk)
    return broken


# ── Main verification ─────────────────────────────────────────────────────────
def main():
    print("=" * 70)
    print("  verify_sprint39.py — Audit SEO global — Aziz Studio Digital V2")
    print("=" * 70)

    # ── Fichiers
    html_files = sorted([f for f in os.listdir(ROOT_DIR)
                         if f.endswith(".html") and os.path.isfile(os.path.join(ROOT_DIR, f))])

    # ── sitemap.xml
    sitemap_path  = os.path.join(ROOT_DIR, "sitemap.xml")
    sitemap_exists = os.path.exists(sitemap_path)
    sitemap_urls  = []
    if sitemap_exists:
        with open(sitemap_path, "r", encoding="utf-8") as f:
            sitemap_urls = re.findall(r"<loc>(.*?)</loc>", f.read())

    # ── robots.txt
    robots_path   = os.path.join(ROOT_DIR, "robots.txt")
    robots_exists = os.path.exists(robots_path)
    robots_content = ""
    if robots_exists:
        with open(robots_path, "r", encoding="utf-8") as f:
            robots_content = f.read()

    global_issues = []
    page_results  = {}

    for page in html_files:
        path = os.path.join(ROOT_DIR, page)
        parser, raw = parse(path)

        r = {}

        # 1. Title
        title, t_issues = check_title(parser, raw)
        r["title"]    = title
        r["t_issues"] = t_issues

        # 2. Meta desc
        desc, d_issues = check_desc(parser, page)
        r["desc"]     = desc
        r["d_issues"] = d_issues

        # 3. Canonical
        canon = parser.get_link("canonical")
        r["canonical"] = canon
        r["c_issue"]   = [] if canon else ["Canonical absent"]

        # 4. Open Graph
        og_miss = check_og(parser)
        r["og_miss"] = og_miss

        # 5. Twitter Cards
        tw_miss = check_twitter(parser)
        r["tw_miss"] = tw_miss

        # 6. Schema.org
        schemas = list(parser.schema_types)
        if parser.ld_json_found and "JSON-LD" not in schemas:
            schemas.append("JSON-LD")
        r["schema"] = schemas

        # 7. Favicon
        fav = parser.get_link("icon") or parser.get_link("shortcut icon")
        r["fav"]      = fav
        r["fav_issue"] = [] if fav else ["Favicon absent"]

        # 8. Lang
        r["lang"]      = parser.lang
        r["lang_issue"] = [] if parser.lang == "fr" else [f"lang='{parser.lang}' (attendu: fr)"]

        # 9. Robots meta
        robots_meta = parser.get_meta("name","robots")
        r["robots_meta"] = robots_meta
        r["rm_issue"]    = [] if robots_meta else ["Robots meta absent"]

        # 10. Sitemap membership
        if page == "404.html":
            r["sitemap"] = "Exclus (normale)"
            r["sm_issue"] = []
        elif page in INDEXED_PAGES:
            in_sm = any(page in u for u in sitemap_urls) or (page == "index.html" and any(u.endswith("/") for u in sitemap_urls))
            r["sitemap"]  = "Présent" if in_sm else "Absent"
            r["sm_issue"] = [] if in_sm else [f"{page} absent du sitemap"]
        else:
            r["sitemap"]  = "Non requis"
            r["sm_issue"] = []

        # 11. H1
        h1s = len(re.findall(r"<h1\b[^>]*>", raw, re.IGNORECASE))
        r["h1"]      = h1s
        r["h1_issue"] = [] if h1s == 1 else [f"H1 count = {h1s} (attendu: 1)"]

        # 12. Hn hierarchy
        hn_ok, hn_msg = check_hn(parser)
        r["hn"]      = hn_msg
        r["hn_issue"] = [] if hn_ok else [f"Hn: {hn_msg}"]

        # 13. Internal links
        broken = check_internal_links(raw, page)
        r["broken"] = broken
        r["bl_issue"] = [f"Lien cassé: {lnk}" for lnk in broken]

        # Aggregate all issues
        all_issues = (r["t_issues"] + r["d_issues"] + r["c_issue"] +
                      [f"OG manque: {p}" for p in r["og_miss"]] +
                      [f"Twitter manque: {n}" for n in r["tw_miss"]] +
                      r["fav_issue"] + r["lang_issue"] + r["rm_issue"] +
                      r["sm_issue"] + r["h1_issue"] + r["hn_issue"] + r["bl_issue"])
        r["issues"] = all_issues
        r["status"] = PASS if not all_issues else FAIL

        page_results[page] = r
        if all_issues:
            global_issues.extend([(page, i) for i in all_issues])

    # ── RAPPORT ───────────────────────────────────────────────────────────────
    print("\n📋  RÉSULTATS PAR CRITÈRE\n")

    # --- 1. Titles ---
    t_fails = [p for p,r in page_results.items() if r["t_issues"]]
    print(f"[{ok(not t_fails)}] Balises <title>  — {len(html_files)-len(t_fails)}/{len(html_files)} conformes")
    for p in t_fails:
        for i in page_results[p]["t_issues"]:
            print(f"       ↳ {p}: {i}")

    # --- 2. Meta descriptions ---
    d_fails = [p for p,r in page_results.items() if r["d_issues"]]
    print(f"[{ok(not d_fails)}] Meta descriptions — {len(html_files)-len(d_fails)}/{len(html_files)} conformes")
    for p in d_fails:
        for i in page_results[p]["d_issues"]:
            print(f"       ↳ {p}: {i}")

    # --- 3. Canonical ---
    c_fails = [p for p,r in page_results.items() if r["c_issue"]]
    print(f"[{ok(not c_fails)}] Canonical        — {len(html_files)-len(c_fails)}/{len(html_files)} conformes")
    for p in c_fails:
        print(f"       ↳ {p}: Canonical absent")

    # --- 4. Open Graph ---
    og_fails = [p for p,r in page_results.items() if r["og_miss"]]
    print(f"[{ok(not og_fails)}] Open Graph       — {len(html_files)-len(og_fails)}/{len(html_files)} conformes")
    for p in og_fails:
        print(f"       ↳ {p}: Manque {', '.join(page_results[p]['og_miss'])}")

    # --- 5. Twitter Cards ---
    tw_fails = [p for p,r in page_results.items() if r["tw_miss"]]
    print(f"[{ok(not tw_fails)}] Twitter Cards    — {len(html_files)-len(tw_fails)}/{len(html_files)} conformes")
    for p in tw_fails:
        print(f"       ↳ {p}: Manque {', '.join(page_results[p]['tw_miss'])}")

    # --- 6. Schema.org ---
    # Not a failure if absent — just report what's present
    schema_present = {p:r["schema"] for p,r in page_results.items() if r["schema"]}
    print(f"[{PASS}] Schema.org       — Présent sur {len(schema_present)} page(s)")
    for p,s in schema_present.items():
        print(f"       ↳ {p}: {', '.join(s)}")

    # --- 7. Favicon ---
    fav_fails = [p for p,r in page_results.items() if r["fav_issue"]]
    print(f"[{ok(not fav_fails)}] Favicon          — {len(html_files)-len(fav_fails)}/{len(html_files)} conformes")

    # --- 8. Lang HTML ---
    lang_fails = [p for p,r in page_results.items() if r["lang_issue"]]
    print(f"[{ok(not lang_fails)}] Lang HTML (fr)   — {len(html_files)-len(lang_fails)}/{len(html_files)} conformes")

    # --- 9. Robots meta ---
    rm_fails = [p for p,r in page_results.items() if r["rm_issue"]]
    print(f"[{ok(not rm_fails)}] Robots meta      — {len(html_files)-len(rm_fails)}/{len(html_files)} conformes")

    # --- 10. Sitemap ---
    print(f"[{ok(sitemap_exists)}] sitemap.xml      — {'Existe' if sitemap_exists else 'ABSENT'}")
    sm_fails = [p for p,r in page_results.items() if r["sm_issue"]]
    print(f"[{ok(not sm_fails)}] Pages dans sitemap — {len(INDEXED_PAGES)-len(sm_fails)}/{len(INDEXED_PAGES)} présentes")
    for p in sm_fails:
        print(f"       ↳ {p}: absent du sitemap")

    # --- 11. robots.txt ---
    print(f"[{ok(robots_exists)}] robots.txt       — {'Existe' if robots_exists else 'ABSENT'}")
    has_sitemap_ref = "sitemap" in robots_content.lower() if robots_exists else False
    print(f"[{ok(has_sitemap_ref)}] robots.txt sitemap ref — {'✅' if has_sitemap_ref else '❌ Manquant'}")

    # --- 12. H1 ---
    h1_fails = [p for p,r in page_results.items() if r["h1_issue"]]
    print(f"[{ok(not h1_fails)}] H1 (exactement 1) — {len(html_files)-len(h1_fails)}/{len(html_files)} conformes")
    for p in h1_fails:
        for i in page_results[p]["h1_issue"]:
            print(f"       ↳ {p}: {i}")

    # --- 13. Hn Hierarchy ---
    hn_fails = [p for p,r in page_results.items() if r["hn_issue"]]
    print(f"[{ok(not hn_fails)}] Hiérarchie Hn    — {len(html_files)-len(hn_fails)}/{len(html_files)} conformes")
    for p in hn_fails:
        print(f"       ↳ {p}: {page_results[p]['hn']}")

    # --- 14. Liens internes ---
    bl_fails = [p for p,r in page_results.items() if r["bl_issue"]]
    print(f"[{ok(not bl_fails)}] Liens internes   — {len(html_files)-len(bl_fails)}/{len(html_files)} sans lien cassé")
    for p in bl_fails:
        for i in page_results[p]["bl_issue"]:
            print(f"       ↳ {p}: {i}")

    # ── RÉSUMÉ GLOBAL ─────────────────────────────────────────────────────────
    total_pages = len(html_files)
    pass_pages  = sum(1 for r in page_results.values() if r["status"] == PASS)
    fail_pages  = total_pages - pass_pages

    print("\n" + "=" * 70)
    print(f"  RÉSULTAT GLOBAL : {pass_pages}/{total_pages} pages PASS")
    if global_issues:
        print(f"  ⚠  {len(global_issues)} anomalie(s) détectée(s) :")
        for page, issue in global_issues:
            print(f"     [{page}] {issue}")
    else:
        print("  ✅ Aucune anomalie — toutes les pages sont conformes.")
    print("=" * 70)

    return 0 if fail_pages == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
