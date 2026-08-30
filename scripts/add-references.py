#!/usr/bin/env python3
"""Add authoritative external links (References section) to every blog post."""
import re
from pathlib import Path

ROOT = Path("/home/admin/sanshibio-astro")

# slug -> list of (url, zh_label, en_label)
REFS = {
    # 基因类
    "ldha-endurance-gene": [
        ("https://en.wikipedia.org/wiki/Lactate_dehydrogenase", "乳酸脱氢酶 — 维基百科", "Lactate dehydrogenase — Wikipedia"),
        ("https://www.ncbi.nlm.nih.gov/gene/3938", "LDHA 基因 — NCBI Gene", "LDHA gene — NCBI Gene"),
    ],
    "mstn-muscle-gene": [
        ("https://en.wikipedia.org/wiki/Myostatin", "肌肉生长抑制素 — 维基百科", "Myostatin — Wikipedia"),
        ("https://www.ncbi.nlm.nih.gov/gene/2660", "MSTN 基因 — NCBI Gene", "MSTN gene — NCBI Gene"),
    ],
    "drd4-homing-gene": [
        ("https://en.wikipedia.org/wiki/Dopamine_receptor_D4", "多巴胺受体 D4 — 维基百科", "Dopamine receptor D4 — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Racing_pigeon", "赛鸽 — 维基百科", "Racing pigeon — Wikipedia"),
    ],
    "cry1-navigation-gene": [
        ("https://en.wikipedia.org/wiki/Cryptochrome", "隐花色素 — 维基百科", "Cryptochrome — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Racing_pigeon", "赛鸽 — 维基百科", "Racing pigeon — Wikipedia"),
    ],
    "f-ker-feather-gene": [
        ("https://en.wikipedia.org/wiki/Keratin", "角蛋白 — 维基百科", "Keratin — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Feather", "羽毛 — 维基百科", "Feather — Wikipedia"),
    ],
    "lrp8-gsr-cask-genes": [
        ("https://en.wikipedia.org/wiki/Glutathione_reductase", "谷胱甘肽还原酶 — 维基百科", "Glutathione reductase — Wikipedia"),
        ("https://en.wikipedia.org/wiki/LRP8", "LRP8 — 维基百科", "LRP8 — Wikipedia"),
    ],
    "speed-distance-gene": [
        ("https://en.wikipedia.org/wiki/Racing_pigeon", "赛鸽 — 维基百科", "Racing pigeon — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Rock_dove", "原鸽 — 维基百科", "Rock dove — Wikipedia"),
    ],
    # 病毒/病原类
    "newcastle-disease-control": [
        ("https://en.wikipedia.org/wiki/Newcastle_disease", "新城疫 — 维基百科", "Newcastle disease — Wikipedia"),
        ("https://www.woah.org/en/disease/newcastle-disease/", "新城疫 — 世界动物卫生组织(WOAH)", "Newcastle disease — WOAH"),
    ],
    "avian-influenza-screening": [
        ("https://en.wikipedia.org/wiki/Avian_influenza", "禽流感 — 维基百科", "Avian influenza — Wikipedia"),
        ("https://www.woah.org/en/disease/avian-influenza/", "禽流感 — 世界动物卫生组织(WOAH)", "Avian influenza — WOAH"),
    ],
    "mycoplasma-detection": [
        ("https://en.wikipedia.org/wiki/Mycoplasma", "支原体 — 维基百科", "Mycoplasma — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Chronic_respiratory_disease", "慢性呼吸道病 — 维基百科", "Chronic respiratory disease — Wikipedia"),
    ],
    "chlamydia-psittaci-control": [
        ("https://en.wikipedia.org/wiki/Chlamydia_psittaci", "鹦鹉热衣原体 — 维基百科", "Chlamydia psittaci — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Psittacosis", "鹦鹉热 — 维基百科", "Psittacosis — Wikipedia"),
    ],
    "salmonella-paratyphoid": [
        ("https://en.wikipedia.org/wiki/Salmonella", "沙门氏菌 — 维基百科", "Salmonella — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Paratyphoid_fever", "副伤寒 — 维基百科", "Paratyphoid fever — Wikipedia"),
    ],
    "pigeon-circovirus-adenovirus": [
        ("https://en.wikipedia.org/wiki/Circovirus", "圆环病毒 — 维基百科", "Circovirus — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Adenoviridae", "腺病毒科 — 维基百科", "Adenoviridae — Wikipedia"),
    ],
    "pigeon-pox-herpes-rotavirus": [
        ("https://en.wikipedia.org/wiki/Fowlpox", "禽痘 — 维基百科", "Fowlpox — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Rotavirus", "轮状病毒 — 维基百科", "Rotavirus — Wikipedia"),
    ],
    "trichomonas-candida-control": [
        ("https://en.wikipedia.org/wiki/Trichomonas_gallinae", "鸽毛滴虫 — 维基百科", "Trichomonas gallinae — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Candida_(fungus)", "念珠菌属 — 维基百科", "Candida (fungus) — Wikipedia"),
    ],
    "antibody-titer-test": [
        ("https://en.wikipedia.org/wiki/Antibody", "抗体 — 维基百科", "Antibody — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Hemagglutination_assay", "血凝试验 — 维基百科", "Hemagglutination assay — Wikipedia"),
    ],
    # 技术/服务类
    "qpcr-principle": [
        ("https://en.wikipedia.org/wiki/Real-time_polymerase_chain_reaction", "实时荧光定量PCR — 维基百科", "Real-time PCR — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Polymerase_chain_reaction", "聚合酶链式反应 — 维基百科", "Polymerase chain reaction — Wikipedia"),
    ],
    "reagent-kit-overview": [
        ("https://en.wikipedia.org/wiki/Polymerase_chain_reaction", "聚合酶链式反应 — 维基百科", "Polymerase chain reaction — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Nucleic_acid", "核酸 — 维基百科", "Nucleic acid — Wikipedia"),
    ],
    "lab-equipment-guide": [
        ("https://en.wikipedia.org/wiki/Polymerase_chain_reaction", "聚合酶链式反应 — 维基百科", "Polymerase chain reaction — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Nucleic_acid_extraction", "核酸提取 — 维基百科", "Nucleic acid extraction — Wikipedia"),
    ],
    "paternity-test-guide": [
        ("https://en.wikipedia.org/wiki/DNA_profiling", "DNA 分型 — 维基百科", "DNA profiling — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Single-nucleotide_polymorphism", "单核苷酸多态性 — 维基百科", "Single-nucleotide polymorphism — Wikipedia"),
    ],
    "gene-id-card-guide": [
        ("https://en.wikipedia.org/wiki/Single-nucleotide_polymorphism", "单核苷酸多态性 — 维基百科", "Single-nucleotide polymorphism — Wikipedia"),
        ("https://en.wikipedia.org/wiki/DNA_profiling", "DNA 分型 — 维基百科", "DNA profiling — Wikipedia"),
    ],
    "ab-pigeon-detection": [
        ("https://en.wikipedia.org/wiki/DNA_profiling", "DNA 分型 — 维基百科", "DNA profiling — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Racing_pigeon", "赛鸽 — 维基百科", "Racing pigeon — Wikipedia"),
    ],
    "pigeon-sex-identification": [
        ("https://en.wikipedia.org/wiki/ZW_sex-determination_system", "ZW 性别决定系统 — 维基百科", "ZW sex-determination system — Wikipedia"),
        ("https://en.wikipedia.org/wiki/CHD1", "CHD1 基因 — 维基百科", "CHD1 — Wikipedia"),
    ],
    "feather-sampling-guide": [
        ("https://en.wikipedia.org/wiki/Feather", "羽毛 — 维基百科", "Feather — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Rock_dove", "原鸽 — 维基百科", "Rock dove — Wikipedia"),
    ],
    "sample-collection-guide": [
        ("https://en.wikipedia.org/wiki/Feather", "羽毛 — 维基百科", "Feather — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Racing_pigeon", "赛鸽 — 维基百科", "Racing pigeon — Wikipedia"),
    ],
    "breeding-selection-guide": [
        ("https://en.wikipedia.org/wiki/Rock_dove", "原鸽 — 维基百科", "Rock dove — Wikipedia"),
        ("https://en.wikipedia.org/wiki/Racing_pigeon", "赛鸽 — 维基百科", "Racing pigeon — Wikipedia"),
    ],
    "test-report-interpretation": [
        ("https://en.wikipedia.org/wiki/Real-time_polymerase_chain_reaction", "实时荧光定量PCR — 维基百科", "Real-time PCR — Wikipedia"),
        ("https://en.wikipedia.org/wiki/DNA_profiling", "DNA 分型 — 维基百科", "DNA profiling — Wikipedia"),
    ],
}

def build_section(prefix, slug):
    if slug not in REFS:
        return None
    if prefix == "/en":
        lines = ["", "## References", ""]
        for url, _, en in REFS[slug]:
            lines.append(f"- [{en}]({url})")
    else:
        lines = ["", "## 参考资料", ""]
        for url, zh, _ in REFS[slug]:
            lines.append(f"- [{zh}]({url})")
    return "\n".join(lines) + "\n"

added = 0
skipped = 0
for rel_dir, prefix in [("src/content/blog", ""), ("src/content/blog-en", "/en")]:
    for f in sorted((ROOT / rel_dir).glob("*.md")):
        text = f.read_text(encoding="utf-8")
        if "## References" in text or "## 参考资料" in text:
            skipped += 1
            continue
        section = build_section(prefix, f.stem)
        if section is None:
            print(f"  [无映射] {f.stem}")
            continue
        f.write_text(text.rstrip() + "\n" + section, encoding="utf-8")
        added += 1

print(f"已添加参考资料: {added} 篇, 跳过(已有): {skipped} 篇")
