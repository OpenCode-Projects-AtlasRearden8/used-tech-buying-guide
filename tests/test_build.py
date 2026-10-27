#!/usr/bin/env python3
"""Tests for the Used Tech Buying Guide builder, docs, and repo hygiene.

Run with:  python3 -m unittest discover -s tests -v
Everything is standard library only; no network is touched.
"""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import build as builder

DOCS = ROOT / "docs"


def built_pages() -> list[str]:
    return [str(Path(page["src"]).with_suffix(".html")) for page in builder.PAGES]


def render_source(markdown: str) -> str:
    return builder.render_markdown(markdown)


def compact(html: str) -> str:
    return re.sub(r"\s+", "", html)


class Converter(unittest.TestCase):
    def test_headings_get_slugs(self):
        html = render_source("# The Big Question\n\n## tax year, explained\n")
        self.assertIn('<h1 id="the-big-question">', html)
        self.assertIn('<h2 id="tax-year-explained">', html)

    def test_inline_formatting_and_escaping(self):
        html = render_source("**bold** and *calm* and `cmd /c` and <script> bad\n")
        self.assertIn("<strong>bold</strong>", html)
        self.assertIn("<em>calm</em>", html)
        self.assertIn("<code>cmd /c</code>", html)
        self.assertNotIn("<script> bad", html)
        self.assertIn("&lt;script&gt;", html)

    def test_code_span_protects_asterisks(self):
        html = render_source("dial `*#*#4636#*#*` on the keypad\n")
        self.assertIn("<code>*#*#4636#*#*</code>", html)
        self.assertNotIn("<em>", html)

    def test_md_links_become_html(self):
        html = render_source("read [the guide](2-battery-health.md) first\n")
        self.assertIn('<a href="2-battery-health.html">the guide</a>', html)

    def test_color_test_asset_link_is_rewritten(self):
        html = render_source("carry [the color test](../assets/color-test.html) on a stick\n")
        self.assertIn('<a href="../color-test.html">', html)

    def test_tasks_render_as_checkboxes(self):
        html = compact(render_source("- [ ] wipe first\n- [x] already signed out\n"))
        self.assertIn('<liclass="task">\u2610wipefirst</li>', html)
        self.assertIn('<liclass="task">\u2611alreadysignedout</li>', html)

    def test_nested_lists(self):
        html = compact(render_source("- top\n  - nested\n- back\n"))
        self.assertTrue(html.startswith("<ul><li>top<ul><li>nested</li></ul></li><li>back</li></ul>"))

    def test_ordered_list_with_start(self):
        html = compact(render_source("3. third\n4. fourth\n"))
        self.assertIn('<olstart="3"><li>third</li><li>fourth</li></ol>', html)

    def test_tables(self):
        html = compact(render_source("| A | B |\n| --- | --- |\n| one | two |\n"))
        self.assertIn("<table><thead><tr><th>A</th><th>B</th></tr></thead>", html)
        self.assertIn("<tbody><tr><td>one</td><td>two</td></tr></tbody></table>", html)

    def test_fenced_code_blocks(self):
        html = render_source("```bash\nls -la\n```\n")
        self.assertIn('<pre><code class="language-bash">ls -la</code></pre>', html)

    def test_blockquote(self):
        html = render_source("> calm note line one\n> still the same note\n")
        self.assertIn("<blockquote><p>calm note line one still the same note</p></blockquote>", html)

    def test_horizontal_rule(self):
        self.assertIn("<hr>", render_source("one\n\n---\n\ntwo\n"))


class CliAndFormatting(unittest.TestCase):
    def test_from_md_produces_wrapped_page(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "build.py"), "--from-md", str(DOCS / "glossary.md")],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("<!DOCTYPE html>", result.stdout)
        self.assertIn("Glossary", result.stdout)

    def test_title_falls_back_to_filename(self):
        self.assertEqual(builder.doc_title("no heading here\n", "fallback.md"), "fallback.md")
        self.assertEqual(builder.doc_title("# Real Title\n", "x"), "Real Title")


class SiteBuild(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls._tmp.name) / "site"
        cls.problems = builder.build_site(DOCS, ROOT / "assets", cls.out, quiet=True)

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def test_site_check_is_clean(self):
        self.assertEqual(self.problems, [])

    def test_expected_manifest(self):
        expected = {Path(src).with_suffix(".html").as_posix() for src in built_pages()}
        expected |= {"index.html", "book.html", "style.css", "color-test.html"}
        manifest = {p.relative_to(self.out).as_posix() for p in self.out.rglob("*") if p.is_file()}
        self.assertEqual(manifest, expected)

    def test_worksheet_pages_exist_in_subfolder(self):
        for sheet in ("laptop-worksheet.html", "phone-worksheet.html", "tablet-worksheet.html", "monitor-worksheet.html"):
            self.assertTrue((self.out / "worksheets" / sheet).is_file())

    def test_index_links_every_page(self):
        html = (self.out / "index.html").read_text(encoding="utf-8")
        for page in built_pages():
            href = page.replace(".md", ".html")
            self.assertIn(f'href="{href}"', html)

    def test_no_scripts_or_external_requests(self):
        for html_path in self.out.rglob("*.html"):
            text = html_path.read_text(encoding="utf-8")
            if html_path.name == "color-test.html":
                continue  # deliberate local-only interactive tool
            self.assertNotIn("<script", text.lower(), f"script tag on {html_path.name}")
            for href in builder.ATTR_RE.findall(text):
                self.assertFalse(
                    href.startswith(("http://", "https://", "//", "data:")),
                    f"external reference on {html_path.name}: {href}",
                )

    def test_color_test_tool_is_offline_and_complete(self):
        text = (self.out / "color-test.html").read_text(encoding="utf-8")
        for color in ("#ffffff", "#000000", "#ff0000", "#00ff00", "#0000ff", "#808080"):
            self.assertIn(color, text)
        self.assertNotIn("http", text.lower())

    def test_footer_credit_and_license_mention(self):
        html = (self.out / "index.html").read_text(encoding="utf-8")
        self.assertIn("Asdale Dynamics, LLC", html)
        self.assertIn("MIT License", html)

    def test_pager_navigation(self):
        html_01 = (self.out / "01-decoding-listings.html").read_text(encoding="utf-8")
        self.assertIn("00-read-this-first.html", html_01)
        self.assertIn("02-battery-health.html", html_01)

    def test_companion_mentioned_on_index(self):
        html = (self.out / "index.html").read_text(encoding="utf-8")
        self.assertIn("Old Laptop Revival Guide", html)

    def test_build_is_reproducible(self):
        with tempfile.TemporaryDirectory() as tmp:
            dir_a, dir_b = Path(tmp) / "a", Path(tmp) / "b"
            builder.build_site(DOCS, ROOT / "assets", dir_a, quiet=True)
            builder.build_site(DOCS, ROOT / "assets", dir_b, quiet=True)
            files_a = {p.relative_to(dir_a).as_posix(): p.read_bytes() for p in sorted(dir_a.rglob("*")) if p.is_file()}
            files_b = {p.relative_to(dir_b).as_posix(): p.read_bytes() for p in sorted(dir_b.rglob("*")) if p.is_file()}
        self.assertIn("index.html", files_a)
        self.assertIn("00-read-this-first.html", files_a)
        self.assertEqual(files_a, files_b)

    def test_missing_critical_file_fails_loudly(self):
        with tempfile.TemporaryDirectory() as tmp:
            empty_docs = Path(tmp) / "docs"
            empty_docs.mkdir()
            with self.assertRaises(SystemExit):
                builder.build_site(empty_docs, ROOT / "assets", Path(tmp) / "site", quiet=True)


class DocsLint(unittest.TestCase):
    def test_docs_pass_check(self):
        problems = builder.lint_docs(DOCS)
        self.assertEqual(problems, [])

    def test_every_worksheet_linked_from_a_guide(self):
        guide_text = "\n".join(
            (DOCS / key["src"]).read_text(encoding="utf-8") for key in builder.PAGES if key["category"] == "guide"
        )
        for sheet in ("laptop-worksheet.md", "phone-worksheet.md", "tablet-worksheet.md", "monitor-worksheet.md"):
            self.assertIn(sheet, guide_text)

    def test_every_chapter_has_glossary_or_next_pointer(self):
        for page in builder.PAGES:
            if page["category"] == "guide" and page["src"] != "11-after-you-buy.md":
                text = (DOCS / page["src"]).read_text(encoding="utf-8")
                self.assertTrue(
                    re.search(r"\]\((?:\.\./)?(?:\d{2}|worksheets/|glossary)", text),
                    f"{page['src']} has no onward pointer",
                )

    def test_seed_phrase_rules_appear_in_locks_chapter(self):
        text = (DOCS / "04-locks-and-seed-phrases.md").read_text(encoding="utf-8")
        self.assertIn("seed phrase", text.lower())
        self.assertIn("Activation Lock", text)


class RepoHygiene(unittest.TestCase):
    def test_license_exact_line(self):
        text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Copyright (c) 2026 Asdale Dynamics, LLC", text)
        self.assertIn("MIT License", text)

    def test_readme_credits_llc(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Asdale Dynamics, LLC", readme)

    def test_no_secret_patterns_in_repo_text(self):
        secret_patterns = [
            re.compile(pattern)
            for pattern in (
                r"AKIA[0-9A-Z]{16}",
                r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
                r"sk-[A-Za-z0-9]{20,}",
                r"gsk_[A-Za-z0-9]{20,}",
                r"ghp_[A-Za-z0-9]{30,}",
                r"(?i)api[_-]?key\s*[:=]\s*['\"][A-Za-z0-9]{16,}",
            )
        ]
        for path in list((ROOT / "docs").rglob("*.md")) + [ROOT / "README.md", ROOT / "LICENSE", ROOT / "build.py"]:
            text = path.read_text(encoding="utf-8", errors="replace")
            for pattern in secret_patterns:
                self.assertIsNone(pattern.search(text), f"suspicious token in {path.name}")

    def test_gitignore_covers_generated_site(self):
        text = (ROOT / ".gitignore").read_text(encoding="utf-8")
        self.assertIn("site/", text)
        self.assertIn("__pycache__/", text)

    def test_no_coauthor_style_contamination(self):
        for path in (ROOT / "docs").rglob("*.md"):
            text = path.read_text(encoding="utf-8", errors="replace")
            self.assertNotIn("Co-authored-by", text, path.name)


if __name__ == "__main__":
    unittest.main()
