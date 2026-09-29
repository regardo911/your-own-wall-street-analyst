"""Offline upkeep checks: the Appendix B6 script's output, the two copies of desk-memo,
and the links in the Markdown files. Run with: python -m unittest discover -s tests -v"""
import contextlib
import io
import os
import re
import runpy
import sys
import unittest
from unittest import mock

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "appendix-b", "latest_numbers.py")

# fixtures: real data.sec.gov companyfacts responses, trimmed to the three tags the script reads
FIXTURES = {
    "https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json": "aapl-companyfacts.json",
    "https://data.sec.gov/api/xbrl/companyfacts/CIK0000040704.json": "gis-companyfacts.json",
}

# Appendix B6, the book's printed run on Apple
APPLE = (
    "Apple Inc.\n"
    "Revenue         109,417,000,000  10-Q filed 2026-07-31  period 2026-03-29..2026-06-27  accn 0000320193-26-000020\n"
    "Gross profit     54,770,000,000  10-Q filed 2026-07-31  period 2026-03-29..2026-06-27\n"
    "Gross margin 50.1%  (computed here from the two lines above)\n"
    "Shares out       14,594,180,000  as of 2026-07-17  10-Q filed 2026-07-31\n"
)


class _Response(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def run_script(cik):
    requests = []

    def fake_urlopen(req, *args, **kwargs):
        requests.append((req.full_url, req.get_header("User-agent")))
        if req.full_url not in FIXTURES:
            raise AssertionError(f"request outside the fixture set: {req.full_url}")
        with open(os.path.join(ROOT, "tests", "fixtures", FIXTURES[req.full_url]), "rb") as fh:
            return _Response(fh.read())

    out = io.StringIO()
    with mock.patch("urllib.request.urlopen", fake_urlopen), \
            mock.patch("socket.socket", side_effect=AssertionError("the script opened a socket")), \
            mock.patch.object(sys, "argv", [SCRIPT, cik]), \
            contextlib.redirect_stdout(out):
        runpy.run_path(SCRIPT, run_name="__main__")
    return out.getvalue(), requests


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


class ScriptTest(unittest.TestCase):
    def test_apple_prints_the_books_output_and_no_warning(self):
        out, requests = run_script("320193")
        self.assertEqual(out, APPLE)
        url, agent = requests[0]
        self.assertEqual(len(requests), 1)
        self.assertTrue(url.endswith("CIK0000320193.json"))
        self.assertTrue(agent, "the SEC refuses requests without a User-Agent")

    def test_general_mills_mixed_periods_print_the_warning(self):
        out, _ = run_script("40704")
        self.assertIn("period 2026-06-01..2026-08-30", out)
        self.assertIn("period 2026-02-23..2026-05-31", out)
        self.assertIn("Gross margin 36.5%", out)
        self.assertIn("WARNING: revenue and gross profit are from different periods", out)

    def test_a_company_outside_the_fixtures_never_reaches_the_network(self):
        with self.assertRaisesRegex(AssertionError, "outside the fixture set"):
            run_script("19617")


class CopyTest(unittest.TestCase):
    def test_skill_body_is_the_desk_memo_command(self):
        _, front, body = read("chapters/05-your-first-memo/desk-memo/SKILL.md").split("---\n", 2)
        self.assertIn("name: desk-memo\n", front)
        self.assertEqual(body, read("research-desk/knowledge/desk-memo.txt"))


# any "](target)", so a badge's outer link is caught as well as its image
LINK = re.compile(r"\]\(([^)\s]+)\)")


class LinkTest(unittest.TestCase):
    def test_every_relative_link_and_image_resolves(self):
        checked, broken = 0, []
        for dirpath, dirnames, filenames in os.walk(ROOT):
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
            for name in (n for n in filenames if n.endswith(".md")):
                text = re.sub(r"```.*?```", "", read(os.path.join(dirpath, name)), flags=re.S)
                for target in LINK.findall(text):
                    if re.match(r"[a-z]+:", target) or target.startswith("#"):
                        continue
                    checked += 1
                    path = os.path.normpath(os.path.join(dirpath, target.split("#")[0]))
                    if not path.startswith(ROOT + os.sep) or not os.path.exists(path):
                        broken.append(f"{os.path.relpath(os.path.join(dirpath, name), ROOT)} -> {target}")
        self.assertEqual(broken, [])
        self.assertGreater(checked, 20)


if __name__ == "__main__":
    unittest.main()
