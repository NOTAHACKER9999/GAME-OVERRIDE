import js

try:
    # Try to open DuckDuckGo in a new tab
    js.window.open("https://duckduckgo.com", "_blank")
except Exception as e:
    # Fallback: alert if opening fails
    js.console.error(f"Failed to open DuckDuckGo: {e}")
