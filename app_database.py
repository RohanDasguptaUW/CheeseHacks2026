# app_database.py
# Hardcoded real-world app data for demo
# Sources: Exodus Privacy website, published research

APP_DATABASE = {
    "tiktok": {
        "app_name": "TikTok",
        "package_name": "com.zhiliaoapp.musically",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.READ_CALL_LOG", "label": "Call Log", "risk": "high"},
            {"name": "android.permission.GET_ACCOUNTS", "label": "Account List", "risk": "high"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.WRITE_EXTERNAL_STORAGE", "label": "Write Files", "risk": "medium"},
        ],
        "trackers": [
            {"name": "AppsFlyer", "website": "appsflyer.com", "categories": ["Analytics"]},
            {"name": "Facebook Ads", "website": "facebook.com", "categories": ["Ads"]},
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
            {"name": "TikTok Analytics", "website": "tiktok.com", "categories": ["Analytics"]},
        ],
        "tracker_count": 4,
        "permission_count": 9,
        "category": "social_media"
    },
    "instagram": {
        "app_name": "Instagram",
        "package_name": "com.instagram.android",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.GET_ACCOUNTS", "label": "Account List", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Facebook Ads", "website": "facebook.com", "categories": ["Ads"]},
            {"name": "Facebook Analytics", "website": "facebook.com", "categories": ["Analytics"]},
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
        ],
        "tracker_count": 3,
        "permission_count": 6,
        "category": "social_media"
    },
    "signal": {
        "app_name": "Signal",
        "package_name": "org.thoughtcrime.securesms",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
        ],
        "trackers": [],
        "tracker_count": 0,
        "permission_count": 4,
        "category": "messaging"
    },
    "whatsapp": {
        "app_name": "WhatsApp",
        "package_name": "com.whatsapp",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.READ_CALL_LOG", "label": "Call Log", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Facebook Ads", "website": "facebook.com", "categories": ["Ads"]},
            {"name": "Facebook Analytics", "website": "facebook.com", "categories": ["Analytics"]},
        ],
        "tracker_count": 2,
        "permission_count": 6,
        "category": "messaging"
    },
    "snapchat": {
        "app_name": "Snapchat",
        "package_name": "com.snapchat.android",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.GET_ACCOUNTS", "label": "Account List", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Snap Analytics", "website": "snap.com", "categories": ["Analytics"]},
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
            {"name": "Placed", "website": "placed.com", "categories": ["Location"]},
        ],
        "tracker_count": 3,
        "permission_count": 6,
        "category": "social_media"
    },
    "google maps": {
        "app_name": "Google Maps",
        "package_name": "com.google.android.apps.maps",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Google Analytics", "website": "google.com", "categories": ["Analytics"]},
            {"name": "Google Ads", "website": "google.com", "categories": ["Ads"]},
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
            {"name": "Google CrashLytics", "website": "google.com", "categories": ["Crash reporting"]},
        ],
        "tracker_count": 4,
        "permission_count": 5,
        "category": "navigation"
    },
    "uber": {
        "app_name": "Uber",
        "package_name": "com.ubercab",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
        ],
        "trackers": [
            {"name": "AppsFlyer", "website": "appsflyer.com", "categories": ["Analytics"]},
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
            {"name": "Braze", "website": "braze.com", "categories": ["Marketing"]},
        ],
        "tracker_count": 3,
        "permission_count": 5,
        "category": "navigation"
    },
    "spotify": {
        "app_name": "Spotify",
        "package_name": "com.spotify.music",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
            {"name": "Google Ads", "website": "google.com", "categories": ["Ads"]},
        ],
        "tracker_count": 2,
        "permission_count": 4,
        "category": "entertainment"
    },
    "chrome": {
        "app_name": "Google Chrome",
        "package_name": "com.android.chrome",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Google Analytics", "website": "google.com", "categories": ["Analytics"]},
            {"name": "Google Ads", "website": "google.com", "categories": ["Ads"]},
        ],
        "tracker_count": 2,
        "permission_count": 5,
        "category": "utilities"
    },
    "gmail": {
        "app_name": "Gmail",
        "package_name": "com.google.android.gm",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.GET_ACCOUNTS", "label": "Account List", "risk": "high"},
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Google Analytics", "website": "google.com", "categories": ["Analytics"]},
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
        ],
        "tracker_count": 2,
        "permission_count": 5,
        "category": "productivity"
    },
    "facebook": {
    "app_name": "Facebook",
    "package_name": "com.facebook.katana",
    "source": "exodus",
    "permissions": [
        {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
        {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
        {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
        {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
        {"name": "android.permission.READ_CALL_LOG", "label": "Call Log", "risk": "high"},
        {"name": "android.permission.GET_ACCOUNTS", "label": "Account List", "risk": "high"},
        {"name": "android.permission.READ_SMS", "label": "Read SMS", "risk": "high"},
        {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
        {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
    ],
    "trackers": [
        {"name": "Facebook Ads", "website": "facebook.com", "categories": ["Ads"]},
        {"name": "Facebook Analytics", "website": "facebook.com", "categories": ["Analytics"]},
        {"name": "Facebook Login", "website": "facebook.com", "categories": ["Identification"]},
        {"name": "Facebook Places", "website": "facebook.com", "categories": ["Location"]},
    ],
    "tracker_count": 4,
    "permission_count": 9,
    "category": "social_media"
},
"discord": {
    "app_name": "Discord",
    "package_name": "com.discord",
    "source": "exodus",
    "permissions": [
        {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
        {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
        {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
        {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
        {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
    ],
    "trackers": [
        {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
        {"name": "Sentry", "website": "sentry.io", "categories": ["Crash reporting"]},
    ],
    "tracker_count": 2,
    "permission_count": 5,
    "category": "social_media"
},
"venmo": {
    "app_name": "Venmo",
    "package_name": "com.venmo",
    "source": "exodus",
    "permissions": [
        {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
        {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
        {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
        {"name": "android.permission.GET_ACCOUNTS", "label": "Account List", "risk": "high"},
        {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
    ],
    "trackers": [
        {"name": "Braze", "website": "braze.com", "categories": ["Marketing"]},
        {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
        {"name": "AppsFlyer", "website": "appsflyer.com", "categories": ["Analytics"]},
    ],
    "tracker_count": 3,
    "permission_count": 5,
    "category": "finance"
},
"zoom": {
    "app_name": "Zoom",
    "package_name": "us.zoom.videomeetings",
    "source": "exodus",
    "permissions": [
        {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
        {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
        {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
        {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
        {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
    ],
    "trackers": [
        {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
        {"name": "Amplitude", "website": "amplitude.com", "categories": ["Analytics"]},
    ],
    "tracker_count": 2,
    "permission_count": 5,
    "category": "productivity"
},
"doordash": {
    "app_name": "DoorDash",
    "package_name": "com.dd.doordash",
    "source": "exodus",
    "permissions": [
        {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
        {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
        {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
        {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
        {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
    ],
    "trackers": [
        {"name": "AppsFlyer", "website": "appsflyer.com", "categories": ["Analytics"]},
        {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
        {"name": "Braze", "website": "braze.com", "categories": ["Marketing"]},
        {"name": "Facebook Ads", "website": "facebook.com", "categories": ["Ads"]},
    ],
    "tracker_count": 4,
    "permission_count": 5,
    "category": "shopping"
}
}

def get_app_data(app_name: str) -> dict:
    """
    Drop-in replacement for Person 1's get_app_data()
    Returns hardcoded real data for known apps,
    falls back to Person 1's live fetcher for unknown apps
    """
    key = app_name.lower().strip()
    
    if key in APP_DATABASE:
        print(f"[Database] Found '{app_name}' in local database")
        return APP_DATABASE[key]
    
    # Fall back to Person 1's live fetcher for unknown apps
    print(f"[Database] '{app_name}' not in database, trying live fetch...")
    try:
        from data_fetcher import get_app_data as live_fetch
        return live_fetch(app_name)
    except Exception as e:
        print(f"[Database] Live fetch failed: {e}")
        return {
            "app_name": app_name,
            "source": "not_found",
            "permissions": [],
            "trackers": [],
            "tracker_count": 0,
            "permission_count": 0,
            "error": f"App not found: {app_name}"
        }


def get_batch_data(app_names: list) -> dict:
    return {name: get_app_data(name) for name in app_names}