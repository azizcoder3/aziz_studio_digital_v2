"""
Conversion WebP des images restantes du Sprint 41.
Qualité adaptée : hero/ODN = 85 (illustrations), portfolio thumbs = 82 (photos).
"""
import os
import sys

try:
    from PIL import Image
except ImportError:
    print("Pillow non disponible, installation en cours...")
    os.system(f"{sys.executable} -m pip install Pillow")
    from PIL import Image

ROOT = r'c:\Users\Aziz\Desktop\aziz_studio_digital_v2'

conversions = [
    # (source, destination, quality, lossless)
    (os.path.join(ROOT, 'assets', 'images', 'home', 'hero-illustration.png'),
     os.path.join(ROOT, 'assets', 'images', 'home', 'hero-illustration.webp'), 85, False),
    (os.path.join(ROOT, 'assets', 'images', 'portfolio', 'ODN.png'),
     os.path.join(ROOT, 'assets', 'images', 'portfolio', 'ODN.webp'), 85, False),
    (os.path.join(ROOT, 'assets', 'images', 'home', 'portfolio-boulevard-hotel.jpg'),
     os.path.join(ROOT, 'assets', 'images', 'home', 'portfolio-boulevard-hotel.webp'), 82, False),
    (os.path.join(ROOT, 'assets', 'images', 'home', 'portfolio-atre-steakhouse.jpg'),
     os.path.join(ROOT, 'assets', 'images', 'home', 'portfolio-atre-steakhouse.webp'), 82, False),
    (os.path.join(ROOT, 'assets', 'images', 'home', 'portfolio-cabinet-maxwell.jpg'),
     os.path.join(ROOT, 'assets', 'images', 'home', 'portfolio-cabinet-maxwell.webp'), 82, False),
    (os.path.join(ROOT, 'assets', 'images', 'home', 'portfolio-dental-glow.jpg'),
     os.path.join(ROOT, 'assets', 'images', 'home', 'portfolio-dental-glow.webp'), 82, False),
    (os.path.join(ROOT, 'assets', 'images', 'home', 'portfolio-molato-commerce.jpg'),
     os.path.join(ROOT, 'assets', 'images', 'home', 'portfolio-molato-commerce.webp'), 82, False),
    (os.path.join(ROOT, 'assets', 'images', 'home', 'agence-voyage.jpg'),
     os.path.join(ROOT, 'assets', 'images', 'home', 'agence-voyage.webp'), 82, False),
]

total_before = 0
total_after = 0

for src, dst, quality, lossless in conversions:
    if not os.path.exists(src):
        print(f"SKIP (absent) : {os.path.basename(src)}")
        continue
    
    src_size = os.path.getsize(src)
    total_before += src_size
    
    img = Image.open(src)
    # Conserver le canal alpha si présent (PNG avec transparence)
    if img.mode == 'RGBA':
        img.save(dst, 'WEBP', quality=quality, lossless=lossless, method=6)
    else:
        # Convertir en RGB si nécessaire (pour JPEG/modes palette)
        if img.mode not in ('RGB', 'RGBA'):
            img = img.convert('RGB')
        img.save(dst, 'WEBP', quality=quality, method=6)
    
    dst_size = os.path.getsize(dst)
    total_after += dst_size
    reduction = (1 - dst_size / src_size) * 100
    
    print(f"OK : {os.path.basename(src):40s} {src_size:>10,} -> {dst_size:>10,} ({reduction:+.1f}%)")

print(f"\n{'='*70}")
print(f"TOTAL : {total_before:>10,} -> {total_after:>10,} ({(1 - total_after/total_before)*100:+.1f}%)")
print(f"Économie : {(total_before - total_after):,} octets")
