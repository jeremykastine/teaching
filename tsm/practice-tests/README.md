# TSM 098 and TSM 099 practice tests

Each of the nine unit tests and two finals has one PDF containing five fresh practice versions and their matching keys (11 PDFs, 55 versions). The course pages link to one file per assessment. PDF bookmarks jump to each version, student test, and key.

These use the current [TSM master specification](../specifications/TSM_Test_Specs.md), [shared October 30 presentation rules](../../docs/test-presentation.md), and the same layout engine as the 20-version actual-test batches. Each form has an independently random five-digit identifier, final-answer spaces in the right column, 100 points, and a vertically matched key. Unit tests have five main questions; finals have ten, including six institutional families and four coverage-balancing supplements. Practice forms are freshly parameterized rather than copied from the instructor batch.

Within each version the order is student test, a truly blank reverse when necessary, matching key, then blank padding to start the next version on a new sheet. Print US Letter, actual size, duplex, long-edge flip. No cover sheets or audit reports are added to the PDFs.

## Rebuilding

From the repository root:

```bash
python -m pip install -r scripts/practice-requirements.txt
python scripts/build_tsm_practice_bundles.py
python scripts/verify_tsm_practice_bundles.py --render
```

Use `--only 99-polynomials` (or another manifest slug) for a focused rebuild. Use `--reformat` to preserve the saved questions and version identifiers when changing layout. `scripts/tsm_practice_content.py` supplies fresh mathematical content; `scripts/algebra_test_layout.py` supplies the shared print layout. The old `generate_practice_batch.py` three-form workflow is superseded for TSM.

`manifest.json` lists the 11 published bundles. Each adjacent JSON reproduction record stores the five forms, seeds, questions, answers, geometry, and packet boundaries. `source/assessments.json` collects the 55 forms. Verification renders all nonblank pages and checks question counts, scoring, numerical/symbolic records, matching geometry, empty response areas, print margins, continuation-only footers, blank padding, version identifiers, PDF bookmarks, and all three practice indexes. Diagnostic exams are not part of the published practice-test inventory.
