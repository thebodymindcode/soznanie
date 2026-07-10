# -*- coding: utf-8 -*-
# Генератор страниц портала «Архитектура сознания». Общие шапка/подвал, единый стиль.
import os

def brand_mark(cls='', px=None):
    # премиум бренд-значок: мозг из двух полушарий + нейро-узлы и связи, на градиенте бренда
    size = 'width="%d" height="%d" ' % (px, px) if px else ''
    clsa = 'class="%s" ' % cls if cls else ''
    gid = 'bm-' + (cls or ('p%d' % (px or 0)))
    return ('<svg %s%sviewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">'
      '<defs><linearGradient id="%s" x1="0" y1="0" x2="48" y2="48" gradientUnits="userSpaceOnUse"><stop stop-color="#2f6bff"/><stop offset="1" stop-color="#221a5e"/></linearGradient></defs>'
      '<rect width="48" height="48" rx="13" fill="url(#%s)"/>'
      '<g stroke="#8fb4ff" stroke-width="1.1" stroke-linecap="round" opacity=".85"><line x1="15.5" y1="18" x2="9.2" y2="14.5"/><line x1="32.5" y1="18" x2="38.8" y2="14.5"/><line x1="24" y1="35" x2="24" y2="40"/></g>'
      '<g transform="translate(6,5) scale(1.5)" stroke="#fff" stroke-width="1.5" fill="none" stroke-linejoin="round" stroke-linecap="round">'
      '<path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-1.5 5.6A3 3 0 0 0 6 18a3 3 0 0 0 3 2V4Z"/>'
      '<path d="M15 4a3 3 0 0 1 3 3 3 3 0 0 1 1.5 5.6A3 3 0 0 1 18 18a3 3 0 0 1-3 2V4Z"/>'
      '<path d="M12 6.5v13" opacity=".55"/></g>'
      '<g fill="#fff"><circle cx="18.6" cy="19" r="1.5"/><circle cx="29.4" cy="19" r="1.5"/><circle cx="24" cy="28" r="1.5"/></g>'
      '<g fill="#cfe0ff"><circle cx="9.2" cy="14.5" r="1.5"/><circle cx="38.8" cy="14.5" r="1.5"/><circle cx="24" cy="40" r="1.5"/></g>'
      '</svg>') % (size, clsa, gid, gid)

MARK = brand_mark('mark')

IC_BRAIN='<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none"><path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-1.5 5.6A3 3 0 0 0 6 18a3 3 0 0 0 3 2V4Zm6 0a3 3 0 0 1 3 3 3 3 0 0 1 1.5 5.6A3 3 0 0 1 18 18a3 3 0 0 1-3 2V4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>'
IC_BODY='<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none"><path d="M12 20s-7-4.35-7-9.5A3.5 3.5 0 0 1 12 8a3.5 3.5 0 0 1 7 2.5C19 15.65 12 20 12 20Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M5 13h3l1.5-3 2 5 1.5-3H19" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
IC_MONEY='<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none"><path d="M4 19V9m5 10V5m5 14v-6m5 6V8" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M4 9l5-4 5 4 5-3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" opacity=".55"/></svg>'
IC_CLOCK='<svg width="15" height="15" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.8"/><path d="M12 7v5l3 2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'
DNA='<svg width="19" height="19" viewBox="0 0 24 24" fill="none"><path d="M8 3c0 4.5 8 4.5 8 9s-8 4.5-8 9M16 3c0 4.5-8 4.5-8 9s8 4.5 8 9" stroke="#fff" stroke-width="1.7" stroke-linecap="round"/><path d="M9.3 7h5.4M9.3 17h5.4M8.4 12h7.2" stroke="#fff" stroke-width="1.4" stroke-linecap="round" opacity=".8"/></svg>'
def wing_ic(w,s=22):
    return {'b':IC_BRAIN,'t':IC_BODY,'m':IC_MONEY}[w] % (s,s)

NAVLINKS=[('index','Главная',''),('mozg','Мозг','wb'),('telo','Тело','wt'),('dengi','Деньги','wm'),
          ('programs','Программы',''),('sessions','Сессии',''),('knigi','Книги',''),
          ('nauka','Наука','')]
NAVEND=[('o-nas','О нас','')]  # отдельный пункт в самом конце меню
# выпадающая «Библиотека»: ровный список с иконкой и подписью
MORE_TITLE='Библиотека'
MORE_ITEMS=[
  ('kviz','Индекс ясности','Тест на шум ума за две минуты','target'),
  ('praktiki','Практики','Таймеры дыхания и восстановления','breath'),
  ('blog','Статьи','Разборы, лонгриды и наука','doc'),
  # ('podhod','Подход',...) СКРЫТ по просьбе Алексея: черновой, ждёт нормального переписывания. Страница остаётся по ссылке.
]
MORE_SLUGS={s for s,_,_,_ in MORE_ITEMS}
MENU_IC={
 'target':'<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="8.2" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="12" r="3.4" stroke="currentColor" stroke-width="1.7"/></svg>',
 'compass':'<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="8.5" stroke="currentColor" stroke-width="1.7"/><path d="M15.5 8.5l-2.2 4.8-4.8 2.2 2.2-4.8 4.8-2.2Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
 'doc':'<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M6 3.5h7l5 5V20.5H6z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M13 3.5v5h5M9 13h6M9 16.5h4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
 'breath':'<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M3 10c3-2 6-2 9 0s6 2 9 0" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="M4 15c2.7-1.7 5.3-1.7 8 0s5.3 1.7 8 0" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" opacity=".65"/></svg>',
}

def header(active=''):
    links=''
    for slug,label,cls in NAVLINKS:
        on=' on' if slug==active else ''
        links+='<a class="%s%s" href="%s.html">%s</a>' % (cls,on,slug,label)
    rows=''
    for s,lbl,desc,ic in MORE_ITEMS:
        on=' on' if s==active else ''
        rows+=('<a class="mrow%s" href="%s.html"><span class="mi">%s</span>'
               '<span class="mtx"><b>%s</b><small>%s</small></span></a>')%(on,s,MENU_IC.get(ic,''),lbl,desc)
    trigon=' on' if active in MORE_SLUGS else ''
    more=('<div class="hasmenu"><button class="mtrig%s" aria-expanded="false" aria-haspopup="true">%s'
          '<svg class="car" width="12" height="12" viewBox="0 0 24 24" fill="none"><path d="M6 9l6 6 6-6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>'
          '<div class="mmenu">%s</div></div>')%(trigon,MORE_TITLE,rows)
    endlinks=''
    for slug,label,cls in NAVEND:
        on=' on' if slug==active else ''
        endlinks+='<a class="%s%s" href="%s.html">%s</a>'%(cls,on,slug,label)
    return '''<header><div class="wrap nav">
<a class="brand" href="index.html" aria-label="Архитектура сознания">%s<span class="bt"><b>АРХИТЕКТУРА</b><span>сознания</span></span></a>
<nav class="menu">%s%s%s</nav>
<div class="nav-r"><a class="shop" href="https://thebodymindcode.github.io/shop/" target="_blank" rel="noopener">Магазин</a>
<a class="enter" href="kontakty.html"><svg width="17" height="17" viewBox="0 0 24 24" fill="none"><path d="M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8ZM5 20a7 7 0 0 1 14 0" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>Войти</a>
<button class="burger" aria-label="Меню"><span></span><span></span><span></span></button></div>
</div></header>''' % (MARK, links, more, endlinks)

# премиум-иконки соцсетей (моно, currentColor)
_IG='<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="18" height="18" rx="5.4" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><circle cx="17.4" cy="6.6" r="1.25" fill="currentColor"/></svg>'
_YT='<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><rect x="2.4" y="5.6" width="19.2" height="12.8" rx="4.2" stroke="currentColor" stroke-width="1.7"/><path d="M10.4 9.3 15.2 12l-4.8 2.7V9.3Z" fill="currentColor"/></svg>'
_TT='<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M13.7 3.2v9.9a3.6 3.6 0 1 1-3.05-3.56" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M13.7 5.6c.85 1.9 2.55 3.15 4.75 3.35" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
_TH='<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M17.6 11.4c-.13-.06-.27-.12-.4-.17-.24-4.35-2.6-6.84-6.58-6.86-2.4-.02-4.4 1-5.63 2.86l1.78 1.22c.9-1.37 2.32-1.66 3.4-1.66h.03c1.36 0 2.38.4 3.05 1.18.48.57.8 1.35.96 2.34-1.2-.2-2.5-.26-3.9-.18-3.9.22-6.4 2.5-6.24 5.66.09 1.6.88 2.98 2.24 3.87 1.15.76 2.63 1.13 4.17 1.05 2.03-.11 3.63-.89 4.74-2.3.84-1.08 1.37-2.48 1.6-4.24.96.58 1.67 1.34 2.06 2.26.66 1.56.7 4.12-1.39 6.2l1.65 1.53c1.42-1.42 2.94-3.86 2.16-7.06-.55-2.24-2.03-3.68-3.93-4.63Zm-5.24 6.9c-1.7.1-3.47-.67-3.56-2.32-.06-1.22.87-2.58 3.67-2.74.32-.02.64-.03.94-.03.94 0 1.82.09 2.62.27-.3 3.73-2.05 4.46-3.67 4.55Z" fill="currentColor"/></svg>'
_TG='<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M21.3 4.3 2.9 11.4c-1 .38-.98 1.78.03 2.13l4.55 1.56 1.76 5.4c.28.85 1.37 1.03 1.9.28l2.5-3.55 4.55 3.36c.7.52 1.7.13 1.87-.72L22.9 5.7c.2-1-.68-1.82-1.6-1.4Z" fill="currentColor"/></svg>'

FOOTER=('<footer><div class="wrap"><div class="fgrid">'
'<div class="fbrand-col">'
'<div class="fbrand">'+brand_mark('',44)+'<b>АРХИТЕКТУРА<span>сознания</span></b></div>'
'<p class="fl">Портал по осознанности. Знание о покое, теле и достатке, проверенное наукой и собранное в программы.</p>'
'<a class="ftg" href="https://t.me/+bo3a92A06cQ3NWMy" target="_blank" rel="noopener">'
'<span class="ic">'+_TG+'</span>'
'<span class="tx"><b>Телеграм-канал</b><small>Присоединиться к «Архитектуре сознания»</small></span>'
'<span class="arr">→</span></a>'
'</div>'
'<div class="fnav"><h4>Разделы</h4><div class="flinks">'
'<a href="mozg.html">Мозг</a><a href="telo.html">Тело</a><a href="dengi.html">Деньги</a>'
'<a href="programs.html">Программы</a><a href="sessions.html">Сессии</a><a href="knigi.html">Книги</a>'
'<a href="nauka.html">Наука</a><a href="blog.html">Статьи</a>'
'<a href="o-nas.html">О нас</a><a href="kontakty.html">Контакты</a></div></div>'
'<div class="fppl">'
'<div class="pers"><div class="nm">Дарья Ростовцева</div><div class="rl">Инсайт, техники, эфиры</div>'
'<div class="sbtns">'
'<a class="sbtn" href="https://instagram.com/daryarostovtseva" target="_blank" rel="noopener" aria-label="Instagram Дарьи">'+_IG+'<span>Instagram</span></a>'
'<a class="sbtn" href="https://www.threads.com/@daryarostovtseva" target="_blank" rel="noopener" aria-label="Threads Дарьи">'+_TH+'<span>Threads</span></a>'
'</div></div>'
'<div class="pers"><div class="nm">Алексей Федотов</div><div class="rl">Структура, наука, проверка</div>'
'<div class="sbtns">'
'<a class="sbtn" href="https://instagram.com/thebodymindcode" target="_blank" rel="noopener" aria-label="Instagram Алексея">'+_IG+'<span>Instagram</span></a>'
'<a class="sbtn" href="https://www.youtube.com/@thebodymindcode" target="_blank" rel="noopener" aria-label="YouTube Алексея">'+_YT+'<span>YouTube</span></a>'
'<a class="sbtn" href="https://www.tiktok.com/@thebodymindcode" target="_blank" rel="noopener" aria-label="TikTok Алексея">'+_TT+'<span>TikTok</span></a>'
'</div></div>'
'<a class="fsupport" href="https://t.me/TheBodyMindCode_support" target="_blank" rel="noopener">'
'<span class="hs"><svg width="17" height="17" viewBox="0 0 24 24" fill="none"><path d="M5 12v-.6a7 7 0 0 1 14 0V12" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><rect x="2.8" y="12" width="3.7" height="6.3" rx="1.7" stroke="currentColor" stroke-width="1.8"/><rect x="17.5" y="12" width="3.7" height="6.3" rx="1.7" stroke="currentColor" stroke-width="1.8"/><path d="M19.3 18.3v.7a3 3 0 0 1-3 3H13.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></span>'
'<span>Написать в поддержку</span></a>'
'</div>'
'</div>'
'<div class="bot"><span>© 2026 «Архитектура сознания». Все права защищены.</span>'
'<span>Дарья Ростовцева и Алексей Федотов</span></div>'
'</div></footer>')

BURGER_JS='''<script>document.querySelector('.burger').addEventListener('click',function(){var h=document.querySelector('header').offsetHeight;var m=document.querySelector('.menu');var open=m.style.display==='flex';m.style.cssText=open?'':'display:flex;position:fixed;top:'+h+'px;left:0;right:0;background:#fff;flex-direction:column;padding:20px 24px;border-bottom:1px solid var(--line);gap:16px;box-shadow:var(--sh2);z-index:90;max-height:calc(100vh - '+h+'px);overflow:auto'});</script>'''

import hashlib, json
try: _CSSV=hashlib.md5(open('styles.css','rb').read()).hexdigest()[:8]
except Exception: _CSSV='1'

# ---------- SEO ----------
BASE='https://thebodymindcode.github.io/soznanie/'
ORG_SAMEAS=['https://t.me/thebodymindcode','https://instagram.com/thebodymindcode',
            'https://www.youtube.com/@thebodymindcode','https://www.tiktok.com/@thebodymindcode',
            'https://instagram.com/daryarostovtseva']
METRIKA_ID=''  # вставить номер счётчика Яндекс.Метрики сюда, когда Алексей даст (пока пусто = не подключён)
ORG_JSONLD=('{"@context":"https://schema.org","@type":"Organization","name":"Архитектура сознания",'
            '"url":"%s","logo":"%sapple-touch-icon.png","sameAs":%s}') % (BASE, BASE, json.dumps(ORG_SAMEAS, ensure_ascii=False))
WEBSITE_JSONLD='{"@context":"https://schema.org","@type":"WebSite","name":"Архитектура сознания","url":"%s"}' % BASE
METRIKA_TMPL=('<script type="text/javascript">(function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};'
  'm[i].l=1*new Date();for(var j=0;j<document.scripts.length;j++){if(document.scripts[j].src===r){return;}}'
  'k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})'
  '(window,document,"script","https://mc.yandex.ru/metrika/tag.js","ym");'
  'ym(%s,"init",{clickmap:true,trackLinks:true,accurateTrackBounce:true,webvisor:true});</script>'
  '<noscript><div><img src="https://mc.yandex.ru/watch/%s" style="position:absolute;left:-9999px" alt=""></div></noscript>')

def seo_head(slug, title, desc, ogimg=None):
    url = BASE if slug=='index' else BASE+slug+'.html'
    img = BASE + (ogimg or 'img/hero-1.jpg')
    return ('<link rel="canonical" href="%s">'
      '<meta property="og:type" content="website"><meta property="og:site_name" content="Архитектура сознания">'
      '<meta property="og:locale" content="ru_RU">'
      '<meta property="og:title" content="%s"><meta property="og:description" content="%s">'
      '<meta property="og:url" content="%s"><meta property="og:image" content="%s">'
      '<meta name="twitter:card" content="summary_large_image">'
      '<meta name="twitter:title" content="%s"><meta name="twitter:description" content="%s"><meta name="twitter:image" content="%s">'
      '<meta name="theme-color" content="#0f1226"><meta name="yandex-verification" content="">'
      '<link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png">'
      '<link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="manifest" href="site.webmanifest">'
      ) % (url, title, desc, url, img, title, desc, img)

def page(slug, title, body, desc, active='', ogimg=None, schema=''):
    seo = seo_head(slug, title, desc, ogimg)
    jsonld = '<script type="application/ld+json">%s</script><script type="application/ld+json">%s</script>' % (ORG_JSONLD, WEBSITE_JSONLD)
    if schema: jsonld += '<script type="application/ld+json">%s</script>' % schema
    met = (METRIKA_TMPL % (METRIKA_ID, METRIKA_ID)) if METRIKA_ID else ''
    html='''<!doctype html><html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%s</title><meta name="description" content="%s">
%s
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">%s</head><body>%s%s%s%s%s</body></html>''' % (title, desc, seo, jsonld, header(active), body, FOOTER, BURGER_JS, met)
    # гейт бренда: ни одного длинного тире в выводе (em → разделитель «·», en между числами → дефис)
    html = html.replace('—', '·').replace('–', '-')
    # версия CSS для кэш-бастинга: правки видны сразу, без старого кэша
    html = html.replace('href="styles.css"', 'href="styles.css?v=%s"' % _CSSV)
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

def infobars(title, bars, cls=''):
    rows=''.join('<div class="bar"><span>%s</span><div class="track"><div class="fill %s" style="width:%s%%"></div></div><b>%s</b></div>'%(l,cls,p,v) for l,p,v in bars)
    return '<figure class="info"><div class="ct">%s</div><div class="bars">%s</div></figure>'%(title,rows)

# ---------- своя SVG-инфографика ----------
def infofig(title, svg, cap):
    return ('<figure class="infofig"><div class="if-h">%s</div><div class="if-svg">%s</div>'
            '<figcaption>%s</figcaption></figure>') % (title, svg, cap)

def fig_dopamine():
    svg=('<svg viewBox="0 0 760 300" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="График дофаминовой волны">'
      '<defs><linearGradient id="dw" x1="0" y1="0" x2="760" y2="0"><stop stop-color="#2f6bff"/><stop offset="1" stop-color="#7a4bd0"/></linearGradient></defs>'
      '<line x1="60" y1="170" x2="720" y2="170" stroke="#c9d2ea" stroke-width="1.5" stroke-dasharray="5 6"/>'
      '<text x="724" y="174" font-size="12.5" fill="#8a90b3" font-family="sans-serif">норма</text>'
      '<path d="M60,170 C150,170 175,58 235,54 C300,50 320,150 360,192 C405,238 430,244 495,235 C585,222 640,176 720,171" stroke="url(#dw)" stroke-width="3.4" stroke-linecap="round"/>'
      '<circle cx="235" cy="54" r="5.5" fill="#2f6bff"/><circle cx="470" cy="238" r="5.5" fill="#e0603a"/>'
      '<text x="235" y="38" font-size="13.5" fill="#1a1f36" font-weight="700" text-anchor="middle" font-family="sans-serif">пик удовольствия</text>'
      '<text x="470" y="268" font-size="13.5" fill="#c0492a" font-weight="700" text-anchor="middle" font-family="sans-serif">провал ниже нормы</text>'
      '<text x="60" y="196" font-size="12.5" fill="#8a90b3" font-family="sans-serif">стимул</text>'
      '<text x="690" y="150" font-size="12.5" fill="#8a90b3" text-anchor="end" font-family="sans-serif">медленный возврат</text>'
      '</svg>')
    return infofig('Дофаминовая волна', svg,
      'Чем выше пик от сильного удовольствия, тем глубже откат под норму. Обычная жизнь после этого кажется пресной, пока уровень медленно возвращается.')

def fig_sleep():
    pts=[(80,54),(120,54),(120,150),(160,150),(160,232),(220,232),(220,150),(258,150),(258,100),(300,100),
         (300,150),(340,150),(340,222),(392,222),(392,150),(432,150),(432,100),(500,100),(500,150),(536,150),
         (536,205),(576,205),(576,150),(612,150),(612,100),(682,100),(682,54),(720,54)]
    poly=' '.join('%d,%d'%(x,y) for x,y in pts)
    rows=[('Бодрствование',54),('REM, сны',100),('Лёгкий сон',150),('Глубокий сон',232)]
    grid=''.join('<line x1="80" y1="%d" x2="720" y2="%d" stroke="#eef1f8" stroke-width="1.5"/>'
                 '<text x="72" y="%d" font-size="12" fill="#8a90b3" text-anchor="end" font-family="sans-serif">%s</text>'%(y,y,y+4,l) for l,y in rows)
    svg=('<svg viewBox="-78 0 838 280" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Гипнограмма ночного сна">'
      '<defs><linearGradient id="sw" x1="0" y1="0" x2="760" y2="0"><stop stop-color="#221a5e"/><stop offset="1" stop-color="#2f6bff"/></linearGradient></defs>'
      + grid +
      '<polyline points="'+poly+'" stroke="url(#sw)" stroke-width="3.2" stroke-linejoin="round" stroke-linecap="round" fill="none"/>'
      '<text x="80" y="270" font-size="12" fill="#8a90b3" font-family="sans-serif">засыпание</text>'
      '<text x="400" y="270" font-size="12" fill="#8a90b3" text-anchor="middle" font-family="sans-serif">~7,5 часа, 5 циклов по 90 минут</text>'
      '<text x="720" y="270" font-size="12" fill="#8a90b3" text-anchor="end" font-family="sans-serif">пробуждение</text>'
      '</svg>')
    return infofig('Что происходит за ночь', svg,
      'Глубокий сон идёт в первых циклах: тело чинит себя и укладывает память. К утру больше быстрого сна со снами, когда мозг разбирает эмоции.')

import math as _math
def fig_hormones():
    hs=[('Кортизол','режим тревоги','#e0603a'),('Тестостерон','смелость заявить','#d9992f'),
        ('Дофамин','топливо движения','#2f6bff'),('Серотонин','планка достатка','#25a06e'),
        ('Окситоцин','доверие и обмен','#7a4bd0'),('Глюкоза','ясность решений','#c74a86')]
    cx,cy,R=400,195,140; n=len(hs); nodes=''; lines=''
    for i,(name,role,col) in enumerate(hs):
        a=_math.radians(-90+i*360.0/n); x=cx+R*_math.cos(a); y=cy+R*_math.sin(a)
        lx=cx+(R+34)*_math.cos(a); ly=cy+(R+34)*_math.sin(a)
        anch='middle'; dyn=-6
        if _math.cos(a)>0.35: anch='start'
        elif _math.cos(a)<-0.35: anch='end'
        if _math.sin(a)>0.5: dyn=14
        lines+='<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="#e0e5f2" stroke-width="1.5"/>'%(cx,cy,x,y)
        nodes+='<circle cx="%.0f" cy="%.0f" r="15" fill="%s"/>'%(x,y,col)
        nodes+='<text x="%.0f" y="%.1f" font-size="14" font-weight="800" fill="#1a1f36" text-anchor="%s" font-family="sans-serif">%s</text>'%(lx,ly+dyn,anch,name)
        nodes+='<text x="%.0f" y="%.1f" font-size="12" fill="#7a80a0" text-anchor="%s" font-family="sans-serif">%s</text>'%(lx,ly+dyn+16,anch,role)
    svg=('<svg viewBox="0 0 800 400" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Шесть гормонов денежного решения">'
      +lines+'<circle cx="%d" cy="%d" r="58" fill="#0f1226"/>'%(cx,cy)
      +'<text x="%d" y="%d" font-size="14" font-weight="800" fill="#fff" text-anchor="middle" font-family="sans-serif">РЕШЕНИЕ</text>'%(cx,cy-4)
      +'<text x="%d" y="%d" font-size="12" fill="#aeb6da" text-anchor="middle" font-family="sans-serif">о деньгах</text>'%(cx,cy+15)
      +nodes+'</svg>')
    return infofig('Шесть гормонов, что решают за вас', svg,
      'Соотношение этих гормонов в крови решает, рискнёте вы или затаитесь, назовёте свою цену или промолчите. Химия тела идёт раньше логики.')

def _brain(ox,oy,s,col,nodes,links,op='1'):
    # мозг из двух полушарий + сеть узлов; s масштаб
    g=('<g transform="translate(%.0f,%.0f) scale(%.2f)" opacity="%s">'%(ox,oy,s,op)
      +'<g stroke="%s" stroke-width="2" fill="none" stroke-linejoin="round" stroke-linecap="round">'%col
      +'<path d="M24 6c-4-3-11-2-12 4-5 1-7 7-3 11-3 4-1 11 4 12 1 4 5 6 9 4"/>'
      +'<path d="M24 6c4-3 11-2 12 4 5 1 7 7 3 11 3 4 1 11-4 12-1 4-5 6-9 4"/>'
      +'<path d="M24 8v33" opacity=".5"/></g>')
    for x,y in nodes: g+='<circle cx="%d" cy="%d" r="2.6" fill="%s"/>'%(x,y,col)
    for a,b in links: g+='<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.2" opacity=".7"/>'%(nodes[a][0],nodes[a][1],nodes[b][0],nodes[b][1],col)
    return g+'</g>'

def fig_dmn():
    noisy=[(16,16),(30,12),(34,24),(20,26),(28,30),(15,32),(33,34),(24,20),(22,38)]
    nl=[(0,3),(0,7),(1,2),(1,7),(2,6),(3,4),(4,8),(5,8),(6,4),(7,3)]
    calm=[(20,20),(28,22),(24,32)]; cl=[(0,2),(1,2)]
    svg=('<svg viewBox="0 0 760 320" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Сеть пассивного режима: шум и тишина">'
      +'<text x="190" y="34" font-size="15" font-weight="800" fill="#c0492a" text-anchor="middle" font-family="sans-serif">ШУМ УМА</text>'
      +_brain(110,70,4.0,'#e0603a',noisy,nl)
      +'<text x="190" y="300" font-size="13" fill="#5a6080" text-anchor="middle" font-family="sans-serif">сеть гоняет мысли по кругу</text>'
      +'<line x1="380" y1="70" x2="380" y2="250" stroke="#e6eaf4" stroke-width="1.5" stroke-dasharray="4 6"/>'
      +'<text x="570" y="34" font-size="15" font-weight="800" fill="#2f6bff" text-anchor="middle" font-family="sans-serif">ТИШИНА</text>'
      +_brain(490,70,4.0,'#2f6bff',calm,cl)
      +'<text x="570" y="300" font-size="13" fill="#5a6080" text-anchor="middle" font-family="sans-serif">внимание тренировано, фон затих</text>'
      +'</svg>')
    return infofig('Сеть пассивного режима', svg,
      'Когда ты не занят делом, включается сеть пассивного режима и гоняет мысли о себе, прошлом и будущем. У тех, кто тренирует внимание, она затихает, и в голове становится тише.')

def fig_vagus():
    svg=('<svg viewBox="0 0 760 340" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Блуждающий нерв как переключатель режимов">'
      +'<defs><linearGradient id="vg" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#7a4bd0"/><stop offset="1" stop-color="#2f6bff"/></linearGradient></defs>'
      # мозг сверху
      +_brain(150,30,3.0,'#2f6bff',[(24,18)],[])
      +'<text x="186" y="26" font-size="12.5" fill="#5a6080" font-family="sans-serif">мозг</text>'
      # нерв вниз к органам
      +'<path d="M186,140 C186,180 150,190 160,230 C168,262 150,278 186,300" stroke="url(#vg)" stroke-width="4" stroke-linecap="round"/>'
      +'<text x="196" y="215" font-size="12.5" fill="#7a4bd0" font-weight="700" font-family="sans-serif" transform="rotate(0)">блуждающий нерв</text>'
      # органы
      +'<circle cx="150" cy="190" r="8" fill="#e0603a"/><text x="132" y="194" font-size="12.5" fill="#5a6080" text-anchor="end" font-family="sans-serif">сердце</text>'
      +'<circle cx="160" cy="235" r="8" fill="#25a06e"/><text x="140" y="239" font-size="12.5" fill="#5a6080" text-anchor="end" font-family="sans-serif">дыхание</text>'
      +'<circle cx="186" cy="300" r="8" fill="#d9992f"/><text x="200" y="304" font-size="12.5" fill="#5a6080" font-family="sans-serif">живот</text>'
      # две карточки-режима справа
      +'<rect x="420" y="60" width="300" height="90" rx="16" fill="#fbeeea" stroke="#f0c8bd"/>'
      +'<text x="444" y="96" font-size="15" font-weight="800" fill="#c0492a" font-family="sans-serif">Режим борьбы</text>'
      +'<text x="444" y="122" font-size="13" fill="#8a6a62" font-family="sans-serif">рваное дыхание, зажатость, тревога</text>'
      +'<rect x="420" y="190" width="300" height="90" rx="16" fill="#e8f0fb" stroke="#c5d7f2"/>'
      +'<text x="444" y="226" font-size="15" font-weight="800" fill="#2456c7" font-family="sans-serif">Режим покоя</text>'
      +'<text x="444" y="252" font-size="13" fill="#5a6a8a" font-family="sans-serif">ровный выдох, тепло, восстановление</text>'
      +'<path d="M300,175 C360,175 370,150 418,120" stroke="#e0603a" stroke-width="2" stroke-dasharray="4 5" opacity=".6"/>'
      +'<path d="M300,235 C360,235 372,250 418,235" stroke="#2f6bff" stroke-width="2.5"/>'
      +'</svg>')
    return infofig('Блуждающий нерв: переключатель тела', svg,
      'Он тянется от мозга к сердцу, лёгким и животу и решает, в каком режиме тело: борьба и тревога или покой и восстановление. Длинный выдох и мягкие практики поворачивают его к покою.')

def fig_mechanism():
    IC={'body':'<svg viewBox="0 0 24 24" fill="none"><path d="M3 9c3-2 6-2 9 0s6 2 9 0M4 14c2.7-1.7 5.3-1.7 8 0s5.3 1.7 8 0" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
        'focus':'<svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="8.2" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="3" fill="currentColor"/></svg>',
        'words':'<svg viewBox="0 0 24 24" fill="none"><path d="M4 6h16v10.5H9L5.5 20v-3.5H4z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M8 10h8M8 13h5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
        'calm':'<svg viewBox="0 0 24 24" fill="none"><path d="M20 13.5A8 8 0 1 1 10.5 4 6.5 6.5 0 0 0 20 13.5Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
        'clarity':'<svg viewBox="0 0 24 24" fill="none"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 1 4 10.5c-.7.6-1 1.2-1 2h-6c0-.8-.3-1.4-1-2A6 6 0 0 1 12 3Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>',
        'wealth':'<svg viewBox="0 0 24 24" fill="none"><path d="M4 20V11m5 9V6m5 14v-9m5 9V4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>'}
    def lev(ic,n,r): return '<div class="mnode"><span class="mi">%s</span><span class="mt"><b>%s</b><span>%s</span></span></div>'%(IC[ic],n,r)
    ins=lev('body','Тело','дыхание, осанка')+lev('focus','Фокус','куда идёт внимание')+lev('words','Слова','внутренняя речь')
    outs=lev('calm','Покой','в голове тихо')+lev('clarity','Ясность','видно решение')+lev('wealth','Достаток','поднимается норма')
    return ('<section class="mech"><div class="wrap">'
      '<div class="sec-h center"><span class="eyebrow">Как это устроено</span>'
      '<h2>Состояние решает, остальное подтягивается</h2>'
      '<p>Три рычага меняют состояние за секунды. А уже из состояния собирается покой, ясность и достаток.</p></div>'
      '<div class="mflow">'
      '<div class="mcol in">'+ins+'</div>'
      '<div class="marrow"></div>'
      '<div class="morb"><span class="orb-glow"></span><b>СОСТОЯНИЕ</b><span>первично</span></div>'
      '<div class="marrow"></div>'
      '<div class="mcol out">'+outs+'</div>'
      '</div></div></section>')

ARTICLE_RELATED={}  # заполняется в pages.py: slug -> HTML блока «связанные материалы»
ARTICLE_FIGURE={}   # slug -> HTML своей инфографики (вставляется после лида)
def related_block(links):
    # links: [(href, kicker, title), ...]
    cards=''.join('<a class="relcard" href="%s"><span class="rk">%s</span><span class="rt">%s</span><span class="rl">Открыть →</span></a>'%(h,k,t) for h,k,t in links)
    return ('<section class="soft"><div class="wrap"><div class="sec-h"><span class="eyebrow">Дальше</span>'
            '<h2>Что почитать и попробовать</h2></div><div class="relgrid">%s</div></div></section>')%cards

def article_page(slug, cover, tag, readtime, title, lead, sections_html, related=''):
    related = ARTICLE_RELATED.get(slug,'') + related  # связанные материалы, затем финальный CTA
    figure = ARTICLE_FIGURE.get(slug,'')  # своя инфографика после лида
    hero=('<section class="phero"><div class="wrap"><div class="arthero"><img class="bg" src="%s" alt="">'
          '<div class="in"><div class="artmeta"><a href="blog.html" style="color:#c3caea">← Все статьи</a>'
          '<span class="tg">%s</span><span>%s</span></div><h1>%s</h1></div></div></div></section>' % (cover, tag, readtime, title))
    body=hero+'<section><div class="article"><p class="lead dropcap">%s</p>%s%s</div></section>%s' % (lead, figure, sections_html, related)
    art_schema=('{"@context":"https://schema.org","@type":"Article","headline":%s,"description":%s,'
      '"image":"%s%s","author":{"@type":"Organization","name":"Архитектура сознания"},'
      '"publisher":{"@type":"Organization","name":"Архитектура сознания","logo":{"@type":"ImageObject","url":"%sapple-touch-icon.png"}},'
      '"mainEntityOfPage":"%s%s.html"}') % (json.dumps(title,ensure_ascii=False), json.dumps(lead[:180],ensure_ascii=False), BASE, cover, BASE, BASE, slug)
    page(slug, title+' — Архитектура сознания', body, lead[:150], active='blog', ogimg=cover, schema=art_schema)

def bcard(slug, cover, tag, title, excerpt, readtime):
    return ('<a class="bcard" href="%s.html"><div class="cov"><img src="%s" alt=""><span class="tag">%s</span></div>'
            '<div class="bd"><h3>%s</h3><p>%s</p><div class="meta"><span>%s</span><span class="rd">Читать →</span></div></div></a>'
            % (slug, cover, tag, title, excerpt, readtime))

def tcard(q, name, tag='', w='b'):
    ini = name.strip().lstrip('@')[0].upper()
    tagh = '<span class="chip %s" style="align-self:flex-start;margin-bottom:14px">%s</span>' % ({'b':'brain','t':'body','m':'money'}[w], tag) if tag else ''
    return '<div class="tcard">%s<div class="stars">★★★★★</div><div class="q">«%s»</div><div class="who"><span class="av">%s</span>%s</div></div>' % (tagh, q, ini, name)

def afig(img, cap=''):
    caph = '<figcaption>%s</figcaption>' % cap if cap else ''
    return '<figure class="afig"><img src="%s" alt="" loading="lazy">%s</figure>' % (img, caph)

def artstats(items, hi=0, hic=''):
    return '<div class="artstats">' + statband(items, hi=hi, hic=hic) + '</div>'

def cta_band(h, p, btn, url):
    return '''<section><div class="wrap"><div class="ctaband"><h2>%s</h2><p>%s</p>
<a class="btn light bracket" href="%s" target="_blank" rel="noopener">%s</a></div></div></section>''' % (h,p,url,btn)
