#!/usr/bin/env python3
"""Build the six Chapter 1 PDFs and the course index. Requires reportlab."""
import json
from html import escape
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')
for name, filename in [('Sans','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR/filename)))
W,H = 612,792  # US Letter portrait; keep the lower page clear for annotations.
MARGIN = 48
CONTENT_WIDTH = W - 2 * MARGIN
INK = HexColor('#14232d')
ACCENT = HexColor('#185f72')
MUTED = HexColor('#52616b')
BASE = 'https://openstax.org/books/introductory-statistics-2e/pages/'
BOOK = BASE+'1-introduction'
sections = json.loads((ROOT/'slides/source/chapter-01.json').read_text())

def paragraph(c, text, x, top, width, size, font='Sans', color=INK):
    style=ParagraphStyle('slide',fontName=font,fontSize=size,leading=size*1.27,textColor=color)
    p=Paragraph(escape(text).replace('\\n','<br/>'),style)
    _,height=p.wrap(width, H)
    p.drawOn(c,x,top-height)
    return top-height

cards=[]
for section in sections:
    number=section['number']
    filename=f'section-{number.replace(".","-")}.pdf'
    target=ROOT/'slides'/filename
    c=canvas.Canvas(str(target),pagesize=(W,H),pageCompression=1,invariant=1)
    c.setTitle(f"{number} {section['title']} - Discussion Slides")
    c.setAuthor('Jeremy Kastine')
    c.setSubject('Original classroom prompts aligned to OpenStax Introductory Statistics 2e; CC BY-NC-SA 4.0')
    c.setViewerPreference('DisplayDocTitle','true')
    for i, slide in enumerate(section['slides'],1):
        assert '?' in slide['question']
        c.setFillColor(ACCENT)
        c.rect(MARGIN,H-49,42,4,fill=1,stroke=0)
        c.setFont('Sans',11)
        c.setFillColor(MUTED)
        c.drawRightString(W-MARGIN,H-50,f'{number}  /  {i} of {len(section["slides"])}')
        top=paragraph(c,slide['title'],MARGIN,H-70,CONTENT_WIDTH,24,'Bold')-17
        body_size=20 if '\\n' in slide['body'] else 22
        top=paragraph(c,slide['body'],MARGIN,top,CONTENT_WIDTH,body_size)-21
        bottom=paragraph(c,slide['question'],MARGIN,top,CONTENT_WIDTH,22,'Bold',ACCENT)
        # Keep a clear writing area beneath the prompt, even on the roster page.
        assert bottom>=H/2,(number,i,bottom)
        c.setFillColor(MUTED)
        c.setFont('Sans',6.5)
        paragraph(c,'Aligned to OpenStax Introductory Statistics 2e, Barbara Illowsky and Susan Dean. Classroom adaptations. CC BY-NC-SA 4.0.',MARGIN,32,CONTENT_WIDTH,6.5,color=MUTED)
        c.drawString(48,14,'Access for free at '+BOOK)
        c.linkURL(BASE+section['slug'],(MARGIN,12,W-MARGIN,33),relative=0)
        c.showPage()
    c.save()
    cards.append(f'''<li><span class="section">Section {number}</span>
<h3><a href="slides/{filename}">{escape(section['title'])}</a></h3>
<p class="links"><a href="slides/{filename}">Open slides <span class="meta">(PDF, {len(section['slides'])} slides)</span></a>
<a href="{BASE+section['slug']}">Read textbook section</a></p></li>''')
    print(f'{target.relative_to(ROOT)}: {len(section["slides"])} slides')

html='''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Statistics | Class Slides</title>
<meta name="description" content="Statistics discussion slides for OpenStax Introductory Statistics 2e, organized by textbook section.">
<style>
:root{color-scheme:light;--ink:#14232d;--accent:#185f72;--muted:#52616b}
*{box-sizing:border-box}body{margin:0;background:#f5f7f8;color:var(--ink);font:18px/1.6 system-ui,sans-serif}
main{max-width:960px;margin:auto;padding:64px 28px}header{margin-bottom:48px}.eyebrow{font-weight:650;color:var(--accent);margin:0}
h1{font-size:clamp(2.6rem,7vw,4rem);line-height:1.05;letter-spacing:-.04em;margin:12px 0 24px}header p{max-width:680px}
h2{font-size:1.65rem;margin:0 0 10px}h3{font-size:1.22rem;line-height:1.4;margin:6px 0 14px}h3 a{color:var(--ink);text-decoration:none}
a{color:var(--accent);text-underline-offset:4px}a:hover{text-decoration:underline}a:focus-visible{outline:3px solid #b05819;outline-offset:5px}
ul{list-style:none;padding:0;margin:24px 0}li{padding:26px 0;border-top:1px solid #c7d2d7}.section{font-size:.88rem;color:var(--muted);font-weight:650}
.links{display:flex;gap:12px 32px;flex-wrap:wrap;margin:0;font-size:.95rem}.meta{color:var(--muted);font-size:.88rem}
footer{margin-top:42px;border-top:1px solid #c7d2d7;padding-top:24px;font-size:.82rem;color:var(--muted)}
@media(max-width:520px){main{padding:36px 20px}.links{flex-direction:column;gap:10px}h2{font-size:1.4rem}}
</style></head><body><main><header><p class="eyebrow">Fall 2026 · Jeremy Kastine</p><h1>Statistics<br>Class slides</h1>
<p>Discussion questions and problems for <a href="https://openstax.org/details/books/introductory-statistics-2e">OpenStax <em>Introductory Statistics 2e</em></a>.</p>
<p>One concept or problem per slide, with room for class notes and worked solutions.</p></header>
<section aria-labelledby="chapter-one"><h2 id="chapter-one">Chapter 1 · Sampling and Data</h2><p>Choose a section to open its PDF slides.</p><ul>'''+''.join(cards)+'''</ul></section>
<footer><p>Aligned to <em>Introductory Statistics 2e</em> by Barbara Illowsky and Susan Dean, OpenStax, Rice University (2023). Classroom prompts and synthetic datasets are original adaptations, not copied textbook exercises. Sections 1.5 and 1.6 use alternative class activities aligned to the lab objectives.</p>
<p>Slide materials: <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a>. <a href="https://openstax.org/books/introductory-statistics-2e/pages/1-introduction">Access the textbook for free</a>.</p></footer></main></body></html>'''
(ROOT/'index.html').write_text(html)
