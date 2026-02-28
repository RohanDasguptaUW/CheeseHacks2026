# test.py
from scorer import full_app_analysis
from gemini_helper import generate_guilt_trip

# Test 1: TikTok (should score very low)
tiktok_data = {
    "name": "TikTok",
    "permissions": [
        "microphone",
        "precise_location",
        "camera",
        "contacts",
        "background_location"
    ],
    "trackers": [
        "appsflyer",
        "facebook",
        "google_ads",
        "tiktok_analytics"
    ],
    "category": "social_media",
    "version_history": [
        {
            "version": "1.0",
            "permissions": ["camera", "microphone"]
        },
        {
            "version": "current",
            "permissions": [
                "microphone", "precise_location",
                "camera", "contacts",
                "background_location"
            ]
        }
    ]
}

# Test 2: Notes app (should score high)
notes_data = {
    "name": "Simple Notes",
    "permissions": ["storage"],
    "trackers": [],
    "category": "productivity"
}

print("=== TIKTOK ANALYSIS ===")
result = full_app_analysis(tiktok_data)
print(f"Score: {result['privacy_score']}/100")
print(f"Label: {result['score_label']['label']}")
print(f"Benchmark: {result['benchmarking']}")
print(f"Time Machine: {result['time_machine']['summary']}")
print(f"Alternative: {result['alternative']}")
print()

print("=== NOTES APP ANALYSIS ===")
result2 = full_app_analysis(notes_data)
print(f"Score: {result2['privacy_score']}/100")
print(f"Label: {result2['score_label']['label']}")
print()

print("=== GEMINI GUILT TRIP ===")
guilt = generate_guilt_trip(
    "TikTok",
    tiktok_data["permissions"],
    tiktok_data["trackers"],
    15
)
print(guilt)