#!/usr/bin/env python3
"""
Fetch Hackatime stats and update README.md
"""

import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


HACKATIME_API = "https://hackatime.hackclub.com/api/v1/users/GK503/stats"
README_PATH = Path(__file__).parent.parent / "README.md"


def fetch_stats():
    """Fetch stats from Hackatime API."""
    try:
        with urllib.request.urlopen(HACKATIME_API, timeout=10) as response:
            data = json.loads(response.read().decode())
            return data.get("data", {})
    except Exception as e:
        print(f"Error fetching Hackatime stats: {e}", file=sys.stderr)
        return None


def format_stats(stats):
    """Format stats for README."""
    if not stats:
        return None

    total_seconds = stats.get("total_seconds", 0)
    human_readable_total = stats.get("human_readable_total", "0s")
    human_readable_daily = stats.get("human_readable_daily_average", "0s")
    languages = stats.get("languages", [])
    streak = stats.get("streak", 0)
    username = stats.get("username", "GK503")

    # Top 5 languages
    top_langs = languages[:5]

    lines = []
    lines.append("### `HACKATIME STATS`")
    lines.append("")
    lines.append(f"> Last updated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| **Total Time** | `{human_readable_total}` |")
    lines.append(f"| **Daily Average** | `{human_readable_daily}` |")
    lines.append(f"| **Current Streak** | `{streak} days` |")
    lines.append("")
    lines.append("**Top Languages**")
    lines.append("")
    lines.append("| Language | Time | % |")
    lines.append("|----------|------|---|")

    for lang in top_langs:
        name = lang.get("name", "Unknown")
        text = lang.get("text", "0m")
        percent = lang.get("percent", 0)
        color = lang.get("color", "#888888")
        lines.append(f"| <span style='color:{color}'>●</span> {name} | `{text}` | {percent:.1f}% |")

    lines.append("")
    lines.append(f"[View full profile on Hackatime](https://hackati.me/GK503)")

    return "\n".join(lines)


def update_readme(stats_content):
    """Update README.md with Hackatime stats."""
    if not stats_content:
        print("No stats content to write")
        return False

    readme_text = README_PATH.read_text(encoding="utf-8")

    replacement = stats_content + "\n"

    pattern = r"(### `HACKATIME STATS`\n.*?)(?=\n### |\Z)"
    new_readme = re.sub(pattern, replacement, readme_text, flags=re.DOTALL)

    if new_readme == readme_text:
        # Section not found, append after PLAYER STATS
        player_stats_pattern = r"(### `PLAYER STATS`\n.*?)(?=\n### |\Z)"
        match = re.search(player_stats_pattern, readme_text, flags=re.DOTALL)
        if match:
            insert_pos = match.end()
            new_readme = readme_text[:insert_pos] + "\n\n" + stats_content + "\n" + readme_text[insert_pos:]
        else:
            print("Could not find PLAYER STATS section", file=sys.stderr)
            return False

    README_PATH.write_text(new_readme, encoding="utf-8")
    print("README.md updated successfully")
    return True


def main():
    stats = fetch_stats()
    if not stats:
        sys.exit(1)

    stats_content = format_stats(stats)
    if not stats_content:
        print("Failed to format stats")
        sys.exit(1)

    if not update_readme(stats_content):
        sys.exit(1)


if __name__ == "__main__":
    main()