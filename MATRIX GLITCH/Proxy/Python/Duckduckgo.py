import js

# Get or create the iframe
iframe_id = "duckduckgo-frame"
iframe = js.document.getElementById(iframe_id)

if not iframe:
    iframe = js.document.createElement("iframe")
    iframe.id = iframe_id
    js.document.body.appendChild(iframe)

# Style iframe to cover the whole screen
iframe.style.position = "fixed"
iframe.style.top = "0"
iframe.style.left = "0"
iframe.style.width = "100%"
iframe.style.height = "100%"
iframe.style.border = "none"
iframe.style.margin = "0"
iframe.style.padding = "0"
iframe.style.zIndex = "9999"  # ensures it's on top

# Load DuckDuckGo
iframe.src = "https://duckduckgo.com"

# Optional: function to navigate to any URL
def go_to(url: str):
    iframe.src = url
