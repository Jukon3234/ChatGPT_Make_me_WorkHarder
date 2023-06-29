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
        self.Init()
        self.ButtonDef()
            
    def ButtonDef(self):
        #OKBUtton
        self.OKButton.clicked.connect(self.showDialog)
        self.CancelButton.clicked.connect(self.showDialog)

    def showDialog(self):        
        #Button
        if sender == self.OKButton:
            self.SetupSet()
            self.Init()
            self.close()
        elif sender == self.CancelButton:
            self.Init()
            self.close()

    def Init(self):        
        print("Resolve")
