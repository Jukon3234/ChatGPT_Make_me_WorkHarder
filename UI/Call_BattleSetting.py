from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Homepage.ui_BattleSetting import Ui_BattleSetting
from PyQt5.QtCore import pyqtSignal,Qt
from ctypes import windll, byref
from win32gui import *
from Function.Action import FCAction
import win32gui
import os
import Function.Foundation as Fun




class BattleSettingPageWindow(QWidget,Ui_BattleSetting):
    
    returnSignal = pyqtSignal()

    def __init__(self,parent=None):
        super(BattleSettingPageWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.Init()
        self.ButtonDef()
            
    def ButtonDef(self):
        self.BS_OK_BT.clicked.connect(self.showDialog)
        self.BS_Cancel_BT.clicked.connect(self.showDialog)

    def showDialog(self):        
        sender = self.sender()

        if sender == self.BS_OK_BT:
            self.Init()
            self.close()
        elif sender == self.BS_Cancel_BT:
            self.close()

    def Init(self):
        print(Fun.Currenttable)
        self.Table_Text.setText(str(Fun.Currenttable))

    def Clean_All_Item(self):
        print("Clean")
