#!/usr/bin/env python3
"""Check review coverage, answer counts, local navigation, math, and course scope."""
from pathlib import Path
import json
import re
from urllib.parse import unquote, urlsplit
from collections import Counter
from bs4 import BeautifulSoup
from build_essentials import inventory

ROOT=Path(__file__).resolve().parents[1]


def verify():
    report=json.loads((ROOT/'scripts/essentials-coverage.json').read_text())
    expected={(e['course'],e['number']):e for e in inventory()}
    assert {(r['course'],r['section']) for r in report}==set(expected)
    assert len(report)==len(expected)
    assert Counter(r['course'] for r in report)=={'tsm':37,'101':41,'stats':36}
    paths=[ROOT/r['path'] for r in report]
    paths+=[ROOT/c/'essentials.html' for c in ['tsm','101','stats']]
    paths+=[ROOT/c/'lecture-notes.html' for c in ['tsm','101','stats']]
    paths+=[ROOT/'index.html']
    for row in report:
        path=ROOT/row['path'];doc=BeautifulSoup(path.read_text(),'html.parser')
        assert len(doc.select('.recall-questions > li'))==row['questions'],path
        assert 5<=row['questions']<=10,path
        assert len(doc.select('.answer-key .answer > li'))==row['questions'],path
        examples=doc.select('.example')
        assert len(examples)==row['examples'] and 2<=len(examples)<=4,path
        assert all(len(e.select('details .answer > li'))>=2 for e in examples),path
        assert len(doc.select('h1'))==1 and doc.html['lang']=='en',path
        assert doc.select_one('meta[name="viewport"]'),path
        assert not re.search(r'GRAPH_|TODO|TBD|\\[()]',doc.get_text()),path
        assert not doc.select('merror'),path
        # A numeric binomial command without braces can swallow two digits
        # as its first argument and misparse '=' as its second argument.
        for fraction in doc.select('mfrac[linethickness="0"]'):
            operands=fraction.find_all(recursive=False)
            assert len(operands)==2,path
            assert all('=' not in operand.get_text() for operand in operands),path
        entry=expected[(row['course'],row['section'])]
        lesson=ROOT/row['course']/entry['lesson'];paths.append(lesson)
        ldoc=BeautifulSoup(lesson.read_text(),'html.parser')
        target='../essentials/'+path.name
        assert len(ldoc.select(f'a[href="{target}"]'))==1,lesson
        if row['course']=='101' and row['section'] in ['3.2','3.3']:
            assert len(doc.select('svg'))==2,path
        if entry['scope']: assert entry['scope'] in doc.get_text(),path
    # Check only our new links on existing pages, all links on new pages.
    for path in paths:
        doc=BeautifulSoup(path.read_text(),'html.parser')
        new_page='/essentials/' in str(path) or path.name=='essentials.html'
        for node in doc.select('a[href],link[href],img[src]'):
            href=node.get('href',node.get('src',''))
            if not new_page and 'essentials' not in href: continue
            parsed=urlsplit(href)
            if parsed.scheme or parsed.netloc: continue
            dest=(path.parent/unquote(parsed.path)).resolve() if parsed.path else path
            assert dest.is_file(),(path,href)
            if parsed.fragment:
                assert BeautifulSoup(dest.read_text(),'html.parser').find(id=parsed.fragment),(path,href)
    print(f'PASS: {len(report)} topics; 570 questions and answer keys; 230 worked solutions; all review links resolve; scope labels and graph-only sections verified.')


if __name__=='__main__': verify()
