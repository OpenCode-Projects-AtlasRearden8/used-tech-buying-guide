#!/usr/bin/env python3
"""Build the Used Tech Buying Guide: static site out of Markdown, plus doc linting.

House style: standard library only, fully offline, byte-for-byte reproducible.
The generated site makes zero external requests, needs no JavaScript to read,
and works straight from file://. CLI:

    python3 build.py                       build docs/ + assets/ into site/
    python3 build.py --out /tmp/preview    build somewhere else
    python3 build.py --check               lint the docs (links, anchors, fences, characters)
    python3 build.py --from-md FILE.md     render one Markdown file to HTML on stdout
"""
from __future__ import annotations

import argparse
import re
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE_NAME = "Used Tech Buying Guide"

FENCE_RE = re.compile(r"^\s{0,3}(```|~~~)\s*([A-Za-z0-9_+-]*)\s*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
HR_RE = re.compile(r"^\s{0,3}(?:-{3,}|\*{3,}|_{3,})\s*$")
LIST_RE = re.compile(r"^(\s*)([-*+]|\d{1,3}[.)])\s+(.*)$")
QUOTE_RE = re.compile(r"^\s{0,3}>\s?(.*)$")
TABLE_DELIM_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")
LINK_MD_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
TASK_RE = re.compile(r"^\[( |x|X)\]\s+(.*)$")
ID_RE = re.compile(r'id="([^"]+)"')
ATTR_RE = re.compile(r'\b(?:href|src)="([^"]+)"')

ALLOWED_NON_ASCII = set("\u2610\u2611\u2014\u2013\u2018\u2019\u201c\u201d\u00b7\u2192\u2190\u2713\u2026\u26a1\u2318\u229e")

PAGES: list[dict] = [
    {"src": "00-read-this-first.md", "category": "guide", "kind": "Front matter",
     "desc": "Who this manual is for, the five golden rules of buying used tech, and how to use the worksheets."},
    {"src": "01-decoding-listings.md", "category": "guide", "kind": "Guide 1 of 11",
     "desc": "What listing phrases really mean: dealbreakers, yellow flags, honest signals, and classic scam patterns."},
    {"src": "02-battery-health.md", "category": "guide", "kind": "Guide 2 of 11",
     "desc": "How to check battery health on a laptop, phone, or tablet before money changes hands."},
    {"src": "03-screen-checks.md", "category": "guide", "kind": "Guide 3 of 11",
     "desc": "Dead pixels, burn-in, backlight bleed, and dead touch zones: the ten-minute screen test."},
    {"src": "04-locks-and-seed-phrases.md", "category": "guide", "kind": "Guide 4 of 11",
     "desc": "Activation Lock, Factory Reset Protection, enterprise Chromebooks, BitLocker, and seed-phrase warnings."},
    {"src": "05-fair-prices.md", "category": "guide", "kind": "Guide 5 of 11",
     "desc": "Percent-of-new price bands, ten-minute comps, and adjustment math for flaws and missing chargers."},
    {"src": "06-test-drives.md", "category": "guide", "kind": "Guide 6 of 11",
     "desc": "The exact order to test a device at the meetup, with what to bring and how long it takes."},
    {"src": "07-negotiation-scripts.md", "category": "guide", "kind": "Guide 7 of 11",
     "desc": "Calm word-for-word scripts for price talk: flaw pricing, comps anchoring, and walking away with the door open."},
    {"src": "08-meetup-safety.md", "category": "guide", "kind": "Guide 8 of 11",
     "desc": "Where to meet, how to pay, overpayment scams, and walk-away triggers, for buyers and sellers."},
    {"src": "09-wipe-it.md", "category": "guide", "kind": "Guide 9 of 11",
     "desc": "Wipe-before-selling checklists for every platform, and the wipe-again-anyway rule for buyers."},
    {"src": "10-new-or-used.md", "category": "guide", "kind": "Guide 10 of 11",
     "desc": "A cost-of-ownership framework for when new-with-warranty is the smarter buy and when used quietly wins."},
    {"src": "11-after-you-buy.md", "category": "guide", "kind": "Guide 11 of 11",
     "desc": "The first 48 hours and first two weeks with a secondhand device, plus battery and resale habits."},
    {"src": "worksheets/laptop-worksheet.md", "category": "worksheet", "kind": "Printable worksheet",
     "desc": "Printable checklist for inspecting a used laptop at the meetup."},
    {"src": "worksheets/phone-worksheet.md", "category": "worksheet", "kind": "Printable worksheet",
     "desc": "Printable checklist for inspecting a used phone at the meetup."},
    {"src": "worksheets/tablet-worksheet.md", "category": "worksheet", "kind": "Printable worksheet",
     "desc": "Printable checklist for inspecting a used tablet at the meetup."},
    {"src": "worksheets/monitor-worksheet.md", "category": "worksheet", "kind": "Printable worksheet",
     "desc": "Printable checklist for inspecting a used monitor, using the offline color test."},
    {"src": "glossary.md", "category": "reference", "kind": "Reference",
     "desc": "Plain-English definitions for every term used in the guide."},
]

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{desc}">
<title>{title}</title>
<link rel="stylesheet" href="{rel}style.css">
</head>
<body>
<a class="skip" href="#content">Skip to content</a>
<header class="site">
  <p class="brand"><a href="{rel}index.html">{site_name}</a></p>
  <nav>
    <a href="{rel}index.html">Contents</a>
    <a href="{rel}00-read-this-first.html">Start here</a>
    <a href="{rel}glossary.html">Glossary</a>
    <a href="{rel}color-test.html">Color test</a>
    <a href="{rel}book.html">Print all</a>
  </nav>
</header>
<main id="content">
<article>
{body}
</article>
{pager}
</main>
<footer>
  <p>Local-first: this site is a folder of files. No network requests, no ads, no trackers, no affiliate links.</p>
  <p>Built from Markdown by <code>build.py</code> \u00b7 \u00a9 2026 <strong>Asdale Dynamics, LLC</strong> \u00b7 MIT License</p>
</footer>
</body>
</html>
"""

BOOK_TO_CSS = ""
COMPANION = """
<section class="companion">
<h2 id="companion-guides">Companion guides</h2>
<p>Buying is the first half. Owning is the rest. Two sibling manuals continue this one without repeating it:</p>
<ul>
<li><strong>The Old Laptop Revival Guide</strong> \u2014 once you own a used laptop, that guide takes over: backup, calm wipe, lightweight Linux, Ollama, and the spare-room station. Where that guide <em>revives</em>, this guide <em>decides and acquires</em>.</li>
<li><strong>The local-AI side of an old laptop</strong> is split the same way: choose and buy a machine here; learn to run models on it in the Revival Guide and The Local AI Handbook.</li>
</ul>
</section>
"""


def slugify(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = text.replace("`", "").replace("*", "").replace("&", "and")
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text.strip("-") or "section"


def doc_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if not line.strip():
            continue
        m = HEADING_RE.match(line)
        if m and len(m.group(1)) == 1:
            return m.group(2).strip()
        return fallback
    return fallback


def md_href(href: str) -> str:
    if href.startswith(("http://", "https://", "mailto:", "#", "/")):
        return href
    href = href.replace("assets/color-test.html", "color-test.html")
    if ".md" in href:
        href = href.replace(".md", ".html", 1)
    return href


def fmt_label(text: str) -> str:
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def inline(text: str) -> str:
    spans: list[str] = []

    def stash(m: re.Match) -> str:
        spans.append(m.group(1))
        return f"\x00{len(spans) - 1}\x00"

    text = escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", stash, text)

    text = LINK_MD_RE.sub(lambda m: f'<a href="{md_href(m.group(2))}">{fmt_label(m.group(1))}</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"<em>\1</em>", text)

    def restore(m: re.Match) -> str:
        return "<code>" + spans[int(m.group(1))] + "</code>"

    return re.sub(r"\x00(\d+)\x00", restore, text)


def split_row(row: str) -> list[str]:
    row = row.strip()
    if row.startswith("|"):
        row = row[1:]
    if row.endswith("|"):
        row = row[:-1]
    return [cell.strip() for cell in row.split("|")]


def align_of(delim: str) -> str:
    left, right = delim.startswith(":"), delim.endswith(":")
    if left and right:
        return "center"
    if right:
        return "right"
    if left:
        return "left"
    return ""


def cell_style(index: int, aligns: list[str]) -> str:
    if index < len(aligns) and aligns[index]:
        return f' style="text-align:{aligns[index]}"'
    return ""


def flush_table(rows: list[str], out: list[str]) -> None:
    header = split_row(rows[0])
    aligns = [align_of(d) for d in split_row(rows[1])]
    parts = ["<table><thead><tr>"]
    for i, cell in enumerate(header):
        parts.append(f"<th{cell_style(i, aligns)}>{inline(cell)}</th>")
    parts.append("</tr></thead><tbody>")
    for row in rows[2:]:
        cells = split_row(row)
        parts.append("<tr>")
        for i in range(len(header)):
            cell = cells[i] if i < len(cells) else ""
            parts.append(f"<td{cell_style(i, aligns)}>{inline(cell)}</td>")
        parts.append("</tr>")
    parts.append("</tbody></table>")
    out.append("".join(parts))


def flush_fence(buf: list[str], lang: str, out: list[str]) -> None:
    cls = f' class="language-{lang}"' if lang else ""
    out.append(f"<pre><code{cls}>{escape(chr(10).join(buf))}</code></pre>")


def render_markdown(text: str) -> str:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    out: list[str] = []
    para: list[str] = []
    ids: dict[str, int] = {}
    fence: str | None = None
    fence_buf: list[str] = []
    fence_lang = ""
    table_rows: list[str] | None = None
    lists: list[dict] = []

    def flush_para() -> None:
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    def close_lists() -> None:
        while lists:
            top = lists.pop()
            if top["open"]:
                out.append("</li>")
            out.append("</ol>" if top["kind"] == "ol" else "</ul>")

    def handle_item(indent: int, kind: str, content: str, start: int) -> None:
        flush_para()
        while lists and lists[-1]["indent"] > indent:
            top = lists.pop()
            if top["open"]:
                out.append("</li>")
            out.append("</ol>" if top["kind"] == "ol" else "</ul>")
        if lists and lists[-1]["indent"] == indent and lists[-1]["kind"] != kind:
            top = lists.pop()
            if top["open"]:
                out.append("</li>")
            out.append("</ol>" if top["kind"] == "ol" else "</ul>")
        if not lists or lists[-1]["indent"] < indent:
            if kind == "ol":
                out.append(f'<ol start="{start}">')
            else:
                out.append("<ul>")
            lists.append({"kind": kind, "indent": indent, "open": False})
        if lists[-1]["open"]:
            out.append("</li>")
        tm = TASK_RE.match(content)
        if kind == "ul" and tm:
            mark = "\u2610" if tm.group(1) == " " else "\u2611"
            out.append(f'<li class="task">{mark} ' + inline(tm.group(2)))
        else:
            out.append("<li>" + inline(content))
        lists[-1]["open"] = True

    i, n = 0, len(lines)
    while i < n:
        line = lines[i]

        if fence is not None:
            if FENCE_RE.match(line) and line.strip().startswith(fence):
                flush_fence(fence_buf, fence_lang, out)
                fence, fence_buf, fence_lang = None, [], ""
            else:
                fence_buf.append(line)
            i += 1
            continue

        if table_rows is not None:
            if line.strip().startswith("|"):
                table_rows.append(line)
                i += 1
                continue
            flush_table(table_rows, out)
            table_rows = None
            continue

        if not line.strip():
            flush_para()
            i += 1
            continue

        fm = FENCE_RE.match(line)
        if fm:
            flush_para()
            close_lists()
            fence, fence_buf, fence_lang = fm.group(1), [], fm.group(2)
            i += 1
            continue

        hm = HEADING_RE.match(line)
        if hm:
            flush_para()
            close_lists()
            level, heading_text = len(hm.group(1)), hm.group(2)
            slug = slugify(heading_text)
            if slug in ids:
                ids[slug] += 1
                slug = f"{slug}-{ids[slug]}"
            else:
                ids[slug] = 0
            out.append(f'<h{level} id="{slug}">' + inline(heading_text) + f"</h{level}>")
            i += 1
            continue

        if HR_RE.match(line):
            flush_para()
            close_lists()
            out.append("<hr>")
            i += 1
            continue

        lm = LIST_RE.match(line)
        if lm:
            indent = len(lm.group(1).expandtabs(4))
            marker = lm.group(2)
            kind = "ol" if marker[0].isdigit() else "ul"
            start = int(marker[:-1]) if kind == "ol" and marker[:-1].isdigit() else 1
            handle_item(indent, kind, lm.group(3), start)
            i += 1
            continue

        qm = QUOTE_RE.match(line)
        if qm:
            flush_para()
            close_lists()
            quote = [qm.group(1)]
            i += 1
            while i < n:
                q2 = QUOTE_RE.match(lines[i])
                if q2:
                    quote.append(q2.group(1))
                    i += 1
                else:
                    break
            out.append("<blockquote><p>" + inline(" ".join(q.strip() for q in quote)) + "</p></blockquote>")
            continue

        if line.strip().startswith("|") and i + 1 < n and TABLE_DELIM_RE.match(lines[i + 1]):
            flush_para()
            close_lists()
            table_rows = [line, lines[i + 1]]
            i += 2
            continue

        if lists and lists[-1]["open"]:
            out.append(" " + inline(line.strip()))
        else:
            flush_para()
            close_lists()
            para.append(line.strip())
        i += 1

    if fence is not None:
        flush_fence(fence_buf, fence_lang, out)
    if table_rows is not None:
        flush_table(table_rows, out)
    flush_para()
    close_lists()
    return "\n".join(out)


def wrap_page(body: str, title: str, desc: str, rel: str, pager: str) -> str:
    full_title = title if title == SITE_NAME else f"{title} \u00b7 {SITE_NAME}"
    return PAGE_TEMPLATE.format(
        desc=escape(desc, quote=True),
        title=escape(full_title, quote=True),
        rel=rel,
        site_name=SITE_NAME,
        body=body,
        pager=pager,
    )


def rel_prefix(out_path: Path) -> str:
    return "../" * (len(out_path.parts) - 1)


def load_pages(docs_dir: Path) -> list[dict]:
    entries = []
    for meta in PAGES:
        path = docs_dir / meta["src"]
        if not path.is_file():
            raise SystemExit(f"build: missing docs file: {meta['src']}")
        text = path.read_text(encoding="utf-8")
        title = doc_title(text, meta["src"])
        out_path = Path(meta["src"]).with_suffix(".html")
        entries.append({**meta, "text": text, "title": title, "src_path": path, "out_path": out_path})
    return entries


def pager_html(index: int, entries: list[dict], rel: str = "") -> str:
    prev_e = entries[index - 1] if index > 0 else None
    next_e = entries[index + 1] if index + 1 < len(entries) else None
    prev_html = (
        f'<a class="pager-prev" href="{rel}{prev_e["href"]}">\u2190 {escape(prev_e["title"])}</a>'
        if prev_e
        else '<span class="pager-prev"></span>'
    )
    next_html = (
        f'<a class="pager-next" href="{rel}{next_e["href"]}">{escape(next_e["title"])} \u2192</a>'
        if next_e
        else '<span class="pager-next"></span>'
    )
    return f'<nav class="pager">{prev_html}{next_html}</nav>'


def build_site(docs_dir: Path, assets_dir: Path, out_dir: Path, quiet: bool = False) -> list[str]:
    pages = load_pages(docs_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for source in ("style.css", "color-test.html"):
        src = assets_dir / source
        if not src.is_file():
            raise SystemExit(f"build: missing asset: assets/{source}")
        (out_dir / source).write_bytes(src.read_bytes())

    hrefs = [{"title": page["title"], "href": str(page["out_path"])} for page in pages]
    problems: list[str] = []
    for index, page in enumerate(pages):
        body = "<p class=\"kicker\">" + page["kind"] + "</p>\n" + render_markdown(page["text"])
        html = wrap_page(
            body=body,
            title=page["title"],
            desc=page["desc"],
            rel=rel_prefix(page["out_path"]),
            pager=pager_html(index, hrefs, rel_prefix(page["out_path"])),
        )
        target = out_dir / page["out_path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")

    anchor_map = {
        Path(page["out_path"]).with_suffix(".html").as_posix(): f"#doc-{Path(page['out_path']).with_suffix('').as_posix().replace('/', '-')}"
        for page in pages
    }

    def rewrite_for_book(html: str, src_dir: Path) -> str:
        def fix(m: re.Match) -> str:
            url = m.group(1)
            if url.startswith(("http://", "https://", "mailto:", "#")):
                return m.group(0)
            base, frag = url.partition("#")[0], url.partition("#")[2]
            if not base.endswith(".html"):
                return m.group(0)
            src_target = (src_dir / base).resolve()
            try:
                rel_docs = src_target.relative_to(docs_dir.resolve()).as_posix()
                site_target = Path(rel_docs).with_suffix(".html").as_posix()
            except ValueError:
                site_target = Path(base).name
            if site_target in anchor_map:
                return f'href="{anchor_map[site_target]}"'
            if Path(site_target).name == "color-test.html":
                return 'href="color-test.html"'
            return m.group(0)

        return re.sub(r'href="([^"]+)"', fix, html)

    book_sections: list[str] = []
    book_toc: list[str] = []
    for page in pages:
        stem = page["out_path"].with_suffix("").as_posix().replace("/", "-")
        book_toc.append(f'<li><a href="#doc-{stem}">{escape(page["title"])}</a></li>')
        rendered = rewrite_for_book(render_markdown(page["text"]), page["src_path"].parent)
        book_sections.append(
            f'<section id="doc-{stem}"><h2 class="book-head">{escape(page["title"])}</h2>'
            + rendered
            + "</section>"
        )
    book_body = (
        '<nav class="booktoc"><p>Contents of this printable edition:</p><ul>'
        + "".join(book_toc)
        + '</ul></nav>'
        + "".join(book_sections)
    )
    book = wrap_page(
        body=book_body,
        title="The whole guide on one page",
        desc="Every chapter and worksheet of the Used Tech Buying Guide on a single printable page.",
        rel="",
        pager="",
    )
    (out_dir / "book.html").write_text(book, encoding="utf-8")

    grouped: dict[str, list[dict]] = {}
    for page in pages:
        grouped.setdefault(page["category"], []).append(page)
    labels = {"guide": "The guides", "worksheet": "Worksheets", "reference": "Reference"}
    intros = {
        "guide": "Read in order, or jump where you need. Every chapter ends by pointing at the next step.",
        "worksheet": "Print these and carry them to the meetup. The checkboxes are real.",
        "reference": "For looking things up mid-meeting, not for reading cover to cover.",
    }
    cards: list[str] = []
    for category in ("guide", "worksheet", "reference"):
        cards.append(f"<h3>{labels[category]}</h3>")
        cards.append(f'<p class="catintro">{intros[category]}</p>')
        cards.append('<ul class="cards">')
        for page in grouped[category]:
            cards.append(
                f'<li><a href="{page["out_path"]}"><strong>{escape(page["title"])}</strong>'
                f"<span>{escape(page['desc'])}</span></a></li>"
            )
        cards.append("</ul>")
    extra_tools = (
        '<section class="cardrow">'
        '<a class="card wide" href="color-test.html"><strong>The offline screen color test</strong>'
        "<span>color-test.html \u2014 put it on a USB stick and cycle solid test colors on any screen, anywhere, with no internet.</span></a>"
        '<a class="card wide" href="book.html"><strong>The whole guide on one page</strong>'
        "<span>book.html \u2014 every chapter and worksheet together, for printing or searching.</span></a>"
        "</section>"
    )
    hero = f"""
<section class="hero">
<h1>{SITE_NAME}</h1>
<p class="tagline">A calm, plain-English manual for buying <em>and selling</em> used laptops, phones,
tablets, and monitors \u2014 written the way a friend would explain it, and built to be read offline.</p>
</section>
<section class="rules">
<h2 id="golden-rules">The five golden rules</h2>
<ol>
<li><strong>You are the money.</strong> Nothing gets paid for until you have held it, unlocked it, and tested it.</li>
<li><strong>Locks come before price.</strong> Activation Lock, Factory Reset Protection, and enterprise Chromebooks are bricks with nice screens.</li>
<li><strong>The battery is the engine.</strong> Its health moves the real price more than the color of the case.</li>
<li><strong>Wipe it twice.</strong> The seller wipes before handoff; the buyer wipes again the same evening, just in case.</li>
<li><strong>Walking away is free.</strong> There is always another listing. Always.</li>
</ol>
</section>
"""
    index_body = hero + "".join(cards) + extra_tools + COMPANION
    index_html = wrap_page(
        body=index_body,
        title=SITE_NAME,
        desc="A calm, local-first manual for buying and selling used laptops, phones, tablets, and monitors.",
        rel="",
        pager="",
    )
    (out_dir / "index.html").write_text(index_html, encoding="utf-8")

    problems = check_site(out_dir, pages)
    if not quiet:
        total = len(pages) + 5
        print(f"Built {total} files into {out_dir.name}")
        if problems:
            print(f"Site check found {len(problems)} problem(s):")
            for problem in problems:
                print(f"  - {problem}")
        else:
            print("Site check: clean (links, anchors, zero external requests)")
    return problems


def check_site(out_dir: Path, pages: list[dict]) -> list[str]:
    problems: list[str] = []
    generated = [out_dir / "index.html", out_dir / "book.html"] + [out_dir / page["out_path"] for page in pages]
    ids_by_file: dict[Path, set[str]] = {}
    texts: dict[Path, str] = {}
    for path in generated:
        if not path.is_file():
            problems.append(f"missing generated file: {path.name}")
            continue
        text = path.read_text(encoding="utf-8")
        texts[path] = text
        ids_by_file[path] = set(ID_RE.findall(text))
        for href in ATTR_RE.findall(text):
            if href.startswith(("http://", "https://", "//", "data:")):
                problems.append(f"{path.name}: external reference: {href}")
    for path in generated:
        if path not in texts:
            continue
        for href in ATTR_RE.findall(texts[path]):
            if href.startswith(("http", "//", "data:")):
                continue
            target_part, _, frag = href.partition("#")
            if not target_part:
                if frag and frag not in ids_by_file[path]:
                    problems.append(f"{path.name}: missing anchor: #{frag}")
                continue
            target = (path.parent / target_part).resolve()
            if not str(target).startswith(str(out_dir.resolve())):
                problems.append(f"{path.name}: link escapes the site: {href}")
                continue
            if not target.exists():
                problems.append(f"{path.name}: dead link: {href}")
                continue
            if frag and target.suffix == ".html" and frag not in ids_by_file.get(target, set()):
                problems.append(f"{path.name}: missing anchor: {href}")
    return problems


def lint_docs(docs_dir: Path) -> list[str]:
    problems: list[str] = []
    for meta in PAGES:
        path = docs_dir / meta["src"]
        rel = meta["src"]
        if not path.is_file():
            problems.append(f"missing file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        fence_count = sum(1 for line in text.splitlines() if FENCE_RE.match(line))
        if fence_count % 2 != 0:
            problems.append(f"{rel}: unbalanced code fences ({fence_count})")
        first_block = next((ln for ln in text.splitlines() if ln.strip()), "")
        if not (hm := HEADING_RE.match(first_block)) or len(hm.group(1)) != 1:
            problems.append(f"{rel}: first block must be an H1 heading")
        bad = sorted({ch for ch in text if ord(ch) > 127 and ch not in ALLOWED_NON_ASCII})
        if bad:
            shown = ", ".join(f"U+{ord(c):04X}" for c in bad)
            problems.append(f"{rel}: unexpected non-Latin characters: {shown}")
        for m in LINK_MD_RE.finditer(text):
            href = m.group(2)
            target, _, frag = href.partition("#")
            if target.startswith(("http://", "https://", "mailto:", "//")):
                problems.append(f"{rel}: external links are not allowed in docs: {href}")
                continue
            if not target:
                if frag and frag not in slugs_of(text):
                    problems.append(f"{rel}: dead local anchor: #{frag}")
                continue
            target_path = path.parent / target
            if not target.endswith(".md"):
                if target.endswith(".html") and not target.startswith("assets/"):
                    continue
                if target.startswith("assets/"):
                    target_path = docs_dir.parent / target
                if not target_path.is_file():
                    problems.append(f"{rel}: dead link target: {href}")
                continue
            if not target_path.is_file():
                problems.append(f"{rel}: dead link target: {href}")
                continue
            if frag and frag not in slugs_of(target_path.read_text(encoding="utf-8")):
                problems.append(f"{rel}: dead anchor: {href}")
    return problems


def slugs_of(text: str) -> set[str]:
    result: dict[str, int] = {}
    for line in text.splitlines():
        hm = HEADING_RE.match(line)
        if not hm:
            continue
        slug = slugify(hm.group(2))
        if slug in result:
            result[slug] += 1
            result[f"{slug}-{result[slug]}"] = result[slug]
        else:
            result[slug] = 0
    return set(result)


def convert_one(md_path: Path) -> str:
    text = md_path.read_text(encoding="utf-8")
    title = doc_title(text, md_path.stem)
    return wrap_page(body=render_markdown(text), title=title, desc=title, rel="", pager="")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build or lint the Used Tech Buying Guide.")
    parser.add_argument("--docs", type=Path, default=ROOT / "docs", help="Markdown source folder")
    parser.add_argument("--assets", type=Path, default=ROOT / "assets", help="copied assets folder")
    parser.add_argument("--out", type=Path, default=ROOT / "site", help="output folder")
    parser.add_argument("--check", action="store_true", help="lint the docs and exit")
    parser.add_argument("--from-md", type=Path, default=None, help="render one Markdown file to stdout")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args(argv)

    if args.from_md is not None:
        print(convert_one(args.from_md))
        return 0

    if args.check:
        problems = lint_docs(args.docs)
        if problems:
            for problem in problems:
                print(f"  - {problem}", file=sys.stderr)
            print(f"Checked docs: {len(problems)} problem(s)", file=sys.stderr)
            return 1
        print(f"Checked {len(PAGES)} markdown files: clean")
        return 0

    problems = build_site(args.docs, args.assets, args.out, quiet=args.quiet)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
