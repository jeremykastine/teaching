# MATH 101 practice tests

Three numerically distinct practice versions are provided for each of the four unit tests and the cumulative final. Links appear after Chapters 2, 4, 5, and 7 in the course index; final practice follows Unit 4.

Each PDF combines problem statements in the left two-thirds of each printable page with aligned answer spaces in the right one-third. The concise instructor key uses one page-matching column per test page (up to three per key page), with identical vertical answer positions and separators. Student tests aim for one or two pages; longer finals may use more. The key starts on a fresh duplex sheet, with a completely blank page inserted after an odd-length test. See the [approved format](../../docs/algebra-test-format.md). Unit tests contain five 20-point questions; finals contain ten 10-point questions. Students show work on separate paper, and graphing grids they complete are in the answer column.

The controlling sources are [unit-test specifications](../unit-test-specifications.md) and [cumulative specifications](../final-exam-specifications.md). Mathematical data, graphs, scoring, and question order are retained in `source/assessments.json`; `manifest.json` supplies index links. The source JSON includes keys and is instructor authoring material.

From the repository root:

```bash
python -m pip install -r scripts/practice-requirements.txt
python scripts/generate_practice_batch.py --version 202610122020
```

This rebuilds the entire 48-file TSM/MATH 101 batch. For a focused rebuild, add `--only 101-unit-1`, `101-unit-2`, `101-unit-3`, `101-unit-4`, or `101-final`. The version is a local timestamp followed by a unique batch suffix, not a lettered version. Unit timing remains an authoring estimate to refine after classroom use.

The index builder reads the manifest so rebuilding slides or homework preserves the practice-test links.

After building, run `python scripts/verify_algebra_tests.py` from the repository root to check scoring, vertical matches, point positions, empty student answer regions, duplex padding, print margins, and index links. Render and visually inspect the PDFs before publishing.
