from lib import *
from faqdata import FAQ, CATS, render_faq

def students():
    r = ""
    body = page_head(r, [("Home","index.html"),("For students",None)], "For students",
        "Study without the Reel rabbit hole.",
        "You open YouTube for a ten-minute physics lecture and look up two hours later. Brainrot closes the Shorts and Reels feeds while your lectures, notes and study-group chats stay exactly as they are.", media="scr-schedule-sm.webp") + f'''
<section class="section"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Why it works for study</span><h2>Block the feed, keep the tools.</h2></div><p>Students need their phones: for lectures, group chats, doubt-clearing and flashcards. A blunt app lock doesn't survive the first group-project message.</p></div>
  <div class="cards">
   <div class="card"><span class="tag">Group chats</span><h3>Study messages stay open.</h3><p>Reply to your project partners on Instagram or Snapchat. Only the Reels and Spotlight feeds are limited.</p></div>
   <div class="card"><span class="tag">Lectures</span><h3>Full-length videos untouched.</h3><p>Watch a two-hour organic chemistry or coding lecture with no timer. Only Shorts count toward your limit.</p></div>
   <div class="card"><span class="tag">Focus blocks</span><h3>Schedule your study hours.</h3><p>Set a recurring focus session for 6–9pm. Distracting apps are blocked, Phone and Messages stay on.</p></div>
  </div>
</div></section>
<section class="section bg-white rule-top"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Exam-season setup</span><h2>A study-week setup that holds.</h2></div><p>Takes about three minutes.</p></div>
  <div class="steps"><div class="step"><h3>Shorts &amp; Reels to 0</h3><p>In Individual mode, set Instagram, YouTube and Snapchat to 0 for exam week. Add a small allowance back afterwards.</p></div>
  <div class="step"><h3>Schedule study blocks</h3><p>Create a focus session for each study window, e.g. weekdays 6–9pm and Sunday 10am–1pm.</p></div>
  <div class="step"><h3>Pick your essentials</h3><p>Keep Phone, Messages and your note-taking or lecture app available. Everything else waits.</p></div></div>
  <div class="prose-wide prose mt-3"><p>For the thinking behind it, read <a href="blog/why-willpower-fails-against-algorithms.html">why willpower fails against algorithms</a> and <a href="blog/how-to-reduce-screen-time-android.html">how to reduce screen time on Android</a>.</p></div>
</div></section>
{cta_band(r,"Make this exam season quieter.","Free on Google Play. Takes about two minutes to set up.")}'''
    return page("students.html", "Brainrot for Students: Block Reels & Shorts While You Study",
        "A study-friendly Reels and Shorts blocker for Android. Keep lectures and group chats, close the feeds that eat your evenings. Free, private.",
        body, root=r, current="", schema=[APP, breadcrumb([("Home","/"),("For students","/students.html")])],
        keywords="study app android, block reels while studying, student focus app, exam focus app, block youtube shorts study, study mode android, reduce phone distraction students")

def professionals():
    r = ""
    body = page_head(r, [("Home","index.html"),("For professionals",None)], "For professionals",
        "Protect deep work from the micro-break.",
        "A thirty-second check of a feed rarely costs thirty seconds. Research on interruptions suggests it can take well over twenty minutes to get fully back into demanding work. Brainrot keeps the phone break a break.", media="scr-hud-sm.webp") + f'''
<section class="section"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Why it works for work</span><h2>You keep your phone. You lose the loop.</h2></div><p>Messages, calendar, banking and maps still work. The one thing that goes is the part designed to be hard to leave.</p></div>
  <div class="cards">
   <div class="card"><span class="tag">Between tasks</span><h3>Breaks with an end.</h3><p>During a build, a render or a long meeting prep, a small daily allowance gives you the break without the rabbit hole.</p></div>
   <div class="card"><span class="tag">Deep-work blocks</span><h3>Scheduled focus sessions.</h3><p>Schedule 90-minute blocks. Distracting apps are blocked, and Phone and Messages stay available for real interruptions.</p></div>
   <div class="card"><span class="tag">Privacy</span><h3>Nothing leaves the device.</h3><p>No account, no cloud sync and no analytics. Safe to run on a personal phone you also use for work.</p></div>
  </div>
</div></section>
<section class="section bg-white rule-top"><div class="container">
  <div class="split reveal"><div><span class="split-num">A WORKDAY SETUP</span><h3>Three settings that cover most of it.</h3>
  <ul class="ticks"><li><strong>Unified limit of 30</strong> short videos a day across every feed</li><li><strong>Focus schedule</strong> for your two best deep-work windows</li><li><strong>App limits</strong> of 20–30 minutes on news or shopping apps that fill the gaps</li></ul>
  <div class="btn-row mt-2"><a class="btn btn-ink btn-sm" href="screen-time-controller.html">Screen time controller</a></div></div>
  <div class="split-media"><img src="assets/img/scr-schedule.webp" alt="Brainrot focus schedule with recurring sessions" width="390" height="844" loading="lazy"></div></div>
</div></section>
{cta_band(r,"Give your best hours back.","Free on Google Play. No account, nothing uploaded.")}'''
    return page("professionals.html", "Brainrot for Professionals: Protect Deep Work on Android",
        "Cut micro-distractions with a Reels and Shorts limiter and scheduled focus sessions for Android. Keep messages and calls. Free and private.",
        body, root=r, current="", schema=[APP, breadcrumb([("Home","/"),("For professionals","/professionals.html")])],
        keywords="deep work app android, focus app for work, productivity app android, block reels at work, stop phone distractions, focus sessions schedule, digital minimalism app")

def comparison():
    r = ""
    rows = [
     ("Counts individual Reels / Shorts", "Yes", "No, app minutes only", "No, app minutes only"),
     ("Keeps DMs and long videos usable at the limit", "Yes, only the feed closes", "No, the whole app locks", "No, the whole app locks"),
     ("One shared budget across several apps", "Yes (Unified mode)", "No", "Sometimes, by app group"),
     ("Live counter over the feed", "Yes", "No", "No"),
     ("Time limits for any app", "Yes", "Yes", "Yes"),
     ("Focus sessions and schedules", "Yes", "Yes (Focus mode, Bedtime mode)", "Yes"),
     ("Account or cloud sync required", "No", "No", "Varies by app"),
     ("Special permission needed", "Accessibility Service", "None, built into Android", "Usually Accessibility or Usage Access"),
    ]
    def cell(v, cls=""):
        k = "yes" if v.startswith("Yes") else ("no" if v.startswith("No") else "")
        return f'<td class="{cls} {k}">{v}</td>'
    trs = "".join(f'<tr><th scope="row">{a}</th>{cell(b,"us")}{cell(c)}{cell(d)}</tr>' for a,b,c,d in rows)
    body = page_head(r, [("Home","index.html"),("Compare",None)], "Comparison",
        "Brainrot vs Digital Wellbeing and typical app blockers.",
        "Built-in tools and classic blockers solve a slightly different problem. Where each one works, where it stops, and when it makes sense to use more than one.", ctas=False) + f'''
<section class="section"><div class="container">
  <div class="table-wrap"><table class="compare">
    <caption class="sr-only">Feature comparison</caption>
    <thead><tr><th scope="col">Capability</th><th class="us" scope="col">Brainrot</th><th scope="col">Android Digital Wellbeing</th><th scope="col">Typical app blockers</th></tr></thead>
    <tbody>{trs}</tbody></table></div>
  <p class="table-note">Comparison reflects general behaviour of each category at time of writing. Features of third-party apps vary and change. Check the current version of any app you are considering.</p>
</div></section>
<section class="section bg-white rule-top"><div class="container">
  <div class="section-head"><div><span class="eyebrow">When to use what</span><h2>Honest advice.</h2></div><p>You don't have to pick only one. Many people use two.</p></div>
  <div class="cards">
   <div class="card"><span class="tag">Digital Wellbeing</span><h3>Good for broad limits.</h3><p>Free, built in, and requires no extra permission. It is a sensible first step for app timers, Bedtime mode and notification control.</p></div>
   <div class="card"><span class="tag">Classic blockers</span><h3>Good for hard app bans.</h3><p>If you want an entire app unavailable during certain hours, a full-app blocker does exactly that.</p></div>
   <div class="card"><span class="tag">Brainrot</span><h3>Good when the feed is the problem.</h3><p>If you need Instagram for messages or YouTube for learning but can't stop the Reels and Shorts, per-video limits are the missing piece.</p></div>
  </div>
</div></section>
<section class="section"><div class="container prose-wide prose">
  <h2 id="why">Why per-video beats per-minute</h2>
  <p>Time-based limits measure how long you were in an app. They can't tell reading a message from watching forty Reels. When the limit fires, it fires on everything, and you override it for a legitimate reason. Once overridden, the feed is right there.</p>
  <p>Counting videos targets the behaviour itself, which is also easier to see: "I watched 38 Reels" is harder to rationalise than "I was on Instagram for 41 minutes".</p>
  <h2 id="paid">Free reel limiter vs paid app blockers</h2>
  <p>Many paid blockers charge a subscription and work by locking a whole app or a time window. Brainrot is free, needs no account, and limits only the Reels, Shorts and Spotlight feed, so messages and long videos keep working. A paid app can still be the better fit if you need iPhone support, cross-device sync or a different kind of lock. Apps such as BrainPal count reels too, but list blocking at the limit as a Pro feature (about ₹99 a month, or about ₹83 a month on the yearly plan, at the time of writing). Check each app's current price and features before you decide.</p>
  <p>Further reading: <a href="blog/best-app-blockers-android.html">how to choose an app blocker for Android</a> and <a href="blog/how-to-reduce-screen-time-android.html">how to reduce screen time on Android</a>.</p>
</div></section>
{cta_band(r)}'''
    return page("comparison.html", "Brainrot vs Digital Wellbeing & App Blockers: Comparison",
        "Compare Brainrot with Android Digital Wellbeing and typical app blockers: per-video limits, shared budgets, focus sessions, permissions and privacy.",
        body, root=r, current="comparison.html", schema=[APP, breadcrumb([("Home","/"),("Compare","/comparison.html")])],
        keywords="digital wellbeing alternative, best app blocker android, focusport vs digital wellbeing, app blocker comparison, screen time apps compared, reels blocker comparison")

def faq():
    r = ""
    pills = '<button type="button" class="chip active" data-cat="all">All</button>' + "".join(f'<button type="button" class="chip" data-cat="{k}">{v}</button>' for k, v in CATS)
    body = page_head(r, [("Home","index.html"),("FAQ",None)], "FAQ",
        "Frequently asked questions.",
        "Everything people ask about reel counting, limits, permissions, privacy and battery. Can't find your answer? Ask us.", ctas=False) + f'''
<section class="section"><div class="container narrow" style="width:min(100% - 2*var(--gutter),860px)">
  <div class="faq-tools"><input class="faq-search" id="faqSearch" type="search" placeholder="Search questions…" aria-label="Search questions"><div class="chips">{pills}</div></div>
  <div class="faq-list" id="faqList">{render_faq(FAQ, with_groups=True)}</div>
  <p class="faq-empty" id="faqEmpty">No matching questions. <a href="contact.html" style="color:var(--blue-deep)">Ask us directly →</a></p>
  <div class="callout mt-3"><strong>Still stuck?</strong>Email <a href="mailto:{EMAIL}" style="color:var(--blue-deep)">{EMAIL}</a> or use the <a href="contact.html" style="color:var(--blue-deep)">contact page</a>. Include your phone model and Android version if something isn't counting.</div>
</div></section>
{cta_band(r)}'''
    return page("faq.html", "FAQ: Reel Limits, Permissions, Privacy & Battery | Brainrot",
        "Answers about Brainrot: how Reels and Shorts counting works, why Accessibility is needed, battery use, privacy, supported apps and focus sessions.",
        body, root=r, current="faq.html",
        schema=[APP, breadcrumb([("Home","/"),("FAQ","/faq.html")]), faq_schema([(q, p) for _, q, _, p in FAQ])],
        keywords="focusport faq, reel limiter faq, accessibility permission reel blocker, does reel blocker drain battery, is focusport safe, block reels android questions")

def about():
    r = ""
    body = page_head(r, [("Home","index.html"),("About",None)], "About Brainrot",
        "Attention is the thing worth protecting.",
        "We build tools that give you control over your own attention without making you give up the parts of your phone that make life easier.", ctas=False) + f'''
<section class="section"><div class="container prose-wide prose">
  <h2 style="margin-top:0">Why we built it</h2>
  <p>Every screen time tool we tried had the same flaw: it punished the whole app. Set a 30-minute timer on Instagram and it also locks the DMs you need to answer. Set one on YouTube and it cuts off the lecture you are halfway through. So you tap "ignore limit", and the moment you do, the feed is one swipe away.</p>
  <p>The problem was never the app. It was one specific, endless, algorithmic scroll inside it. Brainrot was built to recognise that scroll and limit only that.</p>
  <p>Brainrot: Reel Limit was previously known as FocusPort Limit. Same app, same team, a name that says what it fights.</p>
  <h2>What we believe</h2>
  <ul>
    <li><strong>Rules beat willpower.</strong> A decision made in the morning is more reliable than one made at 11pm.</li>
    <li><strong>Targeted beats total.</strong> Limits last when they don't get in the way of real life.</li>
    <li><strong>Your data is yours.</strong> A tool about your attention shouldn't be harvesting it.</li>
    <li><strong>Encouragement over guilt.</strong> A small mascot is a gentler nudge than a red warning.</li>
  </ul>
  <h2>What we won't do</h2>
  <ul><li>Sell or share your usage data</li><li>Show ads inside the app</li><li>Require an account</li><li>Read your messages or what you type</li></ul>
  <h2>A note on honesty</h2>
  <p>Brainrot is a self-control tool. It isn't a medical product and doesn't diagnose or treat anything. If screen use is affecting your sleep, mood or relationships, talking to a doctor or counsellor is worth doing alongside any app.</p>
</div></section>
{cta_band(r,"Try it for a week.","Free on Google Play. If it isn't for you, uninstalling removes everything.")}'''
    return page("about.html", "About Brainrot: Why We Built a Better Reel Limiter",
        "Brainrot limits only the short-video feed, not your whole app. Read why we built it, what we believe and what we will never do with your data.",
        body, root=r, current="", schema=[{"@type":"AboutPage","url":SITE+"/about.html","name":"About Brainrot"}, breadcrumb([("Home","/"),("About","/about.html")])],
        keywords="about focusport, digital wellbeing app, why reel limiter, focusport team, private screen time app")

def contact():
    r = ""
    topics = ["Help with setup or permissions","Something isn't counting / an app changed","Feature request","Press or partnership","General feedback"]
    opts = "".join(f"<option>{t}</option>" for t in topics)
    body = page_head(r, [("Home","index.html"),("Contact",None)], "Contact",
        "Talk to us.",
        "A question, a bug, an app that changed its layout, or an idea. We read every message.", ctas=False) + f'''
<section class="section"><div class="container contact-grid">
  <form class="form" id="contactForm" novalidate>
    <div class="success" id="formSuccess" role="status">Your email app should have opened with the message ready to send. If it didn't, email {EMAIL} directly.</div>
    <div class="field"><label for="name">Your name</label><input id="name" name="name" type="text" autocomplete="name" required></div>
    <div class="field"><label for="email">Email address</label><input id="email" name="email" type="email" autocomplete="email" required></div>
    <div class="field"><label for="topic">Topic</label><select id="topic" name="topic">{opts}</select></div>
    <div class="field"><label for="message">Message</label><textarea id="message" name="message" required placeholder="If something isn't counting, please include your phone model, Android version and the app involved."></textarea></div>
    <button class="btn btn-blue" type="submit">Send message</button>
    <p class="form-note">This opens your email app with the message filled in, so nothing is stored on this website.</p>
  </form>
  <aside>
    <dl class="dl paper-dl">
      <div><dt>Support</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
      <div><dt>Privacy</dt><dd><a href="mailto:{PRIVACY_EMAIL}">{PRIVACY_EMAIL}</a></dd></div>
      <div><dt>Quick answers</dt><dd><a href="faq.html">FAQ</a> · <a href="how-it-works.html">Setup guide</a></dd></div>
      <div><dt>Reviews</dt><dd>Enjoying Brainrot? A rating on <a href="{PLAY}" target="_blank" rel="noopener">Google Play</a> helps others find it.</dd></div>
    </dl>
  </aside>
</div></section>'''
    return page("contact.html", "Contact Brainrot: Support, Feedback & Partnerships",
        "Get help with Brainrot setup, report a detection issue after an app update, suggest a feature or reach us about press and partnerships.",
        body, root=r, current="", schema=[{"@type":"ContactPage","url":SITE+"/contact.html","name":"Contact Brainrot"}, breadcrumb([("Home","/"),("Contact","/contact.html")])],
        keywords="focusport support, contact focusport, report bug reel blocker, feature request screen time app")

def privacy():
    r = ""
    body = page_head(r, [("Home","index.html"),("Privacy",None)], "Legal",
        "Privacy policy.", "Last updated: October 11, 2026. The short version: Brainrot works on your device and doesn't send your data anywhere.", ctas=False) + f'''
<section class="section"><div class="container prose-wide prose">
  <h2 style="margin-top:0">1. Summary</h2>
  <p>Brainrot: Reel Limit processes everything on your device. We don't run user accounts, we don't upload your usage data, and we don't include advertising or third-party analytics SDKs in the app.</p>
  <h2>2. Use of the Android Accessibility Service</h2>
  <p>Brainrot uses Android's AccessibilityService API for one purpose: to detect when a short-video screen (Instagram Reels, YouTube Shorts, Facebook Reels, Snapchat Spotlight) is open and when you swipe to the next video, so it can count videos and enforce your limits. It is also used to detect which app is in the foreground, so app time limits and focus sessions can work.</p>
  <ul>
    <li><strong>What it observes:</strong> the name of the foreground app and screen, and swipe or scroll events within supported short-video feeds.</li>
    <li><strong>What it does not do:</strong> it does not read, record or store messages, passwords, payment details, search queries or text you type.</li>
    <li><strong>Where it is processed:</strong> in memory on your device. Events are discarded after updating your local counters.</li>
  </ul>
  <p>You can turn the permission off at any time in Android Settings → Accessibility. Limits will stop working while it is off.</p>
  <h2>3. Other permissions</h2>
  <p>"Display over other apps" is used only to show the floating counter. Notification and battery-related settings are used to keep the app running reliably and to show limit alerts.</p>
  <h2>4. Data stored on your device</h2>
  <ul><li>Your limits and settings</li><li>Daily video counts and app usage totals, and a short history for your 7-day charts</li><li>Focus-session schedules and progress (streaks, completed sessions)</li><li>Your current mascot stage</li></ul>
  <p>This data stays in the app's private storage. It is deleted when you uninstall the app or clear its storage in Android Settings.</p>
  <h2>5. Sharing</h2>
  <p>We do not sell, rent or share your data with advertisers, data brokers or any third party. The app does not require an internet connection to work.</p>
  <h2>6. Website</h2>
  <p>This website is a static site. It doesn't use advertising cookies. The contact form opens your email app and doesn't store your message on the site. Fonts are loaded from Google Fonts, which may receive your IP address as part of the request. If we add analytics later, we will update this page and prefer privacy-friendly tools.</p>
  <h2>7. Children</h2>
  <p>Brainrot is a self-management tool and is not directed at children under 13. We do not knowingly collect personal information from anyone.</p>
  <h2>8. Changes</h2>
  <p>If we change this policy we'll update the date above. Material changes will be flagged on this page and in the app.</p>
  <h2>9. Contact</h2>
  <p>Questions about privacy: <a href="mailto:{PRIVACY_EMAIL}">{PRIVACY_EMAIL}</a>.</p>
</div></section>'''
    return page("privacy.html", "Privacy Policy | Brainrot",
        "Brainrot processes everything on your device. Read exactly how the Android Accessibility Service is used, what is stored locally and what is never collected.",
        body, root=r, current="", schema=[breadcrumb([("Home","/"),("Privacy","/privacy.html")])],
        keywords="focusport privacy policy, accessibility service privacy, on-device screen time app")

def terms():
    r = ""
    body = page_head(r, [("Home","index.html"),("Terms",None)], "Legal",
        "Terms of service.", "Last updated: October 11, 2026.", ctas=False) + f'''
<section class="section"><div class="container prose-wide prose">
  <h2 style="margin-top:0">1. Acceptance</h2>
  <p>By downloading, installing or using Brainrot: Reel Limit or this website, you agree to these terms. If you don't agree, please don't use them.</p>
  <h2>2. Licence</h2>
  <p>We grant you a personal, non-exclusive, non-transferable, revocable licence to use the app for your own productivity and digital wellbeing.</p>
  <h2>3. Acceptable use</h2>
  <p>Don't reverse engineer, resell or redistribute the app, and don't use it to monitor another person without their knowledge and consent.</p>
  <h2>4. Third-party apps</h2>
  <p>Brainrot works alongside third-party apps such as Instagram, YouTube, Facebook and Snapchat. We are not affiliated with or endorsed by them. Those apps can change at any time, which may affect how reliably Brainrot detects short-video feeds. We aim to update quickly but can't guarantee uninterrupted detection.</p>
  <h2>5. Not medical advice</h2>
  <p>Brainrot is a self-control tool. It is not a medical device and doesn't diagnose, treat or prevent any condition. Content on this website is for general information only.</p>
  <h2>6. Disclaimer</h2>
  <p>The app and website are provided "as is" and "as available" without warranties of any kind, to the extent permitted by law.</p>
  <h2>7. Limitation of liability</h2>
  <p>To the extent permitted by law, Brainrot and its developers are not liable for indirect, incidental or consequential damages arising from use of the app or website.</p>
  <h2>8. Changes</h2>
  <p>We may update these terms. Continued use after an update means you accept the new terms.</p>
  <h2>9. Contact</h2>
  <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></section>'''
    return page("terms.html", "Terms of Service | Brainrot",
        "The terms for using the Brainrot: Reel Limit Android app and the focusport.in website.",
        body, root=r, current="", schema=[breadcrumb([("Home","/"),("Terms","/terms.html")])])

def notfound():
    r = ""
    body = f'''<section class="nf"><div class="container"><h1>404</h1><p class="lede" style="margin:1rem auto 2rem">That page has scrolled out of view.</p>
<div class="btn-row" style="justify-content:center"><a class="btn btn-ink" href="/index.html">Back to home</a><a class="btn btn-line" href="/blog/">Read the blog</a></div></div></section>'''
    # absolute asset paths so the 404 works at any depth
    html_ = page("404.html", "Page not found | Brainrot", "This page doesn't exist.", body, root="/", current="", noindex=True)
    return html_
