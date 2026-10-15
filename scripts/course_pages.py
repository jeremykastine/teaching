"""Build course resource pages linked from the single Teaching index."""
import json
from html import escape
from pathlib import Path

COURSES = {
    '101': ('MATH 101 · College Algebra', 'Class slides', 'class-slides.html'),
    'stats': ('Statistics', 'Class slides', 'class-slides.html'),
    'tsm': ('TSM 098 / 099', 'Lecture notes', 'lecture-notes.html'),
}
ANCHORS = {'101': 'math101', 'stats': 'stats', 'tsm': 'tsm'}


def navigation(course, active=None):
    _, notes, filename = COURSES[course]
    links = [(f'../index.html#{ANCHORS[course]}', 'Teaching'), (filename, notes),
             ('homework.html', 'Homework')]
    if course == 'stats':
        links += [('question-banks/index.html', 'Test banks and answer keys'),
                  ('excel-competency-checks.html', 'Excel competency checks')]
    else:
        links.append(('practice-tests.html', 'Practice tests'))
    return '<nav aria-label="Course resources" class="resource-nav">' + ''.join(
        f'<a href="{href}"' + (' aria-current="page"' if href == active else '') +
        f'>{label}</a>' for href, label in links) + '</nav>'


def page(root, filename, heading, body):
    course, _, _ = COURSES[root.name]
    nav = navigation(root.name, filename)
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
    if root.name == 'stats':
        return
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
    page(root, 'practice-tests.html', 'Practice tests', body)


def build_categories(course_root):
    root = Path(course_root)
    # Preserve old course URLs without introducing another navigation page.
    destination = f'../index.html#{ANCHORS[root.name]}'
    (root / 'index.html').write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="0; url={destination}"><title>Teaching</title></head>
<body><p><a href="{destination}">Teaching resources</a></p></body></html>
''')
    build_homework(root)
    build_practice(root)


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    for course in COURSES:
        build_categories(root / course)
