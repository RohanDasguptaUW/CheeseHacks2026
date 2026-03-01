// src/components/TrackerBadge.jsx
import { useState } from "react"

const trackerInfo = {
  "Facebook Ads": "Collects behavioral data to serve targeted ads across Facebook's network. Shares data with Meta.",
  "Google Analytics": "Tracks user behavior, session data, and device info. Sends data to Google servers.",
  "AppsFlyer": "Mobile attribution tracker. Logs installs, clicks, and in-app events for ad campaign measurement.",
  "Amplitude": "Product analytics platform. Tracks every tap and screen view to build user behavior profiles.",
  "Crashlytics": "Crash reporting tool by Google. Generally low risk — only collects crash logs.",
  "Branch": "Deep linking and attribution SDK. Tracks where users come from across apps and web.",
}

export default function TrackerBadge({ name }) {
  const [open, setOpen] = useState(false)
  const info = trackerInfo[name] || "This tracker collects data about your app usage and behavior."

  return (
    <div style={{ position: "relative", display: "inline-block" }}>
      <span
        onClick={() => setOpen(!open)}
        style={{
          padding: "6px 14px", borderRadius: "100px",
          background: "rgba(229,57,53,0.08)",
          border: "1px solid rgba(229,57,53,0.25)",
          color: "var(--red)", fontSize: "0.8rem",
          fontFamily: "'Space Mono', monospace",
          cursor: "pointer", display: "inline-block",
          transition: "all 0.2s"
        }}
      >
        {name} {open ? "▲" : "▼"}
      </span>

      {open && (
        <div style={{
          position: "absolute", bottom: "110%", left: 0,
          background: "var(--text)", color: "var(--bg)",
          padding: "10px 14px", borderRadius: "10px",
          fontSize: "0.78rem", lineHeight: 1.5,
          width: "220px", zIndex: 10,
          boxShadow: "0 8px 24px rgba(0,0,0,0.15)"
        }}>
          {info}
          <div style={{
            position: "absolute", top: "100%", left: "16px",
            width: 0, height: 0,
            borderLeft: "6px solid transparent",
            borderRight: "6px solid transparent",
            borderTop: `6px solid var(--text)`
          }} />
        </div>
      )}
    </div>
  )
}