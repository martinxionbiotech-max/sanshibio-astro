#!/usr/bin/env python3
"""Content depth scan: word count, FAQ count, tables, AIO structures per post."""
import re
from pathlib import Path

ROOT = Path("/home/admin/sanshibio-astro")

def parse(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    return text[m.end():] if m else text

def word_count(body):
    # Chinese chars + English words
    cn = len(re.findall(r'[\u4e00-\u9fff]', body))
    en = len(re.findall(r'[A-Za-z0-9]+', body))
    return cn + en  # rough proxy

def count_structures(body):
    faq = len(re.findall(r'^###\s+', body, re.MULTILINE))
    tables = len(re.findall(r'^\|.*\|$', body, re.MULTILINE)) // 2
    h2 = len(re.findall(r'^##\s+', body, re.MULTILINE))
    tldr = 1 if re.search(r'TL;DR|核心结论|一句话', body) else 0
    takeaways = 1 if re.search(r'Key Takeaways|核心要点|要点总结|关键要点', body) else 0
    glossary = 1 if re.search(r'Entity|实体|UniProt|NCBI Gene|基因数据库|中英对照', body) else 0
    data_box = 1 if re.search(r'关键数据|核心数据|关键指标', body) else 0
    return faq, tables, h2, tldr, takeaways, glossary, data_box

print(f"{'文章':<42} {'字数':>6} {'FAQ':>4} {'表':>3} {'H2':>3} {'TLDR':>4} {'要点':>4} {'实体':>4}")
print("-" * 85)

rows = []
for rel_dir, prefix in [("src/content/blog", "zh"), ("src/content/blog-en", "en")]:
    for f in sorted((ROOT / rel_dir).glob("*.md")):
        body = parse(f.read_text(encoding="utf-8"))
        wc = word_count(body)
        faq, tables, h2, tldr, takeaways, glossary, data_box = count_structures(body)
        rows.append((prefix, f.stem, wc, faq, tables, h2, tldr, takeaways, glossary))

# sort by word count ascending (weakest first)
rows.sort(key=lambda r: r[2])
for prefix, slug, wc, faq, tables, h2, tldr, takeaways, glossary in rows:
    name = f"{prefix}/{slug}"
    print(f"{name:<42} {wc:>6} {faq:>4} {tables:>3} {h2:>3} {tldr:>4} {takeaways:>4} {glossary:>4}")

# summary
weak = [r for r in rows if r[2] < 900]
few_faq = [r for r in rows if r[3] < 4]
print(f"\n=== 总结 ===")
print(f"总文章: {len(rows)}")
print(f"字数<900(薄弱): {len(weak)} 篇")
print(f"FAQ<4: {len(few_faq)} 篇")
print(f"平均字数: {sum(r[2] for r in rows)//len(rows)}")
