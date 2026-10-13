import re
from lib import *
import posts_a, posts_b, posts_c
POSTS = posts_a.POSTS
BY = {p["slug"]: p for p in POSTS}
ORDER = ["what-is-brainrot","how-to-stop-doomscrolling","how-to-block-reels-on-android","are-reels-addictive","stop-watching-reels-at-night","how-many-reels-a-day-is-too-many","screen-time-for-students","how-to-use-digital-wellbeing-android","how-to-reduce-screen-time-android","best-app-blockers-android","instagram-reels-blocker-guide","youtube-shorts-limiter-guide","dopamine-detox-guide","short-form-video-addiction-effects","adhd-screen-time-management","why-willpower-fails-against-algorithms"]

def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", t).lower()).strip("-")

def post_page(p):
    r = "../"
    toc_items = []
    def sub(m):
        i = slugify(m.group(1)); toc_items.append((i, re.sub(r"<[^>]+>", "", m.group(1))))
        return f'<h2 id="{i}">{m.group(1)}</h2>'
    body = re.sub(r"<h2>(.*?)</h2>", sub, p["body"])
    toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc_items)
    rel = "".join(f'<a class="card" href="{s}.html"><span class="tag">{BY[s]["tag"]}</span><h3>{BY[s]["title"]}</h3><p class="meta">{BY[s]["mins"]} min read</p></a>' for s in p["related"])
    url = f'{SITE}/blog/{p["slug"]}.html'
    crumbs = f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{r}index.html">Home</a><span aria-hidden="true">/</span><a href="index.html">Blog</a><span aria-hidden="true">/</span><span>{p["tag"]}</span></nav>'
    html_body = f'''<div class="progress" id="progress"></div>
<div class="container"><div class="article-head" style="max-width:820px;margin-inline:auto">
{crumbs}<span class="eyebrow">{p["tag"]}</span><h1>{p["title"]}</h1><p class="lede">{p["lede"]}</p>
<div class="article-meta"><span>By Brainrot</span><span>{p["mins"]} min read</span><span>Updated Oct 11, 2026</span></div></div></div>
<div class="article-layout">
<aside class="toc" aria-label="Table of contents"><h2>On this page</h2><ol>{toc}</ol></aside>
<article><div class="prose" id="articleBody">{body}</div>
<div class="article-cta"><h3>Put it into practice.</h3><p>Brainrot counts and caps Reels and Shorts on Android and leaves everything else alone. Free, no account.</p>{play_btn("btn btn-blue","Get it on Google Play","article")}</div>
<div class="related"><h2>Keep reading</h2><div class="cards">{rel}</div></div></article>
</div>'''
    schema = [article_schema(url, p["title"], p["desc"], PUBLISHED, TODAY),
              breadcrumb([("Home","/"),("Blog","/blog/"),(p["title"],f'/blog/{p["slug"]}.html')])]
    if p.get("howto"):
        schema.append(howto_schema(p["title"], p["desc"], p["howto"]))
    return page(f'blog/{p["slug"]}.html', p["seo"], p["desc"], html_body, root=r, current="blog/", schema=schema,
                og_type="article", published=PUBLISHED, modified=TODAY, keywords=p["keywords"])

def index():
    r = "../"
    first = BY[ORDER[0]]
    rest = "".join(f'<a class="card" href="{s}.html"><span class="tag">{BY[s]["tag"]}</span><h3>{BY[s]["title"]}</h3><p>{BY[s]["desc"]}</p><p class="meta">{BY[s]["mins"]} MIN READ</p></a>' for s in ORDER[1:])
    body = f'''<section class="page-head"><div class="container">
<nav class="crumbs" aria-label="Breadcrumb"><a href="{r}index.html">Home</a><span aria-hidden="true">/</span><span>Blog</span></nav>
<span class="eyebrow">The Brainrot blog</span><h1>Attention, habits and screen time.</h1>
<p class="lede">Practical, honest guides on doomscrolling, short-form video and taking back your time on Android.</p></div></section>
<section class="section-tight"><div class="container">
<a class="post-feature" href="{first["slug"]}.html"><div><span class="eyebrow">{first["tag"]} · {first["mins"]} min read</span><h2>{first["title"]}</h2><p>{first["desc"]}</p></div><div class="post-art"><img src="{r}assets/img/mascot-250.webp" alt="" width="170" height="145" style="height:60%"></div></a>
<div class="cards mt-3">{rest}</div></div></section>{cta_band(r)}'''
    schema = [{"@type":"Blog","@id":SITE+"/blog/#blog","url":SITE+"/blog/","name":"Brainrot Blog","publisher":{"@id":SITE+"/#org"},
               "blogPost":[{"@type":"BlogPosting","headline":BY[s]["title"],"url":f'{SITE}/blog/{s}.html'} for s in ORDER]},
              breadcrumb([("Home","/"),("Blog","/blog/")])]
    return page("blog/index.html", "Blog: Doomscrolling, Focus & Android Screen Time | Brainrot",
        "Guides on stopping doomscrolling, limiting Reels and YouTube Shorts, reducing screen time on Android and managing focus with ADHD.",
        body, root=r, current="blog/", schema=schema,
        keywords="doomscrolling blog, screen time tips, focus tips, android digital wellbeing blog, reels addiction")
