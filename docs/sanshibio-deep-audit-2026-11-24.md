# SanshiBio.net — Deep Content and Site Audit

**Date:** 2026-11-24  
**Mode:** READ_ONLY for page content; audit report only  
**Repo:** `/root/.openclaw/workspace/repos/sanshibio.net`  
**HEAD:** `d67a1d3`  
**Site:** https://sanshibio.net/  
**Build:** 108 HTML pages / 107 sitemap URLs / 108 Markdown mirrors

---

## 1. Executive summary

SanshiBio has a clean technical base and a substantial bilingual article library, but it is **not yet a fully trustworthy commercial/technical site**.

The most serious content issues are:

1. **Chinese and English content are not equivalent in depth.**
   - 43 Chinese blog files average **324 words** (203–530).
   - 42 English blog files average **1,358 words** (1,117–1,668).
   - One Chinese-only article (`test-report-interpretation`) has no English counterpart.
2. **Legal/compliance pages are too thin for a service that receives samples and personal data.**
   - Chinese privacy policy: ~114 source words.
   - Chinese disclaimer: ~108 source words.
   - No terms of service and no cookie policy page.
3. **Commercial and company pages are thin.**
   - `/services/` ~100 rendered words.
   - `/about/` ~124–192.
   - `/products/` ~171–240.
   - `/paternity/` ~174–244.
4. **AIO is only partly wired.**
   - 108 Markdown mirrors exist and `/markdown/...` returns 200 `text/markdown`.
   - But `Accept: text/markdown` on normal page URLs still returns **HTML**.
   - `llms.txt` lists only **25 links**, not the full 107-page site; `llms-full.txt` is large.
5. **Chinese citation quality is weaker than English.**
   - Chinese blog external links average 3.2/page, dominated by `en.wikipedia.org` (98 links).
   - English blog external links average 6.4/page, with PMC/DOI/WOAH/CDC among the sources.
6. **FAQPage schema is used on 91/107 pages.**
   - It may be legitimate, but every page needs visible, unique Q&A content. This needs a page-by-page check.

**Overall evidence score: 73.3 / 100 — usable technical foundation, weak content parity and compliance depth.**

No P0 outage or mass duplicate-content problem was found.

---

## 2. Inventory and build

| Item | Result |
|---|---:|
| HTML files | 108 |
| Sitemap URLs | 107 |
| Markdown mirrors | 108 |
| Chinese sitemap pages | 54 |
| English sitemap pages | 53 |
| Blog files: Chinese | 43 |
| Blog files: English | 42 |
| hreflang pages | 107 |
| Noindex pages | 0 |
| Broken internal links | 0 |
| Orphan pages | 0 |
| Canonical mismatches | 0 |
| H1 errors | 0 |
| Duplicate titles | 0 |

Build command succeeded after installing dependencies. The site is a static Astro build; live sitemap and local sitemap both contain 107 URLs.

---

## 3. Content depth and language parity

### 3.1 Chinese blog

- Files: 43
- Word range: **203–530**
- Mean: **324**
- External links: average 3.2 per page
- FAQ blocks: 43/43

### 3.2 English blog

- Files: 42
- Word range: **1,117–1,668**
- Mean: **1,358**
- External links: average 6.4 per page
- FAQ blocks: 42/42

### 3.3 Parity problem

The English articles are roughly **4× longer** than the Chinese originals. That is not a translation difference; it is a content-depth difference.

Implications:

- Chinese readers get shorter articles with fewer sources.
- English readers get substantially more detail and more external citations.
- The site's stated bilingual structure is not delivering equivalent value.
- A Chinese-only article (`test-report-interpretation`) is missing from English.

**Priority:** P1 — decide whether Chinese is the primary market and English is the expanded edition, or bring both languages to the same evidence standard. Do not simply translate the short Chinese pages into short English pages.

### 3.4 Thin commercial and legal pages

Site scan reports 30 pages under 300 words; manual HTML extraction (after navigation/footer) finds 12, including:

```text
/disclaimer/          ~117
/contact/             ~118
/privacy-policy/      ~118
/services/            ~172
/about/               ~192
/                     ~239
/products/            ~240
/paternity/           ~244
/en/contact/          ~257
/virus-detection/     ~287
/blog/one-eye-cold/   ~288
```

Legal pages are not just short; they lack whole categories of information (see section 6).

---

## 4. Technical SEO

### Verified clean

| Check | Result |
|---|---:|
| Missing title/description/canonical | 0 |
| Title >60 chars | 0 |
| Description >160 chars | 0 |
| Duplicate titles | 0 |
| H1 ≠ 1 | 0 |
| Canonical mismatch | 0 |
| Broken internal links | 0 |
| Orphan pages | 0 |
| JSON-LD parse errors | 0 |
| hreflang pages | 107 |
| Sitemap / live sitemap | 107 / 107 |

### Schema inventory

```text
WebPage 109
Organization 107
WebSite 107
BreadcrumbList 103
FAQPage 91
Article 85
Product 4
HowTo 3
ItemList 2
Service 2
```

### Risks

- **FAQPage on 91/107 pages** is broad. Verify that every page has a visible, unique FAQ and that the schema Q&A matches the visible text.
- `Product` schema appears only 4 times; confirm this is intentional and does not leave product pages without structured data.
- `Organization` is repeated on every page; acceptable, but ensure `@id` consistency and contact details match the footer/contact page.
- The README still refers to `sanshibio.com`, while the live/configured domain is `sanshibio.net`.
- `www.sanshibio.net` does not resolve; only the apex domain is live. This is acceptable if intentional, but should be a conscious DNS/redirect decision.

---

## 5. AIO / Markdown

### Working

- `llms.txt`: 200
- `llms-full.txt`: 200, large full-site export
- 108 Markdown mirrors at `/markdown/...`
- Direct mirror example:
  - `/markdown/blog/gene-test-worth-it.md` → 200 `text/markdown`
  - `/markdown/en/blog/gene-test-worth-it.md` → 200 `text/markdown`
- `Content-Signal: ai-train=yes, search=yes, ai-input=yes`
- Sitemap and hreflang are present.

### Gaps

1. **No Markdown negotiation on normal page URLs.**
   `Accept: text/markdown` on `/blog/gene-test-worth-it/` returns `text/html`, not Markdown. The mirrors exist, but the negotiation layer does not route to them.
2. **`llms.txt` is not a full index.**
   It contains 25 links, while the site has 107 sitemap URLs. `llms-full.txt` is large but is not a substitute for a concise, complete discovery index.
3. **One `.md` link remains in `llms.txt`** while the rest of the site uses HTML routes; check that every link resolves.
4. **Mirrors are under `/markdown/`, not the canonical HTML URL.**
   This is a valid design, but the AIO documentation must explain the mirror convention consistently.

---

## 6. Legal and trust content

### Present

- Chinese privacy policy
- Chinese disclaimer
- English privacy policy
- English disclaimer
- Contact page

### Missing or thin

- **No Terms of Service** in either language.
- **No Cookie Policy** page.
- **Chinese privacy policy is too short** for a service that receives names, phone numbers, addresses, pigeon ring numbers and biological samples.
- The privacy page does not visibly address:
  - sample retention and destruction
  - legal basis and consent
  - cross-border transfer
  - data-subject rights procedure and response timeframe
  - children
  - security incident/breach process
  - third-party laboratories or couriers
- The disclaimer does not visibly address:
  - service limitations and re-test policy
  - sample rejection/failure
  - report interpretation boundaries
  - no guarantee of racing performance
  - intellectual-property/licensing
  - consumer rights and governing law

### Contact inconsistency

The contact page uses `martin@senobiocorp.com` while the brand/domain is `sanshibio.net`. That can be legitimate, but it needs explanation or a brand-domain email alias for trust.

---

## 7. Evidence and claims

### Chinese blog sources

- Average 3.2 external links/page.
- Dominant source: `en.wikipedia.org` (98 links across the corpus).
- Other sources: internal subdomains, MSD Veterinary Manual, NCBI, WOAH, a few journals.

### English blog sources

- Average 6.4 external links/page.
- More PMC, DOI, CDC, WOAH, PLOS, OUP, ScienceDirect and Springer links.

### Assessment

Chinese articles lean heavily on Wikipedia and internal links. That is acceptable for orientation, but not enough for claims such as:

- accuracy percentages
- paternity probability thresholds
- gene-performance associations
- disease prevalence/control claims
- “99.9%” sex identification
- “8 genes” / “58 SNP loci” technical claims

Every numeric or comparative claim needs a primary or clearly identified source block. Do not use Wikipedia as the sole support for a commercial diagnostic claim.

---

## 8. Content uniqueness

No 4-gram pair within the Chinese blog corpus or the English blog corpus reached 0.20 Jaccard.

Unique-sentence share:

```text
Chinese blog: 1.00 mean / 1.00 min
English blog: 1.00 mean / 1.00 min
```

This means there is no detectable body-copy duplication inside each language. Cross-language translation similarity was not scored.

---

## 9. Priority fixes

### P1

1. **Bring Chinese and English content to the same evidence standard.**
   - Chinese blog: expand from ~324 to at least the depth of the English version, or explicitly mark Chinese as a summary edition.
2. **Add Terms of Service and Cookie Policy** in Chinese and English.
3. **Expand privacy policy and disclaimer** to cover samples, retention, laboratories, cross-border transfer, rights, service limitations and re-test policy.
4. **Expand commercial pages**:
   - `/services/`
   - `/products/`
   - `/paternity/`
   - `/about/`
5. **Fix Markdown negotiation** or document that only `/markdown/` mirrors are supported.
6. **Make `llms.txt` a complete or clearly scoped index.**
7. **Audit FAQPage schema** against visible FAQs.

### P2

8. Add the missing English counterpart for `test-report-interpretation`.
9. Add primary-source citations to Chinese articles; reduce Wikipedia-only support.
10. Fix README domain (`sanshibio.com` vs `sanshibio.net`).
11. Decide whether `www.sanshibio.net` should resolve/redirect.
12. Clarify the `senobiocorp.com` email relationship.

---

## 10. Seven-dimension score

| Dimension | Weight | Score | Main reason |
|---|---:|---:|---|
| Completeness | 15% | 65 | Bilingual structure exists, but thin commercial/legal pages and one missing translation |
| SEO | 20% | 85 | Metadata, canonical, hreflang and sitemap are clean; FAQ schema breadth needs review |
| AIO | 15% | 65 | Mirrors and llms-full exist; negotiation and llms index incomplete |
| Data consistency | 10% | 75 | Schema and hreflang coherent; language parity and legal coverage uneven |
| Originality | 25% | 80 | No internal duplicate; external originality not fully measured |
| Subjective insight | 10% | 65 | Direct answers exist, but Chinese pages are thin and source quality uneven |
| Content depth | 5% | 55 | Chinese blog 203–530 words; legal/commercial pages very thin |
| **Weighted total** | | **73.3** | **Usable foundation; not yet a trust-complete commercial site** |

This is an evidence score, not a Google ranking prediction.

---

## 11. Limitations

- No GSC, analytics, rankings or traffic data.
- No external source corpus for a full originality comparison.
- No page-by-page human review of all 85 articles.
- No legal review; only public-page compliance signals.
- No sample/COA/laboratory validation.
- No Core Web Vitals/Lighthouse measurement.

---

## 12. Verdict

SanshiBio is technically clean and internally non-duplicative. The problems are **content parity, trust depth and AIO wiring**, not crawlability.

The next release should not be another batch of articles. It should be:

```text
Chinese/English parity
→ legal/commercial pages
→ source quality
→ Markdown negotiation and llms index
→ FAQ/schema verification
```
