// src/pages/ScreenshotScan.jsx
import { useState, useRef, useEffect } from "react"
import { useNavigate } from "react-router-dom"
import { calculateScore, getRiskLevel } from "../utils/scorer"

const riskColor = {
  high: "var(--red)",
  medium: "var(--yellow)",
  low: "var(--green)"
}

const riskBg = {
  high: "rgba(229,57,53,0.08)",
  medium: "rgba(245,158,11,0.08)",
  low: "rgba(5,150,105,0.08)"
}

const riskBorder = {
  high: "rgba(229,57,53,0.2)",
  medium: "rgba(245,158,11,0.2)",
  low: "rgba(5,150,105,0.2)"
}

export default function ScreenshotScan() {
  const [image, setImage] = useState(null)
  const [preview, setPreview] = useState(null)
  const [loading, setLoading] = useState(false)
  const [results, setResults] = useState(null)
  const [appsDetected, setAppsDetected] = useState([])
  const [search, setSearch] = useState("")
  const [error, setError] = useState(null)
  const [icons, setIcons] = useState({})
  const fileRef = useRef()
  const navigate = useNavigate()

  const handleFile = (file) => {
    if (!file) return
    setImage(file)
    setPreview(URL.createObjectURL(file))
    setResults(null)
    setError(null)
  }

  const handleDrop = (e) => {
    e.preventDefault()
    const file = e.dataTransfer.files[0]
    if (file) handleFile(file)
  }

  const handleScan = async () => {
  if (!image) return
  setLoading(true)
  setError(null)

  const formData = new FormData()
  formData.append("image", image)

  try {
    // Step 1 — port 8000 reads the screenshot and returns app names
    const res = await fetch("http://localhost:8000/api/scan-screenshot", {
      method: "POST",
      body: formData
    })
    const data = await res.json()

    if (data.error) {
      setError(data.error)
      setLoading(false)
      return
    }

    const detectedNames = data.apps_detected || []
    if (detectedNames.length === 0) {
      setError("No apps detected in screenshot")
      setLoading(false)
      return
    }

    setAppsDetected(detectedNames)

    // Step 2 — for each app name, ask port 8001 for the real privacy score
    const scored = await Promise.all(
      detectedNames.map(async (name) => {
        try {
          const appRes = await fetch(`http://localhost:8001/app/${encodeURIComponent(name)}`)
          if (!appRes.ok) throw new Error("Not found")
          const appData = await appRes.json()

          // Use privacy_score directly from port 8001
          const score = appData.privacy_score
          const riskLevel = getRiskLevel(score)

          return {
            app_name: appData.app_name || name,
            privacy_score: score,
            privacyScore: score,
            riskLevel,
            permissions: appData.permissions || [],
            raw_trackers: appData.raw_trackers || [],
            permission_count: appData.permissions?.length || 0,
            tracker_count: appData.raw_trackers?.length || 0,
            package_name: appData.package_name || ""
          }
        } catch {
          // App not found in port 8001 — show with no data
          return {
            app_name: name,
            privacy_score: undefined,
            privacyScore: undefined,
            riskLevel: null,
            permissions: [],
            raw_trackers: [],
            permission_count: 0,
            tracker_count: 0,
            package_name: ""
          }
        }
      })
    )

    // Sort — most dangerous (lowest score) first
    const sorted = scored.sort((a, b) => {
      if (a.privacy_score === undefined) return 1
      if (b.privacy_score === undefined) return -1
      return a.privacy_score - b.privacy_score
    })

    setResults(sorted)

  } catch (err) {
    setError("Could not connect to server. Make sure both backends are running.")
  }

  setLoading(false)
}
  useEffect(() => {
    if (!results) return
    results.forEach(app => {
      fetch(`http://localhost:8001/api/icon/${encodeURIComponent(app.app_name)}`)
        .then(res => res.json())
        .then(data => {
          if (data.icon) {
            setIcons(prev => ({ ...prev, [app.app_name]: data.icon }))
          }
        })
        .catch(() => {})
    })
  }, [results])

  const filtered = results
    ? results.filter(app =>
        app.app_name.toLowerCase().includes(search.toLowerCase())
      )
    : []

  return (
    <div style={{
      minHeight: "100vh", background: "var(--bg)",
      padding: "2rem", maxWidth: "720px", margin: "0 auto"
    }}>

      {/* Back */}
      <a href="/" style={{
        display: "inline-flex", alignItems: "center", gap: "6px",
        color: "var(--muted)", textDecoration: "none",
        fontSize: "0.9rem", marginBottom: "1.5rem"
      }}>← Back</a>

      <h1 style={{
        fontSize: "2rem", fontWeight: 700,
        letterSpacing: "-0.02em", marginBottom: "8px"
      }}>
        Scan your phone
      </h1>
      <p style={{ color: "var(--muted)", fontSize: "0.95rem", marginBottom: "2rem" }}>
        Upload a screenshot of your home screen and we'll audit every app we can find.
      </p>

      {/* Upload Area */}
      {!results && (
        <div
          onDrop={handleDrop}
          onDragOver={e => e.preventDefault()}
          onClick={() => fileRef.current.click()}
          style={{
            border: `2px dashed ${preview ? "var(--green)" : "var(--border)"}`,
            borderRadius: "16px", padding: "2.5rem",
            textAlign: "center", cursor: "pointer",
            background: preview ? "rgba(5,150,105,0.03)" : "var(--surface)",
            transition: "all 0.2s", marginBottom: "1.5rem"
          }}
        >
          <input
            ref={fileRef}
            type="file"
            accept="image/*"
            style={{ display: "none" }}
            onChange={e => handleFile(e.target.files[0])}
          />

          {preview ? (
            <div>
              <img
                src={preview}
                alt="Screenshot preview"
                style={{
                  maxHeight: "300px", borderRadius: "12px",
                  marginBottom: "1rem",
                  boxShadow: "0 4px 20px rgba(0,0,0,0.1)"
                }}
              />
              <p style={{ color: "var(--green)", fontWeight: 600, fontSize: "0.9rem" }}>
                ✓ Screenshot ready — click Scan to analyze
              </p>
              <p style={{ color: "var(--muted)", fontSize: "0.8rem", marginTop: "4px" }}>
                Click to change image
              </p>
            </div>
          ) : (
            <div>
              <p style={{ fontSize: "2.5rem", marginBottom: "0.75rem" }}>📱</p>
              <p style={{ fontWeight: 600, fontSize: "1rem", marginBottom: "6px" }}>
                Drop your screenshot here
              </p>
              <p style={{ color: "var(--muted)", fontSize: "0.85rem" }}>
                or click to browse · supports PNG, JPG
              </p>
            </div>
          )}
        </div>
      )}

      {/* Scan Button */}
      {preview && !results && (
        <button
          onClick={handleScan}
          disabled={loading}
          style={{
            width: "100%", padding: "14px",
            background: loading ? "var(--border)" : "var(--red)",
            border: "none", borderRadius: "12px",
            color: loading ? "var(--muted)" : "white",
            fontSize: "1rem", fontWeight: 600,
            fontFamily: "'DM Sans', sans-serif",
            cursor: loading ? "not-allowed" : "pointer",
            transition: "all 0.2s", marginBottom: "1rem"
          }}
        >
          {loading ? "Analyzing screenshot..." : "Scan my apps"}
        </button>
      )}

      {/* Loading State */}
      {loading && (
        <div style={{
          textAlign: "center", padding: "2rem",
          background: "var(--surface)", borderRadius: "16px",
          border: "1px solid var(--border)"
        }}>
          <div style={{
            width: "36px", height: "36px",
            border: "3px solid var(--border)",
            borderTop: "3px solid var(--red)",
            borderRadius: "50%",
            animation: "spin 0.8s linear infinite",
            margin: "0 auto 1rem"
          }} />
          <p style={{ fontWeight: 600, marginBottom: "4px" }}>
            Analyzing your screenshot...
          </p>
          <p style={{ color: "var(--muted)", fontSize: "0.85rem" }}>
            Gemini is reading your app icons
          </p>
        </div>
      )}

      {/* Error */}
      {error && (
        <div style={{
          padding: "1rem 1.25rem",
          background: "rgba(229,57,53,0.06)",
          border: "1px solid rgba(229,57,53,0.2)",
          borderRadius: "12px", marginBottom: "1rem"
        }}>
          <p style={{ color: "var(--red)", fontWeight: 600, fontSize: "0.9rem" }}>
            {error}
          </p>
        </div>
      )}

      {/* Results */}
      {results && (
        <div className="fade-up">

          {/* Summary */}
          <div style={{
            background: "var(--surface)", border: "1px solid var(--border)",
            borderRadius: "16px", padding: "1.25rem 1.5rem",
            marginBottom: "1.25rem",
            display: "flex", justifyContent: "space-between",
            alignItems: "center", flexWrap: "wrap", gap: "1rem"
          }}>
            <div>
              <p style={{ fontWeight: 600, fontSize: "1rem" }}>
                Found {appsDetected.length} apps on your screen
              </p>
              <p style={{ color: "var(--muted)", fontSize: "0.85rem", marginTop: "3px" }}>
                {results.filter(a => a.riskLevel === "high").length} high risk ·{" "}
                {results.filter(a => a.riskLevel === "medium").length} medium ·{" "}
                {results.filter(a => a.riskLevel === "low").length} low risk
              </p>
            </div>
            <button
              onClick={() => {
                setResults(null)
                setPreview(null)
                setImage(null)
                setIcons({})
              }}
              style={{
                padding: "8px 16px", background: "transparent",
                border: "1px solid var(--border)", borderRadius: "8px",
                color: "var(--muted)", fontSize: "0.85rem",
                cursor: "pointer", fontFamily: "'DM Sans', sans-serif"
              }}
            >
              Scan another
            </button>
          </div>

          {/* Search */}
          <input
            value={search}
            onChange={e => setSearch(e.target.value)}
            placeholder="Search your apps..."
            style={{
              width: "100%", padding: "12px 16px",
              background: "var(--surface)",
              border: "1px solid var(--border)",
              borderRadius: "12px", color: "var(--text)",
              fontSize: "0.95rem", fontFamily: "'DM Sans', sans-serif",
              outline: "none", marginBottom: "1rem",
              boxSizing: "border-box"
            }}
          />

          {/* App Grid */}
          <div style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fill, minmax(160px, 1fr))",
            gap: "12px"
          }}>
            {filtered.map((app, i) => {
              const iconUrl = icons[app.app_name] || null

              return (
                <div
                  key={i}
                  onClick={() => navigate(`/app/${app.app_name}`)}
                  style={{
                    background: "var(--surface)",
                    border: `1px solid ${riskBorder[app.riskLevel] || "var(--border)"}`,
                    borderRadius: "14px", padding: "1.25rem",
                    cursor: "pointer", transition: "all 0.2s",
                    textAlign: "center"
                  }}
                  onMouseOver={e => e.currentTarget.style.transform = "translateY(-2px)"}
                  onMouseOut={e => e.currentTarget.style.transform = "translateY(0)"}
                >
                  {/* App Icon */}
                  <div style={{
                    width: "56px", height: "56px", borderRadius: "14px",
                    margin: "0 auto 10px",
                    overflow: "hidden",
                    display: "flex", alignItems: "center", justifyContent: "center",
                    fontSize: "1.4rem", fontWeight: 700,
                    background: iconUrl ? "transparent" : `hsl(${app.app_name.charCodeAt(0) * 15 % 360}, 55%, 88%)`,
                    color: `hsl(${app.app_name.charCodeAt(0) * 15 % 360}, 40%, 35%)`
                  }}>
                    {iconUrl ? (
                      <img
                        src={iconUrl}
                        alt={app.app_name}
                        style={{
                          width: "100%", height: "100%",
                          objectFit: "cover", borderRadius: "14px"
                        }}
                        onError={e => {
                          e.target.style.display = "none"
                          e.target.parentNode.innerText = app.app_name.charAt(0).toUpperCase()
                        }}
                      />
                    ) : (
                      app.app_name.charAt(0).toUpperCase()
                    )}
                  </div>

                  {/* App name */}
                  <p style={{
                    fontWeight: 600, fontSize: "0.88rem",
                    marginBottom: "8px", lineHeight: 1.3
                  }}>
                    {app.app_name}
                  </p>

                  {/* Risk badge */}
                  {app.riskLevel ? (
                    <span style={{
                      display: "inline-block",
                      padding: "3px 10px", borderRadius: "100px",
                      fontSize: "0.7rem", fontWeight: 600,
                      color: riskColor[app.riskLevel],
                      background: riskBg[app.riskLevel],
                      border: `1px solid ${riskBorder[app.riskLevel]}`
                    }}>
                      {app.riskLevel === "high" ? "High risk" : app.riskLevel === "medium" ? "Medium risk" : "Low risk"}
                    </span>
                  ) : (
                    <span style={{
                      display: "inline-block",
                      padding: "3px 10px", borderRadius: "100px",
                      fontSize: "0.7rem", fontWeight: 600,
                      color: "var(--muted)",
                      background: "var(--surface2)",
                      border: "1px solid var(--border)"
                    }}>
                      No data
                    </span>
                  )}

                  {/* Score */}
                  {app.privacyScore !== undefined && (
                    <p style={{
                      color: riskColor[app.riskLevel],
                      fontSize: "0.85rem", fontWeight: 700,
                      marginTop: "8px"
                    }}>
                      {app.privacyScore}/100
                    </p>
                  )}

                  <p style={{ color: "var(--muted)", fontSize: "0.75rem", marginTop: "3px" }}>
                    {app.permission_count > 0
                      ? `${app.permission_count} permissions`
                      : "Unknown permissions"}
                  </p>
                </div>
              )
            })}
          </div>

          {filtered.length === 0 && search && (
            <p style={{ color: "var(--muted)", textAlign: "center", padding: "2rem" }}>
              No apps found matching "{search}"
            </p>
          )}

        </div>
      )}
    </div>
  )
}