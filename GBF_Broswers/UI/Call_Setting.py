from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Homepage.ui_SettingForm import Ui_SettingForm
from PyQt5.QtCore import pyqtSignal,Qt,QUrl
import Function.Foundation as Fun
import os
from PyQt5.QtGui import QDesktopServices
import systemdata.icon.ICON



class SettingPageWindow(QWidget,Ui_SettingForm):
    
    returnSignal = pyqtSignal(str)

    def __init__(self,parent=None):
        super(SettingPageWindow, self).__init__(parent)
        self.setupUi(self)

        WindowIcon = QtGui.QIcon()
        WindowIcon.addPixmap(QtGui.QPixmap(":/tools.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(WindowIcon)
        SettingIcon = QtGui.QIcon()
        SettingIcon.addPixmap(QtGui.QPixmap(":/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)        
        self.Reload.setIcon(SettingIcon)


        self.ScreenWH.clicked.connect(self.showDialog)
        self.ClearCatch.clicked.connect(self.showDialog)
        self.ClearCookie.clicked.connect(self.showDialog)
        self.OpenCatch.clicked.connect(self.showDialog)
        self.Reload.clicked.connect(self.showDialog)

        self.ShowCatch()

        

    def showDialog(self):
        sender = self.sender()
        if sender == self.ScreenWH:
            self.returnSignal.emit('ChangeSize')
        elif sender == self.ClearCatch:
            self.returnSignal.emit('clearcatch')
        elif sender == self.ClearCookie:
            self.returnSignal.emit('clearcookie')
        elif sender == self.OpenCatch:
            try:
                url = QUrl.fromLocalFile(Fun.cache_path)
                QDesktopServices.openUrl(url)
            except:
                print("出錯嘞!")
        elif sender == self.Reload:
            self.ShowCatch()
            

    def ShowCatch(self):
        path = Fun.cache_path
        total_size = 0
        for path, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(path, file)
                total_size += os.path.getsize(file_path)
        total_size_mb = round(total_size / (1024 * 1024),1)
        self.CatchBrowser.setText(str(total_size_mb))
    
    