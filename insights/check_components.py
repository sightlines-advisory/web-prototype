"""Source-level component gate; not a substitute for browser/AT testing."""
from pathlib import Path
from html.parser import HTMLParser
import re
import sys

root = Path(__file__).resolve().parent
errors = []
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.refs = []
        self.covers = []
        self.checks = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = a.get("class", "").split()
        if a.get("id"):
            if a["id"] in self.ids:
                errors.append(f"{self.filename}: duplicate ID {a['id']}")
            self.ids.add(a["id"])
        for k in ("aria-labelledby", "aria-describedby"):
            self.refs.extend(a.get(k, "").split())
        if "tile-art" in classes:
            self.covers.append(classes)
            if "style" in a:
                errors.append(f"{self.filename}: inline cover style")
            if a.get("aria-hidden") != "true":
                errors.append(f"{self.filename}: cover not decorative")
        if tag == "input" and a.get("type") == "checkbox":
            if not (a.get("aria-label") or a.get("aria-labelledby")):
                errors.append(f"{self.filename}: checkbox needs explicit accessible name")

css = (root / "insights.css").read_text()
if len(re.findall(r"\.tile-art--insight\s*\{", css)) != 1:
    errors.append("Insight cover must have exactly one canonical base rule")
if re.search(r"\.tile-art--governance\b", css):
    errors.append("Article-specific governance cover override")
for path in sorted(root.glob("*.html")):
    p = Page()
    p.filename = path.name
    p.feed(path.read_text())
    for ref in p.refs:
        if ref not in p.ids:
            errors.append(f"{path.name}: missing ARIA target {ref}")
    for classes in p.covers:
        if "tile-art--insight" in classes and set(classes) - {"tile-art", "tile-art--insight", "tile-art--white-kicker"}:
            errors.append(f"{path.name}: unapproved Insight cover variant {classes}")
print("\n".join(errors) if errors else "Component source checks passed.")
sys.exit(bool(errors))
