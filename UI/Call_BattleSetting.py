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
    chooseSignal2 = pyqtSignal()

    def __init__(self,parent=None):
        super(BattleSettingPageWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.ButtonDef()

    #接收訊號臨時更改細項
    def handleSignal(self):
        self.Init()
            
    def ButtonDef(self):
        self.BS_OK_BT.clicked.connect(self.showDialog)
        self.BS_Cancel_BT.clicked.connect(self.showDialog)

    def showDialog(self):        
        sender = self.sender()
        if sender == self.BS_OK_BT:
            self.SetupSet()
            self.chooseSignal2.emit()
            self.close()
        elif sender == self.BS_Cancel_BT:
            self.close()

    def Init(self):
        #checkBox
        self.C1_Skill1_CB.setChecked(Fun.TrueList[0])
        self.C1_Skill2_CB.setChecked(Fun.TrueList[1])
        self.C1_Skill3_CB.setChecked(Fun.TrueList[2])
        self.C1_Skill4_CB.setChecked(Fun.TrueList[3])
        self.C2_Skill1_CB.setChecked(Fun.TrueList[4])
        self.C2_Skill2_CB.setChecked(Fun.TrueList[5])
        self.C2_Skill3_CB.setChecked(Fun.TrueList[6])
        self.C2_Skill4_CB.setChecked(Fun.TrueList[7])
        self.C3_Skill1_CB.setChecked(Fun.TrueList[8])
        self.C3_Skill2_CB.setChecked(Fun.TrueList[9])
        self.C3_Skill3_CB.setChecked(Fun.TrueList[10])
        self.C3_Skill4_CB.setChecked(Fun.TrueList[11])
        self.C4_Skill1_CB.setChecked(Fun.TrueList[12])
        self.C4_Skill2_CB.setChecked(Fun.TrueList[13])
        self.C4_Skill3_CB.setChecked(Fun.TrueList[14])
        self.C4_Skill4_CB.setChecked(Fun.TrueList[15])
        #施放腳色
        self.C1_Skill1_CoB.setCurrentIndex(Fun.Skill_Set[0])
        self.C1_Skill2_CoB.setCurrentIndex(Fun.Skill_Set[1])
        self.C1_Skill3_CoB.setCurrentIndex(Fun.Skill_Set[2])
        self.C1_Skill4_CoB.setCurrentIndex(Fun.Skill_Set[3])
        self.C2_Skill1_CoB.setCurrentIndex(Fun.Skill_Set[4])
        self.C2_Skill2_CoB.setCurrentIndex(Fun.Skill_Set[5])
        self.C2_Skill3_CoB.setCurrentIndex(Fun.Skill_Set[6])
        self.C2_Skill4_CoB.setCurrentIndex(Fun.Skill_Set[7])
        self.C3_Skill1_CoB.setCurrentIndex(Fun.Skill_Set[8])
        self.C3_Skill2_CoB.setCurrentIndex(Fun.Skill_Set[9])
        self.C3_Skill3_CoB.setCurrentIndex(Fun.Skill_Set[10])
        self.C3_Skill4_CoB.setCurrentIndex(Fun.Skill_Set[11])
        self.C4_Skill1_CoB.setCurrentIndex(Fun.Skill_Set[12])
        self.C4_Skill2_CoB.setCurrentIndex(Fun.Skill_Set[13])
        self.C4_Skill3_CoB.setCurrentIndex(Fun.Skill_Set[14])
        self.C4_Skill4_CoB.setCurrentIndex(Fun.Skill_Set[15])
        #順序
        self.C1_Skill1_SB.setValue(Fun.SortList[0])
        self.C1_Skill2_SB.setValue(Fun.SortList[1])
        self.C1_Skill3_SB.setValue(Fun.SortList[2])
        self.C1_Skill4_SB.setValue(Fun.SortList[3])
        self.C2_Skill1_SB.setValue(Fun.SortList[4])
        self.C2_Skill2_SB.setValue(Fun.SortList[5])
        self.C2_Skill3_SB.setValue(Fun.SortList[6])
        self.C2_Skill4_SB.setValue(Fun.SortList[7])
        self.C3_Skill1_SB.setValue(Fun.SortList[8])
        self.C3_Skill2_SB.setValue(Fun.SortList[9])
        self.C3_Skill3_SB.setValue(Fun.SortList[10])
        self.C3_Skill4_SB.setValue(Fun.SortList[11])
        self.C4_Skill1_SB.setValue(Fun.SortList[12])
        self.C4_Skill2_SB.setValue(Fun.SortList[13])
        self.C4_Skill3_SB.setValue(Fun.SortList[14])
        self.C4_Skill4_SB.setValue(Fun.SortList[15])
        #召喚石啟用
        self.SommonEn.setChecked(Fun.SommonEn)
        self.SommonCB.setCurrentIndex(Fun.Sommon1)
        self.SommonCB_2.setCurrentIndex(Fun.Sommon2)
        self.Table_Text.setText(str(Fun.Currenttable))
        

    def Clean_All_Item(self):
        print("Clean")
        #checkBox
        for i in range(16):
            Fun.TrueList[i] = False
            Fun.Skill_Set[i] = 0
            Fun.SortList[i] = 0                
        #召喚石啟用
        Fun.SommonEn = False
        Fun.Sommon1 = 0
        Fun.Sommon2 = 0


    def SetupSet(self):
        #checkBox
        Fun.TrueList[0] = self.C1_Skill1_CB.isChecked()
        Fun.TrueList[1] = self.C1_Skill2_CB.isChecked()
        Fun.TrueList[2] = self.C1_Skill3_CB.isChecked()
        Fun.TrueList[3] = self.C1_Skill4_CB.isChecked()
        Fun.TrueList[4] = self.C2_Skill1_CB.isChecked()
        Fun.TrueList[5] = self.C2_Skill2_CB.isChecked()
        Fun.TrueList[6] = self.C2_Skill3_CB.isChecked()
        Fun.TrueList[7] = self.C2_Skill4_CB.isChecked()
        Fun.TrueList[8] = self.C3_Skill1_CB.isChecked()
        Fun.TrueList[9] = self.C3_Skill2_CB.isChecked()
        Fun.TrueList[10] = self.C3_Skill3_CB.isChecked()
        Fun.TrueList[11] = self.C3_Skill4_CB.isChecked()
        Fun.TrueList[12] = self.C4_Skill1_CB.isChecked()
        Fun.TrueList[13] = self.C4_Skill2_CB.isChecked()
        Fun.TrueList[14] = self.C4_Skill3_CB.isChecked()    
        Fun.TrueList[15] = self.C4_Skill4_CB.isChecked()        
        #施放腳色
        Fun.Skill_Set[0] = self.C1_Skill1_CoB.currentIndex()
        Fun.Skill_Set[1] = self.C1_Skill2_CoB.currentIndex()
        Fun.Skill_Set[2] = self.C1_Skill3_CoB.currentIndex()
        Fun.Skill_Set[3] = self.C1_Skill4_CoB.currentIndex()
        Fun.Skill_Set[4] = self.C2_Skill1_CoB.currentIndex()
        Fun.Skill_Set[5] = self.C2_Skill2_CoB.currentIndex()
        Fun.Skill_Set[6] = self.C2_Skill3_CoB.currentIndex()
        Fun.Skill_Set[7] = self.C2_Skill4_CoB.currentIndex()
        Fun.Skill_Set[8] = self.C3_Skill1_CoB.currentIndex()
        Fun.Skill_Set[9] = self.C3_Skill2_CoB.currentIndex()
        Fun.Skill_Set[10] = self.C3_Skill3_CoB.currentIndex()
        Fun.Skill_Set[11] = self.C3_Skill4_CoB.currentIndex()
        Fun.Skill_Set[12] = self.C4_Skill1_CoB.currentIndex()
        Fun.Skill_Set[13] = self.C4_Skill2_CoB.currentIndex()
        Fun.Skill_Set[14] = self.C4_Skill3_CoB.currentIndex()
        Fun.Skill_Set[15] = self.C4_Skill4_CoB.currentIndex()        
        #紀錄給全域變數 
        Fun.SortList[0] = self.C1_Skill1_SB.value()
        Fun.SortList[1] = self.C1_Skill2_SB.value()
        Fun.SortList[2] = self.C1_Skill3_SB.value()    
        Fun.SortList[3] = self.C1_Skill4_SB.value()
        Fun.SortList[4] = self.C2_Skill1_SB.value()
        Fun.SortList[5] = self.C2_Skill2_SB.value()
        Fun.SortList[6] = self.C2_Skill3_SB.value()
        Fun.SortList[7] = self.C2_Skill4_SB.value()
        Fun.SortList[8] = self.C3_Skill1_SB.value()
        Fun.SortList[9] = self.C3_Skill2_SB.value()
        Fun.SortList[10] = self.C3_Skill3_SB.value()
        Fun.SortList[11] = self.C3_Skill4_SB.value()
        Fun.SortList[12] = self.C4_Skill1_SB.value()
        Fun.SortList[13] = self.C4_Skill2_SB.value()
        Fun.SortList[14] = self.C4_Skill3_SB.value()
        Fun.SortList[15] = self.C4_Skill4_SB.value()
