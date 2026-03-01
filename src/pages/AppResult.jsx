// src/pages/AppResult.jsx
import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"
import AnimatedScore from "../components/AnimatedScore"
import TrackerBadge from "../components/TrackerBadge"

const tierConfig = {
  HIGH: { color: "var(--red)", bg: "rgba(229,57,53,0.08)", border: "rgba(229,57,53,0.2)", label: "High risk" },
  MEDIUM: { color: "var(--yellow)", bg: "rgba(245,158,11,0.08)", border: "rgba(245,158,11,0.2)", label: "Medium risk" },
  LOW: { color: "var(--green)", bg: "rgba(5,150,105,0.08)", border: "rgba(5,150,105,0.2)", label: "Low risk" }
}

const scoreConfig = (score) => {
  if (score >= 70) return { color: "var(--green)", label: "Low Risk" }
  if (score >= 40) return { color: "var(--yellow)", label: "Medium Risk" }
  return { color: "var(--red)", label: "High Risk" }
}

export default function AppResult() {
  const { appName } = useParams()
  const [app, setApp] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [appIcon, setAppIcon] = useState(null)

  useEffect(() => {
    fetch(`http://localhost:8001/app/${appName}`)
      .then(res => {
        if (!res.ok) throw new Error("Not found")
        return res.json()
      })
      .then(data => {
        setApp(data)
        setLoading(false)
      })
      .catch(() => {
        setError(true)
        setLoading(false)
      })
  }, [appName])

  useEffect(() => {
    if (!app) return
    fetch(`http://localhost:8001/api/icon/${encodeURIComponent(app.app_name)}`)
      .then(res => res.json())
      .then(data => { if (data.icon) setAppIcon(data.icon) })
      .catch(() => {})
  }, [app])

  if (loading) return (
    <div style={{
      minHeight: "100vh", background: "var(--bg)",
      display: "flex", flexDirection: "column",
      alignItems: "center", justifyContent: "center", gap: "1rem"
    }}>
      <div style={{
        width: "36px", height: "36px",
        border: "3px solid var(--border)",
        borderTop: "3px solid var(--red)",
        borderRadius: "50%", animation: "spin 0.8s linear infinite"
      }} />
      <p style={{ color: "var(--muted)", fontSize: "0.9rem" }}>Scanning {appName}...</p>
    </div>
  )

  if (error || !app) return (
    <div style={{
      minHeight: "100vh", background: "var(--bg)",
      display: "flex", flexDirection: "column",
      alignItems: "center", justifyContent: "center", gap: "1rem"
    }}>
      <p style={{ fontSize: "1.5rem" }}>😕</p>
      <p style={{ fontWeight: 600, fontSize: "1.1rem" }}>We couldn't find that app</p>
      <p style={{ color: "var(--muted)", fontSize: "0.9rem" }}>Try searching for a different app name</p>
      <a href="/" style={{ marginTop: "0.5rem", color: "var(--red)", textDecoration: "none", fontWeight: 600 }}>← Go back</a>
    </div>
  )

  const score = scoreConfig(app.privacy_score)
  const highRiskPerms = app.permissions?.filter(p => p.tier === "HIGH") || []
  const mediumRiskPerms = app.permissions?.filter(p => p.tier === "MEDIUM") || []
  const lowRiskPerms = app.permissions?.filter(p => p.tier === "LOW") || []

  return (
    <div style={{
      minHeight: "100vh", background: "var(--bg)",
      padding: "2rem", maxWidth: "680px", margin: "0 auto"
    }}>

      {/* Back */}
      <a href="/" style={{
        display: "inline-flex", alignItems: "center", gap: "6px",
        color: "var(--muted)", textDecoration: "none",
        fontSize: "0.9rem", marginBottom: "1.5rem"
      }}>← Back</a>

      {/* Header Card */}
      <div className="fade-up" style={{
        background: "var(--surface)", border: "1px solid var(--border)",
        borderRadius: "16px", padding: "1.75rem", marginBottom: "1rem"
      }}>
        <div style={{
          display: "flex", justifyContent: "space-between",
          alignItems: "flex-start", flexWrap: "wrap", gap: "1rem"
        }}>
          {/* Left — icon + name */}
          <div style={{ display: "flex", alignItems: "center", gap: "1rem" }}>
            {appIcon && (
              <img src={appIcon} alt={app.app_name} style={{
                width: "64px", height: "64px", borderRadius: "16px",
                flexShrink: 0, boxShadow: "0 2px 12px rgba(0,0,0,0.1)"
              }} />
            )}
            <div>
              <h1 style={{
                fontSize: "2.2rem", fontWeight: 700,
                letterSpacing: "-0.02em", marginBottom: "6px"
              }}>
                {app.app_name}
              </h1>
              <p style={{ color: "var(--muted)", fontSize: "0.9rem" }}>
                {app.permissions?.length || 0} permissions · {app.raw_trackers?.length || 0} trackers found
              </p>
            </div>
          </div>

          {/* Score Circle */}
          <div style={{
            width: "90px", height: "90px", borderRadius: "50%",
            border: `3px solid ${score.color}`,
            display: "flex", flexDirection: "column",
            alignItems: "center", justifyContent: "center", flexShrink: 0
          }}>
            <span style={{ fontSize: "1.8rem", fontWeight: 700, color: score.color, lineHeight: 1 }}>
              <AnimatedScore target={app.privacy_score} />
            </span>
            <span style={{ fontSize: "0.65rem", color: "var(--muted)" }}>/100</span>
          </div>
        </div>

        {/* Risk Banner */}
        <div style={{
          marginTop: "1.25rem", padding: "12px 16px",
          background: `${score.color}10`,
          border: `1px solid ${score.color}30`,
          borderRadius: "10px", display: "flex", alignItems: "center", gap: "10px"
        }}>
          <span style={{ width: 8, height: 8, borderRadius: "50%", background: score.color, flexShrink: 0 }} />
          <span style={{ color: score.color, fontWeight: 600, fontSize: "0.9rem" }}>
            {app.score_label?.emoji} {app.score_label?.label}
          </span>
          <span style={{ color: "var(--muted)", fontSize: "0.875rem" }}>
            — {app.benchmarking}
          </span>
        </div>
      </div>

      {/* Guilt Trip */}
      {app.guilt_trip && (
        <div className="fade-up-delay-1" style={{
          background: "var(--surface)", border: "1px solid var(--border)",
          borderRadius: "16px", padding: "1.5rem", marginBottom: "1rem",
          borderLeft: "4px solid var(--red)"
        }}>
          <h2 style={{ fontSize: "1rem", fontWeight: 600, marginBottom: "8px", color: "var(--red)" }}>
            ⚠️ What this means for you
          </h2>
          <p style={{ color: "var(--text)", fontSize: "0.9rem", lineHeight: 1.7 }}>
            {app.guilt_trip}
          </p>
        </div>
      )}

      {/* Permissions */}
      <div className="fade-up-delay-1" style={{
        background: "var(--surface)", border: "1px solid var(--border)",
        borderRadius: "16px", padding: "1.5rem", marginBottom: "1rem"
      }}>
        <h2 style={{ fontSize: "1rem", fontWeight: 600, marginBottom: "4px" }}>Permissions</h2>
        <p style={{ color: "var(--muted)", fontSize: "0.85rem", marginBottom: "1.25rem" }}>
          These are the device features this app can access
        </p>

        {[...highRiskPerms, ...mediumRiskPerms, ...lowRiskPerms].map((p, i) => {
          const tier = tierConfig[p.tier] || tierConfig["LOW"]
          return (
            <div key={i} style={{
              display: "flex", alignItems: "flex-start", gap: "12px",
              padding: "12px 14px", borderRadius: "10px",
              background: "var(--surface2)", marginBottom: "8px",
              border: "1px solid var(--border)"
            }}>
              <span style={{
                width: 8, height: 8, borderRadius: "50%",
                flexShrink: 0, marginTop: "6px", background: tier.color
              }} />
              <div style={{ flex: 1 }}>
                <p style={{ fontWeight: 600, fontSize: "0.95rem" }}>{p.permission}</p>
                <p style={{ color: "var(--muted)", fontSize: "0.82rem", marginTop: "3px", lineHeight: 1.5 }}>
                  {p.plain_english}
                </p>
                {p.why_scary && p.tier === "HIGH" && (
                  <p style={{
                    color: "var(--red)", fontSize: "0.78rem",
                    marginTop: "4px", lineHeight: 1.4, fontStyle: "italic"
                  }}>
                    ⚠️ {p.why_scary}
                  </p>
                )}
              </div>
              <span style={{
                padding: "3px 10px", borderRadius: "100px",
                fontSize: "0.72rem", fontWeight: 600,
                flexShrink: 0, marginTop: "2px", whiteSpace: "nowrap",
                color: tier.color, background: tier.bg, border: `1px solid ${tier.border}`
              }}>
                {tier.label}
              </span>
            </div>
          )
        })}
      </div>

      {/* Trackers */}
      {app.raw_trackers?.length > 0 && (
        <div className="fade-up-delay-2" style={{
          background: "var(--surface)", border: "1px solid var(--border)",
          borderRadius: "16px", padding: "1.5rem", marginBottom: "1rem"
        }}>
          <h2 style={{ fontSize: "1rem", fontWeight: 600, marginBottom: "4px" }}>Trackers</h2>
          <p style={{ color: "var(--muted)", fontSize: "0.85rem", marginBottom: "1.25rem" }}>
            These third-party companies receive data about how you use this app
          </p>
          <div style={{ display: "flex", gap: "8px", flexWrap: "wrap" }}>
            {app.raw_trackers.map((t, i) => (
              <TrackerBadge key={i} name={t.name} />
            ))}
          </div>
        </div>
      )}

      {/* Safer Alternative */}
      {app.alternative && (
        <div className="fade-up-delay-2" style={{
          background: "rgba(5,150,105,0.04)",
          border: "1px solid rgba(5,150,105,0.2)",
          borderRadius: "16px", padding: "1.5rem", marginBottom: "1rem"
        }}>
          <h2 style={{ fontSize: "1rem", fontWeight: 600, marginBottom: "8px", color: "var(--green)" }}>
            ✓ Safer Alternative
          </h2>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: "0.5rem" }}>
            <div>
              <p style={{ fontWeight: 700, fontSize: "1.1rem", marginBottom: "4px" }}>
                {app.alternative.alternative}
              </p>
              <p style={{ color: "var(--muted)", fontSize: "0.85rem" }}>
                {app.alternative.reason}
              </p>
            </div>
            <span style={{
              background: "rgba(5,150,105,0.1)",
              border: "1px solid rgba(5,150,105,0.3)",
              color: "var(--green)", padding: "6px 14px",
              borderRadius: "100px", fontWeight: 700, fontSize: "0.85rem"
            }}>
              {app.alternative.score_improvement}
            </span>
          </div>
        </div>
      )}

      {/* How to protect */}
      <div className="fade-up-delay-3" style={{
        background: "var(--surface)", border: "1px solid var(--border)",
        borderRadius: "16px", padding: "1.5rem"
      }}>
        <h2 style={{ fontSize: "1rem", fontWeight: 600, marginBottom: "8px" }}>
          How to protect yourself
        </h2>
        <p style={{ color: "var(--text)", fontSize: "0.9rem", lineHeight: 1.7 }}>
          Go to <strong>Settings → Apps → {app.app_name} → Permissions</strong> and
          revoke any permissions marked High Risk — especially microphone, camera, and precise location.
        </p>
      </div>

    </div>
  )
}// src/pages/AppResult.jsx
import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"
import AnimatedScore from "../components/AnimatedScore"
import TrackerBadge from "../components/TrackerBadge"

const tierConfig = {
  HIGH: { color: "var(--red)", bg: "rgba(229,57,53,0.08)", border: "rgba(229,57,53,0.2)", label: "High risk" },
  MEDIUM: { color: "var(--yellow)", bg: "rgba(245,158,11,0.08)", border: "rgba(245,158,11,0.2)", label: "Medium risk" },
  LOW: { color: "var(--green)", bg: "rgba(5,150,105,0.08)", border: "rgba(5,150,105,0.2)", label: "Low risk" }
}

const scoreConfig = (score) => {
  if (score >= 70) return { color: "var(--green)", label: "Low Risk" }
  if (score >= 40) return { color: "var(--yellow)", label: "Medium Risk" }
  return { color: "var(--red)", label: "High Risk" }
}

export default function AppResult() {
  const { appName } = useParams()
  const [app, setApp] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [appIcon, setAppIcon] = useState(null)

  useEffect(() => {
    fetch(`http://localhost:8001/app/${appName}`)
      .then(res => {
        if (!res.ok) throw new Error("Not found")
        return res.json()
      })
      .then(data => {
        setApp(data)
        setLoading(false)
      })
      .catch(() => {
        setError(true)
        setLoading(false)
      })
  }, [appName])

  useEffect(() => {
    if (!app) return
    fetch(`http://localhost:8001/api/icon/${encodeURIComponent(app.app_name)}`)
      .then(res => res.json())
      .then(data => { if (data.icon) setAppIcon(data.icon) })
      .catch(() => {})
  }, [app])

  if (loading) return (
    <div style={{
      minHeight: "100vh", background: "var(--bg)",
      display: "flex", flexDirection: "column",
      alignItems: "center", justifyContent: "center", gap: "1rem"
    }}>
      <div style={{
        width: "36px", height: "36px",
        border: "3px solid var(--border)",
        borderTop: "3px solid var(--red)",
        borderRadius: "50%", animation: "spin 0.8s linear infinite"
      }} />
      <p style={{ color: "var(--muted)", fontSize: "0.9rem" }}>Scanning {appName}...</p>
    </div>
  )

  if (error || !app) return (
    <div style={{
      minHeight: "100vh", background: "var(--bg)",
      display: "flex", flexDirection: "column",
      alignItems: "center", justifyContent: "center", gap: "1rem"
    }}>
      <p style={{ fontSize: "1.5rem" }}>😕</p>
      <p style={{ fontWeight: 600, fontSize: "1.1rem" }}>We couldn't find that app</p>
      <p style={{ color: "var(--muted)", fontSize: "0.9rem" }}>Try searching for a different app name</p>
      <a href="/" style={{ marginTop: "0.5rem", color: "var(--red)", textDecoration: "none", fontWeight: 600 }}>← Go back</a>
    </div>
  )

  const score = scoreConfig(app.privacy_score)
  const highRiskPerms = app.permissions?.filter(p => p.tier === "HIGH") || []
  const mediumRiskPerms = app.permissions?.filter(p => p.tier === "MEDIUM") || []
  const lowRiskPerms = app.permissions?.filter(p => p.tier === "LOW") || []

  return (
    <div style={{
      minHeight: "100vh", background: "var(--bg)",
      padding: "2rem", maxWidth: "680px", margin: "0 auto"
    }}>

      {/* Back */}
      <a href="/" style={{
        display: "inline-flex", alignItems: "center", gap: "6px",
        color: "var(--muted)", textDecoration: "none",
        fontSize: "0.9rem", marginBottom: "1.5rem"
      }}>← Back</a>

      {/* Header Card */}
      <div className="fade-up" style={{
        background: "var(--surface)", border: "1px solid var(--border)",
        borderRadius: "16px", padding: "1.75rem", marginBottom: "1rem"
      }}>
        <div style={{
          display: "flex", justifyContent: "space-between",
          alignItems: "flex-start", flexWrap: "wrap", gap: "1rem"
        }}>
          {/* Left — icon + name */}
          <div style={{ display: "flex", alignItems: "center", gap: "1rem" }}>
            {appIcon && (
              <img src={appIcon} alt={app.app_name} style={{
                width: "64px", height: "64px", borderRadius: "16px",
                flexShrink: 0, boxShadow: "0 2px 12px rgba(0,0,0,0.1)"
              }} />
            )}
            <div>
              <h1 style={{
                fontSize: "2.2rem", fontWeight: 700,
                letterSpacing: "-0.02em", marginBottom: "6px"
              }}>
                {app.app_name}
              </h1>
              <p style={{ color: "var(--muted)", fontSize: "0.9rem" }}>
                {app.permissions?.length || 0} permissions · {app.raw_trackers?.length || 0} trackers found
              </p>
            </div>
          </div>

          {/* Score Circle */}
          <div style={{
            width: "90px", height: "90px", borderRadius: "50%",
            border: `3px solid ${score.color}`,
            display: "flex", flexDirection: "column",
            alignItems: "center", justifyContent: "center", flexShrink: 0
          }}>
            <span style={{ fontSize: "1.8rem", fontWeight: 700, color: score.color, lineHeight: 1 }}>
              <AnimatedScore target={app.privacy_score} />
            </span>
            <span style={{ fontSize: "0.65rem", color: "var(--muted)" }}>/100</span>
          </div>
        </div>

        {/* Risk Banner */}
        <div style={{
          marginTop: "1.25rem", padding: "12px 16px",
          background: `${score.color}10`,
          border: `1px solid ${score.color}30`,
          borderRadius: "10px", display: "flex", alignItems: "center", gap: "10px"
        }}>
          <span style={{ width: 8, height: 8, borderRadius: "50%", background: score.color, flexShrink: 0 }} />
          <span style={{ color: score.color, fontWeight: 600, fontSize: "0.9rem" }}>
            {app.score_label?.emoji} {app.score_label?.label}
          </span>
          <span style={{ color: "var(--muted)", fontSize: "0.875rem" }}>
            — {app.benchmarking}
          </span>
        </div>
      </div>

      {/* Guilt Trip */}
      {app.guilt_trip && (
        <div className="fade-up-delay-1" style={{
          background: "var(--surface)", border: "1px solid var(--border)",
          borderRadius: "16px", padding: "1.5rem", marginBottom: "1rem",
          borderLeft: "4px solid var(--red)"
        }}>
          <h2 style={{ fontSize: "1rem", fontWeight: 600, marginBottom: "8px", color: "var(--red)" }}>
            ⚠️ What this means for you
          </h2>
          <p style={{ color: "var(--text)", fontSize: "0.9rem", lineHeight: 1.7 }}>
            {app.guilt_trip}
          </p>
        </div>
      )}

      {/* Permissions */}
      <div className="fade-up-delay-1" style={{
        background: "var(--surface)", border: "1px solid var(--border)",
        borderRadius: "16px", padding: "1.5rem", marginBottom: "1rem"
      }}>
        <h2 style={{ fontSize: "1rem", fontWeight: 600, marginBottom: "4px" }}>Permissions</h2>
        <p style={{ color: "var(--muted)", fontSize: "0.85rem", marginBottom: "1.25rem" }}>
          These are the device features this app can access
        </p>

        {[...highRiskPerms, ...mediumRiskPerms, ...lowRiskPerms].map((p, i) => {
          const tier = tierConfig[p.tier] || tierConfig["LOW"]
          return (
            <div key={i} style={{
              display: "flex", alignItems: "flex-start", gap: "12px",
              padding: "12px 14px", borderRadius: "10px",
              background: "var(--surface2)", marginBottom: "8px",
              border: "1px solid var(--border)"
            }}>
              <span style={{
                width: 8, height: 8, borderRadius: "50%",
                flexShrink: 0, marginTop: "6px", background: tier.color
              }} />
              <div style={{ flex: 1 }}>
                <p style={{ fontWeight: 600, fontSize: "0.95rem" }}>{p.permission}</p>
                <p style={{ color: "var(--muted)", fontSize: "0.82rem", marginTop: "3px", lineHeight: 1.5 }}>
                  {p.plain_english}
                </p>
                {p.why_scary && p.tier === "HIGH" && (
                  <p style={{
                    color: "var(--red)", fontSize: "0.78rem",
                    marginTop: "4px", lineHeight: 1.4, fontStyle: "italic"
                  }}>
                    ⚠️ {p.why_scary}
                  </p>
                )}
              </div>
              <span style={{
                padding: "3px 10px", borderRadius: "100px",
                fontSize: "0.72rem", fontWeight: 600,
                flexShrink: 0, marginTop: "2px", whiteSpace: "nowrap",
                color: tier.color, background: tier.bg, border: `1px solid ${tier.border}`
              }}>
                {tier.label}
              </span>
            </div>
          )
        })}
      </div>

      {/* Trackers */}
      {app.raw_trackers?.length > 0 && (
        <div className="fade-up-delay-2" style={{
          background: "var(--surface)", border: "1px solid var(--border)",
          borderRadius: "16px", padding: "1.5rem", marginBottom: "1rem"
        }}>
          <h2 style={{ fontSize: "1rem", fontWeight: 600, marginBottom: "4px" }}>Trackers</h2>
          <p style={{ color: "var(--muted)", fontSize: "0.85rem", marginBottom: "1.25rem" }}>
            These third-party companies receive data about how you use this app
          </p>
          <div style={{ display: "flex", gap: "8px", flexWrap: "wrap" }}>
            {app.raw_trackers.map((t, i) => (
              <TrackerBadge key={i} name={t.name} />
            ))}
          </div>
        </div>
      )}

      {/* Safer Alternative */}
      {app.alternative && (
        <div className="fade-up-delay-2" style={{
          background: "rgba(5,150,105,0.04)",
          border: "1px solid rgba(5,150,105,0.2)",
          borderRadius: "16px", padding: "1.5rem", marginBottom: "1rem"
        }}>
          <h2 style={{ fontSize: "1rem", fontWeight: 600, marginBottom: "8px", color: "var(--green)" }}>
            ✓ Safer Alternative
          </h2>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: "0.5rem" }}>
            <div>
              <p style={{ fontWeight: 700, fontSize: "1.1rem", marginBottom: "4px" }}>
                {app.alternative.alternative}
              </p>
              <p style={{ color: "var(--muted)", fontSize: "0.85rem" }}>
                {app.alternative.reason}
              </p>
            </div>
            <span style={{
              background: "rgba(5,150,105,0.1)",
              border: "1px solid rgba(5,150,105,0.3)",
              color: "var(--green)", padding: "6px 14px",
              borderRadius: "100px", fontWeight: 700, fontSize: "0.85rem"
            }}>
              {app.alternative.score_improvement}
            </span>
          </div>
        </div>
      )}

      {/* How to protect */}
      <div className="fade-up-delay-3" style={{
        background: "var(--surface)", border: "1px solid var(--border)",
        borderRadius: "16px", padding: "1.5rem"
      }}>
        <h2 style={{ fontSize: "1rem", fontWeight: 600, marginBottom: "8px" }}>
          How to protect yourself
        </h2>
        <p style={{ color: "var(--text)", fontSize: "0.9rem", lineHeight: 1.7 }}>
          Go to <strong>Settings → Apps → {app.app_name} → Permissions</strong> and
          revoke any permissions marked High Risk — especially microphone, camera, and precise location.
        </p>
      </div>

    </div>
  )
}