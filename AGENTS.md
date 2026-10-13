# Repository policy

Teaching is the only active repository for Jeremy Kastine's TSM, MATH 101, and Statistics materials.

## Course locations

- MATH 101 / College Algebra: `101/`
- Statistics: `stats/`
- TSM 098 / 099: `tsm/`
- Course landing page: root `index.html`

## Retired repositories

Do not edit or commit to `jeremykastine/101`, `jeremykastine/stats`, or `jeremykastine/tsm`. They are historical repositories with redirects, even if GitHub has not formally archived them. When the user asks for work on 101, Stats, or TSM, use the corresponding folder here. Do not sync future changes back to the old repositories.

Preserve course-specific specifications and build sources in their respective folders. Run slide builders from their course folder. Keep course website links relative to the combined Teaching structure.

## Course navigation

Each course index (`101/index.html`, `stats/index.html`, and `tsm/index.html`) lists only three resource categories: Class slides or Lecture notes, Homework, and Practice tests. Detailed resources belong in separate `class-slides.html` (MATH 101 and Statistics), `lecture-notes.html` (TSM), `homework.html`, and `practice-tests.html` pages in the course folder. Statistics question banks are linked from its practice-tests page. TSM lesson table-of-contents links point to `lecture-notes.html`. Preserve this structure when rebuilding materials with the shared scripts.

This policy was explicitly requested by the user on October 7, 2026. Change it only if the user explicitly reverses the instruction.
