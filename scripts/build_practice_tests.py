#!/usr/bin/env python3
"""Generate the course practice assessments and indexes from verified symbolic data."""
from pathlib import Path
from io import BytesIO
from functools import lru_cache
import json, random, re, math, argparse
from datetime import datetime
from zoneinfo import ZoneInfo
from xml.sax.saxutils import escape
import sympy as S
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.mathtext import math_to_image
from matplotlib.font_manager import FontProperties
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether, PageBreak, Flowable, Table, TableStyle
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader, PdfWriter, Transformation

ROOT=Path(__file__).resolve().parents[1]
for name,font in [('DV','DejaVuSans.ttf'),('DVB','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+font))
pdfmetrics.registerFontFamily('DV',normal='DV',bold='DVB',italic='DV',boldItalic='DVB')
INK='#172A3A'
matplotlib.rcParams.update({'mathtext.fontset':'dejavusans','pdf.fonttype':42,'font.family':'DejaVu Sans'})
BODY=ParagraphStyle('body',fontName='DV',fontSize=10.4,leading=14,spaceAfter=4,textColor=HexColor(INK))
SMALL=ParagraphStyle('small',parent=BODY,fontSize=8.6,leading=11.5)
TITLE=ParagraphStyle('title',parent=BODY,fontName='DVB',fontSize=17,leading=21,spaceAfter=7)
x,y=S.symbols('x y',real=True)
CHECKS=[]

def tex(e):
    return S.latex(e).replace('\\left','').replace('\\right','').replace('\\log','\\mathrm{log}')
def eq(a,b): return tex(a)+' = '+tex(b)
def par(a): return '('+tex(a)+')'
def frac(a,b): return r'\frac{'+tex(a)+'}{'+tex(b)+'}'
def ans(label,value,pts,plain=False): return {'label':label,'answer':str(value) if plain else value,'points':int(pts),'plain':bool(plain)}
def question(fid,prompt,maths,rows,**kw):
    assert sum(r['points'] for r in rows) in (10,20),(fid,rows)
    return dict(id=fid,prompt=prompt,math=maths,rows=rows,**kw)
def solved(fid,lhs,rhs=0,expected=None,denoms=()):
    diff=S.together(lhs-rhs)
    if denoms:
        cleared=S.cancel((lhs-rhs)*S.prod(denoms))
        num,den=S.fraction(cleared)
        assert not den.has(x),(fid,cleared)
    else:
        num=S.fraction(diff)[0]
    candidates=S.solve(num,x)
    valid=[z for z in candidates if all(S.simplify(d.subs(x,z))!=0 for d in denoms) and S.simplify((lhs-rhs).subs(x,z))==0]
    if expected is not None: assert set(valid)==set(map(S.sympify,expected)),(fid,valid,expected)
    CHECKS.append({'id':fid,'equation':eq(lhs,rhs),'candidates':[str(z) for z in candidates],'valid':[str(z) for z in valid]})
    return valid,candidates
def solution_tex(roots): return 'x = '+r',\ '.join(tex(z) for z in roots)
def exact(fid,e,expected=None):
    result=S.cancel(S.expand(e))
    if expected is not None: assert S.simplify(result-expected)==0,(fid,result,expected)
    CHECKS.append({'id':fid,'expression':tex(e),'result':tex(result)})
    return result

class Vector(Flowable):
    def __init__(self,data,overlays,maxwidth=510,maxheight=None):
        super().__init__();self.page=PdfReader(BytesIO(data)).pages[0]
        w,h=float(self.page.mediabox.width),float(self.page.mediabox.height)
        self.scale=min(1,maxwidth/w,maxheight/h if maxheight else 1)
        self.width,self.height=w*self.scale,h*self.scale;self.overlays=overlays;self.hAlign='LEFT'
    def draw(self):
        px,py=self.canv.absolutePosition(0,0)
        self.overlays.append((self.canv.getPageNumber()-1,self.page,self.scale,px,py,self.width,self.height))

@lru_cache(None)
def mathpdf(t,size=13):
    b=BytesIO();math_to_image('$'+t+'$',b,prop=FontProperties(size=size),dpi=72,format='pdf',color=INK);return b.getvalue()
def formula(t,overlays,size=13,maxwidth=510):
    f=Vector(mathpdf(t,size),overlays,maxwidth=maxwidth)
    assert f.scale>.72,('formula too wide',t,f.scale)
    return f

@lru_cache(None)
def graphpdf(serial):
    g=json.loads(serial);kind=g['kind'];fig,ax=plt.subplots(figsize=(5.8,2.65))
    ax.spines[['top','right']].set_visible(False);ax.spines[['left','bottom']].set_position('zero')
    ax.grid(color='#d4d9dd',linewidth=.4);ax.tick_params(labelsize=7)
    if kind in ('blank','line'):
        fig.set_size_inches(3.5,3.5);ax.set(xlim=(-10,10),ylim=(-10,10),xticks=range(-10,11,2),yticks=range(-10,11,2));ax.set_aspect('equal')
        ax.set_xticks(range(-10,11),minor=True);ax.set_yticks(range(-10,11),minor=True);ax.grid(which='minor',color='#e5e7eb',linewidth=.3)
        ax.annotate('',xy=(10,0),xytext=(9,0),arrowprops=dict(arrowstyle='->',lw=.8));ax.annotate('',xy=(0,10),xytext=(0,9),arrowprops=dict(arrowstyle='->',lw=.8))
        if kind=='line':
            xx=np.linspace(-10,10,201);ax.plot(xx,float(g['m'])*xx+g['b'],color=INK,lw=1.5)
            for px in [0,g.get('point',2)]: ax.plot(px,float(g['m'])*px+g['b'],'o',color=INK,ms=3)
    elif kind=='behavior':
        pts=np.array(g['points']);ax.plot(pts[:,0],pts[:,1],'-o',color=INK,lw=1.5,ms=3)
        for px,py in pts:ax.annotate(f'({px}, {py})',(px,py),xytext=(4,7),textcoords='offset points',fontsize=8)
        ax.set(xlim=(pts[:,0].min()-1,pts[:,0].max()+1),ylim=(pts[:,1].min()-2,pts[:,1].max()+2));ax.set_xticks(range(int(pts[:,0].min()),int(pts[:,0].max())+1))
    elif kind=='transform':
        pts=np.array(g['points'],dtype=float);new=pts.copy()
        if g['mode']=='shift':new+=np.array([g['h'],g['k']])
        elif g['mode']=='vertical':new[:,1]*=g['a']
        else:new[:,0]/=g['a']
        ax.plot(pts[:,0],pts[:,1],'-o',label='f',color=INK,lw=1.6,ms=3)
        ax.plot(new[:,0],new[:,1],'--s',label='g',color='#5c6873',lw=1.6,ms=3)
        both=np.vstack([pts,new]);ax.set(xlim=(both[:,0].min()-1,both[:,0].max()+1),ylim=(both[:,1].min()-1,both[:,1].max()+1));ax.legend(loc='upper left',fontsize=9,framealpha=.9)
        ax.set_xticks(np.arange(math.floor(both[:,0].min()),math.ceil(both[:,0].max())+1));ax.set_yticks(np.arange(math.floor(both[:,1].min()),math.ceil(both[:,1].max())+1))
    elif kind=='polynomial':
        roots=g['roots'];a=g['a'];xx=np.linspace(min(roots)-.65,max(roots)+.65,701);yy=np.ones_like(xx)*a
        for root,mult in zip(roots,g['multiplicities']):yy*=(xx-root)**mult
        ax.plot(xx,yy,color=INK,lw=1.6);px,py=g['point'];ax.plot(px,py,'o',color=INK,ms=4)
        ax.annotate(f'({px}, {py})',(px,py),xytext=(8,12),textcoords='offset points',fontsize=9,bbox=dict(facecolor='white',edgecolor='none',pad=1.5))
        inside=(xx>=min(roots)) & (xx<=max(roots))
        cap=max(8,abs(py)*1.8,float(np.max(np.abs(yy[inside])))*1.12)
        ax.set(xlim=(xx.min(),xx.max()),ylim=(-cap,cap));ax.set_xticks(range(math.floor(xx.min()),math.ceil(xx.max())+1))
        for r,m in zip(roots,g['multiplicities']):ax.plot(r,0,'o',color=INK,ms=3)
    elif kind=='exponential':
        # The fixed window gives all four edge labels room; label positions are data values.
        xx=np.linspace(-2,2,401);cols=g['curves']
        for j,(a,b) in enumerate(cols):
            yy=a*b**xx;ax.plot(xx,yy,color=INK,lw=1.3,linestyle='-')
            for side in [-2,2]:ax.text(side,a*b**side,chr(65+j),fontsize=9,ha='right' if side<0 else 'left',va='center',bbox=dict(facecolor='white',edgecolor='none',pad=.4))
        maxy=max(a*b**t for a,b in cols for t in [-2,2]);ax.set(xlim=(-2.35,2.35),ylim=(-.5,maxy*1.12));ax.set_xticks([-2,-1,0,1,2])
    else:raise ValueError(kind)
    ax.set_xlabel('x',loc='right',fontsize=9);ax.set_ylabel('y',loc='top',rotation=0,fontsize=9)
    ax.spines['left'].set_linewidth(.9);ax.spines['bottom'].set_linewidth(.9)
    fig.tight_layout(pad=.8);b=BytesIO();fig.savefig(b,format='pdf');plt.close(fig);return b.getvalue()

def build(a):
    from algebra_test_layout import build as build_combined
    return build_combined(a)

# Question constructors are below. All answers are computed from their source data.
def arithmetic98(v):
    k=v+2
    ops=[(f'{7+k}-(-{3+k})',10+2*k),(f'(-{4+k})(-{2+k})',(4+k)*(2+k)),(f'-{6+k}-{3+k}',-9-2*k),(frac(k+5,0),'Undefined')]
    if v==1:ops[0]=(f'-{7+k}-(-{3+k})',-4);ops[2]=(f'-{6+k}+(-{9+k})',-15-2*k);ops[3]=(frac(0,k+5),0)
    random.Random(400+v).shuffle(ops)
    q1=question('A98-signs','Evaluate each expression.',[rf'({chr(97+i)})\quad '+p for i,(p,a) in enumerate(ops)],[ans('('+chr(97+i)+')',str(a),5,True) for i,(p,a) in enumerate(ops)])
    q2=fraction_reduction(v,'A98-frac')
    e=(k+1)*x-(k+2)*y-k;px=-k;py=k+1;a=exact('A98-eval',e.subs({x:px,y:py}))
    q3=question('A98-eval',f'Evaluate at x = {px}, y = {py}.',[tex(e)],[ans('Value',tex(a),20)])
    e=(v+1)*x*x-(v+3)*x+v+2
    vals=[10,-10,0];weights=[7,7,6]
    q4=question('A98-quad','Evaluate the same expression at (a) x = 10, (b) x = -10, and (c) x = 0.',[tex(e)],[ans('('+chr(97+i)+')',tex(exact('A98-quad',e.subs(x,z))),weights[i]) for i,z in enumerate(vals)])
    l=x*(x+k);r=x*x+k*x+(0 if v==0 else x if v==1 else k)
    q5=comparison('A98-compare',l,r,[k,-k,0],20)
    return [q1,q2,q3,q4,q5]

def fraction_reduction(v,fid):
    pairs=[[(14,21),(42,66)],[(25,35),(60,84)],[(21,35),(70,110)]][v]
    if v==1:pairs.reverse()
    gcds=[math.gcd(*p) for p in pairs];assert sorted(len(S.factorint(g)) for g in gcds)==[1,2]
    return question(fid,'Reduce each fraction to lowest terms.',[rf'({chr(97+i)})\quad '+frac(n,d) for i,(n,d) in enumerate(pairs)],[ans('('+chr(97+i)+')',tex(S.Rational(n,d)),10) for i,(n,d) in enumerate(pairs)])

def comparison(fid,l,r,inputs,points):
    rows=[];matches=[]
    for i,z in enumerate(inputs):
        a,b=S.simplify(l.subs(x,z)),S.simplify(r.subs(x,z));assert a.is_integer and b.is_integer
        match=a==b;matches.append(match);rows.append(ans('x = '+str(z),f'Left {a}; right {b}; '+('yes' if match else 'no'),points//5,True))
    if all(matches):con='All tested values work; this alone does not prove an identity.'
    elif any(matches):con='Only the listed matching value works; the equation is not an identity.'
    else:con='None of these values works; this alone does not prove no solution.'
    rows.append(ans('Conclusion',con,points-3*(points//5),True))
    table=[['x','Left value','Right value','Equal?']]+[[z,'','',''] for z in inputs]
    return question(fid,'Complete the table by evaluating each side separately. State what the tested values establish; do not solve the equation.',[eq(l,r)],rows,table=table)

def polynomials98(v):
    k=v+1
    # Compact, one-line sums: four exponents across two three-term factors.
    p=2*x**3-(k+1)*x**2-k
    q=-(k+2)*x**3+(k+1)*x+k+2
    r=(k+2)*x**4-2*x*x+x-k;t=3*x**4+(k+1)*x*x-4
    e=-(k+2)*x**2*(2*x**3-k*x+3)
    small=[((x+k)*(x-k-2)),((k+1)*x-k)*((k+2)*x+3)]
    factors=[(x-k,2*x*x+x+1),(x+2,2*x**3-x*x+3*x-k),(x*x+x-k,2*x*x-x+3)][v]
    gcf=(k+2)*x**(v+1);inside=2*x*x+(-1 if v%2 else 1)*3*x+5
    gp=S.expand(gcf*inside)
    roots=[(2,3),(-2,-5),(-3,5)][v]
    mono=S.expand((x+roots[0])*(x+roots[1]))
    assert S.Poly(mono,x).LC()==1 and len(S.Poly(mono,x).terms())==3
    assert S.expand(S.factor(gp)-gp)==0 and S.expand(S.factor(mono)-mono)==0
    return [question('P98-addsub','(a) Add and simplify. (b) Subtract and simplify.',
      [r'(a)\quad '+par(p)+' + '+par(q),r'(b)\quad '+par(r)+' - '+par(t)],
      [ans('(a)',tex(exact('P98-add',p+q)),10),ans('(b)',tex(exact('P98-sub',r-t)),10)]),
      question('P98-dist','Distribute and simplify.',[f'-{k+2}x^2'+par(2*x**3-k*x+3)],[ans('Polynomial',tex(exact('P98-dist',e)),20)]),
      question('P98-binomial','Multiply and simplify both products.',[rf'(a)\quad (x+{k})(x-{k+2})',rf'(b)\quad ({k+1}x-{k})({k+2}x+3)'],[ans('(a)',tex(exact('P98-binomial-a',small[0])),10),ans('(b)',tex(exact('P98-binomial-b',small[1])),10)]),
      question('P98-large','Multiply and simplify.',[par(factors[0])+par(factors[1])],[ans('Polynomial',tex(exact('P98-large',factors[0]*factors[1])),20)]),
      question('P98-factor','(a) Factor out the greatest common factor. (b) Factor the trinomial.',
      [r'(a)\quad '+tex(gp),r'(b)\quad '+tex(mono)],
      [ans('(a)',tex(S.factor(gp)),10),ans('(b)',tex(S.factor(mono)),10)])]

def fractions98(v):
    add=[[(1,6),(1,3)],[(2,5),(1,6)],[(1,12),(1,4)]][v]
    sub=[[(3,4),(1,6)],[(5,6),(1,3)],[(5,6),(1,4)]][v]
    def combined(pair,sgn):
        (a,b),(c,d)=pair;l=math.lcm(b,d);n=a*(l//b)+sgn*c*(l//d);return n,l
    ag=math.gcd(*combined(add,1));sg=math.gcd(*combined(sub,-1));assert (ag>1)+(sg>1)==1
    triples=[[(14,15),(25,21),(9,10)],[(4,1),(3,8),(2,9)],[(22,15),(25,33),(9,10)]][v]
    divs=[[(4,1),(8,5)],[(28,45),(42,35)],[(6,1),(9,4)]][v]
    assert sum(d==1 for _,d in triples+divs)==1
    extra=[([(2,7),(3,7)],'+'),([(2,3),(5,7)],r'\times'),([(2,3),(5,7)],r'\div')][v]
    tasks=[('F98-add',add,'+'),('F98-sub',sub,'-'),('F98-mult',triples,r'\times'),('F98-div',divs,r'\div'),('F98-extra',extra[0],extra[1])]
    out=[]
    for fid,pairs,op in tasks:
        values=[S.Rational(n,d) for n,d in pairs];e=values[0]
        for z in values[1:]:e=e+z if op=='+' else e-z if op=='-' else e*z if op==r'\times' else e/z
        assert e>0
        expr=(' '+op+' ').join(tex(S.Integer(n)) if d==1 else frac(n,d) for n,d in pairs)
        prompt='Compute and give the result in lowest terms.'
        out.append(question(fid,prompt,[expr],[ans('Result',tex(e),20)]));exact(fid,e)
    return out

def linear98(v):
    k=v+2;rf=[S.Rational(3,2),S.Integer(2),S.Rational(5,3)][v];rl=[S.Integer(3),S.Rational(5,3),S.Integer(-2)][v]
    lhs=(x+k)/3+(x-1)/4;rhs=lhs.subs(x,rf);solved('L98-frac',lhs,rhs,[rf])
    m=0 if v==1 else (3 if v==2 else 1);const=(3+m)*rl-3*k-(k+1)
    ll=3*(2*x-k)-(x+k+1)+m*x;rr=2*x+const;solved('L98-dist',ll,rr,[rl])
    p,q=v+2,v+1;b=q-2*p
    system=[eq(y,2*x+b),eq(x+y,p+q)];assert S.solve([y-2*x-b,x+y-p-q],[x,y])=={x:p,y:q}
    general=[eq(2*x+3*y,2*p+3*q),eq(3*x+5*y,3*p+5*q)];assert S.solve([2*x+3*y-2*p-3*q,3*x+5*y-3*p-5*q],[x,y])=={x:p,y:q}
    if v==0:ex=[f'3(x+{k})+1 = 3x+{3*k+2}'];answer='No solution; simplifying gives 1 = 2.'
    elif v==1:ex=[f'4(x-{k})+{4*k+2} = 2(2x+1)'];answer='All real numbers; both sides reduce to 4x + 2.'
    else:ex=[eq(2*x+3*y,7),eq(4*x+6*y,15)];answer='No solution; doubling the first equation contradicts the second.'
    return [question('L98-frac','Solve.',[frac(x+k,3)+' + '+frac(x-1,4)+' = '+tex(rhs)],[ans('Solution',solution_tex([rf]),20)]),
      question('L98-dist','Solve.',[f'3(2x-{k})-(x+{k+1})'+(' + '+str(m)+'x' if m else '')+' = '+tex(rr)],[ans('Solution',solution_tex([rl]),20)]),
      question('L98-basic','Solve the system.',system,[ans('Solution',tex(S.Tuple(p,q)),20)]),
      question('L98-general','Solve the system.',general,[ans('Solution',tex(S.Tuple(p,q)),20)]),
      question('L98-exception','Solve and state the complete solution set.',ex,[ans('Solution set',answer,20,True)])]

def arithmetic99(v):
    k=v+2;q1=fraction_reduction(v,'A99-frac')
    roots=[((v+5)**2,v+5),(-((v+7)**2),str(v+7)+'i')]
    if v==1:roots.reverse()
    q2=question('A99-root','Evaluate the principal square root in each part.',[rf'({chr(97+i)})\quad '+r'\sqrt{'+str(n)+'}' for i,(n,a) in enumerate(roots)],[ans('('+chr(97+i)+')',str(a),10,True) for i,(n,a) in enumerate(roots)])
    prime=[2,3,5][v];mult=[3,5,2][v];rad=mult*mult*prime
    q3=question('A99-simplify','Simplify the square root.',[r'\sqrt{'+str(rad)+'}'],[ans('Radical',tex(S.sqrt(rad)),20)])
    if v<2:
        e=(v+1)*x*x-(v+3)*x+2 if v==0 else 2*(x-1)*(x+3)
        vals=[v+2,-v-2];q4=question('A99-eval',f'Evaluate at (a) x = {vals[0]} and (b) x = {vals[1]}.',[tex(e)],[ans('('+chr(97+i)+')',tex(exact('A99-eval',e.subs(x,z))),10) for i,z in enumerate(vals)])
    else:
        a,b,c=2,-5,2;rt=S.solve(a*x*x+b*x+c,x)
        q4=question('A99-formula','Substitute a = 2, b = -5, c = 2 into the formula. Evaluate both branches.',[r'x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}'],[ans('Both values',solution_tex(rt),20)])
    a,b=k,k+1;l=(x*x-a*a)/(x-a);delta=0 if v==0 else x if v==1 else 1;r=((x+a)*(x+b)+delta*(x+b))/(x+b)
    q5=comparison('A99-test',l,r,[k+4,-k-4,0],20)
    q5['math']=[frac(x*x-a*a,x-a)+' = '+frac(S.expand((x+a)*(x+b)+delta*(x+b)),x+b)]
    return [q1,q2,q3,q4,q5]

def polynomials99(v):
    k=v+2;prod=((k)*x-3)*((k+1)*x+2);inside=2*x*x-x+(v+3);gcf=(v+2)*x*x;poly=S.expand(gcf*inside)
    mon=(x-(v+2))*(x+(v+4));ds=[x*x-25,4*x*x-9,9*x*x-16][v]
    small=[((2*x+1)*(x-3),2*x*x+x+3),((3*x-2)*(x+1),3*x*x+2*x+1),((2*x-3)*(x+2),2*x*x+x+2)][v]
    if v==1:small=small[::-1]
    rich=[(3*x+5)*(4*x+3),(3*x+4)*(4*x+3),(3*x-4)*(5*x-3)][v];rp=S.Poly(S.expand(rich),x);a,b,c=rp.all_coeffs();ac=a*c
    pairs=[(d,ac//d) for d in range(1,math.isqrt(abs(int(ac)))+1) if ac%d==0];assert len(pairs)>=8
    split=next((u,w) for u,w in pairs if u+w==abs(b));u,w=split
    if b<0:u,w=-u,-w
    return [question('P99-mult','Multiply and simplify.',[f'({k}x-3)({k+1}x+2)'],[ans('Polynomial',tex(exact('P99-mult',prod)),20)]),
      question('P99-gcf','Factor out the greatest common factor.',[tex(poly)],[ans('Factored form',tex(gcf)+par(inside),20)]),
      question('P99-basic','Factor completely.',[rf'(a)\quad '+tex(S.expand(mon)),rf'(b)\quad '+tex(ds)],[ans('(a)',tex(S.factor(mon)),10),ans('(b)',tex(S.factor(ds)),10)]),
      question('P99-small','Factor completely over the integers, or write prime.',[rf'({chr(97+i)})\quad '+tex(S.expand(e)) for i,e in enumerate(small)],[ans('('+chr(97+i)+')','Prime' if S.Poly(e,x).discriminant()<0 else tex(S.factor(e)),10,S.Poly(e,x).discriminant()<0) for i,e in enumerate(small)]),
      question('P99-group','Factor completely.',[tex(rp.as_expr())],[ans('Factored form',tex(S.factor(rich)),20)])]

def rational99(v):
    h=v+2;b=v+4;a=v+3
    n=S.expand((2*x+1)*(x-h));d=S.expand(3*(x-h)*(x+b));simple=n/d
    k=h+3 if v!=1 else h-3
    den=S.expand((x-h)*(x-k));op='+' if v!=1 else '-'
    cancel=1/(x-h)+(k-h)/den
    other=2/(x-h)+(-1 if v!=1 else 1)/den
    add=cancel if v!=1 else other;sub=other if v!=1 else cancel
    addtex=frac(1 if v!=1 else 2,x-h)+' + '+frac(3 if v!=1 else 1,den)
    subtex=frac(2 if v!=1 else 1,x-h)+' - '+frac(1 if v!=1 else 3,den)
    mul=(6*x*(x-h))/(9*(x-h)*(x+b))*(x+b)/x
    div=(x*x-a*a)/S.expand((x-a)*(x+b))/((x+a)/(x+b))
    tasks=[('R99-simple',frac(n,d),simple,'Simplify.'),('R99-add',addtex,add,'Add and simplify.'),('R99-sub',subtex,sub,'Subtract and simplify.'),('R99-mul',frac(S.expand(6*x*(x-h)),S.expand(9*(x-h)*(x+b)))+r'\times'+frac(x+b,x),mul,'Multiply and simplify.'),('R99-div',frac(x*x-a*a,S.expand((x-a)*(x+b)))+r'\div'+frac(x+a,x+b),div,'Divide and simplify.')]
    out=[]
    for fid,t,e,prompt in tasks:out.append(question(fid,prompt,[t],[ans('Expression',tex(S.factor(exact(fid,e))),20)]))
    assert S.simplify(cancel-1/(x-k))==0
    assert S.degree(S.fraction(S.cancel(other))[0],x)==1
    return out

def equations99(v):
    h=v+2;r=h+2;d=h+1;K=h+r-1
    l=2*h/(x*x-h*h)+(x-d)/(x-h);rr=K/(x+h)
    valid,cand=solved('E99-rquad',l,rr,[r],[x-h,x+h]);assert set(cand)=={S.Integer(h),S.Integer(r)}
    u=v+1;w=u+3;p=u+1;A=2*(v+2);c=v+3;B=c*(p-u)-A*(p-w)//2
    l2=A/(2*x-2*u)+B/S.expand((x-u)*(x-w));rr2=c/(x-w);valid2,cand2=solved('E99-rlinear',l2,rr2,[p],[x-u,x-w]);assert len(cand2)==1
    poly=S.expand((x-(v+1))*(x+v+4));rt,_=solved('E99-factor',poly)
    qp=2*x*x+(v+1)*x-(v+2);qr,_=solved('E99-formula',qp);assert not S.sqrt(S.Poly(qp,x).discriminant()).is_integer
    sh=v-1;sk=v+2
    return [question('E99-factor','Solve.',[eq(poly,0)],[ans('Solutions',solution_tex(rt),20)]),
      question('E99-formula','Solve. Give exact simplified solutions.',[eq(qp,0)],[ans('Solutions',solution_tex(qr),20)]),
      question('E99-sqrt','Solve.',['2'+par(x-sh)+rf'^2 = {2*sk*sk}'],[ans('Solutions',solution_tex([sh-sk,sh+sk]),20)]),
      question('E99-rquad','Solve.',[frac(2*h,x*x-h*h)+' + '+frac(x-d,x-h)+' = '+frac(K,x+h)],[ans('Solution',solution_tex([r]),20)]),
      question('E99-rlinear','Solve.',[frac(A,2*x-2*u)+' + '+frac(B,S.expand((x-u)*(x-w)))+' = '+frac(c,x-w)],[ans('Solution',solution_tex([p]),20)])]

def graph99(v):
    ms=[S.Rational(1,2),S.Rational(2,3),S.Rational(3,2)];m=ms[v];b=v-2
    # Standard form has negative slope and integer nonzero intercepts.
    A,B,C=[(2,3,12),(3,2,12),(1,2,6)][v]
    p,q=[(1,2),(2,1),(2,-1)][v];mm=S.Integer(v+1);nn=-S.Integer(v+2);bb=q-mm*p;cc=q-nn*p
    readm=[-S.Rational(1,2),-S.Rational(2,3),-S.Rational(3,2)][v];readb=v+1
    pointm=[S.Integer(2),S.Rational(1,3),S.Integer(-1)][v];pointb=v-1;xs=[1,4] if v==1 else [1,3];pts=[(z,pointm*z+pointb) for z in xs]
    return [question('G99-slope','Graph the line on the grid. Mark at least two points.',[eq(y,m*x+b)],[ans('Graph (booklet)',eq(y,m*x+b),20)],graph={'kind':'blank','answer_lines':[[float(m),float(b)]]}),
      question('G99-standard','Find both intercepts and graph through them on the grid.',[eq(A*x+B*y,C)],[ans('Intercepts',tex(S.Tuple(S.Rational(C,A),0))+r';\ '+tex(S.Tuple(0,S.Rational(C,B))),8),ans('Graph (booklet)',eq(y,-S.Rational(A,B)*x+S.Rational(C,B)),12)],graph={'kind':'blank','answer_lines':[[-A/B,C/B]]}),
      question('G99-system','Graph both lines on this grid and give their intersection.',[eq(y,mm*x+bb),eq(y,nn*x+cc)],[ans('Graph (booklet)','Both given lines meet at the reported solution.',12,True),ans('Ordered pair',tex(S.Tuple(p,q)),8)],graph={'kind':'blank','answer_lines':[[float(mm),float(bb)],[float(nn),float(cc)]]}),
      question('G99-read','Write the equation of the displayed line in slope-intercept form.',[],[ans('Equation',eq(y,readm*x+readb),20)],graph={'kind':'line','m':float(readm),'b':readb,'point':2 if v!=1 else 3}),
      question('G99-points','Find the slope-intercept equation through the two points.',[tex(S.Tuple(*pts[0]))+r';\ '+tex(S.Tuple(*pts[1]))],[ans('Equation',eq(y,pointm*x+pointb),20)])]
