#!/usr/bin/env python3
"""Export private Unit 1 duplex test/key packets, using the online generator.

Usage: python stats/scripts/export_test_packets.py /absolute/output.pdf
No PDFs are published to the teaching site. Each packet is test front/back,
then a matching key front/back; print US Letter, duplex, long-edge flip.
"""
import json, secrets, subprocess, sys
from pathlib import Path
from html import escape
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import fitz
from reportlab.lib.utils import ImageReader
from io import BytesIO

ROOT=Path(__file__).resolve().parents[2]
BANKS=ROOT/'stats/question-banks'
FONT=Path('/usr/share/fonts/truetype/dejavu')
for name,file in [('Test','DejaVuSans.ttf'),('TestBold','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(FONT/file)))
pdfmetrics.registerFontFamily('Test',normal='Test',bold='TestBold')
STYLE=ParagraphStyle('question',fontName='Test',fontSize=10,leading=12.5)
LEFT,RIGHT,DIVIDER=36,576,396
TOP=668

def para(text,width):
    p=Paragraph(text,STYLE); _,h=p.wrap(width,700); return p,h

def layout(q,n):
    p,h=para(f'<b>{n}.</b> '+escape(q['stem']),340)
    blocks=[(p,h)]
    if q.get('figure'):
        doc=fitz.open(str(BANKS/q['figure']['file']))
        pix=doc[0].get_pixmap(matrix=fitz.Matrix(3,3),alpha=False)
        scale=min(330/pix.width,70/pix.height)
        fig=(ImageReader(BytesIO(pix.tobytes('png'))),pix.width*scale,pix.height*scale)
        blocks.append((fig,fig[2]+4))
    for i,choice in enumerate(q['choices']):
        p,h=para(f'<b>{"ABCD"[i]}.</b> '+escape(choice),330)
        blocks.append((p,h))
    return blocks,sum(h for _,h in blocks)+16

def main():
    out=Path(sys.argv[1]).resolve(); out.parent.mkdir(parents=True,exist_ok=True)
    # Version labels are independently random, as specified; generator seeds
    # are separate so labels never restrict the range of possible tests.
    specs=[{'version':10000+secrets.randbelow(90000),'seed':secrets.randbits(32)} for _ in range(20)]
    js="const fs=require('fs'),{generate}=require('./stats/question-banks/test-generator.js');const bank=JSON.parse(fs.readFileSync('./stats/question-banks/unit-1-question-bank.json'));const specs=JSON.parse(fs.readFileSync(0,'utf8'));console.log(JSON.stringify(specs.map(s=>({...s,questions:generate(bank,s.seed)}))));"
    packets=json.loads(subprocess.check_output(['node','-e',js],input=json.dumps(specs).encode(),cwd=ROOT))
    c=canvas.Canvas(str(out),pagesize=(612,792)); c.setTitle('MSC 201 - Test 1 - 20 duplex versions and answer keys')
    for packet in packets:
        qs=packet['questions']; rows=[layout(q,i+1) for i,q in enumerate(qs)]
        # Use five questions on each side; reject overflow rather than shrink.
        for half in (rows[:5],rows[5:]):
            assert sum(h for _,h in half)<=TOP-42, sum(h for _,h in half)
        for key in (False,True):
            for side in range(2):
                c.setFillColorRGB(0,0,0); c.setFont('TestBold',15)
                c.drawString(LEFT,752,'MSC 201 - Test 1'+(' - ANSWER KEY' if key else ''))
                c.setFont('TestBold',10); c.drawRightString(RIGHT,730,f'Version {packet["version"]} | Page {side+1} of 2')
                c.setFont('Test',10); c.drawString(LEFT,730,'Name: ____________________________')
                c.setFont('Test',9)
                c.drawString(LEFT,710,'Students may use a basic, non-scientific calculator only.')
                c.drawString(LEFT,696,'Choose one answer per question. Write A, B, C, or D in the right column.')
                c.setFont('TestBold',9); c.drawString(LEFT+8,680,'Questions'); c.drawString(DIVIDER+12,680,'Answer choice')
                y=TOP; c.setLineWidth(.6); c.line(LEFT,y,RIGHT,y)
                for j in range(side*5,side*5+5):
                    blocks,height=rows[j]; yy=y-8
                    for block,h in blocks:
                        if isinstance(block,Paragraph): block.drawOn(c,LEFT+8+(10 if block is not blocks[0][0] else 0),yy-h)
                        else: c.drawImage(block[0],LEFT+12,yy-h+2,width=block[1],height=block[2])
                        yy-=h
                    if key:
                        c.setFont('TestBold',16); c.drawString(DIVIDER+18,y-28,'ABCD'[qs[j]['answer_index']])
                    c.setFont('Test',8); c.drawRightString(RIGHT-10,y-height+8,'10 points')
                    c.line(DIVIDER,y,DIVIDER,y-height); y-=height; c.line(LEFT,y,RIGHT,y)
                c.setFont('Test',8); c.drawString(LEFT,24,f'Version {packet["version"]} | '+('Instructor key' if key else 'Student test'))
                c.showPage()
    c.save()
    # Instructor-only local reproduction record; never published.
    out.with_suffix('.json').write_text(json.dumps(packets,indent=2)+'\n')
    print(out)

if __name__=='__main__': main()
