#!/usr/bin/env python3
"""Build and validate four public statistics question banks; refresh course links."""
import hashlib
import json
import random
import re
import sys
from collections import Counter
from html import escape
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, KeepTogether, PageBreak, Image,
    Table, TableStyle,
)
import fitz

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / 'stats'
OUT = COURSE / 'question-banks'
TITLES = {
    1: 'Collecting and describing data',
    2: 'Probability and discrete models',
    3: 'Continuous probability models',
    4: 'Sampling distributions and estimation',
}
REASONING = {'interpret', 'evaluate', 'compare', 'predict', 'calculate'}
INK = '#14232d'
ACCENT = '#185f72'
FONT = Path('/usr/share/fonts/truetype/dejavu')
pdfmetrics.registerFont(TTFont('BankSans', str(FONT / 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('BankBold', str(FONT / 'DejaVuSans-Bold.ttf')))

# Supplemental figures preserve the data stated in the question. Every question
# remains self-contained in text, including when a figure is unavailable.
FIGURES = {
    'U1-008': {'kind': 'dots', 'data': [2, 2, 2, 2, 2, 8], 'xlabel': 'Library visits',
               'alt': 'Five dots at 2 visits and one dot at 8 visits.'},
    'U1-045': {'kind': 'hist', 'edges': [0, 5, 10, 15], 'counts': [3, 7, 2],
               'xlabel': 'Duration (seconds)', 'alt': 'Histogram: [0,5) has 3; [5,10) has 7; [10,15) has 2.'},
    'U1-056': {'kind': 'box', 'summaries': [[0, 2, 3, 4, 20]], 'labels': ['Data'],
               'alt': 'Basic box plot: minimum 0, Q1 2, median 3, Q3 4, maximum 20. Whiskers show min and max.'},
    'U1-091': {'kind': 'box', 'summaries': [[5, 10, 12, 14, 20], [0, 5, 9, 13, 25]], 'labels': ['A', 'B'],
               'alt': 'Basic box plots: A has median 12 and IQR 4; B has median 9 and IQR 8. Whiskers show min and max.'},
    'U2-021': {'kind': 'venn', 'regions': [30, 10, 15, 0], 'labels': ['Laptop', 'Tablet'],
               'alt': 'Venn regions: 30 laptop only, 10 both, 15 tablet only. The illustrated universe is the 55 users of either device.'},
    'U2-036': {'kind': 'tree', 'branches': [0.6, 0.5],
               'alt': 'A proposed tree node has two exhaustive outgoing branches labeled 0.6 and 0.5.'},
    'U2-045': {'kind': 'prob', 'values': [0, 1, 2], 'probabilities': [0.2, 0.5, 0.3],
               'alt': 'Probability bars: P(0)=0.2, P(1)=0.5, P(2)=0.3.'},
    'U2-054': {'kind': 'prob_compare', 'alt': 'Game A has payout 5 with probability 1; Game B has payouts 0 and 10 with probability 0.5 each.'},
    'U3-001': {'kind': 'rectangle', 'low': 0, 'high': 0.5, 'height': 2,
               'alt': 'A rectangular density has height 2 from 0 to 0.5 and is zero outside.'},
    'U3-011': {'kind': 'uniform', 'low': 0, 'high': 10, 'intervals': [[1, 3], [7, 9]],
               'alt': 'A uniform density on 0 to 10 highlights intervals 1 to 3 and 7 to 9.'},
    'U3-031': {'kind': 'exponential', 'rate': 0.2, 'intervals': [[0, 1], [5, 6]],
               'alt': 'A declining exponential density highlights 0 to 1 minute and 5 to 6 minutes.'},
    'U3-052': {'kind': 'normals', 'models': [[50, 2, 'A: SD 2'], [50, 8, 'B: SD 8']], 'cutoff': 60,
               'alt': 'Two normal densities centered at 50, with standard deviations 2 and 8; cutoff 60 is marked.'},
    'U3-100': {'kind': 'normal_interval', 'mean': 500, 'sd': 20, 'limits': [490, 520],
               'alt': 'A normal density with vertical boundary lines at 490 and 520; no area is preselected.'},
    'U4-017': {'kind': 'sampling_curves', 'alt': 'Two normal densities centered at the same mean: one observation is wider, and a mean of 100 is narrower. A common cutoff above the mean is marked.'},
    'U4-052': {'kind': 'interval', 'low': 10, 'high': 14, 'center': 12,
               'alt': 'Interval from 10 to 14 with its center marked at 12.'},
    'U4-059': {'kind': 'interval', 'low': 10, 'high': 14, 'center': 12, 'claim': 12,
               'alt': 'Interval 10 to 14 and proposed mean 12 marked at the center.'},
    'U4-087': {'kind': 'interval', 'low': 0.3, 'high': 0.42, 'center': 0.36, 'claim': 0.5,
               'alt': 'A proportion interval 0.30 to 0.42 with proposed value 0.50 to its right.'},
}


def text_html(text):
    return escape(text).replace('&lt;=', '&#8804;').replace('&gt;=', '&#8805;')


def load_slides():
    slides, hashes = {}, {}
    for n in range(1, 9):
        path = COURSE / f'slides/source/chapter-{n:02}.json'
        hashes[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
        for section in json.loads(path.read_text()):
            slides[section['number']] = section
    return slides, hashes


def parse_bank(unit, slides, hashes):
    questions, groups = [], []
    for line in (OUT / f'source/unit-{unit}.txt').read_text().splitlines():
        if not line.strip():
            continue
        if line.startswith('@ '):
            groups.append({'id': f'U{unit}-G{len(groups)+1:02}', 'name': line[2:]})
            continue
        fields = line.split('|')
        if len(fields) != 8:
            raise ValueError(f'Expected 8 fields: {line}')
        ref, tag, stem, correct, d1, d2, d3, explanation = fields
        section, page = ref.split(':')
        page = int(page)
        assert tag in REASONING
        assert int(section.split('.')[0]) in (2*unit-1, 2*unit)
        assert section not in ('1.5', '1.6')
        assert 1 <= page <= len(slides[section]['slides'])
        assert len(set([correct, d1, d2, d3])) == 4
        assert all([stem, correct, d1, d2, d3, explanation])
        qid = f'U{unit}-{len(questions)+1:03}'
        questions.append({
            'id': qid, 'group': groups[-1]['id'], 'skill_group': groups[-1]['name'],
            'reasoning': tag, 'stem': stem, '_correct': correct,
            '_distractors': [d1, d2, d3], 'explanation': explanation,
            'source': {
                'section': section, 'slide_page': page,
                'slide_title': slides[section]['slides'][page-1]['title'],
                'pdf': f'../slides/section-{section.replace(".", "-")}.pdf#page={page}',
            },
        })
    assert len(questions) == 100 and len(groups) == 10
    assert len(set(q['stem'] for q in questions)) == 100
    assert set(Counter(q['group'] for q in questions).values()) == {10}
    answer_positions = list(range(4))*25
    random.Random(1012+unit).shuffle(answer_positions)
    for q, pos in zip(questions, answer_positions):
        distractors = q.pop('_distractors')
        random.Random(q['id']).shuffle(distractors)
        correct = q.pop('_correct')
        distractors.insert(pos, correct)
        q['choices'] = distractors
        q['answer_index'] = pos
        q['answer_letter'] = 'ABCD'[pos]
        if q['id'] in FIGURES:
            spec = FIGURES[q['id']]
            q['figure'] = {'file': f'figures/{q["id"]}.svg', 'alt': spec['alt'], 'data': spec}
    return {
        'schema_version': 1, 'unit': unit, 'title': TITLES[unit],
        'chapters': [2*unit-1, 2*unit], 'question_count': 100,
        'calculator': 'Four-function calculator allowed; supplied nontrivial values.',
        'study_note': 'All questions, answers, and explanations are public. Numerical examples are illustrative classroom scenarios.',
        'groups': groups, 'questions': questions,
        'alignment': {'basis': 'Existing section slides, original adapted questions; computational load intentionally reduced.',
                      'source_sha256': {p: h for p, h in hashes.items() if any(f'chapter-{n:02}' in p for n in [2*unit-1, 2*unit])}},
    }


def make_figure(q):
    spec = q['figure']['data']
    fig, ax = plt.subplots(figsize=(5.8, 1.75))
    kind = spec['kind']
    if kind == 'dots':
        counts = Counter()
        for x in spec['data']:
            counts[x] += 1
            ax.scatter(x, counts[x], color=ACCENT, s=36)
        ax.set(xlim=(0, 10), ylim=(0, 6), xlabel=spec['xlabel'], yticks=[])
    elif kind == 'hist':
        edges, counts = spec['edges'], spec['counts']
        ax.bar(edges[:-1], counts, width=np.diff(edges), align='edge', color='#b7d3da', edgecolor=INK)
        for x, w, y in zip(edges[:-1], np.diff(edges), counts):
            ax.text(x+w/2, y+.15, str(y), ha='center')
        ax.set(xlabel=spec['xlabel'], ylabel='Count', xticks=edges, ylim=(0, max(counts)+1.5))
    elif kind == 'box':
        stats = [dict(whislo=a, q1=b, med=c, q3=d, whishi=e, fliers=[])
                 for a, b, c, d, e in spec['summaries']]
        ax.bxp(stats, vert=False, showfliers=False, patch_artist=True,
               boxprops={'facecolor': '#b7d3da'}, medianprops={'color': ACCENT, 'linewidth': 2})
        ax.set_yticks(range(1, len(stats)+1), spec['labels'])
        ax.set_xlabel('Value (whiskers show minimum and maximum)')
    elif kind == 'venn':
        from matplotlib.patches import Circle
        ax.add_patch(Circle((1.5, 1), .85, fill=False, ec=ACCENT))
        ax.add_patch(Circle((2.5, 1), .85, fill=False, ec=ACCENT))
        for x, t in [(1.15, '30'), (2, '10'), (2.85, '15')]:
            ax.text(x, 1, t, ha='center')
        ax.text(1.3, 1.95, 'Laptop', ha='center')
        ax.text(2.7, 1.95, 'Tablet', ha='center')
        ax.set(xlim=(0, 4), ylim=(0, 2.2))
        ax.axis('off')
    elif kind == 'tree':
        ax.plot([0, 1], [.5, .8], color=ACCENT)
        ax.plot([0, 1], [.5, .2], color=ACCENT)
        ax.text(.55, .77, '0.6')
        ax.text(.55, .22, '0.5')
        ax.text(1.1, .8, 'Outcome A', va='center')
        ax.text(1.1, .2, 'Outcome B', va='center')
        ax.set(xlim=(-.1, 2), ylim=(0, 1))
        ax.axis('off')
    elif kind == 'prob':
        ax.bar(spec['values'], spec['probabilities'], width=.5, color='#b7d3da', edgecolor=INK)
        ax.set(xlabel='X', ylabel='Probability', xticks=spec['values'], ylim=(0, .65))
        for x, y in zip(spec['values'], spec['probabilities']):
            ax.text(x, y+.02, str(y), ha='center')
    elif kind == 'prob_compare':
        ax.scatter([5], [1], label='Game A', color=ACCENT, s=60)
        ax.scatter([0, 10], [.5, .5], label='Game B', marker='s', color='#ad5c25', s=45)
        ax.vlines([0, 10], [0, 0], [.5, .5], color='#ad5c25')
        ax.vlines([5], [0], [1], color=ACCENT)
        ax.set(xlabel='Payout', ylabel='Probability', xticks=[0, 5, 10], ylim=(0, 1.15))
        ax.legend(loc='upper right', fontsize=8)
    elif kind in ('rectangle', 'uniform'):
        low, high = spec['low'], spec['high']
        height = spec.get('height', 1/(high-low))
        margin = (high-low)*.2
        ax.plot([low-margin, low, low, high, high, high+margin], [0, 0, height, height, 0, 0], color=ACCENT)
        for a, b in spec.get('intervals', []):
            ax.fill_between([a, b], [height, height], color='#b7d3da', alpha=.7)
        ax.set(xlabel='Value', ylabel='Density', ylim=(0, height*1.3), xticks=sorted(set([low, high]+[x for pair in spec.get('intervals', []) for x in pair])))
    elif kind == 'exponential':
        x = np.linspace(0, 15, 400)
        y = spec['rate']*np.exp(-spec['rate']*x)
        ax.plot(x, y, color=ACCENT)
        for a, b in spec['intervals']:
            xs = np.linspace(a, b, 40)
            ax.fill_between(xs, spec['rate']*np.exp(-spec['rate']*xs), color='#b7d3da')
        ax.set(xlabel='Wait (minutes)', ylabel='Density', ylim=(0, .25))
    elif kind in ('normals', 'normal_interval', 'sampling_curves'):
        if kind == 'normals':
            models = spec['models']
            cutoffs = [spec['cutoff']]
        elif kind == 'normal_interval':
            models = [[spec['mean'], spec['sd'], 'One package']]
            cutoffs = spec['limits']
        else:
            models = [[0, 4, 'One observation'], [0, .4, 'Mean of 100']]
            cutoffs = [2]
        low = min(m-3.2*s for m, s, _ in models)
        high = max(m+3.2*s for m, s, _ in models)
        x = np.linspace(low, high, 800)
        for m, s, label in models:
            y = np.exp(-.5*((x-m)/s)**2)/(s*np.sqrt(2*np.pi))
            ax.plot(x, y, label=label)
        for cut in cutoffs:
            ax.axvline(cut, color=INK, linestyle='--', linewidth=.8)
        ax.set(xlabel='Distance above/below population mean (g)' if kind == 'sampling_curves' else 'Value', ylabel='Density', ylim=(0, None))
        ax.legend(loc='upper right', fontsize=8)
    elif kind == 'interval':
        low, high, center = spec['low'], spec['high'], spec['center']
        width = high-low
        ax.plot([low, high], [.5, .5], color=ACCENT, linewidth=3)
        ax.plot([low, low, high, high], [.4, .6, .6, .4], linestyle='None', marker='|', color=ACCENT)
        ax.scatter(center, .5, color=ACCENT, zorder=3)
        if 'claim' in spec:
            ax.scatter(spec['claim'], .2, color='#ad5c25', marker='x', s=40)
            ax.text(spec['claim'], .1, 'Proposed value', ha='center', fontsize=8)
        ticks = sorted(set([low, center, high]+([spec['claim']] if 'claim' in spec else [])))
        ax.set(xticks=ticks, yticks=[], ylim=(0, 1), xlim=(low-width*.25, max(high, spec.get('claim', high))+width*.4))
        for spine in ['left', 'right', 'top']:
            ax.spines[spine].set_visible(False)
    else:
        raise ValueError(kind)
    for spine in ['right', 'top']:
        ax.spines[spine].set_visible(False)
    ax.tick_params(labelsize=8)
    fig.tight_layout(pad=.6)
    path = OUT / q['figure']['file']
    fig.savefig(path, format='svg')
    path.write_text('\n'.join(line.rstrip() for line in path.read_text().splitlines())+'\n')
    fig.savefig(path.with_suffix('.png'), dpi=220)
    plt.close(fig)


STYLES = {
    'title': ParagraphStyle('title', fontName='BankBold', fontSize=21, leading=25, textColor=colors.HexColor(INK), spaceAfter=10),
    'subtitle': ParagraphStyle('subtitle', fontName='BankBold', fontSize=13, leading=17, textColor=colors.HexColor(ACCENT), spaceAfter=8),
    'body': ParagraphStyle('body', fontName='BankSans', fontSize=9.5, leading=13, spaceAfter=7),
    'group': ParagraphStyle('group', fontName='BankBold', fontSize=12, leading=16, textColor=colors.HexColor(ACCENT), spaceBefore=10, spaceAfter=8, keepWithNext=True),
    'stem': ParagraphStyle('stem', fontName='BankSans', fontSize=10, leading=13.2, spaceAfter=5),
    'option': ParagraphStyle('option', fontName='BankSans', fontSize=9.5, leading=12.5, leftIndent=12),
    'source': ParagraphStyle('source', fontName='BankSans', fontSize=7.5, leading=10, textColor=colors.HexColor('#52616b'), spaceBefore=4, spaceAfter=9),
    'keyanswer': ParagraphStyle('keyanswer', fontName='BankSans', fontSize=9.5, leading=12.5, spaceAfter=3),
    'key': ParagraphStyle('key', fontName='BankSans', fontSize=9.2, leading=12.3, spaceAfter=6),
}


def p(text, style='body'):
    return Paragraph(text_html(text), STYLES[style])


def pdf_header(canvas, doc):
    canvas.saveState()
    canvas.setFont('BankSans', 8)
    canvas.setFillColor(colors.HexColor('#52616b'))
    canvas.drawString(42, 767, f'MSC 201 Statistics | Unit {doc.bank_unit} | Public study bank')
    canvas.drawRightString(570, 767, 'Jeremy Kastine')
    canvas.setStrokeColor(colors.HexColor('#c7d2d7'))
    canvas.line(42, 758, 570, 758)
    canvas.drawString(42, 24, 'Illustrative classroom scenarios | Four-function calculator allowed')
    canvas.drawRightString(570, 24, f'Page {doc.page}')
    canvas.restoreState()


def render_pdf(bank, output_path):
    unit = bank['unit']
    # Explicit instructor exports must use a destination outside the published site.
    path = Path(output_path)
    if path.resolve().is_relative_to(ROOT):
        raise ValueError('Write instructor PDF exports outside the published Teaching repository.')
    doc = SimpleDocTemplate(str(path), pagesize=(612, 792), leftMargin=42, rightMargin=42,
                            topMargin=45, bottomMargin=42,
                            title=f'Statistics Unit {unit}: {bank["title"]} - 100 questions', author='Jeremy Kastine')
    doc.bank_unit = unit
    story = [p(f'Statistics - Unit {unit}', 'title'), p(bank['title'], 'subtitle'),
             p(f'Chapters {bank["chapters"][0]}-{bank["chapters"][1]} | 100 multiple-choice questions'),
             p('Choose one answer per question. These questions emphasize interpretation, prediction, and statistical reasoning. A four-function calculator is sufficient; any other required values are supplied. All numerical scenarios are illustrative. Chapter 9 is not tested.'),
             p('Answers and brief explanations appear after Question 100. Each question cites the matching section-slide page.')]
    last_group = None
    for q in bank['questions']:
        block = []
        if q['group'] != last_group:
            block.append(p(f'{q["group"]}: {q["skill_group"]}', 'group'))
            last_group = q['group']
        block.append(p(f'{q["id"]}. {q["stem"]}', 'stem'))
        if 'figure' in q:
            png = OUT / q['figure']['file'].replace('.svg', '.png')
            block.append(Image(str(png), width=390, height=118))
        for letter, choice in zip('ABCD', q['choices']):
            block.append(p(f'{letter}. {choice}', 'option'))
        src = q['source']
        block.append(p(f'Slides {src["section"]}, page {src["slide_page"]}: {src["slide_title"]} | {q["reasoning"]}', 'source'))
        story.append(KeepTogether(block))
    story += [PageBreak(), p('Answers and explanations', 'title'), p('Public study key. Explain the statistical reason as well as selecting the letter.')]
    last_group = None
    for q in bank['questions']:
        block = []
        if q['group'] != last_group:
            block.append(p(q['skill_group'], 'group'))
            last_group = q['group']
        answer = q['choices'][q['answer_index']]
        block.extend([p(f'{q["id"]} - {q["answer_letter"]}. {answer}', 'keyanswer'), p(q['explanation'], 'key')])
        story.append(KeepTogether(block))
    doc.build(story, onFirstPage=pdf_header, onLaterPages=pdf_header)
    return path


CSS = '''
:root{--ink:#14232d;--accent:#185f72;--muted:#52616b}*{box-sizing:border-box}
body{margin:0;color:var(--ink);background:#f5f7f8;font:17px/1.6 system-ui,sans-serif}
main{max-width:920px;margin:auto;padding:42px 24px}h1{line-height:1.15;font-size:2.3rem;margin:18px 0}
h2{font-size:1.35rem;margin:36px 0 12px}a{color:var(--accent);text-underline-offset:3px}
.links{display:flex;gap:16px;flex-wrap:wrap}.question{background:white;border:1px solid #c7d2d7;border-radius:8px;padding:20px;margin:14px 0}
.question h3{font-size:1.08rem;line-height:1.55;margin:0 0 10px}.meta{color:var(--muted);font-size:.82rem}
ol.choices{padding-left:2em;margin:10px 0}ol.choices li{padding-left:.25em;margin:5px 0}
details{border-top:1px solid #dbe3e6;margin-top:12px;padding-top:10px}summary{cursor:pointer;color:var(--accent);font-weight:650}
details p{margin:8px 0}img{display:block;width:min(100%,650px);height:auto;margin:12px auto}
label{font-weight:600}select,input,button{font:inherit;padding:7px;border:1px solid #9aadb5;border-radius:4px}
.controls{display:flex;flex-wrap:wrap;gap:16px;align-items:center}.controls select{max-width:100%;min-width:0}.prompt{background:#eaf2f4;padding:18px;border-radius:6px}
.question[hidden],section[hidden]{display:none}a:focus-visible,summary:focus-visible,button:focus-visible{outline:3px solid #b05819;outline-offset:3px}

.bank-answer{margin-top:16px;padding:12px 16px;background:#edf4f5;border-left:4px solid var(--accent)}.bank-answer p{margin:5px 0}
.bank-list{list-style:none;padding:0}.bank-list>li{border-top:1px solid #c7d2d7;padding:10px 0 24px}
fieldset{border:0;padding:0;margin:0;min-width:0}legend{font-size:1.08rem;font-weight:650;line-height:1.55;padding:0;width:100%;overflow-wrap:anywhere}
.test-choice{display:flex;gap:12px;align-items:flex-start;padding:11px 12px;margin:8px 0;border:1px solid #dbe3e6;border-radius:5px;font-weight:400;cursor:pointer}
.test-choice:has(input:checked){border-color:var(--accent);background:#edf4f5}.test-choice input{flex-shrink:0;width:18px;height:18px;margin:4px 0 0}.test-choice span{min-width:0;overflow-wrap:anywhere}
button{min-height:44px;cursor:pointer}button.primary{background:var(--accent);color:white;font-weight:650}button:disabled{opacity:.6;cursor:default}
.feedback{border-left:4px solid #9aadb5;background:#f4f6f7;padding:12px 16px;margin-top:18px}.feedback.correct{border-color:#287245}.feedback.incorrect{border-color:#ad4f25}.feedback p{margin:6px 0}
.callout{border-left:4px solid var(--accent);background:#edf4f5;padding:15px 18px}.pool-list{margin-top:30px}.pool-list li{margin:8px 0}
[hidden]{display:none!important}#copy-link-text{display:block;width:100%;margin:8px 0;min-width:0}.question{scroll-margin-top:20px}
@media(max-width:520px){main{padding:28px 16px}h1{font-size:1.9rem}.question{padding:16px}.links{gap:12px}.controls{align-items:stretch}.controls select{width:100%}}
@media print{body{background:white;font-size:10pt}main{max-width:none;padding:0}.controls,.prompt{display:none}.question{break-inside:avoid;border-radius:0}img{width:380px}h1{font-size:20pt}}
'''


def render_html(bank):
    unit = bank['unit']
    chunks = []
    for number, group in enumerate(bank['groups'], 1):
        questions = []
        for q in bank['questions']:
            if q['group'] != group['id']:
                continue
            choices = ''.join(f'<li>{text_html(c)}</li>' for c in q['choices'])
            figure = ''
            if 'figure' in q:
                figure = f'<img src="{q["figure"]["file"]}" alt="{escape(q["figure"]["alt"], quote=True)}" loading="lazy">'
            src = q['source']
            questions.append(f'''<article class="question" id="{q['id']}" data-group="{q['group']}">
<h3>{q['id']}. {text_html(q['stem'])}</h3>{figure}<ol class="choices" type="A">{choices}</ol>
<div class="bank-answer"><p><strong>Answer: {q['answer_letter']}. {text_html(q['choices'][q['answer_index']])}</strong></p><p>{text_html(q['explanation'])}</p></div>
<p class="meta"><a href="{src['pdf']}">Slides {src['section']}, page {src['slide_page']}: {escape(src['slide_title'])}</a></p></article>''')
        chunks.append(f'<section id="{group["id"]}" data-group="{group["id"]}"><h2>Pool {number}: {escape(group["name"])}</h2>{"".join(questions)}</section>')
    options = ''.join(f'<option value="{g["id"]}">Pool {i}: {escape(g["name"])}</option>' for i, g in enumerate(bank['groups'], 1))
    html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Statistics Unit {unit}: complete bank with answers</title><meta name="description" content="All 100 statistics questions, each immediately followed by its answer and explanation."><style>{CSS}</style></head>
<body><main><p><a href="../../index.html#stats">Teaching</a> / <a href="index.html">Test banks and answer keys</a></p>
<h1>Unit {unit}: {escape(bank['title'])}</h1><p>Complete bank · Chapters {bank['chapters'][0]}-{bank['chapters'][1]} · 100 questions · Ten topic pools</p>
<p>Read each question and its choices, followed immediately by the correct answer and explanation. A four-function calculator is sufficient. Chapter 9 is not tested.</p>
<p class="links"><a href="unit-{unit}-test-generator.html">Generate a 10-question practice test</a></p>
<div class="controls"><label for="group">Topic pool</label><select id="group"><option value="all">All ten pools (100 questions)</option>{options}</select><span id="count" class="meta" aria-live="polite">100 questions</span></div>
{''.join(chunks)}<footer><p>Original classroom adaptations aligned to the existing MSC 201 slides and OpenStax Introductory Statistics 2e. Numerical scenarios are illustrative.</p></footer></main>
<script>
const group=document.getElementById('group');
function filterPools(){{let n=0;document.querySelectorAll('section[data-group]').forEach(s=>{{s.hidden=group.value!=='all'&&s.dataset.group!==group.value;if(!s.hidden)n+=s.querySelectorAll('.question').length;}});document.getElementById('count').textContent=n+' questions';}}
group.addEventListener('change',filterPools);
// A link to a particular question must reveal its pool, even after filtering.
function showLinkedQuestion(){{if(location.hash){{group.value='all';filterPools();}}}}
window.addEventListener('hashchange',showLinkedQuestion);showLinkedQuestion();
</script></body></html>'''
    (OUT / f'unit-{unit}-question-bank.html').write_text(html)


def render_generator(bank):
    unit = bank['unit']
    # Embedded data also permits local/offline use without fetching a JSON file.
    data = json.dumps({k: bank[k] for k in ('unit', 'groups', 'questions')}, ensure_ascii=False)
    data = data.replace('<', r'\u003c').replace('>', r'\u003e').replace('&', r'\u0026')
    pools = ''.join(f'<li>{escape(g["name"])} ({sum(q["group"] == g["id"] for q in bank["questions"])} questions)</li>' for g in bank['groups'])
    (OUT / f'unit-{unit}-test-generator.html').write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Statistics Unit {unit}: practice test generator</title><style>{CSS}</style><script defer src="test-generator.js"></script></head>
<body><main><p><a href="../../index.html#stats">Teaching</a> / <a href="index.html">Test banks and answer keys</a></p>
<h1>Unit {unit}: practice test generator</h1><p>{escape(bank['title'])} · Chapters {bank['chapters'][0]}-{bank['chapters'][1]}</p>
<p>Each test draws one question from each of the ten topic pools, then shuffles the questions and answer choices. Choose your answers and select <strong>Check answers</strong> for your score and explanations. Generate another test whenever you want more practice. A four-function calculator is allowed.</p>
<p><a href="unit-{unit}-question-bank.html">Read the complete bank with answers</a></p>
<noscript><p class="callout">Enable JavaScript to generate a test, or use the complete bank above.</p></noscript>
<div class="controls"><button id="generate-test" type="button" class="primary" disabled>Generate new test</button><button id="copy-link" type="button" disabled>Copy test link</button></div>
<p id="generator-status" class="meta" role="status" aria-live="polite"></p>
<div id="copy-fallback" hidden><label for="copy-link-text">Copy this test link manually</label><input id="copy-link-text" type="text" readonly></div>
<div id="test-content" hidden><p class="meta"><span id="test-version"></span> · <a id="test-link">Reopen this test</a></p>
<div id="test-questions"></div><button id="check-answers" type="button" class="primary" disabled>Check answers</button>
<p id="test-result" class="callout" role="status" tabindex="-1" hidden></p></div>
<details class="pool-list"><summary>Topics included in every test</summary><ol>{pools}</ol></details>
</main><script id="bank-data" type="application/json">{data}</script></body></html>''')


def build_overview(banks):
    manifest, rows, units = [], [], []
    for b in banks:
        n = b['unit']
        rows.append(f'<li><h2>Unit {n}: {escape(b["title"])}</h2><p>Chapters {b["chapters"][0]}-{b["chapters"][1]} · 100 questions · Ten pools</p><p class="links"><a href="unit-{n}-question-bank.html">Complete bank with answers (HTML)</a><a href="unit-{n}-test-generator.html">10-question test generator (HTML)</a></p></li>')
        manifest.append({'unit': n, 'title': b['title'], 'chapters': b['chapters'],
                         'question_count': 100, 'html': f'unit-{n}-question-bank.html',
                         'generator': f'unit-{n}-test-generator.html', 'json': f'unit-{n}-question-bank.json',
                         'pool_count': 10, 'questions_per_test': 10})
        units.append({'unit': n, 'pools': [{'id': g['id'], 'name': g['name'],
                       'question_ids': [q['id'] for q in b['questions'] if q['group'] == g['id']]}
                      for g in b['groups']]})
    blueprint_path = OUT / 'source/test-blueprint.json'
    existing_policy = json.loads(blueprint_path.read_text()) if blueprint_path.exists() else {}
    blueprint_path.write_text(json.dumps({
        **existing_policy,
        'generator_version': 1, 'questions_per_test': 10, 'questions_per_pool': 1,
        'sampling': 'Choose one question independently from each of ten topic pools, then shuffle the selected questions and their answer choices.',
        'scope': 'Chapters 1-8; Chapter 9 is not tested. Use the same pool coverage for instructor-requested printable tests.',
        'publication': 'Two student HTML options per unit. Printed assessment PDFs are produced separately on instructor request, not published by this builder.',
        'units': units}, indent=2)+'\n')
    (OUT / 'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    (OUT / 'index.html').write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Statistics test banks and practice generators</title><style>{CSS}</style></head><body><main><p><a href="../../index.html#stats">Teaching · Statistics</a> / <a href="../excel-competency-checks.html">Excel competency checks</a></p><h1>Statistics test banks</h1><p>Choose either the complete bank, with an answer and explanation after every question, or a generator that creates a fresh 10-question practice test. Every generated test includes one question from each of ten topic pools, in random order.</p><p>A four-function calculator is sufficient. Chapter 9 is not tested.</p><ul class="bank-list">{''.join(rows)}</ul></main></body></html>''')


def refresh_index():
    sys.path.insert(0, str(ROOT / 'scripts'))
    from slide_builder import build_index, COURSES
    sections = []
    for path in sorted((COURSE / 'slides/source').glob('chapter-*.json')):
        sections.extend(json.loads(path.read_text()))
    build_index(COURSE, COURSES['stats'], sections)


def validate_pdf(path, bank):
    pdf = fitz.open(path)
    text = '\n'.join(page.get_text() for page in pdf)
    assert 'Answers and explanations' in text
    for q in bank['questions']:
        assert len(re.findall(re.escape(q['id'])+r'\b', text)) == 2, f'Missing/duplicated PDF item {q["id"]}'
    boxes_checked = 0
    for page in pdf:
        for x0, y0, x1, y1, line, *_ in page.get_text('blocks'):
            assert x0 >= 40 and x1 <= 574 and y0 >= 10 and y1 <= 780, (path, page.number+1, line)
            boxes_checked += 1
    pages = len(pdf)
    pdf.close()
    return {'pages': pages, 'text_blocks_within_bounds': boxes_checked}


def main():
    OUT.mkdir(exist_ok=True)
    (OUT / 'figures').mkdir(exist_ok=True)
    slides, hashes = load_slides()
    banks, report = [], []
    for n in range(1, 5):
        bank = parse_bank(n, slides, hashes)
        for q in bank['questions']:
            if 'figure' in q:
                make_figure(q)
        (OUT / f'unit-{n}-question-bank.json').write_text(json.dumps(bank, indent=2, ensure_ascii=False)+'\n')
        render_html(bank)
        render_generator(bank)
        report.append({'unit': n, 'questions': 100, 'groups': 10,
                       'reasoning_counts': dict(Counter(q['reasoning'] for q in bank['questions'])),
                       'answer_letter_counts': dict(Counter(q['answer_letter'] for q in bank['questions'])),
                       'section_counts': dict(Counter(q['source']['section'] for q in bank['questions'])),
                       'html_questions_with_visible_answers': len(bank['questions']),
                       'pool_sizes': dict(Counter(q['group'] for q in bank['questions']))})
        banks.append(bank)
    assert len(set(q['stem'] for bank in banks for q in bank['questions'])) == 400
    build_overview(banks)
    refresh_index()
    (OUT / 'source/build-report.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
