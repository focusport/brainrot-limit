(function () {
'use strict';
document.documentElement.classList.add('js');
var $ = function (s, r) { return (r || document).querySelector(s); };
var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
var header = $('.site-header');
var btn = $('#menuBtn');
var drawer = $('#drawer');
function onScroll() { if (header) header.classList.toggle('scrolled', window.scrollY > 8); }
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();
if (btn && drawer) {
btn.addEventListener('click', function () {
var open = drawer.classList.toggle('open');
btn.setAttribute('aria-expanded', open ? 'true' : 'false');
});
$$('a', drawer).forEach(function (a) {
a.addEventListener('click', function () { drawer.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); });
});
}
var root = document.documentElement, tb = $('#themeBtn');
var setTheme = function (t, save) {
root.classList.add('theme-anim'); root.setAttribute('data-theme', t);
if (tb) { tb.setAttribute('aria-label', 'Switch to ' + (t === 'dark' ? 'light' : 'dark') + ' theme'); tb.setAttribute('aria-pressed', t === 'dark'); }
if (save) { try { localStorage.setItem('theme', t); } catch (e) {} }
setTimeout(function () { root.classList.remove('theme-anim'); }, 600);
};
if (tb) {
tb.setAttribute('aria-label', 'Switch to ' + (root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark') + ' theme');
tb.addEventListener('click', function () { setTheme(root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark', true); });
}
try { window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function (m) { if (!localStorage.getItem('theme')) setTheme(m.matches ? 'dark' : 'light'); }); } catch (e) {}
var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
var lastY = window.scrollY;
window.addEventListener('scroll', function () {
var y = window.scrollY;
if (header && !(drawer && drawer.classList.contains('open'))) header.classList.toggle('hide', y > lastY && y > 320);
lastY = y;
}, { passive: true });
$$('.feat-grid, .cards, .steps, .shots, .statement-meta, .calc-stats, .faq-list, .carousel, .hero-facts, .dl').forEach(function (g) {
g.classList.add('stagger');
Array.prototype.forEach.call(g.children, function (c, i) { c.style.setProperty('--i', Math.min(i, 8)); });
});
$$('.section-head, .article-cta, .table-wrap, .sim, .demo').forEach(function (el) { el.classList.add('reveal'); });
var reveals = $$('.reveal, .stagger');
if ('IntersectionObserver' in window && reveals.length && !reduce) {
var io = new IntersectionObserver(function (entries) {
entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
}, { threshold: 0.12, rootMargin: '0px 0px -50px 0px' });
reveals.forEach(function (el) { io.observe(el); });
} else {
reveals.forEach(function (el) { el.classList.add('in'); });
}
var par = $$('[data-parallax]');
if (par.length && !reduce) {
var tick = false;
var run = function () {
var y = window.scrollY;
par.forEach(function (el) { el.style.translate = '0 ' + (-y * parseFloat(el.dataset.parallax)).toFixed(1) + 'px'; });
tick = false;
};
window.addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(run); } }, { passive: true });
}
if (!reduce && window.matchMedia('(hover: hover)').matches) {
$$('.split-media img, .shot img, .page-head-grid img').forEach(function (el) {
el.classList.add('tilt');
el.addEventListener('pointermove', function (e) {
var r = el.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
el.style.transform = 'perspective(900px) rotateY(' + (x * 9).toFixed(2) + 'deg) rotateX(' + (-y * 9).toFixed(2) + 'deg) scale(1.02)';
});
el.addEventListener('pointerleave', function () { el.style.transform = ''; });
});
}
var STAGES = [
{ t: 0,    name: 'Fresh',             sub: 'Sharp and ready to focus',  q: 'Zero videos. Attention is intact and starting a hard task takes no extra effort.' },
{ t: 50,   name: 'Still fine',        sub: 'A little tired',            q: 'A light session. Most people can still put the phone down without noticing a pull.' },
{ t: 100,  name: 'Getting tired',     sub: 'Losing alertness',          q: 'Switching back to reading or writing starts to feel like friction.' },
{ t: 250,  name: 'Losing focus',      sub: 'Mind drifting',             q: 'Attention gets choppy. Slower, harder tasks start to feel boring next to a feed that never stops.' },
{ t: 400,  name: 'Mentally drained',  sub: 'Attention depleted',        q: 'Heavy use. Many people report foggy thinking and a harder time holding ideas in mind.' },
{ t: 500,  name: 'Focus fading',      sub: 'Overstimulated',            q: 'Studying or deep work feels flat. The urge to check the phone arrives every few minutes.' },
{ t: 600,  name: 'Seriously affected', sub: 'Scrolling fatigue',        q: 'Phone checks turn automatic. Time is lost without anything to show for it.' },
{ t: 700,  name: 'Brain overloaded',  sub: 'Cognitive overload',        q: 'Procrastination loops and a flat, regretful feeling when the screen finally locks.' },
{ t: 800,  name: 'Almost broken',     sub: 'Excessive scroll',          q: 'Hours of the day are gone. This is the point a hard limit is meant to stop long before.' },
{ t: 900,  name: 'System failing',    sub: 'Severe overload',           q: 'Sleep, mood and motivation usually take a hit by now.' },
{ t: 1000, name: 'Completely fried',  sub: 'Limit destroyed',           q: 'A limit set at 50 would have ended this session about 950 videos ago.' }
];
var slider = $('#reelSlider');
if (slider) {
var img = $('#mascotImg'), badge = $('#stageBadge'), nameEl = $('#stageName'), subEl = $('#stageSub'),
quote = $('#stageQuote'), val = $('#reelVal'), chips = $$('.chip[data-val]'),
base = (img && img.getAttribute('data-base')) || 'assets/img/', last = -1;
var render = function (n) {
var s = STAGES[0];
for (var i = 0; i < STAGES.length; i++) if (n >= STAGES[i].t) s = STAGES[i];
val.textContent = n >= 1000 ? '1000+' : n;
badge.textContent = s.t + (s.t === 1000 ? '+' : '') + ' videos';
nameEl.textContent = s.name; subEl.textContent = s.sub; quote.textContent = s.q;
if (last !== s.t) {
img.src = base + 'mascot-' + s.t + '.webp';
img.alt = 'FocusPort brain mascot in the "' + s.name + '" state';
img.classList.add('bump'); setTimeout(function () { img.classList.remove('bump'); }, 220);
last = s.t;
}
chips.forEach(function (c) { c.classList.toggle('active', parseInt(c.dataset.val, 10) === s.t); });
slider.setAttribute('aria-valuetext', n + ' videos, ' + s.name);
};
slider.addEventListener('input', function () { render(parseInt(slider.value, 10)); });
chips.forEach(function (c) { c.addEventListener('click', function () { slider.value = c.dataset.val; render(parseInt(c.dataset.val, 10)); }); });
render(parseInt(slider.value, 10) || 0);
}
var calc = $('#calcMinutes');
if (calc) {
var out = { m: $('#calcVal'), h: $('#cHours'), d: $('#cDays'), b: $('#cBooks'), r: $('#cSaved') };
var fmt = function (n) { return n.toLocaleString('en-IN'); };
var run = function () {
var m = parseInt(calc.value, 10);
var hrs = Math.round(m * 365 / 60);
out.m.textContent = m >= 60 ? (Math.floor(m / 60) + 'h' + (m % 60 ? ' ' + (m % 60) + 'm' : '')) : m + ' min';
out.h.textContent = fmt(hrs) + ' hrs';
out.d.textContent = (hrs / 24).toFixed(1) + ' days';
out.b.textContent = fmt(Math.round(hrs / 7)) + ' books';
out.r.textContent = fmt(Math.round(hrs * 0.5)) + ' hrs';
calc.setAttribute('aria-valuetext', out.m.textContent + ' per day');
};
calc.addEventListener('input', run); run();
}
var faqList = $('#faqList');
if (faqList) {
var items = $$('details.faq', faqList), groups = $$('.faq-group', faqList),
search = $('#faqSearch'), empty = $('#faqEmpty'), pills = $$('.chip[data-cat]'), cat = 'all';
var filter = function () {
var q = (search ? search.value : '').toLowerCase().trim(), shown = 0;
items.forEach(function (it) {
var ok = (cat === 'all' || it.dataset.cat === cat) && (!q || it.textContent.toLowerCase().indexOf(q) > -1);
it.style.display = ok ? '' : 'none'; if (ok) shown++;
});
groups.forEach(function (g) {
var any = items.some(function (it) { return it.dataset.cat === g.dataset.cat && it.style.display !== 'none'; });
g.style.display = any ? '' : 'none';
});
if (empty) empty.style.display = shown ? 'none' : 'block';
};
if (search) search.addEventListener('input', filter);
pills.forEach(function (p) {
p.addEventListener('click', function () {
pills.forEach(function (x) { x.classList.remove('active'); }); p.classList.add('active');
cat = p.dataset.cat; filter();
});
});
if (location.hash) { var t = $(location.hash); if (t && t.tagName === 'DETAILS') t.open = true; }
}
var bar = $('#progress'), prose = $('#articleBody');
if (bar && prose) {
var heads = $$('h2[id]', prose), links = $$('.toc a');
var upd = function () {
var r = prose.getBoundingClientRect(), total = r.height - window.innerHeight * 0.6;
var p = Math.min(1, Math.max(0, (-r.top + 80) / Math.max(1, total)));
bar.style.width = (p * 100) + '%';
var cur = null;
heads.forEach(function (h) { if (h.getBoundingClientRect().top < 140) cur = h.id; });
links.forEach(function (a) { a.classList.toggle('on', a.getAttribute('href') === '#' + cur); });
};
window.addEventListener('scroll', upd, { passive: true }); upd();
}
var form = $('#contactForm');
if (form) {
form.addEventListener('submit', function (e) {
e.preventDefault();
var f = new FormData(form);
var subject = '[FocusPort] ' + (f.get('topic') || 'Message');
var body = (f.get('message') || '') + '\n\n— ' + (f.get('name') || '') + ' <' + (f.get('email') || '') + '>';
window.location.href = 'mailto:support@focusport.in?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
var ok = $('#formSuccess'); if (ok) ok.style.display = 'block';
});
}
var demo = $('#demo');
if (demo) {
var LIMIT = parseInt(demo.dataset.limit, 10) || 8, n = 0, locked = false;
var reel = $('#demoReel'), hud = $('#demoHud'), cnt = $('#demoCount'), bar = $('#demoBar'), over = $('#demoOver'),
face = $('#demoFace'), left = $('#demoLeft'), swipeBtn = $('#demoSwipe'), resetBtn = $('#demoReset'),
base = demo.dataset.base || 'assets/img/';
var PAL = ['linear-gradient(#2a1b5e,#c8478a 50%,#f59a5a)', 'linear-gradient(#0f3b4a,#1f8a8a 55%,#e8c26a)', 'linear-gradient(#3b1b2c,#d9544f 55%,#f6b66b)',
'linear-gradient(#10224a,#3c6ee0 55%,#9bd0ff)', 'linear-gradient(#27143f,#7a46c9 55%,#f08fc1)', 'linear-gradient(#112f27,#2f9c6b 55%,#d7e88a)',
'linear-gradient(#3a2210,#c9772b 55%,#ffd27a)', 'linear-gradient(#1a1a2e,#46467e 55%,#c0a3ff)', 'linear-gradient(#2d1233,#b8397a 55%,#ffb48a)'];
var CAP = ['Slow mornings, simple coffee', 'City lights after the rain', 'Five-minute stretch routine', 'Quiet beach, no signal', 'Cat versus the vacuum', 'Sunday pasta, the easy way', 'Desk setup under 5000 rupees', 'Golden hour from the roof'];
var faceFor = function (c) { return c >= LIMIT ? '900' : c >= LIMIT - 1 ? '250' : c >= LIMIT / 2 ? '100' : c >= 2 ? '50' : '0'; };
var paint = function () {
cnt.textContent = n; left.textContent = (LIMIT - n) + ' left'; bar.style.width = (n / LIMIT * 100) + '%';
hud.classList.toggle('warn', n >= LIMIT - 2); face.src = base + 'mascot-' + faceFor(n) + '.webp';
reel.style.setProperty('--g', PAL[n % PAL.length]); var c = $('#demoCap'); if (c) c.textContent = CAP[n % CAP.length];
};
var swipe = function () {
if (locked) return; locked = true;
reel.classList.add('swipe'); hud.classList.add('tick');
setTimeout(function () {
n++; paint(); reel.classList.remove('swipe'); hud.classList.remove('tick');
if (n >= LIMIT) { setTimeout(function () { over.classList.add('on'); }, 350); } else { locked = false; }
}, 280);
};
var reset = function () { over.classList.remove('on'); n = 0; locked = false; paint(); };
swipeBtn.addEventListener('click', swipe); resetBtn.addEventListener('click', reset);
var y0 = null, scr = $('.demo-screen', demo);
scr.addEventListener('pointerdown', function (e) { y0 = e.clientY; });
scr.addEventListener('pointerup', function (e) { if (y0 !== null && y0 - e.clientY > 40) swipe(); y0 = null; });
scr.addEventListener('wheel', function (e) { if (e.deltaY > 20 && !locked) { e.preventDefault(); swipe(); } }, { passive: false });
paint();
}
if (calc) {
var stats = ['cHours', 'cDays', 'cBooks', 'cSaved'].map(function (id) { return document.getElementById(id); });
var seen = {};
var tween = function (el) {
var txt = el.textContent, m = txt.match(/^([\d,.]+)(.*)$/); if (!m) return;
var target = parseFloat(m[1].replace(/,/g, '')), dec = (m[1].split('.')[1] || '').length, suf = m[2], from = seen[el.id] != null ? seen[el.id] : 0, t0 = null;
seen[el.id] = target;
if (reduce) return;
var step = function (t) { if (!t0) t0 = t; var p = Math.min(1, (t - t0) / 450), v = from + (target - from) * (1 - Math.pow(1 - p, 3));
el.textContent = v.toLocaleString('en-IN', { minimumFractionDigits: dec, maximumFractionDigits: dec }) + suf; if (p < 1) requestAnimationFrame(step); };
requestAnimationFrame(step);
};
calc.addEventListener('input', function () { stats.forEach(tween); });
}
var lit = $('#lit'), litText = $('#litText');
if (lit && litText) {
var words = [];
var wrap = function (node) {
Array.prototype.slice.call(node.childNodes).forEach(function (c) {
if (c.nodeType === 3) {
var frag = document.createDocumentFragment();
c.textContent.split(/(\s+)/).forEach(function (t) {
if (!t) return;
if (/^\s+$/.test(t)) { frag.appendChild(document.createTextNode(' ')); return; }
var sp = document.createElement('span'); sp.className = 'w'; sp.textContent = t; words.push(sp); frag.appendChild(sp);
});
node.replaceChild(frag, c);
} else if (c.nodeType === 1) wrap(c);
});
};
wrap(litText);
var upd2 = function () {
var r = lit.getBoundingClientRect(), total = lit.offsetHeight - window.innerHeight;
var p = reduce ? 1 : Math.min(1, Math.max(0, -r.top / Math.max(1, total)));
p = Math.min(1, Math.max(0, (p - 0.04) / 0.8));
var n = words.length;
words.forEach(function (w, i) {
var v = Math.min(1, Math.max(0, (p * (n + 5) - i) / 5));
w.style.opacity = (0.15 + 0.85 * v).toFixed(3);
});
};
var t2 = false;
window.addEventListener('scroll', function () { if (!t2) { t2 = true; requestAnimationFrame(function () { upd2(); t2 = false; }); } }, { passive: true });
window.addEventListener('resize', upd2); upd2();
}
var rail = $('#scRail');
if (rail) {
var cards = $$('.sc-card', rail);
var fit = function () {
var c = rail.scrollLeft + rail.clientWidth / 2;
cards.forEach(function (card) {
var d = Math.abs(card.offsetLeft + card.offsetWidth / 2 - c) / card.offsetWidth;
card.style.setProperty('--s', Math.max(0.9, 1 - d * 0.1).toFixed(3));
card.style.setProperty('--lift', (Math.max(0, 1 - d) * -20).toFixed(1) + 'px');
card.classList.toggle('on', d < 0.5);
});
};
var tk = false;
rail.addEventListener('scroll', function () { if (!tk) { tk = true; requestAnimationFrame(function () { fit(); tk = false; }); } }, { passive: true });
var go = function (dir) { var w = cards[0].offsetWidth + 20; rail.scrollBy({ left: dir * w, behavior: 'smooth' }); };
$('#scPrev').addEventListener('click', function () { go(-1); });
$('#scNext').addEventListener('click', function () { go(1); });
rail.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight') go(1); if (e.key === 'ArrowLeft') go(-1); });
var down = false, sx = 0, sl = 0;
rail.addEventListener('pointerdown', function (e) { if (e.pointerType !== 'mouse') return; down = true; sx = e.clientX; sl = rail.scrollLeft; rail.classList.add('drag'); });
window.addEventListener('pointermove', function (e) { if (down) rail.scrollLeft = sl - (e.clientX - sx); });
window.addEventListener('pointerup', function () { if (down) { down = false; rail.classList.remove('drag'); } });
var start = cards[2] || cards[0];
rail.scrollLeft = start.offsetLeft + start.offsetWidth / 2 - rail.clientWidth / 2; fit();
window.addEventListener('resize', fit);
}
var fc = $('#floatCta'), foot = $('.site-footer');
if (fc) {
var visFoot = false;
var showFc = function () { var on = window.scrollY > 700 && !visFoot; fc.classList.toggle('show', on); fc.tabIndex = on ? 0 : -1; };
if (foot && 'IntersectionObserver' in window) new IntersectionObserver(function (e) { visFoot = e[0].isIntersecting; showFc(); }).observe(foot);
window.addEventListener('scroll', showFc, { passive: true }); showFc();
}
})();