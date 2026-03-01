import { useEffect, useState } from "react"

function AnimatedScore({ target }) {
  const [display, setDisplay] = useState(0)

  useEffect(() => {
    let current = 0
    const step = setInterval(() => {
      current += 1
      setDisplay(current)
      if (current >= target) clearInterval(step)
    }, 15)
    return () => clearInterval(step)
  }, [target])

  return <span>{display}</span>
}

export default AnimatedScore