from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Homepage.ui_SettingForm import Ui_SettingForm
from PyQt5.QtCore import pyqtSignal,Qt
import Function.Foundation as Fun


class SettingPageWindow(QWidget,Ui_SettingForm):
    
    returnSignal = pyqtSignal(str)

    def __init__(self,parent=None):
        super(SettingPageWindow, self).__init__(parent)
        self.setupUi(self)

        self.ScreenWH.clicked.connect(self.showDialog)
        cache_size = Fun.profile
        self.CatchBrowser.setText(str(cache_size))

    def showDialog(self):
        sender = self.sender()
        if sender == self.ScreenWH:
            self.returnSignal.emit('ChangeSize') 
    
    