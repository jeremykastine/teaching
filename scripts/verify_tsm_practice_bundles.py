#!/usr/bin/env python3
"""Check practice content, all student/key geometry, PDFs, bookmarks, and links."""
import argparse
import json
import re
from pathlib import Path
import fitz
import sympy as S
from bs4 import BeautifulSoup as BS
from sympy.parsing.sympy_parser import parse_expr,standard_transformations,implicit_multiplication_application
import build_practice_tests as T
import verify_assessment_batches as V
from build_tsm_practice_bundles import fingerprint
from assessment_content import institutional

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'tsm/practice-tests'
QA=ROOT/'tmp/tsm-practice-qa'
LOCALS={'x':T.x,'y':T.y,'I':S.I,'sqrt':S.sqrt}
def expr(s):return S.sympify(s,locals=LOCALS)

def math_check(q):
    for check in q.get('verification',[]):
        kind=check['kind']
        if kind in ['expression','factoring']:
            e=expr(check['input']);a=expr(check['answer'])
            assert S.simplify(e-a)==0,(q['id'],check)
            if kind=='factoring':
                assert bool(S.discriminant(e,T.x)<0)==check['prime']
        elif kind=='equation':
            lhs,rhs=expr(check['lhs']),expr(check['rhs'])
            denoms=list(map(expr,check['denominators']))
            cleared=S.cancel((lhs-rhs)*S.prod(denoms))
            candidates=S.solve(S.fraction(cleared)[0],T.x)
            assert set(candidates)==set(map(expr,check['candidates']))
            valid=[z for z in candidates if all(d.subs(T.x,z)!=0 for d in denoms)
                and S.simplify((lhs-rhs).subs(T.x,z))==0]
            assert set(valid)==set(map(expr,check['answers']))
            assert q['rows'][0]['answer']==(T.solution_tex(valid) if valid else 'No solution')
        elif kind=='system':
            solved=S.solve([expr(l)-expr(r) for l,r in zip(check['lhs'],check['rhs'])],[T.x,T.y])
            assert solved==dict(zip([T.x,T.y],check['answer']))
            assert q['rows'][0]['answer']==T.tex(S.Tuple(*check['answer']))
        elif kind=='comparison':
            lhs,rhs=expr(check['lhs']),expr(check['rhs'])
            for i,z in enumerate(check['inputs']):
                a,b=lhs.subs(T.x,z),rhs.subs(T.x,z)
                assert a.is_integer and b.is_integer
                assert a==expr(check['left'][i]) and b==expr(check['right'][i])
                assert q['rows'][i]['answer']==f'Left {a}; right {b}; '+('yes' if a==b else 'no')
        elif kind=='signed':
            for (text,answer),row in zip(check['expressions'],q['rows']):
                assert answer==row['answer']
                match=re.fullmatch(r'\\frac\{(-?\d+)\}\{(-?\d+)\}',text)
                if match:
                    a,b=map(int,match.groups())
                    assert answer==('Undefined' if b==0 else str(S.Rational(a,b)))
                else:
                    value=parse_expr(text,transformations=standard_transformations+(implicit_multiplication_application,))
                    assert value==S.Integer(answer)
        elif kind=='line_points':
            (x1,y1),(x2,y2)=[list(map(expr,p)) for p in check['points']]
            slope=(y2-y1)/(x2-x1);intercept=y1-slope*x1
            assert slope==expr(check['slope']) and intercept==expr(check['intercept'])
            assert q['rows'][0]['answer']==T.eq(T.y,slope*T.x+intercept)
        elif kind=='graph':
            lines=[[float(expr(m)),float(expr(b))] for m,b in check['lines']]
            graph=q['graph']
            actual=graph['answer_lines'] if graph['kind']=='blank' else [[graph['m'],graph['b']]]
            assert actual==lines
    if q['id']=='L98-exception':
        # The four exceptional structural families are checked directly.
        texts=q['math'];answer=q['rows'][0]['answer']
        equations=[]
        for text in texts:
            left,right=text.split(' = ')
            parse=lambda t:parse_expr(t,local_dict=LOCALS,transformations=standard_transformations+(implicit_multiplication_application,))
            equations.append(S.expand(parse(left)-parse(right)))
        if len(equations)==1:
            assert not equations[0].has(T.x)
            assert answer==('All real numbers' if equations[0]==0 else 'No solution')
        else:
            consistent=S.simplify(equations[1]-2*equations[0])==0
            assert answer.startswith('Infinitely many') if consistent else answer=='No solution'

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--render',action='store_true');args=p.parse_args()
    manifest=json.loads((OUT/'manifest.json').read_text())
    assert len(manifest)==11 and sum(e['versions'] for e in manifest)==55
    QA.mkdir(parents=True,exist_ok=True);V.OUT=OUT;V.QA=QA
    report=[]
    for entry in manifest:
        result=V.audit(entry,args.render,5)
        records=json.loads((OUT/entry['file']).with_suffix('.json').read_text())
        pdf=fitz.open(OUT/entry['file'])
        top=[z for z in pdf.get_toc() if z[0]==1]
        assert len(top)==5
        old=ROOT/'_instructor/assessments/2026-10-30'/f"{entry['assessment']}-20-versions.json"
        prior={fingerprint(r['questions']) for r in json.loads(old.read_text())} if old.exists() else set()
        for i,a in enumerate(records):
            assert fingerprint(a['questions']) not in prior
            assert top[i][2]==a['start']+1 and a['version'] in top[i][1]
            for q in a['questions']:math_check(q)
            if entry['assessment'].endswith('final'):
                expected={q['id']:q for q in institutional(a['course'],a['seed'],i%4)}
                actual={q['id']:q for q in a['questions'] if q['id'].startswith('I')}
                assert actual==expected and len(actual)==6
        result['mathematics']='verified'
        report.append(result);print(json.dumps(result),flush=True)
    for course,expected in [('098',5),('099',6),('',11)]:
        path=ROOT/'tsm'/('practice-tests'+('-'+course if course else '')+'.html')
        s=BS(path.read_text(),'html.parser')
        links=[a['href'] for a in s.select('a[href]') if a['href'].endswith('.pdf')]
        assert len(links)==expected
        assert all((path.parent/href).is_file() and '-practice-5-versions.pdf' in href for href in links)
        assert 'five practice versions' in s.get_text().lower()
    (QA/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print('Verified 11 bundles, 55 versions, all mathematical records, PDF geometry, and practice indexes.')

if __name__=='__main__':main()
