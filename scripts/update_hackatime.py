#!/usr/bin/env python3
"""Fetch Hackatime stats and refresh the live part of assets/panel-activity.svg.

The circuit-board background lives in the SVG itself. This script only rewrites
the block between <!--DYN:START--> and <!--DYN:END-->.
"""

import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape

HACKATIME_API = "https://hackatime.hackclub.com/api/v1/users/GK503/stats"
SVG_PATH = Path(__file__).parent.parent / "assets" / "panel-activity.svg"
FONT = "font-family=\"'Nunito','Quicksand','Varela Round','Trebuchet MS',ui-rounded,'Segoe UI',sans-serif\""


def fetch_stats():
    try:
        with urllib.request.urlopen(HACKATIME_API, timeout=10) as response:
            return json.loads(response.read().decode()).get("data", {})
    except Exception as e:
        print(f"Error fetching Hackatime stats: {e}", file=sys.stderr)
        return None


def _t(x, y, s, size, weight=600, anchor="middle", opacity=1, shadow=False):
    f = ' filter="url(#ts)"' if shadow else ""
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" {FONT} font-size="{size}" font-weight="{weight}" '
            f'fill="#fff" opacity="{opacity}"{f}>{escape(str(s))}</text>')


def build_dynamic(stats):
    """Panel content in local coordinates (0..1000 x 0..510)."""
    total = stats.get("human_readable_total", "0s")
    daily = stats.get("human_readable_daily_average", "0s")
    streak = stats.get("streak", 0)
    langs = stats.get("languages", [])[:5]

    o = _t(500, 70, "my coding activity", 38, 800, shadow=True)
    o += '<rect x="40" y="100" width="920" height="380" rx="24" fill="#12106a" fill-opacity="0.66" stroke="#8fb0ff" stroke-opacity="0.55"/>'
    for x, v, label in [(90, total, "total time"), (370, daily, "daily average"), (650, f"{streak} days", "current streak")]:
        o += (f'<rect x="{x}" y="124" width="260" height="90" rx="18" fill="#fff" fill-opacity="0.07" stroke="#8fb0ff" stroke-opacity="0.4"/>'
              + _t(x + 130, 166, v, 30, 800) + _t(x + 130, 194, label, 15, 600, opacity=0.8))
    o += _t(90, 258, "top languages", 20, 800, "start")
    for i, lang in enumerate(langs):
        y = 284 + i * 34
        pct = float(lang.get("percent", 0))
        o += (_t(90, y + 13, lang.get("name", "Unknown"), 17, 700, "start")
              + f'<rect x="230" y="{y}" width="540" height="14" rx="7" fill="#fff" fill-opacity="0.12"/>'
              + f'<rect x="230" y="{y}" width="{max(pct * 5.4, 14):.1f}" height="14" rx="7" fill="url(#bar)"/>'
              + _t(790, y + 13, f"{pct:.1f}%  ·  {lang.get('text', '0m')}", 16, 600, "start"))
    o += _t(500, 462, "last updated " + datetime.now(timezone.utc).strftime("%Y-%m-%d"), 14, 600, opacity=0.65)
    return o


def main():
    stats = fetch_stats()
    if not stats:
        sys.exit(1)
    svg = SVG_PATH.read_text(encoding="utf-8")
    pattern = r"(<!--DYN:START-->).*?(<!--DYN:END-->)"
    if not re.search(pattern, svg, flags=re.S):
        print("DYN markers not found in panel-activity.svg", file=sys.stderr)
        sys.exit(1)
    new = re.sub(pattern, lambda m: m.group(1) + build_dynamic(stats) + m.group(2), svg, flags=re.S)
    SVG_PATH.write_text(new, encoding="utf-8")
    print(f"Updated {SVG_PATH}")


if __name__ == "__main__":
    main()
