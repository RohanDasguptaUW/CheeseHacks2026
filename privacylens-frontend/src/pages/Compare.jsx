import { useState } from "react"
import { mockDashboard } from "../mockData"

const riskColor = {
  high: "var(--red)",
  medium: "var(--yellow)",
  low: "var(--green)"
}

export default function Compare() {
  const [appA, setAppA] = useState(mockDashboard[0])
  const [appB, setAppB] = useState(mockDashboard[1])

  const winner = appA.privacyScore > appB.privacyScore ? appA : appB

  return (
    <div style={{ minHeight: "100vh", background: "var(--bg)", padding: "2rem", maxWidth: "700px", margin: "0 auto" }}>
      <a href="/" style={{
        display: "inline-flex", alignItems: "center", gap: "6px",
        color: "var(--muted)", textDecoration: "none",
        fontFamily: "'Space Mono', monospace", fontSize: "0.8rem",
        marginBottom: "2rem"
      }}>← Back</a>

      <h2 style={{ fontSize: "2rem", fontWeight: 800, marginBottom: "0.5rem" }}>Compare Apps</h2>
      <p style={{ color: "var(--muted)", fontSize: "0.9rem", marginBottom: "2rem" }}>
        See how two apps stack up against each other
      </p>

      {/* Selectors */}
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "1rem", marginBottom: "1.5rem" }}>
        {[{ val: appA, set: setAppA }, { val: appB, set: setAppB }].map(({ val, set }, idx) => (
          <div key={idx}>
            <p style={{ fontFamily: "'Space Mono', monospace", fontSize: "0.7rem", color: "var(--muted)", marginBottom: "8px" }}>
              APP {idx + 1}
            </p>
            <select
              value={val.app_name}
              onChange={e => set(mockDashboard.find(a => a.app_name === e.target.value))}
              style={{
                width: "100%", padding: "10px 14px",
                background: "var(--surface)", border: "1px solid var(--border)",
                borderRadius: "10px", color: "var(--text)",
                fontFamily: "'Syne', sans-serif", fontSize: "1rem",
                outline: "none", cursor: "pointer"
              }}
            >
              {mockDashboard.map(a => (
                <option key={a.app_name} value={a.app_name}>{a.app_name}</option>
              ))}
            </select>
          </div>
        ))}
      </div>

      {/* Score Cards */}
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "1rem", marginBottom: "1.5rem" }}>
        {[appA, appB].map((app, i) => (
          <div key={i} style={{
            background: "var(--surface)", border: `2px solid ${app.app_name === winner.app_name ? "var(--green)" : "var(--border)"}`,
            borderRadius: "16px", padding: "1.5rem", textAlign: "center",
            position: "relative"
          }}>
            {app.app_name === winner.app_name && (
              <div style={{
                position: "absolute", top: "-12px", left: "50%", transform: "translateX(-50%)",
                background: "var(--green)", color: "white",
                padding: "2px 12px", borderRadius: "100px",
                fontSize: "0.7rem", fontFamily: "'Space Mono', monospace", fontWeight: 700
              }}>
                SAFER
              </div>
            )}
            <p style={{ fontWeight: 800, fontSize: "1.1rem", marginBottom: "0.75rem" }}>{app.app_name}</p>
            <p style={{
              fontSize: "3.5rem", fontWeight: 800,
              color: riskColor[app.riskLevel],
              fontFamily: "'Space Mono', monospace", lineHeight: 1
            }}>
              {app.privacyScore}
            </p>
            <p style={{ color: "var(--muted)", fontSize: "0.75rem", marginTop: "4px" }}>/100</p>
            <span style={{
              display: "inline-block", marginTop: "12px",
              padding: "3px 12px", borderRadius: "100px",
              fontSize: "0.7rem", fontFamily: "'Space Mono', monospace",
              color: riskColor[app.riskLevel],
              background: `${riskColor[app.riskLevel]}15`,
              border: `1px solid ${riskColor[app.riskLevel]}40`
            }}>
              {app.riskLevel.toUpperCase()}
            </span>
          </div>
        ))}
      </div>

      {/* Verdict */}
      <div style={{
        background: "var(--surface)", border: "1px solid var(--border)",
        borderRadius: "16px", padding: "1.5rem", textAlign: "center"
      }}>
        <p style={{ color: "var(--muted)", fontSize: "0.85rem", marginBottom: "0.5rem" }}>VERDICT</p>
        <p style={{ fontSize: "1.1rem", fontWeight: 700 }}>
          <span style={{ color: "var(--green)" }}>{winner.app_name}</span> is {Math.abs(appA.privacyScore - appB.privacyScore)} points safer than{" "}
          <span style={{ color: "var(--red)" }}>{winner.app_name === appA.app_name ? appB.app_name : appA.app_name}</span>
        </p>
      </div>
    </div>
  )
}