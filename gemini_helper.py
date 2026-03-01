import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_guilt_trip(app_name, permissions, trackers, score):
    prompt = f"""
    App name: {app_name}
    Privacy Score: {score}/100 (lower is worse)
    Permissions: {', '.join(permissions)}
    Number of ad trackers: {len(trackers)}
    
    Write exactly 2-3 sentences explaining what 
    this means for a college student in plain English.
    Be specific about real world impact.
    No technical jargon. Make it personal and 
    slightly alarming but completely factual.
    Do not use bullet points.
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text


def analyze_privacy_policy(policy_text):
    prompt = f"""
    Here is a privacy policy:
    {policy_text[:3000]}
    
    Extract exactly 3 bullet points of the most
    concerning things this policy allows the company
    to do with user data. Be specific and alarming
    but factual. Write for a college student audience.
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def scan_apps_from_image(image_path: str) -> list:
    """
    Takes a screenshot of phone app drawer
    Returns list of app names found in image
    Uses Gemini Vision - no extra setup needed!
    """
    import base64
    
    # Read and encode the image
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(
            image_file.read()
        ).decode("utf-8")
    
    # Ask Gemini to read all app names from image
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            {
                "parts": [
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",
                            "data": image_data
                        }
                    },
                    {
                        "text": """
                        Look at this screenshot of a phone.
                        List ONLY the app names you can see.
                        Return them as a simple comma separated 
                        list with nothing else.
                        Example: TikTok, Instagram, Spotify
                        Do not include any other text.
                        """
                    }
                ]
            }
        ]
    )
    
    # Parse comma separated response into list
    raw = response.text.strip()
    apps = [app.strip() for app in raw.split(",")]
    apps = [app for app in apps if len(app) > 1]
    
    print(f"[Vision] Found apps: {apps}")
    return apps

def generate_app_data(app_name: str) -> dict:
    """
    Uses Gemini to generate realistic privacy data for any app
    """
    prompt = f"""
    You are a privacy researcher. Generate realistic Android privacy data for the app "{app_name}".
    
    Return ONLY a JSON object with this exact structure, nothing else:
    {{
        "app_name": "{app_name}",
        "package_name": "the.android.package.name",
        "permissions": [
            {{"name": "android.permission.PERMISSION_NAME", "label": "Human Readable Name", "risk": "high|medium|low"}}
        ],
        "trackers": [
            {{"name": "Tracker Name", "website": "tracker.com", "categories": ["Analytics|Ads|Attribution|Crash reporting"]}}
        ]
    }}
    
    Rules:
    - Use real Android permission names (android.permission.X format)
    - Only include permissions this type of app would realistically need
    - Only include trackers this type of app would realistically use
    - Risk levels: high for location/mic/camera/contacts, medium for storage/phone state, low for internet/boot
    - Be accurate based on what you know about this app
    - Return ONLY the JSON, no markdown, no explanation
    """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    import json
    raw = response.text.strip().replace("```json", "").replace("```", "").strip()
    
    try:
        data = json.loads(raw)
        data["source"] = "gemini"
        data["tracker_count"] = len(data.get("trackers", []))
        data["permission_count"] = len(data.get("permissions", []))
        data["cached"] = False
        data["error"] = None
        print(f"[Gemini] Generated data for '{app_name}'")
        return data
    except json.JSONDecodeError:
        print(f"[Gemini] Failed to parse response for '{app_name}': {raw}")
        return None