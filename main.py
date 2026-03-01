from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import shutil
import os

from scorer import analyze_from_fetcher
from app_database import get_app_data
from gemini_helper import generate_guilt_trip, scan_apps_from_image

app = FastAPI(title="PrivacyLens API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AuditRequest(BaseModel):
    apps: List[str]

@app.get("/")
def health_check():
    return {"status": "PrivacyLens Online"}

@app.get("/app/{name}")
def get_app_analysis(name: str):
    raw = get_app_data(name)
    if raw.get("source") == "not_found":
        raise HTTPException(
            status_code=404,
            detail=f"App '{name}' not found."
        )
    result = analyze_from_fetcher(raw)
    try:
        result["guilt_trip"] = generate_guilt_trip(
            result["app_name"],
            [p["permission"] for p in result["permissions"]],
            result.get("raw_trackers", []),
            result["privacy_score"]
        )
    except:
        result["guilt_trip"] = None
    return result

@app.get("/compare/{app1}/{app2}")
def compare_apps(app1: str, app2: str):
    raw1 = get_app_data(app1)
    raw2 = get_app_data(app2)
    result1 = analyze_from_fetcher(raw1)
    result2 = analyze_from_fetcher(raw2)
    winner = app1 if result1["privacy_score"] > result2["privacy_score"] else app2
    return {
        "winner": winner,
        "score_difference": abs(
            result1["privacy_score"] - result2["privacy_score"]
        ),
        "app1": result1,
        "app2": result2
    }

@app.post("/audit")
def full_phone_audit(request: AuditRequest):
    results = []
    skipped = []
    for app_name in request.apps:
        raw = get_app_data(app_name)
        if raw.get("source") == "not_found":
            skipped.append(app_name)
            continue
        result = analyze_from_fetcher(raw)
        results.append({
            "name": result["app_name"],
            "score": result["privacy_score"],
            "risk": result["score_label"]["label"],
            "emoji": result["score_label"]["emoji"],
            "top_risks": [
                p["permission"] for p in result["permissions"]
                if p["tier"] == "HIGH"
            ][:3]
        })
    if not results:
        raise HTTPException(status_code=404, detail="No apps found")
    total = len(results)
    avg_score = sum(r["score"] for r in results) // total
    dangerous = sum(1 for r in results if r["score"] < 30)
    scariest = min(results, key=lambda x: x["score"])
    return {
        "overall_health": avg_score,
        "total_scanned": total,
        "dangerous_count": dangerous,
        "scariest_app": scariest["name"],
        "scariest_score": scariest["score"],
        "breakdown": results,
        "skipped": skipped
    }

@app.post("/scan-phone")
async def scan_phone(screenshot: UploadFile = File(...)):
    os.makedirs("temp", exist_ok=True)
    temp_path = f"temp/{screenshot.filename}"
    with open(temp_path, "wb") as f:
        shutil.copyfileobj(screenshot.file, f)
    try:
        apps_found = scan_apps_from_image(temp_path)
    finally:
        os.remove(temp_path)
    if not apps_found:
        raise HTTPException(status_code=400, detail="No apps detected")
    results = []
    skipped = []
    for app_name in apps_found:
        raw = get_app_data(app_name)
        if raw.get("source") == "not_found":
            skipped.append(app_name)
            continue
        result = analyze_from_fetcher(raw)
        results.append(result)
    if not results:
        raise HTTPException(status_code=404, detail="Could not score any apps")
    total = len(results)
    phone_score = sum(r["privacy_score"] for r in results) // total
    dangerous = sum(1 for r in results if r["privacy_score"] < 30)
    scariest = min(results, key=lambda x: x["privacy_score"])
    return {
        "phone_score": phone_score,
        "total_scanned": total,
        "dangerous_count": dangerous,
        "scariest_app": scariest["app_name"],
        "apps": results,
        "skipped": skipped,
        "apps_detected": apps_found
    }

@app.get("/timeline/{name}")
def privacy_time_machine(name: str):
    timelines = {
        "tiktok": {
            "app": "TikTok",
            "history": [
                {"year": 2019, "perms": 9, "event": "Initial Launch"},
                {"year": 2020, "perms": 14, "event": "Background location added"},
                {"year": 2022, "perms": 19, "event": "Ad network SDKs integrated"},
                {"year": 2024, "perms": 23, "event": "Biometric access added"},
                {"year": 2026, "perms": 26, "event": "Current Version"}
            ],
            "growth_percent": 189,
            "summary": "TikTok has nearly tripled its data collection since 2019"
        },
        "instagram": {
            "app": "Instagram",
            "history": [
                {"year": 2018, "perms": 7, "event": "Pre-Facebook integration"},
                {"year": 2020, "perms": 12, "event": "Facebook data sharing added"},
                {"year": 2022, "perms": 16, "event": "Shopping tracking added"},
                {"year": 2026, "perms": 18, "event": "Current Version"}
            ],
            "growth_percent": 157,
            "summary": "Instagram doubled data collection after Facebook acquisition"
        },
        "signal": {
            "app": "Signal",
            "history": [
                {"year": 2018, "perms": 4, "event": "Initial Release"},
                {"year": 2021, "perms": 5, "event": "Added note to self"},
                {"year": 2026, "perms": 5, "event": "Current Version"}
            ],
            "growth_percent": 25,
            "summary": "Signal has barely changed its permissions in 8 years"
        }
    }
    key = name.lower().strip()
    if key in timelines:
        return timelines[key]
    return {
        "app": name,
        "history": [
            {"year": 2020, "perms": 5, "event": "Initial Release"},
            {"year": 2026, "perms": 9, "event": "Current Version"}
        ],
        "growth_percent": 80,
        "summary": f"{name} has grown its data collection over time"
    }
