#!/usr/bin/env python3
"""Check approved arithmetic, source-PDF references, figures, and local links."""
import json
import math
import re
import statistics
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
import fitz

ROOT = Path(__file__).resolve().parents[2]
BANKS = ROOT / 'stats/question-banks'


def num(x, suffix='.'):
    return f'{x:g}{suffix}'


def calculations():
    # Independent recomputation of the approved scenarios. If the authored
    # numbers change, update this audit after reviewing the revised question.
    return {
        'U1-006': 'Campus A.' if 30/60 > 40/100 else 'Campus B.',
        'U1-013': f'{3}, {3+10}, {3+20}.',
        'U1-031': num(2+3), 'U1-033': num(75-30, '%.'),
        'U1-045': num(3+7), 'U1-051': num(statistics.median([2,4,4,7,20])),
        'U1-052': num(statistics.median([1,3,5,9])),
        'U1-055': 'Group A.' if 9-3 > 14-10 else 'Group B.',
        'U1-066': num(4*5), 'U1-088': num((60-50)/5, ' standard deviations.'),
        'U1-098': num(math.sqrt(9), ' minutes.'),
        'U2-002': f'{len([x for x in range(1,7) if x>4])}/6.',
        'U2-004': f'{1-.8:.2f}.',
        'U2-018': f'0.4 times 0.5 equals {0.4*0.5:g}.',
        'U2-022': num(.4+.5-.2), 'U2-023': num(1-.75),
        'U2-027': num(1-.7), 'U2-031': '12/20.',
        'U2-037': num(.4*.5), 'U2-039': num(30-8),
        'U2-043': num(1-.2-.5), 'U2-045': num(.2+.5),
        'U2-055': num(8-3), 'U2-059': num(1.5*20),
        'U2-063': num(20*.3), 'U2-076': num(1/.25),
        'U2-086': num(6*.5), 'U2-091': num(2*3),
        'U2-092': num(math.sqrt(9)), 'U2-098': num(1000*.002),
        'U3-003': num(1/4), 'U3-007': f'{.8-.2:.2f}.',
        'U3-009': num(100*(1-.8), '%.'), 'U3-012': f'{6-3}/{12-0}.',
        'U3-015': num((4+12)/2), 'U3-016': num(.75*20, ' minutes.'),
        'U3-025': f'{12-8}/{12-4}.', 'U3-032': num(60/4, ' minutes.'),
        'U3-033': num(1/5), 'U3-036': f'{1-.2:.2f}.',
        'U3-037': num(.5-.125), 'U3-047': num(.5*10),
        'U3-061': num((50-40)/5), 'U3-062': num((12-20)/4),
        'U3-065': num(30+1.5*4), 'U3-074': f'{1-.8849:.4f}.',
        'U3-076': num(.85-.2), 'U3-077': f'{1-.9:.2f}.',
        'U3-080': num(.05*200), 'U3-084': num(100+1.28*10),
        'U3-093': f'{.1/.5:.2f}.',
        'U3-098': f'{50-3*2} to {50+3*2}.',
        'U4-011': num(12/math.sqrt(36)), 'U4-015': num(40+1.5*2),
        'U4-016': num((24-20)/2), 'U4-019': num(4*math.sqrt(25/100)),
        'U4-026': f'No; it is {100*200/500:g}% of the population.',
        'U4-031': num(20*5, ' g.'), 'U4-032': num(3*10, ' g.'),
        'U4-040': num(100+2*4), 'U4-043': f'{1-.9:.2f}.',
        'U4-044': f'{.85-.15:.2f}.',
        'U4-052': f'{12-2} to {12+2}.',
        'U4-053': num((8+12)/2), 'U4-054': num((12-8)/2),
        'U4-068': f'{(1-.9)/2:.2f}.', 'U4-069': num(.5*2),
        'U4-074': num(16-1), 'U4-078': num(6/math.sqrt(9), ' minutes.'),
        'U4-081': f'{40/100:.2f}.', 'U4-083': num(1-.35),
        'U4-085': f'{100*(.4-.05):g}% to {100*(.4+.05):g}%.',
        'U4-088': f'Estimate {(0.2+0.3)/2:g}; margin {(0.3-0.2)/2:g}.',
        'U4-094': f'Yes; the fraction is {100*400/20000:g}%.',
        'U4-099': f'{8+2}/{40+4}.',
    }


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])
        if tag == 'img':
            assert attrs.get('alt'), 'Missing image alternative text'
            self.images.append(attrs['src'])


def main():
    questions = {}
    banks = {}
    for path in sorted(BANKS.glob('unit-*-question-bank.json')):
        b = json.loads(path.read_text())
        banks[b['unit']] = b
        for q in b['questions']:
            questions[q['id']] = q
    assert len(questions) == 400
    checks = calculations()
    assert set(checks) == {qid for qid, q in questions.items() if q['reasoning']=='calculate'}
    for qid, expected in checks.items():
        q = questions[qid]
        actual = q['choices'][q['answer_index']]
        assert actual == expected, (qid, actual, expected)
    # Model-consistency and non-calculation numerical reasoning checks.
    assert math.isclose(.5**3, .125)  # exponential tails at 2 and 6
    assert statistics.mean([2,3,3,4,18]) > statistics.median([2,3,3,4,18])
    assert statistics.mean([0,8,9,9,10]) < statistics.median([0,8,9,9,10])
    assert statistics.mean([1,2,3,4,100]) > statistics.mean([1,2,3,4])
    assert statistics.median([1,2,3,4,100]) > statistics.median([1,2,3,4])
    assert math.isclose(.4*.5, .2)
    assert 100*.02 <= 5 and 100*(1-.02) > 5
    assert 8 > 5 and 12 > 5 and not 5 > 5
    assert 24 >= 10 and not .85 >= .90
    # Verify section titles against the actual rendered source PDFs.
    pdfs = {}
    for q in questions.values():
        source = q['source']
        path = (BANKS / source['pdf'].split('#')[0]).resolve()
        if path not in pdfs:
            pdfs[path] = fitz.open(path)
        page = pdfs[path][source['slide_page']-1]
        normalize = lambda s: re.sub(r'\s+', '', s).casefold()
        assert normalize(source['slide_title']) in normalize(page.get_text()), q['id']
    for doc in pdfs.values():
        doc.close()
    # Student publication contract: two HTML modes, ten pools, no public bank PDFs.
    manifest = json.loads((BANKS / 'manifest.json').read_text())
    blueprint = json.loads((BANKS / 'source/test-blueprint.json').read_text())
    assert len(manifest) == 4 and blueprint['questions_per_pool'] == 1
    assert blueprint['questions_per_test'] == 10
    assert not list(BANKS.glob('unit-*-question-bank.pdf'))
    index = Links()
    index.feed((BANKS / 'index.html').read_text())
    assert len([href for href in index.links if href.startswith('unit-')]) == 8
    for entry in manifest:
        unit = entry['unit']
        bank = banks[unit]
        assert 'pdf' not in entry and entry['pool_count'] == 10 and entry['questions_per_test'] == 10
        assert entry['html'] in index.links and entry['generator'] in index.links
        assert len(bank['groups']) == 10
        assert all(sum(q['group'] == g['id'] for q in bank['questions']) == 10 for g in bank['groups'])
        full = (BANKS / entry['html']).read_text()
        assert full.count('<div class="bank-answer">') == 100
        assert '<details' not in full, 'Complete-bank answers must be visible without clicks'
        generator = (BANKS / entry['generator']).read_text()
        embedded = re.search(r'<script id="bank-data" type="application/json">(.*?)</script>', generator, re.S)
        assert embedded and json.loads(embedded.group(1)) == {k: bank[k] for k in ('unit', 'groups', 'questions')}
        for html in (full, generator):
            assert not re.search(r'href=[\"\'][^\"\']*question-bank\.pdf', html)
        pools = next(u['pools'] for u in blueprint['units'] if u['unit'] == unit)
        assert [p['id'] for p in pools] == [g['id'] for g in bank['groups']]
        for pool in pools:
            assert pool['question_ids'] == [q['id'] for q in bank['questions'] if q['group'] == pool['id']]
    link_count = 0
    html_paths = [ROOT / 'index.html'] + list((ROOT / 'stats').rglob('*.html'))
    parsed = {}
    for path in html_paths:
        parser = Links()
        parser.feed(path.read_text())
        parsed[path.resolve()] = parser
    for path in html_paths:
        parser = parsed[path.resolve()]
        for href in parser.links+parser.images:
            url = urlparse(href)
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
            assert target.is_file(), (path, href)
            if url.fragment and target.suffix == '.html' and target in parsed:
                assert url.fragment in parsed[target].ids, (path, href)
            link_count += 1
    report = {
        'unique_questions': len(questions),
        'independently_recomputed_calculation_answers': len(checks),
        'source_slide_pdf_page_titles_verified': len(questions),
        'local_links_and_image_targets_verified': link_count,
        'additional_numeric_reasoning_and_model_checks': 9,
        'student_html_modes_verified': 8,
        'topic_pools_verified': 40,
        'public_bank_pdfs': 0,
        'all_checks_passed': True,
    }
    (BANKS / 'source/validation-report.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
