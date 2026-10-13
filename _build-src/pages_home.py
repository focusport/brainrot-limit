from lib import *
from faqdata import FAQ, render_faq

def home():
    r = ""
    faq6 = [FAQ[i] for i in (0, 1, 5, 6, 12, 13)]
    body = f'''
<section class="hero">
  <div class="container hero-grid">
    <div>
      <span class="eyebrow rise" style="--i:0">Reel limiter &amp; screen time controller · Android</span>
      <h1><span class="ln"><span>Scroll less.</span></span><span class="ln"><span style="--i:1"><em>Keep your phone.</em></span></span></h1>
      <p class="lede rise" style="--i:2">Brainrot counts every Reel, Short and Spotlight you watch and stops the feed when you hit your daily limit. Your DMs, calls and long videos stay exactly where they are.</p>
      <div class="btn-row rise" style="--i:3">{play_btn("btn btn-blue btn-lg","Get it on Google Play","hero")}<a class="btn btn-line" href="how-it-works.html">See how it works</a></div>
      <ul class="hero-facts rise" style="--i:4"><li>Free</li><li>No account</li><li>Works on-device</li></ul>
    </div>
    <div class="hero-shots rise" style="--i:2">
      <img data-parallax=".05" src="assets/img/scr-hud.webp" alt="Brainrot live counter showing 14 of 40 reels over a Reel on Android" width="390" height="844" fetchpriority="high">
      <img data-parallax=".11" src="assets/img/scr-limit.webp" alt="Brainrot limit reached screen: that's your limit for today" width="390" height="844">
      <div class="hud-chip" aria-hidden="true"><span class="dot"></span><div><b>14 / 40 reels</b><small>Instagram · 26 left today</small></div></div>
    </div>
  </div>
</section>

<div class="ticker" aria-label="Supported feeds"><div class="ticker-track"><ul><li><span>01</span>Instagram Reels</li><li><span>02</span>YouTube Shorts</li><li><span>03</span>Facebook Reels</li><li><span>04</span>Snapchat Spotlight</li><li><span>05</span>Any app, by time</li><li><span>06</span>No account</li><li><span>07</span>On-device</li></ul><ul aria-hidden="true"><li><span>01</span>Instagram Reels</li><li><span>02</span>YouTube Shorts</li><li><span>03</span>Facebook Reels</li><li><span>04</span>Snapchat Spotlight</li><li><span>05</span>Any app, by time</li><li><span>06</span>No account</li><li><span>07</span>On-device</li></ul></div></div>

<section class="lit" id="lit" aria-label="Why limits fail">
  <div class="lit-stick"><div class="lit-wrap"><span class="eyebrow">The problem</span>
  <p class="lit-text" id="litText">Most screen time limits lock the whole app. But you open Instagram to message a friend and YouTube to watch a lecture. It's the <b>endless vertical feed</b> inside them that eats your evening.</p></div></div>
</section>
<section class="night lit-meta"><div class="container"><div class="statement-meta">
  <div><b>Videos, not minutes</b><p>Swipe past fifty Reels and the counter says fifty, however fast you go.</p></div>
  <div><b>Only the feed closes</b><p>Chats, profiles, Stories and long videos carry on working as normal.</p></div>
  <div><b>No snooze button</b><p>Nothing to bargain with at 11pm, when you're tired and the next video is one swipe away.</p></div>
</div></div></section>

<section class="section night tools">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">Two tools, one app</span><h2>A reel limiter and a screen time controller.</h2></div>
    <p>Most people end up needing both: something for the feeds that are built to keep you swiping, and something that guards the hours you've set aside to get things done.</p></div>

    <div class="split reveal">
      <div>
        <span class="pill">Reel limiter</span>
        <h3>Cap the feed, not the app.</h3>
        <p>Set a daily number, one shared across every app or a separate one for each. A small counter floats over the feed while you watch, so the number never sneaks up on you.</p>
        <ul class="ticks">
          <li>Instagram Reels, YouTube Shorts, Facebook Reels, Snapchat Spotlight</li>
          <li>Shared "Unified" budget or per-app "Individual" limits</li>
          <li>Live counter and a 7-day history of your totals</li>
        </ul>
        <div class="btn-row mt-2"><a class="btn btn-ink btn-sm" href="features.html">All features</a><a class="btn btn-line btn-sm" href="instagram-reels-blocker.html">Instagram Reels blocker</a></div>
      </div>
      <div class="split-media glow g1"><img class="p3d" src="assets/img/scr-limits.webp" alt="Brainrot daily limit screen with Instagram, YouTube, Facebook and Snapchat" width="390" height="844" loading="lazy"></div>
    </div>

    <div class="split flip reveal">
      <div>
        <span class="pill">Screen time controller</span>
        <h3>Protect the hours that matter.</h3>
        <p>Start a timed focus session, or schedule them for study and work hours. Distracting apps are blocked, and only the essentials you pick, like Phone and Messages, stay available.</p>
        <ul class="ticks">
          <li>Focus timer with quick presets, from 15 minutes up</li>
          <li>Recurring schedules for mornings, classes or deep-work blocks</li>
          <li>Daily time limits for any app on your phone</li>
        </ul>
        <div class="btn-row mt-2"><a class="btn btn-ink btn-sm" href="screen-time-controller.html">Screen time controller</a><a class="btn btn-line btn-sm" href="students.html">For students</a></div>
      </div>
      <div class="split-media glow g2"><img class="p3d r" src="assets/img/scr-focus.webp" alt="Brainrot focus session with no-escape timer" width="390" height="844" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="section bg-white rule-top" id="try">
  <div class="container demo" id="demo" data-limit="8" data-base="assets/img/">
    <div class="demo-copy">
      <span class="eyebrow">Try it</span>
      <h2 style="margin:1rem 0 1.25rem">Feel the limit in ten seconds.</h2>
      <p class="lede">This is a demo with a limit of 8. Swipe up on the phone, or press the button. Watch the counter and the mascot, then see what happens at the end.</p>
      <ul class="ticks"><li>The counter goes up with every swipe</li><li>The mascot gets more tired as you go</li><li>At the limit the feed closes. No snooze button</li></ul>
      <div class="demo-actions" style="justify-content:flex-start"><button class="btn btn-ink" id="demoSwipe" type="button">Swipe to next reel</button></div>
      <p class="demo-note">Demo only. Nothing is tracked.</p>
    </div>
    <div class="demo-phone" aria-label="Interactive demo of the Brainrot limit">
      <div class="demo-screen">
        <div class="demo-reel" id="demoReel"><svg viewBox="0 0 300 600" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><circle cx="150" cy="330" r="62" fill="#ffd7a0" opacity=".9"/><path d="M0 400 Q70 340 150 380 T300 350 V600 H0z" fill="rgba(30,14,48,.8)"/><path d="M0 470 Q90 420 180 460 T300 440 V600 H0z" fill="rgba(16,8,30,.9)"/></svg></div>
        <div class="demo-top"><span>Reels</span><span>◎</span></div>
        <div class="demo-hud" id="demoHud"><img id="demoFace" src="assets/img/mascot-0.webp" alt=""><div><b id="demoCount">0</b><span> / 8</span><div class="bar"><i id="demoBar" style="width:0"></i></div></div><span id="demoLeft">8 left</span></div>
        <div class="demo-rail" aria-hidden="true"><span>♡</span><span>◌</span><span>➤</span></div>
        <div class="demo-cap"><b><i></i>slowmornings</b><span id="demoCap">Slow mornings, simple coffee</span></div>
        <div class="demo-hint" aria-hidden="true">Swipe up</div>
        <div class="demo-over" id="demoOver" role="status"><img src="assets/img/mascot-900.webp" alt="" width="170" height="145"><h3>That's your limit for today.</h3><p>Messages and long videos are still open. The feed opens again at midnight.</p><button class="btn btn-blue" id="demoReset" type="button">Reset demo</button></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">Setup</span><h2>Two minutes, three steps.</h2></div>
    <p>There's no account and nothing to configure except a number. Most people are done before their tea cools.</p></div>
    <div class="steps reveal">
      <div class="step"><h3>Install and open</h3><p>Get Brainrot: Reel Limit from Google Play. The first screen walks you through everything it needs.</p></div>
      <div class="step"><h3>Allow Accessibility</h3><p>This is how Android lets Brainrot see that a Reel or Short is open. It is used for counting swipes only. <a href="privacy.html" style="color:var(--blue-deep)">What it does and doesn't read →</a></p></div>
      <div class="step"><h3>Pick your limit</h3><p>Choose a shared daily budget or one per app. Start with a number slightly under your current average and lower it each week.</p></div>
    </div>
    <p class="mt-2"><a href="how-it-works.html" class="btn btn-line btn-sm">Full setup guide</a></p>
  </div>
</section>

<section class="section bg-white rule-top">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">What's inside</span><h2>What's in the app.</h2></div>
    <p>Built around one idea: the fewer decisions you have to make while tired, the better your limits hold.</p></div>
    <div class="feat-grid reveal">
      <div class="feat">{icon("count")}<h3>Per-video counting</h3><p>Counts each Reel, Short or Spotlight as you swipe, instead of guessing from minutes.</p></div>
      <div class="feat">{icon("layers")}<h3>Unified or individual</h3><p>One shared budget for every feed, or a separate cap for each app. Switch any time.</p></div>
      <div class="feat">{icon("hud")}<h3>Floating counter</h3><p>A small live number over the feed so you always know where you stand.</p></div>
      <div class="feat">{icon("grid")}<h3>App time limits</h3><p>Set a daily limit on any installed app, not just social media.</p></div>
      <div class="feat">{icon("timer")}<h3>Focus sessions</h3><p>Timed sessions that block distractions and keep only your essentials available.</p></div>
      <div class="feat">{icon("calendar")}<h3>Schedules</h3><p>Plan once. Focus sessions start on their own on the days and times you choose.</p></div>
      <div class="feat">{icon("chart")}<h3>Insights and streaks</h3><p>See 7 days of totals, daily averages and your focus streak at a glance.</p></div>
      <div class="feat">{icon("brain")}<h3>Brain mascot</h3><p>Eleven mascot states turn a daily count into something you can feel.</p></div>
      <div class="feat">{icon("shield")}<h3>Private by design</h3><p>No account, no ads, no uploads. Your data stays on your phone.</p></div>
    </div>
  </div>
</section>

<section class="section showcase" id="screens">
  <div class="container center"><span class="eyebrow">Inside the app</span><h2 style="margin:1rem auto .9rem;max-width:14em">A look at what <em class="serif">you'll see.</em></h2>
  <p class="lede" style="margin-inline:auto">Home shows today's count, Limits sets your rules, and Screen Time shows whether it's working. Drag or use the arrows.</p></div>
  <div class="sc-wrap"><ul class="sc-rail" id="scRail" tabindex="0" aria-label="App screens"><li class="sc-card" style="--tint:#3a1f6e"><h3>Count every <em class="serif">Reel</em></h3><img src="assets/img/scr-hud.webp" alt="Brainrot hud screen" width="390" height="844" loading="lazy"><div class="pills"><span>Live counter</span><span>Per video</span></div></li><li class="sc-card" style="--tint:#5a1d24"><h3>Hit your <em class="serif">limit</em></h3><img src="assets/img/scr-limit.webp" alt="Brainrot limit screen" width="390" height="844" loading="lazy"><div class="pills"><span>Hard stop</span><span>No snooze</span></div></li><li class="sc-card" style="--tint:#1d2a6e"><h3>Your daily <em class="serif">home</em></h3><img src="assets/img/scr-home.webp" alt="Brainrot home screen" width="390" height="844" loading="lazy"><div class="pills"><span>Count</span><span>Remaining</span></div></li><li class="sc-card" style="--tint:#2a1f6e"><h3>Set the <em class="serif">rules</em></h3><img src="assets/img/scr-limits.webp" alt="Brainrot limits screen" width="390" height="844" loading="lazy"><div class="pills"><span>Unified</span><span>Individual</span></div></li><li class="sc-card" style="--tint:#4a2a12"><h3>A limit per <em class="serif">app</em></h3><img src="assets/img/scr-individual.webp" alt="Brainrot individual screen" width="390" height="844" loading="lazy"><div class="pills"><span>Instagram</span><span>YouTube</span></div></li><li class="sc-card" style="--tint:#2c1f5a"><h3>Watch your <em class="serif">brain</em></h3><img src="assets/img/scr-mascot.webp" alt="Brainrot mascot screen" width="390" height="844" loading="lazy"><div class="pills"><span>11 mascot stages</span></div></li><li class="sc-card" style="--tint:#12384a"><h3>See the <em class="serif">trend</em></h3><img src="assets/img/scr-usage.webp" alt="Brainrot usage screen" width="390" height="844" loading="lazy"><div class="pills"><span>7-day history</span><span>Daily average</span></div></li><li class="sc-card" style="--tint:#241a5e"><h3>Deep <em class="serif">focus</em></h3><img src="assets/img/scr-focus.webp" alt="Brainrot focus screen" width="390" height="844" loading="lazy"><div class="pills"><span>No escape</span><span>Emergency access</span></div></li><li class="sc-card" style="--tint:#1b2f5e"><h3>Plan it <em class="serif">once</em></h3><img src="assets/img/scr-schedule.webp" alt="Brainrot schedule screen" width="390" height="844" loading="lazy"><div class="pills"><span>Recurring</span><span>Per day</span></div></li><li class="sc-card" style="--tint:#143a32"><h3>Keep the <em class="serif">essentials</em></h3><img src="assets/img/scr-essentials.webp" alt="Brainrot essentials screen" width="390" height="844" loading="lazy"><div class="pills"><span>Phone</span><span>Messages</span></div></li></ul>
  <div class="sc-nav container"><button type="button" class="sc-btn" id="scPrev" aria-label="Previous screen">←</button><button type="button" class="sc-btn" id="scNext" aria-label="Next screen">→</button></div></div>
</section>

<section class="section" id="mascot">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">Brain mascot</span><h2>Because a number is easy to ignore.</h2></div>
    <p>Numbers are easy to ignore. Drag the slider to see how the mascot changes across eleven stages, from 0 to 1000+ videos in a day.</p></div>
    <div class="sim reveal">
      <div class="sim-stage" aria-live="polite">
        <img id="mascotImg" src="assets/img/mascot-0.webp" data-base="assets/img/" alt="Brainrot brain mascot in the Fresh state" width="170" height="145">
        <span class="sim-badge" id="stageBadge">0 videos</span>
        <div class="sim-name" id="stageName">Fresh</div>
        <div class="sim-sub" id="stageSub">Sharp and ready to focus</div>
      </div>
      <div class="sim-ctrl">
        <div>
          <div class="row-between"><label class="label" for="reelSlider">Short videos watched in a day</label><span class="value" id="reelVal">0</span></div>
          <input type="range" id="reelSlider" min="0" max="1000" step="50" value="0">
        </div>
        <div>
          <p class="label" style="margin-bottom:.7rem">Jump to stage</p>
          <div class="chips">{"".join(f'<button type="button" class="chip{" active" if v==0 else ""}" data-val="{v}">{v if v<1000 else "1000+"}</button>' for v in (0,50,100,250,400,500,600,700,800,900,1000))}</div>
        </div>
        <p class="sim-quote" id="stageQuote">Zero videos. Attention is intact and starting a hard task takes no extra effort.</p>
      </div>
    </div>
  </div>
</section>

<section class="section night" id="calculator">
  <div class="container calc">
    <div>
      <span class="eyebrow">The real cost</span>
      <h2 style="margin:1rem 0 1.25rem">How much of your year is going into the feed?</h2>
      <p>Short-form feeds are built so that 90 minutes feels like 10. Move the slider to your daily short-video time and see what a year adds up to.</p>
      <div style="margin-top:2.25rem">
        <div class="row-between"><label class="label" for="calcMinutes">Daily short-video time</label><span class="value" id="calcVal">90 min</span></div>
        <input type="range" id="calcMinutes" min="15" max="360" step="15" value="90">
      </div>
      <p class="calc-note">"Time reclaimed" assumes a limit cuts your feed time in half. It's a rough illustration, not a guarantee. Your result depends on the limit you set.</p>
    </div>
    <div class="calc-stats" aria-live="polite">
      <div class="calc-stat"><b id="cHours">548 hrs</b><span>per year</span></div>
      <div class="calc-stat"><b id="cDays">22.8 days</b><span>of non-stop scrolling</span></div>
      <div class="calc-stat"><b id="cBooks">78 books</b><span>at about 7 hours each</span></div>
      <div class="calc-stat hl"><b id="cSaved">274 hrs</b><span>reclaimed if you halve it</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">Compared</span><h2>Why timers alone don't hold.</h2></div>
    <p>A timer asks you to give up the whole app. Brainrot only asks you to give up the feed, which is a much easier deal to stick to.</p></div>
    <div class="table-wrap reveal"><table class="compare">
      <caption class="sr-only">Brainrot compared with built-in app timers</caption>
      <thead><tr><th scope="col"></th><th class="us" scope="col">Brainrot</th><th scope="col">Built-in app timers</th></tr></thead>
      <tbody>
        <tr><th scope="row">Counts each Reel / Short</th><td class="us yes">Yes, per video</td><td class="no">No, minutes in app only</td></tr>
        <tr><th scope="row">DMs and tutorials stay usable at the limit</th><td class="us yes">Yes, only the feed closes</td><td class="no">No, the whole app is locked</td></tr>
        <tr><th scope="row">One shared budget across apps</th><td class="us yes">Yes (Unified mode)</td><td class="no">No, one timer per app</td></tr>
        <tr><th scope="row">Live counter while you scroll</th><td class="us yes">Yes</td><td class="no">No</td></tr>
        <tr><th scope="row">Needs Accessibility permission</th><td class="us">Yes, used only to detect swipes</td><td>No</td></tr>
      </tbody></table></div>
    <p class="mt-2"><a class="btn btn-line btn-sm" href="comparison.html">Full comparison</a></p>
  </div>
</section>

<section class="section bg-white rule-top">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">Who it's for</span><h2>Built for people with something to do.</h2></div>
    <p>If you've ever opened your phone for one message and looked up forty minutes later, this was built for you.</p></div>
    <div class="cards reveal">
      <a class="card" href="students.html"><span class="tag">Students</span><h3>Study without the rabbit hole.</h3><p>Keep lectures and study-group chats. Close the Shorts and Reels that eat the evening before an exam.</p><span class="more">For students</span></a>
      <a class="card" href="professionals.html"><span class="tag">Professionals</span><h3>Protect your deep work.</h3><p>Phone breaks that actually stay breaks, plus scheduled focus sessions for your best hours.</p><span class="more">For professionals</span></a>
      <a class="card" href="blog/adhd-screen-time-management.html"><span class="tag">ADHD &amp; focus</span><h3>Limits that don't rely on memory.</h3><p>Rules set in advance, enforced automatically, with no negotiating at 11pm.</p><span class="more">Read the guide</span></a>
    </div>
  </div>
</section>

<section class="section night">
  <div class="container privacy-block">
    <div>
      <span class="eyebrow">Privacy</span>
      <h2 style="margin:1rem 0 1.25rem">Your scrolling is your business.</h2>
      <p>Brainrot needs the Accessibility Service to count swipes, and we think you deserve a plain explanation of what that means.</p>
      <p class="mt-1"><a class="btn btn-line btn-sm" href="privacy.html">Read the privacy policy</a></p>
    </div>
    <dl class="dl">
      <div><dt>It reads</dt><dd>Whether a Reel, Short or Spotlight screen is open, and when you swipe to the next one.</dd></div>
      <div><dt>It never reads</dt><dd>Messages, passwords, what you type, search queries or your watch history.</dd></div>
      <div><dt>It stores</dt><dd>Your limits and daily counts, on your phone only.</dd></div>
      <div><dt>It sends</dt><dd>Nothing. No account, no ads, no analytics, no uploads.</dd></div>
    </dl>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">Questions</span><h2>Quick answers.</h2></div>
    <p>The short version of what people ask before installing. The full list is on the <a href="faq.html" style="color:var(--blue-deep)">FAQ page</a>.</p></div>
    <div class="faq-list">{render_faq(faq6)}</div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">From the blog</span><h2>Read before you scroll.</h2></div><p>Practical guides on doomscrolling, attention and Android screen time.</p></div>
    <div class="cards reveal">
      <a class="card" href="blog/how-to-stop-doomscrolling.html"><span class="tag">Habits</span><h3>How to stop doomscrolling</h3><p>Seven tactics that work with your brain instead of against it.</p><span class="more">Read</span></a>
      <a class="card" href="blog/how-to-reduce-screen-time-android.html"><span class="tag">How-to</span><h3>How to reduce screen time on Android</h3><p>The built-in tools, their limits, and a setup that sticks.</p><span class="more">Read</span></a>
      <a class="card" href="blog/instagram-reels-blocker-guide.html"><span class="tag">How-to</span><h3>Block Instagram Reels without deleting Instagram</h3><p>Keep the messages. Lose the infinite scroll.</p><span class="more">Read</span></a>
    </div>
  </div>
</section>
{cta_band(r)}
'''
    schema = [APP, {"@type": "WebPage", "@id": SITE + "/#webpage", "url": SITE + "/", "name": "Brainrot: Reel Limiter & Screen Time App for Android",
                    "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + "/#app"}, "primaryImageOfPage": {"@type": "ImageObject", "url": OG_IMAGE}}]
    return page("index.html",
        "Brainrot: Reel Limiter & Screen Time App for Android",
        "Count and cap Instagram Reels, YouTube Shorts, Facebook Reels and Snapchat Spotlight on Android. Stop doomscrolling, keep your DMs. Free and private.",
        body, root=r, current="index.html", schema=schema,
        keywords="brainrot, brainrot app, stop brainrot, brain rot app, brainrot reel limit, reel limiter, reels blocker android, block instagram reels, youtube shorts blocker, stop doomscrolling app, screen time controller android, short video limit, app limit android, digital wellbeing app, focus app android, Brainrot")
