from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI(title="PrivacyLens API")

# 1. FIX CORS: This allows Person 3's React app to talk to your Mac
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. DATA MODELS
class AuditRequest(BaseModel):
    apps: List[str]

# 3. PRIVACY GLOSSARY (Your "Plain English" Engine)
PRIVACY_GLOSSARY = {
    "microphone": "Can listen to your room in the background. High risk for apps that don't need voice features.",
    "camera": "Can access your lens at any time. Potential for unauthorized photo/video capture.",
    "precise_location": "Tracks your exact GPS coordinates within 3 feet. Drains battery and maps your daily routine.",
    "contacts": "Uploads your friend list to their servers. Used to track people you know who aren't even on the app.",
    "storage": "Can read your personal photos and private files. Massive risk for identity or data theft.",
    "notifications": "Can send alerts to your lock screen. Low privacy risk, but high 'annoyance' factor.",
    "internet": "Required for the app to function, but also used to send your data back to company servers."
}

# 4. MOCK DATABASE (For Demoing while Person 1/2 finish their logic)
MOCK_APPS = {
    "TikTok": {"score": 28, "risk": "Critical", "perms": ["microphone", "precise_location", "contacts", "camera"]},
    "Flashlight Plus": {"score": 12, "risk": "Extreme", "perms": ["precise_location", "camera", "storage", "contacts"]},
    "Spotify": {"score": 74, "risk": "Low", "perms": ["microphone", "storage", "notifications"]},
    "Instagram": {"score": 42, "risk": "High", "perms": ["camera", "microphone", "precise_location", "contacts"]},
    "Google Maps": {"score": 55, "risk": "Medium", "perms": ["precise_location", "notifications", "internet"]}
}

# 5. ROUTES
@app.get("/")
def health_check():
    return {"status": "PrivacyLens Online", "engine": "FastAPI"}

@app.get("/app/{name}")
def get_app_analysis(name: str):
    """Detailed audit for a single app"""
    # Case-insensitive lookup
    app_key = next((k for k in MOCK_APPS if k.lower() == name.lower()), None)
    
    if not app_key:
        raise HTTPException(status_code=404, detail=f"App '{name}' not found in audit database.")
    
    data = MOCK_APPS[app_key]
    
    # Map the technical permissions to your Plain English Glossary
    analysis = [
        {"permission": p, "warning": PRIVACY_GLOSSARY.get(p, "Standard access requested.")} 
        for p in data["perms"]
    ]
    
    return {
        "app": app_key,
        "privacy_score": data["score"],
        "risk_tier": data["risk"],
        "analysis": analysis,
        "recommendation": "Restrict permissions in Settings" if data["score"] < 50 else "Safe to use"
    }

@app.get("/compare/{app1}/{app2}")
def compare_apps(app1: str, app2: str):
    """Side-by-side comparison for the UI"""
    res1 = MOCK_APPS.get(app1, {"score": 50})
    res2 = MOCK_APPS.get(app2, {"score": 50})
    
    winner = app1 if res1["score"] >= res2["score"] else app2
    
    return {
        "winner": winner,
        "comparison": {
            app1: res1["score"],
            app2: res2["score"]
        },
        "verdict": f"{winner} is significantly more private for your data."
    }

@app.post("/audit")
def full_phone_audit(request: AuditRequest):
    """The 'Bulk Upload' feature for the dashboard"""
    results = []
    total_score = 0
    
    for app_name in request.apps:
        app_data = MOCK_APPS.get(app_name, {"score": 50, "risk": "Unknown"})
        results.append({"name": app_name, "score": app_data["score"], "risk": app_data["risk"]})
        total_score += app_data["score"]
    
    avg_score = total_score / len(request.apps) if request.apps else 0
    
    return {
        "overall_health": round(avg_score),
        "total_scanned": len(request.apps),
        "breakdown": results
    }

@app.get("/timeline/{name}")
def privacy_time_machine(name: str):
    """The 'Innovation Award' feature: Tracking permission creep over time"""
    return {
        "app": name,
        "history": [
            {"year": 2020, "perms": 5, "event": "Initial Release"},
            {"year": 2022, "perms": 12, "event": "Ad-Network Integration"},
            {"year": 2024, "perms": 18, "event": "Background Tracking Added"},
            {"year": 2026, "perms": 23, "event": "Current Version"}
        ]
    }
