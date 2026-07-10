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

NAVLINKS=[('mozg','Мозг','wb'),('telo','Тело','wt'),('dengi','Деньги','wm'),
          ('programs','Программы',''),('knigi','Книги',''),('nauka','Наука',''),('o-nas','О нас','')]

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
<div><h4>Портал</h4><a href="programs.html">Программы</a><a href="knigi.html">Книги</a><a href="nauka.html">Наука</a><a href="o-nas.html">О нас</a></div>
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

def bullet(text):
    return '<li><span class="bm">%s</span><span>%s</span></li>' % (DNA, text)

def phero(img, eyebrow, h1, p, crumb):
    return '''<section class="phero"><div class="wrap"><div class="phero-card"><img class="bg" src="%s" alt="">
<div class="phero-in"><div class="crumbs"><a href="index.html">Главная</a> · %s</div>
<div class="eyebrow" style="margin-top:14px">%s</div><h1>%s</h1><p>%s</p></div></div></div></section>''' % (img, crumb, eyebrow, h1, p)

def cta_band(h, p, btn, url):
    return '''<section><div class="wrap"><div class="ctaband"><h2>%s</h2><p>%s</p>
<a class="btn light bracket" href="%s" target="_blank" rel="noopener">%s</a></div></div></section>''' % (h,p,url,btn)
