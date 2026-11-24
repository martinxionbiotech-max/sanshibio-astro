---
title: "58 SNPs and Paternity Probability: Limits of a Panel"
description: "What a 58-SNP pigeon paternity panel can and cannot prove: PI, CPI, exclusion vs support, sample quality and why different panels are not directly comparable."
pubDate: 2026-11-24
category: "Bloodline"
tags: [SNP, paternity testing, CPI, parentage probability, bloodline]
author: "Sanshi Bio Molecular Diagnostics Team"
---

**Short answer:** A paternity test is not a binary “guilty or innocent” verdict. It either excludes parentage or supports it at a probability. A 58-SNP panel can provide strong identification, but the number depends on the markers, population frequencies, sample quality and the laboratory’s calculation. Do not compare percentages from different panels as if they were the same test.

## 1. Two different conclusions

A paternity report usually contains one of two conclusions:

1. **Exclusion** — multiple markers are inconsistent with inheritance.
2. **Support** — the cumulative probability of parentage meets the laboratory’s threshold.

They do not have the same logical strength:

- **Exclusion is categorical.** If the marker set does not fit, the claimed parentage is excluded.
- **Support is probabilistic.** It means the evidence is very strong, not that the relationship is mathematically 100% certain.

Reading “supports parentage” as “absolute proof” is the most common overreach in report interpretation.

## 2. The reasoning: PI, CPI and probability

A single-marker **paternity index (PI)** can be understood as:

```text
PI = probability of the genotype if the tested male is the father
     ÷ probability of the genotype in an unrelated random male
```

Multiply the independent marker PIs to get the **cumulative paternity index (CPI)**:

```text
CPI = PI₁ × PI₂ × … × PIₙ
```

Under a simplified two-hypothesis model:

```text
P = CPI / (CPI + 1)
```

That gives:

| CPI | Approximate probability |
|---:|---:|
| 100 | 99.0% |
| 1,000 | 99.90% |
| 10,000 | 99.99% |

So “99.99%” is not a number that can be detached from the formula and the laboratory’s assumptions. Different labs may use different priors, marker sets and software. The report’s own method controls.

## 3. What 58 SNPs actually mean

The number of SNPs is not the only measure of power. What matters is:

- how polymorphic the markers are in the target population
- whether the markers are independent
- the allele frequencies in that population
- genotyping quality and error rate
- mutations, null alleles and sample contamination
- whether the sample is traceable to the bird

Therefore:

```text
58 SNPs ≠ every laboratory’s 58 SNPs are equivalent
```

The same percentage can mean different things under different panels, populations and calculations.

## 4. What follows for reading the report

| Report content | What it can support | What it cannot support |
|---|---|---|
| Multiple markers inconsistent | Exclusion of parentage | Proving another bird is the father |
| CPI above the laboratory threshold | Support for parentage | Mathematical 100% certainty |
| One inconsistent marker | A need to review | A conclusion from one marker alone |
| Percentages from different labs | Separate interpretation | Direct ranking of “higher” or “lower” |
| Sample ID not linked to the bird | No attribution | Use in trade or registration |

A practical sequence:

1. Verify sample ID, ring number, collection date and sample type.
2. Check the panel size, marker set and threshold used by the laboratory.
3. Read whether the report says “excluded” or “supported” — not just the percentage.
4. For trade or auction use, retain the sample chain and raw records.

## 5. Editorial take

I prefer to treat a paternity report as an **evidence document**, not a **pedigree certificate**.

- It can provide strong support or a clear exclusion when the sample, panel and calculation are sound.
- It cannot replace a pedigree, transaction due diligence or loft records.
- For a buyer, the important question is not only “does it say 99.99%?” but: **who collected the sample, how did it reach the lab, what panel was used, and can the result be reviewed?**

A “99.99%” on a sheet with no sample chain, no marker information and no laboratory identity is not the same evidence as a traceable report.

## 6. Boundaries

This explains the general logic of paternity indices. It is not legal, transactional or veterinary advice. Laboratories may use different algorithms and thresholds. For a high-value transaction, use traceable samples, confirm the panel and keep a route for independent review.

## Sources

- International Society for Forensic Genetics: https://www.isfg.org/
- Paternity Index: https://en.wikipedia.org/wiki/Paternity_Index
- NIST STRBase: https://strbase.nist.gov/
- Sanshi Bio paternity service: /en/paternity/
