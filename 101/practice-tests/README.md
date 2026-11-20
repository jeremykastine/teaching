# MATH 101 practice tests

Each of the four unit tests and the cumulative final has **one PDF containing five practice versions and their matched answer keys**. The student-facing links are on `../practice-tests.html`. Units have five 20-point questions; the final has ten 10-point questions. Each version totals 100 points.

The practice forms draw complete questions and matched answers from the current 20-version instructor banks under `_instructor/assessments/2026-10-30/`. Each question family is sampled separately, numerical variety is preferred within each family, and the question order is shuffled. No complete practice form duplicates an instructor form or another practice form. Individual questions can also occur in the instructor banks. The practice records retain the source version for every question so the selection and its answers can be checked.

Use the current [unit](../unit-test-specifications.md), [final](../final-exam-specifications.md), and [shared presentation](../../docs/test-presentation.md) specifications. Print US Letter, actual size, duplex, long-edge flip. Each student test and key starts on a fresh front; intentional blank pages preserve that alignment. PDF bookmarks jump to each version, student test, and key.

From the repository root:

```bash
python -m pip install -r scripts/practice-requirements.txt
python scripts/build_math101_practice_bundles.py
python scripts/verify_math101_practice_bundles.py --render
```

Use `--only 101-unit-1` (or another unit/final slug) for a focused rebuild. Use `--reformat` to preserve the saved practice questions and identifiers while rebuilding their layout. The shared `generate_practice_batch.py` entry point also builds bundles rather than restoring the former three-file sets.

`manifest.json` supplies the five website links. Each PDF has an adjacent JSON reproduction record with questions, keys, source version references, seeds, version identifiers, and geometry. `source/assessments.json` collects the 25 forms. The verifier reruns symbolic source constructors, checks every selected question and key against its source, then checks scoring, question families, distinct forms, bookmarks, blank padding, response/key alignment, margins, footers, and index links. Rendered pages are temporary QA artifacts.
