"""Visibility contract for the public meeting links page."""

from html.parser import HTMLParser
from pathlib import Path
import unittest


PAGE = Path(__file__).resolve().parents[1] / "index.html"


class Sections(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sections = {}
        self.current = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "section":
            self.current = attrs.get("aria-labelledby")
            self.sections[self.current] = {"hidden": "hidden" in attrs, "links": []}
        elif tag == "a" and self.current:
            self.sections[self.current]["links"].append(attrs.get("href"))

    def handle_endtag(self, tag):
        if tag == "section":
            self.current = None


class VisibilityTests(unittest.TestCase):
    def test_meeting_visible_and_assembly_hidden(self):
        parser = Sections()
        parser.feed(PAGE.read_text())
        meeting = parser.sections["meetings-title"]
        assembly = parser.sections["assembly-title"]
        self.assertFalse(meeting["hidden"])
        self.assertTrue(any(link and link.startswith("https://jworg.zoom.us/") for link in meeting["links"]))
        self.assertTrue(assembly["hidden"])
        self.assertTrue(assembly["links"], "Assembly links must be retained for later reuse")


if __name__ == "__main__":
    unittest.main()
