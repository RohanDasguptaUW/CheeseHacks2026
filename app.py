# CheeseHacks2026/app.py
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
from data_fetcher import get_app_data, get_batch_data, PERMISSION_META
from demo_data import get_demo_data
from gemini_helper import scan_apps_from_image, generate_guilt_trip
from datetime import datetime, timezone

app = Flask(__name__)
CORS(app)

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/api/scan/<app_name>")
def scan_app(app_name):
    demo = get_demo_data(app_name.lower().strip())
    if demo:
        return jsonify({**demo, "fetched_at": datetime.now(timezone.utc).isoformat()})
    data = get_app_data(app_name)
    return jsonify(data)

@app.route("/api/batch", methods=["POST"])
def batch_scan():
    body = request.get_json()
    apps = body.get("apps", [])
    data = get_batch_data(apps)
    return jsonify(data)

@app.route("/api/scan-screenshot", methods=["POST"])
def scan_screenshot():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    filename = secure_filename(file.filename)
    filepath = os.path.join("/tmp", filename)
    file.save(filepath)

    # Step 1 — get app names from screenshot
    apps_from_image = scan_apps_from_image(filepath)
    os.remove(filepath)

    if not apps_from_image:
        return jsonify({"error": "No apps detected in screenshot"}), 400

    # Step 2 — handle both string list and dict list
    results = []
    app_names = []
    for item in apps_from_image:
        # Handle both {"name": "TikTok"} and "TikTok"
        if isinstance(item, dict):
            name = item.get("name", "")
            package = item.get("package", "")
        else:
            name = item
            package = ""

        if not name:
            continue

        app_names.append(name)
        data = get_demo_data(name.lower()) or get_app_data(package or name)
        if data and data.get("source") != "not_found":
            if not data.get("package_name") and package:
                data["package_name"] = package
            results.append(data)
        else:
            results.append({
                "app_name": name,
                "package_name": package,
                "source": "unknown",
                "permissions": [],
                "trackers": [],
                "tracker_count": 0,
                "permission_count": 0,
                "error": None
            })

    return jsonify({
        "apps_detected": app_names,
        "results": results
    })

@app.route("/api/guilt-trip/<app_name>")
def guilt_trip(app_name):
    data = get_demo_data(app_name.lower()) or get_app_data(app_name)
    if not data:
        return jsonify({"error": "App not found"}), 404

    permissions = [p["label"] for p in data.get("permissions", [])]
    trackers = data.get("trackers", [])

    score = 100
    for p in data.get("permissions", []):
        meta = PERMISSION_META.get(p["name"])
        score += meta["weight"] if meta else -1
    score = max(0, min(100, score))

    text = generate_guilt_trip(app_name, permissions, trackers, score)
    return jsonify({"guilt_trip": text})

@app.route("/api/icon/<app_name>")
def get_icon(app_name):
    import requests
    try:
        res = requests.get(
            f"https://itunes.apple.com/search",
            params={"term": app_name, "entity": "software", "limit": 1},
            timeout=5
        )
        data = res.json()
        if data["results"]:
            return jsonify({"icon": data["results"][0]["artworkUrl100"]})
    except:
        pass
    return jsonify({"icon": None})

if __name__ == "__main__":
    app.run(debug=True, port=8000)