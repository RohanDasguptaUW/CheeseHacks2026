## Inspiration

Most people have no idea what their apps are actually doing. You install a flashlight app and it quietly requests your precise GPS coordinates, microphone, and contact list — and you just tap "Allow" because the permission dialog is a wall of legalese at 2am. We wanted to build something that answers one question every smartphone user should be able to ask: *"Is this app spying on me?"* — and get a real answer in plain English, not a 47-page privacy policy.

## What it does

**PrivacyLens** is a privacy auditing tool that scans any Android app and tells you exactly how much of your life it can access.

- **App Audit** — Search any app by name and get a 0–100 Privacy Score, a risk tier (Safe / Moderate / High / Dangerous), and a plain-English breakdown of every permission it holds and why each one matters
- **Suspicious Combo Detection** — Flags dangerous permission combinations, like an app that has both your microphone *and* precise location, which is a classic surveillance pattern
- **Side-by-Side Comparison** — Compare two apps head-to-head to see which is less invasive (e.g. Spotify vs. Apple Music)
- **Full Phone Audit** — Paste in your full app list and get an overall Privacy Health Score for your phone, with a per-app breakdown
- **Privacy Time Machine** — See how an app's data collection has grown since its initial release, measuring "permission creep" year by year
- **AI Guilt Trip** — Gemini 2.5 Flash generates a 2–3 sentence, jargon-free explanation of what an app's permissions mean *for you specifically*, written for a real person, not a lawyer
- **Privacy Policy Analyzer** — Paste any privacy policy and Gemini extracts the 3 most alarming things the company is actually allowed to do with your data
- **Alternative Suggestions** — Recommends a privacy-respecting substitute for high-risk apps (e.g. Signal instead of WhatsApp, +28 points)
- **Category Benchmarking** — Shows how an app compares to others in its category ("Worse than 68% of social media apps")

## How we built it

We split into four parallel workstreams that integrated at the API layer:

- **Data Pipeline (Person 1):** Python scraper querying the [Exodus Privacy](https://reports.exodus-privacy.eu.org/) API and Google Play Store to pull real-world permission and tracker data for any app by name
- **Scoring Engine (Person 2):** A weighted penalty system in `scorer.py` that deducts points for high-risk permissions (microphone: −20, precise location: −15), tracker count (up to −30), and suspicious permission combos. Also handles risk-tier classification, category benchmarking, and version-history growth rate
- **REST API (Person 3/4):** FastAPI backend with five endpoints (`/app/{name}`, `/compare`, `/audit`, `/timeline`, `/`) with CORS enabled for the React frontend
- **Frontend (Person 3):** React dashboard consuming the FastAPI endpoints and rendering scores, risk tiers, and permission breakdowns
- **AI Layer:** Google Gemini 2.5 Flash via `gemini_helper.py` for the plain-English guilt-trip summaries and privacy policy extraction

## Challenges we ran into

- **Real data is messy.** The Exodus Privacy API doesn't always find apps by display name — package names like `com.zhiliaoapp.musically` are needed, not "TikTok." We built a fallback chain: Exodus → Google Play scraper → curated local database.
- **Permission naming is inconsistent.** Exodus returns technical Android permission strings (`ACCESS_FINE_LOCATION`), the Play Store returns human labels ("Precise Location"), and our scoring engine needed both. Normalizing across three sources without losing data took significant effort.
- **Coordinating four people's outputs at a hackathon.** Person 1's `get_app_data()` output shape had to exactly match what Person 2's `analyze_from_fetcher()` expected, which then had to match Eric's API response schema. We wrote a bridge function and a shared mock database so all four tracks could build in parallel without blocking each other.
- **Avoiding alarm fatigue.** Early versions flagged everything as dangerous. We tuned the penalty weights so that a genuinely low-risk app like a calculator scores 90+, while a surveillance-heavy app like a free flashlight scores below 20 — making the signal meaningful.

## Accomplishments that we're proud of

- The **suspicious combo detector** genuinely surfaces patterns that individual permission flags miss. An app with camera alone isn't alarming; an app with camera + microphone + precise location is a surveillance suite, and we catch that.
- The **AI guilt trip** feature resonates immediately with users. Telling someone "TikTok can cross-reference your physical location with your contact list to build a social graph of everyone you know — including people who've never downloaded the app" is far more impactful than listing `ACCESS_FINE_LOCATION`.
- We shipped a **working end-to-end pipeline** — real data in, scored JSON out, rendered in a UI — in a single hackathon session, across four people who had never worked together before.

## What we learned

- Privacy scoring is inherently opinionated. Choosing penalty weights forced us to take explicit positions on what counts as high-risk, which made us research the real-world implications of each permission more deeply than we expected.
- LLMs are excellent at the "translation layer" between technical data and human understanding. Gemini takes a permission list and turns it into something your grandparent would find alarming — that's the whole product value.
- Mock data is a superpower for parallel development. By agreeing on the shape of data at each interface upfront, all four of us could build and test independently before integration.

## What's next for PrivacyLens

- **iOS support** — extend the data pipeline to the App Store and Apple's permission system
- **Browser extension** — scan an app's Play Store page in-context and show the Privacy Score as an overlay before you install it
- **Automatic phone scan** — on-device analysis using Android's `PackageManager` API so users can audit all installed apps without manually entering names
- **Historical trending** — track score changes over time as apps push updates, and alert users when a previously safe app quietly adds new permissions
- **Crowd-sourced ratings** — let users flag permissions they find surprising or unjustified, building a community trust layer on top of the technical score
