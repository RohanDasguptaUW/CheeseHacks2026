# scorer.py
# Person 2's main file - Privacy Score Engine

# ============================================
# SECTION 1: PRIVACY SCORE CALCULATOR
# ============================================

def calculate_privacy_score(permissions, trackers):
    """
    Takes a list of permissions and trackers
    Returns a privacy score from 0-100
    Higher = more private (better)
    """
    score = 100

    # High risk permissions and their penalties
    high_risk = {
        "microphone": 20,
        "precise_location": 15,
        "camera": 15,
        "contacts": 12,
        "call_logs": 12,
        "background_location": 15,
        "read_sms": 12,
        "record_audio": 18,
        "access_fine_location": 15,
        "read_contacts": 12,
        "process_outgoing_calls": 10
    }

    # Medium risk permissions and their penalties
    medium_risk = {
        "approximate_location": 8,
        "storage": 6,
        "calendar": 7,
        "sms": 10,
        "read_external_storage": 5,
        "write_external_storage": 5,
        "access_coarse_location": 6,
        "get_accounts": 7,
        "use_biometric": 5
    }

    # Deduct for each permission
    for permission in permissions:
        perm_lower = permission.lower()
        if perm_lower in high_risk:
            score -= high_risk[perm_lower]
        elif perm_lower in medium_risk:
            score -= medium_risk[perm_lower]
        else:
            score -= 2  # unknown permission = small penalty

    # Deduct for trackers (max penalty = 30)
    tracker_penalty = min(len(trackers) * 10, 30)
    score -= tracker_penalty

    # Extra penalty for suspicious combos
    score -= calculate_unnecessary_penalty(permissions)

    # Never go below 0
    return max(0, score)


# ============================================
# SECTION 2: UNNECESSARY PERMISSION PENALTY
# ============================================

def calculate_unnecessary_penalty(permissions):
    """
    Penalizes apps that have suspicious
    combinations of permissions they
    shouldn't need
    """
    penalty = 0
    perms_lower = [p.lower() for p in permissions]

    suspicious_combos = [
        {
            "combo": ["microphone", "precise_location"],
            "penalty": 10,
            "reason": "Microphone + precise location is unusual"
        },
        {
            "combo": ["contacts", "precise_location"],
            "penalty": 8,
            "reason": "Contacts + location suggests surveillance"
        },
        {
            "combo": ["background_location", "microphone"],
            "penalty": 15,
            "reason": "Can track and listen in background"
        },
        {
            "combo": ["camera", "microphone", "precise_location"],
            "penalty": 20,
            "reason": "Full surveillance combo"
        },
        {
            "combo": ["read_sms", "contacts"],
            "penalty": 12,
            "reason": "Can read your messages and contacts"
        }
    ]

    for item in suspicious_combos:
        if all(p in perms_lower for p in item["combo"]):
            penalty += item["penalty"]

    return penalty


# ============================================
# SECTION 3: RISK TIER CLASSIFIER
# ============================================

def classify_permissions(permissions):
    """
    Takes permissions list
    Returns detailed classification of each one
    """
    permission_details = {
        "microphone": {
            "tier": "HIGH",
            "color": "red",
            "plain_english": "This app can listen through your microphone",
            "why_scary": "Can record conversations and background audio even when minimized"
        },
        "precise_location": {
            "tier": "HIGH",
            "color": "red",
            "plain_english": "This app knows exactly where you are at all times",
            "why_scary": "Can map your daily routine, home, workplace, and everywhere you go"
        },
        "camera": {
            "tier": "HIGH",
            "color": "red",
            "plain_english": "This app can access your camera",
            "why_scary": "Can potentially take photos or video without your knowledge"
        },
        "contacts": {
            "tier": "HIGH",
            "color": "red",
            "plain_english": "This app can see everyone in your phone",
            "why_scary": "Your contacts' data is shared without their knowledge or consent"
        },
        "call_logs": {
            "tier": "HIGH",
            "color": "red",
            "plain_english": "This app can see your entire call history",
            "why_scary": "Knows who you call, when, and for how long"
        },
        "background_location": {
            "tier": "HIGH",
            "color": "red",
            "plain_english": "This app tracks your location even when closed",
            "why_scary": "Builds a complete map of everywhere you go 24/7"
        },
        "approximate_location": {
            "tier": "MEDIUM",
            "color": "orange",
            "plain_english": "This app knows roughly where you are",
            "why_scary": "Can determine your neighborhood and general area"
        },
        "storage": {
            "tier": "MEDIUM",
            "color": "orange",
            "plain_english": "This app can read files on your phone",
            "why_scary": "Can access photos, documents, and downloads"
        },
        "calendar": {
            "tier": "MEDIUM",
            "color": "orange",
            "plain_english": "This app can see your calendar",
            "why_scary": "Knows your schedule, appointments, and plans"
        },
        "sms": {
            "tier": "MEDIUM",
            "color": "orange",
            "plain_english": "This app can read your text messages",
            "why_scary": "Can see personal conversations and 2FA codes"
        }
    }

    results = []
    for p in permissions:
        p_lower = p.lower()
        if p_lower in permission_details:
            results.append({
                "permission": p,
                **permission_details[p_lower]
            })
        else:
            results.append({
                "permission": p,
                "tier": "LOW",
                "color": "green",
                "plain_english": f"This app uses {p}",
                "why_scary": "Low risk permission"
            })

    # Sort by risk tier
    tier_order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    results.sort(key=lambda x: tier_order[x["tier"]])

    return results


# ============================================
# SECTION 4: SCORE LABEL
# ============================================

def get_score_label(score):
    if score >= 80:
        return {"label": "Safe", "color": "green",
                "emoji": "✅"}
    elif score >= 60:
        return {"label": "Moderate Risk",
                "color": "yellow", "emoji": "⚠️"}
    elif score >= 40:
        return {"label": "High Risk",
                "color": "orange", "emoji": "🔶"}
    else:
        return {"label": "Dangerous",
                "color": "red", "emoji": "🚨"}


# ============================================
# SECTION 5: CATEGORY BENCHMARKING
# ============================================

category_benchmarks = {
    "social_media": 35,
    "navigation": 45,
    "messaging": 50,
    "productivity": 70,
    "games": 55,
    "shopping": 48,
    "health_fitness": 52,
    "finance": 65,
    "entertainment": 45,
    "utilities": 72
}

def get_benchmarking(app_score, category):
    avg = category_benchmarks.get(
        category.lower(), 55
    )

    if app_score > avg:
        diff = round(((app_score - avg) / avg) * 100)
        return f"Better than {diff}% of {category} apps"
    else:
        diff = round(((avg - app_score) / avg) * 100)
        return f"Worse than {diff}% of {category} apps"


# ============================================
# SECTION 6: APP COMPARISON ENGINE
# ============================================

def compare_apps(app1_data, app2_data):
    score1 = calculate_privacy_score(
        app1_data["permissions"],
        app1_data["trackers"]
    )
    score2 = calculate_privacy_score(
        app2_data["permissions"],
        app2_data["trackers"]
    )

    unique_to_app1 = list(
        set(app1_data["permissions"]) -
        set(app2_data["permissions"])
    )
    unique_to_app2 = list(
        set(app2_data["permissions"]) -
        set(app1_data["permissions"])
    )

    winner = app1_data["name"] \
        if score1 > score2 else app2_data["name"]

    return {
        "app1": {
            "name": app1_data["name"],
            "score": score1,
            "label": get_score_label(score1)
        },
        "app2": {
            "name": app2_data["name"],
            "score": score2,
            "label": get_score_label(score2)
        },
        "winner": winner,
        "score_difference": abs(score1 - score2),
        "winner_reason": f"{winner} has {abs(score1-score2)} fewer risk points",
        "app1_unique_risks": unique_to_app1,
        "app2_unique_risks": unique_to_app2
    }


# ============================================
# SECTION 7: PRIVACY TIME MACHINE
# ============================================

def calculate_growth_score(version_history):
    """
    version_history = [
      {"version": "1.0", "permissions": [...]},
      {"version": "2.0", "permissions": [...]},
    ]
    """
    if not version_history or len(version_history) < 2:
        return None

    first = version_history[0]
    latest = version_history[-1]

    first_count = len(first["permissions"])
    latest_count = len(latest["permissions"])

    new_permissions = list(
        set(latest["permissions"]) -
        set(first["permissions"])
    )

    removed_permissions = list(
        set(first["permissions"]) -
        set(latest["permissions"])
    )

    growth_rate = round(
        (latest_count - first_count) /
        max(first_count, 1) * 100
    )

    return {
        "original_count": first_count,
        "current_count": latest_count,
        "growth_rate_percent": growth_rate,
        "new_permissions": new_permissions,
        "removed_permissions": removed_permissions,
        "summary": f"This app expanded data collection by {growth_rate}% since launch",
        "concerning": growth_rate > 20
    }


# ============================================
# SECTION 8: ALTERNATIVE APP SUGGESTIONS
# ============================================

alternatives = {
    "tiktok": {
        "alternative": "YouTube (with restrictions)",
        "reason": "0 background location, fewer trackers",
        "score_improvement": "+45 points"
    },
    "instagram": {
        "alternative": "Pixelfed",
        "reason": "Open source, no ad tracking",
        "score_improvement": "+41 points"
    },
    "facebook": {
        "alternative": "No direct alternative",
        "reason": "Consider using browser version instead",
        "score_improvement": "+38 points"
    },
    "google maps": {
        "alternative": "OsmAnd",
        "reason": "0 trackers vs Google Maps 7",
        "score_improvement": "+34 points"
    },
    "whatsapp": {
        "alternative": "Signal",
        "reason": "End-to-end encrypted, 0 ad trackers",
        "score_improvement": "+28 points"
    },
    "snapchat": {
        "alternative": "Signal for messaging",
        "reason": "No location tracking or ad profiling",
        "score_improvement": "+30 points"
    },
    "chrome": {
        "alternative": "Firefox Focus",
        "reason": "Built-in tracking protection",
        "score_improvement": "+22 points"
    },
    "uber": {
        "alternative": "Lyft (slightly better)",
        "reason": "Less background location usage",
        "score_improvement": "+10 points"
    },
    "spotify": {
        "alternative": "Apple Music or local files",
        "reason": "Fewer ad trackers",
        "score_improvement": "+15 points"
    }
}

def get_alternative(app_name):
    key = app_name.lower().strip()
    return alternatives.get(key, None)


# ============================================
# SECTION 9: FULL ANALYSIS (main function)
# This is what Person 4's backend will call
# ============================================

def full_app_analysis(app_data):
    """
    app_data = {
        "name": "TikTok",
        "permissions": ["microphone", ...],
        "trackers": ["tracker1", ...],
        "category": "social_media",
        "version_history": [...] (optional)
    }
    """
    score = calculate_privacy_score(
        app_data["permissions"],
        app_data["trackers"]
    )

    result = {
        "app_name": app_data["name"],
        "privacy_score": score,
        "score_label": get_score_label(score),
        "permissions": classify_permissions(
            app_data["permissions"]
        ),
        "benchmarking": get_benchmarking(
            score,
            app_data.get("category", "general")
        ),
        "alternative": get_alternative(
            app_data["name"]
        ),
        "time_machine": calculate_growth_score(
            app_data.get("version_history", [])
        )
    }

    return result