#!/usr/bin/env python3
"""Fix over-length English titles/descriptions and short Chinese descriptions."""
from pathlib import Path

ROOT = Path("/home/admin/sanshibio-astro")

# (dir, slug) -> (old_title, new_title)  — title must include surrounding quotes as in file
TITLE_FIX = {
    ("blog-en", "ab-pigeon-detection"): (
        '"Racing Pigeon AB Pigeon Detection: DNA ID Against Substitution"',
        '"Racing Pigeon AB Detection: DNA ID vs Substitution"'),
    ("blog-en", "antibody-titer-test"): (
        '"Antibody Titer Testing for Racing Pigeons: Evaluating Vaccine Efficacy"',
        '"Antibody Titer Testing for Pigeons: Evaluating Vaccines"'),
    ("blog-en", "breeding-selection-guide"): (
        '"Racing Pigeon Breeding & Selection Guide: Gene Testing Meets Experience"',
        '"Pigeon Breeding & Selection: Gene Testing Meets Experience"'),
    ("blog-en", "cry1-navigation-gene"): (
        '"Racing Pigeon Navigation Gene CRY1: Cryptochrome and Magnetic Sensing"',
        '"Racing Pigeon Navigation Gene CRY1: Magnetic Sensing"'),
    ("blog-en", "f-ker-feather-gene"): (
        '"Racing Pigeon Feather Gene F-KER: Keratin and Feather Quality"',
        '"Racing Pigeon Feather Gene F-KER: Keratin Quality"'),
    ("blog-en", "feather-sampling-guide"): (
        '"Racing Pigeon Feather Sampling Guide: From Sampling to Report"',
        '"Pigeon Feather Sampling Guide: From Sample to Report"'),
    ("blog-en", "lab-equipment-guide"): (
        '"Racing Pigeon Lab Equipment Guide: Tiered Setup for Every Loft"',
        '"Pigeon Lab Equipment Guide: Tiered Setup for Every Loft"'),
    ("blog-en", "ldha-endurance-gene"): (
        '"Racing Pigeon Endurance Gene LDHA: Lactic Acid Metabolism Explained"',
        '"Racing Pigeon Endurance Gene LDHA: Lactic Acid Explained"'),
    ("blog-en", "lrp8-gsr-cask-genes"): (
        '"Racing Pigeon Memory, Weather Orientation & Intelligence Genes: LRP8, GSR, CASK"',
        '"Pigeon Memory & Orientation Genes: LRP8, GSR, CASK"'),
    ("blog-en", "newcastle-disease-control"): (
        '"Racing Pigeon Newcastle Disease: Symptoms, Spread & Control Guide"',
        '"Pigeon Newcastle Disease: Symptoms, Spread & Control"'),
    ("blog-en", "paternity-test-guide"): (
        '"Racing Pigeon Paternity Test Guide: Principles, Process & Bloodline"',
        '"Pigeon Paternity Test Guide: Principles & Bloodline"'),
    ("blog-en", "pigeon-pox-herpes-rotavirus"): (
        '"Pigeon Pox, Herpesvirus & Rotavirus: Recognizing Three Common Viruses"',
        '"Pigeon Pox, Herpesvirus & Rotavirus: Three Common Viruses"'),
    ("blog-en", "reagent-kit-overview"): (
        '"Racing Pigeon Molecular Testing Reagent Kits: The Complete Range"',
        '"Racing Pigeon Testing Reagent Kits: The Complete Range"'),
    ("blog-en", "salmonella-paratyphoid"): (
        '"Racing Pigeon Salmonella (Paratyphoid): Signs, Diagnosis & Control"',
        '"Pigeon Salmonella (Paratyphoid): Signs, Diagnosis & Control"'),
    ("blog-en", "sample-collection-guide"): (
        '"Sample Collection Guide for Racing Pigeons: Feather, Swab and Blood"',
        '"Pigeon Sample Collection Guide: Feather, Swab and Blood"'),
    ("blog-en", "speed-distance-gene"): (
        '"Speed vs Endurance Racing Pigeons: Gene-Based Breeding Strategy"',
        '"Speed vs Endurance Pigeons: Gene-Based Breeding Strategy"'),
}

DESC_FIX = {
    ("blog-en", "avian-influenza-screening"): (
        "Understand avian influenza risk in racing pigeons, clinical signs, detection methods, and how PCR and serological testing support early screening and quarantine.",
        "Understand avian influenza risk in racing pigeons, clinical signs, and how PCR and serology support early screening and quarantine."),
    ("blog-en", "cry1-navigation-gene"): (
        "Understand the CRY1 (cryptochrome) gene in racing pigeons, the circadian and geomagnetic sensing mechanisms behind navigation, and breeding for directional accuracy.",
        "Understand the CRY1 gene in racing pigeons, the geomagnetic sensing behind navigation, and breeding for directional accuracy."),
    ("blog-en", "lab-equipment-guide"): (
        "Tiered equipment lists for hobby lofts, professional lofts and testing labs, covering nucleic acid extractors, PCR cyclers, qPCR instruments and budget references.",
        "Tiered equipment lists for hobby, professional and lab setups, covering extractors, PCR cyclers, qPCR instruments and budgets."),
    ("blog-en", "lrp8-gsr-cask-genes"): (
        "Understand the LRP8 (memory), GSR (bad-weather orientation) and CASK (intelligence) genes in racing pigeons, and how cognition shapes trainability and stability.",
        "Understand the LRP8 (memory), GSR (orientation) and CASK (intelligence) genes and how cognition shapes trainability."),
    ("blog-en", "reagent-kit-overview"): (
        "A systematic overview of the reagents needed for racing pigeon molecular testing, from nucleic acid extraction to PCR amplification and rapid test cards, for a complete testing workflow.",
        "A systematic overview of racing pigeon testing reagents, from nucleic acid extraction to PCR and rapid test cards."),
    ("blog-en", "salmonella-paratyphoid"): (
        "Understand Salmonella infection (paratyphoid) in racing pigeons — symptoms, diagnosis and control — and the zoonotic risk that makes molecular detection essential.",
        "Understand Salmonella (paratyphoid) in racing pigeons, and the zoonotic risk that makes molecular detection essential."),
    ("blog", "salmonella-paratyphoid"): (
        "解析赛鸽沙门氏菌感染（副伤寒）的症状表现、诊断方法与防控措施，强调人畜共患风险与分子检测的重要性。",
        "解析赛鸽沙门氏菌感染（副伤寒）的症状表现、传播途径、诊断方法与防控措施，强调其潜伏性与人畜共患风险，说明分子检测在早期确诊中的关键作用。"),
    ("blog", "trichomonas-candida-control"): (
        "解析赛鸽毛滴虫与白色念珠菌感染的典型症状、传播途径与防治要点，重点说明嗉囊与消化道健康的日常管理。",
        "解析赛鸽毛滴虫与白色念珠菌感染的典型症状、传播途径与防治要点，重点说明嗉囊与消化道健康管理及分子检测在确诊中的价值。"),
}

fixed_t = 0
fixed_d = 0
for (dirn, slug), (old, new) in TITLE_FIX.items():
    p = ROOT / "src" / "content" / dirn / f"{slug}.md"
    text = p.read_text(encoding="utf-8")
    if old in text:
        p.write_text(text.replace(old, new), encoding="utf-8")
        fixed_t += 1
    else:
        print(f"  [title未匹配] {dirn}/{slug}")

for (dirn, slug), (old, new) in DESC_FIX.items():
    p = ROOT / "src" / "content" / dirn / f"{slug}.md"
    text = p.read_text(encoding="utf-8")
    if old in text:
        p.write_text(text.replace(old, new), encoding="utf-8")
        fixed_d += 1
    else:
        print(f"  [desc未匹配] {dirn}/{slug}")

print(f"title 修复: {fixed_t}, desc 修复: {fixed_d}")
