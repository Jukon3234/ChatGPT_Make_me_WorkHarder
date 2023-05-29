from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Homepage.ui_Setting import Ui_Setting
from PyQt5.QtCore import pyqtSignal,Qt
import Function.Foundation as Fun
import json
import os


class SettingPageWindow(QWidget,Ui_Setting):
    
    returnSignal = pyqtSignal()

    def __init__(self,parent=None):
        super(SettingPageWindow, self).__init__(parent)
        self.setupUi(self)
        self.Init()
        self.ButtonSetup()
        self.groupBox.toggled.connect(self.showDialog)
        self.OKButton.clicked.connect(self.showDialog)
        self.CancelButton.clicked.connect(self.showDialog)

    def showDialog(self):
        sender = self.sender()
        if sender == self.groupBox:
            self.ButtonSetup()
        elif sender == self.OKButton:
            self.SetupSet()
            self.Init()
            self.close()
        elif sender == self.CancelButton:
            self.Init()
            self.close()

    def Init(self):
        if os.path.exists('./systemdata/datasave/data.json'):
            SaveFile = open('systemdata/datasave/data.json')
        else:
            SaveFile = open('systemdata/datasave/Default.json')
        savedata= json.load(SaveFile)
        self.DC_TOKEN.setText(savedata['Bot']['TOKEN'])
        self.DC_CHID.setText(savedata['Bot']['Channal_ID'])
        Fun.DCBOT_EN = savedata['Bot']['Enabled']
        if Fun.DCBOT_EN == True:
            self.groupBox.setChecked(True)
        elif Fun.DCBOT_EN == False:
            self.groupBox.setChecked(False)
    
    def SetupSet(self):
        Fun.DCBOT_Token = self.DC_TOKEN.text()
        Fun.DCBOT_ChannalID = self.DC_CHID.text()
        Savedata = {}
        Savedata['function'] = {'FightCount': Fun.Function1FightCount, 'TypeSelect': 0}
        Savedata['Bot'] = {'TOKEN': Fun.DCBOT_Token,'Channal_ID': Fun.DCBOT_ChannalID,'Enabled' : Fun.DCBOT_EN}
        with open('systemdata/datasave/data.json', 'w') as datafile:
            json.dump(Savedata,datafile)
    
    def ButtonSetup(self):
        if self.groupBox.isChecked() == False:
            Fun.DCBOT_EN = False
        else:
            Fun.DCBOT_EN = True    
