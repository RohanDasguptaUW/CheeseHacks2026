def get_app_data(app_name: str) -> dict:
    key = app_name.lower().strip()
    
    if key in APP_DATABASE:
        print(f"[Database] Found '{app_name}' in local database")
        return APP_DATABASE[key]
    
    # Try Gemini to generate data dynamically
    print(f"[Database] '{app_name}' not in database")
    try:
        from gemini_helper import generate_app_data
        data = generate_app_data(app_name)
        if data:
            # Cache it so we don't call Gemini again for same app
            APP_DATABASE[key] = data
            return data
    except Exception as e:
        print(f"[Database] generation failed: {e}")

    # Final fallback
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