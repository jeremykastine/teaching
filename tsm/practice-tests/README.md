# TSM 098 and TSM 099 practice tests

Three distinct practice versions are provided for all four TSM 098 unit tests, all five TSM 099 unit tests, and each course's final. Links are embedded at the current scheduled test points: after Topics 8, 17, 23, 29, and 34. Final practice appears after Topic 34, before the word-problem activities.

Each PDF combines problem statements in the left two-thirds of each printable page with aligned answer spaces in the right one-third. The concise instructor key uses one page-matching column per test page (up to three per key page), with identical vertical answer positions and separators. Student tests aim for one or two pages; longer finals may use more. The key starts on a fresh duplex sheet, with a completely blank page inserted after an odd-length test. See the [approved format](../../docs/algebra-test-format.md). Unit tests contain five 20-point questions; finals contain ten 10-point questions. Students show work on separate paper, and graphing grids they complete are in the answer column.

The [master specification](../specifications/TSM_Test_Specs.md) controls content. Each practice final contains six institutional-family questions and four supplemental questions selected to broaden coverage. These are randomized practice finals; an official final's standardized position map is not needed for them.

Source data, keys, graphs, scores, and question order are retained in `source/assessments.json`. This is instructor authoring material. The manifest supplies the published links.

From the repository root:

```bash
python -m pip install -r scripts/practice-requirements.txt
python scripts/generate_practice_batch.py --version 202610122020
```

This rebuilds the 48-file TSM/MATH 101 batch. For a focused rebuild, add `--only` followed by a slug in the manifest, such as `98-arithmetic`, `99-graphing`, or `99-final`. Identifiers use the timestamp plus a unique batch suffix. The key is for checking after attempting the test; no extra compliance report is included in the practice PDFs.

After building, run `python scripts/verify_algebra_tests.py` from the repository root to check scoring, vertical matches, point positions, empty student answer regions, duplex padding, print margins, and index links. Render and visually inspect the PDFs before publishing.
