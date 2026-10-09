import re,glob,html as H
import os; os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','docs'))
idx=open('index.html',encoding='utf-8').read()
chs=[]
for m in re.finditer(r'<h2>(Chương[^<]*)</h2>(.*?)</ul>',idx,re.S):
    items=re.findall(r'<a href="([^"]+)"><strong>([^<]*)</strong>',m.group(2))
    chs.append((m.group(1),items))
CSS='''  /* sidebar */
  nav.side { position: fixed; top: 0; left: 0; bottom: 0; width: 290px; overflow-y: auto; background: var(--card);
             border-right: 1px solid var(--line); padding: 16px 12px 32px; font-size: 14px; line-height: 1.4; z-index: 10; }
  nav.side .home { display: block; font-weight: 700; font-size: 15px; text-decoration: none; color: var(--text); padding: 6px 8px 12px; }
  nav.side details { margin-bottom: 2px; }
  nav.side summary { cursor: pointer; font-weight: 600; padding: 7px 8px; border-radius: 8px; list-style-position: inside; }
  nav.side summary:hover { background: var(--brand-soft); }
  nav.side ul { list-style: none; margin: 2px 0 6px; padding: 0; }
  nav.side li a { display: block; padding: 6px 8px 6px 22px; border-radius: 8px; text-decoration: none; color: var(--text); }
  nav.side li a:hover { background: var(--brand-soft); }
  nav.side li a.cur { background: var(--brand-soft); color: var(--brand); font-weight: 700; }
  body { padding-left: 290px; }
  nav.side .toggle { display: none; }
  @media (max-width: 900px) {
    body { padding-left: 0; }
    nav.side { position: static; width: auto; border-right: 0; border-bottom: 1px solid var(--line); padding: 10px 12px; max-height: none; overflow: visible; }
    nav.side .toggle { display: block; }
    nav.side .menu { display: none; max-height: 60vh; overflow-y: auto; margin-top: 8px; }
    nav.side.open .menu { display: block; }
    nav.side .home { display: inline-block; padding: 6px 0; }
    nav.side .toggle { float: right; background: var(--brand); color: #fff; border: 0; border-radius: 8px; padding: 6px 14px; font-size: 14px; }
  }
'''
JS='''<script>
(function(){var n=document.querySelector('nav.side');if(!n)return;
var b=n.querySelector('.toggle');b.addEventListener('click',function(){n.classList.toggle('open')});
var c=n.querySelector('a.cur');if(c&&n.scrollTo){var t=c.offsetTop-n.clientHeight/3;if(getComputedStyle(n).position==='fixed')n.scrollTop=t;}})();
</script>
'''
def nav(cur):
    s='<nav class="side">\n<button class="toggle" type="button">☰ Mục lục</button>\n<a class="home" href="index.html">📘 Cẩm nang TNTDRINK ERP</a>\n<div class="menu">\n'
    for t,items in chs:
        op=' open' if any(h==cur for h,_ in items) else ''
        s+=f'<details{op}><summary>{t}</summary><ul>'
        for h,n in items:
            s+=f'<li><a href="{h}"'+(' class="cur"' if h==cur else '')+f'>{n}</a></li>'
        s+='</ul></details>\n'
    return s+'</div>\n</nav>\n'
for f in glob.glob('*.html'):
    x=open(f,encoding='utf-8').read()
    x=re.sub(r'<nav class="side">.*?</nav>\n','',x,flags=re.S)
    x=re.sub(r'  /\* sidebar \*/.*?(?=</style>)','',x,flags=re.S)
    x=x.replace(JS,'')
    x=x.replace('</style>',CSS+'</style>',1)
    x=x.replace('<body>\n','<body>\n'+nav(f),1)
    x=x.replace('</body>',JS+'</body>',1)
    open(f,'w',encoding='utf-8').write(x)
print(len(chs),sum(len(i) for _,i in chs))
