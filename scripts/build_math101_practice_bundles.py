#!/usr/bin/env python3
"""Build five practice forms per MATH 101 test from the current question banks."""
import argparse
from copy import deepcopy
import json
import random
import secrets
from pathlib import Path

from build_tsm_practice_bundles import fingerprint, write_bundle
from course_pages import build_practice
from generate_practice_batch import ASSESSMENTS

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '101/practice-tests'
SOURCE = ROOT / '_instructor/assessments/2026-10-30'


def make_forms(slug, title, end):
    """Recombine matched questions/answers without duplicating a complete exam."""
    source = json.loads((SOURCE / f'{slug}-20-versions.json').read_text())
    families = sorted(q['id'] for q in source[0]['questions'])
    pools = {fid: [] for fid in families}
    for record in source:
        assert sorted(q['id'] for q in record['questions']) == families
        for q in record['questions']:
            pools[q['id']].append((record['version'], q))
    excluded = {fingerprint(r['questions']) for r in source}
    used = {fid: set() for fid in families}
    forms = []
    for i in range(5):
        for attempt in range(100):
            seed = secrets.randbits(32)
            rng = random.Random(seed)
            questions, provenance = [], {}
            for fid, pool in pools.items():
                available = [(v, q) for v, q in pool if fingerprint([q]) not in used[fid]]
                version, q = rng.choice(available or pool)
                questions.append(deepcopy(q))
                provenance[fid] = version
            identity = fingerprint(questions)
            if identity not in excluded:
                break
        else:
            raise ValueError(f'Could not build a distinct practice form: {slug}')
        excluded.add(identity)
        for q in questions:
            used[q['id']].add(fingerprint([q]))
        rng.shuffle(questions)
        expected = 10 if slug.endswith('final') else 5
        assert len(questions) == expected
        assert all(sum(row['points'] for row in q['rows']) == 100 // expected for q in questions)
        forms.append(dict(course='MATH 101', assessment=slug,
                          title='MATH 101 ' + title + ' - Practice Test', end=end,
                          practice=i + 1, version=str(secrets.randbelow(90000) + 10000),
                          seed=seed, questions=questions, content_fingerprint=identity,
                          source_question_versions=provenance))
    return forms


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--only', choices=[a[1] for a in ASSESSMENTS if a[0] == 'MATH 101'])
    parser.add_argument('--reformat', action='store_true', help='Preserve saved questions and identifiers')
    args = parser.parse_args(argv)
    entries, allforms = [], []
    for course, slug, title, _, end in ASSESSMENTS:
        if course != 'MATH 101' or (args.only and args.only != slug):
            continue
        path = OUT / f'{slug}-practice-5-versions.pdf'
        forms = (json.loads(path.with_suffix('.json').read_text()) if args.reformat
                 else make_forms(slug, title, end))
        entries.append(write_bundle(forms, path))
        allforms.extend(forms)
    manifest = OUT / 'manifest.json'
    if args.only and manifest.exists():
        entries = [e for e in json.loads(manifest.read_text()) if e['assessment'] != args.only] + entries
        prior = json.loads((OUT / 'source/assessments.json').read_text())
        allforms = [a for a in prior if a['assessment'] != args.only] + allforms
    manifest.write_text(json.dumps(sorted(entries, key=lambda e: e['assessment']), indent=2) + '\n')
    (OUT / 'source/assessments.json').write_text(json.dumps(allforms, indent=2) + '\n')
    build_practice(ROOT / '101')
    print(f'Published {len(entries)} MATH 101 five-version practice bundles.')


if __name__ == '__main__':
    main()
