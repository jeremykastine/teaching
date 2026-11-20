#!/usr/bin/env python3
"""Verify practice packets, source mathematics, coverage, bookmarks, and links."""
import argparse
import json
from pathlib import Path

import fitz
from bs4 import BeautifulSoup
from build_math101_practice_bundles import SOURCE
from build_tsm_practice_bundles import fingerprint
from export_assessment_batches import improve
from assessment_content import math101_solving
from generate_practice_batch import ASSESSMENTS
import verify_assessment_batches as V

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '101/practice-tests'
QA = ROOT / 'tmp/math101-practice-qa'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--render', action='store_true')
    args = parser.parse_args()
    QA.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((OUT / 'manifest.json').read_text())
    expected = {slug: fn for course, slug, _, fn, _ in ASSESSMENTS if course == 'MATH 101'}
    assert len(manifest) == 5 and {e['assessment'] for e in manifest} == set(expected)
    V.OUT, V.QA = OUT, QA
    report = []
    for entry in manifest:
        slug = entry['assessment']
        result = V.audit(entry, args.render, 5, official_finals=False)
        source = json.loads((SOURCE / f'{slug}-20-versions.json').read_text())
        originals = {fingerprint(r['questions']) for r in source}
        by_version = {}
        for r in source:
            v = r['constructor_variant']
            regenerated = improve(expected[slug](v), slug, v)
            if slug.endswith('final'):
                regenerated = [math101_solving(v, r['seed']) if q['id'] == 'M101-solving' else q
                               for q in regenerated]
            # Re-run the symbolic constructors and equation/graph checks, then
            # compare complete questions and keys, not only their display text.
            regenerated = json.loads(json.dumps(regenerated))
            assert {q['id']: q for q in regenerated} == {q['id']: q for q in r['questions']}
            by_version[r['version']] = {q['id']: q for q in r['questions']}
        records = json.loads((OUT / entry['file']).with_suffix('.json').read_text())
        with fitz.open(OUT / entry['file']) as pdf:
            bookmarks = [item for item in pdf.get_toc() if item[0] == 1]
        assert len(bookmarks) == 5
        for i, r in enumerate(records):
            assert fingerprint(r['questions']) == r['content_fingerprint'] not in originals
            assert set(q['id'] for q in r['questions']) == set(by_version[source[0]['version']])
            for q in r['questions']:
                assert q == by_version[r['source_question_versions'][q['id']]][q['id']]
                assert not any(ord(c) < 32 for text in q['math'] + [row['answer'] for row in q['rows']] for c in text)
                assert 'remainder theorem' not in q['prompt'].lower() and 'descartes' not in q['prompt'].lower()
            assert bookmarks[i][2] == r['start'] + 1 and r['version'] in bookmarks[i][1]
        result['mathematics'] = 'symbolic constructors and saved source keys verified'
        report.append(result)
        print(json.dumps(result), flush=True)
    path = ROOT / '101/practice-tests.html'
    page = BeautifulSoup(path.read_text(), 'html.parser')
    links = [a['href'] for a in page.select('a[href]') if a['href'].endswith('.pdf')]
    assert len(links) == 5
    assert all((path.parent / href).is_file() and '-practice-5-versions.pdf' in href for href in links)
    assert 'five practice versions' in page.get_text().lower()
    assert '101/practice-tests.html' in (ROOT / 'index.html').read_text()
    (QA / 'verification.json').write_text(json.dumps(report, indent=2) + '\n')
    print('Verified five MATH 101 bundles, 25 versions, mathematics, PDF layout, and index links.')


if __name__ == '__main__':
    main()
