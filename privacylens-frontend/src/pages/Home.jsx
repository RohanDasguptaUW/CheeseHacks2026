// src/pages/Home.jsx
import { useState } from "react"
import { useNavigate } from "react-router-dom"

export default function Home() {
  const [appName, setAppName] = useState("")
  const [focused, setFocused] = useState(false)
  const navigate = useNavigate()

  const handleScan = () => {
    if (appName.trim()) navigate(`/app/${appName.trim()}`)
  }

  return (
    <div style={{
      minHeight: "100vh", background: "var(--bg)",
      display: "flex", flexDirection: "column",
      alignItems: "center", justifyContent: "center",
      padding: "2rem"
    }}>
      <div style={{ maxWidth: "580px", width: "100%", textAlign: "center" }}>

        {/* Eyebrow */}
        <p style={{
          fontSize: "0.8rem", fontWeight: 600, letterSpacing: "0.08em",
          color: "var(--red)", marginBottom: "1rem", textTransform: "uppercase"
        }}>
          Free Privacy Audit
        </p>

        {/* Title */}
        <h1 style={{
          fontSize: "clamp(2.2rem, 6vw, 3.5rem)",
          fontWeight: 700, lineHeight: 1.15,
          letterSpacing: "-0.03em", marginBottom: "1rem", color: "var(--text)"
        }}>
          How much do your apps{" "}
          <span style={{ color: "var(--red)" }}>actually know about you?</span>
        </h1>

        <p style={{
          color: "var(--muted)", fontSize: "1rem",
          marginBottom: "2rem", lineHeight: 1.6,
          maxWidth: "460px", margin: "0 auto 2rem"
        }}>
          Search any app to see its permissions, trackers, and privacy score — in plain English.
        </p>

        {/* Search */}
        <div style={{ display: "flex", gap: "10px", marginBottom: "1rem" }}>
          <input
            value={appName}
            onChange={e => setAppName(e.target.value)}
            onFocus={() => setFocused(true)}
            onBlur={() => setFocused(false)}
            onKeyDown={e => e.key === "Enter" && handleScan()}
            placeholder="Try 'TikTok' or 'Instagram'"
            style={{
              flex: 1, padding: "14px 18px",
              background: "var(--surface)",
              border: `1.5px solid ${focused ? "var(--red)" : "var(--border)"}`,
              borderRadius: "12px", color: "var(--text)",
              fontSize: "1rem", fontFamily: "'DM Sans', sans-serif",
              outline: "none", transition: "border-color 0.2s",
              boxShadow: focused ? "0 0 0 3px rgba(229,57,53,0.08)" : "none"
            }}
          />
          <button onClick={handleScan} style={{
            padding: "14px 24px", background: "var(--red)",
            border: "none", borderRadius: "12px",
            color: "white", fontSize: "1rem", fontWeight: 600,
            fontFamily: "'DM Sans', sans-serif", cursor: "pointer",
            transition: "opacity 0.2s"
          }}
            onMouseOver={e => e.target.style.opacity = "0.85"}
            onMouseOut={e => e.target.style.opacity = "1"}
          >
            Scan
          </button>
        </div>

        {/* Quick links */}
        <p style={{ fontSize: "0.8rem", color: "var(--muted)", marginBottom: "10px" }}>
          Popular searches
        </p>
        <div style={{
          display: "flex", gap: "8px", flexWrap: "wrap",
          justifyContent: "center", marginBottom: "1.5rem"
        }}>
          {["TikTok", "Instagram", "Snapchat", "Spotify", "WhatsApp", "Signal"].map(name => (
            <button key={name} onClick={() => navigate(`/app/${name}`)} style={{
              padding: "6px 14px", background: "var(--surface)",
              border: "1.5px solid var(--border)", borderRadius: "100px",
              color: "var(--muted)", fontSize: "0.85rem",
              fontFamily: "'DM Sans', sans-serif", cursor: "pointer",
              transition: "all 0.15s"
            }}
              onMouseOver={e => { e.target.style.borderColor = "var(--red)"; e.target.style.color = "var(--text)" }}
              onMouseOut={e => { e.target.style.borderColor = "var(--border)"; e.target.style.color = "var(--muted)" }}
            >
              {name}
            </button>
          ))}
        </div>

        {/* Action Buttons */}
        <div style={{
          display: "flex", flexDirection: "column",
          gap: "12px", width: "100%", marginBottom: "2.5rem"
        }}>
          <button onClick={() => navigate("/scan")} style={{
            width: "100%", padding: "16px 24px",
            background: "var(--text)", border: "none",
            borderRadius: "12px", color: "white",
            fontSize: "1rem", fontWeight: 600,
            fontFamily: "'DM Sans', sans-serif",
            cursor: "pointer", transition: "all 0.2s",
            display: "flex", alignItems: "center",
            justifyContent: "center", gap: "10px"
          }}
            onMouseOver={e => e.currentTarget.style.opacity = "0.85"}
            onMouseOut={e => e.currentTarget.style.opacity = "1"}
          >
            <span style={{ fontSize: "1.2rem" }}>📱</span>
            Scan my phone screenshot
            <span style={{
              background: "var(--red)", color: "white",
              fontSize: "0.7rem", fontWeight: 700,
              padding: "3px 8px", borderRadius: "100px",
              letterSpacing: "0.05em"
            }}>
              NEW
            </span>
          </button>

          <button onClick={() => navigate("/compare")} style={{
            width: "100%", padding: "14px 24px",
            background: "var(--surface)",
            border: "1.5px solid var(--border)",
            borderRadius: "12px", color: "var(--text)",
            fontSize: "1rem", fontWeight: 600,
            fontFamily: "'DM Sans', sans-serif",
            cursor: "pointer", transition: "all 0.2s",
            display: "flex", alignItems: "center",
            justifyContent: "center", gap: "10px"
          }}
            onMouseOver={e => {
              e.currentTarget.style.borderColor = "var(--text)"
              e.currentTarget.style.background = "var(--surface2)"
            }}
            onMouseOut={e => {
              e.currentTarget.style.borderColor = "var(--border)"
              e.currentTarget.style.background = "var(--surface)"
            }}
          >
            <span style={{ fontSize: "1.1rem" }}>⚖️</span>
            Compare two apps side by side
          </button>
        </div>

        {/* Stats Row */}
        <div style={{
          display: "grid", gridTemplateColumns: "1fr 1fr 1fr",
          gap: "12px", marginBottom: "2rem"
        }}>
          {[
            { number: "1000+", label: "Apps in database" },
            { number: "30+", label: "Permissions tracked" },
            { number: "100%", label: "Free to use" },
          ].map((stat, i) => (
            <div key={i} style={{
              background: "var(--surface)",
              border: "1px solid var(--border)",
              borderRadius: "12px", padding: "1rem",
              textAlign: "center"
            }}>
              <p style={{
                fontSize: "1.5rem", fontWeight: 700,
                color: "var(--text)", marginBottom: "4px"
              }}>
                {stat.number}
              </p>
              <p style={{ fontSize: "0.75rem", color: "var(--muted)" }}>
                {stat.label}
              </p>
            </div>
          ))}
        </div>

        {/* How it works */}
        <div style={{
          background: "var(--surface)",
          border: "1px solid var(--border)",
          borderRadius: "16px", padding: "1.5rem",
          textAlign: "left"
        }}>
          <p style={{ fontWeight: 700, fontSize: "0.95rem", marginBottom: "1rem" }}>
            How it works
          </p>
          {[
            { step: "1", title: "Search or scan", desc: "Type an app name or upload a screenshot of your home screen" },
            { step: "2", title: "We analyze it", desc: "We check permissions, trackers, and data sharing practices" },
            { step: "3", title: "You take control", desc: "See your privacy score and exactly how to fix any issues" },
          ].map((item, i) => (
            <div key={i} style={{
              display: "flex", gap: "12px", alignItems: "flex-start",
              marginBottom: i < 2 ? "1rem" : "0"
            }}>
              <div style={{
                width: "28px", height: "28px", borderRadius: "50%",
                background: "var(--red)", color: "white",
                display: "flex", alignItems: "center", justifyContent: "center",
                fontSize: "0.75rem", fontWeight: 700, flexShrink: 0
              }}>
                {item.step}
              </div>
              <div>
                <p style={{ fontWeight: 600, fontSize: "0.9rem", marginBottom: "2px" }}>
                  {item.title}
                </p>
                <p style={{ color: "var(--muted)", fontSize: "0.82rem", lineHeight: 1.5 }}>
                  {item.desc}
                </p>
              </div>
            </div>
          ))}
        </div>

      </div>
    </div>
  )
}