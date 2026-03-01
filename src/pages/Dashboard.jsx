// src/pages/Dashboard.jsx
import { mockDashboard } from "../mockData"
import { useNavigate } from "react-router-dom"

const riskColor = {
  high: "var(--red)",
  medium: "var(--yellow)",
  low: "var(--green)"
}

export default function Dashboard() {
  const navigate = useNavigate()
  const overallScore = Math.round(mockDashboard.reduce((sum, a) => sum + a.privacyScore, 0) / mockDashboard.length)

  const overallRisk = overallScore < 40 ? "high" : overallScore < 70 ? "medium" : "low"
  const overallColor = riskColor[overallRisk]

  return (
    <div style={{ minHeight: "100vh", background: "var(--bg)", padding: "2rem", maxWidth: "700px", margin: "0 auto" }}>

      <a href="/" style={{
        display: "inline-flex", alignItems: "center", gap: "6px",
        color: "var(--muted)", textDecoration: "none",
        fontFamily: "'Space Mono', monospace", fontSize: "0.8rem",
        marginBottom: "2rem"
      }}>← Back</a>

      {/* Overall Score Card */}
      <div className="fade-up" style={{
        background: "var(--surface)", border: "1px solid var(--border)",
        borderRadius: "16px", padding: "2rem", marginBottom: "1.5rem",
        textAlign: "center"
      }}>
        <p style={{ fontFamily: "'Space Mono', monospace", fontSize: "0.75rem", color: "var(--muted)", letterSpacing: "0.1em", marginBottom: "1rem" }}>
          OVERALL PRIVACY HEALTH
        </p>
        <div style={{
          fontSize: "6rem", fontWeight: 800, color: overallColor,
          fontFamily: "'Space Mono', monospace", lineHeight: 1,
          textShadow: `0 0 40px ${overallColor}60`
        }}>
          {overallScore}
        </div>
        <p style={{ color: "var(--muted)", fontSize: "0.85rem", marginTop: "0.5rem" }}>
          Based on {mockDashboard.length} apps scanned
        </p>
      </div>

      {/* App List */}
      <div className="fade-up-delay-1" style={{
        background: "var(--surface)", border: "1px solid var(--border)",
        borderRadius: "16px", padding: "1.5rem"
      }}>
        <h3 style={{ fontFamily: "'Space Mono', monospace", fontSize: "0.75rem", letterSpacing: "0.1em", color: "var(--muted)", marginBottom: "1rem" }}>
          APPS RANKED BY RISK
        </h3>
        {mockDashboard
          .sort((a, b) => a.privacyScore - b.privacyScore)
          .map((app, i) => (
          <div key={i}
            onClick={() => navigate(`/app/${app.app_name}`)}
            style={{
              display: "flex", alignItems: "center", justifyContent: "space-between",
              padding: "14px 16px", borderRadius: "10px",
              background: "var(--surface2)", border: "1px solid var(--border)",
              marginBottom: "8px", cursor: "pointer", transition: "all 0.2s"
            }}
            onMouseOver={e => e.currentTarget.style.borderColor = riskColor[app.riskLevel]}
            onMouseOut={e => e.currentTarget.style.borderColor = "var(--border)"}
          >
            <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
              <span style={{ color: "var(--muted)", fontFamily: "'Space Mono', monospace", fontSize: "0.8rem", width: "20px" }}>
                {String(i + 1).padStart(2, "0")}
              </span>
              <span style={{ fontWeight: 700 }}>{app.app_name}</span>
            </div>
            <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
              <span style={{
                padding: "3px 10px", borderRadius: "100px", fontSize: "0.7rem",
                fontFamily: "'Space Mono', monospace",
                color: riskColor[app.riskLevel],
                background: `${riskColor[app.riskLevel]}15`,
                border: `1px solid ${riskColor[app.riskLevel]}40`
              }}>
                {app.riskLevel.toUpperCase()}
              </span>
              <span style={{
                fontSize: "1.5rem", fontWeight: 800,
                color: riskColor[app.riskLevel],
                fontFamily: "'Space Mono', monospace"
              }}>
                {app.privacyScore}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}