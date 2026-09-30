#!/usr/bin/env python3
"""Fetch Hackatime stats and regenerate assets/panel-activity.svg."""

import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape

HACKATIME_API = "https://hackatime.hackclub.com/api/v1/users/GK503/stats"
SVG_PATH = Path(__file__).parent.parent / "assets" / "panel-activity.svg"

# Background gradient slice for this panel (must match the other panels).
TOTAL, Y0, Y1 = 1480, 330, 440
STOPS = [(0, "#5e3a86"), (.2, "#6e52b4"), (.4, "#5872cf"), (.6, "#3f66c3"), (.8, "#27408a"), (1, "#121c4a")]
FONT = "font-family=\"'Nunito','Quicksand','Varela Round','Trebuchet MS',ui-rounded,'Segoe UI',sans-serif\""


def fetch_stats():
    try:
        with urllib.request.urlopen(HACKATIME_API, timeout=10) as response:
            return json.loads(response.read().decode()).get("data", {})
    except Exception as e:
        print(f"Error fetching Hackatime stats: {e}", file=sys.stderr)
        return None


def _rgb(c):
    return [int(c[i:i + 2], 16) for i in (1, 3, 5)]


def _color_at(t):
    for (t0, c0), (t1, c1) in zip(STOPS, STOPS[1:]):
        if t <= t1:
            f = (t - t0) / (t1 - t0)
            a, b = _rgb(c0), _rgb(c1)
            return "#%02x%02x%02x" % tuple(round(a[i] + (b[i] - a[i]) * f) for i in range(3))
    return STOPS[-1][1]


def _text(x, y, s, size, weight=600, anchor="middle", opacity=1):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" {FONT} font-size="{size}" '
            f'font-weight="{weight}" fill="#fff" opacity="{opacity}">{escape(str(s))}</text>')


def build_svg(stats):
    total = stats.get("human_readable_total", "0s")
    daily = stats.get("human_readable_daily_average", "0s")
    streak = stats.get("streak", 0)
    langs = stats.get("languages", [])[:5]

    grad = "".join(
        f'<stop offset="{i / 7:.3f}" stop-color="{_color_at((Y0 + (Y1 - Y0) * i / 7) / TOTAL)}"/>'
        for i in range(8))

    o = _text(500, 70, "my coding activity", 38, 800)
    o += '<rect x="40" y="100" width="920" height="380" rx="24" fill="#fff" fill-opacity="0.11" stroke="#fff" stroke-opacity="0.35"/>'
    for x, v, label in [(90, total, "total time"), (370, daily, "daily average"), (650, f"{streak} days", "current streak")]:
        o += (f'<rect x="{x}" y="124" width="260" height="90" rx="18" fill="#fff" fill-opacity="0.1" stroke="#fff" stroke-opacity="0.25"/>'
              + _text(x + 130, 166, v, 30, 800) + _text(x + 130, 194, label, 15, 600, opacity=0.8))
    o += _text(90, 258, "top languages", 20, 800, "start")
    for i, lang in enumerate(langs):
        y = 284 + i * 34
        pct = float(lang.get("percent", 0))
        o += (_text(90, y + 13, lang.get("name", "Unknown"), 17, 700, "start")
              + f'<rect x="230" y="{y}" width="540" height="14" rx="7" fill="#fff" fill-opacity="0.15"/>'
              + f'<rect x="230" y="{y}" width="{max(pct * 5.4, 14):.1f}" height="14" rx="7" fill="url(#bar)"/>'
              + _text(790, y + 13, f"{pct:.1f}%  ·  {lang.get('text', '0m')}", 16, 600, "start"))
    o += _text(500, 462, "last updated " + datetime.now(timezone.utc).strftime("%Y-%m-%d"), 14, 600, opacity=0.65)
    o += ('<circle cx="22" cy="60" r="1.6" fill="#fff"><animate attributeName="opacity" values="0.15;0.9;0.15" dur="3s" repeatCount="indefinite"/></circle>'
          '<circle cx="978" cy="140" r="1.4" fill="#fff"><animate attributeName="opacity" values="0.9;0.15;0.9" dur="3.7s" repeatCount="indefinite"/></circle>')

    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 510" width="1000" height="510" role="img" aria-label="Hackatime coding activity">'
            f'<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1">{grad}</linearGradient>'
            '<linearGradient id="bar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffd6e4"/><stop offset="1" stop-color="#a9c8ff"/></linearGradient></defs>'
            f'<rect width="100%" height="100%" fill="url(#g)"/>{o}</svg>')


def main():
    stats = fetch_stats()
    if not stats:
        sys.exit(1)
    SVG_PATH.parent.mkdir(parents=True, exist_ok=True)
    SVG_PATH.write_text(build_svg(stats), encoding="utf-8")
    print(f"Wrote {SVG_PATH}")


if __name__ == "__main__":
    main()
