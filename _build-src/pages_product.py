from lib import *
from faqdata import FAQ, render_faq

def features():
    r = ""
    body = page_head(r, [("Home","index.html"),("Features",None)], "Features",
        "Everything Brainrot does, in one place.",
        "A short-video limiter, a screen time controller, and a few small tools that make both easier to stick to. This is what each part does.") + f'''
<section class="section"><div class="container">
  <div class="split reveal">
    <div><span class="split-num">01 — SHORT-VIDEO LIMITER</span><h3>Per-video counting for four feeds.</h3>
    <p>Brainrot has a dedicated detector for each feed, so it can tell a Reel from a regular post and a Short from a long video.</p>
    <ul class="ticks">
      <li><strong>Instagram Reels:</strong> counts swipes in the Reels viewer. DMs, Stories and the regular feed stay open.</li>
      <li><strong>YouTube Shorts:</strong> counts Shorts only. Lectures, podcasts and music play without a counter.</li>
      <li><strong>Facebook Reels:</strong> stops the autoplay chain of vertical videos.</li>
      <li><strong>Snapchat Spotlight:</strong> caps the endless Spotlight feed while chats and Snaps stay available.</li>
    </ul></div>
    <div class="split-media"><img src="assets/img/scr-hud.webp" alt="Brainrot counting Reels live with a floating counter" width="390" height="844" loading="lazy"></div>
  </div>
  <div class="split flip reveal">
    <div><span class="split-num">02 — LIMIT MODES</span><h3>One shared budget, or one per app.</h3>
    <p><strong>Unified</strong> gives you a single daily pool. Watch 20 on Instagram and 30 on YouTube and a 50-video limit is used up. It's the mode that stops you from swapping one feed for another.</p>
    <p class="mt-1"><strong>Individual</strong> lets you set separate numbers, say 20 on Instagram, 10 on YouTube and 0 on Snapchat, for when each app plays a different role in your life.</p></div>
    <div class="split-media"><img src="assets/img/scr-limits.webp" alt="Brainrot limits screen with All Platforms and Individual modes" width="390" height="844" loading="lazy"></div>
  </div>
  <div class="split reveal">
    <div><span class="split-num">03 — FOCUS SESSIONS</span><h3>Timed sessions with no way out.</h3>
    <p>Start a focus timer with quick presets or schedule recurring sessions. While a session runs, distracting apps are blocked and notifications are muted. Only the essential apps you chose, such as Phone and Messages, stay available.</p>
    <ul class="ticks"><li>Focus timer from 15 minutes upward</li><li>Recurring schedules by day and time</li><li>Essential-apps allow list</li><li>Emergency access if something real comes up</li></ul></div>
    <div class="split-media"><img src="assets/img/scr-focus.webp" alt="Brainrot focus session with timer and no-escape mode" width="390" height="844" loading="lazy"></div>
  </div>
  <div class="split flip reveal">
    <div><span class="split-num">04 — INSIGHTS</span><h3>See whether it's working.</h3>
    <p>A 7-day usage history, weekly total and daily average for your short-video watching, plus focus time, completed sessions and a streak for your focus sessions. Everything is computed on your phone.</p></div>
    <div class="split-media"><img src="assets/img/scr-usage.webp" alt="Brainrot screen time and 7-day usage history" width="390" height="844" loading="lazy"></div>
  </div>
</div></section>

<section class="section bg-white rule-top"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Also included</span><h2>The small things.</h2></div><p>None of these is the headline, but together they are why the app stays out of your way.</p></div>
  <div class="feat-grid">
    <div class="feat">{icon("hud")}<h3>Floating counter</h3><p>Appears only inside a short-video feed and disappears when you leave it.</p></div>
    <div class="feat">{icon("grid")}<h3>Any-app time limits</h3><p>Set a daily time limit on any installed app: games, news, shopping, anything.</p></div>
    <div class="feat">{icon("brain")}<h3>11-stage brain mascot</h3><p>From fresh at 0 to completely fried at 1000+. A number you can read at a glance.</p></div>
    <div class="feat">{icon("lock")}<h3>Hard stop screen</h3><p>When you hit the limit the feed closes. There is no snooze button to bargain with.</p></div>
    <div class="feat">{icon("phone")}<h3>Essentials stay open</h3><p>Calls, messages, maps and the apps you choose are never blocked.</p></div>
    <div class="feat">{icon("shield")}<h3>No account, no ads</h3><p>Install and go. Data stays on the device and is deleted when you uninstall.</p></div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><div><span class="eyebrow">The mascot</span><h2>Eleven stages of brain.</h2></div><p>The mascot steps forward at each milestone of your daily count. <a href="index.html#mascot" style="color:var(--blue-deep)">Try the interactive version →</a></p></div>
  <div class="table-wrap"><table class="compare"><thead><tr><th scope="col">Daily videos</th><th scope="col">Stage</th><th scope="col">Feeling</th></tr></thead><tbody>
  <tr><td>0</td><th scope="row">Fresh</th><td>Sharp and ready to focus</td></tr>
  <tr><td>50</td><th scope="row">Still fine</th><td>A little tired</td></tr>
  <tr><td>100</td><th scope="row">Getting tired</th><td>Losing alertness</td></tr>
  <tr><td>250</td><th scope="row">Losing focus</th><td>Mind drifting</td></tr>
  <tr><td>400</td><th scope="row">Mentally drained</th><td>Attention depleted</td></tr>
  <tr><td>500</td><th scope="row">Focus fading</th><td>Overstimulated</td></tr>
  <tr><td>600</td><th scope="row">Seriously affected</th><td>Scrolling fatigue</td></tr>
  <tr><td>700</td><th scope="row">Brain overloaded</th><td>Cognitive overload</td></tr>
  <tr><td>800</td><th scope="row">Almost broken</th><td>Excessive scroll</td></tr>
  <tr><td>900</td><th scope="row">System failing</th><td>Severe overload</td></tr>
  <tr><td>1000+</td><th scope="row">Completely fried</th><td>Limit destroyed</td></tr></tbody></table></div>
</div></section>
{cta_band(r)}'''
    return page("features.html", "Brainrot Features: Reel Counter, App Limits, Focus",
        "Per-video Reels and Shorts counter, shared or per-app limits, app time limits, focus sessions and schedules. See every Brainrot feature for Android.",
        body, root=r, current="features.html",
        schema=[APP, breadcrumb([("Home","/"),("Features","/features.html")])],
        keywords="reel counter app, short video limiter, app limit android, focus sessions, screen time features, doomscrolling blocker features")

def how():
    r = ""
    steps = [
     ("Install Brainrot: Reel Limit","Get the app from Google Play. It's free and there's no sign-up."),
     ("Turn on the Accessibility Service","Open Settings → Accessibility → Brainrot: Reel Limit and switch it on. This is the permission that lets the app detect when a Reel or Short is open and when you swipe."),
     ("Allow the floating counter (optional)","Allow \"display over other apps\" if you'd like the live counter on top of the feed. The limit works without it."),
     ("Choose Unified or Individual","Unified is one shared daily number across every feed. Individual is one number per app."),
     ("Set your daily limit","Pick a number a little below your current daily average. Lower it every week or two."),
     ("Open your usual apps","DMs, calls, long videos and everything else work as before. Only the short-video feed is counted and capped."),
    ]
    steps_html = "".join(f'<div class="step"><h3>{n}</h3><p>{t}</p></div>' for n, t in steps)
    faq = [FAQ[12], FAQ[13], FAQ[14], FAQ[15]]
    body = page_head(r, [("Home","index.html"),("How it works",None)], "Setup guide",
        "How to set up a reel limit in two minutes.",
        "Brainrot needs one permission and one number. This guide walks through both, then explains what happens when you reach your limit.") + f'''
<section class="section"><div class="container">
  <div class="steps reveal" style="grid-template-columns:repeat(3,1fr)">{steps_html}</div>
</div></section>

<section class="section bg-white rule-top"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Under the hood</span><h2>What Brainrot actually does.</h2></div><p>Nothing hidden here. This is what happens each time you open a short-video feed.</p></div>
  <div class="cards two">
    <div class="card"><span class="tag">When you open a feed</span><h3>It notices the screen.</h3><p>Android's Accessibility Service tells Brainrot that a particular screen opened. Brainrot checks whether it's a Reel, Short or Spotlight viewer. If it isn't, nothing happens.</p></div>
    <div class="card"><span class="tag">When you swipe</span><h3>It adds one.</h3><p>Each swipe to a new video counts as one. The number updates the floating counter and your daily total, which is stored on your phone only.</p></div>
    <div class="card"><span class="tag">When you reach the limit</span><h3>It closes the feed.</h3><p>A stop screen appears and you're taken out of the short-video feed. The rest of the app, and the rest of your phone, keep working.</p></div>
    <div class="card"><span class="tag">At midnight</span><h3>It resets.</h3><p>Counters start from zero each day. Your previous totals stay in the 7-day history so you can see the trend.</p></div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Picking a number</span><h2>How to choose a good limit.</h2></div><p>Too strict and you'll switch it off by Wednesday. Too loose and nothing changes. A simple approach works well.</p></div>
  <div class="prose-wide prose">
    <ol>
      <li><strong>Find your baseline.</strong> Install, set a very high limit (say 500) and use your phone normally for two days. The 7-day history will show your real average.</li>
      <li><strong>Start about 25% under it.</strong> If you average 120 a day, start at 90.</li>
      <li><strong>Lower it every week or two.</strong> Aim for a number that leaves you a little bored, not deprived. 20 to 40 a day is a common landing zone.</li>
      <li><strong>Use Unified mode first.</strong> A shared budget stops you from just moving the habit from Instagram to YouTube.</li>
    </ol>
    <div class="callout"><strong>Tip</strong>Set the limit in the morning, when you're clear-headed. The point of a limit is that you don't have to decide again at night.</div>
  </div>
</div></section>

<section class="section bg-white rule-top"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Troubleshooting</span><h2>If something isn't counting.</h2></div><p>Almost every problem comes down to one of these.</p></div>
  <dl class="dl paper-dl" style="max-width:860px">
    <div><dt>Not counting</dt><dd>Check Settings → Accessibility → Brainrot: Reel Limit is on. Some phones turn it off after an update or when "battery optimisation" is aggressive.</dd></div>
    <div><dt>Turned itself off</dt><dd>On some brands (Xiaomi, Oppo, Vivo, Samsung and others), set Brainrot's battery usage to "Unrestricted" or allow it to "Autostart".</dd></div>
    <div><dt>Counter missing</dt><dd>Allow "Display over other apps" for Brainrot. The limit still works without the counter.</dd></div>
    <div><dt>After an app update</dt><dd>Apps change their layouts. Update Brainrot and the other app, then <a href="contact.html" style="color:var(--blue-deep)">tell us</a> if it still misbehaves.</dd></div>
  </dl>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Permissions</span><h2>Questions about permissions.</h2></div><p>See the <a href="faq.html" style="color:var(--blue-deep)">full FAQ</a> for everything else.</p></div>
  <div class="faq-list">{render_faq(faq)}</div>
</div></section>
{cta_band(r)}'''
    hs = [(n, t) for n, t in steps]
    return page("how-it-works.html", "How Brainrot Works: Set Up a Reel Limit in 2 Minutes",
        "Step-by-step guide to installing Brainrot, enabling the Accessibility Service and setting a daily Reels and Shorts limit on Android.",
        body, root=r, current="how-it-works.html",
        schema=[APP, howto_schema("How to set a Reels and Shorts limit on Android with Brainrot", "Install Brainrot, enable the Accessibility Service and set a daily limit for short-video feeds.", hs),
                breadcrumb([("Home","/"),("How it works","/how-it-works.html")]), faq_schema([(q, p) for _, q, _, p in faq])],
        keywords="how to limit reels android, set reels limit, accessibility service reel counter, how to block shorts, focusport setup")

def landing(path, title, meta, h1, lede, eyebrow, keywords, screen, sections, faq_idx, related, crumb):
    r = ""
    faq = [FAQ[i] for i in faq_idx]
    body = page_head(r, [("Home","index.html"),(crumb,None)], eyebrow, h1, lede, media=screen) + sections + f'''
<section class="section bg-white rule-top"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Related</span><h2>Keep reading.</h2></div><p>Guides and pages that go deeper on this topic.</p></div>
  <div class="cards">{"".join(f'<a class="card" href="{h}"><span class="tag">{t}</span><h3>{n}</h3><span class="more">Open</span></a>' for n,t,h in related)}</div>
</div></section>
<section class="section"><div class="container">
  <div class="section-head"><div><span class="eyebrow">FAQ</span><h2>Common questions.</h2></div><p></p></div>
  <div class="faq-list">{render_faq(faq)}</div>
</div></section>
{cta_band(r)}'''
    return page(path, title, meta, body, root=r, current="",
        schema=[APP, breadcrumb([("Home","/"),(crumb,"/"+path)]), faq_schema([(q, p) for _, q, _, p in faq])], keywords=keywords)

def landings():
    out = {}
    insta = '''
<section class="section"><div class="container">
  <div class="split reveal"><div><span class="split-num">THE PROBLEM</span><h3>Instagram gives you no off switch for Reels.</h3>
  <p>Reels are now one of the main reasons people open Instagram, and the app has no setting to hide them. So you either delete Instagram and lose your messages, or you open it for one DM and surface half an hour later.</p>
  <p class="mt-1">Brainrot sits between those two options. It lets Instagram stay installed and useful, and limits only the Reels viewer.</p></div>
  <div class="split-media"><img src="assets/img/scr-limits.webp" alt="Brainrot daily limit including Instagram Reels" width="390" height="844" loading="lazy"></div></div>
  <div class="split flip reveal"><div><span class="split-num">HOW IT WORKS</span><h3>Count the Reels. Close the viewer at your limit.</h3>
  <ul class="ticks"><li>Set a number: 0 for a full Reels ban, or 10 to 30 for a light daily allowance</li><li>Open Instagram normally. Messages, Stories, profiles and posts are untouched</li><li>Every Reel you swipe past adds one to the counter</li><li>At the limit, the Reels viewer closes and a stop screen appears</li></ul>
  <div class="btn-row mt-2"><a class="btn btn-ink btn-sm" href="blog/instagram-reels-blocker-guide.html">Step-by-step guide</a></div></div>
  <div class="split-media"><img src="assets/img/scr-limit.webp" alt="Brainrot limit reached screen after the Reels cap" width="390" height="844" loading="lazy"></div></div>
</div></section>
<section class="section bg-white rule-top"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Good to know</span><h2>What it blocks, and what it doesn't.</h2></div><p>Being clear about this is the whole point of the app.</p></div>
  <div class="cards two">
   <div class="card"><span class="tag">Limited</span><h3>Reels</h3><p>The vertical Reels viewer, including Reels opened from the Reels tab, the home feed and search.</p></div>
   <div class="card"><span class="tag">Left alone</span><h3>Everything else</h3><p>Direct messages, group chats, Stories, profiles, regular photo and video posts, notes and search for people.</p></div>
  </div>
  <p class="table-note">Instagram changes its app often. If a layout change ever stops counting, update both apps and <a href="contact.html">let us know</a>.</p>
</div></section>'''
    out["instagram-reels-blocker.html"] = landing("instagram-reels-blocker.html",
        "Instagram Reels Blocker for Android | Brainrot",
        "Block or limit Instagram Reels on Android without deleting Instagram. Brainrot counts every Reel and closes the viewer at your limit. DMs stay open.",
        "Block Instagram Reels. Keep Instagram.", "Set a daily Reels limit, from zero to as many as you like. Brainrot closes the Reels viewer when you reach it, and leaves your messages, Stories and profile alone.",
        "Instagram Reels blocker", "instagram reels blocker, block instagram reels android, limit instagram reels, disable reels instagram, instagram reels limit app, reels time limit, stop watching reels",
        "scr-hud-sm.webp", insta, (5,1,7,3),
        [("How-to","Block Instagram Reels without deleting Instagram","blog/instagram-reels-blocker-guide.html"),("Habits","How to stop doomscrolling","blog/how-to-stop-doomscrolling.html"),("Product","YouTube Shorts blocker","youtube-shorts-blocker.html")],
        "Instagram Reels blocker")

    yt = '''
<section class="section"><div class="container">
  <div class="split reveal"><div><span class="split-num">THE PROBLEM</span><h3>You went to YouTube to learn. You left with 200 Shorts.</h3>
  <p>YouTube is one of the best free learning tools there is, and Shorts sit right next to it in the app. A regular timer can't tell a three-hour lecture from three hundred Shorts, so it either interrupts your learning or does nothing.</p></div>
  <div class="split-media"><img src="assets/img/scr-mascot.webp" alt="Brainrot brain mascot stage screen" width="390" height="844" loading="lazy"></div></div>
  <div class="split flip reveal"><div><span class="split-num">HOW IT WORKS</span><h3>Shorts are counted. Everything else isn't.</h3>
  <ul class="ticks"><li>Brainrot distinguishes the vertical Shorts player from regular horizontal videos</li><li>Long-form videos, live streams and music play with no counter and no timer</li><li>Every Short adds one to your daily count</li><li>At the limit, the Shorts feed closes and you can keep watching everything else</li></ul>
  <div class="btn-row mt-2"><a class="btn btn-ink btn-sm" href="blog/youtube-shorts-limiter-guide.html">Step-by-step guide</a></div></div>
  <div class="split-media"><img src="assets/img/scr-usage.webp" alt="Brainrot 7-day Shorts and Reels history" width="390" height="844" loading="lazy"></div></div>
</div></section>
<section class="section bg-white rule-top"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Pick a number</span><h2>Suggested YouTube Shorts limits.</h2></div><p>Starting points, not rules. Adjust to your own baseline.</p></div>
  <div class="cards">
   <div class="card"><span class="tag">Exam season</span><h3>0 per day</h3><p>A full Shorts ban while you study. Lectures and notes stay available.</p></div>
   <div class="card"><span class="tag">Everyday</span><h3>10–20 per day</h3><p>Enough for a short break, not enough to lose an evening.</p></div>
   <div class="card"><span class="tag">Unified mode</span><h3>30–50 shared</h3><p>One pool across YouTube, Instagram and the rest, so the habit can't just move apps.</p></div>
  </div>
</div></section>'''
    out["youtube-shorts-blocker.html"] = landing("youtube-shorts-blocker.html",
        "YouTube Shorts Blocker & Limiter for Android | Brainrot",
        "Limit or block YouTube Shorts on Android while still watching normal long videos. Brainrot counts every Short and closes the feed at your daily limit.",
        "Limit YouTube Shorts. Keep YouTube.", "Count and cap Shorts without touching lectures, tutorials, podcasts or music. A daily limit that closes the Shorts feed and leaves the rest of YouTube alone.",
        "YouTube Shorts blocker", "youtube shorts blocker, block youtube shorts android, limit youtube shorts, disable shorts, youtube shorts time limit, youtube shorts limiter app",
        "scr-limit-sm.webp", yt, (6,1,7,3),
        [("How-to","Limit YouTube Shorts and keep long videos","blog/youtube-shorts-limiter-guide.html"),("Product","Instagram Reels blocker","instagram-reels-blocker.html"),("Learn","What short-form video does to attention","blog/short-form-video-addiction-effects.html")],
        "YouTube Shorts blocker")

    sv = '''
<section class="section"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Every feed</span><h2>Four feeds. One limit.</h2></div><p>Block one feed and the habit usually moves to the next. That is why Brainrot counts them together if you want.</p></div>
  <div class="cards">
   <div class="card"><span class="tag">Instagram</span><h3>Reels</h3><p>Counts swipes in the Reels viewer. DMs and Stories stay open. <a href="instagram-reels-blocker.html" style="color:var(--blue-deep)">Details</a></p></div>
   <div class="card"><span class="tag">YouTube</span><h3>Shorts</h3><p>Counts Shorts only. Long videos play with no limit. <a href="youtube-shorts-blocker.html" style="color:var(--blue-deep)">Details</a></p></div>
   <div class="card"><span class="tag">Facebook</span><h3>Reels</h3><p>Stops the autoplay chain of vertical videos, while Messenger-style chats and groups stay usable.</p></div>
   <div class="card"><span class="tag">Snapchat</span><h3>Spotlight</h3><p>Caps the Spotlight feed. Chats, Snaps and Stories stay available.</p></div>
  </div>
</div></section>
<section class="section bg-white rule-top"><div class="container">
  <div class="split reveal"><div><span class="split-num">UNIFIED MODE</span><h3>Stop the whack-a-mole.</h3>
  <p>Cap Instagram alone and you'll find yourself on YouTube Shorts ten minutes later. In Unified mode every supported feed draws from one daily number, so 20 on Instagram plus 30 on YouTube uses up a 50-video limit.</p>
  <p class="mt-1">Prefer different rules per app? Individual mode lets you set 20 for Instagram, 10 for YouTube and 0 for Snapchat.</p></div>
  <div class="split-media"><img src="assets/img/scr-individual.webp" alt="Brainrot individual limits per app" width="390" height="844" loading="lazy"></div></div>
</div></section>'''
    out["short-video-blocker.html"] = landing("short-video-blocker.html",
        "Short Video Blocker for Android | Brainrot",
        "One limit for Instagram Reels, YouTube Shorts, Facebook Reels and Snapchat Spotlight. Brainrot is a short video blocker and limiter for Android.",
        "One limit for every short-video feed.", "Instagram Reels, YouTube Shorts, Facebook Reels and Snapchat Spotlight, counted together or separately. Set the rules once and let the app enforce them.",
        "Short video blocker", "short video blocker, block reels and shorts, facebook reels blocker, snapchat spotlight blocker, tiktok alternative limit, short form video limiter android, doomscrolling blocker",
        "scr-individual-sm.webp", sv, (4,8,7,12),
        [("Product","Instagram Reels blocker","instagram-reels-blocker.html"),("Product","YouTube Shorts blocker","youtube-shorts-blocker.html"),("Habits","How to stop doomscrolling","blog/how-to-stop-doomscrolling.html")],
        "Short video blocker")

    st = '''
<section class="section"><div class="container">
  <div class="section-head"><div><span class="eyebrow">What it controls</span><h2>Four ways to take control.</h2></div><p>Brainrot covers short-video feeds, other apps, timed sessions and schedules in one place.</p></div>
  <div class="feat-grid">
   <div class="feat">''' + icon("count") + '''<h3>Short-video limits</h3><p>Daily caps on Reels, Shorts, Facebook Reels and Spotlight, counted per video.</p></div>
   <div class="feat">''' + icon("grid") + '''<h3>App time limits</h3><p>A daily time limit for any installed app, for the ones that aren't short-video feeds.</p></div>
   <div class="feat">''' + icon("timer") + '''<h3>Focus sessions</h3><p>Start a timed session that blocks distractions and mutes notifications.</p></div>
   <div class="feat">''' + icon("calendar") + '''<h3>Schedules</h3><p>Recurring sessions for study hours, work blocks or a morning routine.</p></div>
   <div class="feat">''' + icon("phone") + '''<h3>Essential apps</h3><p>Phone, Messages and the apps you choose are always available, even mid-session.</p></div>
   <div class="feat">''' + icon("chart") + '''<h3>Progress tracking</h3><p>Focus time, completed sessions, success rate and a daily streak.</p></div>
  </div>
</div></section>
<section class="section bg-white rule-top"><div class="container">
  <div class="split reveal"><div><span class="split-num">FOCUS SESSIONS</span><h3>Plan once. Focus daily.</h3>
  <p>Set up a session like "Morning Study" or "Deep Work" once, choose the days and times, and Brainrot starts it on its own. During a session, distracting apps are blocked and only your essential apps stay available.</p>
  <ul class="ticks"><li>Quick timer presets</li><li>Recurring daily or weekday schedules</li><li>Emergency access for real emergencies</li></ul></div>
  <div class="split-media"><img src="assets/img/scr-schedule.webp" alt="Brainrot focus schedule screen" width="390" height="844" loading="lazy"></div></div>
  <div class="split flip reveal"><div><span class="split-num">ESSENTIAL APPS</span><h3>Block distractions. Keep the essentials.</h3>
  <p>An all-or-nothing blocker is one you'll uninstall the first time you need to take a call. Brainrot keeps Phone and Messages available and lets you add a few more, so a focus session never leaves you unreachable.</p></div>
  <div class="split-media"><img src="assets/img/scr-essentials.webp" alt="Brainrot essential apps screen" width="390" height="844" loading="lazy"></div></div>
</div></section>
<section class="section"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Compared with Digital Wellbeing</span><h2>Built-in tools are a good start.</h2></div><p>Android's Digital Wellbeing has app timers and a Focus mode, and needs no extra permission. Where it stops is inside the app: it can't count Reels, and it can't close just the feed. See the <a href="comparison.html" style="color:var(--blue-deep)">full comparison</a>.</p></div>
</div></section>'''
    out["screen-time-controller.html"] = landing("screen-time-controller.html",
        "Screen Time Controller for Android | Brainrot",
        "Control screen time on Android with app time limits, focus sessions, schedules and per-video Reels and Shorts limits. Free, private, no account.",
        "A screen time controller for Android that goes inside the app.", "App time limits, timed focus sessions and schedules, plus per-video limits on Reels and Shorts. One free app, no account, nothing leaves your phone.",
        "Screen time controller", "screen time controller android, screen time app android, app limit android, app blocker android, focus mode android, digital wellbeing alternative, limit app usage, phone usage limiter, screen time control",
        "scr-focus-sm.webp", st, (4,9,2,12),
        [("Guide","How to reduce screen time on Android","blog/how-to-reduce-screen-time-android.html"),("Compare","Brainrot vs Digital Wellbeing and app blockers","comparison.html"),("Learn","Best app blockers for Android","blog/best-app-blockers-android.html")],
        "Screen time controller")
    return out
