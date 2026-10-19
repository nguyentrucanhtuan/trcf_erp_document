"""Sinh _site/*.html từ noi-dung/*.md — Markdown là bản gốc, HTML là bản sinh ra.

Chạy:  python3 tools/build.py      → mở _site/index.html để xem thử
Không cần cài gì thêm (chỉ dùng thư viện chuẩn Python).
_site/ không commit: GitHub Actions chạy lại lệnh này mỗi lần push rồi đăng web.

Cú pháp Markdown dùng trong cẩm nang: xem README.md, mục "Cách sửa bài".
"""
import glob
import html
import os
import re
import shutil
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
SRC = os.path.join(ROOT, 'noi-dung')
OUT = os.path.join(ROOT, '_site')
CSS = open(os.path.join(ROOT, 'tools', 'style.css'), encoding='utf-8').read()
SITE_NAME = 'Cẩm nang TNTDRINK ERP'
SKIP = set()  # tệp .md trong noi-dung/ không sinh thành trang (nếu có)

NOTE = {'CAUTION': ('danger', '⚠️'), 'WARNING': ('warn', '⚠️'), 'TIP': ('tip', '💡'),
        'IMPORTANT': ('danger', '⚠️'), 'NOTE': ('tip', '💡')}

warnings = []


# ---------- inline ----------

def inline(s):
    """**đậm**, *nghiêng*, `mã`, [chữ](tệp.md), ==đường dẫn menu==."""
    out, i = [], 0
    for m in re.finditer(r'`([^`]+)`', s):
        out.append(_inline_text(s[i:m.start()]))
        out.append('<code>' + html.escape(m.group(1), quote=False) + '</code>')
        i = m.end()
    out.append(_inline_text(s[i:]))
    return ''.join(out)


def _inline_text(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', lambda m: f'<a href="{_href(m.group(2))}">{m.group(1)}</a>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])', r'<em>\1</em>', s)
    s = re.sub(r'==(.+?)==', r'<span class="path">\1</span>', s)
    return s


def _href(h):
    h = html.unescape(h)
    if not re.match(r'[a-z]+:', h):
        if h.endswith('.md'):
            h = h[:-3] + '.html'
        target = h.split('#')[0]
        if target and not os.path.exists(os.path.join(SRC, target)) \
                and not os.path.exists(os.path.join(SRC, target[:-5] + '.md')):
            warnings.append(f'link hỏng: {h}')
    return html.escape(h)


# ---------- block ----------

def parse_front(text):
    meta = {}
    if text.startswith('---\n'):
        head, text = text[4:].split('\n---\n', 1)
        for line in head.splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                meta[k.strip()] = v.strip()
    return meta, text


def blocks(lines):
    """Chia dòng thành khối: ('h', level, text) ('p', text) ('ul'/'ol'/'check', items)
    ('table', rows) ('img', alt, src) ('quote', lines) ('code', text)."""
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        st = line.strip()
        if not st:
            i += 1
            continue
        if st.startswith('```'):
            j = i + 1
            while j < n and not lines[j].strip().startswith('```'):
                j += 1
            out.append(('code', '\n'.join(lines[i + 1:j])))
            i = j + 1
            continue
        m = re.match(r'(#{1,4})\s+(.*)', st)
        if m:
            out.append(('h', len(m.group(1)), m.group(2).strip()))
            i += 1
            continue
        if st.startswith('>'):
            j = i
            while j < n and lines[j].strip().startswith('>'):
                j += 1
            out.append(('quote', [re.sub(r'^\s*>\s?', '', l) for l in lines[i:j]]))
            i = j
            continue
        if st.startswith('|'):
            j = i
            while j < n and lines[j].strip().startswith('|'):
                j += 1
            rows = [[c.strip() for c in re.split(r'(?<!\\)\|', l.strip())[1:-1]] for l in lines[i:j]]
            rows = [[c.replace('\\|', '|') for c in r] for r in rows if not all(re.fullmatch(r':?-+:?', c) for c in r)]
            out.append(('table', rows))
            i = j
            continue
        m = re.fullmatch(r'!\[(.*)\]\((\S+)\)', st)
        if m:
            out.append(('img', m.group(1), m.group(2)))
            i += 1
            continue
        if re.match(r'([-*]|\d+\.)\s', st):
            kind = 'ol' if re.match(r'\d+\.', st) else 'ul'
            if re.match(r'[-*]\s\[[ xX]\]\s', st):
                kind = 'check'
            items = []
            while i < n and lines[i].strip():
                l = lines[i]
                m = re.match(r'(\s*)(?:[-*]|\d+\.)\s(?:\[[ xX]\]\s)?(.*)', l)
                if m and len(m.group(1)) < 2:
                    items.append([m.group(2), []])
                elif m and items:
                    items[-1][1].append(m.group(2))
                elif items:  # dòng nối tiếp của mục trước
                    items[-1][0] += ' ' + l.strip()
                i += 1
            out.append((kind, items))
            continue
        j = i
        while j < n and lines[j].strip() and not re.match(r'(#|>|\||```|!\[|[-*]\s|\d+\.\s)', lines[j].strip()):
            j += 1
        j = max(j, i + 1)
        out.append(('p', ' '.join(l.strip() for l in lines[i:j])))
        i = j
    return out


def render_list(kind, items):
    tag = 'ol' if kind == 'ol' else 'ul'
    lis = []
    for text, subs in items:
        sub = ''.join(f'<li>{inline(s)}</li>' for s in subs)
        lis.append(f'<li>{inline(text)}' + (f'<ul>{sub}</ul>' if sub else '') + '</li>')
    return f'<{tag}>' + ''.join(lis) + f'</{tag}>'


def render_block(b):
    k = b[0]
    if k == 'p':
        return f'<p>{inline(b[1])}</p>'
    if k in ('ul', 'ol'):
        return render_list(k, b[1])
    if k == 'check':
        lis = ''.join(f'<li><label><input type="checkbox"><span>{inline(t)}</span></label></li>' for t, _ in b[1])
        return f'<ul class="check">{lis}</ul>'
    if k == 'table':
        head, *body = b[1]
        th = ''.join(f'<th>{inline(c)}</th>' for c in head)
        trs = ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>' for r in body)
        return f'<div class="table-wrap"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'
    if k == 'img':
        alt, src = b[1], b[2]
        if not os.path.exists(os.path.join(SRC, src)):
            warnings.append(f'thiếu ảnh: {src}')
        return f'<img class="shot" src="{html.escape(src)}" alt="{html.escape(alt)}">'
    if k == 'code':
        return f'<pre class="example">{html.escape(b[1], quote=False)}</pre>'
    if k == 'quote':
        lines = b[1]
        m = re.fullmatch(r'\[!(\w+)\]', lines[0].strip()) if lines else None
        inner = ''.join(render_block(x) for x in blocks(lines[1:] if m else lines))
        if m:
            cls, ic = NOTE.get(m.group(1).upper(), ('tip', '💡'))
            return f'<div class="note {cls}"><div class="ic">{ic}</div><div>{inner}</div></div>'
        return f'<div class="example">{inner}</div>'
    if k == 'h':
        lv = min(b[1], 6)
        return f'<h{lv}>{inline(b[2])}</h{lv}>'
    raise ValueError(b)


def render_article(bs):
    """## N. … mở một khung (section). ### Bước N: … là một bước (khung xanh có số)."""
    out, in_section, in_step = [], False, False
    title = ''
    for b in bs:
        if b[0] == 'h' and b[1] == 1:
            title = b[2]
            continue
        is_sec = b[0] == 'h' and b[1] == 2 and re.match(r'\d+\.\s', b[2])
        step = b[0] == 'h' and b[1] == 3 and re.match(r'(Bước\s+\d+)\s*[:—–-]\s*(.*)', b[2])
        if in_step and (b[0] == 'h' and b[1] <= 3):
            out.append('</div>')
            in_step = False
        if is_sec:
            if in_section:
                out.append('</section>')
            out.append('<section>')
            in_section = True
            out.append(render_block(b))
        elif step:
            out.append(f'<div class="step"><h3><span>{step.group(1)}</span>{inline(step.group(2))}</h3>')
            in_step = True
        else:
            if not in_section:
                out.append('<section>')
                in_section = True
            out.append(render_block(b))
    if in_step:
        out.append('</div>')
    if in_section:
        out.append('</section>')
    return title, '\n'.join(out)


def parse_index(bs):
    """index.md: ## Giai đoạn: X → nhóm; ### Bước N — Tên → ô; dòng thường → mô tả; list link → nút con."""
    intro, phases = [], []
    for b in bs:
        if b[0] == 'h' and b[1] == 2 and b[2].lower().startswith('giai đoạn'):
            phases.append({'name': b[2].split(':', 1)[1].strip(), 'steps': []})
        elif b[0] == 'h' and b[1] == 3 and phases:
            m = re.match(r'Bước\s+(\d+)\s*[:—–-]\s*(.*)', b[2])
            phases[-1]['steps'].append({'no': m.group(1), 'name': m.group(2), 'desc': [], 'links': []})
        elif phases and phases[-1]['steps']:
            s = phases[-1]['steps'][-1]
            if b[0] == 'ul':
                for text, _ in b[1]:
                    m = re.fullmatch(r'\[(.+)\]\((\S+)\)', text.strip())
                    s['links'].append((_href(m.group(2)), m.group(1)))
            else:
                s['desc'].append(b)
        else:
            intro.append(b)
    return intro, phases


def render_index(bs):
    intro, phases = parse_index(bs)
    title, body = render_article(intro)
    out = [body]
    for k, ph in enumerate(phases):
        if k:
            out.append('<div class="arrow">↓</div>')
        out.append(f'<div class="phase">{html.escape(ph["name"])}</div>\n<ol class="flow">')
        for s in ph['steps']:
            desc = ''.join(render_block(d) for d in s['desc'])
            sub = ''.join(f'<a href="{h}">{inline(t)}</a>' for h, t in s['links'])
            out.append(f'<li><span class="no">{s["no"]}</span><h3>{inline(s["name"])}</h3>{desc}<div class="sub">{sub}</div></li>')
        out.append('</ol>')
    return title, '\n'.join(out), phases


def nav(phases, cur):
    s = ['<nav class="side">', '<button class="toggle" type="button">☰ Mục lục</button>',
         f'<a class="home" href="index.html">📘 {SITE_NAME}</a>', '<div class="menu">']
    for ph in phases:
        for st in ph['steps']:
            op = ' open' if any(h == cur for h, _ in st['links']) else ''
            lis = ''.join(f'<li><a href="{h}"' + (' class="cur"' if h == cur else '') + f'>{inline(t)}</a></li>'
                          for h, t in st['links'])
            s.append(f'<details{op}><summary>Bước {st["no"]} — {inline(st["name"])}</summary><ul>{lis}</ul></details>')
    return '\n'.join(s + ['</div>', '</nav>'])


JS = '''<script>
(function(){var n=document.querySelector('nav.side');if(!n)return;
var b=n.querySelector('.toggle');b.addEventListener('click',function(){n.classList.toggle('open')});
var c=n.querySelector('a.cur');if(c&&n.scrollTo){var t=c.offsetTop-n.clientHeight/3;if(getComputedStyle(n).position==='fixed')n.scrollTop=t;}})();
</script>'''


def page(title, crumb, h1, body, navhtml):
    return f'''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- TỆP SINH TỰ ĐỘNG từ tệp .md cùng tên — đừng sửa ở đây, sửa .md rồi chạy: python3 tools/build.py -->
<title>{html.escape(title)}</title>
<style>
{CSS}</style>
</head>
<body>
{navhtml}
<main>
<div class="crumb">{inline(crumb)}</div>
<h1>{inline(h1)}</h1>
{body}
</main>
{JS}
</body>
</html>
'''


def read(path):
    meta, text = parse_front(open(path, encoding='utf-8').read())
    return meta, blocks(text.splitlines())


def main():
    meta, bs = read(os.path.join(SRC, 'index.md'))
    h1, body, phases = render_index(bs)
    pages = {'index.html': page(meta.get('title', SITE_NAME), meta.get('crumb', ''), h1, body, nav(phases, 'index.html'))}
    listed = {h for ph in phases for st in ph['steps'] for h, _ in st['links']}

    for md in sorted(glob.glob(os.path.join(SRC, '*.md'))):
        name = os.path.basename(md)
        if name == 'index.md' or name in SKIP:
            continue
        out = name[:-3] + '.html'
        meta, bs = read(md)
        h1, body = render_article(bs)
        if not h1:
            warnings.append(f'{name}: thiếu tiêu đề "# ..."')
        if out not in listed:
            warnings.append(f'{name}: chưa có trong mục lục index.md')
        pages[out] = page(meta.get('title', h1), meta.get('crumb', ''), h1, body, nav(phases, out))

    shutil.rmtree(OUT, ignore_errors=True)
    shutil.copytree(os.path.join(SRC, 'images'), os.path.join(OUT, 'images'))
    for out, text in pages.items():
        open(os.path.join(OUT, out), 'w', encoding='utf-8').write(text)
    for h in sorted(listed - set(pages)):
        warnings.append(f'index.md trỏ tới {h} nhưng không có tệp .md')

    print(f'Đã sinh {len(pages)} trang HTML trong _site/')
    for w in warnings:
        print('  ⚠', w)
    return 1 if warnings else 0


if __name__ == '__main__':
    sys.exit(main())
