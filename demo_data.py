# demo_data.py — hardcoded fallback data for demo apps
# Based on real Exodus Privacy research data

DEMO_APPS = {
    "com.zhiliaoapp.musically": {
        "app_name": "TikTok",
        "package_name": "com.zhiliaoapp.musically",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.GET_ACCOUNTS", "label": "Account List", "risk": "high"},
            {"name": "android.permission.READ_PHONE_STATE", "label": "Phone Identity (IMEI)", "risk": "medium"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.WRITE_EXTERNAL_STORAGE", "label": "Write Files", "risk": "medium"},
            {"name": "android.permission.RECEIVE_BOOT_COMPLETED", "label": "Start on Boot", "risk": "low"},
            {"name": "android.permission.INTERNET", "label": "Internet", "risk": "low"},
        ],
        "trackers": [
            {"name": "Facebook Ads", "website": "https://facebook.com", "categories": ["Advertising"]},
            {"name": "Google Firebase Analytics", "website": "https://firebase.google.com", "categories": ["Analytics"]},
            {"name": "AppsFlyer", "website": "https://appsflyer.com", "categories": ["Attribution"]},
            {"name": "Pangle", "website": "https://www.pangleglobal.com", "categories": ["Advertising"]},
        ],
        "tracker_count": 4,
        "permission_count": 11,
        "cached": False,
        "error": None,
    },
    "com.instagram.android": {
        "app_name": "Instagram",
        "package_name": "com.instagram.android",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.GET_ACCOUNTS", "label": "Account List", "risk": "high"},
            {"name": "android.permission.READ_PHONE_STATE", "label": "Phone Identity (IMEI)", "risk": "medium"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.WRITE_EXTERNAL_STORAGE", "label": "Write Files", "risk": "medium"},
            {"name": "android.permission.INTERNET", "label": "Internet", "risk": "low"},
        ],
        "trackers": [
            {"name": "Facebook Ads", "website": "https://facebook.com", "categories": ["Advertising"]},
            {"name": "Google Firebase Analytics", "website": "https://firebase.google.com", "categories": ["Analytics"]},
            {"name": "Branch", "website": "https://branch.io", "categories": ["Attribution"]},
        ],
        "tracker_count": 3,
        "permission_count": 9,
        "cached": False,
        "error": None,
    },
    "com.spotify.music": {
        "app_name": "Spotify",
        "package_name": "com.spotify.music",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.BLUETOOTH", "label": "Bluetooth", "risk": "low"},
            {"name": "android.permission.INTERNET", "label": "Internet", "risk": "low"},
        ],
        "trackers": [
            {"name": "Google Firebase Analytics", "website": "https://firebase.google.com", "categories": ["Analytics"]},
            {"name": "Crashlytics", "website": "https://firebase.google.com/crashlytics", "categories": ["Crash Reporting"]},
        ],
        "tracker_count": 2,
        "permission_count": 5,
        "cached": False,
        "error": None,
    },
    "org.thoughtcrime.securesms": {
        "app_name": "Signal",
        "package_name": "org.thoughtcrime.securesms",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.READ_SMS", "label": "Read SMS", "risk": "high"},
            {"name": "android.permission.INTERNET", "label": "Internet", "risk": "low"},
        ],
        "trackers": [],
        "tracker_count": 0,
        "permission_count": 5,
        "cached": False,
        "error": None,
    },
    "com.whatsapp": {
        "app_name": "WhatsApp",
        "package_name": "com.whatsapp",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.READ_PHONE_STATE", "label": "Phone Identity (IMEI)", "risk": "medium"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.INTERNET", "label": "Internet", "risk": "low"},
        ],
        "trackers": [
            {"name": "Facebook Ads", "website": "https://facebook.com", "categories": ["Advertising"]},
        ],
        "tracker_count": 1,
        "permission_count": 7,
        "cached": False,
        "error": None,
    },
    "com.snapchat.android": {
        "app_name": "Snapchat",
        "package_name": "com.snapchat.android",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.READ_PHONE_STATE", "label": "Phone Identity (IMEI)", "risk": "medium"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.INTERNET", "label": "Internet", "risk": "low"},
        ],
        "trackers": [
            {"name": "Snap Ads", "website": "https://snapchat.com", "categories": ["Advertising"]},
            {"name": "Google Firebase Analytics", "website": "https://firebase.google.com", "categories": ["Analytics"]},
            {"name": "Amplitude", "website": "https://amplitude.com", "categories": ["Analytics"]},
        ],
        "tracker_count": 3,
        "permission_count": 7,
        "cached": False,
        "error": None,
    },
}

# Also map friendly names to package names for convenience
NAME_TO_PACKAGE = {
    "tiktok": "com.zhiliaoapp.musically",
    "instagram": "com.instagram.android",
    "spotify": "com.spotify.music",
    "signal": "org.thoughtcrime.securesms",
    "whatsapp": "com.whatsapp",
    "snapchat": "com.snapchat.android",
}

def get_demo_data(query: str):
    """Check demo data by package name or friendly name."""
    key = query.lower().strip()
    # Try friendly name first
    pkg = NAME_TO_PACKAGE.get(key)
    if pkg:
        return DEMO_APPS.get(pkg)
    # Try direct package name
    return DEMO_APPS.get(key)