// src/mockData.js
export const mockAppResult = {
  app_name: "TikTok",
  package_name: "com.zhiliaoapp.musically",
  source: "exodus",
  privacyScore: 23,
  riskLevel: "high",
  permissions: [
    { name: "android.permission.RECORD_AUDIO", label: "Microphone", risk: "high", reason: "Can record audio at any time" },
    { name: "android.permission.ACCESS_FINE_LOCATION", label: "Precise Location", risk: "high", reason: "Tracks exactly where you are" },
    { name: "android.permission.CAMERA", label: "Camera", risk: "high", reason: "Can access camera in background" },
    { name: "android.permission.READ_CONTACTS", label: "Contacts", risk: "high", reason: "Can read your contact list" },
    { name: "android.permission.READ_EXTERNAL_STORAGE", label: "Read Files", risk: "medium", reason: "Can read files on your device" },
    { name: "android.permission.WRITE_EXTERNAL_STORAGE", label: "Write Files", risk: "medium", reason: "Can write files on your device" },
  ],
  trackers: [
    { name: "Facebook Ads", website: "https://facebook.com", categories: ["Advertising"] },
    { name: "Google Analytics", website: "https://analytics.google.com", categories: ["Analytics"] },
    { name: "AppsFlyer", website: "https://appsflyer.com", categories: ["Attribution"] },
  ],
  tracker_count: 3,
  permission_count: 6,
  cached: false,
  fetched_at: "2026-02-28T10:00:00Z",
  error: null,
  fixInstructions: "Go to Settings > Apps > TikTok > Permissions and revoke Microphone and Location access"
}

export const mockDashboard = [
  { app_name: "TikTok", privacyScore: 23, riskLevel: "high" },
  { app_name: "Instagram", privacyScore: 31, riskLevel: "high" },
  { app_name: "Spotify", privacyScore: 67, riskLevel: "medium" },
  { app_name: "Calculator", privacyScore: 95, riskLevel: "low" },
]