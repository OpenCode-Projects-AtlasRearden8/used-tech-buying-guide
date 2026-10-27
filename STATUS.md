# STATUS

Project: The Used Tech Buying Guide
Owner: Asdale Dynamics, LLC
State: complete and verified (October 2026)

## What was built

A calm, beginner-facing manual for buying used laptops, phones, tablets, and monitors - reading listings honestly, checking battery health and screens, avoiding locked devices and seed-phrase traps, pricing fairly, meeting safely, haggling gently, wiping on both sides of the deal, and knowing when new-with-warranty is the smarter buy - plus the tooling to turn it into a static website and a one-file offline screen-test tool. It complements the sibling **Old Laptop Revival Guide** without repeating it: where that guide *revives* a machine someone already owns, this guide *decides and acquires*; laptop-content crossover (calm wipes, Linux installs, local AI) is pointed there, not duplicated.

- **docs/** (17 Markdown files):
  - `00-read-this-first.md` - front matter: audience, the five golden rules, trip map, fine print, a 90-second version of the whole method.
  1. Decoding Listings - the four buckets (dealbreakers / yellow flags / honest signals / scam patterns), a phrase-to-meaning decoder table, five copy-paste seller questions.
  2. Battery Health - capacity vs cycle counts, per-platform checks (iPhone/iPad Settings, Android diagnostics and live charge tests, macOS System Report, Windows `powercfg /batteryreport`, Linux/Chromebook), age-vs-capacity bands, swollen-battery safety.
  3. Screen Checks - dead vs stuck pixels, burn-in, bleed, tint, dead digitizer zones; the ten-minute test order; laptop/phone/OLED/monitor specifics; screen-problem pricing table.
  4. Locks, Accounts, and Seed Phrases - Activation Lock and the Hello-screen verification ritual, Android FRP, enterprise Chromebooks, BitLocker/BIOS passwords, the seed-phrase rules for buyers and sellers, IMEI/blacklist basics, kind walk-away language.
  5. Fair Prices - percent-of-new bands by age, adjustment table (battery, screen, locked, finance), ten-minute sold-comps method, irresistible-price sanity check.
  6. Test Drives - what to pack, the order of operations, per-device checklists (laptop/phone/tablet/monitor) with discount triggers, the reset-then-pay ritual.
  7. Negotiation Scripts - calm mindset, text-stage scripts, eleven meetup scripts (flaw-price, comps anchor, silence, walk-away line...), scam-response table, and the seller-side mirror.
  8. Meetup Safety - where to meet (police exchange zones), payment rules, the overpayment scam, a two-minute street checklist, walk-away triggers.
  9. Wipe It - the universal sign-out-first rule, what bad wipes leave behind, per-platform seller checklists (iPhone/iPad, Android, Windows, Mac, Chromebook, monitor), buyer's wipe-again-anyway rule.
  10. New or Used - cost-of-ownership frame with a worked example, when new-with-warranty wins, when used wins, refurb/open-box middle paths, trade-in vs sell-private, a five-question gut-check.
  11. After You Buy - the first evening and first two weeks, secondhand-battery habits, resale-forward records, and the handoff point to the Revival Guide.
- **docs/worksheets/** - four printable inspection worksheets (laptop, phone, tablet, monitor) with real checkboxes, fill-in price lines, red-flag boxes, and walk-away lines.
- **docs/glossary.md** - 26 plain-English terms anchored in the site, written for phone reading at a meetup.
- **build.py**: standard-library-only static site builder. Zero dependencies, zero network. Produces an index with reading cards, one polished page per chapter with prev/next pagers, a single-page printable `book.html`, worksheets subfolder, plus `--check` (docs lint: links, cross-file anchors, code-fence balance, first-heading rule, forbidden external links, stray non-Latin characters) and `--from-md` (one file to stdout). The generated site makes zero external requests and works from `file://`.
- **assets/style.css**: warm light/dark stylesheet, print styles for worksheets, no JS needed for reading.
- **assets/color-test.html**: one-file offline screen color test (white/grays/black/RGB), keyboard and click navigation, fullscreen button - designed to be copied to a USB stick for meetup screen checks. Inline script only; no external references.
- **tests/test_build.py**: 34 tests covering the Markdown converter (headings/slugs, inline formatting, escaping, code-span protection, md-link rewriting, checkboxes, nested/ordered lists, tables, fences, quotes, rules), the CLI (`--from-md`, title fallback), the built site (manifest, worksheet pages, index links, no-script/zero-external-request policy, color-test completeness, footer credit, pager navigation, companion mention, reproducible builds, loud failure on missing docs), docs lint (clean check, worksheets linked, onward pointers, seed-phrase rules present), and repo hygiene (exact MIT line, README credit, secret-pattern scan, gitignore coverage, no co-author contamination).
- **README.md**, **LICENSE** (MIT, "Copyright (c) 2026 Asdale Dynamics, LLC"), **.gitignore** (site/ and __pycache__/ ignored).

## How to run it

```bash
python3 build.py                       # build site/ from docs/ (22 files)
python3 build.py --check               # lint the 17 markdown docs
python3 build.py --from-md docs/05-fair-prices.md   # one chapter to stdout
python3 -m unittest discover -s tests -v            # run the test suite (34 tests)
```

Then open `site/index.html` in any browser - no server needed; the site makes no external requests, so it works offline and from file://. `site/book.html` is the whole manual on one printable page; `site/color-test.html` is the offline color test (copy it to a USB stick and open it anywhere).

## Verification results (run in this folder)

- `python3 --version` -> Python 3.13.5
- `python3 -m py_compile build.py tests/test_build.py` -> OK
- `python3 build.py --check` -> "Checked 17 markdown files: clean" (exit 0)
- `python3 build.py` -> "Built 22 files into site" + "Site check: clean (links, anchors, zero external requests)" (exit 0)
- HTML structural check (html.parser tag balance over all 20 generated HTML files) -> 0 problems
- `python3 -m unittest discover -s tests` -> 34 tests, OK (0 failures, 0 errors)
- Reproducible-build test passes (two consecutive builds byte-identical)
- Zero external references verified by test across every generated page (no CDNs, no fonts, no analytics, no affiliate links)
- Secret-pattern scan across docs/README/LICENSE/build.py/tests -> 0 matches
- Git initialized with the existing configured identity (Dylan Asdale); committed once, nothing pushed, no remote, plain message with no Co-authored-by trailers

## Fix-ups applied during this pass

- Several chapters accumulated garbled tokens while drafting (stray non-Latin characters, mangled table rows, broken link syntax). Each was rewritten clean, and the docs lint now guards the character-level version of that mistake permanently (unexpected non-Latin characters fail `--check`).
- First run of `--check` exposed that every cross-chapter link was written un-padded (`1-decoding-listings.md` instead of `01-…`); fixed mechanically across all docs and now covered by the link check.
- First site build exposed per-depth link bugs: pager links from `worksheets/` pages lacked the `../` prefix, and `book.html` inherited each section's relative links (escaping the site). Both fixed: pagers are now depth-aware, and book sections rewrite cross-chapter links to in-page section anchors.
- The converter's table start dropped the delimiter row, collapsing tables to an empty tbody - fixed and covered by a table test.
- The color-test tool was originally scoped as a symlink idea; it is now a plain `assets/` file copied into `site/`, so `file://` usage from a USB stick anywhere works.

## Known gaps

- Price figures are US-market orientation values for October 2026; they will age. The durable part is the method (percent-of-new bands plus sold comps), and the guide says so out loud.
- Android battery-health flows vary wildly by maker; the chapter leans on maker diagnostics and a live charge-rate test rather than pretending one universal screen exists.
- The docs lint's first-block rule requires each doc to start with an H1, and external URLs are deliberately banned inside docs text (links never rot; vendor menus are given as paths instead). If you want a web-links edition, `--check` would need an allowlist.
- The Markdown renderer supports the subset these docs use (headings, lists incl. tasks, tables, fences, quotes, inline styles). Raw HTML in Markdown is escaped, not passed through, by design.
- The site has no search beyond `book.html` + browser Ctrl+F; no analytics of any kind, also no visitor stats (intentional, local-first).
- No mobile app, RSS feed, or auto-generated changelog. The manual is a folder; updating means editing Markdown and re-running `python3 build.py`.
