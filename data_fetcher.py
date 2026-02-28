#!/usr/bin/env python3
"""
data_fetcher.py — Person 1: Data Engineer
==========================================
Fetches Android app permissions + trackers.

Primary source:  Exodus Privacy API  (https://reports.exodus-privacy.eu.org)
Fallback source: Google Play Store   (via google-play-scraper)

Output schema (all public functions return this shape):
{
    "app_name":        str,
    "package_name":    str | null,
    "source":          "exodus" | "google_play" | "not_found",
    "permissions": [
        {"name": str, "label": str, "risk": "high" | "medium" | "low"}
    ],
    "trackers": [
        {"name": str, "website": str, "categories": [str]}
    ],
    "tracker_count":    int,
    "permission_count": int,
    "cached":           bool,
    "fetched_at":       ISO-8601 str,
    "error":            str | null   # only present on failure
}

Usage:
    python data_fetcher.py TikTok
    python data_fetcher.py TikTok Instagram Signal   # batch
    python data_fetcher.py --clear-cache
"""

import json
import os
import sys
from datetime import datetime, timezone
from typing import Optional

import requests

# ── Constants ─────────────────────────────────────────────────────────────────

CACHE_FILE = "cache/app_data.json"

EXODUS_SEARCH  = "https://reports.exodus-privacy.eu.org/api/search/{query}/"
EXODUS_REPORTS = "https://reports.exodus-privacy.eu.org/api/applications/{handle}/reports"

HEADERS = {
    "Accept":     "application/json",
    "User-Agent": "CheeseHacks2026/1.0 (privacy-scanner hackathon project)",
}

REQUEST_TIMEOUT = 10  # seconds

# ── Permission metadata ────────────────────────────────────────────────────────
# Maps Android permission constant → human label + risk tier.
# Person 2 uses "risk" + "weight" for scoring; weights are stored here so the
# two modules stay in sync.  Add more as needed.

PERMISSION_META: dict[str, dict] = {
    "android.permission.RECORD_AUDIO":           {"label": "Microphone",            "risk": "high",   "weight": -20},
    "android.permission.ACCESS_FINE_LOCATION":   {"label": "Precise Location",      "risk": "high",   "weight": -15},
    "android.permission.CAMERA":                 {"label": "Camera",                "risk": "high",   "weight": -15},
    "android.permission.READ_CONTACTS":          {"label": "Contacts",              "risk": "high",   "weight": -12},
    "android.permission.READ_CALL_LOG":          {"label": "Call Log",              "risk": "high",   "weight": -12},
    "android.permission.READ_SMS":               {"label": "Read SMS",              "risk": "high",   "weight": -12},
    "android.permission.SEND_SMS":               {"label": "Send SMS",              "risk": "high",   "weight": -12},
    "android.permission.PROCESS_OUTGOING_CALLS": {"label": "Outgoing Calls",        "risk": "high",   "weight": -10},
    "android.permission.GET_ACCOUNTS":           {"label": "Account List",          "risk": "high",   "weight": -10},
    "android.permission.USE_BIOMETRIC":          {"label": "Biometrics",            "risk": "medium", "weight": -6},
    "android.permission.BODY_SENSORS":           {"label": "Body Sensors",          "risk": "medium", "weight": -6},
    "android.permission.ACTIVITY_RECOGNITION":   {"label": "Physical Activity",     "risk": "medium", "weight": -5},
    "android.permission.ACCESS_COARSE_LOCATION": {"label": "Approximate Location",  "risk": "medium", "weight": -8},
    "android.permission.READ_PHONE_STATE":       {"label": "Phone Identity (IMEI)", "risk": "medium", "weight": -6},
    "android.permission.BLUETOOTH_SCAN":         {"label": "Bluetooth Scan",        "risk": "medium", "weight": -4},
    "android.permission.READ_EXTERNAL_STORAGE":  {"label": "Read Files",            "risk": "medium", "weight": -4},
    "android.permission.WRITE_EXTERNAL_STORAGE": {"label": "Write Files",           "risk": "medium", "weight": -4},
    "android.permission.INTERNET":               {"label": "Internet",              "risk": "low",    "weight": -1},
    "android.permission.BLUETOOTH":              {"label": "Bluetooth",             "risk": "low",    "weight": -1},
    "android.permission.VIBRATE":                {"label": "Vibrate",               "risk": "low",    "weight":  0},
    "android.permission.RECEIVE_BOOT_COMPLETED": {"label": "Start on Boot",         "risk": "low",    "weight": -2},
    "android.permission.FOREGROUND_SERVICE":     {"label": "Foreground Service",    "risk": "low",    "weight": -1},
}

# Keywords for inferring risk when Exodus returns human-readable strings (Play fallback)
_HIGH_KEYWORDS   = ["microphone", "location", "camera", "contact", "sms", "call", "phone", "biometric", "account"]
_MEDIUM_KEYWORDS = ["storage", "file", "bluetooth", "sensor", "activity", "identity"]


# ── Cache helpers ──────────────────────────────────────────────────────────────

def _load_cache() -> dict:
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE) as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def _save_cache(cache: dict) -> None:
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)


def clear_cache() -> None:
    """Wipe the on-disk cache (useful during testing)."""
    if os.path.exists(CACHE_FILE):
        os.remove(CACHE_FILE)
        print("[cache] Cleared.")
    else:
        print("[cache] Nothing to clear.")


# ── Permission helpers ─────────────────────────────────────────────────────────

def _enrich_permission(raw: str) -> dict:
    """Turn a raw Android permission string into a labelled, risk-rated dict."""
    meta = PERMISSION_META.get(raw)
    if meta:
        return {"name": raw, "label": meta["label"], "risk": meta["risk"]}
    # Fallback: derive label from the constant name itself
    label = raw.split(".")[-1].replace("_", " ").title()
    return {"name": raw, "label": label, "risk": "low"}


def _infer_risk_from_label(label: str) -> str:
    """Infer risk tier from a human-readable permission string (Play Store fallback)."""
    low = label.lower()
    if any(kw in low for kw in _HIGH_KEYWORDS):
        return "high"
    if any(kw in low for kw in _MEDIUM_KEYWORDS):
        return "medium"
    return "low"


# ── Exodus Privacy API ─────────────────────────────────────────────────────────

def _exodus_search(query: str) -> Optional[dict]:
    """
    Search Exodus for an app by name or package.
    Returns the first matching app entry, or None.
    """
    url = EXODUS_SEARCH.format(query=query)
    try:
        res = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        res.raise_for_status()
        data = res.json()
    except requests.RequestException as e:
        print(f"[Exodus search error] {e}")
        return None

    # Exodus may return {"applications": [...]} or a flat list
    apps = (
        data.get("applications")
        or data.get("apps")
        or data.get("results")
        or (data if isinstance(data, list) else [])
    )

    if not apps:
        print(f"[Exodus] No results for '{query}'")
        return None

    return apps[0]


def _exodus_latest_report(handle: str) -> Optional[dict]:
    """Fetch the latest analysis report for a package handle from Exodus."""
    url = EXODUS_REPORTS.format(handle=handle)
    try:
        res = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        res.raise_for_status()
        data = res.json()
    except requests.RequestException as e:
        print(f"[Exodus report error] {e}")
        return None

    reports = data.get("reports") or (data if isinstance(data, list) else [])
    if not reports:
        return None
    return reports[0]  # most recent first


def _fetch_from_exodus(app_name: str) -> Optional[dict]:
    """Full Exodus pipeline: search → latest report → clean JSON."""
    print(f"[Exodus] Searching for '{app_name}'...")
    entry = _exodus_search(app_name)
    if not entry:
        return None

    handle = entry.get("handle") or entry.get("package_name") or entry.get("app_pkg")
    name   = entry.get("name") or app_name
    if not handle:
        print(f"[Exodus] Found entry but no package handle for '{app_name}'")
        return None

    print(f"[Exodus] Found '{name}' ({handle}), fetching report...")
    report = _exodus_latest_report(handle)
    if not report:
        print(f"[Exodus] No report available for '{handle}'")
        return None

    # ── Permissions ──
    raw_perms = report.get("permissions") or []
    permissions = []
    for p in raw_perms:
        if isinstance(p, dict):
            perm_name = p.get("name") or p.get("permission") or ""
        else:
            perm_name = str(p)
        if perm_name:
            permissions.append(_enrich_permission(perm_name))

    # ── Trackers ──
    raw_trackers = report.get("trackers") or []
    trackers = []
    for t in raw_trackers:
        if isinstance(t, dict):
            trackers.append({
                "name":       t.get("name", "Unknown Tracker"),
                "website":    t.get("website", ""),
                "categories": t.get("categories") or [],
            })
        else:
            # Sometimes Exodus returns tracker IDs; keep them labelled
            trackers.append({"name": f"Tracker #{t}", "website": "", "categories": []})

    return {
        "app_name":        name,
        "package_name":    handle,
        "source":          "exodus",
        "permissions":     permissions,
        "trackers":        trackers,
        "tracker_count":   len(trackers),
        "permission_count": len(permissions),
        "cached":          False,
        "fetched_at":      datetime.now(timezone.utc).isoformat(),
        "error":           None,
    }


# ── Google Play Store fallback ─────────────────────────────────────────────────

def _fetch_from_play_store(app_name: str) -> Optional[dict]:
    """
    Fallback for apps not in Exodus.
    Requires:  pip install google-play-scraper
    Returns permissions from Play Store listing (no tracker data available here).
    """
    try:
        from google_play_scraper import app as gps_app, search as gps_search
    except ImportError:
        print("[Play fallback] google-play-scraper not installed — run: pip install google-play-scraper")
        return None

    print(f"[Play Store] Searching for '{app_name}'...")
    try:
        results = gps_search(app_name, n_hits=3, lang="en", country="us")
    except Exception as e:
        print(f"[Play Store search error] {e}")
        return None

    if not results:
        return None

    package_name = results[0].get("appId")
    if not package_name:
        return None

    print(f"[Play Store] Fetching details for '{package_name}'...")
    try:
        details = gps_app(package_name, lang="en", country="us")
    except Exception as e:
        print(f"[Play Store details error] {e}")
        return None

    raw_perms = details.get("permissions") or []
    permissions = []
    for p in raw_perms:
        label = str(p)
        permissions.append({
            "name":  label,
            "label": label.title(),
            "risk":  _infer_risk_from_label(label),
        })

    return {
        "app_name":        details.get("title") or app_name,
        "package_name":    package_name,
        "source":          "google_play",
        "permissions":     permissions,
        "trackers":        [],   # Play Store doesn't expose tracker data
        "tracker_count":   0,
        "permission_count": len(permissions),
        "cached":          False,
        "fetched_at":      datetime.now(timezone.utc).isoformat(),
        "error":           None,
        "note":            "Tracker data unavailable — app not indexed by Exodus Privacy",
    }


# ── Not-found sentinel ─────────────────────────────────────────────────────────

def _not_found(app_name: str) -> dict:
    return {
        "app_name":        app_name,
        "package_name":    None,
        "source":          "not_found",
        "permissions":     [],
        "trackers":        [],
        "tracker_count":   0,
        "permission_count": 0,
        "cached":          False,
        "fetched_at":      datetime.now(timezone.utc).isoformat(),
        "error":           f"No data found for '{app_name}' in Exodus or Google Play.",
    }


# ── Public API ─────────────────────────────────────────────────────────────────

def get_app_data(app_name: str) -> dict:
    """
    Fetch permissions + trackers for a single app.

    1. Checks disk cache first.
    2. Tries Exodus Privacy API.
    3. Falls back to Google Play Store scraper.
    4. Returns a not-found sentinel if both fail.

    Results are persisted to cache/app_data.json so repeat calls are instant.
    """
    cache = _load_cache()
    key   = app_name.lower().strip()

    if key in cache:
        result = dict(cache[key])
        result["cached"] = True
        return result

    result = _fetch_from_exodus(app_name) or _fetch_from_play_store(app_name) or _not_found(app_name)

    cache[key] = result
    _save_cache(cache)
    return result


def get_batch_data(app_names: list[str]) -> dict[str, dict]:
    """
    Fetch data for multiple apps at once.

    Returns a dict keyed by the original app name strings.

    Example:
        results = get_batch_data(["TikTok", "Signal", "Instagram"])
        print(results["TikTok"]["tracker_count"])   # → e.g. 9
        print(results["Signal"]["tracker_count"])   # → e.g. 0
    """
    return {name: get_app_data(name) for name in app_names}


# ── CLI ────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    args = sys.argv[1:]

    if not args or args == ["--help"]:
        print(__doc__)
        sys.exit(0)

    if args == ["--clear-cache"]:
        clear_cache()
        sys.exit(0)

    if len(args) == 1:
        output = get_app_data(args[0])
    else:
        output = get_batch_data(args)

    print(json.dumps(output, indent=2))
