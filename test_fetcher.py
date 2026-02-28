#!/usr/bin/env python3
"""
Quick smoke-test for data_fetcher.py.

Run:  python test_fetcher.py
"""

import json
from data_fetcher import get_app_data, get_batch_data, clear_cache

# ── Demo apps that should have high tracker counts → good for judging reactions
DEMO_APPS = [
    "TikTok",
    "Instagram",
    "Spotify",
    "Signal",
    "Flashlight",   # expect weird permissions for a simple app
]

def print_summary(name: str, data: dict) -> None:
    src    = data["source"]
    perms  = data["permission_count"]
    tracks = data["tracker_count"]
    cached = "CACHED" if data["cached"] else "live"
    err    = f'  ERROR: {data["error"]}' if data.get("error") else ""
    high   = [p["label"] for p in data["permissions"] if p["risk"] == "high"]

    print(f"\n{'─'*50}")
    print(f"  {name}  [{src}] [{cached}]")
    print(f"  Permissions: {perms}   Trackers: {tracks}")
    if high:
        print(f"  High-risk:   {', '.join(high)}")
    if data["trackers"]:
        tracker_names = [t["name"] for t in data["trackers"][:5]]
        print(f"  Trackers:    {', '.join(tracker_names)}")
    if err:
        print(err)

if __name__ == "__main__":
    print("=== Single app fetch ===")
    tiktok = get_app_data("TikTok")
    print_summary("TikTok", tiktok)

    print("\n\n=== Batch fetch ===")
    results = get_batch_data(DEMO_APPS)
    for app_name, data in results.items():
        print_summary(app_name, data)

    print("\n\n=== Full JSON for Signal (expected low trackers) ===")
    print(json.dumps(results.get("Signal", {}), indent=2))

    print("\n\n=== Cache test (second call should be instant + cached=True) ===")
    tiktok2 = get_app_data("TikTok")
    assert tiktok2["cached"] is True, "Expected cached=True on second call"
    print("  PASS — cache working correctly")
