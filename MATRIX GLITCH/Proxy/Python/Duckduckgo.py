import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtWebEngineWidgets import QWebEngineView

class FullScreenBrowser(QMainWindow):
    def __init__(self, url="https://duckduckgo.com"):
        super().__init__()
        self.setWindowTitle("Full-Screen Browser Overlay")
        
        # Full-screen, no title bar
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.showFullScreen()
        
        # Browser engine
        self.browser = QWebEngineView()
        self.browser.setUrl(url)
        self.setCentralWidget(self.browser)
        
        # Disable right-click
        self.browser.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Change the URL to any website you want
    window = FullScreenBrowser("https://duckduckgo.com")
    window.show()
    sys.exit(app.exec())
