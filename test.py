from scorer import analyze_from_fetcher
from app_database import get_app_data, get_batch_data
from gemini_helper import generate_guilt_trip, scan_apps_from_image

print("=== TIKTOK ANALYSIS ===")
tiktok_raw = get_app_data("TikTok")
result = analyze_from_fetcher(tiktok_raw)
print(f"Score: {result['privacy_score']}/100")
print(f"Label: {result['score_label']['label']}")
print()

print("=== PHONE SCREENSHOT SCAN ===")
apps_found = scan_apps_from_image("test_screenshot.jpeg")
print(f"Apps detected: {apps_found}")
print()

print("=== SCORING EACH APP ===")
for app_name in apps_found:
    raw = get_app_data(app_name)
    result = analyze_from_fetcher(raw)
    score = result['privacy_score']
    label = result['score_label']['label']
    emoji = result['score_label']['emoji']
    print(f"{emoji} {app_name}: {score}/100 - {label}")
