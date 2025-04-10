
import sys
import time
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Screenshot(QWebEngineView):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self._loaded = False
        self.loadFinished.connect(self._loadFinished)

    def capture(self, url, output_file):
        """Load the URL and capture a screenshot."""
        self.load(QUrl(url))
        self.wait_load()
        # Set viewport size
        self.resize(1024, 768)
        # Render image
        self.grab().save(output_file)
        print(f"Saving screenshot to {output_file}")
        return True

    def wait_load(self, delay=0):
        """Wait until page is loaded."""
        while not self._loaded:
            self.app.processEvents()
            time.sleep(delay)
        self._loaded = False

    def _loadFinished(self, result):
        """Signal handler for loadFinished signal."""
        self._loaded = True
