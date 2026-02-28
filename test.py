from app_database import get_app_data, get_batch_data
from scorer import analyze_from_fetcher
from gemini_helper import generate_guilt_trip

print("=== TIKTOK ANALYSIS ===")
tiktok_raw = get_app_data("TikTok")
result = analyze_from_fetcher(tiktok_raw)
print(f"Score: {result['privacy_score']}/100")
print(f"Label: {result['score_label']['label']}")
print(f"Benchmark: {result['benchmarking']}")
print()

print("=== TOP RISKS ===")
high_risks = [p for p in result['permissions']
              if p['tier'] == 'HIGH']
for p in high_risks[:3]:
    print(f"🔴 {p['permission']}: {p['plain_english']}")
print()

print("=== BATCH TEST ===")
batch = get_batch_data(["Signal", "Instagram", "WhatsApp"])
for app_name, raw in batch.items():
    analysis = analyze_from_fetcher(raw)
    print(f"{app_name}: {analysis['privacy_score']}/100 "
          f"({analysis['score_label']['label']})")
print()

print("=== GEMINI GUILT TRIP ===")
guilt = generate_guilt_trip(
    result['app_name'],
    [p['permission'] for p in result['permissions']],
    result['raw_trackers'],
    result['privacy_score']
)
print(guilt)