#!/usr/bin/env python3
"""Build compact homework PDFs from course-owned JSON sources; keep answers off PDFs."""
from pathlib import Path
from io import BytesIO
import json
import argparse
import re
from xml.sax.saxutils import escape
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.mathtext import math_to_image
from matplotlib.font_manager import FontProperties
import numpy as np
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Flowable, KeepTogether, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader, PdfWriter, Transformation

ROOT = Path(__file__).resolve().parents[1]
INK = '#172A3A'
for name, file in [('DV','DejaVuSans.ttf'),('DV-Bold','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, '/usr/share/fonts/truetype/dejavu/'+file))
pdfmetrics.registerFontFamily('DV', normal='DV', bold='DV-Bold', italic='DV', boldItalic='DV-Bold')
matplotlib.rcParams.update({'mathtext.fontset':'dejavusans','pdf.fonttype':42,'font.family':'DejaVu Sans'})
BODY = ParagraphStyle('body',fontName='DV',fontSize=10.2,leading=14.1,textColor=HexColor(INK),spaceAfter=4)
SMALL = ParagraphStyle('small',parent=BODY,fontSize=9,leading=12.4)
SECTION = ParagraphStyle('section',parent=BODY,fontName='DV-Bold',fontSize=11.2,leading=15,spaceBefore=9,spaceAfter=6,keepWithNext=True)
TITLE = ParagraphStyle('title',parent=BODY,fontName='DV-Bold',fontSize=21,leading=25,spaceAfter=7)
SUBTITLE = ParagraphStyle('subtitle',parent=BODY,fontSize=12,leading=16,spaceAfter=7)

class Vector(Flowable):
    def __init__(self, buffer, overlays, max_width=490, max_height=None):
        super().__init__()
        self.buffer=buffer
        self.page=PdfReader(buffer).pages[0]
        w,h=float(self.page.mediabox.width),float(self.page.mediabox.height)
        self.scale=min(1,max_width/w,(max_height/h if max_height else 1))
        self.width,self.height=w*self.scale,h*self.scale
        self.overlays=overlays
        self.hAlign='LEFT'
    def draw(self):
        x,y=self.canv.absolutePosition(0,0)
        self.overlays.append((self.canv.getPageNumber()-1,self.page,self.scale,x,y,self.width,self.height))

def formula(tex, overlays):
    b=BytesIO()
    math_to_image('$'+tex+'$',b,prop=FontProperties(size=13.5),dpi=72,format='pdf',color=INK)
    b.seek(0)
    v=Vector(b,overlays)
    if v.scale<.85: raise ValueError('Formula too wide: '+tex)
    return v

def graph(kind, overlays):
    fig,ax=plt.subplots(figsize=(4.5,2.3))
    ax.spines[['top','right']].set_visible(False)
    ax.spines[['bottom','left']].set_position('zero')
    ax.grid(alpha=.22); ax.tick_params(labelsize=8)
    ax.set_xlabel('x',loc='right',fontsize=9); ax.set_ylabel('y',loc='top',rotation=0,fontsize=9)
    if kind=='transform':
        x=np.array([-3,-1,0,2]); y=np.array([0,2,-1,1])
        ax.plot(x,y,'-o',color='#172A3A',lw=1.5,ms=3)
        ax.plot(x+3,y-2,'--o',color='#536F7B',lw=1.5,ms=3)
        ax.text(-2.8,1.5,'f',fontsize=11);ax.text(4,-3.1,'g',fontsize=11)
        ax.set(xlim=(-4,6),ylim=(-4,3),xticks=np.arange(-4,7),yticks=np.arange(-4,4))
    elif kind=='polynomial':
        x=np.linspace(-2.5,3,401); ax.plot(x,(x+2)*(x-1)**2,color=INK,lw=1.6)
        ax.plot([0],[2],'o',color=INK,ms=4); ax.annotate('(0, 2)',(0,2),xytext=(.25,3.7),fontsize=9)
        ax.set(xlim=(-3,3.3),ylim=(-3,13),xticks=np.arange(-3,4),yticks=np.arange(-2,14,2))
    elif kind=='line':
        x=np.array([-3,5]);ax.plot(x,2*x/3-1,color=INK,lw=1.6)
        ax.plot([0,3],[-1,1],'o',color=INK,ms=4)
        ax.set(xlim=(-3,5),ylim=(-4,4),xticks=np.arange(-3,6),yticks=np.arange(-4,5))
    else: raise ValueError(kind)
    fig.tight_layout(pad=.6)
    b=BytesIO();fig.savefig(b,format='pdf');plt.close(fig);b.seek(0)
    return Vector(b,overlays,max_height=168)

def table(data):
    rows=[[Paragraph(escape(str(x)),SMALL) for x in row] for row in data]
    t=Table(rows,hAlign='LEFT',colWidths=[490/len(data[0])]*len(data[0]))
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),HexColor('#EAF0F3')),('LINEBELOW',(0,0),(-1,0),.5,HexColor('#9BAEB9')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),4),('TOPPADDING',(0,0),(-1,-1),4)]))
    return t

def build(course, a):
    target=ROOT/course/'homework'/a['file']
    target.parent.mkdir(parents=True,exist_ok=True)
    overlays=[];story=[]
    body=ParagraphStyle('compact-body',parent=BODY,leading=13,spaceAfter=3) if a.get('compact') else BODY
    problem_gap=3 if a.get('compact') else 5
    formula_gap=4 if a.get('compact') else 5
    story.append(Paragraph(escape(a['course'].upper()),SMALL))
    story.append(Paragraph(escape(a['title']),TITLE))
    story.append(Paragraph(escape(a['subtitle']),SUBTITLE))
    story.append(Paragraph('<b>'+escape(a['coverage'])+'</b> | Estimated time: about 1 hour',SMALL))
    story.append(Paragraph('<b>Complete all problems and show your work on separate paper.</b> Plan for about 45-50 minutes of work and 10-15 minutes to check, correct, and submit.',BODY))
    story.append(Paragraph('Use available resources to check your answers and reasoning. Complete the self-evaluation in Blackboard, upload a clear photo of your one best representative page, and retain all your written work.',SMALL))
    if a.get('directions'): story.append(Paragraph(a['directions'],SMALL))
    number=0
    for section in a['sections']:
        prefix=[Paragraph(escape(section['title']),SECTION)]
        if section.get('intro'):prefix.append(Paragraph(section['intro'],SMALL))
        for section_index,p in enumerate(section['problems']):
            number+=1
            parts=(prefix if section_index==0 else [])+[Paragraph(f'<b>{number}.</b>  '+p['prompt'],body)]
            if p.get('table'):parts.extend([table(p['table']),Spacer(1,4)])
            for tex in p.get('math',[]):parts.extend([formula(tex,overlays),Spacer(1,formula_gap)])
            if p.get('graph'):parts.append(graph(p['graph'],overlays))
            parts.append(Spacer(1,problem_gap))
            story.append(KeepTogether(parts))
    def footer(c,doc):
        c.setStrokeColor(HexColor('#B8C5CD'));c.setLineWidth(.5);c.line(48,45,564,45)
        c.setFillColor(HexColor('#475569'));c.setFont('DV',7.4)
        c.drawString(48,32,a['course']+' | '+a['title']+' | Original practice problems')
        c.drawRightString(564,32,str(doc.page))
        if doc.page>1:
            c.setFont('DV-Bold',9);c.drawString(48,756,a['course']+' | '+a['title'])
    b=BytesIO()
    doc=SimpleDocTemplate(b,pagesize=(612,792),leftMargin=48,rightMargin=48,topMargin=48,bottomMargin=59)
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    b.seek(0);reader=PdfReader(b);writer=PdfWriter()
    for idx,p,s,x,y,w,h in overlays:
        assert x>=47 and x+w<=565 and y>=58 and y+h<=745,(a['file'],idx,x,y,w,h)
        reader.pages[idx].merge_transformed_page(p,Transformation().scale(s).translate(x,y),over=True)
    for page in reader.pages:writer.add_page(page)
    writer.add_metadata({'/Title':a['course']+' - '+a['title']+': '+a['subtitle'],'/Author':'Jeremy Kastine','/Subject':a['coverage'],'/Creator':'Teaching homework builder (ReportLab and vector mathematics)'})
    with target.open('wb') as f:writer.write(f)
    text='\n'.join(p.extract_text() for p in PdfReader(target).pages)
    for i in range(1,number+1):assert re.search(r'\b'+str(i)+r'\.',text),(target,i)
    assert 'one best representative page' in text
    assert all(p.get('answer') for s in a['sections'] for p in s['problems'])
    minutes=sum(p['minutes'] for s in a['sections'] for p in s['problems'])
    assert 44<=minutes<=52,(target,minutes)
    return {'file':str(target.relative_to(ROOT)),'pages':len(reader.pages),'problems':number,'work_minutes':minutes}

def link_tsm(assignments):
    from course_pages import build_categories
    build_categories(ROOT/'tsm')
    # Add each packet at its completion point as well as in the homework list.
    for lesson in (ROOT/'tsm/lessons').glob('topic-*.html'):
        n=int(lesson.name.split('-')[1]);html=lesson.read_text()
        links=[f'<a href="../homework/{a["file"]}">{a["course"]} {a["title"]}: {escape(a["coverage"])} (PDF)</a>' for a in assignments if max(a['topics'])==n]
        if not links:continue
        block='<!-- homework:start -->\n<aside class="homework-links"><h2>Homework</h2><p>'+'</p><p>'.join(links)+'</p><p>Complete on separate paper; upload one best representative page in Blackboard and retain all work.</p></aside>\n<!-- homework:end -->'
        if '<!-- homework:start -->' in html:html=re.sub(r'<!-- homework:start -->.*?<!-- homework:end -->',lambda _:block,html,flags=re.S)
        else:html=html.replace('  </main>',block+'\n  </main>')
        lesson.write_text(html)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--course',choices=['101','stats','tsm'],action='append');args=parser.parse_args()
    report=[]
    for course in args.course or ['101','stats','tsm']:
        assignments=json.loads((ROOT/course/'homework/source/assignments.json').read_text())
        for a in assignments:report.append(build(course,a))
        if course=='tsm':link_tsm(assignments)
        else:
            from slide_builder import COURSES,build_index
            sections=[]
            for f in sorted((ROOT/course/'slides/source').glob('chapter-*.json')):sections.extend(json.loads(f.read_text()))
            build_index(ROOT/course,COURSES[course],sections)
    for r in report:print(json.dumps(r))

if __name__=='__main__':main()
