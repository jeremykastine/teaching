"""Build the ten TSM 098 independent-practice packets and separate keys.

Run from the repository root with Python containing reportlab, matplotlib,
and pypdf. All calculations use exact rational or polynomial arithmetic.
"""
from __future__ import annotations
import io, json, math, random, re
from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams.update({'savefig.transparent': True, 'mathtext.fontset': 'dejavusans'})
from matplotlib.mathtext import math_to_image
from matplotlib.font_manager import FontProperties
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from pypdf import PdfReader, PdfWriter, Transformation

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'practice' / 'independent'
OUT.mkdir(parents=True, exist_ok=True)
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')
pdfmetrics.registerFont(TTFont('DV', str(FONT_DIR/'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('DVB', str(FONT_DIR/'DejaVuSans-Bold.ttf')))
NAVY, GRAY, LIGHT = map(HexColor, ['#163a5f','#52606d','#d9e2ec'])

def frac(n,d=1):
    n,d=int(n),int(d)
    assert d
    return str(n) if d==1 else rf'\frac{{{n}}}{{{d}}}'
def ft(q):
    q=F(q)
    return str(q.numerator) if q.denominator==1 else ('-' if q<0 else '')+frac(abs(q.numerator),q.denominator)
def poly(values):
    """Ascending coefficients -> conventional polynomial TeX."""
    parts=[]
    for power,coef in reversed(list(enumerate(values))):
        coef=F(coef)
        if not coef: continue
        mag=abs(coef)
        variable='' if power==0 else ('x' if power==1 else rf'x^{{{power}}}')
        term=('' if mag==1 and power else ft(mag))+variable
        parts.append((' - ' if coef<0 else ' + ',term))
    if not parts:return '0'
    return ('-' if parts[0][0]==' - ' else '')+parts[0][1]+''.join(s+t for s,t in parts[1:])
def mul(a,b):
    ans=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):ans[i+j]+=x*y
    return ans
def add(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def ev(a,x):return sum(F(v)*F(x)**i for i,v in enumerate(a))
def item(prompt,expr=None,answer=None,answer_text=None):
    assert answer is not None or answer_text
    return dict(prompt=prompt,expr=expr,answer=answer,answer_text=answer_text)
def prime(n):
    original=n;factors=[];d=2
    while d*d<=n:
        while n%d==0:factors.append(d);n//=d
        d+=1
    if n>1:factors.append(n)
    assert math.prod(factors)==original
    counts={x:factors.count(x) for x in sorted(set(factors))}
    return r'\cdot'.join(str(x) if k==1 else rf'{x}^{{{k}}}' for x,k in counts.items())

def reductions(values):
    return [item('Write in lowest terms.',frac(n,d),frac(n,d)+'='+ft(F(n,d))) for n,d in values]
def equivalents(values):
    return [item('Find the missing numerator.',frac(n,d)+'='+rf'\frac{{?}}{{{d*k}}}',rf'?={n*k}',f'Multiply numerator and denominator by {k}.') for n,d,k in values]
def comparisons(values):
    result=[]
    for n,d,a,b in values:
        equal=F(n,d)==F(a,b)
        result.append(item('Are these fractions equivalent? Justify.',frac(n,d)+r'\quad\mathrm{and}\quad'+frac(a,b),ft(F(n,d))+r'\quad\mathrm{and}\quad'+ft(F(a,b)), 'Yes; the reduced values match.' if equal else 'No; the reduced values differ.'))
    return result
def fraction_packet(topic,prime_first=False):
    if not prime_first:
        pages=[('Core: simplifying fractions',reductions([(18,24),(21,35),(28,42),(45,60),(48,72),(54,90),(64,80),(84,126)])),
        ('Core: signs and further reduction',reductions([(-24,36),(30,-45),(-42,-56),(0,19),(96,144),(150,210),(81,54),(128,160)])),
        ('Core: equivalent fractions',equivalents([(2,3,4),(3,5,6),(-4,7,3),(5,8,7),(7,9,4),(0,5,6),(11,6,5),(-3,10,8)]))]
    else:
        pages=[('Core: prime factorization',[item('Write as a product of prime factors.',str(n),str(n)+'='+prime(n)) for n in [36,48,60,72,84,90,120,180]]),
        ('Core: simplify using common prime factors',reductions([(36,84),(48,180),(72,108),(90,150),(126,210),(-84,132),(144,96),(-120,-168)])),
        ('Core: equivalent fractions',equivalents([(3,4,6),(5,6,5),(-2,9,4),(7,10,3),(4,15,4),(11,12,3),(-5,8,5),(0,7,9)]))]
    ext=comparisons([(6,8,9,12),(4,9,8,15),(-3,5,9,-15),(12,18,3,4)])
    ext+=reductions([(252,420),(-165,225)])
    ext+=[item('Explain why dividing only the numerator by 3 changes the value.',frac(9,12),frac(9,12)+r'\ne'+frac(3,12),'The original is 3/4; the new fraction is 1/4. Divide both parts by the same nonzero factor to preserve value.'),
          item('Can multiplying both numerator and denominator by zero produce an equivalent fraction? Explain.',None,None,'No. It produces 0/0, which is undefined.')]
    pages.append(('Extension: compare and explain',ext))
    return pages

def polynomial_packet(topic):
    rng=random.Random(topic);pages=[]
    base=[]
    for i in range(3):
        a=[rng.randint(-6,6) for _ in range(3)];b=[rng.randint(-6,6) for _ in range(3)]
        ans=add(a,b);assert all(ev(ans,x)==ev(a,x)+ev(b,x) for x in [-3,0,2])
        base.append(item('Combine like terms.',f'({poly(a)})+({poly(b)})',poly(ans)))
    for i in range(3):
        a=[0,rng.choice([-4,-3,2,5])];b=[rng.choice([-5,-2,3]),rng.choice([-3,2,4]),rng.choice([1,2,-1])]
        while any(q['expr']==f'{poly(a)}({poly(b)})' for q in base):b[0]+=1
        ans=mul(a,b);assert all(ev(ans,x)==ev(a,x)*ev(b,x) for x in [-2,1,3])
        base.append(item('Distribute and simplify.',f'{poly(a)}({poly(b)})',poly(ans)))
    pages.append(('Core: like terms and distribution',base))
    products=[]
    for i in range(6):
        a=[rng.choice([-5,-3,-1,2,4]),1] if i<4 else [rng.choice([-3,1,2]),rng.choice([-2,1,3]),1]
        b=[rng.choice([-4,-2,1,3]),rng.choice([1,2])] if i<4 else [rng.choice([-2,1,3]),rng.choice([-1,2]),1]
        ans=mul(a,b);assert all(ev(ans,x)==ev(a,x)*ev(b,x) for x in [-2,0,3])
        products.append(item('Multiply and combine like terms.',f'({poly(a)})({poly(b)})',poly(ans)))
    pages.append(('Core: polynomial multiplication',products))
    factors=[]
    for m,n in ([(2,5),(-3,-4),(6,-2),(-7,3)] if topic==16 else [(3,4),(-2,-6),(5,-3),(-8,2)]):
        a=[m,1];b=[n,1];factors.append(item('Factor completely; check by multiplying.',poly(mul(a,b)),f'({poly(a)})({poly(b)})'))
    for a,b in [([0,3],[4,2]),([-4,1],[4,1])]:
        factors.append(item('Factor completely; check by multiplying.',poly(mul(a,b)),f'{poly(a)}({poly(b)})' if a[0]==0 else f'({poly(a)})({poly(b)})'))
    # The first GCF example must be fully factored, including the coefficient 2.
    factors[-2]['answer']=r'6x(x+2)'
    pages.append(('Core: introductory factoring',factors))
    ext=[]
    for a,b in [([1,2,1],[-2,1,1]),([-3,1,2],[2,-1,1]),([2,1],[-4,0,1])]:
        ans=mul(a,b);ext.append(item('Multiply and simplify.',f'({poly(a)})({poly(b)})',poly(ans)))
    for m,n in [(4,-7),(-5,-5)]:
        ext.append(item('Factor completely and verify.',poly([m*n,m+n,1]),f'({poly([m,1])})({poly([n,1])})'))
    ext.append(item('Explain the error: only the first and last terms were multiplied.',r'(x+2)(x+3)=x^2+6',r'(x+2)(x+3)=x^2+5x+6','Every term in one factor must multiply every term in the other. The missing middle products are 3x and 2x.'))
    pages.append(('Extension: mixed polynomial practice',ext))
    return pages

def fraction_ops(topic):
    rng=random.Random(topic);pages=[]
    def pair(op,count):
        result=[]
        for i in range(count):
            a,b,c,d=[rng.randint(1,9),rng.choice([3,4,5,6,8,10,12]),rng.randint(1,9),rng.choice([2,3,4,5,6,8,10])]
            if i%3==1:a=-a
            if i%4==2:c=-c
            q1,q2=F(a,b),F(c,d)
            ans={'*':lambda:q1*q2,'/':lambda:q1/q2,'+':lambda:q1+q2,'-':lambda:q1-q2}[op]()
            sym={'*':r'\cdot','/':r'\div','+':'+','-':'-'}[op]
            expr=frac(a,b)+sym+'('+frac(c,d)+')'
            if op=='/':step=frac(a,b)+r'\cdot('+frac(d,c)+')'
            elif op=='*':step=frac(a*c,b*d)
            else:
                lcd=math.lcm(b,d);num=a*(lcd//b)+(1 if op=='+' else -1)*c*(lcd//d)
                step=frac(num,lcd)
                assert F(num,lcd)==ans
            result.append(item('Evaluate and simplify.',expr,step+'='+ft(ans)))
        return result
    if topic==20:
        pages=[('Core: multiplying fractions',pair('*',8)),('Core: dividing fractions',pair('/',8)),('Core: mixed multiplication and division',pair('*',4)+pair('/',4))]
    else:
        pages=[('Core: adding fractions',pair('+',8)),('Core: subtracting fractions',pair('-',8)),('Core: mixed addition and subtraction',pair('+',4)+pair('-',4))]
    ext=[]
    for i in range(6):
        a,b,c=F(rng.choice([-5,-3,2,4]),rng.choice([3,4,6])),F(rng.choice([-4,2,3,5]),rng.choice([5,6,8])),F(rng.choice([-3,1,2]),rng.choice([2,3,4]))
        if topic==20:
            expr=ft(a)+r'\cdot('+ft(b)+r')\div('+ft(c)+')';ans=a*b/c
        else:expr=ft(a)+'+('+ft(b)+')-('+ft(c)+')';ans=a+b-c
        ext.append(item('Evaluate and simplify. Show intermediate steps.',expr,ft(ans)))
    if topic==20:
        ext+=[item('Explain why dividing by a fraction is different from multiplying by that fraction.',r'\frac{2}{3}\div\frac{4}{5}',r'\frac{2}{3}\cdot\frac{5}{4}=\frac{5}{6}','Use the reciprocal of the divisor.'),item('Determine whether the expression is defined. Explain.',r'\frac{3}{7}\div0',None,'Undefined: no number multiplied by zero gives 3/7.')]
    else:
        ext+=[item('Explain the error and give the correct answer.',r'\frac{1}{3}+\frac{1}{4}=\frac{2}{7}',r'\frac{4}{12}+\frac{3}{12}=\frac{7}{12}','Use a common denominator; do not add the denominators.'),item('Evaluate. Explain why the sign of the answer makes sense.',r'\frac{2}{5}-\frac{7}{10}',r'\frac{4}{10}-\frac{7}{10}=-\frac{3}{10}','The amount subtracted is larger than the starting amount.')]
    pages.append(('Extension: longer expressions and reasoning',ext))
    return pages

def side_tex(terms):
    return '+'.join('('+fractex(a,b,d)+')' for a,b,d in terms)
def fractex(a,b,d):
    return poly([b,a]) if d==1 else rf'\frac{{{poly([b,a])}}}{{{d}}}'
def combined(terms):
    den=math.lcm(*(t[2] for t in terms));a=sum(x*(den//d) for x,y,d in terms);b=sum(y*(den//d) for x,y,d in terms)
    g=math.gcd(math.gcd(abs(a),abs(b)),den)
    return a//g,b//g,den//g
def equation(left,right,display=None):
    al,bl=sum((F(a,d) for a,b,d in left),F(0)),sum((F(b,d) for a,b,d in left),F(0))
    ar,br=sum((F(a,d) for a,b,d in right),F(0)),sum((F(b,d) for a,b,d in right),F(0))
    a,b=al-ar,br-bl
    if a:
        root=b/a;assert al*root+bl==ar*root+br
        answer=rf'x={ft(root)}';note='Check by substituting into the original equation.'
    else:
        answer=None;note='All real numbers (the two sides are identical).' if b==0 else 'No solution (the two sides cannot be equal).'
    A,B,D=combined(left);C,E,G=combined(right)
    steps=fractex(A,B,D)+'='+fractex(C,E,G)
    if D>1 or G>1:steps+='; '+f'{G}({poly([B,A])})={D}({poly([E,C])})'
    if answer:steps+='; '+answer
    return item('Solve and check in the original equation.',display or side_tex(left)+'='+side_tex(right),steps,note)
def ordinary_equations(topic):
    rng=random.Random(topic);basic=[];both=[];parentheses=[];extra=[]
    for i in range(6):
        a=rng.choice([-6,-4,-3,2,3,5]);b=rng.randint(-8,8);s=rng.randint(-5,6)
        basic.append(equation([(a,b,1)],[(0,a*s+b,1)],poly([b,a])+'='+str(a*s+b)))
    for i in range(6):
        a=rng.choice([-5,-3,2,4]);c=rng.choice([-2,1,3,5]);b=rng.randint(-7,7);e=rng.randint(-8,8)
        if a==c:c+=1
        both.append(equation([(a,b,1)],[(c,e,1)],poly([b,a])+'='+poly([e,c])))
    for i in range(6):
        k=rng.choice([-3,-2,2,3]);a=rng.choice([1,2,3]);b=rng.randint(-4,4);c=rng.randint(-3,3);e=rng.randint(-6,6);s=rng.randint(-5,5);r=k*(a*s+b)+e-c*s
        expr=f'{k}({poly([b,a])})'+('+' if e>=0 else '')+str(e)+'='+poly([r,c])
        parentheses.append(equation([(k*a,k*b+e,1)],[(c,r,1)],expr))
    extra=both[:2]+parentheses[-2:]
    extra+=[equation([(2,6,1)],[(2,6,1)],r'2(x+3)=2x+6'),equation([(3,-6,1)],[(3,1,1)],r'3(x-2)=3x+1')]
    # Replace repeated extension questions with additional independent equations.
    extra[:4]=[equation([(5,-3,1)],[(2,8,1)],'5x-3=2x+8'),equation([(-4,9,1)],[(3,-2,1)],'-4x+9=3x-2'),equation([(6,-11,1)],[(2,5,1)],'2(3x-4)-3=2x+5'),equation([(-6,-1,1)],[(3,-7,1)],'-3(2x+1)+2=3x-7')]
    return [('Core: two-term and short linear equations',basic),('Core: variable terms on both sides',both),('Core: equations with parentheses',parentheses),('Extension: mixed equations and special cases',extra)]
def fraction_equations(topic):
    rng=random.Random(topic);rows=[]
    while len(rows)<24:
        ds=rng.sample([2,3,4,5,6,8],3)
        left=[(rng.choice([-3,-2,1,2,3]),rng.randint(-5,5),ds[0]),(rng.choice([0,1,-1]),rng.randint(-4,4),ds[1])]
        right=[(rng.choice([-2,-1,0,1,2]),rng.randint(-6,6),ds[2])]
        al=sum((F(a,d) for a,b,d in left),F(0));bl=sum((F(b,d) for a,b,d in left),F(0));ar=sum((F(a,d) for a,b,d in right),F(0));br=sum((F(b,d) for a,b,d in right),F(0))
        if al==ar:continue
        root=(br-bl)/(al-ar)
        if abs(root)>15 or root.denominator>12:continue
        obj=equation(left,right)
        if any(q['expr']==obj['expr'] for q in rows):continue
        rows.append(obj)
    return [('Core: combine fractions on each side',rows[:6]),('Core: numerical denominators on both sides',rows[6:12]),('Core: signed numerators and fractions',rows[12:18]),('Extension: mixed fraction equations',rows[18:])]
def verify_pair(a,b,c,d,e,f,x,y):
    ok1=a*x+b*y==c;ok2=d*x+e*y==f
    return item('Does the ordered pair solve both equations? Show both substitutions.',rf'\left({x},{y}\right):\quad {poly2(a,b)}={c},\quad {poly2(d,e)}={f}',rf'{a}({x})+({b})({y})={a*x+b*y};\quad {d}({x})+({e})({y})={d*x+e*y}', 'Yes; both equations are true.' if ok1 and ok2 else 'No; at least one equation is false.')
def poly2(a,b):
    x=('' if a==1 else '-' if a==-1 else str(a))+'x'
    return x+(' + ' if b>=0 else ' - ')+('' if abs(b)==1 else str(abs(b)))+'y'
def packet32():
    p=ordinary_equations(32)
    p[2]=('Core: review linear equations with fractions',fraction_equations(32)[0][1])
    checks=[verify_pair(1,1,5,2,-1,1,2,3),verify_pair(1,-1,4,2,1,8,3,-1),verify_pair(2,3,1,1,-2,4,2,-1),verify_pair(1,2,7,3,-1,0,1,3),verify_pair(2,-1,5,1,1,4,3,1),verify_pair(3,1,-2,1,-1,-2,-1,1)]
    p[3]=('Extension: check proposed solutions of systems',checks)
    return p
def system(a,b,c,d,e,f,method):
    determinant=a*e-b*d
    if determinant:
        x,y=F(c*e-b*f,determinant),F(a*f-c*d,determinant)
        assert a*x+b*y==c and d*x+e*y==f
        ans=rf'(x,y)=\left({ft(x)},{ft(y)}\right)'
        check=rf'{ft(a*x)}+({ft(b*y)})={c};\quad {ft(d*x)}+({ft(e*y)})={f}'
        text='Substitute the resulting x and y into both original equations.'
    else:
        consistent=a*f==c*d and b*f==c*e
        ans=None;check=None;text='Infinitely many solutions; the second equation is a multiple of the first.' if consistent else 'No solution; eliminating a variable produces a contradiction.'
    expr=rf'{poly2(a,b)}={c}; {poly2(d,e)}={f}'
    if method=='substitution' and b==1:
        expr=rf'y={poly([c,-a])}; {poly2(d,e)}={f}'
        step=rf'{d}x+({e})({poly([c,-a])})={f}'
    else:
        l=math.lcm(abs(b),abs(e));k1=l//abs(b);k2=(-1 if b*e>0 else 1)*(l//abs(e));aa=k1*a+k2*d;cc=k1*c+k2*f
        step=rf'({k1})E_1+({k2})E_2:\quad {aa}x={cc}'
    return item(f'Solve by {method}; check both equations.',expr,step+('; '+ans if ans else '')+('; '+check if check else ''),text)
def packet34():
    rng=random.Random(34);p=[ordinary_equations(34)[2]];sub=[];elim=[]
    for i in range(6):
        x,y=rng.randint(-4,4),rng.randint(-4,4);a=rng.choice([-3,-2,1,2]);d=rng.choice([2,3,4]);e=rng.choice([1,2])
        if a*e==d:a+=1
        sub.append(system(a,1,a*x+y,d,e,d*x+e*y,'substitution'))
        a,b,d,e=rng.choice([1,2,3]),rng.choice([2,3]),rng.choice([2,4]),-rng.choice([2,3])
        elim.append(system(a,b,a*x+b*y,d,e,d*x+e*y,'elimination'))
    p += [('Core: systems by substitution',sub),('Core: systems by elimination',elim)]
    ext=[system(2,3,7,3,-2,4,'elimination'),system(-2,1,5,3,2,8,'substitution'),system(1,2,4,2,4,8,'elimination'),system(1,2,4,2,4,11,'elimination'),equation([(3,6,1)],[(3,6,1)],'3(x+2)=3x+6'),equation([(4,-5,1)],[(2,3,1)],'4x-5=2x+3')]
    p.append(('Extension: mixed equations and systems',ext));return p

META={
6:('Simplifying fractions',[4],'Review simplifying numerical fractions and creating equivalent fractions.'),
16:('Polynomial operations and basic factoring',[9,10,11,12,14,15],'Continue polynomial operations and introductory factoring.'),
17:('Polynomial operations and basic factoring',[9,10,11,12,14,15],'Continue polynomial operations and introductory factoring with a new practice set.'),
18:('Prime factorization and numerical fractions',[2,4],'Review prime factorization and simplifying numerical fractions.'),
20:('Multiplying and dividing numerical fractions',[19],'Continue multiplication and division of numerical fractions.'),
23:('Adding and subtracting numerical fractions',[21,22],'Continue addition and subtraction of numerical fractions.'),
27:('Linear equations',[24,25,26],'Continue linear equations, including equations with parentheses.'),
29:('Linear equations with numerical fractions',[28],'Continue linear equations with numerical fractions.'),
32:('Linear equations and checking systems',[24,25,26,28,31],'Review linear equations and check proposed ordered-pair solutions of systems.'),
34:('Linear equations and algebraic systems',[24,25,26,28,33],'Review linear equations and solve systems by substitution and elimination.')}

@lru_cache(maxsize=None)
def math_pdf(expr):
    stream=io.BytesIO();math_to_image('$'+expr.replace(r'\frac',r'\dfrac')+'$',stream,format='pdf',color='#163a5f',prop=FontProperties(size=12),dpi=300)
    return stream.getvalue()
def wrap(text,width,size=10):
    lines=[];line=''
    for word in text.split():
        candidate=(line+' '+word).strip()
        if pdfmetrics.stringWidth(candidate,'DV',size)>width and line:lines.append(line);line=word
        else:line=candidate
    if line:lines.append(line)
    return lines
def text(c,x,y,body,width,size=10,color=GRAY):
    c.setFont('DV',size);c.setFillColor(color)
    for line in wrap(body,width,size):c.drawString(x,y,line);y-=size*1.35
    return y
def make_pdf(topic,title,pages,key=False):
    name=f'topic-{topic:02d}-tsm-098-'+('answers' if key else 'practice')+'.pdf'
    path=OUT/name;buffer=io.BytesIO();c=canvas.Canvas(buffer,pagesize=(612,792));overlays=[];number=0
    c.setTitle(f'TSM 098 - {title} - '+('Answer key' if key else f'Independent practice during Topic {topic}'))
    c.setAuthor('Jeremy Kastine')
    for page_num,(heading,items) in enumerate(pages,1):
        c.setFillColor(NAVY);c.setFont('DVB',12);c.drawString(44,752,'TSM 098 | '+('ANSWER KEY' if key else 'INDEPENDENT PRACTICE'))
        y=text(c,44,726,title,524,18,NAVY)
        text(c,44,y-4,f'While TSM 099 studies Topic {topic}. Review: '+', '.join(f'Topic {n}' for n in META[topic][1])+'.',524,9)
        if not key:
            c.setFont('DV',9);c.setFillColor(GRAY);c.drawString(44,662,'Name: ______________________________    Date: __________________')
            text(c,44,641,'Complete the core pages first; use the extension page for remaining time. Show all work here or on separate paper. Check answers after attempting each section and correct errors.',524,9)
        else:text(c,44,655,'Equivalent forms are acceptable. Use these answers after attempting the problems; revisit the linked lecture notes for additional examples.',524,9)
        c.setFont('DVB',11);c.setFillColor(NAVY);c.drawString(44,598,heading)
        rows=math.ceil(len(items)/2);cell_h=510/rows
        page_overlays=[]
        for j,q in enumerate(items):
            number+=1;col=j%2;row=j//2;x=44+col*272;top=575-row*cell_h
            c.setStrokeColor(LIGHT);c.line(x,top+8,x+252,top+8)
            c.setFont('DVB',10);c.setFillColor(NAVY);c.drawString(x,top,f'{number}.')
            y=text(c,x+24,top,q['prompt'],228,9.3)
            expr=q['answer'] if key else q['expr']
            if expr:
                # Semicolon-separated worked steps become separate math lines.
                for formula in expr.split('; '):
                    b=math_pdf(formula);pg=PdfReader(io.BytesIO(b)).pages[0]
                    w,h=float(pg.mediabox.width),float(pg.mediabox.height)
                    scale=min(1.12,224/w)
                    y-=h*scale+8
                    page_overlays.append((b,x+24,y,scale))
            if key and q.get('answer_text'):y=text(c,x+24,y-5,q['answer_text'],228,8.4)
            assert y>top-cell_h+14, f'Overflow {topic=} {key=} {number=} {y=} {top-cell_h=}'
        overlays.append(page_overlays)
        c.setFont('DV',8);c.setFillColor(GRAY);c.drawString(44,34,f'Topic {topic} | '+('Answers' if key else 'Practice')+f' | {page_num} of {len(pages)}')
        c.showPage()
    c.save();reader=PdfReader(io.BytesIO(buffer.getvalue()));writer=PdfWriter()
    for pg,eqs in zip(reader.pages,overlays):
        for b,x,y,scale in eqs:
            eq=PdfReader(io.BytesIO(b)).pages[0]
            pg.merge_transformed_page(eq,Transformation().scale(scale).translate(x,y))
        writer.add_page(pg)
    writer.add_metadata({'/Title':f'TSM 098: {title}', '/Author':'Jeremy Kastine'})
    with path.open('wb') as out:writer.write(out)
    check=PdfReader(path);assert len(check.pages)==4
    assert all(p.extract_text().strip() for p in check.pages)
    return path,number

def main():
    manifest=[]
    for topic,(title,review,description) in META.items():
        if topic in [6,18]:pages=fraction_packet(topic,topic==18)
        elif topic in [16,17]:pages=polynomial_packet(topic)
        elif topic in [20,23]:pages=fraction_ops(topic)
        elif topic==27:pages=ordinary_equations(topic)
        elif topic==29:pages=fraction_equations(topic)
        elif topic==32:pages=packet32()
        else:pages=packet34()
        # Avoid repeated questions within a packet.
        qs=[q for _,items in pages for q in items]
        tokens=[(q['prompt'],q['expr']) for q in qs]
        assert len(tokens)==len(set(tokens)),f'Duplicate question in Topic {topic}'
        practice,count=make_pdf(topic,title,pages)
        answers,count2=make_pdf(topic,title,pages,key=True)
        assert count==count2
        manifest.append(dict(topic=topic,course='TSM 098',focus=description,review_topics=review,practice='independent/'+practice.name,answers='independent/'+answers.name,problem_count=count,core_problem_count=sum(len(items) for _,items in pages[:3]),pages=4,estimated_minutes='45-60 core; 15-25 extension'))
        print(f'Topic {topic}: {count} problems; practice and answers created',flush=True)
    (ROOT/'practice'/'independent-practice.json').write_text(json.dumps(manifest,indent=2)+'\n')

if __name__=='__main__':main()
