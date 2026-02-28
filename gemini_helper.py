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