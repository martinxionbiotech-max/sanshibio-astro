# SanshiBio FAQ Answer Quality Audit

Date: 2026-11-24  
Scope: 85 content pages with a Markdown FAQ block; 579 visible questions.

## Results

| Metric | Result |
|---|---:|
| Pages with FAQ block | 85 |
| Visible questions | 579 |
| Answers under 60 characters (normalized) | 555 |
| Exact duplicate question text across pages | 7 groups |
| Duplicate answer text across pages | 0 |

The 60-character threshold is a screening metric, not a quality verdict. A short answer such as “Usually 1–3 working days — see testing services” can be correct and useful. The number is useful for finding pages where answers may be too terse for the question.

## Duplicate question groups

- 基因检测能预测成绩吗？ — `breeding-selection-guide`, `speed-distance-gene`
- 亲子鉴定需要父母双方都提供样本吗？ — `paternity-cost`, `paternity-test-guide`
- 幼鸽多大可以做性别鉴定？ — `pigeon-sex-identification`, `pigeon-sex-tell`
- 外观判断性别可靠吗？ — `pigeon-sex-identification`, `pigeon-sex-tell`
- 性别鉴定对育种有什么用？ — `pigeon-sex-identification`, `pigeon-sex-tell`
- 沙门氏菌在环境中能存活多久？ — `salmonella-paratyphoid`, `salmonella-prevention`
- how much earlier can i select birds with testing? — `gene-test-breeding-value-en`, `gene-test-worth-it-en`

These are not automatically harmful, but overlapping pages with the same FAQ can cannibalise each other. The preferred fix is to keep the question on the canonical page and link to it from the related page, or rewrite the secondary page's question around a distinct intent.

## Lowest average answer length (Chinese pages)

```text
sample-collection-guide.md      43.3
antibody-titer-test.md          51.2
gene-id-card-guide.md           51.8
pigeon-sex-tell.md              52.6
molting-feed.md                 53.6
vaccine-training-gap.md         54.3
chlamydia-psittaci-control.md   54.8
lab-equipment-guide.md          55.1
pigeon-introduction-tips.md     55.1
ab-pigeon-detection.md          55.2
```

## Editorial rules for the next pass

1. Answer the question in the first sentence.
2. Add one boundary (sample, method, species, timing) if it changes the answer.
3. Link to the relevant service, pillar hub or testing policy.
4. Do not pad an answer just to reach a length target.
5. Do not add a therapeutic or performance guarantee to make an answer sound stronger.

## Priority

### P1

- Resolve the 7 duplicate question groups.
- Review the five lowest-average Chinese pages above.
- Check commercial/service FAQs against the actual service policy.

### P2

- Sample 20% of the remaining short answers for correctness.
- Add source links where an answer contains a number or a comparative claim.
