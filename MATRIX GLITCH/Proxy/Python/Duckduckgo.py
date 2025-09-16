import js

# Function to open DuckDuckGo in a new tab/window
def open_duckduckgo():
    # "_blank" opens a new tab
    js.window.open("https://duckduckgo.com", "_blank")

# Call the function
open_duckduckgo()
