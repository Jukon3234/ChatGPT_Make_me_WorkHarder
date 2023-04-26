from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Homepage.ui_Broswers import Ui_GBFBroswers
from UI.Call_Help import HelpPageWindow
from UI.Call_Setting import SettingPageWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal,Qt,QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineHistory
import systemdata.icon.ICON
import Function.Foundation as Fun

class WebPageWindow(QtWidgets.QMainWindow,Ui_GBFBroswers):

    def __init__(self,parent=None):
        super(WebPageWindow, self).__init__(parent)        
        self.setupUi(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/unnamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)
        self.setWindowTitle('GBF Broswers')
        self.resize(480, 840)
        self.WEBBrowser()
        self.WebButton()

        self.CallsettingUi = SettingPageWindow()
        self.CallHelpUi = HelpPageWindow()

        self.CallsettingUi.returnSignal.connect(self.showDialog)

    def WEBBrowser(self):
        self.web = QWebEngineView(self.WebBroswerFrame)        
        self.web.setGeometry(QtCore.QRect(0, 0, 500, 770)) # 設置小部件的大小和位置
        self.web.load(QUrl('https://game.granbluefantasy.jp/#top'))
        Fun.profile = QWebEngineProfile.defaultProfile()
    
    def WebButton(self):
        self.Back.clicked.connect(self.BackURL)
        self.Reload.clicked.connect(self.ReloadURL)
        self.Enter.clicked.connect(self.EnterURL)
        self.web.urlChanged.connect(self.UpdateUrl)
        self.actionHelp.triggered.connect(self.showDialog)
        self.actionsetting.triggered.connect(self.showDialog)



    def closeEvent(self, event):
        self.CallHelpUi.close()


    def showDialog(self,msg):
        sender = self.sender()
        if sender == self.actionHelp:
            self.CallHelpUi.show()                       
        elif sender == self.actionsetting:
            self.CallsettingUi.show()
        elif msg == 'ChangeSize':
            self.resize(480, 840)

    def UpdateUrl(self,url):
        sender = self.sender()
        self.WEBLineEdit.setText(url.toString())
        Fun.HTML_Text = url.toString()
        
    def BackURL(self):
        self.web.back()

    def ReloadURL(self,url):
        self.web.load(QUrl(Fun.HTML_Text))
        self.WEBLineEdit.setText(Fun.HTML_Text)

    def EnterURL(self,url):
        url = self.WEBLineEdit.text()
        self.web.load(QUrl(url))
        Fun.HTML_Text = url

    def CleanCatch(self):
        profile = self.web.page().profile()
        profile.clearAllVisitedLinks()
        
            