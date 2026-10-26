# Brainrot: Reel Limit website

Marketing site for **Brainrot: Reel Limit**, a free Android app that counts Instagram Reels, YouTube Shorts, Facebook Reels and Snapchat Spotlight and blocks the feed when your daily limit is reached. Powered by FocusPort.

- Live site: https://brainrot.focusport.in
- Google Play: https://play.google.com/store/apps/details?id=com.focusport.limit
- Support: support@focusport.in

## Tech
Static HTML, CSS and JS with no framework. It is GitHub Pages ready, and the `CNAME` file is set to `brainrot.focusport.in`.

Preview locally:

```
node server.js
```

## Project structure
| Path | What it is |
|---|---|
| `*.html`, `blog/*.html` | Generated pages (33 in total) |
| `assets/` | CSS, JS and images (WebP screenshots, mascot, OG image) |
| `sitemap.xml`, `robots.txt`, `llms.txt` | Search engine and AI-crawler files |
| `_headers` | Cache and security headers (Netlify / Cloudflare style) |
| `_build-src/` | Python source the HTML pages are generated from |

## Editing content
You can edit the HTML files directly. If you do, delete `_build-src/` so the two don't drift apart.

Or edit the source and rebuild:

| To change | Edit |
|---|---|
| Domain, footer, schema, emails, Play link | `_build-src/lib.py` |
| FAQ questions and answers | `_build-src/faqdata.py` |
| Comparison, about, contact, students, professionals pages | `_build-src/pages_company.py` |
| Home page | `_build-src/pages_home.py` |
| Feature and landing pages | `_build-src/pages_product.py` |
| Blog posts | `_build-src/posts_*.py`, `blog.py` |

Build:

```
cd _build-src
python3 build.py
```

`build.py` writes to the `OUT` path set at the top of the file (it currently points to `/home/claude/out/site/`). Change `OUT` to your own folder, which must already hold a copy of the site (with `assets/css` and `assets/js`). Then copy the generated files back into the project. Remember to update `TODAY` in `lib.py` when you publish new content, because it sets the sitemap dates.

## Launch checklist
1. Confirm the Play ID `com.focusport.limit` matches the live Play Store listing.
2. Point DNS for `brainrot.focusport.in` at the host (GitHub Pages or similar) and enable HTTPS.
3. Add `https://brainrot.focusport.in` as a property in Google Search Console, submit `/sitemap.xml`, and request indexing for the home, Instagram, YouTube and comparison pages.
4. If the old `focusport.in` was indexed, set up 301 redirects to the new domain.
5. Check the Open Graph image (`assets/img/og-image.jpg`) by sharing the link on WhatsApp and Twitter.
6. Check the competitor pricing in the FAQ and comparison page (BrainPal) against the current Play Store listing before each release.

## Notes
- The site makes claims about other apps (BrainPal and others). Keep them accurate and dated.
- The app is Android-only and uses the Accessibility Service to count and block short-video feeds. All processing happens on the device.
