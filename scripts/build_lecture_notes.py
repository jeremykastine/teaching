#!/usr/bin/env python3
"""Build textbook-sequence HTML lecture notes from licensed source snapshots."""
from pathlib import Path
import sys,json,re,copy,hashlib,urllib.request,base64,concurrent.futures
from urllib.parse import urljoin
from bs4 import BeautifulSoup as BS
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'stats/notes-source'))
from answers import A,Q
from special import PAGES,ex
BOOK={'stats':'introductory-statistics-2e','101':'college-algebra-2e'}
ASSETS=json.loads((ROOT/'notes-assets/manifest.json').read_text()) if (ROOT/'notes-assets/manifest.json').exists() else {}
NAME={'stats':'Statistics','101':'College Algebra'}
OPTIONAL={'2.3','4.2','4.3','6.7','6.8'}
def soup(x):return BS(x,'html.parser')
def inner(x):return ''.join(map(str,x.contents)) if x else ''
def filename(m):return 'section-'+m['slug']+'.html'
def block(label,q,a,id=''):
 return f'<section class="worked-example" id="{id}"><div class="problem-statement"><h3>{label}</h3>{q}</div><div class="solution-panel" data-solution-panel style="color:#ffffff;background-color:#ffffff">{a}</div></section>'
def convert(c,m):
 n=m['number'];src=soup((ROOT/c/'notes-source/textbook'/f'{n}.html').read_text());page=src.select_one('[data-type="page"]') or src
 if c=='stats' and n in PAGES:
  body=PAGES[n]
  if n=='1.6':body=body.replace('<!-- RESTAURANT_TABLE -->',str(page.select_one('table')))
  return body
 if c=='101' and n=='2.4':
  return '<h2>The imaginary unit and standard form</h2><p>The imaginary unit satisfies i² = −1. For a positive real number a, √(−a) = i√a. A complex number has the form a + bi; a is its real part and b is its imaginary part. This course limits Section 2.4 to these ideas.</p>'+ex('Example 1 · Identify the parts','<p>Write √(−9) and 5 + √(−16) in standard form and identify their real and imaginary parts.</p>','<p>√(−9) = 3i = 0 + 3i: real part 0, imaginary part 3. The second number is 5 + 4i: real part 5, imaginary part 4.</p>')+ex('Try It 1 · Standard form','<p>Write √(−24) in standard form. Identify its real and imaginary parts.</p>','<p>√(−24) = i√(4·6) = 2i√6 = 0 + (2√6)i; real part 0 and imaginary part 2√6.</p>')+ex('Additional practice · Nonperfect squares','<p>Simplify √(−12), −√(−18), and 2 + √(−32).</p>','<p>√(−12) = i√(4·3) = 2i√3. Next, −√(−18) = −3i√2. Finally, 2 + √(−32) = 2 + 4i√2.</p>')+ex('Additional practice · A root versus an equation','<p>Evaluate √(−36). Then solve x² = −36. Explain why the answers differ.</p>','<p>The principal square root is √(−36) = 6i. The equation has two solutions, x = ±6i, because both (6i)² and (−6i)² equal −36.</p>')
 for x in page.select('[data-type="document-title"],.os-section-exercises-container'):x.decompose()
 keys={}
 if c=='101':
  key=soup((ROOT/c/'notes-source/textbook'/('key-'+n.split('.')[0]+'.html')).read_text())
  for x in key.select('[data-type="solution"][id]'):
   keys[x['id'].removesuffix('-solution')]=inner(x.select_one('.os-solution-container'))
 targets=page.select('[data-type="example"],.try,.collab')
 for x in targets:
  if not x.parent:continue
  head=x.select_one('header');label=head.get_text(' ',strip=True) if head else 'Practice'
  label=re.sub(r'\s+',' ',label);label=re.sub(r'Example\s+(\d)',r'Example \1',label)
  aid=n+':'+x.get('id','');override=Q.get(aid,Q.get(label)) if c=='stats' else None
  original=copy.deepcopy(x)
  answers=[]
  for sol in x.select('[data-type="solution"]'):
   answers.append(inner(sol.select_one('.os-solution-container')) or inner(sol));sol.decompose()
  for analysis in x.select('.analysis'):
   answers.append(str(analysis));analysis.decompose()
  if not answers and c=='101':
   answers=[keys[e['id']] for e in x.select('[data-type="exercise"][id]') if e['id'] in keys]
  ans=A.get(aid,A.get(label)) if c=='stats' else None
  if ans is None:ans=''.join(answers)
  if head and head.parent:head.decompose()
  q=inner(x)
  if override:
   if isinstance(override,str):q=override
   elif 'custom' in override:q=override['custom']
   elif 'tables' in override:q='<p>'+override['intro']+'</p>'+''.join(str(t) for t in original.select('table')[:override['tables']])
   else:
    text=inner(original);marker=override['before_text'];pos=text.find(marker);q=text[:text.rfind('<p',0,pos)]+override['append'] if pos>=0 else q+override['append']
    if not ans:ans=inner(original)
  if not ans:raise ValueError(f'Missing answer: {c} {n} {label} {aid}')
  x.replace_with(soup(block(label,q,ans,x.get('id',''))))
 return inner(page)
def clean(body,c,m):
 s=soup(body);base='https://openstax.org/books/'+BOOK[c]+'/pages/'+m['slug']
 for x in s.select('annotation,annotation-xml,script,summary'):x.decompose()
 for x in s.select('button'):x.unwrap()
 for x in s.select('details'):x.unwrap()
 for x in s.select('[style]'):
  if 'solution-panel' not in x.get('class',[]):del x['style']
 for x in s.select('a[href]'):
  u=x['href'];x['href']=urljoin(base,u)
 for x in s.select('img'):
  u=urljoin('https://openstax.org',x.get('data-original-src',x.get('src','')));x['src']=('../../notes-assets/'+ASSETS[u]) if u in ASSETS else u
  for a in ['srcset','sizes','width','height']:x.attrs.pop(a,None)
 for x in s.select('math'):
  wrap=s.new_tag('span',attrs={'class':'math-scroll '+('display-math' if x.get('display')=='block' else 'inline-math')});x.wrap(wrap)
 for x in s.select('table'):
  if x.parent.get('class')!=['table-scroll']:
   wrap=s.new_tag('div',attrs={'class':'table-scroll'});x.wrap(wrap)
 for x in s.select('[data-type="problem-title"],[data-type="solution-title"]'):x.decompose()
 return str(s)
def build():
 report=[]
 for c in BOOK:
  manifest=json.loads((ROOT/c/'notes-source/manifest.json').read_text());dest=ROOT/c/'lessons';dest.mkdir(exist_ok=True)
  index=[]
  for i,m in enumerate(manifest):
   n=m['number'];f=filename(m);url='https://openstax.org/books/'+BOOK[c]+'/pages/'+m['slug']
   nav='<a href="../lecture-notes.html">Table of contents</a>'
   if i:nav+=f'<a href="{filename(manifest[i-1])}">Previous: {manifest[i-1]["number"]}</a>'
   if i+1<len(manifest):nav+=f'<a href="{filename(manifest[i+1])}">Next: {manifest[i+1]["number"]}</a>'
   nav+=f'<a href="{url}">Textbook section</a>'
   if c=='stats' and n in ['3.4','3.5']:
    existing=(dest/f).read_text();body=re.sub(r'<nav.*?</nav>',lambda _: '<nav class="topic-nav" aria-label="Lesson navigation">'+nav+'</nav>',existing,count=1,flags=re.S);(dest/f).write_text(body)
   else:
    body=clean(convert(c,m),c,m)
    title=n+': '+m['title'];optional='<p class="source-note">Optional applications topic.</p>' if c=='101' and n in OPTIONAL else ''
    html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title} | {NAME[c]} Lecture Notes</title><link rel="stylesheet" href="../../tsm/styles.css"><link rel="stylesheet" href="../../stats/lecture-notes.css"><script defer src="../../tsm/solutions.js"></script></head><body><main class="lecture-notes"><nav class="topic-nav" aria-label="Lesson navigation">{nav}</nav><p class="series-title">{NAME[c]} Lecture Notes · OpenStax</p><h1>{title}</h1><p class="solution-instructions">Double-click or double-tap a blank solution area to show or hide the answer. With a keyboard, focus the area and press Enter or Space.</p>{optional}<p class="source-note">Follow the textbook’s sequence below. Historical datasets and supplied models are classroom exercises. Try It answers may be concise; use the preceding worked example as a method guide.</p>{body}<footer class="attribution">Adapted from <a href="{url}">OpenStax {"Introductory Statistics 2e, by Barbara Illowsky and Susan Dean" if c=="stats" else "College Algebra 2e, by Jay Abramson"}</a>, Rice University. Licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a>. Changes include classroom formatting, concealed solutions, supplemental explanations, and course-specific scope. Textbook example and Try It labels are retained where applicable.</footer></main></body></html>'''
    (dest/f).write_text(html)
   count=len(soup(body).select('[data-solution-panel]'));report.append({'course':c,'section':n,'file':f,'solutions':count})
   index.append(f'<li><a href="lessons/{f}">{n}: {m["title"]}</a>'+(' <span>— Optional applications</span>' if c=='101' and n in OPTIONAL else '')+'</li>')
  (ROOT/c/'lecture-notes.html').write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{NAME[c]} Lecture Notes</title><link rel="stylesheet" href="../tsm/styles.css"></head><body><main class="lecture-notes"><nav class="topic-nav"><a href="../index.html#{"math101" if c=="101" else "stats"}">Teaching home</a></nav><h1>{NAME[c]} Lecture Notes</h1><p>Textbook-aligned notes for every topic covered in this course. Double-click or double-tap the blank area beneath a problem to reveal its solution; keyboard users can press Enter or Space.</p><p>'+('Section 2.4 is limited to introductory imaginary numbers. Optional application sections are marked.' if c=='101' else 'Sections 1.5 and 1.6 are guided labs. Topic 9.0 is a conceptual overview of hypothesis testing.')+'</p><ol class="topic-list">'+''.join(index)+'</ol></main></body></html>')
 (ROOT/'scripts/lecture-notes-coverage.json').write_text(json.dumps(report,indent=2)+'\n')
 print('Built',len(report),'sections;',sum(x['solutions'] for x in report),'solution panels')
if __name__=='__main__':build()
