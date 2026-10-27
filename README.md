# Teaching

Course materials for Jeremy Kastine. **This is the only active repository for TSM, MATH 101, and Statistics. All future edits must be made here.**

- [TSM 098 / 099](tsm/index.html) — lecture notes
- [MATH 101](101/index.html) — College Algebra slides, schedule, and assessment specifications
- [Statistics](stats/index.html) — slides, homework, test banks with answer keys, and Excel competency checks

Publish GitHub Pages from `main` and `/(root)`. The root `index.html` links to each course.

Each course retains its original files and relative folder structure. Slide build scripts, requirements, and specifications remain in the corresponding course folder; run each script from that course folder. Shared documents can be added at the root as needed.

The former standalone repositories retain their original commit history and have migration notices and index redirects. They are retired: **do not edit `jeremykastine/101`, `jeremykastine/stats`, or `jeremykastine/tsm` anymore**, even while they remain unarchived. `migration.json` records the source commit and file count imported for each course.

### Full textbook-aligned lecture notes

Statistics now has 36 section documents at `stats/lecture-notes.html`; College Algebra has 40 at `101/lecture-notes.html`. Both follow their course coverage registries and the textbook sequence, using the TSM answer-reveal controls. The approved Statistics 3.4/3.5 notes are retained. Optional Algebra applications, restricted complex-number scope, Statistics labs, and the conceptual-only Chapter 9 overview are identified in the notes.

The reproducible builder is `scripts/build_lecture_notes.py`; licensed textbook snapshots and course-specific supplements live in each course's `notes-source/` folder. See those READMEs for provenance, scope, and build instructions. Figures are shared locally in `notes-assets/`. Existing slides, schedules, and assessment files remain available.
