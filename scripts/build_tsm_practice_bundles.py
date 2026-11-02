#!/usr/bin/env python3
"""Publish five fresh, duplex-safe practice versions per TSM unit test/final."""
import argparse
import hashlib
import json
import random
import secrets
from pathlib import Path
from pypdf import PdfWriter
import algebra_test_layout as L
import tsm_practice_content as C
import generate_practice_batch as B
from course_pages import build_practice

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'tsm/practice-tests'
COUNT=5

def fingerprint(questions):
    return hashlib.sha256(json.dumps(sorted(
        [dict(id=q['id'],math=q['math'],table=q.get('table'),graph=q.get('graph')) for q in questions],
        key=lambda q:q['id']),sort_keys=True).encode()).hexdigest()

def make_forms(course,slug,title,end):
    old=ROOT/'_instructor/assessments/2026-10-30'/f'{slug}-20-versions.json'
    excluded={fingerprint(r['questions']) for r in json.loads(old.read_text())} if old.exists() else set()
    forms=[]
    for i in range(COUNT):
        for attempt in range(100):
            seed=secrets.randbits(32);questions=C.questions(slug,i,seed)
            identity=fingerprint(questions)
            if identity not in excluded:break
        else:raise ValueError('Could not generate distinct form: '+slug)
        excluded.add(identity)
        random.Random(seed).shuffle(questions)
        assert len(questions)==(10 if slug.endswith('final') else 5)
        assert sum(r['points'] for q in questions for r in q['rows'])==100
        for q in questions:
            assert not any(ord(c)<32 for t in q['math']+[r['answer'] for r in q['rows']] for c in t)
        forms.append(dict(course=course,assessment=slug,title=course+' '+title+' - Practice Test',
            end=end,practice=i+1,version=str(secrets.randbelow(90000)+10000),seed=seed,
            questions=questions,content_fingerprint=identity))
    return forms

def write_bundle(forms,path):
    writer=PdfWriter();records=[]
    for a in forms:
        reader,n,keyidx,pages,cols=L.packet(a)
        start=len(writer.pages);assert start%2==keyidx%2==0
        writer.append(reader,import_outline=False)
        if len(writer.pages)%2:writer.add_blank_page(width=612,height=792)
        mark=writer.add_outline_item(f"Practice {a['practice']} - Version {a['version']}",start)
        writer.add_outline_item('Student test',start,parent=mark)
        writer.add_outline_item('Answer key',start+keyidx,parent=mark)
        geometry=[]
        for pi,blocks in enumerate(pages):
            y=L.TOP
            for b in blocks:
                rows=[];ry=y
                for row in b['rows']:
                    rows.append(dict(top=ry,bottom=ry-row['height'],label=row['source']['label'],points=row['source']['points']))
                    ry-=row['height']
                geometry.append(dict(question=b['num'],page=pi,top=y,bottom=y-b['height'],rows=rows));y-=b['height']
        records.append(dict(a,start=start,test_pages=n,key_start=start+keyidx,
            packet_pages=len(writer.pages)-start,geometry=geometry))
        print(a['assessment'],a['practice'],a['version'],'student pages',n,flush=True)
    writer.add_metadata({'/Title':forms[0]['title']+' - Five Versions','/Author':'Jeremy Kastine',
        '/Subject':'Five practice tests with matching keys; US Letter, duplex, long-edge flip, actual size.'})
    writer.write(path);path.with_suffix('.json').write_text(json.dumps(records,indent=2)+'\n')
    return dict(course=forms[0]['course'],assessment=forms[0]['assessment'],
        title=forms[0]['title'].removesuffix(' - Practice Test'),end=forms[0]['end'],
        file=path.name,versions=COUNT,pages=len(writer.pages),
        version_ids=[r['version'] for r in records],
        student_pages=sorted({r['test_pages'] for r in records}))

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--only');p.add_argument('--reformat',action='store_true')
    args=p.parse_args();OUT.mkdir(parents=True,exist_ok=True);(OUT/'source').mkdir(exist_ok=True)
    entries=[];allforms=[]
    for course,slug,title,fn,end in B.ASSESSMENTS:
        if not course.startswith('TSM') or (args.only and args.only!=slug):continue
        path=OUT/f'{slug}-practice-5-versions.pdf'
        if args.reformat:
            forms=json.loads(path.with_suffix('.json').read_text())
        else:forms=make_forms(course,slug,title,end)
        entry=write_bundle(forms,path);entries.append(entry);allforms.extend(forms)
    if args.only and (OUT/'manifest.json').exists():
        old=json.loads((OUT/'manifest.json').read_text())
        entries=[e for e in old if e['assessment']!=args.only]+entries
        oldforms=json.loads((OUT/'source/assessments.json').read_text())
        allforms=[a for a in oldforms if a['assessment']!=args.only]+allforms
    (OUT/'manifest.json').write_text(json.dumps(entries,indent=2)+'\n')
    (OUT/'source/assessments.json').write_text(json.dumps(allforms,indent=2)+'\n')
    build_practice(ROOT/'tsm')
    # Keep the course-specific pages and their navigation intact.
    from bs4 import BeautifulSoup as BS
    combined=BS((ROOT/'tsm/practice-tests.html').read_text(),'html.parser')
    intro=combined.select_one('main > p')
    for course in ['098','099']:
        path=ROOT/f'tsm/practice-tests-{course}.html';s=BS(path.read_text(),'html.parser')
        s.select_one('main > p').replace_with(BS(str(intro),'html.parser'))
        s.select_one('main > section').replace_with(BS(str(next(sec for sec in combined.select('main > section') if sec.h2.get_text()=='TSM '+course)),'html.parser'))
        path.write_text(str(s)+'\n')
    print('Published',len(entries),'five-version TSM practice PDFs.',flush=True)

if __name__=='__main__':main()
