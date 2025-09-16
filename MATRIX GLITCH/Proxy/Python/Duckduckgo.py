import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtWebEngineWidgets import QWebEngineView

class FullScreenBrowser(QMainWindow):
    def __init__(self, url="https://duckduckgo.com"):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.showFullScreen()
        self.browser = QWebEngineView()
        self.browser.setUrl(url)
        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FullScreenBrowser()
    window.show()
    sys.exit(app.exec())
