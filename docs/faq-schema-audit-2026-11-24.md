# SanshiBio FAQ Schema Audit

Date: 2026-11-24  
Scope: 91 pages with FAQPage JSON-LD in the current build.

## Result

| Metric | Result |
|---|---:|
| Pages with FAQPage | 91 |
| FAQ questions in schema | 601 |
| Pages with a visible question mismatch after quote normalization | 0 |
| Duplicate questions within a page | 0 |

## Method

1. Parsed every `application/ld+json` block in `dist/**/*.html`.
2. Extracted every `FAQPage.mainEntity` question.
3. Extracted visible text from `<main>`.
4. Normalized whitespace and typographic punctuation (including curly quotes).
5. Checked whether each schema question appeared in the visible text.

## Note

A naive exact-string check initially flagged 12 English pages because the rendered HTML uses typographic quotation marks (`“ ”`) while the Markdown/schema source uses straight quotes (`" "`). This is a display typography difference, not a missing visible FAQ. After normalizing quotation marks, all 601 questions were present in visible text.

No FAQ schema was found on a page without a visible FAQ heading.

## Remaining editorial check

The audit proves visibility, not answer quality. A separate editorial review should still check:

- answers are specific to the page topic;
- no unsupported medical or performance claims;
- no duplicated boilerplate answers across unrelated pages;
- FAQ answers match current service and pricing policies.
