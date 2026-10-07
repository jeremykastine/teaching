#!/usr/bin/env python3
"""Build portrait classroom prompts from per-chapter JSON sources."""
import argparse
import io
import json
from html import escape
from pathlib import Path

import fitz
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.mathtext import math_to_image
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle

W, H, MARGIN = 612, 792, 48
CONTENT_WIDTH = W - 2 * MARGIN
INK, ACCENT, MUTED = [HexColor(x) for x in ('#14232d', '#185f72', '#52616b')]
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')
for name, filename in [('Sans', 'DejaVuSans.ttf'), ('Bold', 'DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / filename)))

COURSES = {
    '101': {'book': 'College Algebra 2e', 'slug': 'college-algebra-2e', 'authors': 'Jay Abramson',
            'year': 2021, 'intro': '1-introduction-to-prerequisites', 'name': 'MATH 101',
            'heading': 'MATH 101<br>College Algebra',
            'chapters': {1: 'Prerequisites', 2: 'Equations and Inequalities', 3: 'Functions',
                         4: 'Linear Functions', 5: 'Polynomial and Rational Functions',
                         6: 'Exponential and Logarithmic Functions', 7: 'Systems of Equations and Inequalities'},
            'optional': {'2.3', '4.2', '4.3', '6.7', '6.8'}},
    'stats': {'book': 'Introductory Statistics 2e', 'slug': 'introductory-statistics-2e',
              'authors': 'Barbara Illowsky and Susan Dean', 'year': 2023, 'intro': '1-introduction',
              'name': 'Statistics', 'heading': 'Statistics<br>Class slides',
              'chapters': {1: 'Sampling and Data', 2: 'Descriptive Statistics', 3: 'Probability Topics',
                           4: 'Discrete Random Variables', 5: 'Continuous Random Variables',
                           6: 'The Normal Distribution', 7: 'The Central Limit Theorem',
                           8: 'Confidence Intervals', 9: 'Hypothesis Testing: Conceptual Overview'},
              'optional': set()},
}


def paragraph(c, text, x, top, width, size, font='Sans', color=INK):
    style = ParagraphStyle('slide', fontName=font, fontSize=size, leading=size * 1.27, textColor=color)
    p = Paragraph(escape(text).replace('\\n', '<br/>').replace('\n', '<br/>'), style)
    _, height = p.wrap(width, H)
    p.drawOn(c, x, top - height)
    return top - height


_math_cache = {}


def formula_pdf(expression):
    if expression not in _math_cache:
        stream = io.BytesIO()
        math_to_image('$' + expression.replace(r'\frac', r'\dfrac') + '$', stream,
                      prop=FontProperties(size=28), format='pdf', color='#14232d')
        _math_cache[expression] = stream.getvalue()
    return fitz.open(stream=_math_cache[expression], filetype='pdf')


def plot_pdf(spec):
    fig, ax = plt.subplots(figsize=(5.8, 2.0))
    kind = spec['kind']
    if kind == 'histogram':
        ax.hist(spec['data'], bins=spec['bins'], color='#b7d3da', edgecolor='#14232d', linewidth=1)
        ax.set_xticks(spec['bins'])
    elif kind == 'boxplot':
        ax.boxplot(spec['data'], vert=False, whis=spec.get('whis', 1.5), patch_artist=True,
                   boxprops={'facecolor': '#b7d3da', 'edgecolor': '#14232d'},
                   medianprops={'color': '#14232d'}, flierprops={'markeredgecolor': '#14232d'})
        ax.set_yticks([])
    elif kind == 'line':
        ax.plot(spec['x'], spec['y'], 'o-', color='#185f72', markersize=4)
        if 'xticklabels' in spec:
            ax.set_xticks(spec['x'], spec['xticklabels'])
    elif kind == 'venn':
        from matplotlib.patches import Circle, Rectangle
        ax.add_patch(Rectangle((.1, .1), 5.6, 2.2, fill=False, edgecolor='#52616b'))
        for center, label in zip([(2.25, 1.2), (3.35, 1.2)], spec.get('labels', ['A', 'B'])):
            ax.add_patch(Circle(center, .86, facecolor='#b7d3da', alpha=.32, edgecolor='#14232d'))
            ax.text(center[0], 2.12, label, ha='center', va='center', fontsize=13)
        for key, x, y in [('a', 1.86, 1.2), ('both', 2.8, 1.2), ('b', 3.74, 1.2), ('neither', 5.1, .48)]:
            ax.text(x, y, str(spec['regions'][key]), ha='center', va='center', fontsize=14)
        ax.set_xlim(0, 5.8); ax.set_ylim(0, 2.4); ax.set_aspect('equal'); ax.axis('off')
    elif kind == 'tree':
        if len(spec['first']) != 2 or any(len(branch) != 2 for branch in spec['second']):
            raise ValueError('Tree plot supports two first branches with two outcomes each')
        ax.set_xlim(0, 5.8); ax.set_ylim(-.25, 3.25); ax.axis('off')
        for j, node in enumerate(spec['first']):
            y = 2.5 if j == 0 else .5
            ax.plot([.15, 1.65], [1.5, y], color='#14232d', lw=1)
            ax.text(.65, (1.5+y)/2 + (.20 if j == 0 else -.20), str(node['p']),
                    fontsize=12, ha='center', va='center', bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1})
            ax.text(1.7, y, node['label'], fontsize=13, va='center')
            for k, child in enumerate(spec['second'][j]):
                cy = y + (.45 if k == 0 else -.45)
                ax.plot([2.3, 4.05], [y, cy], color='#14232d', lw=1)
                ax.text(3.2, (y+cy)/2 + (.20 if k == 0 else -.20), str(child['p']),
                        fontsize=12, ha='center', va='center', bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1})
                ax.text(4.12, cy, child['label'], fontsize=13, va='center')
    else:
        raise ValueError(f'Unsupported plot kind: {kind}')
    ax.set_xlabel(spec.get('xlabel', ''), fontsize=12)
    ax.set_ylabel(spec.get('ylabel', ''), fontsize=12)
    ax.tick_params(labelsize=11)
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    if kind == 'histogram':
        from matplotlib.ticker import MaxNLocator
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    fig.tight_layout(pad=.4)
    stream = io.BytesIO()
    fig.savefig(stream, format='pdf')
    plt.close(fig)
    return fitz.open(stream=stream.getvalue(), filetype='pdf')


def draw_table(c, spec, top):
    rows = [spec['headers']] + spec['rows']
    if not all(len(row) == len(rows[0]) for row in rows):
        raise ValueError('Table rows have different column counts')
    style = ParagraphStyle('cell', fontName='Sans', fontSize=18, leading=21, textColor=INK)
    cells = [[Paragraph(escape(str(cell)), style) for cell in row] for row in rows]
    table = Table(cells, colWidths=[CONTENT_WIDTH / len(rows[0])] * len(rows[0]))
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 2), ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LINEBELOW', (0, 0), (-1, 0), .8, ACCENT),
        ('LINEBELOW', (0, 1), (-1, -1), .3, HexColor('#c7d2d7')),
    ]))
    _, height = table.wrap(CONTENT_WIDTH, H)
    table.drawOn(c, MARGIN, top - height)
    return top - height - 18


def build_section(root, cfg, section):
    number = section['number']
    target = root / 'slides' / f'section-{number.replace(".", "-")}.pdf'
    buffer, layers = io.BytesIO(), []
    c = canvas.Canvas(buffer, pagesize=(W, H), pageCompression=1, invariant=1)
    c.setTitle(f'{number} {section["title"]} - Discussion Slides')
    c.setAuthor('Jeremy Kastine')
    c.setSubject(f'Original classroom prompts aligned to OpenStax {cfg["book"]}; CC BY-NC-SA 4.0')
    c.setViewerPreference('DisplayDocTitle', 'true')
    base = f'https://openstax.org/books/{cfg["slug"]}/pages/'
    for i, slide in enumerate(section['slides'], 1):
        if '?' not in slide['question']:
            raise ValueError(f'{number} slide {i}: missing discussion question')
        c.setFillColor(ACCENT)
        c.rect(MARGIN, H - 49, 42, 4, fill=1, stroke=0)
        c.setFont('Sans', 11)
        c.setFillColor(MUTED)
        c.drawRightString(W - MARGIN, H - 50, f'{number}  /  {i} of {len(section["slides"])}')
        top = paragraph(c, slide['title'], MARGIN, H - 70, CONTENT_WIDTH, 24, 'Bold') - 17
        body = slide.get('body', '')
        if body:
            size = 20 if '\\n' in body or '\n' in body else 22
            top = paragraph(c, body, MARGIN, top, CONTENT_WIDTH, size) - 19
        if slide.get('math'):
            doc = formula_pdf(slide['math'])
            width, height = doc[0].rect.width, doc[0].rect.height
            doc.close()
            if width > CONTENT_WIDTH:
                raise ValueError(f'{number} slide {i}: formula width {width:.1f} exceeds {CONTENT_WIDTH}')
            layers.append((i - 1, 'math', slide['math'], fitz.Rect(MARGIN, H - top, MARGIN + width, H - top + height)))
            top -= height + 23
        if slide.get('table'):
            top = draw_table(c, slide['table'], top)
        if slide.get('plot'):
            width, height = 440, 145
            layers.append((i - 1, 'plot', slide['plot'], fitz.Rect(MARGIN, H - top, MARGIN + width, H - top + height)))
            top -= height + 16
        bottom = paragraph(c, slide['question'], MARGIN, top, CONTENT_WIDTH, 22, 'Bold', ACCENT)
        if bottom < H / 2:
            raise ValueError(f'{number} slide {i}: prompt extends to y={H - bottom:.1f}; limit {H / 2}')
        paragraph(c, f'Aligned to OpenStax {cfg["book"]}, {cfg["authors"]}. Classroom adaptations. CC BY-NC-SA 4.0.',
                  MARGIN, 32, CONTENT_WIDTH, 6.5, color=MUTED)
        c.setFillColor(MUTED)
        c.setFont('Sans', 6.5)
        c.drawString(MARGIN, 14, 'Access for free at ' + base + cfg['intro'])
        c.linkURL(base + section['slug'], (MARGIN, 12, W - MARGIN, 33), relative=0)
        c.showPage()
    c.save()
    document = fitz.open(stream=buffer.getvalue(), filetype='pdf')
    for page, kind, value, rect in layers:
        doc = formula_pdf(value) if kind == 'math' else plot_pdf(value)
        document[page].show_pdf_page(rect, doc, 0)
        doc.close()
    document.save(target, garbage=4, deflate=True)
    document.close()
    print(f'{target.relative_to(root)}: {len(section["slides"])} slides', flush=True)


CSS = '''
:root{color-scheme:light;--ink:#14232d;--accent:#185f72;--muted:#52616b}
*{box-sizing:border-box}body{margin:0;background:#f5f7f8;color:var(--ink);font:18px/1.6 system-ui,sans-serif}
main{max-width:960px;margin:auto;padding:64px 28px}header{margin-bottom:48px}.eyebrow{font-weight:650;color:var(--accent);margin:0}
h1{font-size:clamp(2.6rem,7vw,4rem);line-height:1.05;letter-spacing:-.04em;margin:12px 0 24px}header p{max-width:720px}
h2{font-size:1.65rem;margin:42px 0 10px}h3{font-size:1.22rem;line-height:1.4;margin:6px 0 14px}h3 a{color:var(--ink);text-decoration:none}
a{color:var(--accent);text-underline-offset:4px}a:hover{text-decoration:underline}a:focus-visible{outline:3px solid #b05819;outline-offset:5px}
ul{list-style:none;padding:0;margin:24px 0}li{padding:26px 0;border-top:1px solid #c7d2d7}.section{font-size:.88rem;color:var(--muted);font-weight:650}
.links,.chapter-links{display:flex;gap:12px 28px;flex-wrap:wrap;margin:0;font-size:.95rem}.meta{color:var(--muted);font-size:.88rem}
footer{margin-top:42px;border-top:1px solid #c7d2d7;padding-top:24px;font-size:.82rem;color:var(--muted)}
@media(max-width:520px){main{padding:36px 20px}.links{flex-direction:column;gap:10px}h2{font-size:1.4rem}}
'''


def build_index(root, cfg, sections):
    base = f'https://openstax.org/books/{cfg["slug"]}/pages/'
    groups = {}
    for section in sections:
        chapter = int(section['number'].split('.')[0])
        groups.setdefault(chapter, []).append(section)
    nav = ''.join(f'<a href="#chapter-{ch}">Chapter {ch}</a>' for ch in groups)
    chunks = []
    for chapter, group in groups.items():
        note = 'Selected sections from the course schedule.'
        if cfg['name'] == 'Statistics' and chapter == 9:
            note = 'A conceptual introduction; detailed Chapter 9 calculation procedures are outside this course plan.'
        cards = []
        for section in group:
            number = section['number']
            filename = f'section-{number.replace(".", "-")}.pdf'
            label = 'Chapter 9 overview' if number == '9.0' else f'Section {number}'
            if number in cfg['optional']:
                label += ' · Optional application'
            cards.append(f'<li><span class="section">{label}</span><h3><a href="slides/{filename}">{escape(section["title"])}</a></h3>'
                         f'<p class="links"><a href="slides/{filename}">Open slides <span class="meta">(PDF, {len(section["slides"])} slides)</span></a>'
                         f'<a href="{base + section["slug"]}">Read textbook section</a></p></li>')
        chunks.append(f'<section aria-labelledby="chapter-{chapter}"><h2 id="chapter-{chapter}">Chapter {chapter} · {cfg["chapters"][chapter]}</h2>'
                      f'<p>{note}</p><ul>{"".join(cards)}</ul></section>')
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{cfg['name']} | Class Slides</title><meta name="description" content="Portrait discussion slides for OpenStax {cfg['book']}, organized by covered chapter and section.">
<style>{CSS}</style></head><body><main><header><p class="eyebrow">Fall 2026 · Jeremy Kastine</p><p><a href="../index.html">Teaching</a></p>
<h1>{cfg['heading']}</h1><p>Discussion questions and problems for <a href="https://openstax.org/details/books/{cfg['slug']}">OpenStax <em>{cfg['book']}</em></a>.</p>
<p>One concept or problem per portrait slide, with room for class notes and worked solutions.</p>
<nav aria-label="Chapters" class="chapter-links">{nav}</nav></header>{''.join(chunks)}
<footer><p>Aligned to <em>{cfg['book']}</em> by {cfg['authors']}, OpenStax, Rice University ({cfg['year']}). Definitions, problems, and synthetic datasets are original classroom adaptations aligned to the textbook sections.</p>
<p>Slide materials: <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a>. <a href="{base + cfg['intro']}">Access the textbook for free</a>.</p></footer></main></body></html>'''
    (root / 'index.html').write_text(html)


def main(course_root):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--chapters', nargs='*', type=int, help='Only regenerate PDFs for these chapters; index always includes all sources')
    args = parser.parse_args()
    root = Path(course_root)
    cfg = COURSES[root.name]
    sections = []
    for path in sorted((root / 'slides/source').glob('chapter-*.json')):
        data = json.loads(path.read_text())
        sections.extend(data)
    sections.sort(key=lambda s: tuple(int(n) for n in s['number'].split('.')))
    numbers = [s['number'] for s in sections]
    if len(numbers) != len(set(numbers)):
        raise ValueError('Duplicate section numbers')
    coverage = json.loads((root / 'slides/coverage.json').read_text())
    missing = set(coverage['sections']) - set(numbers)
    extra = set(numbers) - set(coverage['sections'])
    if missing or extra:
        raise ValueError(f'Course coverage differs from the plan: missing {sorted(missing)}, extra {sorted(extra)}')
    (root / 'slides').mkdir(exist_ok=True)
    for section in sections:
        chapter = int(section['number'].split('.')[0])
        if args.chapters is None or chapter in args.chapters:
            build_section(root, cfg, section)
    build_index(root, cfg, sections)

