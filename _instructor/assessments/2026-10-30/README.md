# October 30, 2026 instructor assessment batches

25 PDFs, each containing 20 fresh versions and matching keys (500 versions total).

| Course | Unit tests | Diagnostic | Final | PDFs |
|---|---:|---:|---:|---:|
| TSM 098 | 4 | 1 | 1 | 6 |
| TSM 099 | 5 | 1 | 1 | 7 |
| MATH 101 | 4 | 1 | 1 | 6 |
| MSC 201 | 4 | 1 | 1 | 6 |

Print US Letter at actual size, duplex, **long-edge flip**. Each student test and key begins on a front side. Blank padding is intentional, including at the end of each packet. Remove instructor-key sheets before distributing student tests.

The five-digit number at the upper right of each student test matches the large centered number on its key. Key columns retain the exact vertical positions of the corresponding student pages. Statistics keys align each correct letter with the printed position of that specific option.

`manifest.json` lists the PDFs and their page counts. The adjacent JSON records preserve exact questions, choices, answers, seeds, identifiers, and geometry for reproduction. No course navigation or student resource page links to this directory. The repository is public, so these files remain accessible to anyone browsing it.

The presentation requirements are maintained in `docs/test-presentation.md` and referenced by each course's assessment specifications. Generate batches with `python scripts/export_assessment_batches.py`; use `--only ASSESSMENT` for a single set and `--reformat` to preserve the saved questions and identifiers while rebuilding layout. Validate and render with `python scripts/verify_assessment_batches.py --render`.
