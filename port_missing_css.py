#!/usr/bin/env python3
"""
port_missing_css.py

Automatic helper: for each target page it uses verify_sprint53.check_page()
to get missing classes, searches the workspace for CSS rule blocks that
define those classes, and appends those blocks to the page-specific CSS
file (with a backup).

Usage: python port_missing_css.py
"""
import os
import re
import shutil
import importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))

PAGES = ["contact.html", "a-propos.html", "portfolio.html"]


def load_verifier():
    spec = importlib.util.spec_from_file_location("verify_sprint53", os.path.join(ROOT, "verify_sprint53.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def find_css_files():
    css_files = []
    for dirpath, dirs, files in os.walk(ROOT):
        for f in files:
            if f.endswith('.css'):
                css_files.append(os.path.join(dirpath, f))
    return css_files


def extract_blocks_containing_class(css_text, classname):
    blocks = []
    for m in re.finditer(r'([^\{]+)\{([^}]*)\}', css_text, re.S):
        selector = m.group(1)
        body = m.group(2)
        if re.search(r'\.' + re.escape(classname) + r'(?![A-Za-z0-9_-])', selector):
            blocks.append(selector.strip() + " {" + body + "}\n")
    return blocks


def append_blocks_to_file(page_css_path, blocks):
    bak = page_css_path + ".sprint53.bak"
    if not os.path.exists(bak):
        shutil.copy2(page_css_path, bak)
    with open(page_css_path, 'a', encoding='utf-8') as f:
        f.write('\n/* Auto-ported rules (Sprint53) */\n')
        for b in blocks:
            f.write(b)


def main():
    verifier = load_verifier()
    css_files = find_css_files()
    for page in PAGES:
        print(f"\nProcessing page: {page}")
        result = verifier.check_page(page)
        if result.get('error'):
            print("  page missing or error, skipping")
            continue
        missing = result.get('missing_classes', [])
        if not missing:
            print("  no missing classes")
            continue
        page_css = None
        for f in result.get('css_files', []):
            if f.endswith(os.path.splitext(page)[0] + '.css'):
                page_css = f
                break
        if not page_css:
            print("  could not locate page CSS file, skipping")
            continue
        all_blocks = []
        for cls in missing:
            found = False
            for css in css_files:
                try:
                    txt = open(css, 'r', encoding='utf-8', errors='ignore').read()
                except Exception:
                    continue
                blocks = extract_blocks_containing_class(txt, cls)
                if blocks:
                    found = True
                    for b in blocks:
                        if b not in all_blocks:
                            all_blocks.append(b)
                    break
            if not found:
                print(f"  WARNING: definition for .{cls} not found in workspace")
        if all_blocks:
            print(f"  Appending {len(all_blocks)} rule blocks to {page_css}")
            append_blocks_to_file(page_css, all_blocks)
        else:
            print("  No blocks found to append for this page")


if __name__ == '__main__':
    main()
