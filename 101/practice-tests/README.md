# MATH 101 practice tests

Three numerically distinct practice versions are provided for each of the four unit tests and the cumulative final. Links appear after Chapters 2, 4, 5, and 7 in the course index; final practice follows Unit 4.

Each PDF contains a compact booklet, a student answer sheet, and a matched concise key. Sections start on fresh duplex sheets. Unit tests contain five 20-point questions and are designed for 30 minutes. Finals contain ten 10-point questions. All tests cover strictly algebraic content; applications and word problems remain classroom labs.

The controlling sources are [unit-test specifications](../unit-test-specifications.md) and [cumulative specifications](../final-exam-specifications.md). Mathematical data, graphs, scoring, and question order are retained in `source/assessments.json`; `manifest.json` supplies index links. The source JSON includes keys and is instructor authoring material.

From the repository root:

```bash
python -m pip install -r scripts/practice-requirements.txt
python scripts/generate_practice_batch.py --version 202610122020
```

This rebuilds the entire 48-file TSM/MATH 101 batch. For a focused rebuild, add `--only 101-unit-1`, `101-unit-2`, `101-unit-3`, `101-unit-4`, or `101-final`. The version is a local timestamp followed by a unique batch suffix, not a lettered version. Unit timing remains an authoring estimate to refine after classroom use.

The index builder reads the manifest so rebuilding slides or homework preserves the practice-test links.
