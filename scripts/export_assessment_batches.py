#!/usr/bin/env python3
"""Generate unlinked instructor batches; all geometry and seeds are recorded.

Run: python scripts/export_assessment_batches.py [--only SLUG] [--count 20]
Use US Letter, actual size, duplex, long-edge flip.
"""
import argparse, json, random, secrets, re, math, hashlib, fcntl
from pathlib import Path
from io import BytesIO
from html import escape
import fitz
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from pypdf import PdfReader, PdfWriter
import build_practice_tests as T
import generate_practice_batch as B
import algebra_test_layout as L
from assessment_content import institutional, math101_solving

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'_instructor/assessments/2026-10-30'
STYLE=ParagraphStyle('stats-print',fontName='DV',fontSize=9.5,leading=11.8)
TOP=660

def fractions(v):
    rng=random.Random(91000+v)
    def pair(op,reduce):
        while True:
            b,d=rng.sample(range(3,16),2)
            if math.lcm(b,d)>60:continue
            a=rng.randrange(1,b);c=rng.randrange(1,d)
            n=a*(math.lcm(b,d)//b)+(1 if op=='+' else -1)*c*(math.lcm(b,d)//d)
            if n<=0:continue
            g=math.gcd(n,math.lcm(b,d));z=T.S.Rational(n,math.lcm(b,d))
            if (g>1)==reduce and z.q!=1:return [(a,b),(c,d)]
    def q(fid,pairs,op):
        vals=[T.S.Rational(a,b) for a,b in pairs];z=vals[0]
        for w in vals[1:]:z=z+w if op=='+' else z-w if op=='-' else z*w if op==r'\times' else z/w
        expr=(' '+op+' ').join(str(a) if b==1 else T.frac(a,b) for a,b in pairs)
        return T.question(fid,'Compute and give the result in lowest terms.',[expr],[T.ans('',T.tex(z),20)])
    n=2+v%7
    if v%2==0:
        mult=[(n,1),(2,3),(3,5)]
        div=[(22+22*(v%3),15),(33,25)]
    else:
        mult=[(14,15),(25,21),(7+2*(v%3),10)]
        div=[(2*n,1),(4,5)]
    extra=[([(1,7),(2,7)],'+'), ([(5,11),(2,11)],'-'), ([(2,5),(3,7)],r'\times'), ([(2,5),(7,3)],r'\div')][v%4]
    return [q('F98-add',pair('+',v%2==0),'+'),q('F98-sub',pair('-',v%2!=0),'-'),q('F98-mult',mult,r'\times'),q('F98-div',div,r'\div'),q('F98-extra',*extra)]

def improve(qs,slug,v):
    """Keep generated values within the course's workload bounds."""
    rng=random.Random(82172+v)
    for q in qs:
        if q['id'].endswith('-frac') and q['id'].startswith(('A98','A99')):
            pairs=[]
            for g in [rng.choice([2,3,5,7]),rng.choice([6,10,14,15])]:
                a,b=rng.choice([(2,3),(3,5),(4,7),(5,8),(7,9)])
                pairs.append((a*g,b*g))
            rng.shuffle(pairs)
            q['math']=[rf'({chr(97+i)})\quad '+T.frac(a,b) for i,(a,b) in enumerate(pairs)]
            for row,(a,b) in zip(q['rows'],pairs):row['answer']=T.tex(T.S.Rational(a,b));row['plain']=False
        if q['id']=='A98-quad':
            a=1+v%3;b=-(2+v%5);c=1+v%7;e=a*T.x**2+b*T.x+c
            q['math']=[T.tex(e)]
            for row,z in zip(q['rows'],[10,-10,0]):row['answer']=T.tex(e.subs(T.x,z))
        if q['id']=='A98-eval':
            e=(2+v%4)*T.x-(2+v%3)*T.y+(v%5-2);px=-(2+v%4);py=1+v%3
            q['prompt']=f'Evaluate at x = {px}, y = {py}.';q['math']=[T.tex(e)];q['rows'][0]['answer']=T.tex(e.subs({T.x:px,T.y:py}))
        if q['id']=='A99-root':
            roots=[(4+v%7,False),(5+(v+2)%7,True)];rng.shuffle(roots)
            q['math']=[rf'({chr(97+i)})\quad \sqrt{{{-(n*n) if imag else n*n}}}' for i,(n,imag) in enumerate(roots)]
            for row,(n,imag) in zip(q['rows'],roots):row['answer']=str(n)+('i' if imag else '')
        if q['id'] in ('A99-eval','A99-formula'):
            k=2+v%3
            if v%3==2:
                a=2;b=-(2*k+1);c=k
                q.update(id='A99-formula',prompt=f'Evaluate both values in the formula for a = {a}, b = {b}, c = {c}.',math=[r'x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}'],rows=[T.ans('',T.solution_tex([T.S.Rational(1,2),k]),20)])
            else:
                e=(1+v%2)*T.x**2-(2+v%3)*T.x+1+v%4 if v%3==0 else (1+v%2)*(T.x-1)*(T.x+2+v%2)
                q.update(prompt=f'Evaluate at (a) x = {k} and (b) x = {-k}.',math=[T.tex(e) if v%3==0 else T.tex(T.S.factor(e))],rows=[T.ans('(a)',T.tex(e.subs(T.x,k)),10),T.ans('(b)',T.tex(e.subs(T.x,-k)),10)])
        if q['id']=='P98-binomial':
            a=2+v%3;c=2+(v+1)%3;b=1+v%4;d=2+v%2;e=(a*T.x-b)*(c*T.x+d)
            if T.S.Poly(e,T.x).coeff_monomial(T.x)==0:d+=1;e=(a*T.x-b)*(c*T.x+d)
            q['math'][1]=r'(b)\quad '+T.par(a*T.x-b)+T.par(c*T.x+d);q['rows'][1]['answer']=T.tex(T.S.expand(e))
        if q['id']=='L98-dist':
            # The other ordinary equation has a fractional solution except the
            # middle structural family, whose solution is an integer.
            z=T.S.Rational(5,3) if v%3==1 else T.S.Integer(2+v%4)
            k=2+v%5;lhs=3*(2*T.x-k)-(4*T.x+k+1)+T.x;rhs=lhs.subs(T.x,z)
            assert T.S.simplify(lhs.subs(T.x,z)-rhs)==0
            q['math']=[f'3(2x-{k})-(4x+{k+1})+x = '+T.tex(rhs)];q['rows'][0]['answer']=T.solution_tex([z])
        if q['id']=='E99-formula':
            pool=[(a,b,c) for a in range(2,5) for b in range(1,6) for c in range(1,7) if math.isqrt(b*b+4*a*c)**2!=b*b+4*a*c and math.gcd(math.gcd(a,b),c)==1]
            a,b,c=pool[v%len(pool)];poly=a*T.x*T.x+b*T.x-c
            q['math']=[T.eq(poly,0)];q['rows'][0]['answer']=T.solution_tex(T.S.solve(poly,T.x))
        if q['id']=='U4-5':
            q['rows'][-1]['answer']='Yes' if 'yes' in q['rows'][-1]['answer'].lower() else 'No'
        if q['id']=='R99-simple':
            h=2+v%5;b=3+(v+2)%5
            # Exactly one required nonmonic trinomial across this test.
            n=T.S.expand((2*T.x+1)*(T.x-h));d=T.S.expand(3*(T.x-h)*(T.x+b))
            q['math']=[T.frac(n,d)];q['rows'][0]['answer']=T.tex(T.S.cancel(n/d))
        if q['id']=='R99-add' or q['id']=='R99-sub':
            h=2+(v//3)%7;k=h+3;den=T.S.expand((T.x-h)*(T.x-k))
            cancel_add=v%2==0
            if q['id']=='R99-add':a,b=(1,3) if cancel_add else (2,1);op='+';e=a/(T.x-h)+b/den
            else:a,b=(2,1) if cancel_add else (1,3);op='-';e=a/(T.x-h)-b/den
            q['math']=[T.frac(a,T.x-h)+' '+op+' '+T.frac(b,den)];q['rows'][0]['answer']=T.tex(T.S.factor(T.S.cancel(e)))
        if q['id']=='R99-mul':
            h=2+v%5;b=3+v%4
            n=6*T.x*(T.x-h);d=9*(T.x-h)*(T.x+b)
            q['math']=[T.frac(T.S.expand(n),T.S.expand(d))+r'\times'+T.frac(T.x+b,T.x)];q['rows'][0]['answer']=r'\frac{2}{3}'
    return qs

def stats_questions(unit,seed):
    rng=random.Random(seed);banks=[json.loads((ROOT/f'stats/question-banks/unit-{u}-question-bank.json').read_text()) for u in range(1,5)]
    selected=[]
    if unit:
        bank=banks[unit-1];groups=[(bank,g) for g in bank['groups']]
    else:
        groups=[]
        # 3/2/3/2 or 2/3/2/3 questions; every chapter represented.
        for i,bank in enumerate(banks):
            count=3 if (seed+i)%2==0 else 2
            chosen=rng.sample(bank['groups'][:5],count//2)+rng.sample(bank['groups'][5:],count-count//2)
            groups.extend((bank,g) for g in chosen)
    for bank,g in groups:
        q=dict(rng.choice([q for q in bank['questions'] if q['group']==g['id']]))
        order = rng.sample(range(4), 4)
        q['choices'] = [q['choices'][i] for i in order]
        q['answer_index'] = order.index(q['answer_index'])
        q['answer_letter'] = 'ABCD'[q['answer_index']]
        selected.append(q)
    rng.shuffle(selected);assert len(selected)==10 and len({q['id'] for q in selected})==10
    return selected

def paragraph(s,width):
    p=Paragraph(escape(s),STYLE);_,h=p.wrap(width,700);return p,h

def stat_layout(q,num):
    p,h=paragraph(str(num)+'. '+q['stem'],252);left=[(p,h)]
    if q.get('figure'):
        doc=fitz.open(ROOT/'stats/question-banks'/q['figure']['file']);pix=doc[0].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False)
        scale=min(250/pix.width,100/pix.height);left.append(((ImageReader(BytesIO(pix.tobytes('png'))),pix.width*scale,pix.height*scale),pix.height*scale))
    choices=[]
    for i,text in enumerate(q['choices']):
        p,h=paragraph('ABCD'[i]+'. '+text,252);choices.append((p,h))
    height=max(sum(h for _,h in left)+5*(len(left)-1),sum(h+3 for _,h in choices)-3)+26
    return dict(q=q,num=num,left=left,choices=choices,height=height)

def stats_packet(a):
    blocks=[stat_layout(q,i+1) for i,q in enumerate(a['questions'])];pages=[];page=[];used=0
    for b in blocks:
        assert b['height']<=TOP-42
        if page and used+b['height']>TOP-42:pages.append(page);page=[];used=0
        page.append(b);used+=b['height']
    if page:pages.append(page)
    buf=BytesIO();c=Canvas(buf,pagesize=(612,792));geom=[]
    for pi,blocks in enumerate(pages):
        L.header(c,a,pi+1,len(pages));c.setFont('DV',8.5)
        y=TOP;L.rule(c,36,576,y)
        for b in blocks:
            yy=y-8
            for obj,h in b['left']:
                if isinstance(obj,Paragraph):obj.drawOn(c,45,yy-h)
                else:c.drawImage(obj[0],45,yy-h,width=obj[1],height=obj[2])
                yy-=h+5
            yy=y-8;positions=[]
            for p,h in b['choices']:
                p.drawOn(c,315,yy-h);positions.append(yy);yy-=h+3
            correct_top=positions[b['q']['answer_index']]
            geom.append(dict(question=b['num'],page=pi,row_top=y,row_bottom=y-b['height'],answer_top=correct_top,letter='ABCD'[b['q']['answer_index']]))
            c.setFont('DV',7.6);c.drawRightString(567,y-b['height']+7,'10 pts')
            c.line(306,y,306,y-b['height']);y-=b['height'];L.rule(c,36,576,y)
        c.showPage()
    n=len(pages)
    if n%2:c.showPage()
    keyidx=c.getPageNumber()-1
    for start in range(0,n,3):
        L.header(c,a,1,n,True)
        for col in range(min(3,n-start)):
            x=36+col*90;pi=start+col
            c.setFont('DVB',8.8);c.drawString(x+3,TOP+5,f'TEST PAGE {pi+1}')
            L.rule(c,x,x+80,TOP)
            for g in [g for g in geom if g['page']==pi]:
                c.setFont('DV',8);c.drawString(x+3,g['row_top']-7-STYLE.fontSize,f"{g['question']}.")
                p,h=paragraph(g['letter']+'.',60);p.drawOn(c,x+26,g['answer_top']-h)
                c.setFont('DV',7.6);c.drawRightString(x+77,g['row_bottom']+7,'10 pts');L.rule(c,x,x+80,g['row_bottom'])
        c.showPage()
    c.save();return PdfReader(BytesIO(buf.getvalue())),n,keyidx,geom

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--only');ap.add_argument('--reformat',action='store_true');ap.add_argument('--count',type=int,default=20);args=ap.parse_args();OUT.mkdir(parents=True,exist_ok=True)
    registry=list(B.ASSESSMENTS)
    for course in ['TSM 098','TSM 099','MATH 101']:
        entry=next(t for t in registry if t[0]==course and t[1].endswith('final'))
        registry.append((course,entry[1].replace('final','diagnostic'),'Diagnostic Exam',entry[3],entry[4]))
    for i in range(1,5):registry.append(('MSC 201',f'stats-unit-{i}',f'Unit {i} Test',i,0))
    registry.extend([('MSC 201','stats-final','Final Exam',0,0),('MSC 201','stats-diagnostic','Diagnostic Exam',0,0)])
    index=[]
    for course,slug,title,fn,end in registry:
        if args.only and slug!=args.only:continue
        writer=PdfWriter();records=[];seen=set();item_seen={}
        saved=json.loads((OUT/(slug+'-20-versions.json')).read_text()) if args.reformat else None
        for i in range(args.count):
            if saved:
                seed=saved[i]['seed'];version=saved[i]['version'];v=saved[i]['constructor_variant'];qs=saved[i]['questions']
            else:
                seed=secrets.randbits(32);version=str(10000+secrets.randbelow(90000));v=i if not slug.endswith('diagnostic') else i+1
                if course=='MSC 201':qs=stats_questions(fn,seed)
                else:
                    qs=fractions(v) if slug=='98-fractions' else fn(v)
                    qs=improve(qs,slug,v)
                    if slug.endswith(('final','diagnostic')) and course.startswith('TSM'):
                        extra=[q for q in qs if not q['id'].startswith('I')]
                        attempt=0
                        while True:
                            fresh=institutional(course,seed+attempt,i%4)
                            if all(json.dumps(q['math']) not in item_seen.get(q['id'],set()) for q in fresh):break
                            attempt+=1
                        for q in fresh:item_seen.setdefault(q['id'],set()).add(json.dumps(q['math']))
                        qs=fresh+extra
                    if slug.endswith(('final','diagnostic')) and course=='MATH 101':
                        qs=[math101_solving(i,seed) if q['id']=='M101-solving' else q for q in qs]
                    random.Random(seed).shuffle(qs)
            assert sum(10 for q in qs)==100 if course=='MSC 201' else sum(r['points'] for q in qs for r in q['rows'])==100
            identity=hashlib.sha256(json.dumps(sorted(qs,key=lambda q:q['id']),sort_keys=True).encode()).hexdigest();assert identity not in seen,(slug,'duplicate form');seen.add(identity)
            a=dict(course=course,title=course+' '+title,version=version,questions=qs,seed=seed)
            if course=='MSC 201':reader,n,keyidx,geometry=stats_packet(a)
            else:
                reader,n,keyidx,pages,cols=L.packet(a)
                geometry=[]
                for pi,blocks in enumerate(pages):
                    y=L.TOP
                    for b in blocks:
                        rows=[];ry=y
                        for row in b['rows']:rows.append(dict(top=ry,bottom=ry-row['height'],label=row['source']['label'],points=row['source']['points']));ry-=row['height']
                        geometry.append(dict(question=b['num'],page=pi,top=y,bottom=y-b['height'],rows=rows));y-=b['height']
            start=len(writer.pages);assert start%2==0 and keyidx%2==0
            writer.append(reader,import_outline=False)
            if len(writer.pages)%2:writer.add_blank_page(width=612,height=792)
            records.append(dict(version=version,seed=seed,constructor_variant=v,start=start,test_pages=n,key_start=start+keyidx,packet_pages=len(writer.pages)-start,geometry=geometry,questions=qs))
            print(slug,i+1,'student pages',n,flush=True)
        path=OUT/(slug+'-20-versions.pdf');writer.add_metadata({'/Title':course+' '+title+' - 20 versions','/Author':'Jeremy Kastine'})
        with path.open('wb') as f:writer.write(f)
        path.with_suffix('.json').write_text(json.dumps(records,indent=2)+'\n')
        index.append(dict(course=course,assessment=slug,file=path.name,versions=len(records),pages=len(writer.pages),student_pages=sorted({r['test_pages'] for r in records})))
        print('SAVED',path.name,len(writer.pages),flush=True)
    manifest=OUT/'manifest.json'
    with (OUT/'.manifest.lock').open('w') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX)
        old=json.loads(manifest.read_text()) if manifest.exists() else []
        old=[a for a in old if a['assessment'] not in {b['assessment'] for b in index}]
        manifest.write_text(json.dumps(sorted(old+index,key=lambda a:a['assessment']),indent=2)+'\n')
if __name__=='__main__':main()
