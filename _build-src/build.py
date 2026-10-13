import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
import pages_home, pages_product, pages_company, blog
OUT = "/home/claude/out/site/"
pages = {"index.html": pages_home.home(), "features.html": pages_product.features(), "how-it-works.html": pages_product.how(),
         "students.html": pages_company.students(), "professionals.html": pages_company.professionals(),
         "comparison.html": pages_company.comparison(), "faq.html": pages_company.faq(), "about.html": pages_company.about(),
         "contact.html": pages_company.contact(), "privacy.html": pages_company.privacy(), "terms.html": pages_company.terms(),
         "404.html": pages_company.notfound(), "blog/index.html": blog.index()}
pages.update(pages_product.landings())
for p in blog.POSTS: pages[f'blog/{p["slug"]}.html'] = blog.post_page(p)
import re, shutil
def srcset(h):
    def f(m):
        pre, root, name, post = m.group(1), m.group(2), m.group(3), m.group(4)
        if name.endswith("-sm") or "srcset" in pre + post: return m.group(0)
        sizes = "(max-width: 900px) 42vw, 270px" if "fetchpriority" in pre + post else "(max-width: 640px) 70vw, 330px"
        return f'<img{pre}src="{root}assets/img/{name}.webp" srcset="{root}assets/img/{name}-sm.webp 390w, {root}assets/img/{name}.webp 780w" sizes="{sizes}" decoding="async"{post}>'
    return re.sub(r'<img([^>]*?)src="([^"]*?)assets/img/(scr-[a-z]+)\.webp"([^>]*?)>', lambda m: f(type("M",(),{"group":lambda self,i,m=m:(m.group(0) if i==0 else m.group(i))})()), h)

def accent(h):
    def one(m):
        tag, inner = m.group(1), m.group(2)
        if "<" in inner or inner.count(" ") < 3: return m.group(0)
        words = inner.rsplit(" ", 2)
        return f'{tag}{words[0]} <em class="serif">{words[1]} {words[2]}</em>' + m.group(3)
    h = re.sub(r'(<div class="section-head"><div><span class="eyebrow">[^<]*</span><h2>)([^<]*)(</h2>)', one, h)
    h = re.sub(r'(<div class="cta-band[^>]*>\s*<div><h2>)([^<]*)(</h2>)', one, h)
    h = re.sub(r'(<span class="eyebrow">[^<]*</span>\s*<h1>)([^<]*)(</h1>)', one, h)
    return h
for k in pages: pages[k] = accent(pages[k])
for k in pages: pages[k] = srcset(pages[k])
pages["index.html"] = pages["index.html"].replace("</head>", '<link rel="preload" as="image" href="assets/img/scr-hud-sm.webp" imagesrcset="assets/img/scr-hud-sm.webp 390w, assets/img/scr-hud.webp 780w" imagesizes="(max-width: 900px) 42vw, 270px" fetchpriority="high">\n</head>', 1)
def mincss(t):
    t = re.sub(r"/\*.*?\*/", "", t, flags=re.S); t = re.sub(r"\s+", " ", t)
    t = re.sub(r"\s*([{};,>])\s*", r"\1", t); t = re.sub(r";}", "}", t); return t.strip()
def minjs(t):
    t = re.sub(r"/\*.*?\*/", "", t, flags=re.S)
    out = []
    for ln in t.split("\n"):
        l = ln.strip()
        if not l or l.startswith("//"): continue
        out.append(l)
    return "\n".join(out)
here = os.path.dirname(__file__)
open(OUT + "assets/css/style.css", "w").write(mincss(open(here + "/src/style.css").read()))
open(OUT + "assets/js/main.js", "w").write(minjs(open(here + "/src/main.js").read()))
open(OUT + "_headers", "w").write("""/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n/*.png\n  Cache-Control: public, max-age=604800\n/*.html\n  Cache-Control: public, max-age=0, must-revalidate\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n""")
os.makedirs(OUT + "blog", exist_ok=True)
for k, v in pages.items(): open(OUT + k, "w", encoding="utf-8").write(v)
# sitemap
prio = {"index.html":"1.0","features.html":"0.9","how-it-works.html":"0.9","screen-time-controller.html":"0.9","instagram-reels-blocker.html":"0.9","youtube-shorts-blocker.html":"0.9","short-video-blocker.html":"0.8","blog/index.html":"0.8"}
urls = []
for k in pages:
    if k == "404.html": continue
    loc = SITE + "/" if k == "index.html" else (SITE + "/blog/" if k == "blog/index.html" else SITE + "/" + k)
    pr = prio.get(k, "0.7" if k.startswith("blog/") else ("0.3" if k in ("privacy.html","terms.html") else "0.7"))
    urls.append(f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>")
open(OUT + "sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
open(OUT + "robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
open(OUT + "CNAME", "w").write("focusport.in")
open(OUT + "site.webmanifest", "w").write(json.dumps({"name":"Brainrot","short_name":"Brainrot","description":"Reel limiter and screen time controller for Android.","start_url":"/","display":"browser","background_color":"#f4f2ec","theme_color":"#f4f2ec","icons":[{"src":"/icon-192.png","sizes":"192x192","type":"image/png"},{"src":"/icon-512.png","sizes":"512x512","type":"image/png"}]}, indent=1))
open(OUT + "llms.txt", "w").write(f"""# Brainrot

> Brainrot (app name: Brainrot: Reel Limit) is a free Android app that counts and caps short-video feeds (Instagram Reels, YouTube Shorts, Facebook Reels, Snapchat Spotlight), sets daily time limits on any app, and runs timed focus sessions. Processing is on-device; no account is required.

## Key pages
- [Home]({SITE}/): overview
- [Features]({SITE}/features.html)
- [How it works]({SITE}/how-it-works.html)
- [Screen time controller]({SITE}/screen-time-controller.html)
- [Instagram Reels blocker]({SITE}/instagram-reels-blocker.html)
- [YouTube Shorts blocker]({SITE}/youtube-shorts-blocker.html)
- [Short video blocker]({SITE}/short-video-blocker.html)
- [Comparison]({SITE}/comparison.html)
- [FAQ]({SITE}/faq.html)
- [Blog]({SITE}/blog/)
- [Privacy]({SITE}/privacy.html)

## Facts
- Platform: Android only. Price: free. Permission: Accessibility Service (used to detect short-video screens and swipes).
- Google Play: {PLAY}
- Support: {EMAIL}
""")
print(len(pages), "pages")
