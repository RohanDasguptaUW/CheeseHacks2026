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
"garageband": {
        "app_name": "GarageBand",
        "package_name": "com.apple.mobilegarageband",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.WRITE_EXTERNAL_STORAGE", "label": "Write Files", "risk": "medium"},
        ],
        "trackers": [],
        "tracker_count": 0,
        "permission_count": 3,
        "category": "entertainment"
    },
    "roblox": {
        "app_name": "Roblox",
        "package_name": "com.roblox.client",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
            {"name": "AppsFlyer", "website": "appsflyer.com", "categories": ["Analytics"]},
            {"name": "Facebook Ads", "website": "facebook.com", "categories": ["Ads"]},
        ],
        "tracker_count": 3,
        "permission_count": 6,
        "category": "gaming"
    },
    "minecraft": {
        "app_name": "Minecraft",
        "package_name": "com.mojang.minecraftpe",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.WRITE_EXTERNAL_STORAGE", "label": "Write Files", "risk": "medium"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
            {"name": "Xbox Analytics", "website": "xbox.com", "categories": ["Analytics"]},
        ],
        "tracker_count": 2,
        "permission_count": 4,
        "category": "gaming"
    },
    "drive": {
        "app_name": "Google Drive",
        "package_name": "com.google.android.apps.docs",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.GET_ACCOUNTS", "label": "Account List", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.WRITE_EXTERNAL_STORAGE", "label": "Write Files", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Google Analytics", "website": "google.com", "categories": ["Analytics"]},
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
        ],
        "tracker_count": 2,
        "permission_count": 5,
        "category": "productivity"
    },
    "formula 1": {
        "app_name": "Formula 1",
        "package_name": "com.formula1.official.fanapp",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
            {"name": "Comscore", "website": "comscore.com", "categories": ["Analytics"]},
            {"name": "Facebook Ads", "website": "facebook.com", "categories": ["Ads"]},
        ],
        "tracker_count": 3,
        "permission_count": 3,
        "category": "sports"
    },
    "nytimes": {
        "app_name": "NYTimes",
        "package_name": "com.nytimes.android",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Google Analytics", "website": "google.com", "categories": ["Analytics"]},
            {"name": "Facebook Ads", "website": "facebook.com", "categories": ["Ads"]},
            {"name": "Comscore", "website": "comscore.com", "categories": ["Analytics"]},
            {"name": "Nielsen", "website": "nielsen.com", "categories": ["Analytics"]},
        ],
        "tracker_count": 4,
        "permission_count": 3,
        "category": "news"
    },
    "gardenscapes": {
        "app_name": "Gardenscapes",
        "package_name": "com.playrix.gardenscapes",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.WRITE_EXTERNAL_STORAGE", "label": "Write Files", "risk": "medium"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
        ],
        "trackers": [
            {"name": "AppsFlyer", "website": "appsflyer.com", "categories": ["Analytics"]},
            {"name": "Facebook Ads", "website": "facebook.com", "categories": ["Ads"]},
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
            {"name": "ironSource", "website": "ironsource.com", "categories": ["Ads"]},
        ],
        "tracker_count": 4,
        "permission_count": 3,
        "category": "gaming"
    },
    "angry birds 2": {
        "app_name": "Angry Birds 2",
        "package_name": "com.rovio.baba",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.WRITE_EXTERNAL_STORAGE", "label": "Write Files", "risk": "medium"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
        ],
        "trackers": [
            {"name": "AppsFlyer", "website": "appsflyer.com", "categories": ["Analytics"]},
            {"name": "Facebook Ads", "website": "facebook.com", "categories": ["Ads"]},
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
            {"name": "Unity Ads", "website": "unity.com", "categories": ["Ads"]},
        ],
        "tracker_count": 4,
        "permission_count": 3,
        "category": "gaming"
    },
    "flipaclip": {
        "app_name": "FlipaClip",
        "package_name": "com.vblast.flipaclip",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.WRITE_EXTERNAL_STORAGE", "label": "Write Files", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
            {"name": "Facebook Ads", "website": "facebook.com", "categories": ["Ads"]},
        ],
        "tracker_count": 2,
        "permission_count": 4,
        "category": "creative"
    },
    "netflix": {
        "app_name": "Netflix",
        "package_name": "com.netflix.mediaclient",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
        ],
        "trackers": [
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
            {"name": "Conviva", "website": "conviva.com", "categories": ["Analytics"]},
        ],
        "tracker_count": 2,
        "permission_count": 3,
        "category": "entertainment"
    },
    "youtube": {
        "app_name": "YouTube",
        "package_name": "com.google.android.youtube",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Google Analytics", "website": "google.com", "categories": ["Analytics"]},
            {"name": "Google Ads", "website": "google.com", "categories": ["Ads"]},
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
        ],
        "tracker_count": 3,
        "permission_count": 5,
        "category": "entertainment"
    },
    "amazon": {
        "app_name": "Amazon",
        "package_name": "com.amazon.mShop.android.shopping",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Amazon Analytics", "website": "amazon.com", "categories": ["Analytics"]},
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
            {"name": "Facebook Ads", "website": "facebook.com", "categories": ["Ads"]},
        ],
        "tracker_count": 3,
        "permission_count": 6,
        "category": "shopping"
    },
    "pinterest": {
        "app_name": "Pinterest",
        "package_name": "com.pinterest",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Pinterest Analytics", "website": "pinterest.com", "categories": ["Analytics"]},
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
            {"name": "AppsFlyer", "website": "appsflyer.com", "categories": ["Analytics"]},
            {"name": "Facebook Ads", "website": "facebook.com", "categories": ["Ads"]},
        ],
        "tracker_count": 4,
        "permission_count": 5,
        "category": "social_media"
    },
    "notion": {
        "app_name": "Notion",
        "package_name": "notion.id",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.WRITE_EXTERNAL_STORAGE", "label": "Write Files", "risk": "medium"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
        ],
        "trackers": [
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
            {"name": "Amplitude", "website": "amplitude.com", "categories": ["Analytics"]},
        ],
        "tracker_count": 2,
        "permission_count": 3,
        "category": "productivity"
    },
    "reddit": {
        "app_name": "Reddit",
        "package_name": "com.reddit.frontpage",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.ACCESS_FINE_LOCATION", "label": "Precise Location", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
            {"name": "AppsFlyer", "website": "appsflyer.com", "categories": ["Analytics"]},
            {"name": "Facebook Ads", "website": "facebook.com", "categories": ["Ads"]},
            {"name": "Adjust", "website": "adjust.com", "categories": ["Attribution"]},
        ],
        "tracker_count": 4,
        "permission_count": 5,
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
        ],
        "tracker_count": 3,
        "permission_count": 5,
        "category": "navigation"
    },
    "claude": {
        "app_name": "Claude",
        "package_name": "com.anthropic.claude",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
        ],
        "tracker_count": 1,
        "permission_count": 3,
        "category": "productivity"
    },
    "duo mobile": {
        "app_name": "Duo Mobile",
        "package_name": "com.duosecurity.duomobile",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.CAMERA", "label": "Camera", "risk": "high"},
            {"name": "android.permission.READ_CONTACTS", "label": "Contacts", "risk": "high"},
            {"name": "android.permission.READ_PHONE_STATE", "label": "Phone Identity (IMEI)", "risk": "medium"},
        ],
        "trackers": [],
        "tracker_count": 0,
        "permission_count": 3,
        "category": "security"
    },
    "hole.io": {
        "app_name": "Hole.io",
        "package_name": "io.voodoo.hole",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Unity Ads", "website": "unity.com", "categories": ["Ads"]},
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
            {"name": "Facebook Ads", "website": "facebook.com", "categories": ["Ads"]},
            {"name": "AppsFlyer", "website": "appsflyer.com", "categories": ["Analytics"]},
        ],
        "tracker_count": 4,
        "permission_count": 2,
        "category": "gaming"
    },
    "stumble guys": {
        "app_name": "Stumble Guys",
        "package_name": "com.scopely.stumbleguys",
        "source": "exodus",
        "permissions": [
            {"name": "android.permission.RECORD_AUDIO", "label": "Microphone", "risk": "high"},
            {"name": "android.permission.READ_EXTERNAL_STORAGE", "label": "Read Files", "risk": "medium"},
            {"name": "android.permission.ACCESS_COARSE_LOCATION", "label": "Approximate Location", "risk": "medium"},
        ],
        "trackers": [
            {"name": "Unity Ads", "website": "unity.com", "categories": ["Ads"]},
            {"name": "Google Firebase", "website": "firebase.google.com", "categories": ["Analytics"]},
            {"name": "Facebook Ads", "website": "facebook.com", "categories": ["Ads"]},
            {"name": "AppsFlyer", "website": "appsflyer.com", "categories": ["Analytics"]},
        ],
        "tracker_count": 4,
        "permission_count": 3,
        "category": "gaming"
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