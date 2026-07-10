# -*- coding: utf-8 -*-
# Генератор страниц портала «Архитектура сознания». Общие шапка/подвал, единый стиль.
import os

MARK = '''<svg class="mark" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="48" height="48" rx="13" fill="url(#g)"/><path d="M13 33V25c0-6.08 4.92-11 11-11s11 4.92 11 11v8" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/><path d="M18.5 33v-8a5.5 5.5 0 0 1 11 0v8" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".7"/><circle cx="24" cy="25" r="2.6" fill="#fff"/><defs><linearGradient id="g" x1="0" y1="0" x2="48" y2="48" gradientUnits="userSpaceOnUse"><stop stop-color="#2f6bff"/><stop offset="1" stop-color="#221a5e"/></linearGradient></defs></svg>'''

IC_BRAIN='<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none"><path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-1.5 5.6A3 3 0 0 0 6 18a3 3 0 0 0 3 2V4Zm6 0a3 3 0 0 1 3 3 3 3 0 0 1 1.5 5.6A3 3 0 0 1 18 18a3 3 0 0 1-3 2V4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>'
IC_BODY='<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none"><path d="M12 20s-7-4.35-7-9.5A3.5 3.5 0 0 1 12 8a3.5 3.5 0 0 1 7 2.5C19 15.65 12 20 12 20Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M5 13h3l1.5-3 2 5 1.5-3H19" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
IC_MONEY='<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none"><path d="M4 19V9m5 10V5m5 14v-6m5 6V8" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M4 9l5-4 5 4 5-3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" opacity=".55"/></svg>'
IC_CLOCK='<svg width="15" height="15" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.8"/><path d="M12 7v5l3 2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'
DNA='<svg width="19" height="19" viewBox="0 0 24 24" fill="none"><path d="M8 3c0 4.5 8 4.5 8 9s-8 4.5-8 9M16 3c0 4.5-8 4.5-8 9s8 4.5 8 9" stroke="#fff" stroke-width="1.7" stroke-linecap="round"/><path d="M9.3 7h5.4M9.3 17h5.4M8.4 12h7.2" stroke="#fff" stroke-width="1.4" stroke-linecap="round" opacity=".8"/></svg>'
def wing_ic(w,s=22):
    return {'b':IC_BRAIN,'t':IC_BODY,'m':IC_MONEY}[w] % (s,s)

NAVLINKS=[('index','Главная',''),('mozg','Мозг','wb'),('telo','Тело','wt'),('dengi','Деньги','wm'),
          ('programs','Программы',''),('sessions','Сессии',''),('knigi','Книги',''),
          ('nauka','Наука',''),('o-nas','О нас','')]

def header(active=''):
    links=''
    for slug,label,cls in NAVLINKS:
        on=' on' if slug==active else ''
        links+='<a class="%s%s" href="%s.html">%s</a>' % (cls,on,slug,label)
    return '''<header><div class="wrap nav">
<a class="brand" href="index.html" aria-label="Архитектура сознания">%s<span class="bt"><b>АРХИТЕКТУРА</b><span>сознания</span></span></a>
<nav class="menu">%s</nav>
<div class="nav-r"><a class="shop" href="https://thebodymindcode.github.io/shop/" target="_blank" rel="noopener">Магазин</a>
<a class="enter" href="kontakty.html"><svg width="17" height="17" viewBox="0 0 24 24" fill="none"><path d="M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8ZM5 20a7 7 0 0 1 14 0" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>Войти</a>
<button class="burger" aria-label="Меню"><span></span><span></span><span></span></button></div>
</div></header>''' % (MARK, links)

FOOTER='''<footer><div class="wrap"><div class="grid">
<div><div class="fbrand"><svg width="40" height="40" viewBox="0 0 48 48" fill="none"><rect width="48" height="48" rx="13" fill="url(#g2)"/><path d="M13 33V25c0-6.08 4.92-11 11-11s11 4.92 11 11v8" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/><circle cx="24" cy="25" r="2.6" fill="#fff"/><defs><linearGradient id="g2" x1="0" y1="0" x2="48" y2="48"><stop stop-color="#2f6bff"/><stop offset="1" stop-color="#221a5e"/></linearGradient></defs></svg><b>АРХИТЕКТУРА СОЗНАНИЯ</b></div>
<p class="fl">Портал по осознанности. Знание о покое, теле и достатке, собранное в программы. Дарья и Алексей.</p></div>
<div><h4>Крылья</h4><a href="mozg.html">Мозг</a><a href="telo.html">Тело</a><a href="dengi.html">Деньги</a></div>
<div><h4>Портал</h4><a href="programs.html">Программы</a><a href="sessions.html">Сессии</a><a href="knigi.html">Книги</a><a href="nauka.html">Наука</a><a href="o-nas.html">О нас</a></div>
<div><h4>Связь</h4><a href="https://t.me/+bo3a92A06cQ3NWMy" target="_blank" rel="noopener">Канал Дарьи</a><a href="https://t.me/+aEgupwOOOq84YTNi" target="_blank" rel="noopener">Канал Алексея</a><a href="kontakty.html">Контакты</a></div>
</div><div class="bot"><span>© 2026 Архитектура сознания</span><span>Портал в разработке, версия 0.5</span></div></div></footer>'''

BURGER_JS='''<script>document.querySelector('.burger').addEventListener('click',function(){var m=document.querySelector('.menu');var open=m.style.display==='flex';m.style.cssText=open?'':'display:flex;position:absolute;top:88px;left:0;right:0;background:#fff;flex-direction:column;padding:20px 24px;border-bottom:1px solid var(--line);gap:16px;box-shadow:var(--sh2);z-index:90'});</script>'''

def page(slug, title, body, desc, active=''):
    html='''<!doctype html><html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%s</title><meta name="description" content="%s">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css"></head><body>%s%s%s%s</body></html>''' % (title, desc, header(active), body, FOOTER, BURGER_JS)
    open(slug+'.html','w',encoding='utf-8').write(html)
    print('written', slug+'.html', len(html))

# ---------- продукты ----------
def card(w, chip, name, fmt, price, url):
    cic='<span class="cic">%s</span>' % wing_ic(w)
    return '''<div class="card %s"><div class="top"><span class="chip %s">%s</span>%s</div>
<h3>%s</h3><div class="fmt">%s%s</div>
<div class="foot"><span class="price">%s</span><a class="go" href="%s" target="_blank" rel="noopener">Открыть →</a></div></div>''' % (
        w, {'b':'brain','t':'body','m':'money'}[w], chip, cic, name, IC_CLOCK, fmt, price, url)

# иконки буллетов по СМЫСЛУ (заказ Алексея: каждый буллет рисуется под своё содержание)
BICONS = {
 'dna': DNA,
 'brain': '<svg width="19" height="19" viewBox="0 0 24 24" fill="none"><path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-1.5 5.6A3 3 0 0 0 6 18a3 3 0 0 0 3 2V4Zm6 0a3 3 0 0 1 3 3 3 3 0 0 1 1.5 5.6A3 3 0 0 1 18 18a3 3 0 0 1-3 2V4Z" stroke="#fff" stroke-width="1.7" stroke-linejoin="round"/></svg>',
 'clock': '<svg width="19" height="19" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="#fff" stroke-width="1.7"/><path d="M12 7v5l3 2" stroke="#fff" stroke-width="1.7" stroke-linecap="round"/></svg>',
 'grow': '<svg width="19" height="19" viewBox="0 0 24 24" fill="none"><path d="M4 20h16M6 20V11m6 9V6m6 14v-9" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/><path d="M5 8l4-3 4 3 5-4" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" opacity=".75"/></svg>',
 'waves': '<svg width="19" height="19" viewBox="0 0 24 24" fill="none"><path d="M3 9c3-2.5 6-2.5 9 0s6 2.5 9 0M3 15c3-2.5 6-2.5 9 0s6 2.5 9 0" stroke="#fff" stroke-width="1.7" stroke-linecap="round"/></svg>',
 'moon': '<svg width="19" height="19" viewBox="0 0 24 24" fill="none"><path d="M20 13.5A8 8 0 1 1 10.5 4 6.5 6.5 0 0 0 20 13.5Z" stroke="#fff" stroke-width="1.7" stroke-linejoin="round"/></svg>',
 'book': '<svg width="19" height="19" viewBox="0 0 24 24" fill="none"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5V5.5Z" stroke="#fff" stroke-width="1.7" stroke-linejoin="round"/><path d="M4 20.5A2.5 2.5 0 0 1 6.5 18H20" stroke="#fff" stroke-width="1.7"/></svg>',
 'heart': '<svg width="19" height="19" viewBox="0 0 24 24" fill="none"><path d="M12 20s-7-4.35-7-9.5A3.5 3.5 0 0 1 12 8a3.5 3.5 0 0 1 7 2.5C19 15.65 12 20 12 20Z" stroke="#fff" stroke-width="1.7" stroke-linejoin="round"/></svg>',
}
def cardx(w, chip, name, fmt, price, url, desc):
    cic='<span class="cic">%s</span>' % wing_ic(w)
    return '''<div class="card %s"><div class="top"><span class="chip %s">%s</span>%s</div>
<h3>%s</h3><div class="fmt">%s%s</div><p class="desc">%s</p>
<div class="foot"><span class="price">%s</span><a class="go" href="%s" target="_blank" rel="noopener">Открыть →</a></div></div>''' % (
        w, {'b':'brain','t':'body','m':'money'}[w], chip, cic, name, IC_CLOCK, fmt, desc, price, url)

def bullet(text, icon='dna'):
    return '<li><span class="bm">%s</span><span>%s</span></li>' % (BICONS.get(icon, DNA), text)

# иконки соцсетей (крутые SVG вместо голого текста)
SOC_IC = {
 'Instagram': '<svg width="15" height="15" viewBox="0 0 24 24" fill="none"><rect x="3.5" y="3.5" width="17" height="17" rx="5" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.8"/><circle cx="17.2" cy="6.8" r="1.3" fill="currentColor"/></svg>',
 'YouTube': '<svg width="15" height="15" viewBox="0 0 24 24" fill="none"><rect x="2.5" y="6" width="19" height="12.5" rx="4" stroke="currentColor" stroke-width="1.8"/><path d="M10.5 9.8l4.5 2.45-4.5 2.45V9.8Z" fill="currentColor"/></svg>',
 'TikTok': '<svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M14 4v9.5a3.75 3.75 0 1 1-3.2-3.71" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/><path d="M14 6.5c.9 1.9 2.6 3.1 4.7 3.3" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>',
 'Telegram': '<svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M20.5 4.5 3.8 11c-.8.3-.75 1.4.06 1.66l4.2 1.34 1.6 4.9c.25.77 1.24.9 1.7.23l2.1-3.1 4.3 3.2c.62.46 1.5.12 1.66-.63l2-12.9c.14-.9-.74-1.6-1.62-1.3Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
 'Threads': '<svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M12 21c-4.5 0-7.5-3.2-7.5-9S7.5 3 12 3c3.8 0 6.3 2 7.1 5.1" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M9.5 13.6c0-2 1.6-3.1 3.4-3.1 2.1 0 3.6 1.3 3.6 3.5 0 2.4-1.7 3.9-3.7 3.9-1.6 0-3-.9-3-2.3 0-1.3 1.1-2.1 2.7-2.2 1.9-.15 4.5.4 5.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
 'Поддержка': '<svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M4 6h16v10.5H9L5.5 20v-3.5H4V6Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M8 10h8M8 13h5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
}
def soc(name, url):
    return '<a href="%s" target="_blank" rel="noopener">%s%s</a>' % (url, SOC_IC.get(name,''), name)

def phero(img, eyebrow, h1, p, crumb, labels=None):
    lab = hero_labels(labels) if labels else ''
    return '''<section class="phero"><div class="wrap"><div class="phero-card"><img class="bg" src="%s" alt="">%s
<div class="phero-in"><div class="crumbs"><a href="index.html">Главная</a> · %s</div>
<div class="eyebrow" style="margin-top:14px">%s</div><h1>%s</h1><p>%s</p></div></div></div></section>''' % (img, lab, crumb, eyebrow, h1, p)

def hero_labels(labels):
    # чипы соединены в нейросеть: линии + светящиеся узлы-точки (на чипах и в узлах сегментов),
    # плюс пара свободных точек-созвездий, как на фоновой картинке
    node = [(70,26),(85,46),(74,66),(58,40),(64,80)]
    extra = [(90,32),(52,58),(80,74)]  # свободные точки-звёзды
    n = min(len(labels), len(node)); pts = node[:n]
    segs = [(a,b) for a,b in [(0,1),(1,2),(3,0),(3,2),(2,4)] if a<n and b<n]
    # линии чип-чип и чип-свободная точка
    lines = ''.join('<line x1="%s" y1="%s" x2="%s" y2="%s"/>'%(pts[a][0],pts[a][1],pts[b][0],pts[b][1]) for a,b in segs)
    if n>=2: lines += '<line x1="%s" y1="%s" x2="%s" y2="%s"/>'%(pts[1][0],pts[1][1],extra[0][0],extra[0][1])
    if n>=4: lines += '<line x1="%s" y1="%s" x2="%s" y2="%s"/>'%(pts[3][0],pts[3][1],extra[1][0],extra[1][1])
    if n>=3: lines += '<line x1="%s" y1="%s" x2="%s" y2="%s"/>'%(pts[2][0],pts[2][1],extra[2][0],extra[2][1])
    svg = '<svg class="net" viewBox="0 0 100 100" preserveAspectRatio="none">%s</svg>' % lines
    dots = ''
    for x,y in pts: dots += '<i class="node" style="left:%s%%;top:%s%%"></i>'%(x,y)
    for x,y in extra[:max(0,n-1)]: dots += '<i class="node sm" style="left:%s%%;top:%s%%"></i>'%(x,y)
    for a,b in segs:  # узел в середине сегмента
        mx=(pts[a][0]+pts[b][0])/2; my=(pts[a][1]+pts[b][1])/2
        dots += '<i class="node sm" style="left:%s%%;top:%s%%"></i>'%(mx,my)
    chips = ''.join('<span style="left:%s%%;top:%s%%">%s</span>'%(pts[i][0],pts[i][1],labels[i]) for i in range(n))
    return '<div class="labels">%s%s%s</div>' % (svg, dots, chips)

def factbox(th, body, src, cls=''):
    srch = '<div class="src">%s</div>' % src if src else ''
    return '<div class="factbox %s"><div class="th">%s</div><p>%s</p>%s</div>' % (cls, th, body, srch)
def pullq(text, cite, cls=''):
    return '<div class="pullquote %s">«%s»<cite>%s</cite></div>' % (cls, text, cite)
def mq_wrap(text, cite, cls=''):
    return '<div class="miniquote %s"><q>%s</q><cite>%s</cite></div>' % (cls, text, cite)
def pullq_section(text, cls=''):
    return '<section><div class="wrap"><div class="pullbig %s">%s</div></div></section>' % (cls, text)
def statband(items, hi=None, hic=''):
    tiles=''
    for i,(n,l) in enumerate(items):
        c=' hi '+hic if hi==i else ''
        tiles+='<div class="stat%s"><b>%s</b><span>%s</span></div>'%(c,n,l)
    return '<div class="stats">%s</div>'%tiles
def fgrid(*boxes):
    return '<div class="factgrid">%s</div>' % ''.join(boxes)
def wsci(cls, eyebrow, h2, *boxes):
    ec={'w1':'','w2':'t','w3':'m'}.get(cls,'')
    return '<section><div class="wrap"><div class="sec-h"><span class="eyebrow %s">%s</span><h2>%s</h2></div>%s</div></section>' % (ec, eyebrow, h2, fgrid(*boxes))
def wfaq(items):
    inner=''.join('<details%s><summary>%s<span></span></summary><p>%s</p></details>'%(' open' if i==0 else '',q,a) for i,(q,a) in enumerate(items))
    return '<section class="soft"><div class="wrap"><div class="sec-h center"><span class="eyebrow">Вопросы</span><h2>Коротко о главном</h2></div><div class="faq">%s</div></div></section>'%inner

def cta_band(h, p, btn, url):
    return '''<section><div class="wrap"><div class="ctaband"><h2>%s</h2><p>%s</p>
<a class="btn light bracket" href="%s" target="_blank" rel="noopener">%s</a></div></div></section>''' % (h,p,url,btn)
