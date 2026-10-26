"""Combined algebra tests and vertically matched compact instructor keys."""
from pathlib import Path
from io import BytesIO
import json, math, hashlib
from xml.sax.saxutils import escape
import matplotlib.pyplot as plt
INK="#111111"
import numpy as np
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from pypdf import PdfReader, PdfWriter, Transformation

from functools import lru_cache
import build_practice_tests as old
ROOT=Path(__file__).resolve().parents[1]
old.INK='#111111'
W,H=612,792
M=36; INNER=540; SPLIT=396; TOP=656; BOTTOM=48
BODY=ParagraphStyle('combined',fontName='DV',fontSize=10.2,leading=13.3,textColor=HexColor('#111111'))
SMALL=ParagraphStyle('combined-small',parent=BODY,fontSize=8.5,leading=11)
KEY=ParagraphStyle('combined-key',parent=BODY,fontSize=9.3,leading=12)
TITLE=ParagraphStyle('combined-title',parent=BODY,fontName='DVB',fontSize=14,leading=17)

def para(s,width,style=BODY):
    p=Paragraph(escape(s),style); _,h=p.wrap(width,700); return p,h

def vector(data,width,height=None):
    page=PdfReader(BytesIO(data)).pages[0]
    w,h=float(page.mediabox.width),float(page.mediabox.height)
    scale=min(1,width/w,height/h if height else 1)
    return ('vector',page,w*scale,h*scale,scale)

def math_item(s,width,size=13):
    # Mathtext supports the common TeX subset used by the existing sources.
    s=s.replace(r'\log',r'\mathrm{log}')
    cache=ROOT/'tmp/algebra-render-cache';cache.mkdir(parents=True,exist_ok=True)
    path=cache/(hashlib.sha256((str(size)+'|'+s).encode()).hexdigest()+'.pdf')
    if not path.is_file():path.write_bytes(old.mathpdf(s,size))
    return vector(path.read_bytes(),width)

def math_answer(s,width):
    item=math_item(s,width,11.5)
    if item[4]>=.80:return item
    parts=[];start=0;depth=0;parens=0
    for i,char in enumerate(s):
        if char=='{':depth+=1
        elif char=='}':depth-=1
        elif char=='(':parens+=1
        elif char==')':parens-=1
        elif char in ',;' and depth==0 and parens==0:
            parts.append(s[start:i].strip());start=i+1
    parts.append(s[start:].strip())
    assert len(parts)>1,('answer needs line break',s,width)
    items=[]
    for part in parts:
        while part.startswith(r'\ '):part=part[2:].lstrip()
        items.append(math_item(part,width,11.5))
    assert all(i[4]>=.8 for i in items),('answer still too wide',s,width)
    return ('stack',items,max(i[2] for i in items),sum(i[3] for i in items)+3*(len(items)-1))

def draw_item(c,overlays,item,x,top):
    if item[0]=='stack':
        y=top
        for part in item[1]:y-=draw_item(c,overlays,part,x,y)+3
        return item[3]
    if item[0]=='paragraph':
        item[1].drawOn(c,x,top-item[2]); return item[2]
    _,page,w,h,scale=item
    overlays.append((c.getPageNumber()-1,page,scale,x,top-h))
    return h

def pitem(text,width,style=BODY):
    p,h=para(text,width,style); return ('paragraph',p,h)

@lru_cache(None)
def compact_graphpdf(serial):
    g=json.loads(serial);kind=g['kind'];fig,ax=plt.subplots(figsize=(4.8,1.5))
    ax.spines[['top','right']].set_visible(False);ax.spines[['left','bottom']].set_position('zero')
    ax.grid(color='#d4d9dd',linewidth=.4);ax.tick_params(labelsize=9)
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
        # Keep endpoint labels distinct even where decay curves approach the axis.
        xx=np.linspace(-2,2,401);cols=g['curves']
        for j,(a,b) in enumerate(cols):
            yy=a*b**xx;ax.plot(xx,yy,color=INK,lw=1.3,linestyle='-')
        maxy=max(a*b**t for a,b in cols for t in [-2,2])
        for side in [-2,2]:
            previous=-math.inf
            for val,j in sorted((a*b**side,j) for j,(a,b) in enumerate(cols)):
                label_y=max(val,maxy*.06,previous+maxy*.20)
                ax.annotate(chr(65+j),xy=(side,val),xytext=(side*1.24,label_y),
                            fontsize=9,ha='right' if side<0 else 'left',va='center',
                            bbox=dict(facecolor='white',edgecolor='none',pad=.4),
                            arrowprops=dict(arrowstyle='-',color='#666666',lw=.5))
                previous=label_y
        ax.set(xlim=(-2.75,2.75),ylim=(-.5,maxy*1.3));ax.set_xticks([-2,-1,0,1,2])
    else:raise ValueError(kind)
    ax.set_xlabel('x',loc='right',fontsize=9);ax.set_ylabel('y',loc='top',rotation=0,fontsize=9)
    ax.spines['left'].set_linewidth(.9);ax.spines['bottom'].set_linewidth(.9)
    fig.tight_layout(pad=.8);b=BytesIO();fig.savefig(b,format='pdf');plt.close(fig);return b.getvalue()


def graphdata(g,answer=False,qid=None):
    if g['kind']!='blank':return compact_graphpdf(json.dumps(g,sort_keys=True))
    if not answer:return old.graphpdf(json.dumps({'kind':'blank'}))
    assert g.get('answer_lines'),('missing key graph',qid)
    fig,ax=plt.subplots(figsize=(3.5,3.5))
    ax.spines[['top','right']].set_visible(False)
    ax.spines[['left','bottom']].set_position('zero')
    ax.set(xlim=(-10,10),ylim=(-10,10),xticks=range(-10,11,2),yticks=range(-10,11,2))
    ax.set_aspect('equal'); ax.tick_params(labelsize=7)
    ax.set_xticks(range(-10,11),minor=True);ax.set_yticks(range(-10,11),minor=True)
    ax.grid(which='both',color='#cccccc',linewidth=.35)
    x=np.linspace(-10,10,201)
    lines=g['answer_lines']
    for m,b in lines:ax.plot(x,m*x+b,color='black',lw=1.3)
    if len(lines)==2:
        (m1,b1),(m2,b2)=lines
        px=(b2-b1)/(m1-m2);py=m1*px+b1
        ax.plot(px,py,'o',color='black',ms=4)
    ax.set_xlabel('x',loc='right',fontsize=9);ax.set_ylabel('y',loc='top',rotation=0,fontsize=9)
    fig.tight_layout(pad=.8);buf=BytesIO();fig.savefig(buf,format='pdf');plt.close(fig)
    return buf.getvalue()

def adapted_q(q):
    q=json.loads(json.dumps(q))
    if q.get('table'):
        inputs=[row[0] for row in q['table'][1:]]
        q['prompt']='Evaluate each side separately at x = '+', '.join(map(str,inputs))+'. Record the left value, right value, and whether they are equal. State what the tested values establish; do not solve the equation.'
        for r in q['rows'][:-1]:r['label']+=': left / right / equal?'
    for r in q['rows']:
        r['label']=r['label'].replace('Graph (booklet)','Graph')
    return q

def question_layout(q,num,keywidth):
    leftwidth=INNER*2/3-22
    items=[pitem(f'{num}. '+q['prompt'],leftwidth)]
    for s in q['math']:items.append(math_item(s,leftwidth))
    if q.get('graph') and q['graph']['kind']!='blank':
        items.append(vector(graphdata(q['graph']),leftwidth,196 if q['graph']['kind']=='line' else (100 if q['id'].startswith('M101-') else 145)))
    lh=sum(i[2] if i[0]=='paragraph' else i[3] for i in items)+5*(len(items)-1)+16
    rows=[]
    for r in q['rows']:
        # Each row reserves label, answer, and bottom-aligned points.
        lab=pitem((str(num)+'. ' if len(rows)==0 else '')+r['label'],min(164,keywidth-18),SMALL)
        isgraph=r['label']=='Graph' and q.get('graph',{}).get('kind')=='blank'
        if isgraph:
            student=vector(graphdata(q['graph']),156,156)
            answer=vector(graphdata(q['graph'],True,q['id']),156,156)
            h=lab[2]+answer[3]+31
        else:
            answer=pitem(r['answer'],keywidth-46,KEY) if r['plain'] else math_answer(r['answer'],keywidth-46)
            ah=answer[2] if answer[0]=='paragraph' else answer[3]
            assert answer[0]!='vector' or answer[4]>=.80,(q['id'],'answer too small',answer[4])
            h=max(38 if len(q['rows'])>2 else 48,lab[2]+ah+15)
            student=None
        rows.append({'source':r,'label':lab,'answer':answer,'height':h,'graph':student})
    rh=sum(r['height'] for r in rows)
    height=max(lh,rh)
    if height>rh:
        for r in rows:r['height']+=(height-rh)/len(rows)
    return {'q':q,'num':num,'items':items,'height':height,'rows':rows}

def paginate(blocks):
    pages=[];page=[];used=0
    for b in blocks:
        assert b['height']<=TOP-BOTTOM,(b['num'],b['height'])
        if page and used+b['height']>TOP-BOTTOM:
            pages.append(page);page=[];used=0
        page.append(b);used+=b['height']
    if page:pages.append(page)
    return pages

def layouts(a):
    qs=[adapted_q(q) for q in a['questions']]
    # Key geometry is computed first; the same row positions drive the test.
    n=1
    for _ in range(6):
        blocks=[question_layout(q,i+1,INNER/min(n,3)) for i,q in enumerate(qs)]
        pages=paginate(blocks)
        if len(pages)==n:return pages
        n=len(pages)
    raise ValueError('layout failed to stabilize')

def header(c,a,page,total,key=False):
    title=('Instructor answer key: ' if key else '')+a['title']
    p,h=para(title,INNER,TITLE);p.drawOn(c,M,762-h)
    c.setFillColor(HexColor('#111111'));c.setFont('DV',8)
    c.drawString(M,718,((f"Practice {a['practice']} | " if a.get('practice') else '')+f"Version {a['version']}")+(' | 30 minutes' if a.get('minutes') else ''))
    if key:
        c.drawString(M,700,'Each column matches the vertical answer positions on its corresponding test page.')
        c.drawString(M,683,'Grade the requested final answers in the response column.')
    else:
        c.setFont('DV',10);c.drawString(M,700,'Name: _________________________________________   Date: __________________')
        text='Write exact final answers in the right column. Students may use a basic, non-scientific calculator only.'
        p,h=para(text,INNER,SMALL);p.drawOn(c,M,687-h)
    c.setFont('DVB',8.8)
    if not key:
        c.drawString(M+8,TOP+5,'QUESTIONS');c.drawString(SPLIT+9,TOP+5,'ANSWERS')
    c.setFont('DV',7.5);c.setFillColor(HexColor('#444444'))
    c.drawString(M,28,a['course']+' | '+a['version'])
    c.drawRightString(W-M,28,'Instructor key' if key else f'Test page {page} of {total}')
    c.setFillColor(HexColor('#111111'))

def rule(c,x1,x2,y,dashed=False):
    c.saveState();c.setStrokeColor(HexColor('#b0b0b0' if dashed else '#333333'))
    c.setLineWidth(.4 if dashed else .65)
    if dashed:c.setDash(1.2,2.3)
    c.line(x1,y,x2,y);c.restoreState()

def draw_rows(c,overlays,b,x,width,top,key):
    y=top
    for j,r in enumerate(b['rows']):
        h=r['height'];label=r['source']['label']
        lab=pitem((str(b['num'])+'. ' if j==0 else '')+label,min(164,width-18),SMALL)
        draw_item(c,overlays,lab,x+9,y-7)
        if key:
            item=r['answer'];draw_item(c,overlays,item,x+9,y-10-lab[2])
        elif r['graph']:
            draw_item(c,overlays,r['graph'],x+9,y-10-lab[2])
        c.setFont('DV',7.6);c.drawRightString(x+width-9,y-h+7,str(r['source']['points'])+' pts')
        y-=h
        if j<len(b['rows'])-1:rule(c,x+6,x+width-6,y,True)
    return y

def packet(a):
    pages=layouts(a);n=len(pages)
    buf=BytesIO();c=Canvas(buf,pagesize=(W,H));overlays=[]
    for pi,blocks in enumerate(pages):
        header(c,a,pi+1,n)
        y=TOP;rule(c,M,W-M,y)
        c.setLineWidth(.65);c.line(SPLIT,TOP,SPLIT,TOP-sum(b['height'] for b in blocks))
        for b in blocks:
            cur=y-8
            for item in b['items']:
                cur-=draw_item(c,overlays,item,M+9,cur)+5
            draw_rows(c,overlays,b,SPLIT,INNER/3,y,False)
            y-=b['height'];rule(c,M,W-M,y)
        c.showPage()
    if n%2:c.showPage() # Truly blank reverse side before the instructor key.
    keyidx=c.getPageNumber()-1
    key_columns=[]
    for offset in range(0,n,3):
        subset=pages[offset:offset+3]
        header(c,a,1,n,True)
        columns=len(subset);key_columns.append(columns);cw=INNER/columns
        for pi,blocks in enumerate(subset):
            x=M+pi*cw;y=TOP
            c.setFont('DVB',8.8);c.drawString(x+9,TOP+5,f'TEST PAGE {offset+pi+1}')
            rule(c,x,x+cw,y)
            for b in blocks:
                draw_rows(c,overlays,b,x,cw,y,True)
                y-=b['height'];rule(c,x,x+cw,y)
            if pi:c.setLineWidth(.65);c.line(x,TOP+18,x,BOTTOM)
        c.showPage()
    c.save()
    reader=PdfReader(BytesIO(buf.getvalue()))
    for idx,page,scale,x,y in overlays:
        assert y>=BOTTOM-1,(a['title'],idx,x,y)
        reader.pages[idx].merge_transformed_page(page,Transformation().scale(scale).translate(x,y))
    return reader,n,keyidx,pages,key_columns

def build(a):
    reader,n,keyidx,pages,key_columns=packet(a)
    writer=PdfWriter();writer.append(reader,import_outline=False)
    writer.add_outline_item('Student test',0)
    writer.add_outline_item('Instructor answer key',keyidx)
    writer.add_metadata({'/Title':a['title']+' - Practice '+str(a['practice']),'/Author':'Jeremy Kastine','/Subject':'Combined questions and answers with vertically matched instructor key','/Creator':'Teaching algebra-test builder'})
    target=ROOT/a['folder']/'practice-tests'/a['file']
    target.parent.mkdir(parents=True,exist_ok=True)
    writer.write(target)
    assert (keyidx+1)%2==1
    return dict(file=str(target.relative_to(ROOT)),pages=len(writer.pages),test_pages=n,sheet_pages=0,key_pages=len(key_columns),key_columns=key_columns,starts={'test':1,'key':keyidx+1},questions=len(a['questions']))
