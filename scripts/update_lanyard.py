#!/usr/bin/env python3
"""
Fetch Lanyard data and generate an SVG with a live-ticking timer.
"""

import json
import sys
import time
import urllib.request
from pathlib import Path

LANYARD_API = "https://api.lanyard.rest/v1/users/1279876954081984628"
OUTPUT_PATH = Path(__file__).parent.parent / "dist" / "lanyard.svg"


def fetch_data():
    try:
        with urllib.request.urlopen(LANYARD_API, timeout=10) as response:
            data = json.loads(response.read().decode())
            return data.get("data", {})
    except Exception as e:
        print(f"Error fetching Lanyard data: {e}", file=sys.stderr)
        return None


def format_timer(seconds):
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes}:{secs:02d}"


def generate_svg(data):
    if not data:
        return None

    discord_user = data.get("discord_user", {})
    discord_status = data.get("discord_status", "offline")
    activities = data.get("activities", [])
    spotify = data.get("spotify", {})

    username = discord_user.get("username", "gk503")
    avatar_hash = discord_user.get("avatar", "")
    user_id = discord_user.get("id", "1279876954081984628")
    avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_hash}.png?size=128"

    status_colors = {
        "online": "#39ff14",
        "idle": "#ffe600",
        "dnd": "#ff0040",
        "offline": "#4d4d6b"
    }
    status_color = status_colors.get(discord_status, "#4d4d6b")

    timer_text = "0:00"
    progress = 0
    total_text = ""
    activity_name = ""
    activity_detail = ""
    activity_type = ""

    if spotify:
        start_time = spotify.get("timestamps", {}).get("start", 0)
        end_time = spotify.get("timestamps", {}).get("end", 0)
        if start_time:
            start_time /= 1000
            end_time /= 1000
            elapsed = max(0, int(time.time() - start_time))
            timer_text = format_timer(elapsed)
            if end_time > start_time:
                progress = min(1.0, elapsed / (end_time - start_time))
                total_text = format_timer(int(end_time - start_time))
        activity_name = spotify.get("song", "")
        activity_detail = spotify.get("artist", "")
        activity_type = "LISTENING TO SPOTIFY"
    elif activities:
        activity = activities[0]
        activity_name = activity.get("name", "")
        activity_detail = activity.get("details", "")
        activity_type = "PLAYING"
        start_time = activity.get("timestamps", {}).get("start", 0)
        if start_time:
            start_time /= 1000
            elapsed = max(0, int(time.time() - start_time))
            timer_text = format_timer(elapsed)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 150" width="400" height="150">
  <defs>
    <linearGradient id="cardBg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0a0a1f"/>
      <stop offset="1" stop-color="#04040f"/>
    </linearGradient>
    <clipPath id="avatarClip">
      <circle cx="50" cy="50" r="32"/>
    </clipPath>
  </defs>
  <rect width="400" height="150" rx="12" fill="url(#cardBg)"/>
  <rect width="400" height="150" rx="12" fill="none" stroke="#00ffff" stroke-opacity="0.3" stroke-width="1"/>
  <image href="{avatar_url}" x="18" y="18" width="64" height="64" clip-path="url(#avatarClip)"/>
  <circle cx="50" cy="50" r="32" fill="none" stroke="{status_color}" stroke-width="3"/>
  <text x="100" y="45" font-family="Arial, Helvetica, sans-serif" font-weight="700" font-size="18" fill="#ffffff">{username}</text>
  <circle cx="102" cy="62" r="5" fill="{status_color}">
    <animate attributeName="opacity" values="1;0.4;1" dur="1.5s" repeatCount="indefinite"/>
  </circle>
  <text x="112" y="66" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="{status_color}">{discord_status.upper()}</text>
  <text x="20" y="110" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#888888">{activity_type}</text>
  <text x="20" y="128" font-family="Arial, Helvetica, sans-serif" font-weight="600" font-size="13" fill="#ffffff">{activity_name}</text>
  <text x="20" y="144" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#888888">{activity_detail}</text>
  <rect x="20" y="100" width="360" height="4" rx="2" fill="#1a1a2e"/>
  <rect x="20" y="100" width="{360 * progress:.1f}" height="4" rx="2" fill="#00ffff">
    <animate attributeName="opacity" values="1;0.7;1" dur="2s" repeatCount="indefinite"/>
  </rect>
  <text x="380" y="100" text-anchor="end" font-family="'Courier New', monospace" font-size="11" fill="#00ffff">{timer_text}</text>
  <text x="380" y="114" text-anchor="end" font-family="'Courier New', monospace" font-size="9" fill="#4d4d6b">/ {total_text}</text>
  <circle cx="370" cy="30" r="4" fill="#ff0040">
    <animate attributeName="opacity" values="1;0.2;1" dur="1s" repeatCount="indefinite"/>
  </circle>
  <text x="360" y="34" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="700" fill="#ff0040">LIVE</text>
</svg>'''

    return svg


def main():
    data = fetch_data()
    if not data:
        sys.exit(1)

    svg = generate_svg(data)
    if not svg:
        print("Failed to generate SVG", file=sys.stderr)
        sys.exit(1)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(svg, encoding="utf-8")
    print(f"SVG written to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
