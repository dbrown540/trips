"""Build the public copy of the trip page from ~/Documents/trips, scrubbed of private details.

Scrub (Danny 2026-10-11): no name, no links to the Airbnb listings we sleep in. The gate below
fails the build if either comes back.
"""
import re, pathlib
SRC = pathlib.Path.home() / "Documents/trips/redwoods-to-yosemite-loop.html"
s = SRC.read_text()
s = s.replace("Danny's place", "home")
s = re.sub(r'<a href="https://www\.airbnb\.com/rooms/\d+">(.*?)</a>', r"\1", s)
for bad in ("Danny", "airbnb.com/rooms"):
    assert bad not in s, f"scrub gate: {bad!r} still in output"
pathlib.Path("redwoods-to-yosemite-loop.html").write_text(s)
print("built, gate passed")
