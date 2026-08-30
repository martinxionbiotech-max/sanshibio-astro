#!/usr/bin/env python3
"""SEO audit for Sanshi Bio: scan all blog posts + pages for SEO issues."""
import re
from pathlib import Path

ROOT = Path("/home/admin/sanshibio-astro")
SITE = "https://sanshibio.com"

def parse_frontmatter(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, text[m.end():]

def extract_links(body):
    """Extract internal /path/ links and external http links from markdown."""
    internal = re.findall(r'\]\((/(?:en/)?[a-z0-9\-/]*)/?\)', body)
    external = re.findall(r'\]\((https?://[^)]+)\)', body)
    return internal, external

# collect all valid paths (static pages + blog slugs)
valid_paths = set()
for d in ["src/pages"]:
    for p in (ROOT / d).rglob("*.astro"):
        rel = str(p.relative_to(ROOT / d))
        if rel.endswith(".astro"):
            path = rel.replace("index.astro", "").replace("[slug].astro", "").replace(".astro", "")
            # remove trailing slash and dynamic segments
            path = "/" + path.strip("/")
            valid_paths.add(path)
            if path == "/blog" or path == "/en/blog":
                pass

blog_dirs = {"src/content/blog": "", "src/content/blog-en": "/en"}
blog_slugs = {"": set(), "/en": set()}
for rel_dir, prefix in blog_dirs.items():
    for f in sorted((ROOT / rel_dir).glob("*.md")):
        slug = f.stem
        blog_slugs[prefix].add(slug)
        valid_paths.add(f"{prefix}/blog/{slug}")

# add static routes manually (dirs)
for extra in ["/", "/about", "/contact", "/products", "/services",
              "/flight-ability", "/virus-detection", "/paternity",
              "/blog", "/disclaimer", "/privacy-policy",
              "/en", "/en/about", "/en/contact", "/en/products", "/en/services",
              "/en/flight-ability", "/en/virus-detection", "/en/paternity", "/en/blog"]:
    valid_paths.add(extra)

def is_valid_internal(link, current_prefix):
    link = link.rstrip("/")
    if not link:
        return True
    # normalize: if link starts with /en but current is zh, and vice versa
    return link in valid_paths or link + "/" in valid_paths or (link + "/") in valid_paths

print("=" * 70)
print("SEO 审计报告 — Sanshi Bio")
print("=" * 70)

issues = []
total = 0
for rel_dir, prefix in blog_dirs.items():
    for f in sorted((ROOT / rel_dir).glob("*.md")):
        total += 1
        text = f.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        slug = f.stem
        title = fm.get("title", "").strip().strip('"')
        desc = fm.get("description", "").strip().strip('"')
        cat = fm.get("category", "")
        tags = fm.get("tags", "")
        pub = fm.get("pubDate", "")

        # title length
        if len(title) > 60:
            issues.append(f"[title>60] {prefix}/blog/{slug}: {len(title)}字 | {title}")
        if len(title) < 15:
            issues.append(f"[title<15] {prefix}/blog/{slug}: {title}")
        # description length
        if len(desc) > 160:
            issues.append(f"[desc>160] {prefix}/blog/{slug}: {len(desc)}字")
        if len(desc) < 50:
            issues.append(f"[desc<50] {prefix}/blog/{slug}: {len(desc)}字")
        # H1 count
        h1 = len(re.findall(r'^#\s+', body, re.MULTILINE))
        if h1 != 1:
            issues.append(f"[H1={h1}] {prefix}/blog/{slug}")
        # FAQ count
        faq = len(re.findall(r'^###\s+', body, re.MULTILINE))
        # external links
        internal, external = extract_links(body)
        if not external:
            issues.append(f"[无外链] {prefix}/blog/{slug}")
        # broken internal links
        for link in internal:
            if not is_valid_internal(link, prefix):
                issues.append(f"[死链] {prefix}/blog/{slug}: {link}")

print(f"\n总文章数: {total}")
print(f"问题总数: {len(issues)}")
print("\n--- 问题清单 ---")
for i in issues:
    print(" ", i)

# 汇总统计
print("\n--- 统计 ---")
title_over = sum(1 for i in issues if i.startswith("[title>60]"))
desc_over = sum(1 for i in issues if i.startswith("[desc>160]"))
no_ext = sum(1 for i in issues if i.startswith("[无外链]"))
dead = sum(1 for i in issues if i.startswith("[死链]"))
h1bad = sum(1 for i in issues if i.startswith("[H1="))
print(f"  title>60字符: {title_over}")
print(f"  desc>160字符: {desc_over}")
print(f"  无外部权威链接: {no_ext}")
print(f"  死链: {dead}")
print(f"  H1异常: {h1bad}")
