# -*- coding: utf-8 -*-
from build import *

U='https://thebodymindcode.github.io/'
# продукты: (крыло, чип, имя, формат, цена, url)
P={
 'money17':('m','Деньги','Протокол денег','17 дней · платформа с кабинетом','от 3 500 ₽',U+'moneyaccess/'),
 'stop':('b','Мозг','Протокол остановки ума','28 дней · 16 минут в день','2 990 ₽',U+'protocol/'),
 'codemoney':('m','Деньги','Код денег','14 дней · 5 встреч · 19 техник','5 900 ₽',U+'themoneycode/'),
 'authority':('b','Мозг','Внутренний Авторитет','3 встречи по 120 минут','4 900 ₽',U+'authority/'),
 'biohim':('m','Деньги','Биохимия денег','Запись эфира + книга','1 990 ₽',U+'biohimmoney/'),
 'choice':('b','Мозг','Выбор','180 минут записи','1 490 ₽',U+'choice/'),
 'beyond':('t','Тело','За пределами заболеваний','120 минут записи','1 490 ₽',U+'Beyond/'),
 'beauty':('t','Тело','Красота без оправданий','90 минут записи','1 490 ₽',U+'beauty/'),
 'newyear':('b','Мозг','Код нового года','3 дня + фраза-код','3 990 ₽',U+'NewYearCode/'),
 'book':('m','Деньги','Механизмы сдвига','Книга, 144 страницы','690 ₽',U+'moneybook/'),
 'session':('b','Личное','Персональная сессия с Дарьей','60-90 минут, один на один','12 500 ₽',U+'session1/'),
}
def C(k): return card(*P[k])

# ============ ГЛАВНАЯ ============
home='''
<section class="hero"><div class="wrap"><div class="hero-card"><img class="bg" src="img/hero-1.jpg" alt="">
<div class="hero-in"><span class="hero-badge"><span class="dot"></span> Портал по осознанности</span>
<h1>Архитектура<br>сознания</h1>
<p class="sub">Знание о покое, теле и достатке, <span class="hl">проверенное наукой</span> и собранное в программы-маршруты.</p>
<div class="hero-cta"><a class="btn primary bracket" href="programs.html">Найти свою программу</a><a class="btn light bracket" href="#wings">С чего начать</a></div>
<div class="hero-trust"><div><b>2 500+</b><span>человек в программах</span></div><div><b>23 200</b><span>читателей канала</span></div><div><b>наука</b><span>за каждой техникой</span></div></div>
</div></div></div></section>

<section class="soft" id="wings"><div class="wrap"><div class="sec-h"><span class="eyebrow">Дом с тремя крыльями</span>
<h2>Заходи в то, которое болит</h2>
<p>Твоё сознание можно спроектировать, как дом. <span class="hl">Три крыла, один хозяин.</span> Выбирай, куда зайти.</p></div>
<div class="wings">
<a class="wing w1" href="mozg.html"><div class="ic">%s</div><h3>Мозг</h3><p>Покой, ясность, сон и решения. Как затихает внутренний шум.</p><div class="tags"><span>покой</span><span>сон</span><span>ясность</span><span>решения</span></div><span class="more">Войти в крыло →</span></a>
<a class="wing w2" href="telo.html"><div class="ic">%s</div><h3>Тело</h3><p>Здоровье, психосоматика, красота. Как тело слышит мысли.</p><div class="tags"><span>здоровье</span><span>психосоматика</span><span>красота</span></div><span class="more">Войти в крыло →</span></a>
<a class="wing w3" href="dengi.html"><div class="ic">%s</div><h3>Деньги</h3><p>Потолок дохода и биохимия решений. Где достаток начинается внутри.</p><div class="tags"><span>потолок</span><span>биохимия</span><span>достаток</span></div><span class="more">Войти в крыло →</span></a>
</div>
<div class="pains"><a href="mozg.html">Гонка в голове</a><a href="mozg.html">Не сплю</a><a href="mozg.html">Тревога</a><a href="telo.html">Тело подводит</a><a href="dengi.html">Потолок в деньгах</a><a href="programs.html">Всё понимаю, ничего не меняю</a></div>
</div></section>

<section id="why"><div class="wrap"><div class="why">
<div class="why-media"><img src="img/sci-c.jpg" alt=""><span class="cap"><span class="d"></span> За каждой техникой данные</span></div>
<div><span class="eyebrow">Проверено наукой</span>
<h2 class="disp" style="font-size:clamp(26px,3.4vw,42px);margin:14px 0 4px">За каждой техникой стоит <span class="hl">исследование</span></h2>
<p class="mut" style="font-size:17px;margin:14px 0 0;max-width:48ch">То, что веками знали мудрецы, сегодня видно на приборах. Мы берём то, что проверено, и собираем в понятные шаги.</p>
<ul class="thm-list">
%s%s%s%s
</ul>
<a class="btn ghost bracket" style="margin-top:26px" href="nauka.html">Раздел «Наука»</a>
</div></div></div></section>

<section class="soft"><div class="wrap"><div class="sec-h"><span class="eyebrow">Флагманы</span>
<h2>Программы как маршрут по дням</h2>
<p>Ты идёшь маршрутом, день за днём, в своём темпе, и видишь <span class="hl">прогресс в личном кабинете</span>.</p></div>
<div class="flag">
<div class="fcard"><img class="bg" src="img/money-1.jpg" alt=""><div class="fin"><span class="kick">17 дней · платформа с кабинетом</span><h3>Протокол денег</h3><p>Перенастройка денежной программы. Каждый день открывается по расписанию, с аудио и заданиями.</p><a class="btn light bracket" href="%smoneyaccess/" target="_blank" rel="noopener">Смотреть программу</a></div></div>
<div class="fcard"><img class="bg" src="img/stopum-1.jpg" alt=""><div class="fin"><span class="kick">28 дней · 16 минут в день</span><h3>Протокол остановки ума</h3><p>Голова перестаёт гудеть, внутренний диалог затихает. Маршрут на четыре недели.</p><a class="btn light bracket" href="%sprotocol/" target="_blank" rel="noopener">Смотреть программу</a></div></div>
</div></div></section>

<section id="catalog"><div class="wrap"><div class="sec-h"><span class="eyebrow">Каталог</span>
<h2>Все программы бренда</h2><p>Записи, книги и длинные программы. Выбирай по крылу и по формату.</p></div>
<div class="pgrid">%s%s%s%s%s%s</div>
<div class="catf"><a class="btn ghost bracket" href="programs.html">Смотреть все программы</a></div></div></section>

<section class="soft" id="books"><div class="wrap"><div class="sec-h"><span class="eyebrow m">Книги</span>
<h2>Знание, которое остаётся с тобой</h2>
<p>Две книги бренда: <span class="hl m">глубоко и по делу</span>. Читаешь в своём темпе и возвращаешься к главному.</p></div>
<div class="b2grid">
<div class="bk"><div class="cv gold"><span class="kb">Книга бренда</span><h4>Механизмы сдвига</h4><span class="bm2">144 стр · 20 глав</span></div>
<div class="bi"><h3>Механизмы сдвига</h3><p>Шесть гормональных механизмов денег, четыре финансовых архетипа, протокол сдвига и дневник на 30 дней.</p>
<div class="row"><span class="price">690 ₽</span><a class="btn primary bracket" href="%smoneybook/" target="_blank" rel="noopener">Открыть книгу</a></div></div></div>
<div class="bk"><div class="cv teal"><span class="kb">Книга бренда</span><h4>Тело говорит первым</h4><span class="bm2">40 стр · 30 сигналов</span></div>
<div class="bi"><h3>Тело говорит первым</h3><p>30 сигналов тела и 50+ анализов: как услышать организм раньше, чем он перейдёт на крик.</p>
<div class="row"><span class="tagf">в комплекте программы</span><a class="btn ghost bracket" href="%sBeyond/" target="_blank" rel="noopener">Смотреть программу</a></div></div></div>
</div></div></section>

<section id="cabinet"><div class="wrap"><div class="cab"><span class="eyebrow">Личный кабинет</span>
<h2>Одна почта. Все твои программы</h2>
<p>Входишь по почте и видишь всё, что купил: курсы, прогресс по дням, аудио и практики. Каждая новая программа появляется здесь же.</p>
<a class="btn light bracket" href="kontakty.html">Войти в кабинет</a>
<div class="cabf"><div>Мои курсы</div><div>Прогресс по дням</div><div>Аудио и практики</div><div>Доступ навсегда</div></div>
</div></div></section>
''' % (wing_ic('b',30),wing_ic('t',30),wing_ic('m',30),
       bullet('<b>Мозг перестраивается</b> в любом возрасте, вопрос метода. Нейропластичность работает всю жизнь.','brain'),
       bullet('<b>47% времени</b> ум занят не тем, что происходит, и там прячется тревога. Гарвард, Science.','clock'),
       bullet('<b>Гиппокамп растёт</b> от практики. У лондонских таксистов серое вещество прибавило в объёме.','grow'),
       bullet('<b>Внутренний шум затихает</b> у тех, кто тренирует внимание. Сеть пассивного режима успокаивается.','waves'),
       U,U, C('biohim'),C('beyond'),C('authority'),C('beauty'),C('choice'),C('codemoney'), U, U)
page('index','АРХИТЕКТУРА СОЗНАНИЯ — портал','\n'+home,'Портал по осознанности: знание о покое, теле и достатке, проверенное наукой и собранное в программы. Один вход, все курсы в одном месте.')

# ============ КРЫЛО: шаблон ============
def wing_page(slug,img,ew,title,lead,intro,states,progs,bullets,cls):
    st=''
    for ic,h,p in states:
        st+='<div class="wing %s"><div class="ic">%s</div><h3>%s</h3><p>%s</p></div>' % (cls,ic,h,p)
    bl=''.join(bullet(b) for b in bullets)
    body='''
%s
<section><div class="wrap"><div class="prose"><p class="lead">%s</p><p>%s</p></div></div></section>
<section class="soft"><div class="wrap"><div class="sec-h"><span class="eyebrow %s">Что внутри крыла</span><h2>С чем работаем</h2></div>
<div class="wings">%s</div></div></section>
<section><div class="wrap"><div class="sec-h"><span class="eyebrow %s">Программы крыла</span><h2>С чего начать</h2><p>Выбирай формат: короткая запись или длинный маршрут с кабинетом.</p></div>
<div class="pgrid">%s</div></div></section>
<section class="soft"><div class="wrap"><div class="why"><div class="why-media"><img src="img/sci-a.jpg" alt=""><span class="cap"><span class="d"></span> Проверенный механизм</span></div>
<div><span class="eyebrow %s">Проверено наукой</span><h2 class="disp" style="font-size:clamp(24px,3vw,38px);margin:14px 0 6px">Почему это работает</h2>
<ul class="thm-list %s">%s</ul></div></div></div></section>
%s
''' % (phero(img,ew,title,lead,title), lead, intro,
       {'w1':'','w2':'t','w3':'m'}.get(cls,''), st,
       {'w1':'','w2':'t','w3':'m'}.get(cls,''), progs,
       {'w1':'','w2':'t','w3':'m'}.get(cls,''), {'w1':'','w2':'t','w3':'m'}.get(cls,''), bl,
       cta_band('Найди свою программу в этом крыле','Один вход по почте, и весь маршрут на платформе, с прогрессом и практиками.','Смотреть все программы',U+'shop/'))
    page(slug,title+' — Архитектура сознания',body,lead,active=slug)

wing_page('mozg','img/hero-1.jpg','Крыло портала','Мозг',
  'Покой, ясность, сон и решения. Как затихает внутренний шум и возвращается тишина.',
  'Большую часть дня ум занят не тем, что происходит рядом. Он крутит прошлое и будущее, и там копится усталость. Это крыло про то, как вернуть внимание себе: тише голова, яснее решения, глубже сон.',
  [(wing_ic('b',30),'Покой','Как гаснет тревожная болтовня и появляется тишина внутри.'),
   (wing_ic('b',30),'Сон','Сон это мастерская: ночью мозг достраивает связи, которые ты задал днём.'),
   (wing_ic('b',30),'Ясность','Внимание как мышца: замечаешь, что ум уплыл, и мягко возвращаешь.'),
   (wing_ic('b',30),'Решения','95% решений идут из подсознания. Учимся видеть их до того, как они случились.')],
  C('stop')+C('choice')+C('authority')+C('newyear'),
  ['<b>Нейропластичность</b> работает всю жизнь, мозг меняется под опытом и вниманием.',
   '<b>47% времени</b> человек думает не о текущем деле, и именно там ему хуже. Гарвард, Science.',
   '<b>Сеть пассивного режима</b> затихает у тех, кто тренирует внимание. Внутренней болтовни меньше.'],'w1')

wing_page('telo','img/telo-1.jpg','Крыло портала','Тело',
  'Здоровье, психосоматика, красота. Как тело слышит мысли и отвечает на состояние.',
  'Тело не отдельно от головы. Оно слышит мысли, держит напряжение и хранит старые решения. Это крыло про то, как вернуть телу опору: меньше зажимов, больше энергии, спокойное отношение к себе.',
  [(wing_ic('t',30),'Здоровье','Связь состояния и тела: где напряжение превращается в симптом.'),
   (wing_ic('t',30),'Психосоматика','Скрытые выгоды и старые решения, которые тело держит за нас.'),
   (wing_ic('t',30),'Красота','Как отношение к себе меняет то, как ты выглядишь и держишься.')],
  C('beyond')+C('beauty'),
  ['<b>Тело слышит состояние</b>: хроническое напряжение меняет дыхание, сон и осанку.',
   '<b>Психосоматика</b> это сигнал тела: его можно услышать и мягко переписать.',
   '<b>Красота</b> держится на отношении к себе, уход идёт следом.'],'w2')

wing_page('dengi','img/dengi-1.jpg','Крыло портала','Деньги',
  'Потолок дохода и биохимия решений. Где достаток начинается внутри.',
  'Доход упирается во внутренний потолок: сколько человек считает своей нормой. Это крыло про то, как увидеть этот потолок и сдвинуть его через решения, состояние и биохимию. Тайм-менеджмент тут ни при чём.',
  [(wing_ic('m',30),'Потолок','Внутренняя норма достатка, к которой всё время возвращается доход.'),
   (wing_ic('m',30),'Биохимия','Шесть механизмов, которые решают за нас до того, как мы подумали.'),
   (wing_ic('m',30),'Достаток','Как состояние и решения поднимают уровень жизни, а цифры идут следом.')],
  C('money17')+C('codemoney')+C('biohim')+C('book'),
  ['<b>Внутренний потолок</b> держит доход на месте, пока не сдвинется норма.',
   '<b>Биохимия решений</b>: состояние влияет на выбор раньше, чем включается разум.',
   '<b>Достаток начинается внутри</b>: сначала меняется норма, потом реальность.'],'w3')

# ============ ПРОГРАММЫ ============
allcards=''.join(C(k) for k in ['money17','stop','biohim','beyond','authority','beauty','session','choice','newyear','codemoney','book'])
prog='''
%s
<section><div class="wrap"><div class="sec-h"><span class="eyebrow">Каталог</span><h2>Все программы и записи</h2>
<p>Одиннадцать продуктов: короткие записи, книга, длинные маршруты и личная работа. Фильтруй по крылу.</p></div>
<div class="filterbar"><button class="on" data-f="all">Все</button><button data-f="b">Мозг</button><button data-f="t">Тело</button><button data-f="m">Деньги</button></div>
<div class="pgrid" id="pg">%s</div></div></section>
<script>document.querySelectorAll('.filterbar button').forEach(function(b){b.onclick=function(){document.querySelectorAll('.filterbar button').forEach(function(x){x.classList.remove('on')});b.classList.add('on');var f=b.dataset.f;document.querySelectorAll('#pg .card').forEach(function(c){c.style.display=(f==='all'||c.classList.contains(f))?'':'none'})}});</script>
''' % (phero('img/hero-1.jpg','Портал','Программы','Всё, что собрано в портале: записи, книга, длинные маршруты и личная сессия. Выбирай по крылу и формату.','Программы'), allcards)
page('programs','Программы — Архитектура сознания',prog,'Каталог всех программ портала: мозг, тело, деньги. Записи, книга, длинные маршруты, личная сессия.',active='programs')

# ============ КНИГИ ============
books='''
%s
<section><div class="wrap"><div class="sec-h"><span class="eyebrow m">Библиотека</span><h2>Две книги бренда</h2>
<p>Каждая написана по нашим программам: живой опыт Дарьи, проверка Алексея, механизм и практика внутри.</p></div>
<div class="b2grid">
<div class="bk"><div class="cv gold"><span class="kb">Книга бренда</span><h4>Механизмы сдвига</h4><span class="bm2">144 стр · 20 глав</span></div>
<div class="bi"><h3>Механизмы сдвига</h3><p>Шесть гормональных механизмов денег, четыре финансовых архетипа, протокол сдвига и дневник наблюдений на 30 дней. Самая мягкая точка входа в тему биохимии денег.</p>
<div class="row"><span class="price">690 ₽</span><a class="btn primary bracket" href="%smoneybook/" target="_blank" rel="noopener">Открыть книгу</a></div></div></div>
<div class="bk"><div class="cv teal"><span class="kb">Книга бренда</span><h4>Тело говорит первым</h4><span class="bm2">40 стр · 30 сигналов</span></div>
<div class="bi"><h3>Тело говорит первым</h3><p>30 сигналов тела и 50+ анализов: как услышать организм раньше, чем он перейдёт на крик. Плюс модуль про блуждающий нерв: как тело выходит из режима борьбы.</p>
<div class="row"><span class="tagf">в комплекте программы</span><a class="btn ghost bracket" href="%sBeyond/" target="_blank" rel="noopener">Смотреть программу</a></div></div></div>
</div></div></section>
<section class="soft"><div class="wrap"><div class="sec-h center"><span class="eyebrow">Почему книги</span><h2>Опора, к которой возвращаешься</h2>
<p style="margin-left:auto;margin-right:auto">Библиотека портала растёт: новые книги появятся здесь же.</p></div>
<div class="prose center" style="margin:0 auto"><ul class="thm-list m" style="display:inline-block;text-align:left">%s%s%s</ul></div>
<div class="catf"><a class="btn ghost bracket" href="%sshop/" target="_blank" rel="noopener">Все продукты в магазине</a></div>
</div></section>
''' % (phero('img/books-1.jpg','Портал','Книги','Книги бренда: глубоко и по делу. Читаешь в своём темпе и возвращаешься к главному.','Книги'),
       U, U,
       bullet('<b>Глубже поста</b>: то, что в ленте мелькает, здесь разложено по полкам.','book'),
       bullet('<b>В своём темпе</b>: возвращаешься к главам, когда нужно.','clock'),
       bullet('<b>С практикой</b>: внутри дневник и протокол на 30 дней.','grow'), U)
page('knigi','Книги — Архитектура сознания',books,'Книги бренда «Архитектура сознания»: Механизмы сдвига и растущая библиотека.',active='knigi')

# ============ НАУКА ============
nauka='''
%s
<section><div class="wrap"><div class="prose"><p class="lead">То, что веками знали мудрецы, сегодня видно на приборах. Мы берём то, что проверено, и собираем в понятные шаги. Здесь коротко о том, на чём стоят программы.</p></div>
<div class="stats" style="margin-top:20px">
<div class="stat"><b>47%%</b><span>времени ум занят не текущим делом. Гарвард, Science, 2010</span></div>
<div class="stat"><b>18%%</b><span>на столько уменьшается миндалина за 4 недели практики. МРТ</span></div>
<div class="stat"><b>25-30%%</b><span>снижение кортизола в исследованиях спокойных состояний</span></div>
<div class="stat"><b>всю жизнь</b><span>работает нейропластичность, мозг меняется под опытом</span></div>
</div></div></section>
<section class="soft"><div class="wrap"><div class="why"><div class="why-media"><img src="img/nauka-1.jpg" alt=""><span class="cap"><span class="d"></span> Данные и связи</span></div>
<div><span class="eyebrow">Как мы проверяем</span><h2 class="disp" style="font-size:clamp(24px,3vw,38px);margin:14px 0 6px">Факт, источник, механизм</h2>
<ul class="thm-list">%s%s%s%s</ul></div></div></div></section>
<section><div class="wrap"><div class="prose"><h3>Источники</h3>
<p class="mut">Killingsworth &amp; Gilbert, «A Wandering Mind Is an Unhappy Mind», Science, 2010. Maguire, гиппокамп лондонских таксистов, UCL. Brewer et al., медитация и сеть пассивного режима, PNAS, 2011. Обзоры по нейропластичности, Huberman Lab.</p></div></div></section>
%s
''' % (phero('img/nauka-1.jpg','Портал','Наука','Доказательная опора портала: за каждой техникой стоит исследование. Факт, источник, механизм.','Наука'),
       bullet('<b>Внимание меняет мозг.</b> На что регулярно смотришь, тем и становятся связи.'),
       bullet('<b>Практика растит ткань.</b> У таксистов вырос задний гиппокамп от нагрузки на память.'),
       bullet('<b>Тишина тренируется.</b> Возврат внимания успокаивает сеть, которая гоняет тревогу.'),
       bullet('<b>Сон достраивает.</b> Днём задаёшь направление, ночью мозг перепаивает связи.'),
       cta_band('Готов проверить на себе','Программы собраны из того, что проверено. Начни с крыла, которое ближе.','Смотреть программы',U+'shop/'))
page('nauka','Наука — Архитектура сознания',nauka,'Доказательная база портала: исследования, цифры и механизмы за каждой техникой.',active='nauka')


SD = soc('Instagram','https://instagram.com/daryarostovtseva')+soc('Threads','https://www.threads.com/@daryarostovtseva')+soc('Telegram','https://t.me/+bo3a92A06cQ3NWMy')
SA = soc('Instagram','https://instagram.com/thebodymindcode')+soc('YouTube','https://www.youtube.com/@thebodymindcode')+soc('TikTok','https://www.tiktok.com/@thebodymindcode')
SA2 = SA + soc('Telegram','https://t.me/+aEgupwOOOq84YTNi')

# ============ О НАС ============
onas='''
%s
<section><div class="wrap"><div class="prose">
<p class="lead">За «Архитектурой сознания» стоят два живых человека. Дарья находит технику в живой практике. Алексей сверяет её с исследованиями: механизм, источник, цифры. В программы попадает то, что прошло обе проверки.</p>
<p>Шесть лет назад мы оказались в одном поле. Одни вопросы, одна одержимость: как на самом деле устроены мозг, тело, сознание. С тех пор идём вместе. Дарья чувствует и находит: инсайт, технику, живой ключ. Алексей видит структуру и проверяет: исследование, механизм, цифры. Она летит, он приземляет.</p>
<p>Каждая техника проходит два фильтра: живой опыт и проверку наукой. То, что проходит, попадает в программы и работает у сотен людей. То, что нет, остаётся за бортом.</p>
</div></div></section>
<section class="soft"><div class="wrap"><div class="sec-h"><span class="eyebrow">Дуэт</span><h2>Двое за каждой программой</h2></div>
<div class="duo">
<div class="person"><div class="pav" style="background:linear-gradient(145deg,#2f6bff,#221a5e)">Д</div><h3>Дарья Ростовцева</h3><div class="role">Инсайт, техники, эфиры</div><p>Ведёт эфиры и программы, создаёт техники, работает с людьми один на один. Чувствует, где болит, и находит ключ.</p><div class="socs">%s</div></div>
<div class="person d"><div class="pav">А</div><h3>Алексей</h3><div class="role">Структура, наука, проверка</div><p>Находит исследования, проверяет каждый факт и цифру, приземляет технику в понятный механизм. Пока за кадром, но в каждой детали.</p><div class="socs">%s</div></div>
</div>
<div class="stats" style="margin-top:22px">
<div class="stat"><b>2 500+</b><span>человек в программах</span></div>
<div class="stat"><b>23 200</b><span>читателей канала</span></div>
<div class="stat"><b>6 лет</b><span>вместе копаем одну тему</span></div>
<div class="stat"><b>2</b><span>живых человека за каждой программой</span></div>
</div></div></section>
%s
''' % (phero('img/about-1.jpg','О проекте','Два человека, одна одержимость','Дарья приносит технику из живой практики, Алексей сверяет её с исследованиями. В программы попадает то, что прошло обе проверки.','О нас'),
       SD, SA,
       cta_band('Познакомься ближе','Мы ведём каналы и делимся тем, что находим и проверяем. Заходи.','Каналы и контакты','kontakty.html'))
onas=onas.replace('rel="noopener">Каналы и контакты</a></div></div></section>','rel="noopener">Каналы и контакты</a></div></div></section>').replace('target="_blank" rel="noopener">Каналы и контакты</a>','>Каналы и контакты</a>')
page('o-nas','О нас — Архитектура сознания',onas,'За «Архитектурой сознания» два человека: Дарья находит инсайт, Алексей проверяет наукой.',active='o-nas')

# ============ КОНТАКТЫ ============
kont='''
%s
<section><div class="wrap"><div class="sec-h"><span class="eyebrow">Ресурсы</span><h2>Где мы есть</h2><p>Каналы, соцсети и поддержка. Заходи, куда удобнее.</p></div>
<div class="hub">
<div class="hcard"><h3>Дарья Ростовцева</h3><div class="role">Инсайт, техники, эфиры</div><div class="socs">%s</div></div>
<div class="hcard"><h3>Алексей</h3><div class="role">Структура, наука, проверка</div><div class="socs">%s</div></div>
</div>
<div class="cab" style="margin-top:22px"><span class="eyebrow">Поддержка</span><h2>Нужна помощь или доступ</h2><p>Напиши в поддержку, поможем с доступом к программам и ответим на вопросы.</p><a class="btn light bracket" href="https://t.me/TheBodyMindCode_support" target="_blank" rel="noopener">Написать в поддержку</a></div>
</div></section>
''' % (phero('img/hero-1.jpg','Связь','Контакты','Каналы, соцсети и поддержка портала «Архитектура сознания».','Контакты'), SD, SA2)
page('kontakty','Контакты — Архитектура сознания',kont,'Каналы, соцсети и поддержка портала «Архитектура сознания».',active='')

# ============ FAQ ============
faqitems=[
 ('Насколько это подтверждено наукой','За каждой техникой стоит исследование: фМРТ, объём серого вещества, конкретные проценты. В разделе «Наука» собраны факты и источники.'),
 ('Сколько времени нужно в день','У программ разный формат. Флагман «Протокол остановки ума» это 16 минут в день на 28 дней. Записи смотришь в своём темпе.'),
 ('Чем портал отличается от отдельных курсов','Здесь всё в одном месте. Один вход по почте, и все твои программы, прогресс и практики рядом. Не нужно искать по ссылкам и письмам.'),
 ('Доступ остаётся навсегда','Да, купленные материалы остаются у тебя в кабинете. Возвращаешься к ним когда захочешь.'),
 ('С чего начать','Пройди в крыло, которое ближе: Мозг, Тело или Деньги. Там подобраны программы под состояние. Или напиши в поддержку, подскажем.'),
]
fq=''.join('<details%s><summary>%s<span></span></summary><p>%s</p></details>' % (' open' if i==0 else '',q,a) for i,(q,a) in enumerate(faqitems))
faq='''
%s
<section><div class="wrap"><div class="faq">%s</div></div></section>
%s
''' % (phero('img/hero-1.jpg','Помощь','Вопросы и ответы','Коротко о главном: как устроен портал, сколько нужно времени и с чего начать.','FAQ'), fq,
       cta_band('Не нашёл ответ','Напиши в поддержку, ответим и поможем с доступом.','Написать в поддержку','https://t.me/TheBodyMindCode_support'))
page('faq','Вопросы и ответы — Архитектура сознания',faq,'Частые вопросы о портале «Архитектура сознания».',active='')

print('ALL PAGES BUILT')
