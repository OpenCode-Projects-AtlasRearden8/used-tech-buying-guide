# The Used Tech Buying Guide

A calm, plain-English manual for buying (and selling) used laptops, phones, tablets, and monitors - written the way a friend would explain it: step by step, honest trade-offs, never condescending. Published as a free resource by [Asdale Dynamics, LLC](https://dylanasdale.github.io), the beginner- friendly AI education project of author Dylan Asdale.

## The one-sentence version

**Read the listing like a detective, check the locks before the price, test everything before you pay, wipe it when it changes hands - twice - and keep your walking-away pride.**

This guide is the *deciding and buying half* of the used-tech story. For what happens after the deal - backing up, calm wiping, lightweight Linux, Ollama, and turning a tired laptop into a spare-room station - read the companion manual, the **Old Laptop Revival Guide** (also free, also by Asdale Dynamics). The two guides share a voice but not a job: this one gets you a good machine; that one gives it a second life.

## Who this is for

- You are browsing secondhand listings and want a short, reliable routine instead of vibes and luck.
- You are not a technician, and you do not want to become one; you want to check the right five things and walk away safe.
- You may be the seller instead: the wiping chapters here protect your accounts, photos, and wallets on the way out.

## What is inside

- **docs/** - the manual, one Markdown file per chapter:
  - `00-read-this-first.md` - front matter: audience, golden rules, trip map
  1. Decoding Listings (dealbreakers, yellow flags, honest signals, scam patterns)
  2. Battery Health (capacity and cycles on every platform, swollen-battery safety)
  3. Screen Checks (dead pixels, burn-in, bleed, dead touch zones - in ten minutes)
  4. Locks, Accounts, and Seed Phrases (Activation Lock, FRP, enterprise Chromebooks, BitLocker, the crypto rules)
  5. Fair Prices (percent-of-new bands, ten-minute comps, adjustment math)
  6. Test Drives (the exact order of checks at the meetup, per device)
  7. Negotiation Scripts (eleven word-for-word tools, plus the seller's mirror)
  8. Meetup Safety (where to meet, how to pay, overpayment scams, walk-away triggers)
  9. Wipe It (sign-out-then-erase checklists for every platform, both sides)
  10. New or Used (cost-of-ownership frame; when new-with-warranty is the smarter buy)
  11. After You Buy (the first 48 hours, battery habits, resale-forward records)
- **docs/worksheets/** - printable inspection worksheets for laptop, phone, tablet, and monitor
- **docs/glossary.md** - plain-English definitions for every term used
- **build.py** - standard-library-only static site builder, plus `--check` docs linting and a `--from-md` single-file converter
- **assets/style.css** - the site stylesheet (light/dark aware, print styles for the worksheets)
- **assets/color-test.html** - a one-file offline screen test: cycle solid colors on any screen from a USB stick; no internet needed
- **tests/test_build.py** - tests for the converter, builder, docs lint, and repo hygiene
- **site/** - the generated site (built locally; gitignored, not committed)

## Quick start

Read it as plain text:

```bash
less docs/00-read-this-first.md
```

Build the static site (Python 3.9+, nothing else to install, nothing to download):

```bash
python3 build.py
```

Then open `site/index.html` in any browser - no server needed, no JavaScript required for reading, no network. Everything works from `file://`. Prefer the whole manual on one printable page?

```bash
xdg-open site/book.html      # Linux (or: open site/book.html on macOS)
```

Lint the documentation (links, anchors, code fences, stray characters):

```bash
python3 build.py --check
```

Convert one chapter to HTML on stdout:

```bash
python3 build.py --from-md docs/09-wipe-it.md
```

Run the tests:

```bash
python3 -m unittest discover -s tests -v
```

## How this complements the Old Laptop Revival Guide

| Question | Where to go |
| --- | --- |
| Which used laptop should I even buy, and for how much? | This guide (Guides 1, 5, 6, 10) |
| How do I not buy a locked brick or a stolen phone? | This guide (Guide 4), then test it (Guide 6) |
| How do I wipe my old device before it leaves the house? | This guide (Guide 9) - the hand-off wipe |
| I own the laptop now - how do I back it up, install Linux, run Ollama? | Old Laptop Revival Guide (all of it) |
| How do I wipe a laptop I am *keeping*, to revive it? | Revival Guide's "Calm Wipe" chapter |

## Principles

- **Local-first:** built and read offline; the generated site makes zero external requests.
- **No affiliates, no ads, no trackers:** the only links in the docs are internal ones; the only "product placement" is one offline color-test file you can copy to a USB stick.
- **Tested:** the build is reproducible byte-for-byte, the docs are linted (links, anchors, fences), and the test suite runs offline.

## Copyright and license

Copyright (c) 2026 Asdale Dynamics, LLC. Released under the MIT License - see `LICENSE`.
