# Shared layout, SEO + schema helpers for the Brainrot static site.
import json, html, datetime

SITE = "https://brainrot.focusport.in"
PLAY = "https://play.google.com/store/apps/details?id=com.focusport.limit"
EMAIL = "support@focusport.in"
PRIVACY_EMAIL = "privacy@focusport.in"
TODAY = "2026-10-26"
PUBLISHED = "2026-09-30"
OG_IMAGE = SITE + "/assets/img/og-image.jpg"
FONTS = ("https://fonts.googleapis.com/css2?family=Archivo:wght@600..900"
         "&family=Instrument+Sans:wght@400;500;600"
         "&family=JetBrains+Mono:wght@500&family=Instrument+Serif:ital@1&display=swap")

def e(s): return html.escape(s, quote=True)

ICONS = {
 "play": '<path d="M5 3.5v17a1 1 0 0 0 1.5.86l14-8.5a1 1 0 0 0 0-1.72l-14-8.5A1 1 0 0 0 5 3.5z" fill="currentColor" stroke="none"/>',
 "count": '<path d="M5 5v14M10 5v14M15 5v14M20 5v14M3 17 22 7"/>',
 "layers": '<path d="m12 3 9 5-9 5-9-5 9-5z"/><path d="m3 13 9 5 9-5"/>',
 "hud": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3" fill="currentColor"/>',
 "grid": '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
 "timer": '<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2M9 2h6"/>',
 "calendar": '<rect x="3" y="4.5" width="18" height="16" rx="2"/><path d="M3 9.5h18M8 2.5v4M16 2.5v4"/>',
 "shield": '<path d="M12 3 4.5 6v5.5c0 4.6 3.1 8.2 7.5 9.5 4.4-1.3 7.5-4.9 7.5-9.5V6L12 3z"/><path d="m8.5 12 2.5 2.5 4.5-5"/>',
 "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
 "lock": '<rect x="4.5" y="10.5" width="15" height="10" rx="2"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/>',
 "brain": '<path d="M9 4.5a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 4.7A3 3 0 0 0 12 18V6a3 3 0 0 0-3-1.5zM15 4.5a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 4.7A3 3 0 0 1 12 18"/>',
 "phone": '<rect x="6.5" y="2.5" width="11" height="19" rx="2.5"/><path d="M10.5 18.5h3"/>',
 "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
}
def icon(name, cls=""):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'

NAV = [
 ("features.html", "Features"),
 ("how-it-works.html", "How it works"),
 ("screen-time-controller.html", "Screen time"),
 ("comparison.html", "Compare"),
 ("blog/", "Blog"),
 ("faq.html", "FAQ"),
]

def play_btn(cls="btn btn-blue", label="Get it on Google Play", where="cta"):
    return (f'<a class="{cls}" href="{PLAY}" target="_blank" rel="noopener" data-where="{where}">'
            f'{icon("play")}{label}</a>')

def header(root, current):
    links = "".join(
        f'<a href="{root}{h}"' + (' aria-current="page"' if h == current else '') + f'>{t}</a>' for h, t in NAV)
    drawer = "".join(f'<a href="{root}{h}">{t}</a>' for h, t in
        [("index.html","Home")] + NAV + [("students.html","For students"),("professionals.html","For professionals"),("about.html","About"),("contact.html","Contact")])
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="{root}index.html" aria-label="Brainrot home"><img src="{root}assets/img/logo-256.webp" alt="" width="36" height="36"><span class="wm">Brain<b>rot</b></span><small class="wm-sub">Reel Limit</small></a>
    <nav class="nav-links" aria-label="Primary">{links}</nav>
    <div class="nav-cta">
      <button class="theme-btn" id="themeBtn" type="button" aria-label="Switch theme" title="Switch theme"><svg class="i-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2.5M12 19v2.5M2.5 12H5M19 12h2.5M5.3 5.3l1.8 1.8M16.9 16.9l1.8 1.8M5.3 18.7l1.8-1.8M16.9 7.1l1.8-1.8"/></svg><svg class="i-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5z"/></svg></button>
      {play_btn("btn btn-ink btn-sm","Get the app","header")}
      <button class="menu-btn" id="menuBtn" aria-label="Menu" aria-expanded="false" aria-controls="drawer"><span></span></button>
    </div>
  </div>
  <nav class="drawer" id="drawer" aria-label="Mobile">{drawer}{play_btn("btn btn-blue","Get it on Google Play","drawer")}</nav>
</header>'''

def footer(root):
    def col(title, items):
        return f'<div><h2>{title}</h2><ul>' + "".join(f'<li><a href="{root}{h}">{t}</a></li>' for h, t in items) + '</ul></div>'
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="{root}index.html"><img src="{root}assets/img/logo-256.webp" alt="" width="36" height="36"><span class="wm">Brain<b>rot</b></span><small class="wm-sub">Reel Limit</small></a>
        <p>A reel limiter and screen time controller for Android. Count short videos, cap them, and keep the rest of your phone.</p>
        <p class="mt-1"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      {col("Product", [("features.html","Features"),("how-it-works.html","How it works"),("screen-time-controller.html","Screen time controller"),("comparison.html","Compare"),("faq.html","FAQ")])}
      {col("Block", [("instagram-reels-blocker.html","Instagram Reels"),("youtube-shorts-blocker.html","YouTube Shorts"),("short-video-blocker.html","Facebook Reels & Spotlight")])}
      {col("Learn", [("blog/","Blog"),("blog/how-to-stop-doomscrolling.html","Stop doomscrolling"),("blog/how-to-reduce-screen-time-android.html","Reduce screen time"),("blog/what-is-brainrot.html","What is brainrot?"),("blog/how-to-block-reels-on-android.html","Block Reels on Android")])}
      {col("Company", [("about.html","About"),("students.html","For students"),("professionals.html","For professionals"),("contact.html","Contact"),("privacy.html","Privacy"),("terms.html","Terms")])}
    </div>
    <div class="footer-bottom">
      <p>© 2026 Brainrot: Reel Limit. Powered by FocusPort. Android is a trademark of Google LLC. Instagram, YouTube, Facebook and Snapchat are trademarks of their respective owners; Brainrot is not affiliated with or endorsed by them.</p>
      <p><a href="{root}privacy.html">Privacy</a> · <a href="{root}terms.html">Terms</a> · <a href="{root}sitemap.xml">Sitemap</a></p>
    </div>
  </div>
</footer>'''

# ---------- JSON-LD ----------
ORG = {"@type": "Organization", "@id": SITE + "/#org", "name": "Brainrot", "url": SITE + "/",
       "logo": {"@type": "ImageObject", "url": SITE + "/icon-512.png", "width": 512, "height": 512},
       "parentOrganization": {"@type": "Organization", "name": "FocusPort"}, "email": EMAIL, "contactPoint": {"@type": "ContactPoint", "email": EMAIL, "contactType": "customer support", "availableLanguage": "English"}}
WEBSITE = {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Brainrot",
           "description": "Reel limiter and screen time controller for Android.", "inLanguage": "en", "publisher": {"@id": SITE + "/#org"}}
APP = {"@type": "MobileApplication", "@id": SITE + "/#app", "name": "Brainrot: Reel Limit",
       "alternateName": ["Brainrot", "Brainrot Reel Limiter", "Brainrot app", "FocusPort Limit"],
       "description": "Brainrot: Reel Limit counts and caps Instagram Reels, YouTube Shorts, Facebook Reels and Snapchat Spotlight on Android, adds app time limits and focus sessions, and processes everything on-device.",
       "operatingSystem": "Android", "applicationCategory": "LifestyleApplication",
       "applicationSubCategory": "Digital wellbeing, screen time control",
       "url": SITE + "/", "downloadUrl": PLAY, "installUrl": PLAY,
       "image": SITE + "/assets/img/scr-hud.webp", "screenshot": [SITE + f"/assets/img/scr-{k}.webp" for k in ("home","hud","limit","limits","usage","focus")],
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "availability": "https://schema.org/InStock"},
       "featureList": ["Per-video Reels and Shorts counter", "Daily limits for Instagram Reels, YouTube Shorts, Facebook Reels and Snapchat Spotlight",
                       "Shared limit across all apps or per-app limits", "Floating on-screen counter", "Daily time limits for any app",
                       "Focus sessions with essential-apps allow list", "Focus schedules", "7-day usage insights", "On-device processing, no account"],
       "publisher": {"@id": SITE + "/#org"}}

def breadcrumb(trail):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(trail)]}

def faq_schema(qas):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qas]}

def howto_schema(name, desc, steps):
    return {"@type": "HowTo", "name": name, "description": desc, "totalTime": "PT2M",
            "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t} for i, (n, t) in enumerate(steps)]}

def article_schema(url, title, desc, published, modified, image=OG_IMAGE):
    return {"@type": "BlogPosting", "@id": url + "#article", "headline": title, "description": desc, "image": image,
            "datePublished": published, "dateModified": modified, "inLanguage": "en",
            "author": {"@id": SITE + "/#org"}, "publisher": {"@id": SITE + "/#org"},
            "mainEntityOfPage": {"@type": "WebPage", "@id": url}}

def page(path, title, desc, body, *, keywords="", root="", current="", schema=None, og_type="website",
         og_image=OG_IMAGE, noindex=False, extra_head="", published=None, modified=None):
    url = SITE + "/" + path if path != "index.html" else SITE + "/"
    if path.endswith("/index.html") : url = SITE + "/" + path[:-10]
    graph = [ORG, WEBSITE] + (schema or [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))
    robots = "noindex,follow" if noindex else "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"
    art = ""
    if og_type == "article":
        art = (f'<meta property="article:published_time" content="{published}T09:00:00+05:30">'
               f'<meta property="article:modified_time" content="{modified}T09:00:00+05:30">'
               f'<meta property="article:author" content="Brainrot">')
    kw = f'<meta name="keywords" content="{e(keywords)}">' if keywords else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{kw}
<meta name="robots" content="{robots}">
<meta name="author" content="Brainrot">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta name="theme-color" content="#f4f2ec" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0d0e13" media="(prefers-color-scheme: dark)">
<meta name="color-scheme" content="light dark">
<script>(function(){{try{{var t=localStorage.getItem("theme");if(!t)t=matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light";document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}}})()</script>
<meta name="application-name" content="Brainrot">
<meta name="apple-mobile-web-app-title" content="Brainrot">
<meta name="format-detection" content="telephone=no">
<link rel="icon" href="{root}favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="32x32" href="{root}favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="{root}icon-192.png">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<link rel="manifest" href="{root}site.webmanifest">
<meta property="og:site_name" content="Brainrot">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="en_IN">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Brainrot — reel limiter and screen time controller for Android">
{art}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{og_image}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="{FONTS}"></noscript>
<link rel="stylesheet" href="{root}assets/css/style.css">
<script type="application/ld+json">{ld}</script>
{extra_head}
</head>
<body>
{header(root, current)}
<main id="main">
{body}
</main>
{footer(root)}
<a class="float-cta" id="floatCta" href="{PLAY}" target="_blank" rel="noopener" aria-label="Get Brainrot on Google Play" tabindex="-1"><img src="{root}assets/img/mascot-0.webp" alt="" width="34" height="30"><span><b>Brainrot: Reel Limit</b><small>Free on Google Play</small></span><i aria-hidden="true">→</i></a>
<script src="{root}assets/js/main.js" defer></script>
</body>
</html>
'''

def page_head(root, crumbs, eyebrow, h1, lede, media=None, ctas=True):
    """Inner-page header. crumbs: list of (label, href|None)."""
    c = '<span aria-hidden="true">/</span>'.join(
        (f'<a href="{root}{h}">{l}</a>' if h else f'<span>{l}</span>') for l, h in crumbs)
    btns = f'<div class="btn-row mt-2">{play_btn()}<a class="btn btn-line" href="{root}how-it-works.html">How it works</a></div>' if ctas else ""
    inner = f'''<nav class="crumbs" aria-label="Breadcrumb">{c}</nav>
<span class="eyebrow">{eyebrow}</span>
<h1>{h1}</h1>
<p class="lede">{lede}</p>{btns}'''
    if media:
        return f'<section class="page-head"><div class="container page-head-grid"><div>{inner}</div><img src="{root}assets/img/{media}" alt="Brainrot app screen" width="250" height="444" loading="eager"></div></section>'
    return f'<section class="page-head"><div class="container">{inner}</div></section>'

def cta_band(root, h="Take your scroll back.", p="Free on Google Play. Set a limit in two minutes and keep every app you actually need."):
    return f'''<section class="section-tight"><div class="container"><div class="cta-band reveal">
<div><h2>{h}</h2><p>{p}</p></div>
<div class="btn-row">{play_btn("btn btn-blue","Get it on Google Play","band")}<a class="btn btn-line" style="border-color:rgba(255,255,255,.25);color:#fff" href="{root}faq.html">Read the FAQ</a></div>
</div></div></section>'''
