"""Check built HTML's local links and required routes, including subpath deployment."""
import os
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
ROOT = Path(__file__).resolve().parents[1] / 'site/dist'
BASE = (os.environ.get('SITE_BASE') or '/zinnober-haus').rstrip('/')
ORIGIN = os.environ.get('SITE_URL') or 'https://zinnoberhaus.github.io'
class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.urls=[]; self.ids=set()
    def handle_starttag(self, tag, attrs):
        props=dict(attrs)
        if tag == 'link' and props.get('rel') == 'canonical': return  # Metadata, not a navigable or asset link.
        if props.get('id'): self.ids.add(props['id'])
        for key in ('href','src'):
            if key in props: self.urls.append(props[key])

pages={}
for file in ROOT.rglob('*.html'):
    parser=Links(); parser.feed(file.read_text()); pages[file]=parser
errors=[]
for file,parser in pages.items():
    route='/' + str(file.relative_to(ROOT)).removesuffix('index.html')
    address=ORIGIN + BASE + route
    for href in parser.urls:
        target=urlsplit(urljoin(address, href))
        if target.netloc != urlsplit(ORIGIN).netloc or target.scheme not in ('http','https'): continue
        if BASE and not (target.path == BASE or target.path.startswith(BASE+'/')):
            errors.append(f'{file.relative_to(ROOT)}: outside site base {href}'); continue
        rel=unquote(target.path[len(BASE):]).lstrip('/')
        dest=ROOT/rel
        if dest.is_dir(): dest=dest/'index.html'
        if not dest.exists(): errors.append(f'{file.relative_to(ROOT)}: missing {href}')
        elif target.fragment and dest in pages and unquote(target.fragment) not in pages[dest].ids:
            errors.append(f'{file.relative_to(ROOT)}: missing anchor {href}')
for route in ['index.html','projects/zettel/index.html','projects/carthouse/index.html','handbook/operations/ticketing/index.html','handbook/operations/agent-assignments/index.html']:
    if not (ROOT/route).is_file(): errors.append(f'Required route missing: {route}')
if not (ROOT/'pagefind').is_dir(): errors.append('Search index is missing')
if errors: raise SystemExit('\n'.join(sorted(set(errors))))
print(f'Checked local links and anchors in {len(pages)} HTML pages, required project/operations routes and search output.')
