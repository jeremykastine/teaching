"""Build the three resource categories and a compact landing page for each course."""
import json
from html import escape
from pathlib import Path

COURSES = {
    '101': ('MATH 101 · College Algebra', 'Class slides', 'class-slides.html'),
    'stats': ('Statistics', 'Class slides', 'class-slides.html'),
    'tsm': ('TSM 098 / 099', 'Lecture notes', 'lecture-notes.html'),
}


def navigation(course, active=None):
    _, notes, filename = COURSES[course]
    links = [('index.html', 'Course home'), (filename, notes),
             ('homework.html', 'Homework'), ('practice-tests.html', 'Practice tests')]
    return '<nav aria-label="Course resources" class="resource-nav">' + ''.join(
        f'<a href="{href}"' + (' aria-current="page"' if href == active else '') +
        f'>{label}</a>' for href, label in links) + '</nav>'


def page(root, filename, heading, body, *, landing=False):
    course, _, _ = COURSES[root.name]
    nav = '' if landing else navigation(root.name, filename)
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(course)} · {escape(heading)}</title><link rel="stylesheet" href="../course-pages.css"></head>
<body><main><header><p class="eyebrow">{escape(course)}</p><p><a href="../index.html">Teaching</a></p>
<h1>{escape(heading)}</h1>{nav}</header>{body}</main></body></html>
'''
    (root / filename).write_text(html)


def build_homework(root):
    assignments = json.loads((root / 'homework/source/assignments.json').read_text())
    if root.name == '101' and (root / 'homework/chapter-1-homework.pdf').is_file():
        assignments.insert(0, {'course': 'MATH 101', 'file': 'chapter-1-homework.pdf',
                              'title': 'Chapter 1 Homework', 'coverage': 'Sections 1.1–1.6',
                              'subtitle': 'Essential prerequisites'})
    groups = {}
    for a in assignments:
        groups.setdefault(a['course'], []).append(a)
    body = '<p>Each assignment is designed for about one hour, including checking and corrections. Show all work on separate paper, upload a clear photo of your one best representative page in Blackboard, and keep all your work.</p>'
    for course, items in groups.items():
        body += f'<section><h2>{escape(course)}</h2><ul class="resources">'
        for a in items:
            title = f'{a["title"]}: {a["coverage"]} — {a["subtitle"]}'
            body += f'<li><a href="homework/{escape(a["file"], quote=True)}">{escape(title)} (PDF)</a></li>'
        body += '</ul></section>'
    page(root, 'homework.html', 'Homework', body)


def build_practice(root):
    manifest = root / 'practice-tests/manifest.json'
    body = ''
    if manifest.is_file():
        groups = {}
        for a in json.loads(manifest.read_text()):
            groups.setdefault(a['course'], {}).setdefault(a['assessment'], []).append(a)
        body += '<p>Three practice tests are available for each unit test and final exam. Each PDF includes space for answers beside the questions and an instructor answer key. Try the test before checking the key.</p>'
        for course, assessments in groups.items():
            body += f'<section><h2>{escape(course)}</h2><ul class="resources">'
            for items in assessments.values():
                body += f'<li><h3>{escape(items[0]["title"])}</h3><p class="links">'
                body += ''.join(f'<a href="practice-tests/{escape(a["file"], quote=True)}">Practice {a["practice"]} (PDF)</a>' for a in items)
                body += '</p></li>'
            body += '</ul></section>'
    bank_manifest = root / 'question-banks/manifest.json'
    if bank_manifest.is_file():
        body += '<section id="unit-test-banks"><h2>Unit-test question banks</h2><p>Practice with 100 multiple-choice questions per unit, including answers, explanations, and slide references. Tests draw ten questions across the ten skill groups, emphasizing conceptual reasoning and small calculations. A four-function calculator is allowed. Chapter 9 is not tested.</p><p class="links"><a href="question-banks/index.html">All question banks and AI study prompt</a><a href="unit-test-specifications.md">Unit-test specifications</a><a href="question-banks/create-unit-test-prompt.txt">Instructor test-generation prompt</a></p><ul class="resources">'
        for bank in json.loads(bank_manifest.read_text()):
            a, b = bank['chapters']
            body += f'<li><p class="meta">Unit {bank["unit"]} · Chapters {a}–{b} · {bank["question_count"]} questions</p><h3>{escape(bank["title"])}</h3><p class="links">'
            body += f'<a href="question-banks/{bank["html"]}">Practice online</a><a href="question-banks/{bank["pdf"]}">Bank and answer key (PDF)</a><a href="question-banks/{bank["json"]}" download>JSON for AI study</a></p></li>'
        body += '</ul></section>'
    page(root, 'practice-tests.html', 'Practice tests', body)


def build_categories(course_root):
    root = Path(course_root)
    course, label, filename = COURSES[root.name]
    body = '<nav aria-label="Course categories"><ul class="category-list">' + ''.join(
        f'<li><a href="{href}">{text}</a></li>' for href, text in
        [(filename, label), ('homework.html', 'Homework'), ('practice-tests.html', 'Practice tests')]
    ) + '</ul></nav>'
    page(root, 'index.html', course, body, landing=True)
    build_homework(root)
    build_practice(root)


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    for course in COURSES:
        build_categories(root / course)
