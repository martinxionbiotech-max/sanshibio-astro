#!/usr/bin/env python3
"""Generate public/sitemap.xml for Sanshi Bio from static pages + content collections."""
import os
from pathlib import Path

SITE = "https://sanshibio.com"
ROOT = Path(__file__).resolve().parent.parent

# static pages: path -> priority
PAGES = {
    "/": 1.0,
    "/flight-ability": 0.9,
    "/paternity": 0.9,
    "/products": 0.9,
    "/virus-detection": 0.9,
    "/services": 0.8,
    "/about": 0.6,
    "/contact": 0.6,
    "/blog": 0.3,
    "/disclaimer": 0.3,
    "/privacy-policy": 0.3,
    "/en": 0.9,
    "/en/about": 0.9,
    "/en/blog": 0.9,
    "/en/contact": 0.9,
    "/en/flight-ability": 0.9,
    "/en/paternity": 0.9,
    "/en/products": 0.9,
    "/en/services": 0.9,
    "/en/virus-detection": 0.9,
}

def slugs(rel_dir: str, prefix: str) -> list[tuple[str, float]]:
    d = ROOT / rel_dir
    out = []
    for f in sorted(d.glob("*.md")):
        out.append((f"{prefix}/{f.stem}", 0.6))
    return out

urls = list(PAGES.items())
urls += slugs("src/content/blog", "/blog")
urls += slugs("src/content/blog-en", "/en/blog")

lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for path, prio in urls:
    lines.append(f'  <url><loc>{SITE}{path}</loc><priority>{prio}</priority></url>')
lines.append('</urlset>')

out = ROOT / "public" / "sitemap.xml"
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Wrote {out} with {len(urls)} URLs")
