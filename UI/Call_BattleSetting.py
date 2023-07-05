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
        self.C1_Skill1_CB.setChecked(Fun.TotleTrueList[Fun.Currenttable][0])
        self.C1_Skill2_CB.setChecked(Fun.TotleTrueList[Fun.Currenttable][1])
        self.C1_Skill3_CB.setChecked(Fun.TotleTrueList[Fun.Currenttable][2])
        self.C1_Skill4_CB.setChecked(Fun.TotleTrueList[Fun.Currenttable][3])
        self.C2_Skill1_CB.setChecked(Fun.TotleTrueList[Fun.Currenttable][4])
        self.C2_Skill2_CB.setChecked(Fun.TotleTrueList[Fun.Currenttable][5])
        self.C2_Skill3_CB.setChecked(Fun.TotleTrueList[Fun.Currenttable][6])
        self.C2_Skill4_CB.setChecked(Fun.TotleTrueList[Fun.Currenttable][7])
        self.C3_Skill1_CB.setChecked(Fun.TotleTrueList[Fun.Currenttable][8])
        self.C3_Skill2_CB.setChecked(Fun.TotleTrueList[Fun.Currenttable][9])
        self.C3_Skill3_CB.setChecked(Fun.TotleTrueList[Fun.Currenttable][10])
        self.C3_Skill4_CB.setChecked(Fun.TotleTrueList[Fun.Currenttable][11])
        self.C4_Skill1_CB.setChecked(Fun.TotleTrueList[Fun.Currenttable][12])
        self.C4_Skill2_CB.setChecked(Fun.TotleTrueList[Fun.Currenttable][13])
        self.C4_Skill3_CB.setChecked(Fun.TotleTrueList[Fun.Currenttable][14])
        self.C4_Skill4_CB.setChecked(Fun.TotleTrueList[Fun.Currenttable][15])
        print(Fun.TotleTrueList)
        #施放腳色
        self.C1_Skill1_CoB.setCurrentIndex(Fun.TotleSkillSet[Fun.Currenttable][0])
        self.C1_Skill2_CoB.setCurrentIndex(Fun.TotleSkillSet[Fun.Currenttable][1])
        self.C1_Skill3_CoB.setCurrentIndex(Fun.TotleSkillSet[Fun.Currenttable][2])
        self.C1_Skill4_CoB.setCurrentIndex(Fun.TotleSkillSet[Fun.Currenttable][3])
        self.C2_Skill1_CoB.setCurrentIndex(Fun.TotleSkillSet[Fun.Currenttable][4])
        self.C2_Skill2_CoB.setCurrentIndex(Fun.TotleSkillSet[Fun.Currenttable][5])
        self.C2_Skill3_CoB.setCurrentIndex(Fun.TotleSkillSet[Fun.Currenttable][6])
        self.C2_Skill4_CoB.setCurrentIndex(Fun.TotleSkillSet[Fun.Currenttable][7])
        self.C3_Skill1_CoB.setCurrentIndex(Fun.TotleSkillSet[Fun.Currenttable][8])
        self.C3_Skill2_CoB.setCurrentIndex(Fun.TotleSkillSet[Fun.Currenttable][9])
        self.C3_Skill3_CoB.setCurrentIndex(Fun.TotleSkillSet[Fun.Currenttable][10])
        self.C3_Skill4_CoB.setCurrentIndex(Fun.TotleSkillSet[Fun.Currenttable][11])
        self.C4_Skill1_CoB.setCurrentIndex(Fun.TotleSkillSet[Fun.Currenttable][12])
        self.C4_Skill2_CoB.setCurrentIndex(Fun.TotleSkillSet[Fun.Currenttable][13])
        self.C4_Skill3_CoB.setCurrentIndex(Fun.TotleSkillSet[Fun.Currenttable][14])
        self.C4_Skill4_CoB.setCurrentIndex(Fun.TotleSkillSet[Fun.Currenttable][15])
        print(Fun.TotleSkillSet)
        #順序
        self.C1_Skill1_SB.setValue(Fun.TotleSortList[Fun.Currenttable][0])
        self.C1_Skill2_SB.setValue(Fun.TotleSortList[Fun.Currenttable][1])
        self.C1_Skill3_SB.setValue(Fun.TotleSortList[Fun.Currenttable][2])
        self.C1_Skill4_SB.setValue(Fun.TotleSortList[Fun.Currenttable][3])
        self.C2_Skill1_SB.setValue(Fun.TotleSortList[Fun.Currenttable][4])
        self.C2_Skill2_SB.setValue(Fun.TotleSortList[Fun.Currenttable][5])
        self.C2_Skill3_SB.setValue(Fun.TotleSortList[Fun.Currenttable][6])
        self.C2_Skill4_SB.setValue(Fun.TotleSortList[Fun.Currenttable][7])
        self.C3_Skill1_SB.setValue(Fun.TotleSortList[Fun.Currenttable][8])
        self.C3_Skill2_SB.setValue(Fun.TotleSortList[Fun.Currenttable][9])
        self.C3_Skill3_SB.setValue(Fun.TotleSortList[Fun.Currenttable][10])
        self.C3_Skill4_SB.setValue(Fun.TotleSortList[Fun.Currenttable][11])
        self.C4_Skill1_SB.setValue(Fun.TotleSortList[Fun.Currenttable][12])
        self.C4_Skill2_SB.setValue(Fun.TotleSortList[Fun.Currenttable][13])
        self.C4_Skill3_SB.setValue(Fun.TotleSortList[Fun.Currenttable][14])
        self.C4_Skill4_SB.setValue(Fun.TotleSortList[Fun.Currenttable][15])
        print(Fun.TotleSortList)
        #召喚石啟用
        self.SommonEn.setChecked(Fun.TotleSommonCheck[Fun.Currenttable][0])
        self.SommonCB.setCurrentIndex(Fun.TotleSommon1[Fun.Currenttable][0])
        self.SommonCB_2.setCurrentIndex(Fun.TotleSommon2[Fun.Currenttable][0])
        self.Table_Text.setText(str(Fun.Currenttable))
        print(Fun.TotleSommonCheck)
        print(Fun.TotleSommon1)
        print(Fun.TotleSommon2)
        

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
        Fun.TotleTrueList[Fun.Currenttable][0] = self.C1_Skill1_CB.isChecked()
        Fun.TotleTrueList[Fun.Currenttable][1] = self.C1_Skill2_CB.isChecked()
        Fun.TotleTrueList[Fun.Currenttable][2] = self.C1_Skill3_CB.isChecked()
        Fun.TotleTrueList[Fun.Currenttable][3] = self.C1_Skill4_CB.isChecked()
        Fun.TotleTrueList[Fun.Currenttable][4] = self.C2_Skill1_CB.isChecked()
        Fun.TotleTrueList[Fun.Currenttable][5] = self.C2_Skill2_CB.isChecked()
        Fun.TotleTrueList[Fun.Currenttable][6] = self.C2_Skill3_CB.isChecked()
        Fun.TotleTrueList[Fun.Currenttable][7] = self.C2_Skill4_CB.isChecked()
        Fun.TotleTrueList[Fun.Currenttable][8] = self.C3_Skill1_CB.isChecked()
        Fun.TotleTrueList[Fun.Currenttable][9] = self.C3_Skill2_CB.isChecked()
        Fun.TotleTrueList[Fun.Currenttable][10] = self.C3_Skill3_CB.isChecked()
        Fun.TotleTrueList[Fun.Currenttable][11] = self.C3_Skill4_CB.isChecked()
        Fun.TotleTrueList[Fun.Currenttable][12] = self.C4_Skill1_CB.isChecked()
        Fun.TotleTrueList[Fun.Currenttable][13] = self.C4_Skill2_CB.isChecked()
        Fun.TotleTrueList[Fun.Currenttable][14] = self.C4_Skill3_CB.isChecked()    
        Fun.TotleTrueList[Fun.Currenttable][15] = self.C4_Skill4_CB.isChecked()        
        #施放腳色
        Fun.TotleSkillSet[Fun.Currenttable][0] = self.C1_Skill1_CoB.currentIndex()
        Fun.TotleSkillSet[Fun.Currenttable][1] = self.C1_Skill2_CoB.currentIndex()
        Fun.TotleSkillSet[Fun.Currenttable][2] = self.C1_Skill3_CoB.currentIndex()
        Fun.TotleSkillSet[Fun.Currenttable][3] = self.C1_Skill4_CoB.currentIndex()
        Fun.TotleSkillSet[Fun.Currenttable][4] = self.C2_Skill1_CoB.currentIndex()
        Fun.TotleSkillSet[Fun.Currenttable][5] = self.C2_Skill2_CoB.currentIndex()
        Fun.TotleSkillSet[Fun.Currenttable][6] = self.C2_Skill3_CoB.currentIndex()
        Fun.TotleSkillSet[Fun.Currenttable][7] = self.C2_Skill4_CoB.currentIndex()
        Fun.TotleSkillSet[Fun.Currenttable][8] = self.C3_Skill1_CoB.currentIndex()
        Fun.TotleSkillSet[Fun.Currenttable][9] = self.C3_Skill2_CoB.currentIndex()
        Fun.TotleSkillSet[Fun.Currenttable][10] = self.C3_Skill3_CoB.currentIndex()
        Fun.TotleSkillSet[Fun.Currenttable][11] = self.C3_Skill4_CoB.currentIndex()
        Fun.TotleSkillSet[Fun.Currenttable][12] = self.C4_Skill1_CoB.currentIndex()
        Fun.TotleSkillSet[Fun.Currenttable][13] = self.C4_Skill2_CoB.currentIndex()
        Fun.TotleSkillSet[Fun.Currenttable][14] = self.C4_Skill3_CoB.currentIndex()
        Fun.TotleSkillSet[Fun.Currenttable][15] = self.C4_Skill4_CoB.currentIndex()        
        #紀錄給全域變數 
        Fun.TotleSortList[Fun.Currenttable][0] = self.C1_Skill1_SB.value()
        Fun.TotleSortList[Fun.Currenttable][1] = self.C1_Skill2_SB.value()
        Fun.TotleSortList[Fun.Currenttable][2] = self.C1_Skill3_SB.value()    
        Fun.TotleSortList[Fun.Currenttable][3] = self.C1_Skill4_SB.value()
        Fun.TotleSortList[Fun.Currenttable][4] = self.C2_Skill1_SB.value()
        Fun.TotleSortList[Fun.Currenttable][5] = self.C2_Skill2_SB.value()
        Fun.TotleSortList[Fun.Currenttable][6] = self.C2_Skill3_SB.value()
        Fun.TotleSortList[Fun.Currenttable][7] = self.C2_Skill4_SB.value()
        Fun.TotleSortList[Fun.Currenttable][8] = self.C3_Skill1_SB.value()
        Fun.TotleSortList[Fun.Currenttable][9] = self.C3_Skill2_SB.value()
        Fun.TotleSortList[Fun.Currenttable][10] = self.C3_Skill3_SB.value()
        Fun.TotleSortList[Fun.Currenttable][11] = self.C3_Skill4_SB.value()
        Fun.TotleSortList[Fun.Currenttable][12] = self.C4_Skill1_SB.value()
        Fun.TotleSortList[Fun.Currenttable][13] = self.C4_Skill2_SB.value()
        Fun.TotleSortList[Fun.Currenttable][14] = self.C4_Skill3_SB.value()
        Fun.TotleSortList[Fun.Currenttable][15] = self.C4_Skill4_SB.value()
        #召喚石
        Fun.TotleSommonCheck[Fun.Currenttable] = self.SommonEn.isChecked()
        Fun.TotleSommon1[Fun.Currenttable] = self.SommonCB.currentIndex()
        Fun.TotleSommon2[Fun.Currenttable] = self.SommonCB_2.currentIndex()
