#!/usr/bin/env python3
"""Build named master-course navigation from the shared curriculum registry."""

from html import escape
from pathlib import Path
import json
import posixpath
import re

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "master-documents/curriculum.json"


def relative(target, source):
    return posixpath.relpath(target, posixpath.dirname(source))


def replace_one(pattern, replacement, text, label):
    text, count = re.subn(pattern, lambda match: replacement(match), text, count=1, flags=re.S)
    if count != 1:
        raise ValueError(f"Missing {label}")
    return text


def build_course(course):
    topics = [(unit, topic) for unit in course["units"] for topic in unit["topics"]]
    slugs = [topic["slug"] for _, topic in topics]
    if len(slugs) != len(set(slugs)):
        raise ValueError(f"Duplicate topic identity in {course['name']}")
    sections = []
    for unit in course["units"]:
        links = "\n".join(
            f'    <li><a href="{relative(topic["file"], course["index"])}">{escape(topic["name"])}</a></li>'
            for topic in unit["topics"]
        )
        sections.append(
            f'<section class="master-unit" id="{unit["slug"]}" aria-labelledby="{unit["slug"]}-heading">\n'
            f'  <h2 id="{unit["slug"]}-heading">{escape(unit["name"])}</h2>\n'
            f'  <ul class="master-topic-list">\n{links}\n  </ul>\n</section>'
        )
    contents = "\n".join(sections)
    index = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(course["name"])} Master Lecture Notes</title>
  <link rel="stylesheet" href="../tsm/styles.css">
  <link rel="stylesheet" href="lecture-notes.css">
</head>
<body>
<main class="lecture-notes">
<nav class="topic-nav" aria-label="Course navigation">
  <a href="../index.html#master-documents">Teaching · Master Documents</a>
  <a href="{relative(course["plan"], course["index"])}">Lecture and assessment plan</a>
</nav>
<p class="series-title">{escape(course["name"])}</p>
<h1>Master Lecture Notes</h1>
<p>Use these named topics, grouped into units, to prepare future quarters. For your current class, use the links under your course on the <a href="../index.html">Teaching page</a>.</p>
{contents}
</main>
</body>
</html>
'''
    (ROOT / course["index"]).write_text(index, encoding="utf-8")

    for position, (unit, topic) in enumerate(topics):
        path = ROOT / topic["file"]
        text = path.read_text(encoding="utf-8")
        links = [
            f'<a href="{relative(course["index"], topic["file"])}">Table of contents</a>',
            f'<a href="{relative(course["plan"], topic["file"])}#{topic["slug"]}">Lecture and assessment plan</a>',
        ]
        if position:
            previous = topics[position - 1][1]
            links.append(f'<a href="{relative(previous["file"], topic["file"])}">Previous: {escape(previous["name"])}</a>')
        if position + 1 < len(topics):
            following = topics[position + 1][1]
            links.append(f'<a href="{relative(following["file"], topic["file"])}">Next: {escape(following["name"])}</a>')
        nav = '<nav class="topic-nav" aria-label="Lecture navigation">' + "".join(links) + "</nav>"
        text = replace_one(r'<nav class="topic-nav"[^>]*>.*?</nav>', lambda _: nav, text, topic["file"])
        text = replace_one(r"<title>.*?</title>", lambda _: f'<title>{escape(topic["name"])} | {escape(course["name"])} Master Lecture Notes</title>', text, "title")
        text = replace_one(r"<h1>.*?</h1>", lambda _: f'<h1>{escape(topic["name"])}</h1>', text, "heading")
        text = re.sub(r'\n<p class="unit-name">.*?</p>', "", text)
        unit_line = f'<p class="unit-name"><strong>Unit:</strong> <a href="{relative(course["index"], topic["file"])}#{unit["slug"]}">{escape(unit["name"])}</a></p>'
        text = replace_one(r'(<p class="series-title">.*?</p>)', lambda m: m.group(1) + "\n" + unit_line, text, "unit")
        path.write_text(text, encoding="utf-8")

    plan_path = ROOT / course["plan"]
    plan = plan_path.read_text(encoding="utf-8")
    rows = {
        slug: row
        for row, slug in re.findall(
            r'(<tr\b[^>]*\bdata-topic="([^"]+)"[^>]*>.*?</tr>)', plan, flags=re.S
        )
    }
    if set(rows) != set(slugs):
        raise ValueError(f"Plan topics differ from curriculum in {course['plan']}")
    columns = 4 if course["name"].startswith("TSM") else 3
    groups = []
    for unit in course["units"]:
        group_rows = []
        for topic in unit["topics"]:
            row = rows[topic["slug"]]
            header = (
                f'<th scope="row"><a href="{relative(topic["file"], course["plan"])}">'
                f'{escape(topic["name"])}</a></th>'
            )
            # Keep pre-migration bookmarks functional without visible numbering.
            alias = re.search(r'<span id="topic-\d+"></span>', row)
            if alias:
                header = header.replace('<th scope="row">', '<th scope="row">' + alias.group(0))
            row = replace_one(r'<th scope="row">.*?</th>', lambda _: header, row, "plan topic heading")
            group_rows.append(row)
        groups.append(
            f'<tbody id="{unit["slug"]}" data-unit="{unit["slug"]}">\n'
            f'        <tr class="unit-heading"><th colspan="{columns}" scope="rowgroup">{escape(unit["name"])}</th></tr>\n'
            + "\n".join("        " + row for row in group_rows) + "\n      </tbody>"
        )
    plan = replace_one(r"<tbody\b.*</tbody>", lambda _: "\n      ".join(groups), plan, "unit groups")
    plan_path.write_text(plan, encoding="utf-8")
    return len(topics)


def main():
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    for course in registry["courses"].values():
        count = build_course(course)
        print(f"{course['name']}: {len(course['units'])} named units, {count} named topics")


if __name__ == "__main__":
    main()
