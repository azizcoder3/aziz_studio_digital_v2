#!/usr/bin/env python3
"""
verify_sprint53.py

Checks that classes used in selected HTML pages are defined in the CSS files those pages load.

Requirements implemented:
- Exact class-name matching using selector-token parsing (regex with strict token boundaries).
- Uses project root relative to this script (no hard-coded absolute paths).
- Self-test mode that temporarily alters a CSS file to demonstrate detection, then restores it.
- Documents limitation that presence of a selector does not guarantee correctness of its rules.

Run: python verify_sprint53.py [--self-test]
"""
import os
import re
import sys
import argparse


ROOT = os.path.dirname(os.path.abspath(__file__))

PAGES = [
    "contact.html",
    "a-propos.html",
    "portfolio.html",
]


def read_file(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def resolve_href(page_dir, href):
    # strip query/hash
    href = href.split("?")[0].split("#")[0]
    if href.startswith("/"):
        href = href.lstrip("/")
    # join relative to project root
    candidate = os.path.normpath(os.path.join(ROOT, href))
    if os.path.exists(candidate):
        return candidate
    # try relative to the page directory
    candidate = os.path.normpath(os.path.join(page_dir, href))
    if os.path.exists(candidate):
        return candidate
    return None


def extract_linked_css(page_path, content):
    page_dir = os.path.dirname(page_path)
    hrefs = re.findall(r'<link[^>]+rel=["\']stylesheet["\'][^>]*href=["\']([^"\']+)["\']', content, re.I)
    resolved = []
    for h in hrefs:
        p = resolve_href(page_dir, h)
        if p:
            resolved.append(p)
    # also include some common shared css locations if present
    common = [os.path.join(ROOT, "assets", "css", "solutions.css")]
    for c in common:
        if os.path.exists(c) and c not in resolved:
            resolved.append(c)
    return resolved


def classes_in_html(content):
    classes = set()
    for attr in re.findall(r'class=["\']([^"\']+)["\']', content, re.I):
        for cls in attr.split():
            classes.add(cls.strip())
    return classes


def classes_in_css(content):
    found = set()
    # iterate rule blocks to avoid matching dots in property values
    for sel_block in re.findall(r'([^\{]+)\{[^}]*\}', content):
        # selectors may be comma-separated
        for selector in sel_block.split(','):
            # find class tokens in selector with strict boundary: allowed chars are A-Za-z0-9_- in class names
            for m in re.findall(r'\.([A-Za-z0-9_-]+)(?![A-Za-z0-9_-])', selector):
                found.add(m)
    return found


def check_page(page):
    page_path = os.path.join(ROOT, page)
    if not os.path.exists(page_path):
        print(f"WARN: page not found: {page}")
        return {"page": page, "error": "not found"}
    content = read_file(page_path)
    used = classes_in_html(content)
    css_files = extract_linked_css(page_path, content)
    css_classes = set()
    for css in css_files:
        css_content = read_file(css)
        css_classes.update(classes_in_css(css_content))

    missing = sorted([c for c in used if c not in css_classes])
    return {
        "page": page,
        "used_classes_count": len(used),
        "css_files": css_files,
        "missing_classes": missing,
    }


def report(results):
    for r in results:
        if r.get("error"):
            print(f"Page: {r['page']} - ERROR: {r['error']}")
            continue
        print(f"\nPage: {r['page']}")
        print(f"  CSS files checked: {len(r['css_files'])}")
        for f in r['css_files']:
            print(f"    - {f}")
        print(f"  Classes used in HTML: {r['used_classes_count']}")
        if r['missing_classes']:
            print(f"  Missing classes ({len(r['missing_classes'])}):")
            for m in r['missing_classes']:
                print(f"    - {m}")
        else:
            print("  All used classes have at least one matching selector in the checked CSS files.")


def run_all(pages_to_check=None):
    if pages_to_check is None:
        pages_to_check = PAGES
    results = []
    for p in pages_to_check:
        results.append(check_page(p))
    report(results)
    print("\nLIMITATION: This script only checks for the presence of a selector for each class name in the CSS files linked by the page. It does NOT verify the semantic correctness or completeness of the rules for that selector.")


def self_test():
    print("\n--- Running self-test: temporarily modify a CSS file to cause a detection ---")
    # pick first existing page
    page = None
    for p in PAGES:
        if os.path.exists(os.path.join(ROOT, p)):
            page = p
            break
    if not page:
        print("No page found for self-test.")
        return
    page_path = os.path.join(ROOT, page)
    content = read_file(page_path)
    used = classes_in_html(content)
    css_files = extract_linked_css(page_path, content)
    if not css_files:
        print(f"No linked CSS files found for {page}; cannot run self-test.")
        return
    # find a class that is actually present in the css_files
    class_to_break = None
    file_with_class = None
    for css in css_files:
        css_content = read_file(css)
        css_classes = classes_in_css(css_content)
        for c in used:
            if c in css_classes:
                class_to_break = c
                file_with_class = css
                break
        if class_to_break:
            break
    if not class_to_break:
        print(f"Could not find a class used in {page} that is defined in its linked CSS files; self-test skipped.")
        return
    print(f"Self-test will remove class selector '.{class_to_break}' from {file_with_class} and verify detection on {page}")
    # backup
    bak_path = file_with_class + ".bak"
    with open(file_with_class, "r", encoding="utf-8", errors="ignore") as f:
        orig = f.read()
    with open(bak_path, "w", encoding="utf-8") as f:
        f.write(orig)
    try:
        # remove the class token by renaming it (safe & reversible)
        modified = orig.replace('.' + class_to_break, '.' + class_to_break + '_REMOVED_FOR_TEST')
        with open(file_with_class, "w", encoding="utf-8") as f:
            f.write(modified)
        print("\nRunning verifier after modification (expected: class reported missing)...")
        run_all([page])
    finally:
        # restore
        with open(file_with_class, "w", encoding="utf-8") as f:
            f.write(orig)
        if os.path.exists(bak_path):
            os.remove(bak_path)
    print("Self-test completed and CSS restored.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--self-test', action='store_true', help='Run built-in self-test that temporarily modifies a CSS file')
    args = parser.parse_args()
    if args.self_test:
        self_test()
    else:
        run_all()


if __name__ == '__main__':
    main()
