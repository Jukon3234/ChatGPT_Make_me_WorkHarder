from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Homepage.ui_BattleSetting import Ui_BattleSetting
from PyQt5.QtCore import pyqtSignal,Qt,pyqtSlot
from ctypes import windll, byref
from win32gui import *
from Function.Action import FCAction
import win32gui
import os
import Function.Foundation as Fun




class BattleSettingPageWindow(QWidget,Ui_BattleSetting):

    def __init__(self,parent=None):
        super(BattleSettingPageWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.ButtonDef()

    #接收訊號臨時更改細項
    def handleSignal(self,value):
        if value:
            self.Init()
        else:
            self.Clean_All_Item()
            self.Init()
            
    def ButtonDef(self):
        self.BS_OK_BT.clicked.connect(self.showDialog)
        self.BS_Cancel_BT.clicked.connect(self.showDialog)

    def showDialog(self):        
        sender = self.sender()
        if sender == self.BS_OK_BT:
            self.close()
        elif sender == self.BS_Cancel_BT:
            self.close()

    def Init(self):
        #checkBox
        self.C1_Skill1_CB.setChecked(Fun.C1_Skill1_CB)
        self.C1_Skill2_CB.setChecked(Fun.C1_Skill2_CB)
        self.C1_Skill3_CB.setChecked(Fun.C1_Skill3_CB)
        self.C1_Skill4_CB.setChecked(Fun.C1_Skill4_CB)
        self.C2_Skill1_CB.setChecked(Fun.C2_Skill1_CB)
        self.C2_Skill2_CB.setChecked(Fun.C2_Skill2_CB)
        self.C2_Skill3_CB.setChecked(Fun.C2_Skill3_CB)
        self.C2_Skill4_CB.setChecked(Fun.C2_Skill4_CB)
        self.C3_Skill1_CB.setChecked(Fun.C3_Skill1_CB)
        self.C3_Skill2_CB.setChecked(Fun.C3_Skill2_CB)
        self.C3_Skill3_CB.setChecked(Fun.C3_Skill3_CB)
        self.C3_Skill4_CB.setChecked(Fun.C3_Skill4_CB)
        self.C4_Skill1_CB.setChecked(Fun.C4_Skill1_CB)
        self.C4_Skill2_CB.setChecked(Fun.C4_Skill2_CB)
        self.C4_Skill3_CB.setChecked(Fun.C4_Skill3_CB)
        self.C4_Skill4_CB.setChecked(Fun.C4_Skill4_CB)
        #施放腳色
        self.C1_Skill1_CoB.setCurrentIndex(Fun.C1_Skill1_CoB)
        self.C1_Skill2_CoB.setCurrentIndex(Fun.C1_Skill2_CoB)
        self.C1_Skill3_CoB.setCurrentIndex(Fun.C1_Skill3_CoB)
        self.C1_Skill4_CoB.setCurrentIndex(Fun.C1_Skill4_CoB)
        self.C2_Skill1_CoB.setCurrentIndex(Fun.C2_Skill1_CoB)
        self.C2_Skill2_CoB.setCurrentIndex(Fun.C2_Skill2_CoB)
        self.C2_Skill3_CoB.setCurrentIndex(Fun.C2_Skill3_CoB)
        self.C2_Skill4_CoB.setCurrentIndex(Fun.C2_Skill4_CoB)
        self.C3_Skill1_CoB.setCurrentIndex(Fun.C3_Skill1_CoB)
        self.C3_Skill2_CoB.setCurrentIndex(Fun.C3_Skill2_CoB)
        self.C3_Skill3_CoB.setCurrentIndex(Fun.C3_Skill3_CoB)
        self.C3_Skill4_CoB.setCurrentIndex(Fun.C3_Skill4_CoB)
        self.C4_Skill1_CoB.setCurrentIndex(Fun.C4_Skill1_CoB)
        self.C4_Skill2_CoB.setCurrentIndex(Fun.C4_Skill2_CoB)
        self.C4_Skill3_CoB.setCurrentIndex(Fun.C4_Skill3_CoB)
        self.C4_Skill4_CoB.setCurrentIndex(Fun.C4_Skill4_CoB)
        #順序
        self.C1_Skill1_SB.setValue(Fun.C1_Skill1_SB)
        self.C1_Skill2_SB.setValue(Fun.C1_Skill2_SB)
        self.C1_Skill3_SB.setValue(Fun.C1_Skill3_SB)
        self.C1_Skill4_SB.setValue(Fun.C1_Skill4_SB)
        self.C2_Skill1_SB.setValue(Fun.C2_Skill1_SB)
        self.C2_Skill2_SB.setValue(Fun.C2_Skill2_SB)
        self.C2_Skill3_SB.setValue(Fun.C2_Skill3_SB)
        self.C2_Skill4_SB.setValue(Fun.C2_Skill4_SB)
        self.C3_Skill1_SB.setValue(Fun.C3_Skill1_SB)
        self.C3_Skill2_SB.setValue(Fun.C3_Skill2_SB)
        self.C3_Skill3_SB.setValue(Fun.C3_Skill3_SB)
        self.C3_Skill4_SB.setValue(Fun.C3_Skill4_SB)
        self.C4_Skill1_SB.setValue(Fun.C4_Skill1_SB)
        self.C4_Skill2_SB.setValue(Fun.C4_Skill2_SB)
        self.C4_Skill3_SB.setValue(Fun.C4_Skill3_SB)
        self.C4_Skill4_SB.setValue(Fun.C4_Skill4_SB)
        #召喚石啟用
        self.SommonEn.setChecked(Fun.SommonEn)
        self.SommonCB.setCurrentIndex(Fun.Sommon1)
        self.SommonCB_2.setCurrentIndex(Fun.Sommon2)
        self.Table_Text.setText(str(Fun.Currenttable))
        

    def Clean_All_Item(self):
        print("Clean")
        #checkBox
        Fun.C1_Skill1_CB = False
        Fun.C1_Skill2_CB = False
        Fun.C1_Skill3_CB = False
        Fun.C1_Skill4_CB = False
        Fun.C2_Skill1_CB = False
        Fun.C2_Skill2_CB = False
        Fun.C2_Skill3_CB = False
        Fun.C2_Skill4_CB = False
        Fun.C3_Skill1_CB = False
        Fun.C3_Skill2_CB = False
        Fun.C3_Skill3_CB = False
        Fun.C3_Skill4_CB = False
        Fun.C4_Skill1_CB = False
        Fun.C4_Skill2_CB = False
        Fun.C4_Skill3_CB = False
        Fun.C4_Skill4_CB = False
        #施放腳色
        Fun.C1_Skill1_CoB = 0
        Fun.C1_Skill2_CoB = 0
        Fun.C1_Skill3_CoB = 0
        Fun.C1_Skill4_CoB = 0
        Fun.C2_Skill1_CoB = 0
        Fun.C2_Skill2_CoB = 0
        Fun.C2_Skill3_CoB = 0
        Fun.C2_Skill4_CoB = 0
        Fun.C3_Skill1_CoB = 0
        Fun.C3_Skill2_CoB = 0
        Fun.C3_Skill3_CoB = 0
        Fun.C3_Skill4_CoB = 0
        Fun.C4_Skill1_CoB = 0
        Fun.C4_Skill2_CoB = 0
        Fun.C4_Skill3_CoB = 0
        Fun.C4_Skill4_CoB = 0
        #順序
        Fun.C1_Skill1_SB = 0
        Fun.C1_Skill2_SB = 0
        Fun.C1_Skill3_SB = 0
        Fun.C1_Skill4_SB = 0
        Fun.C2_Skill1_SB = 0
        Fun.C2_Skill2_SB = 0
        Fun.C2_Skill3_SB = 0
        Fun.C2_Skill4_SB = 0
        Fun.C3_Skill1_SB = 0
        Fun.C3_Skill2_SB = 0
        Fun.C3_Skill3_SB = 0
        Fun.C3_Skill4_SB = 0
        Fun.C4_Skill1_SB = 0
        Fun.C4_Skill2_SB = 0
        Fun.C4_Skill3_SB = 0
        Fun.C4_Skill4_SB = 0
        #召喚石啟用
        Fun.SommonEn = False
        Fun.Sommon1 = 0
        Fun.Sommon2 = 0


    def SetupSet(self):
        #偏移延遲紀錄給全域變數
        x = FCAction()
        Fun.RandomX = self.RandomXSpin.value()
        Fun.NRandomX = self.setobset(Fun.RandomX)
        Fun.RandomY = self.RandomYSpin.value()
        Fun.NRandomY = self.setobset(Fun.RandomY)
        Fun.stepdelayRandom = self.stepdelayran.value()
        Fun.NstepdelayRandom = self.setobset(Fun.stepdelayRandom)
        Fun.RounddelayRandom = self.Rounddelayran.value()
        Fun.NRounddelayRandom = self.setobset(Fun.RounddelayRandom)
        Fun.CurmoveTimeRandom = self.CurMoveTimeRan.value()
        Fun.NCurmoveTimeRandom = self.setobset(Fun.CurmoveTimeRandom)
        Fun.StepDelay = self.stepspinBox.value()
        Fun.RoundDelay = self.RoundspinBox.value()
        Fun.CurmoveTime = self.CurMoveTime.value()        
        Fun.DCBOT_Token = self.DC_TOKEN.text()
        Fun.DCBOT_ChannalID = self.DC_CHID.text()        
        x.SaveChange()

    
