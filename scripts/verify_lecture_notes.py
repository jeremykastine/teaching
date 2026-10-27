from pathlib import Path
from bs4 import BeautifulSoup as B
import json,collections
r=Path(__file__).resolve().parents[1];errors=[]
for c in ['stats','101']:
 manifest=json.loads((r/c/'notes-source/manifest.json').read_text())
 for m in manifest:
  p=r/c/'lessons'/('section-'+m['slug']+'.html');s=B(p.read_text(),'html.parser')
  for a in s.select('[href],[src]'):
   u=a.get('href',a.get('src',''))
   if u and not u.startswith(('http','data:','#','mailto:')) and not (p.parent/u.split('#')[0]).exists():errors.append((str(p),u))
  for x in s.select('[data-solution-panel]'):
   if not x.get_text(strip=True) and not x.select('img,svg'):errors.append(('empty',str(p)))
  unknown=[x.name for x in s.find_all() if '<' in str(x.name) or '=' in str(x.name)]
  if unknown:errors.append(('malformed',str(p),unknown))
 print(c,len(manifest),'pages')
print('Errors:',errors);assert not errors
