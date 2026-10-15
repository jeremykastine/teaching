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

The root `index.html` is the single Teaching navigation page. Under each course heading, link directly to its up-to-date class schedule(s) and its resource categories. MATH 101 and TSM use Class slides or Lecture notes, Homework, and Practice tests. Statistics uses Class slides, Homework, Test banks and answer keys (`stats/question-banks/index.html`), and Excel competency checks (`stats/excel-competency-checks.html`). Statistics has no separate practice tests, test-form specifications, or AI study/test-generation prompts; keep its bank HTML and PDFs focused on questions, answers, explanations, and slide references. Its old `practice-tests.html` URL is only a compatibility redirect to the banks. This Statistics exception was requested on October 14, 2026. The former course indexes (`101/index.html`, `stats/index.html`, and `tsm/index.html`) redirect to their course heading on the root index. Detailed resources belong in separate pages in the course folder. TSM lesson table-of-contents links point to `lecture-notes.html`. Below the three course sections, keep a shared Generic Resources heading with an Absence Procedure link to `absence-procedure.html`. Preserve this structure when rebuilding materials with the shared scripts.

## Absence procedure

`absence-procedure.html` is the single source for student directions and the complete AI instructions. State the allowance as **one free unexcused absence per quarter**. Keep student directions minimal: copy the short starter prompt into an AI tool and follow its guidance through emailing the full transcript. The starter prompt links back to `absence-procedure.html#ai-instructions`. Provide separate copy buttons for the short prompt and the full AI instructions, with a manual-copy fallback. Keep all AI instructions as readable static HTML in the same file, even when displayed in an expandable section. The AI must begin with an overview of expectations before collecting intake information; detailed preparation, timing, work, review, and submission requirements belong in its instructions rather than in a separate student checklist. Preserve the existing flexibility for documented independent work. `missed-class-ai-guided-assignment.html` is a compatibility redirect to the consolidated page, not a second copy of the assignment. Use `tsm/lecture-notes.html` for the TSM topic index, not the redirecting `tsm/` course URL.

The active-repository policy was explicitly requested by the user on October 7, 2026; the consolidated absence procedure was requested on October 13, 2026. Change these policies only if the user explicitly reverses the relevant instruction.

## Live class schedules

Before creating or updating any class schedule, load and follow `schedule-update-rules.json`. It contains the machine-readable schedule registry and update policy. Preserve separate 9 a.m. and 1 p.m. TSM schedules and their root-index links. These HTML schedules are instructor-maintained sources, not outputs to regenerate from lecture notes or generic planning documents.
