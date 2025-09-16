import js

def create_fullscreen_iframe(url="https://duckduckgo.com"):
    # Wait for the document body to exist
    body = js.document.body

    # Check if iframe exists
    iframe_id = "duckduckgo-frame"
    iframe = js.document.getElementById(iframe_id)
    if not iframe:
        # Create iframe
        iframe = js.document.createElement("iframe")
        iframe.id = iframe_id
        body.appendChild(iframe)

    # Style iframe
    iframe.style.position = "fixed"
    iframe.style.top = "0"
    iframe.style.left = "0"
    iframe.style.width = "100vw"
    iframe.style.height = "100vh"
    iframe.style.border = "none"
    iframe.style.margin = "0"
    iframe.style.padding = "0"
    iframe.style.zIndex = "9999"

    # Set the URL
    iframe.src = url

# Run the function
create_fullscreen_iframe()
