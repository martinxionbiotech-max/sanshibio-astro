#!/usr/bin/env python3
"""AIO enhancement for English gene + virus articles: TLDR + Entity Glossary + Key Takeaways + FAQ."""
from pathlib import Path

ROOT = Path("/home/admin/sanshibio-astro/src/content/blog-en")

GENE_TABLE = """| Gene | Full Name | Detection Meaning |
|------|-----------|-------------------|
| LDHA | Lactate Dehydrogenase A | Endurance (lactic acid metabolism) |
| DRD4 | Dopamine Receptor D4 | Homing persistence |
| CRY1 | Cryptochrome 1 | Navigation |
| MSTN | Myostatin | Muscle power |
| F-KER | Feather Keratin | Feather quality |
| LRP8 | LDL Receptor Related Protein 8 | Learning & memory |
| GSR | Glutathione Reductase | Bad-weather orientation |
| CASK | Calcium/Calmodulin-Dependent Serine Protein Kinase | Cognition |

*Full 8-gene flight-ability panel is available via [flight ability gene testing](/en/flight-ability/).*"""

PATHOGEN_TABLE = """| Pathogen | Name | Classification |
|----------|------|----------------|
| NDV | Newcastle Disease Virus | Paramyxoviridae |
| AIV | Avian Influenza Virus | Orthomyxoviridae |
| PiCV | Pigeon Circovirus | Circoviridae |
| PHV | Pigeon Herpesvirus | Herpesviridae |
| — | Pigeon Adenovirus | Adenoviridae |
| — | Pigeon Pox Virus | Poxviridae |
| C. psittaci | Chlamydia psittaci | Chlamydiaceae |
| Salmonella | Salmonella | Enterobacteriaceae |
| Mycoplasma | Mycoplasma | Mycoplasmataceae |
| T. gallinae | Trichomonas gallinae | Trichomonadidae |
| C. albicans | Candida albicans | Saccharomycetaceae |"""

ENH = {
    # 基因文章
    "ldha-endurance-gene": {
        "tldr": "The LDHA gene encodes lactate dehydrogenase A — the core endurance marker for long-distance racing pigeons. This guide explains lactic-acid metabolism, how LDHA genotype drives endurance, and how to breed for it.",
        "takeaways": [
            "LDHA is the core endurance marker — it determines lactic-acid clearance and sustained energy supply.",
            "Lactic-acid buildup causes fatigue — high LDHA activity means faster clearance and better stamina.",
            "Prioritize for long races — 500 km+ endurance races favor strong LDHA genotypes.",
            "Squabs can be tested — feather DNA testing enables early endurance screening.",
            "Genes + training work together — genes set the ceiling, training delivers the performance.",
        ],
        "new_faqs": [
            ("Can LDHA genotype be changed?", "No. Genotype is inherited, but progressive endurance training can amplify the expression of favorable genes."),
            ("What is the difference between LDHA and MSTN?", "LDHA drives endurance (lactic-acid metabolism); MSTN drives muscle power (explosiveness). See the [speed vs endurance guide](/en/blog/speed-distance-gene/)."),
        ],
    },
    "drd4-homing-gene": {
        "tldr": "The DRD4 gene encodes the dopamine D4 receptor — the key driver of homing persistence and behavioral stability in racing pigeons.",
        "takeaways": [
            "DRD4 drives homing persistence — it shapes focus, tenacity and the explore-return tendency.",
            "Dopamine signaling underlies motivation — DRD4 genotype affects homing drive.",
            "Stability wins repeated races — persistent homers perform more consistently.",
            "Squabs can be screened — feather testing reveals homing potential early.",
            "Pair with navigation genes — homing drive works with navigation ability.",
        ],
        "new_faqs": [
            ("Can DRD4 predict homing rate?", "It estimates homing tendency, not an exact rate. Weather, distance and training also matter."),
            ("How does DRD4 differ from CRY1?", "DRD4 is the motivation to return; CRY1 is the ability to navigate. Both drive long-distance homing."),
        ],
    },
    "cry1-navigation-gene": {
        "tldr": "The CRY1 gene encodes cryptochrome — the candidate molecule behind magnetic sensing and navigation in racing pigeons.",
        "takeaways": [
            "CRY1 is the navigation compass — cryptochrome participates in magnetic sensing and circadian rhythm.",
            "Magnetoreception mechanism — the radical-pair hypothesis places CRY1 at the core of light-dependent sensing.",
            "Long-distance accuracy — strong CRY1 genotypes correlate with directional precision.",
            "Squabs can be tested — feather DNA reveals navigation potential early.",
            "Works with homing genes — finding the way + wanting to return.",
        ],
        "new_faqs": [
            ("Can pigeons really sense Earth's magnetic field?", "Yes — research strongly supports magnetoreception, with cryptochrome CRY1 as the leading candidate molecule."),
            ("Does CRY1 work in bad weather?", "CRY1 is light-dependent, so dim light may weaken it. Bad-weather orientation also involves the GSR gene."),
        ],
    },
    "mstn-muscle-gene": {
        "tldr": "The MSTN gene encodes myostatin — the negative regulator of muscle growth that underpins muscle power and sprint speed in racing pigeons.",
        "takeaways": [
            "MSTN is the power marker — myostatin negatively regulates muscle growth.",
            "Genotype drives explosiveness — weaker myostatin means more muscle and power.",
            "Prioritize for sprint races — 200-400 km races favor strong MSTN genotypes.",
            "Squabs can be screened — feather testing reveals muscle potential early.",
            "Distinct from endurance — MSTN powers sprints, LDHA sustains distance.",
        ],
        "new_faqs": [
            ("Is MSTN genotype linked to muscle mass?", "Yes. Some genotypes reduce myostatin inhibition, yielding more developed muscle and greater explosive power."),
            ("Can MSTN and LDHA both be optimized?", "They are independent loci and can be tested together. Speed and endurance involve some trade-off — see the [speed vs endurance guide](/en/blog/speed-distance-gene/)."),
        ],
    },
    "f-ker-feather-gene": {
        "tldr": "The F-KER gene encodes feather keratin — the structural basis of feather quality and aerodynamic performance in racing pigeons.",
        "takeaways": [
            "F-KER drives feather quality — feather keratin shapes strength, elasticity and water resistance.",
            "Quality feathers fly efficiently — feather structure directly affects aerodynamics.",
            "Relevant to sprint breeding — wing structure influences speed.",
            "Squabs can be tested — feather DNA reveals feather potential early.",
            "Pairs with muscle genes — feather + muscle determine speed.",
        ],
        "new_faqs": [
            ("How does F-KER affect flight?", "Feather keratin determines feather strength, elasticity and waterproofing, which shape aerodynamic efficiency and speed."),
            ("Can feather quality be improved?", "Nutrition and management improve feather health, but the genetic baseline comes from genes like F-KER."),
        ],
    },
    "lrp8-gsr-cask-genes": {
        "tldr": "LRP8, GSR and CASK govern learning & memory, bad-weather orientation and cognition respectively — the genetic basis of a trainable, 'smart' racing pigeon.",
        "takeaways": [
            "LRP8 drives learning & memory — synaptic plasticity and route memory.",
            "GSR drives bad-weather orientation — antioxidant defense under harsh conditions.",
            "CASK drives cognition — neuronal development and synaptic signaling.",
            "Trainability is a hidden edge — smart pigeons learn faster and memorize routes.",
            "Three genes work together — cognition is polygenic.",
        ],
        "new_faqs": [
            ("Can these genes measure 'IQ'?", "They assess cognition-related genetic potential, not a human-style IQ score, reflecting trainability."),
            ("Why is GSR linked to bad weather?", "GSR encodes glutathione reductase for antioxidant defense; harsh weather raises oxidative stress, so GSR activity affects orientation."),
        ],
    },
    "speed-distance-gene": {
        "tldr": "Speed-type and endurance-type racing pigeons follow two distinct physiological routes with different gene combinations. This guide helps you pair breeders by race distance.",
        "takeaways": [
            "Two physiological routes — anaerobic sprint vs aerobic endurance.",
            "Sprints favor MSTN + F-KER — explosive power and feather structure.",
            "Long races favor LDHA + CRY1 + DRD4 — endurance, navigation and homing.",
            "Middle races need balance — a balanced speed-endurance gene mix.",
            "Build a gene profile first — then pair by race distance.",
        ],
        "new_faqs": [
            ("How do I know if my pigeon is speed or endurance type?", "Test key genes (MSTN, LDHA) and combine with bloodline and race records for an objective genetic basis."),
            ("Can I breed a balanced speed-endurance pigeon?", "Yes, through gene-based pairing, but there is a physiological trade-off; middle-distance (400-700 km) suits balanced types best."),
        ],
    },
    "gene-id-card-guide": {
        "tldr": "A racing pigeon gene ID card uses 58 SNP loci to give every pigeon a unique, traceable genetic identity — unforgeable and irreplaceable.",
        "takeaways": [
            "58 SNP loci form a genetic fingerprint — each pigeon's identity is nearly unique.",
            "Unforgeable — genetic identity based on DNA far exceeds physical leg rings.",
            "Four core values — uniqueness, anti-cheating, bloodline management, trade credentials.",
            "Complements AB-pigeon testing — one builds identity, the other verifies it.",
            "Archive the whole loft — every breeder and racer should be profiled.",
        ],
        "new_faqs": [
            ("What is the difference between a gene ID and a paternity test?", "A gene ID establishes individual identity; a paternity test verifies parentage. Use both for full bloodline management."),
            ("Why can SNP loci uniquely identify an individual?", "The combination of 58 SNP loci is astronomically large, making identical matches between two pigeons virtually impossible."),
        ],
    },
    # 病毒文章
    "newcastle-disease-control": {
        "tldr": "Newcastle disease is among the most severe viral diseases in racing pigeons — highly contagious and often fatal. This guide covers virology, symptoms, spread and control, emphasizing early PCR detection.",
        "takeaways": [
            "Caused by a paramyxovirus — highly contagious and highly lethal.",
            "Three symptom clusters — respiratory, digestive and neurological signs.",
            "Early detection is critical — qPCR detects the pathogen before symptoms appear.",
            "Control = vaccination + biosecurity — standard immunization, pre-race screening, quarantine.",
            "No specific cure — prevention first; isolate early to limit losses.",
        ],
        "new_faqs": [
            ("How does Newcastle disease differ from avian influenza?", "Different virus families (paramyxovirus vs orthomyxovirus) with overlapping symptoms but different control. Testing distinguishes them."),
            ("Can vaccinated pigeons still be infected?", "Yes — protection is not 100%. Check [antibody titer testing](/en/blog/antibody-titer-test/) and boost when titers drop."),
        ],
    },
    "avian-influenza-screening": {
        "tldr": "Racing pigeons are mostly silent carriers of avian influenza — low morbidity but a real transmission risk. This guide covers risk, symptoms and detection for quarantine.",
        "takeaways": [
            "Mostly silent infections — signs are mild, but pigeons can carry and spread the virus.",
            "Transmission-vector risk — releases and cross-region transport increase contact with wild birds.",
            "Three detection tools — PCR for nucleic acid, rapid cards for antigen, serology for antibody.",
            "Three screening scenarios — event quarantine, new-bird isolation, outbreak investigation.",
            "A notifiable disease — handle suspected positives per veterinary authority rules.",
        ],
        "new_faqs": [
            ("Can pigeons get highly pathogenic avian influenza?", "They are relatively tolerant and mostly carry low-pathogenic strains, but their vector role still warrants routine testing."),
            ("Which sample for AI screening?", "Combine oral and cloacal swabs to raise detection rate — see the [sampling guide](/en/blog/sample-collection-guide/)."),
        ],
    },
    "mycoplasma-detection": {
        "tldr": "Mycoplasmosis (chronic respiratory disease) is the most common hidden respiratory infection in racing pigeons — persistent and recurrent. This guide covers its impact, symptoms and detection, emphasizing breeder purification.",
        "takeaways": [
            "A silent performance killer — atypical symptoms, yet steadily reduces endurance.",
            "Frequent mixed infections — often with Newcastle disease, adenovirus and chlamydia.",
            "Breeder purification is key — vertical transmission requires a negative core flock.",
            "PCR + treatment + re-test — a detection-treatment-clearance loop.",
            "Avoid blind medication — test first to identify the cause and prevent resistance.",
        ],
        "new_faqs": [
            ("Can CRD be cured?", "Proper medication plus breeder purification can control or eliminate mycoplasma, but persistence requires ongoing biosecurity."),
            ("Which sample for mycoplasma?", "Use flocked swabs for throat or nasal secretions — higher release rate than cotton."),
        ],
    },
    "chlamydia-psittaci-control": {
        "tldr": "Chlamydia psittaci is a common zoonotic pathogen in racing pigeons — it harms flock health and can infect humans. This guide covers symptoms, transmission and control, emphasizing molecular detection and personal protection.",
        "takeaways": [
            "A zoonotic pathogen — can infect humans; wear protection when handling sick birds.",
            "Silent infections are common — lab testing is needed for diagnosis.",
            "PCR is the gold standard — chlamydia is hard to culture, molecular detection is most reliable.",
            "Antibiotics can control it — under veterinary guidance.",
            "Personal protection matters — wear masks and gloves when cleaning lofts.",
        ],
        "new_faqs": [
            ("Can psittacosis infect humans?", "Yes — Chlamydia psittaci is zoonotic. Wear protective gear and practice hand hygiene when handling birds or cleaning lofts."),
            ("How is chlamydia detected?", "qPCR is the gold standard, detecting chlamydial nucleic acid directly from swabs."),
        ],
    },
    "salmonella-paratyphoid": {
        "tldr": "Salmonella (paratyphoid) is a common bacterial disease in racing pigeons with zoonotic risk. This guide covers symptoms, transmission and control, emphasizing molecular detection for early diagnosis.",
        "takeaways": [
            "A zoonotic pathogen — practice hygiene when handling sick birds.",
            "Vertical transmission risk — infected breeders can pass it via eggs.",
            "Diverse symptoms — digestive, joint and neurological signs.",
            "PCR enables early diagnosis — faster and more sensitive than culture.",
            "Breeder purification + disinfection — control it at the source.",
        ],
        "new_faqs": [
            ("Can Salmonella infection be cured?", "Proper antibiotics can control it, but follow the full course and do sensitivity testing to avoid resistance."),
            ("Which sample for Salmonella?", "Cloacal swabs or feces; tissue samples may be used for joint or neurological signs."),
        ],
    },
    "pigeon-circovirus-adenovirus": {
        "tldr": "Pigeon circovirus and adenovirus are common immunosuppressive pathogens in racing pigeons, often mixed infections that worsen disease. This guide covers their features, harm and detection.",
        "takeaways": [
            "Circovirus weakens immunity — causing immunosuppression and secondary infections.",
            "Adenovirus hits multiple organs — liver, digestive and respiratory systems.",
            "Mixed infections are common — often with Newcastle disease, complicating diagnosis.",
            "PCR enables differential diagnosis — identify the exact pathogen.",
            "Boost overall immunity — vaccination + nutrition are the foundation.",
        ],
        "new_faqs": [
            ("What harm does circovirus cause?", "It primarily attacks the immune system, causing immunosuppression and predisposing birds to secondary infections."),
            ("Can both viruses be tested together?", "Yes — multiplex PCR can detect multiple pathogens in one run to identify mixed infections."),
        ],
    },
    "pigeon-pox-herpes-rotavirus": {
        "tldr": "Pigeon pox, herpesvirus and rotavirus are three common viral pathogens with distinct yet confusable symptoms. This guide covers identification, harm and control.",
        "takeaways": [
            "Pox shows skin and mucosal lesions — mosquitoes are key vectors.",
            "Herpesvirus hits multiple systems — respiratory, digestive and neurological.",
            "Rotavirus mainly causes diarrhea — especially in squabs and young birds.",
            "Three pathogens are confusable — PCR differential diagnosis is essential.",
            "Mosquito control + isolation + disinfection — comprehensive prevention.",
        ],
        "new_faqs": [
            ("How does pigeon pox spread?", "Mainly via mosquito bites, and through broken skin or mucosa. Peaks in mosquito season — control insects and hygiene."),
            ("Which stage does rotavirus harm most?", "Squabs and young birds are most susceptible, showing diarrhea; adults are often silent or mild."),
        ],
    },
    "trichomonas-candida-control": {
        "tldr": "Trichomonas gallinae and Candida albicans are the two most common pathogens of the crop and digestive tract in racing pigeons, often mixed and persistent. This guide covers symptoms, spread and control.",
        "takeaways": [
            "Trichomonas causes 'canker' — attacking the mouth and crop in all ages.",
            "Candida is opportunistic — often secondary to immune weakness or antibiotic overuse.",
            "Mixed infections are common — differential diagnosis is needed.",
            "Proper medication + management — avoid antibiotic overuse that triggers Candida.",
            "Crop health is the foundation — clean water and fresh feed matter.",
        ],
        "new_faqs": [
            ("How to distinguish trichomonas from candida?", "Trichomonas is a protozoan, Candida is a fungus — different pathogens, different drugs. Confirm by microscopy or PCR."),
            ("Does antibiotic overuse cause candida?", "Yes — overuse disrupts the normal flora, promoting opportunistic fungal overgrowth. Only medicate after confirmed diagnosis."),
        ],
    },
    "antibody-titer-test": {
        "tldr": "Antibody titer testing answers with data whether vaccination actually worked. This guide covers the principle, methods and result interpretation for precise flock immunization.",
        "takeaways": [
            "Evaluate vaccine efficacy — use antibody titer data to confirm the vaccine worked.",
            "Two methods — hemagglutination inhibition (HI) and ELISA, both expressed as titers.",
            "Tiered interpretation — high/moderate/low map to different actions.",
            "Three scenarios — efficacy evaluation, booster timing, diagnostic aid.",
            "Complements PCR — PCR detects disease, antibody reflects immunity.",
        ],
        "new_faqs": [
            ("How does antibody testing differ from pathogen testing?", "Antibody reflects immune status (vaccinated/infected); PCR detects current infection. Use both for precise prevention."),
            ("When should I test after vaccination?", "Antibodies peak 2-4 weeks post-vaccination — test then for the truest response."),
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

    # 新 FAQ 插到 References 前
    if "## References" in body and cfg["new_faqs"]:
        body = body.replace("## References", build_faqs(cfg["new_faqs"]) + "\n\n## References", 1)
    elif cfg["new_faqs"]:
        body = body.rstrip() + "\n\n" + build_faqs(cfg["new_faqs"]) + "\n"

    # Takeaways + 实体表
    if "gene" in slug or slug in ("speed-distance-gene", "gene-id-card-guide", "ldha-endurance-gene", "drd4-homing-gene", "cry1-navigation-gene", "mstn-muscle-gene", "f-ker-feather-gene", "lrp8-gsr-cask-genes"):
        table = GENE_TABLE
    else:
        table = PATHOGEN_TABLE
    tail = build_takeaways(cfg["takeaways"]) + "\n\n## Entity Quick Reference\n\n" + table
    if "## References" in body:
        body = body.replace("## References", tail + "\n\n## References", 1)
    else:
        body = body.rstrip() + "\n\n" + tail + "\n"

    p.write_text(body, encoding="utf-8")
    print(f"✅ {slug}")

print("完成英文基因+病毒文章 AIO 增强")
