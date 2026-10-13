#!/usr/bin/env python3
"""Build three practice forms per assessment, then refresh the two course indexes."""
import sys
from build_practice_tests import *
import practice_math101 as M
import practice_tsm_finals as T

ASSESSMENTS=[
 ('TSM 098','98-arithmetic','Arithmetic Test',arithmetic98,8),
 ('TSM 098','98-polynomials','Polynomials Test',polynomials98,17),
 ('TSM 098','98-fractions','Fractions Test',fractions98,23),
 ('TSM 098','98-linear','Linear Equations and Linear Systems Test',linear98,34),
 ('TSM 098','98-final','Final Exam',lambda v:T.final('TSM 098',v),34),
 ('TSM 099','99-arithmetic','Arithmetic Test',arithmetic99,8),
 ('TSM 099','99-polynomials','Polynomials Test',polynomials99,17),
 ('TSM 099','99-rational','Rational Expressions Test',rational99,23),
 ('TSM 099','99-equations','Quadratic and Rational Equations Test',equations99,29),
 ('TSM 099','99-graphing','Graphing Test',graph99,34),
 ('TSM 099','99-final','Final Exam',lambda v:T.final('TSM 099',v),34),
 ('MATH 101','101-unit-1','Unit 1: Expressions, Equations, and Inequalities',M.unit1,2),
 ('MATH 101','101-unit-2','Unit 2: Functions and Their Graphs',M.unit2,4),
 ('MATH 101','101-unit-3','Unit 3: Polynomial, Rational, and Radical Functions',M.unit3,5),
 ('MATH 101','101-unit-4','Unit 4: Exponentials, Logarithms, and Systems',M.unit4,7),
 ('MATH 101','101-final','Final Exam',M.final,7),
]

def make_batch(timestamp):
    batch=[];counter=0
    for course,slug,title,constructor,end in ASSESSMENTS:
        seen=set()
        for v in range(3):
            counter+=1;questions=constructor(v)
            expected=10 if title=='Final Exam' else 5
            assert len(questions)==expected
            assert all(sum(r['points'] for r in q['rows'])==(10 if expected==10 else 20) for q in questions)
            assert sum(r['points'] for q in questions for r in q['rows'])==100
            for q in questions:
                for t in q['math']+[r['answer'] for r in q['rows']]:
                    assert not any(ord(c)<32 for c in t),(slug,q['id'],repr(t))
            identity=json.dumps([{'math':q['math'],'graph':q.get('graph'),'table':q.get('table')} for q in questions],sort_keys=True)
            assert identity not in seen;seen.add(identity)
            random.Random(counter+720).shuffle(questions)
            a=dict(course=course,folder='101' if course=='MATH 101' else 'tsm',assessment=slug,title=course+' '+title,short=course+' '+('Final' if expected==10 else 'Unit Practice'),practice=v+1,version=timestamp+'.'+str(counter),questions=questions,end=end)
            a['file']=slug+'-practice-'+a['version']+'.pdf'
            if course=='MATH 101' and expected==5:a['minutes']=30
            batch.append(a)
    assert len(batch)==48
    return batch

def cards(manifest):
    groups=[]
    for entry in manifest:
        if entry['assessment'] in [g['assessment'] for g in groups]:continue
        related=[a for a in manifest if a['assessment']==entry['assessment']]
        links=' &middot; '.join(f'<a href="practice-tests/{a["file"]}">Practice {a["practice"]} (PDF)</a>' for a in related)
        groups.append(dict(assessment=entry['assessment'],title=entry['title'],end=entry['end'],html='<li class="practice-test-links"><strong>'+escape(entry['title'])+'</strong><p>'+links+'</p><p class="practice-note">Includes an answer sheet and answer key. Try the test before checking the key.</p></li>'))
    return groups

def link_tsm(manifest):
    path=ROOT/'tsm/index.html';html=path.read_text()
    html=re.sub(r'<!-- practice-tests-topic-\d+:start -->.*?<!-- practice-tests-topic-\d+:end -->\s*','',html,flags=re.S)
    for topic in sorted(set(a['end'] for a in manifest)):
        block='\n<!-- practice-tests-topic-'+str(topic)+':start -->\n'+''.join(g['html'] for g in cards(manifest) if g['end']==topic)+'\n<!-- practice-tests-topic-'+str(topic)+':end -->'
        pattern=r'(<li><a href="lessons/topic-'+f'{topic:02d}'+r'-.*?</li>)'
        html,count=re.subn(pattern,lambda m:m.group(1)+block,html,count=1,flags=re.S);assert count==1,topic
    html=html.replace('<p>Topics 1 through 37</p>','<p>Topics 1 through 37</p>\n      <p>Three practice tests for each unit and final are linked below at the corresponding test points.</p>') if 'Three practice tests for each unit' not in html else html
    path.write_text(html)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--version',default='202610122020');parser.add_argument('--only',help='Assessment slug for a focused rebuild');parser.add_argument('--validate-only',action='store_true');args=parser.parse_args()
    batch=make_batch(args.version)
    if args.validate_only:
        print('48 forms; 285 question units; all question counts and point totals verified.');return
    report=[]
    for a in batch:
        if args.only and a['assessment']!=args.only:continue
        report.append(build(a));print(a['file'],flush=True)
    rebuilt_count=len(report)
    if report:
        for folder in ['101','tsm']:
            subset=[a for a in batch if a['folder']==folder]
            d=ROOT/folder/'practice-tests';(d/'source').mkdir(parents=True,exist_ok=True)
            manifest=[{k:a[k] for k in ['course','assessment','title','practice','version','file','end']} for a in subset]
            (d/'manifest.json').write_text(json.dumps(manifest,indent=2))
            (d/'source/assessments.json').write_text(json.dumps(subset,indent=2))
        link_tsm([a for a in batch if a['folder']=='tsm'])
        from slide_builder import COURSES,build_index
        sections=[]
        for f in sorted((ROOT/'101/slides/source').glob('chapter-*.json')):sections.extend(json.loads(f.read_text()))
        build_index(ROOT/'101',COURSES['101'],sections)
        report_path=ROOT/'101/practice-tests/source/build-report.json'
        if args.only and report_path.is_file():
            new={a['file']:a for a in report}
            report=[new.get(a['file'],a) for a in json.loads(report_path.read_text())]
        report_path.write_text(json.dumps(report,indent=2))
    print(json.dumps({'rebuilt':rebuilt_count,'total_files':len(report),'pages':sum(a['pages'] for a in report)}))

if __name__=='__main__':main()
