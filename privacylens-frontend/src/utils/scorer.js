// src/utils/scorer.js

const PERMISSION_WEIGHTS = {
  "android.permission.RECORD_AUDIO":           -12,
  "android.permission.ACCESS_FINE_LOCATION":   -10,
  "android.permission.CAMERA":                 -10,
  "android.permission.READ_CONTACTS":          -8,
  "android.permission.READ_CALL_LOG":          -8,
  "android.permission.READ_SMS":               -8,
  "android.permission.SEND_SMS":               -8,
  "android.permission.GET_ACCOUNTS":           -6,
  "android.permission.ACCESS_COARSE_LOCATION": -5,
  "android.permission.READ_PHONE_STATE":       -4,
  "android.permission.USE_BIOMETRIC":          -4,
  "android.permission.BODY_SENSORS":           -4,
  "android.permission.READ_EXTERNAL_STORAGE":  -3,
  "android.permission.WRITE_EXTERNAL_STORAGE": -3,
  "android.permission.BLUETOOTH_SCAN":         -2,
  "android.permission.RECEIVE_BOOT_COMPLETED": -2,
  "android.permission.INTERNET":               -1,
  "android.permission.FOREGROUND_SERVICE":     -1,
}

const TRACKER_PENALTY = -5

export function calculateScore(permissions, trackers) {
  let score = 100

  for (const perm of permissions) {
    const weight = PERMISSION_WEIGHTS[perm.name] ?? -1
    score += weight
  }

  const trackerPenalty = Math.min(trackers.length, 5) * TRACKER_PENALTY
  score += trackerPenalty

  return Math.max(0, Math.min(100, score))
}

export function getRiskLevel(score) {
  if (score < 40) return "high"
  if (score < 70) return "medium"
  return "low"
}

export function getRiskLevelFromTier(tier) {
  if (!tier) return "low"
  const t = tier.toLowerCase()
  if (t === "critical" || t === "high") return "high"
  if (t === "medium" || t === "moderate") return "medium"
  return "low"
}