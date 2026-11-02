#!/usr/bin/env python3
"""Audit every exported packet and render every nonblank page for print QA."""
import json,re,argparse,hashlib
from pathlib import Path
from collections import Counter
import fitz
from PIL import Image,ImageOps,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'_instructor/assessments/2026-10-30'
QA=ROOT/'tmp/assessment-qa'
WORDS={};DRAWINGS={};RULES={}

def page_words(page):
    if page.number not in WORDS:WORDS[page.number]=page.get_text('words')
    return WORDS[page.number]

def rules(page,left,right):
    cachekey=(page.number,left,right)
    if cachekey in RULES:return RULES[cachekey]
    if page.number not in DRAWINGS:DRAWINGS[page.number]=page.get_drawings()
    result=[]
    for drawing in DRAWINGS[page.number]:
        for item in drawing['items']:
            if item[0]!='l':continue
            a,b=item[1:]
            if abs(a.y-b.y)<.02 and abs(a.x-left)<.02 and abs(b.x-right)<.02:result.append(round(a.y,2))
    RULES[cachekey]=sorted(result)
    return RULES[cachekey]

def audit(entry,render,expected_versions=20):
    WORDS.clear();DRAWINGS.clear();RULES.clear()
    path=OUT/entry['file'];records=json.loads(path.with_suffix('.json').read_text());doc=fitz.open(path)
    assert len(records)==entry['versions']==expected_versions,(path,'version count')
    assert len(doc)==entry['pages']
    ident=set();student_pages=Counter();thumbnails=[];blanks=0
    for r in records:
        version=r['version'];assert re.fullmatch(r'[1-9]\d{4}',version)
        start=r['start'];n=r['test_pages'];key=r['key_start'];end=start+r['packet_pages']
        assert start%2==key%2==0 and r['packet_pages']%2==0
        assert key==start+n+n%2
        qs=r['questions'];assert len(qs)==(10 if entry['course']=='MSC 201' or entry['assessment'].endswith(('final','diagnostic')) else 5)
        if entry['course']=='MSC 201':
            assert all(len(q['choices'])==4 and 0<=q['answer_index']<=3 and len(set(q['choices']))==4 for q in qs)
            if 'unit-' in entry['assessment']:assert len({q['group'] for q in qs})==10
        else:assert sum(row['points'] for q in qs for row in q['rows'])==100
        identity=hashlib.sha256(json.dumps(sorted(qs,key=lambda q:q['id']),sort_keys=True).encode()).hexdigest();assert identity not in ident,(path,'duplicate content');ident.add(identity)
        student_pages[n]+=1
        keypages=(n+2)//3
        for i in list(range(start+n,key))+list(range(key+keypages,end)):
            page=doc[i];assert not page.get_text().strip() and not page.get_drawings() and not page.get_images(),(path,i,'nonblank padding');blanks+=1
        for pi in range(n):
            page=doc[start+pi];text=page.get_text()
            assert version in text and 'Name:' in text and 'Date:' in text
            assert 'basic, non-scientific calculator only.' in text and 'No notes or other technology.' in text
            foot=page.get_text(clip=fitz.Rect(0,748,612,792)).strip()
            expected=('Test continues on the other side of the sheet.' if pi%2==0 else 'Test continues on the next sheet.') if pi<n-1 else ''
            assert foot==expected,(path,i,'footer',foot,expected)
        for ki in range(keypages):
            page=doc[key+ki];text=page.get_text();header=page.get_text(clip=fitz.Rect(0,0,612,100)).strip()
            assert header==version,(path,'key header',header)
            assert not page.get_text(clip=fitz.Rect(0,748,612,792)).strip()
            for phrase in ['Instructor','ANSWER KEY','Name:','100 points','corresponding']:assert phrase not in text
        for g in r['geometry']:
            pi=g['page'];student=doc[start+pi];answer=doc[key+pi//3];col=pi%3
            if entry['course']=='MSC 201':
                x=36+90*col
                assert rules(student,36,576)==rules(answer,x,x+80),(path,'stats row rules')
                correct=g['letter']+'.';top=792-g['row_top'];bottom=792-g['row_bottom']
                sw=[w for w in page_words(student) if w[0]>309 and w[0]<325 and top<=w[1]<bottom and w[4]==correct]
                kw=[w for w in page_words(answer) if x+20<w[0]<x+40 and top<=w[1]<bottom and w[4]==correct]
                assert len(sw)==len(kw)==1,(path,'missing choice',g,sw,kw)
                assert abs(sw[0][1]-kw[0][1])<.02 and abs(sw[0][3]-kw[0][3])<.02,(path,'choice baseline')
            else:
                x=36+180*col
                assert rules(student,36,576)==rules(answer,x,x+174),(path,'algebra row rules')
                for row in g['rows']:
                    top=792-row['top'];bottom=792-row['bottom']
                    # Point baselines must match independently in each view.
                    sw=[w for w in page_words(student) if w[0]>540 and top<=w[1]<bottom and w[4]=='pts']
                    kw=[w for w in page_words(answer) if x+140<w[0]<x+174 and top<=w[1]<bottom and w[4]=='pts']
                    assert len(sw)==len(kw)==1 and abs(sw[0][1]-kw[0][1])<.02,(path,'point baseline',row)
                    q=qs[g['question']-1]
                    if not(q.get('graph',{}).get('kind')=='blank'):
                        words=[w for w in page_words(student) if w[0]>=395.99 and w[2]<=576.01 and w[1]>=top-.01 and w[3]<=bottom+.01]
                        actual=' '.join(w[4] for w in words)
                        labels=[f"{g['question']}.",row['label'],str(row['points']),'pts']
                        allowed=set(' '.join(labels).split())
                        assert all(w[4] in allowed for w in words),(path,'unexpected student answer text',actual,allowed)
        for i in range(start,end):
            page=doc[i];assert page.rect==fitz.Rect(0,0,612,792)
            for block in page.get_text('dict')['blocks']:
                if 'lines' not in block:continue
                for line in block['lines']:
                    for span in line['spans']:
                        x0,y0,x1,y1=span['bbox']
                        assert x0>=34 and x1<=578 and y0>=23 and y1<=766,(path,i,'print bounds',span['text'],span['bbox'])
            if render and page.get_text().strip():
                # Full-size raster render catches malformed PDF resources.
                full=QA/'pages'/entry['assessment']/f'{i+1:03}.png';full.parent.mkdir(parents=True,exist_ok=True)
                if not full.exists() or full.stat().st_mtime<path.stat().st_mtime:
                    pix=page.get_pixmap(matrix=fitz.Matrix(1,1),alpha=False);pix.save(full)
                im=Image.open(full).convert('RGB');im.thumbnail((153,198));tile=Image.new('RGB',(165,220),'#dddddd');tile.paste(im,(6,4));ImageDraw.Draw(tile).text((6,204),str(i+1),fill='black');thumbnails.append(tile)
    if render:
        for k in range(0,len(thumbnails),40):
            subset=thumbnails[k:k+40];sheet=Image.new('RGB',(165*8,220*((len(subset)+7)//8)),'white')
            for j,tile in enumerate(subset):sheet.paste(tile,((j%8)*165,(j//8)*220))
            sheet.save(QA/f"{entry['assessment']}-contact-{k//40+1}.jpg")
    return dict(assessment=entry['assessment'],versions=expected_versions,pages=len(doc),blank_pages=blanks,student_page_counts=dict(student_pages))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--render',action='store_true');ap.add_argument('--only');args=ap.parse_args();QA.mkdir(parents=True,exist_ok=True)
    entries=json.loads((OUT/'manifest.json').read_text());results=[]
    for entry in entries:
        if args.only and entry['assessment']!=args.only:continue
        result=audit(entry,args.render);results.append(result);print(json.dumps(result),flush=True)
    (QA/'verification.json').write_text(json.dumps(results,indent=2))
    print('Verified',len(results),'batches;',sum(r['versions'] for r in results),'versions',flush=True)
if __name__=='__main__':main()

