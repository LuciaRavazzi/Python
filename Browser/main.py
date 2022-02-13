# https://www.youtube.com/watch?v=z-5bZ8EoKu4

# The purpose is to create a web browser and embed a google page.

import sys

from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget((self.browser))
        # max size.
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # it helps to return to the previous page.
        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://google.com"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))


app = QApplication(sys.argv)
QApplication.setApplicationName("My cool browser")
window = MainWindow()
app.exec_()
