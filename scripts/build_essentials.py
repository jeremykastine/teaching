#!/usr/bin/env python3
"""Build linked, static essentials reviews for every topic in the lecture indexes.

Run: python scripts/build_essentials.py
Requires beautifulsoup4 and latex2mathml; see essentials-requirements.txt.
Run after any lecture-note rebuild to restore essentials navigation.
"""
from pathlib import Path
from html import escape
import json
import re
from bs4 import BeautifulSoup
from latex2mathml.converter import convert
from essentials_content import CONTENT

ROOT = Path(__file__).resolve().parents[1]
COURSES = {'tsm': ('TSM 098 / 099', 'tsm'),
           '101': ('MATH 101 · College Algebra', 'math101'),
           'stats': ('Statistics', 'stats')}
OPTIONAL = {'2.3', '4.2', '4.3', '6.7', '6.8'}


def rich(text):
    """Escape prose and compile only delimited math into accessible native MathML."""
    parts = re.split(r'(\\\(.*?\\\))', text)
    return ''.join(convert(p[2:-2]) if p.startswith(r'\(') else escape(p)
                   for p in parts)


def graph(kind):
    def px(x): return 290 + 55*x
    def py(y): return 235 - 45*y
    grid = []
    for x in range(-4, 5):
        grid.append(f'<path d="M{px(x)} 35V340" class="grid"/>')
        if x: grid.append(f'<text x="{px(x)}" y="253" text-anchor="middle">{x}</text>')
    for y in range(-2, 5):
        grid.append(f'<path d="M45 {py(y)}H535" class="grid"/>')
        if y: grid.append(f'<text x="279" y="{py(y)+5}" text-anchor="end">{y}</text>')
    def dot(x,y,closed):
        return f'<circle cx="{px(x)}" cy="{py(y)}" r="6" fill="{"#185f72" if closed else "white"}" stroke="#185f72" stroke-width="2.5"/>'
    if kind == 'DOMAIN_SEGMENT':
        label='Line segment from a filled endpoint at (−3, −2) to an open endpoint at (2, 3).'
        path=f'M{px(-3)} {py(-2)}L{px(2)} {py(3)}'
        points=dot(-3,-2,True)+dot(2,3,False)
    elif kind == 'DOMAIN_PARABOLA':
        label='Parabolic arc with open endpoint (−2, 4), vertex (0, 0), and filled endpoint (1, 1).'
        path='M'+' L'.join(f'{px(-2+3*i/100):.2f} {py((-2+3*i/100)**2):.2f}' for i in range(101))
        points=dot(-2,4,False)+dot(1,1,True)
    elif kind == 'BEHAVIOR_W':
        label='Smooth curve from filled (−4, 3), through minima (−2, −1) and (2, −2) and a peak (0, 2), to filled (3, 1).'
        path=(f'M{px(-4)} {py(3)} '
              f'C{px(-3.3)} {py(2)} {px(-2.7)} {py(-1)} {px(-2)} {py(-1)} '
              f'C{px(-1.3)} {py(-1)} {px(-0.7)} {py(2)} {px(0)} {py(2)} '
              f'C{px(0.7)} {py(2)} {px(1.3)} {py(-2)} {px(2)} {py(-2)} '
              f'C{px(2.4)} {py(-2)} {px(2.7)} {py(0)} {px(3)} {py(1)}')
        points=dot(-4,3,True)+dot(3,1,True)
    else:
        label='Increasing line segment from filled (−2, −1) toward open (2, 3).'
        path=f'M{px(-2)} {py(-1)}L{px(2)} {py(3)}'
        points=dot(-2,-1,True)+dot(2,3,False)
    return (f'<figure><svg viewBox="0 0 580 370" role="img" aria-label="{escape(label)}">'
            +''.join(grid)+f'<path d="M45 235H545M290 340V25" class="axis"/>'
            '<text x="548" y="228">x</text><text x="299" y="24">y</text>'
            '<text x="278" y="253" text-anchor="end">0</text>'
            f'<path d="{path}" class="curve"/>{points}</svg>'
            '<figcaption>Filled endpoints are included; open endpoints are excluded.</figcaption></figure>')


def problem(text):
    if not text.startswith('GRAPH_'):
        return '<p>'+rich(text)+'</p>'
    kind=text.removeprefix('GRAPH_')
    prompt=('Find the domain and range in interval notation.' if kind.startswith('DOMAIN')
            else 'Find intervals of increase and decrease, interior local extrema, and absolute extrema, when they exist.')
    return '<p>'+prompt+'</p>'+graph(kind)


def shell(title, css, body):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title><link rel="stylesheet" href="{css}"></head>
<body><main>{body}</main></body></html>
'''


def inventory():
    result=[]
    for course in COURSES:
        doc=BeautifulSoup((ROOT/course/'lecture-notes.html').read_text(), 'html.parser')
        for a in doc.select('a[href^="lessons/"]'):
            label=a.get_text(' ',strip=True)
            match=re.match(r'(?:Topic\s+)?(\d+(?:\.\d+)?[Bb]?)',label)
            if not match: raise ValueError(label)
            number=match.group(1).upper()
            assignment=a.find_parent('li').select_one('.assignment')
            scope=assignment.get_text(' ',strip=True) if assignment else ''
            if course=='101' and number in OPTIONAL: scope='Optional applications'
            if course=='101' and number=='3.1B': scope='Supplemental lesson'
            if course=='stats' and number in {'1.5','1.6'}: scope='Guided lab'
            if course=='stats' and number=='9.0': scope='Conceptual overview'
            result.append({'course':course,'number':number,'title':label,
                           'lesson':a['href'],'scope':scope})
    return result


def build():
    entries=inventory()
    expected={(e['course'],e['number']) for e in entries}
    assert expected==set(CONTENT), (expected-set(CONTENT),set(CONTENT)-expected)
    report=[]
    for course,(name,anchor) in COURSES.items():
        indexpath=ROOT/course/'lecture-notes.html'
        text=indexpath.read_text()
        text=re.sub(r' <a class="essentials-link" href="[^"]*">Essentials review</a>', '', text)
        indexpath.write_text(text)
        subset=[e for e in entries if e['course']==course]
        dest=ROOT/course/'essentials';dest.mkdir(exist_ok=True)
        links=[]
        for i,e in enumerate(subset):
            key=(course,e['number']);data=CONTENT[key];filename=Path(e['lesson']).name
            assert 5<=len(data['questions'])<=10,key
            assert 2<=len(data['examples'])<=4,key
            title=e['title']+' · Essentials'
            nav=(f'<a href="../essentials.html">All essentials</a>'
                 f'<a href="../{e["lesson"]}">Lecture notes</a>'
                 f'<a href="../../index.html#{anchor}">Teaching home</a>')
            if i: nav+=f'<a href="{Path(subset[i-1]["lesson"]).name}">Previous</a>'
            if i+1<len(subset): nav+=f'<a href="{Path(subset[i+1]["lesson"]).name}">Next</a>'
            body=f'<nav aria-label="Review navigation">{nav}</nav><p class="eyebrow">{escape(name)}</p><h1>{escape(title)}</h1>'
            if e['scope']: body+=f'<p class="scope">{escape(e["scope"])}</p>'
            body+='<p>Answer the questions from memory on paper. Then check the answer key. Attempt each example before opening its solution.</p>'
            body+='<h2>Essential facts, definitions, and procedures</h2><ol class="recall-questions">'
            body+=''.join(f'<li>{rich(q)}</li>' for q,a in data['questions'])+'</ol>'
            body+='<details class="answer-key"><summary>Check short-answer key</summary><ol class="answer">'
            body+=''.join(f'<li>{rich(a)}</li>' for q,a in data['questions'])+'</ol></details>'
            body+='<h2>Example problems</h2>'
            for j,(q,steps) in enumerate(data['examples'],1):
                body+=f'<section class="example"><h3>Example {j}</h3>{problem(q)}<details><summary>Show solution</summary><ol class="answer">'
                body+=''.join(f'<li>{rich(s)}</li>' for s in steps)+'</ol></details></section>'
            body+='<p class="source-note">Review alongside the linked lecture notes. These questions and worked examples are original course review material.</p>'
            (dest/filename).write_text(shell(title,'../../essentials.css',body))
            scope=f'<span class="scope">{escape(e["scope"])}</span>' if e['scope'] else ''
            links.append(f'<li><a href="essentials/{filename}">{escape(e["title"])}</a>{scope}</li>')
            # Add a link beside each existing lesson entry without replacing its markup.
            indexpath=ROOT/course/'lecture-notes.html'
            text=indexpath.read_text()
            pattern=r'(<a href="'+re.escape(e['lesson'])+r'">[^<]*</a>)'
            text=re.sub(pattern,lambda m:m[1]+f' <a class="essentials-link" href="essentials/{filename}">Essentials review</a>',text,count=1,flags=re.S)
            indexpath.write_text(text)
            lessonpath=ROOT/course/e['lesson'];text=lessonpath.read_text()
            href=f'../essentials/{filename}'
            if href not in text:
                text=re.sub(r'(<nav\b[^>]*>)',lambda m:m[1]+f'<a href="{href}">Essentials review</a>',text,count=1)
                lessonpath.write_text(text)
            report.append({'course':course,'section':e['number'],'path':str((dest/filename).relative_to(ROOT)),
                           'questions':len(data['questions']),'examples':len(data['examples'])})
        intro=(f'<nav aria-label="Course navigation"><a href="../index.html#{anchor}">Teaching home</a>'
               '<a href="lecture-notes.html">Lecture notes</a></nav>'
               f'<p class="eyebrow">{escape(name)}</p><h1>Essentials reviews</h1>'
               '<p>Each topic has five short-answer questions about essential facts, definitions, and procedures, plus two or three example problems with worked solutions. Try the work before expanding the answers.</p>')
        (ROOT/course/'essentials.html').write_text(shell(name+' · Essentials reviews','../essentials.css',intro+'<ol class="topic-list">'+''.join(links)+'</ol>'))
        # Course-wide hub link is useful even before a topic is selected.
        indexpath=ROOT/course/'lecture-notes.html';text=indexpath.read_text()
        if 'href="essentials.html"' not in text:
            text=re.sub(r'(</h1>)',r'\1<p><a href="essentials.html">Essentials reviews for every topic</a></p>',text,count=1)
            indexpath.write_text(text)
    rootpath=ROOT/'index.html';text=rootpath.read_text()
    for course in COURSES:
        href=f'{course}/essentials.html'
        if f'href="{href}"' not in text:
            needle=f'<li><a href="{course}/lecture-notes.html">Lecture notes</a></li>'
            assert needle in text,course
            text=text.replace(needle,needle+f'<li><a href="{href}">Essentials reviews</a></li>',1)
    rootpath.write_text(text)
    (ROOT/'scripts/essentials-coverage.json').write_text(json.dumps(report,indent=2)+'\n')
    print(f'Built {len(report)} reviews; {sum(r["questions"] for r in report)} recall questions; {sum(r["examples"] for r in report)} worked examples.')


if __name__=='__main__': build()
