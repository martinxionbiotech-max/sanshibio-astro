#!/usr/bin/env python3
"""AIO enhancement for 9 English service articles."""
from pathlib import Path

ROOT = Path("/home/admin/sanshibio-astro/src/content/blog-en")

ENH = {
    "reagent-kit-overview": {
        "tldr": "Reagents are the invisible pipeline of molecular testing — they decide result reliability. This guide covers the four reagent categories for a complete pigeon testing workflow.",
        "takeaways": [
            "Four workflow steps — sample processing, extraction, amplification and result reading, each with dedicated reagents.",
            "Magnetic-bead extraction is the mainstream — high purity, automatable, no toxic reagents.",
            "Ready-to-use PCR master mixes — less manual error, more stability.",
            "Rapid test cards suit loft screening — confirm positives in the lab.",
            "Cold-chain storage is key — keep at -20°C, avoid repeated freeze-thaw.",
        ],
        "new_faqs": [
            ("Must reagents match the instrument?", "Preferably yes. Paired reagents guarantee compatibility and stable results. Confirm the instrument model before buying."),
            ("Can reagents be shipped at room temperature?", "Extraction and PCR reagents need cold-chain transport; rapid cards ship at room temperature. Store per the label on arrival."),
        ],
    },
    "lab-equipment-guide": {
        "tldr": "A pigeon testing lab should be sized to your needs, not to the priciest gear. This guide gives three tiered setups with budget references for rational purchasing.",
        "takeaways": [
            "Three tiers — entry (¥5k-10k), professional (¥30k-80k), laboratory (¥150k+).",
            "Eight core equipment types — extractor, PCR cycler, qPCR, centrifuge, gel electrophoresis, etc.",
            "Match throughput — choose 8/16/96 channels by sample volume.",
            "Contamination control is the lifeline — three-zone separation + UV sterilization.",
            "Prefer local after-sales — domestic equipment means faster spare-part supply.",
        ],
        "new_faqs": [
            ("Do I need a PCR cycler at entry level?", "No. Entry level focuses on proper sampling and mail-in testing, leaving core testing to the lab."),
            ("qPCR vs conventional PCR?", "For SNP genotyping, conventional PCR + electrophoresis suffices; for pathogen quantification (viral load), qPCR is required."),
        ],
    },
    "qpcr-principle": {
        "tldr": "Real-time qPCR is the gold standard for pigeon pathogen detection, delivering both qualitative and quantitative results. This guide covers the principle, Ct value and applications.",
        "takeaways": [
            "qPCR vs conventional PCR — real-time fluorescence, closed-tube, quantifiable.",
            "Two fluorescent systems — SYBR Green (low cost) and TaqMan probes (high specificity).",
            "Ct value is the core — lower Ct means higher viral load (~3.3 cycles ≈ 10×).",
            "Four applications — screening, load assessment, treatment monitoring, mixed-infection detection.",
            "Gray zone needs re-testing — Ct 35-40 warrants a 3-5 day re-test.",
        ],
        "new_faqs": [
            ("Is a Ct of 37 positive or negative?", "It falls in the gray zone (35-40), suggesting low load or sampling error — re-test in 3-5 days."),
            ("How many pathogens can qPCR detect at once?", "Multiplex qPCR detects 2-6 pathogens simultaneously via different fluorescent channels."),
        ],
        "extra_table": """## Molecular Testing Terminology

| Term | Meaning |
|------|---------|
| qPCR | Real-time quantitative PCR |
| Ct value | Cycle threshold; lower = higher load |
| Primer | Short nucleic acid that initiates amplification |
| Probe | Fluorescently labeled detection sequence |
| Multiplex PCR | Detects multiple pathogens in one run |""",
    },
    "feather-sampling-guide": {
        "tldr": "Feather sampling is the easiest and most common way to collect pigeon DNA. This guide covers proper technique, storage and common mistakes.",
        "takeaways": [
            "The pulp is the DNA bank — pluck feathers with the root pulp intact.",
            "Take 3-5 feathers — wing or tail feathers, avoid breakage.",
            "Avoid the molting period — feather quality drops, affecting extraction.",
            "Room temperature is fine — label each sample clearly.",
            "Ship within 48 hours — prompt submission preserves DNA quality.",
        ],
        "new_faqs": [
            ("Is one feather enough?", "A single feather with intact pulp usually works, but 3-5 are recommended in case of missing pulp or contamination."),
            ("Can down feathers be used?", "Squabs can use down, but the pulp is essential — pure feather shafts lack enough DNA."),
        ],
    },
    "sample-collection-guide": {
        "tldr": "Half of a reliable result depends on proper sampling. This guide covers feather, swab and blood collection with storage and shipping tips.",
        "takeaways": [
            "Three sample types — feather for genes, swab for pathogens, blood for antibodies.",
            "Feather pulp is essential — the DNA source for gene testing.",
            "Flocked swabs beat cotton tips — higher release, better accuracy.",
            "Refrigerate swabs and blood — 2-8°C, ship within 48 hours.",
            "Label clearly — mark each sample with bird ID and test item.",
        ],
        "new_faqs": [
            ("Do I need to fast the pigeon before sampling?", "No fasting needed for feather (gene) testing; for pathogen testing, sample before medication to avoid interference."),
            ("Can I pool multiple birds into one sample?", "No. Each sample must be labeled and tested individually — pooling makes results impossible to attribute."),
        ],
    },
    "paternity-test-guide": {
        "tldr": "Pigeon paternity testing uses DNA parentage analysis to confirm bloodlines scientifically — the core tool for pedigree certification and breeding management.",
        "takeaways": [
            "Parentage via SNP comparison — determines parent-offspring relationships.",
            "Three applications — pedigree certification, breeding management, race eligibility.",
            "High accuracy — molecular parentage determination is highly reliable.",
            "Feather testing — no blood needed, squabs can be tested.",
            "Complements gene ID cards — profile + parentage for full bloodline management.",
        ],
        "new_faqs": [
            ("How accurate is paternity testing?", "SNP-based parentage analysis can exclude non-parents with over 99.9% accuracy."),
            ("Do I need both parents' samples?", "Ideally provide suspected parents and offspring — more samples mean more accurate determination."),
        ],
    },
    "ab-pigeon-detection": {
        "tldr": "AB pigeons (substituted birds) are a cheating tactic in pigeon racing. This guide covers how DNA comparison identifies substitution and safeguards fair competition.",
        "takeaways": [
            "AB pigeon is substitution fraud — replacing the racing bird with a same-name, same-ring double.",
            "DNA comparison catches it — genetic identity cannot be forged.",
            "Pre-race identity verification — sample before basketing, compare after the race.",
            "Works with gene ID cards — one builds identity, the other verifies it.",
            "Protects race fairness — eliminates 'look-alike' substitution.",
        ],
        "new_faqs": [
            ("How is AB-pigeon testing done?", "Sample and profile racers pre-race, then re-sample winners post-race — a genotype mismatch indicates substitution."),
            ("Can leg rings prevent AB pigeons?", "Rings can be swapped or duplicated. Genetic identity based on DNA is unforgeable and far more reliable."),
        ],
    },
    "pigeon-sex-identification": {
        "tldr": "DNA sexing accurately determines squab gender, solving the problem of visually indistinguishable sexes. This guide covers the principle and applications.",
        "takeaways": [
            "Squabs are hard to sex visually — DNA sexing is accurate and reliable.",
            "Based on sex-chromosome genes — the avian ZW sex-determination system.",
            "Feather testing — no blood needed, test squabs early.",
            "Three applications — breeding pairs, race classification, flock management.",
            "Near-100% accuracy — molecular sexing vastly outperforms visual judgment.",
        ],
        "new_faqs": [
            ("How accurate is DNA sexing?", "Molecular detection of sex-chromosome genes (e.g., CHD1) reaches near-100% accuracy, far exceeding visual judgment."),
            ("At what age can pigeons be sexed?", "From hatching onward. Feather or blood DNA enables accurate early sexing."),
        ],
    },
    "breeding-selection-guide": {
        "tldr": "Scientific selection is the core of performance improvement. This guide covers how gene testing combines with traditional selection for data-driven breeding.",
        "takeaways": [
            "Gene testing provides a genetic basis — objectively assessing flight potential.",
            "Genotype + race record — evaluate potential and performance together.",
            "Pair by race distance — optimize speed and endurance gene combinations.",
            "Build a gene archive — track offspring performance over time.",
            "Avoid gene-only thinking — bloodline, fitness and training matter equally.",
        ],
        "new_faqs": [
            ("Can gene testing predict results?", "It cannot predict rankings, but it assesses genetic potential, guiding pairing and training to avoid blind breeding."),
            ("Does gene selection conflict with traditional selection?", "No — it is a data supplement to traditional bloodline selection, sharpening the identification of superior breeders."),
        ],
    },
}

def insert_after_h1(body, block):
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("# "):
            insert_at = i + 1
            while insert_at < len(lines) and lines[insert_at].strip() == "":
                insert_at += 1
            lines.insert(insert_at, block + "\n")
            return "\n".join(lines)
    return body

def build_takeaways(items):
    return "## Key Takeaways\n\n" + "\n".join(f"{i}. {t}" for i, t in enumerate(items, 1))

def build_faqs(faqs):
    return "\n\n".join(f"### {q}\n{a}" for q, a in faqs)

for slug, cfg in ENH.items():
    p = ROOT / f"{slug}.md"
    if not p.exists():
        print(f"⚠️ 跳过(不存在) {slug}")
        continue
    body = p.read_text(encoding="utf-8")

    tldr_block = f"> **TL;DR**: {cfg['tldr']}"
    if "TL;DR" not in body:
        body = insert_after_h1(body, tldr_block)

    if "## References" in body and cfg["new_faqs"]:
        body = body.replace("## References", build_faqs(cfg["new_faqs"]) + "\n\n## References", 1)
    elif cfg["new_faqs"]:
        body = body.rstrip() + "\n\n" + build_faqs(cfg["new_faqs"]) + "\n"

    tail = build_takeaways(cfg["takeaways"])
    if cfg.get("extra_table"):
        tail += "\n\n" + cfg["extra_table"]
    if "## References" in body:
        body = body.replace("## References", tail + "\n\n## References", 1)
    else:
        body = body.rstrip() + "\n\n" + tail + "\n"

    p.write_text(body, encoding="utf-8")
    print(f"✅ {slug}")

print("完成英文服务文章 AIO 增强")
