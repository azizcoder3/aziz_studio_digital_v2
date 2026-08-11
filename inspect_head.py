import os, re

ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'
pages = [f for f in os.listdir(ROOT) if f.endswith('.html')]

for p in sorted(pages):
    fp = os.path.join(ROOT, p)
    content = open(fp, encoding='utf-8').read()
    
    t_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    m_match = re.search(r'<meta\s+[^>]*name=["\']description["\']\s+[^>]*content=["\'](.*?)["\']', content, re.IGNORECASE | re.DOTALL)
    if not m_match:
        m_match = re.search(r'<meta\s+[^>]*content=["\'](.*?)["\']\s+[^>]*name=["\']description["\']', content, re.IGNORECASE | re.DOTALL)
        
    title = t_match.group(1).strip() if t_match else "MISSING"
    meta = m_match.group(1).strip() if m_match else "MISSING"
    
    print(f"Page: {p}")
    print(f"  Title ({len(title)} chars): {repr(title)}")
    print(f"  Meta  ({len(meta)} chars): {repr(meta)}")
    print()
