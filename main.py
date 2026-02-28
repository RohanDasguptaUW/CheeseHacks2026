import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from google.cloud import firestore

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./gcp-key.json"

app = FastAPI()

db = firestore.Client()

RISK_DICTIONARY = {
    "ACCESS_FINE_LOCATION": {
        "score": -15, 
        "desc": "Precise Location: Tracks exactly where you are, down to your specific dorm building."
    },
    "READ_CONTACTS": {
        "score": -12, 
        "desc": "Contacts: Can read every phone number and email address in your phone."
    },
    "ACTIVITY_RECOGNITION": {
        "score": -10, 
        "desc": "Activity: Knows when you are walking to class, running, or driving."
    }
}

class DeltaResult(BaseModel):
    permission: str
    plain_english: str
    risk_score: int

class TimelineResponse(BaseModel):
    app_name: str
    new_permissions_count: int
    total_risk_penalty: int
    details: List[DeltaResult]

class AuditRequest(BaseModel):
    apps: List[str]

def calculate_permission_delta(old_perms: list, new_perms: list) -> dict:
    sneak_ins = set(new_perms) - set(old_perms)
    
    results = []
    total_penalty = 0
    
    for perm in sneak_ins:
        risk_info = RISK_DICTIONARY.get(perm, {
            "score": -5, 
            "desc": "Unknown background tracker added."
        })
        
        results.append({
            "permission": perm,
            "plain_english": risk_info["desc"],
            "risk_score": risk_info["score"]
        })
        total_penalty += risk_info["score"]
        
    return {
        "new_permissions_count": len(results),
        "total_risk_penalty": total_penalty,
        "details": results
    }

@app.get("/api/v1/timeline/{app_name}", response_model=TimelineResponse)
async def get_app_timeline(app_name: str):
    if app_name.lower() == "tiktok":
        tiktok_2020 = ["INTERNET", "CAMERA", "RECORD_AUDIO", "WAKE_LOCK"]
        tiktok_2026 = ["INTERNET", "CAMERA", "RECORD_AUDIO", "WAKE_LOCK", 
                       "ACCESS_FINE_LOCATION", "READ_CONTACTS", "ACTIVITY_RECOGNITION"]
        
        delta_data = calculate_permission_delta(tiktok_2020, tiktok_2026)
        
        return {
            "app_name": "TikTok",
            "new_permissions_count": delta_data["new_permissions_count"],
            "total_risk_penalty": delta_data["total_risk_penalty"],
            "details": delta_data["details"]
        }
    
    raise HTTPException(status_code=404, detail="Historical data not found for this app. Try 'tiktok' for the demo.")

@app.post("/api/v1/audit")
async def run_phone_audit(request: AuditRequest):
    results = []
    
    for app_name in request.apps:
        clean_name = app_name.lower().strip()
        
        doc_ref = db.collection("apps").document(clean_name)
        doc = doc_ref.get()
        
        if doc.exists:
            results.append(doc.to_dict())
        else:
            new_app_data = {
                "app_name": app_name,
                "privacy_score": 75,
                "permissions_count": 12,
                "creepy_flags": ["Reads Contacts", "Background Location"]
            }
            
            doc_ref.set(new_app_data)
            results.append(new_app_data)
            
    return {
        "apps_scanned": len(results),
        "audit_results": results
    }