# (category, question, answer_html, answer_plain)
FAQ = [
 ("general","What is Brainrot?",
  "<p>Brainrot (the app is called <strong>Brainrot: Reel Limit</strong>) is a free Android app that counts the short videos you watch and stops the feed when you reach your daily limit. It also lets you set time limits on any app and run timed focus sessions. Your messages, calls and long-form videos are left alone.</p>",
  "Brainrot (the app is called Brainrot: Reel Limit) is a free Android app that counts the short videos you watch and stops the feed when you reach your daily limit. It also lets you set time limits on any app and run timed focus sessions. Your messages, calls and long-form videos are left alone."),
 ("general","How is Brainrot different from a normal app blocker or Digital Wellbeing?",
  "<p>Normal app timers lock the whole app, including the parts you need, like Instagram DMs or YouTube tutorials. That is why people end up tapping \"ignore limit\" and going straight back to the feed. Brainrot counts and limits only the vertical short-video feed, so the rest of the app keeps working.</p>",
  "Normal app timers lock the whole app, including the parts you need, like Instagram DMs or YouTube tutorials. That is why people end up tapping ignore limit and going straight back to the feed. Brainrot counts and limits only the vertical short-video feed, so the rest of the app keeps working."),
 ("general","Is Brainrot free?",
  "<p>Yes. Brainrot: Reel Limit is free to install from Google Play and there is no account to create.</p>",
  "Yes. Brainrot: Reel Limit is free to install from Google Play and there is no account to create."),
 ("general","Does it work on iPhone?",
  "<p>Not at the moment. Brainrot relies on Android's Accessibility Service, which is what makes per-video counting possible. iOS does not offer an equivalent, so the app is Android-only.</p>",
  "Not at the moment. Brainrot relies on Android's Accessibility Service, which is what makes per-video counting possible. iOS does not offer an equivalent, so the app is Android-only."),
 ("platforms","Which apps can Brainrot limit?",
  "<p>Instagram Reels, YouTube Shorts, Facebook Reels and Snapchat Spotlight. On top of that, the app-limits feature lets you set a daily time limit on any app installed on your phone.</p>",
  "Instagram Reels, YouTube Shorts, Facebook Reels and Snapchat Spotlight. On top of that, the app-limits feature lets you set a daily time limit on any app installed on your phone."),
 ("platforms","Can I block Instagram Reels but keep Instagram DMs?",
  "<p>Yes, that is the main use case. Brainrot counts videos in the Reels viewer. Direct messages, your profile, Stories and the regular feed stay open. When you hit your limit, only the Reels feed is closed. See the <a href=\"instagram-reels-blocker.html\">Instagram Reels blocker page</a> for the details.</p>",
  "Yes, that is the main use case. Brainrot counts videos in the Reels viewer. Direct messages, your profile, Stories and the regular feed stay open. When you hit your limit, only the Reels feed is closed."),
 ("platforms","Can I limit YouTube Shorts but still watch normal YouTube videos?",
  "<p>Yes. Brainrot tells vertical Shorts apart from regular horizontal videos. Lectures, tutorials, podcasts and music keep playing without a counter. Only Shorts count toward your limit. More on the <a href=\"youtube-shorts-blocker.html\">YouTube Shorts blocker page</a>.</p>",
  "Yes. Brainrot tells vertical Shorts apart from regular horizontal videos. Lectures, tutorials, podcasts and music keep playing without a counter. Only Shorts count toward your limit."),
 ("platforms","What happens when I reach my limit?",
  "<p>Brainrot shows a stop screen and takes you out of the short-video feed. You can still use the rest of the app and the rest of your phone. The counter resets the next day.</p>",
  "Brainrot shows a stop screen and takes you out of the short-video feed. You can still use the rest of the app and the rest of your phone. The counter resets the next day."),
 ("features","What is the difference between Unified and Individual limits?",
  "<p><strong>Unified</strong> gives you one shared daily budget across every supported app, for example 50 videos in total, whether they are Reels, Shorts or Spotlight. <strong>Individual</strong> lets you set a separate number for each app, for example 20 on Instagram, 10 on YouTube and 0 on Snapchat.</p>",
  "Unified gives you one shared daily budget across every supported app, for example 50 videos in total, whether they are Reels, Shorts or Spotlight. Individual lets you set a separate number for each app, for example 20 on Instagram, 10 on YouTube and 0 on Snapchat."),
 ("features","What are focus sessions?",
  "<p>A focus session is a timed block where distracting apps are blocked and only the essentials you choose (like Phone and Messages) stay available. You can start one on demand or schedule recurring sessions for study or work hours. See <a href=\"screen-time-controller.html\">the screen time controller page</a>.</p>",
  "A focus session is a timed block where distracting apps are blocked and only the essentials you choose (like Phone and Messages) stay available. You can start one on demand or schedule recurring sessions for study or work hours."),
 ("features","What is the brain mascot?",
  "<p>A small visual cue. As your daily count climbs from 0 to 1000+, the mascot moves through 11 states, from fresh to completely fried. It makes a number feel real at a glance. You can try it on the <a href=\"index.html#mascot\">home page</a>.</p>",
  "A small visual cue. As your daily count climbs from 0 to 1000+, the mascot moves through 11 states, from fresh to completely fried. It makes a number feel real at a glance."),
 ("features","Does it show how many videos I watched?",
  "<p>Yes. A small floating counter appears only while you are inside a short-video feed, and the app keeps a 7-day history of your daily totals so you can see the trend.</p>",
  "Yes. A small floating counter appears only while you are inside a short-video feed, and the app keeps a 7-day history of your daily totals so you can see the trend."),
 ("privacy","Why does Brainrot need the Accessibility Service permission?",
  "<p>Android has no other supported way for an app to know that you swiped to the next Reel or Short. The Accessibility Service lets Brainrot see that a short-video screen is open and that a swipe happened. That is all it is used for. Brainrot does not read your messages, passwords or what you type, and nothing is sent to a server. Details are in the <a href=\"privacy.html\">privacy policy</a>.</p>",
  "Android has no other supported way for an app to know that you swiped to the next Reel or Short. The Accessibility Service lets Brainrot see that a short-video screen is open and that a swipe happened. That is all it is used for. Brainrot does not read your messages, passwords or what you type, and nothing is sent to a server."),
 ("privacy","Does Brainrot collect or upload my data?",
  "<p>No. Your limits, daily counts and history are stored on your phone only. There is no account, no analytics SDK and no advertising. Uninstalling the app or clearing its data deletes everything.</p>",
  "No. Your limits, daily counts and history are stored on your phone only. There is no account, no analytics SDK and no advertising. Uninstalling the app or clearing its data deletes everything."),
 ("privacy","Will it drain my battery?",
  "<p>It is designed not to. Brainrot reacts to system events instead of polling in the background, so it is mostly idle unless a short-video app is open. Actual battery use varies by device, and you can check it under Android Settings → Battery.</p>",
  "It is designed not to. Brainrot reacts to system events instead of polling in the background, so it is mostly idle unless a short-video app is open. Actual battery use varies by device, and you can check it under Android Settings, Battery."),
 ("privacy","The limit stopped working after an Instagram or YouTube update. What do I do?",
  "<p>Apps change their layouts, and occasionally a detector needs an update. First make sure Brainrot and the other app are both up to date and that the Accessibility permission is still on. If it still misbehaves, <a href=\"contact.html\">send us a note</a> with your phone model and the app version, and we will look into it.</p>",
  "Apps change their layouts, and occasionally a detector needs an update. First make sure Brainrot and the other app are both up to date and that the Accessibility permission is still on. If it still misbehaves, contact us with your phone model and the app version."),
 ("privacy","Can I use Brainrot for my child?",
  "<p>Brainrot is built as a self-control tool for adults and teens who want to manage their own scrolling. It is not a parental control product and has no remote monitoring.</p>",
  "Brainrot is built as a self-control tool for adults and teens who want to manage their own scrolling. It is not a parental control product and has no remote monitoring."),
 ("compare","Is there a free reels blocker for Android?",
  "<p>Yes. Brainrot: Reel Limit is a free Android reels blocker. It counts Instagram Reels, YouTube Shorts, Facebook Reels and Snapchat Spotlight, and closes the feed when you reach your daily limit. There is no account to create and nothing is processed outside your phone. Get it on <a href=\"https://play.google.com/store/apps/details?id=com.focusport.limit\" rel=\"noopener\">Google Play</a>.</p>",
  "Yes. Brainrot: Reel Limit is a free Android reels blocker. It counts Instagram Reels, YouTube Shorts, Facebook Reels and Snapchat Spotlight, and closes the feed when you reach your daily limit. There is no account to create and nothing is processed outside your phone."),
 ("compare","What is a free alternative to paid reel blockers and app blockers?",
  "<p>Brainrot is a free alternative if your main problem is Reels and Shorts rather than whole apps. Many paid blockers charge a subscription for their reel-blocking features. Brainrot gives you a per-video limit, app time limits and focus sessions at no cost, with no account. Pricing of other apps changes, so check their current Play Store listing before comparing. See the <a href=\"comparison.html\">full comparison</a>.</p>",
  "Brainrot is a free alternative if your main problem is Reels and Shorts rather than whole apps. Many paid blockers charge a subscription for their reel-blocking features. Brainrot gives you a per-video limit, app time limits and focus sessions at no cost, with no account. Pricing of other apps changes, so check their current Play Store listing before comparing."),
 ("compare","How does Brainrot compare with paid screen time and app blocker apps?",
  "<p>The main difference is what gets limited. Most paid blockers lock a whole app or a time window. Brainrot counts individual Reels and Shorts, so you keep Instagram DMs and long YouTube videos while the feed stops at your number. Paid apps may suit you better if you need iPhone support or sync across devices, since Brainrot is Android-only and has no account. Many people use one of each. Read the <a href=\"comparison.html\">comparison page</a> for details.</p>",
  "The main difference is what gets limited. Most paid blockers lock a whole app or a time window. Brainrot counts individual Reels and Shorts, so you keep Instagram DMs and long YouTube videos while the feed stops at your number. Paid apps may suit you better if you need iPhone support or sync across devices, since Brainrot is Android-only and has no account. Many people use one of each."),
 ("compare","Is Brainrot a free alternative to BrainPal?",
  "<p>Both apps count Reels and Shorts on Android. BrainPal (BrainPal: Quit Scrolling) describes itself as a reels tracker and scroll counter, and its store listing labels blocking reels and shorts at a limit as a Pro feature, priced at about ₹99 a month, or about ₹83 a month on the yearly plan, at the time of writing. In Brainrot, stopping the feed at your daily limit is part of the free app, along with app time limits and focus sessions, and there is no account. Features and pricing change, so check BrainPal's current Play Store listing before you compare. See the <a href=\"comparison.html\">comparison page</a>.</p>",
  "Both apps count Reels and Shorts on Android. BrainPal (BrainPal: Quit Scrolling) describes itself as a reels tracker and scroll counter, and its store listing labels blocking reels and shorts at a limit as a Pro feature, priced at about ₹99 a month, or about ₹83 a month on the yearly plan, at the time of writing. In Brainrot, stopping the feed at your daily limit is part of the free app, along with app time limits and focus sessions, and there is no account. Features and pricing change, so check BrainPal's current Play Store listing before you compare."),
]
CATS = [("general","Basics"),("platforms","Apps & limits"),("features","Features"),("privacy","Privacy & permissions"),("compare","Free vs paid")]

def faq_items(cat=None, limit=None, ids=False):
    out = []
    items = [f for f in FAQ if cat is None or f[0] == cat]
    if limit: items = items[:limit]
    return items

def render_faq(items, with_groups=False):
    out = []
    last = None
    names = dict(CATS)
    for i, (c, q, a, _) in enumerate(items):
        if with_groups and c != last:
            out.append(f'<h2 class="faq-group" data-cat="{c}">{names[c]}</h2>')
            last = c
        out.append(f'<details class="faq" data-cat="{c}" id="q-{i+1}"><summary>{q}</summary><div class="answer">{a}</div></details>')
    return "\n".join(out)
