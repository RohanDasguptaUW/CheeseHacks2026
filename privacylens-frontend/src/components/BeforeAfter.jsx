// src/components/BeforeAfter.jsx
import { useState } from "react"
import { calculateScore } from "../utils/scorer"

const pointsMap = { high: 12, medium: 5, low: 2 }

export default function BeforeAfter({ permissions, baseScore }) {
  const [revoked, setRevoked] = useState([])

  const improvedScore = Math.min(
    100,
    baseScore + revoked.reduce((sum, name) => {
      const p = permissions.find(p => p.name === name)
      return sum + (p ? pointsMap[p.risk] : 0)
    }, 0)
  )

  const toggle = (name) => {
    setRevoked(prev =>
      prev.includes(name) ? prev.filter(n => n !== name) : [...prev, name]
    )
  }

  const improvement = improvedScore - baseScore

  return (
    <div style={{
      background: "var(--surface)", border: "1px solid var(--border)",
      borderRadius: "16px", padding: "1.5rem", marginBottom: "1.5rem"
    }}>
      <h3 style={{ fontSize: "1rem", fontWeight: 700, marginBottom: "4px" }}>
        What if you revoked some permissions?
      </h3>
      <p style={{ fontSize: "0.85rem", color: "var(--muted)", marginBottom: "1.25rem" }}>
        Toggle permissions off to see how your privacy score improves
      </p>

      {permissions.map((p, i) => (
        <div key={i} onClick={() => toggle(p.name)} style={{
          display: "flex", alignItems: "center", justifyContent: "space-between",
          padding: "10px 14px", borderRadius: "8px", marginBottom: "8px",
          background: revoked.includes(p.name) ? "rgba(16,185,129,0.05)" : "var(--surface2)",
          border: `1px solid ${revoked.includes(p.name) ? "rgba(16,185,129,0.3)" : "var(--border)"}`,
          cursor: "pointer", transition: "all 0.2s"
        }}>
          <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
            <span style={{
              width: 8, height: 8, borderRadius: "50%", flexShrink: 0,
              background: p.risk === "high" ? "var(--red)" : p.risk === "medium" ? "var(--yellow)" : "var(--green)"
            }} />
            <span style={{
              fontSize: "0.9rem", fontWeight: 600,
              textDecoration: revoked.includes(p.name) ? "line-through" : "none",
              color: revoked.includes(p.name) ? "var(--muted)" : "var(--text)"
            }}>
              {p.label}
            </span>
          </div>
          <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
            {revoked.includes(p.name) && (
              <span style={{ fontSize: "0.75rem", color: "var(--green)", fontWeight: 600 }}>
                +{pointsMap[p.risk]} pts
              </span>
            )}
            <div style={{
              width: "36px", height: "20px", borderRadius: "100px",
              background: revoked.includes(p.name) ? "var(--green)" : "var(--border)",
              position: "relative", transition: "all 0.2s", flexShrink: 0
            }}>
              <div style={{
                width: "14px", height: "14px", borderRadius: "50%",
                background: "white", position: "absolute", top: "3px",
                transition: "all 0.2s",
                left: revoked.includes(p.name) ? "19px" : "3px"
              }} />
            </div>
          </div>
        </div>
      ))}

      <div style={{
        marginTop: "1.25rem", padding: "1rem",
        background: "var(--surface2)", borderRadius: "12px",
        border: "1px solid var(--border)",
        display: "flex", justifyContent: "space-around", alignItems: "center"
      }}>
        <div style={{ textAlign: "center" }}>
          <p style={{ fontSize: "0.75rem", color: "var(--muted)", marginBottom: "4px" }}>Current score</p>
          <p style={{ fontSize: "2.5rem", fontWeight: 800, color: "var(--red)", lineHeight: 1 }}>{baseScore}</p>
        </div>
        <div style={{ textAlign: "center" }}>
          <p style={{ fontSize: "1.5rem" }}>→</p>
        </div>
        <div style={{ textAlign: "center" }}>
          <p style={{ fontSize: "0.75rem", color: "var(--muted)", marginBottom: "4px" }}>After changes</p>
          <p style={{ fontSize: "2.5rem", fontWeight: 800, color: "var(--green)", lineHeight: 1 }}>{improvedScore}</p>
        </div>
        {improvement > 0 && (
          <div style={{ textAlign: "center" }}>
            <p style={{ fontSize: "0.75rem", color: "var(--muted)", marginBottom: "4px" }}>Improvement</p>
            <p style={{ fontSize: "2.5rem", fontWeight: 800, color: "var(--green)", lineHeight: 1 }}>+{improvement}</p>
          </div>
        )}
      </div>
    </div>
  )
}