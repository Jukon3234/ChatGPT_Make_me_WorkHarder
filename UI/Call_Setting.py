from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Homepage.ui_Setting import Ui_Setting
from PyQt5.QtCore import pyqtSignal,Qt
import Function.Foundation as Fun


class SettingPageWindow(QWidget,Ui_Setting):
    
    returnSignal = pyqtSignal()

    def __init__(self,parent=None):
        super(SettingPageWindow, self).__init__(parent)
        self.setupUi(self)
        self.Init()
        self.ButtonSetup()

        self.groupBox.toggled.connect(self.showDialog)

    def showDialog(self):
        sender = self.sender()
        if sender == self.groupBox:
            self.ButtonSetup()
    

    def Init(self):        
        Fun.DCBOT_Token = self.DC_TOKEN.text()
        Fun.DCBOT_ChannalID = self.DC_CHID.text()
        print(Fun.DCBOT_Token)
        print(Fun.DCBOT_ChannalID)
    
    def ButtonSetup(self):
        if self.groupBox.isChecked() == False:
            Fun.DCBOT_EN = False
        else:
            Fun.DCBOT_EN = True
