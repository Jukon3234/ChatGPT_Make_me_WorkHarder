from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Homepage.ui_temp import Ui_Data
from PyQt5.QtCore import pyqtSignal,Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile


class WebPageWindow(QWidget,Ui_Data):
    def __init__(self,parent=None):
        super(WebPageWindow, self).__init__(parent)
        self.setupUi(self)
        profile = QWebEngineProfile.defaultProfile()
        profile.setHttpCacheMaximumSize(0) # 禁用 Cookie，避免跨站 Cookie 的問題
        self.web = QWebEngineView(self.frame)
        self.web.setGeometry(QtCore.QRect(0, 0, 800, 600)) # 設置小部件的大小和位置
        self.web.load(QUrl('https://www.google.com.tw/')) # 載入網頁