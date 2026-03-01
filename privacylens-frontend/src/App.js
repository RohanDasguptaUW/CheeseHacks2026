import { BrowserRouter, Routes, Route } from "react-router-dom"
import Home from "./pages/Home"
import AppResult from "./pages/AppResult"
import Dashboard from "./pages/Dashboard"
import Compare from "./pages/Compare"
import ScreenshotScan from "./pages/ScreenshotScan"



export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/app/:appName" element={<AppResult />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/compare" element={<Compare />} />
        <Route path="/scan" element={<ScreenshotScan />} />
      </Routes>
    </BrowserRouter>
  )
}