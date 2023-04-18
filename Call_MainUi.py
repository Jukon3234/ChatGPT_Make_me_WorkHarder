from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Homepage.ui_MainUI import Ui_GBF_MAIN
from Homepage.ui_temp import Ui_Data
from PyQt5.QtCore import pyqtSignal,Qt
from PyQt5.QtGui import QPixmap
import systemdata.icon.ICON

from ctypes import windll, byref
from ctypes.wintypes import HWND, POINT
import time
import sys
import win32gui
import os
import pyautogui as pag

StopFuntion = False
FightCount = "0"
IntFightCount = 0
fcset=("不設限")
RunFlag = False
TypeSelect = 0

class MainPageWindow(QtWidgets.QMainWindow,Ui_GBF_MAIN):
    
    chooseSignal = pyqtSignal(str)    

    def __init__(self,parent=None):
        super(MainPageWindow, self).__init__(parent)        
        self.setupUi(self)
        #self.init_data()
        self.initUiindex()
        self.initbuttonUI()
        self.change_Page1()#預設為page1
        self.AppDataCheck()

    def init_data(self):
        #self.DataWidget.hide()
        HWNS = win32gui.FindWindow(None, "Qt Designer")
        left, top, right, bottom = win32gui.GetWindowRect(HWNS)
        
        ScreenLeft = str(left)
        ScreenTop = str(top)
        ScreenRight =str(right)
        ScreenBottom = str(bottom)        
        StopFuntion = str(0)
        FightCount =str(0)
        RunFlag = str(0)
        TypeSelect =str(0)
        self.DataWidget.setItem(0,0,QTableWidgetItem(ScreenLeft))    #AppPos
        self.DataWidget.setItem(0,1,QTableWidgetItem(ScreenTop))    #AppPos
        self.DataWidget.setItem(0,2,QTableWidgetItem(ScreenRight))    #AppPos
        self.DataWidget.setItem(0,3,QTableWidgetItem(ScreenBottom))    #AppPos
        self.DataWidget.setItem(1,0,QTableWidgetItem(StopFuntion))    #StopFuntion = 0
        self.DataWidget.setItem(2,0,QTableWidgetItem(FightCount))    #FightCount = 0
        self.DataWidget.setItem(3,0,QTableWidgetItem(RunFlag))    #RunFlag = 0
        self.DataWidget.setItem(4,0,QTableWidgetItem(TypeSelect))    #TypeSelect = 0
        print("AppPos:L: " + ScreenLeft +",T: "+ ScreenTop +",R: " + ScreenRight +",B: "+ ScreenBottom)   
        print("StopFuntion: ", StopFuntion)
        print("FightCount: ", FightCount)
        print("TypeSelect: ", TypeSelect)
        print("RunFlag: ", RunFlag)

    def initUiindex(self):
        titleicon = QtGui.QIcon()
        titleicon.addPixmap(QtGui.QPixmap(":/ICON.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Helpicon = QtGui.QIcon()
        Saveicon = QtGui.QIcon()
        Loadicon = QtGui.QIcon()
        Exiticon = QtGui.QIcon()
        self.setWindowIcon(titleicon)
        self.setWindowTitle('自動人 我的超人')#title
        Helpicon.addPixmap(QtGui.QPixmap(":/Heip.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionHelp.setIcon(Helpicon)#help
        Saveicon.addPixmap(QtGui.QPixmap(":/Save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionAdd.setIcon(Saveicon)#help
        Loadicon.addPixmap(QtGui.QPixmap(":/Load.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionOpen.setIcon(Loadicon)#help
        Exiticon.addPixmap(QtGui.QPixmap(":/door.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionEXIT.setIcon(Exiticon)#help



    def initbuttonUI(self):
        self.actionHelp.triggered.connect(self.showDialog)
        self.Funtionlist.clicked.connect(self.showDialog)
        self.DebugButton.clicked.connect(self.showDialog)
        #self.changebutton.clicked.connect(self.showDialog)
    
    def showDialog(self):
        sender = self.sender()
        if sender == self.actionHelp:
            self.chooseSignal.emit('Help')        
        if  sender == self.Funtionlist:
            text = self.Funtionlist.currentItem().text()
            if text == "轉世":
                self.Info_broswer.setText("轉世")
                self.change_Page1()
            if text == "方陣":
                self.Info_broswer.setText("方陣")
                self.change_Page2()
            if text == "方陣速刷":
                self.Info_broswer.setText("方陣速刷")
                self.change_Page3()
        if sender == self.DebugButton:           
            self.AppDataCheck()

    def change_Page1(self):
        #horizontalLayout_7.replaceWidget(self.groupBox_2,self.groupBox_7,self.groupBox_16)
        self.Page1.show() 
        self.Page2.hide()
        self.Page3.hide()

    def change_Page2(self):
        #horizontalLayout_7.replaceWidget(self.groupBox_2,self.groupBox_7,self.groupBox_16)
        self.Page1.hide()
        self.Page2.show() 
        self.Page3.hide()

    def change_Page3(self):
        #horizontalLayout_7.replaceWidget(self.groupBox_2,self.groupBox_7,self.groupBox_16)
        self.Page1.hide()
        self.Page2.hide() 
        self.Page3.show()

    def AppDataCheck(self):        
        #ScreenLeft = self.DataWidget.item(0,0).text()
        #ScreenTop= self.DataWidget.item(0,1).text()
        #ScreenRight= self.DataWidget.item(0,2).text()
        #ScreenBottom= self.DataWidget.item(0,3).text()
        #StopFuntion = self.DataWidget.item(1,0).text()
        #FightCount = self.DataWidget.item(2,0).text()
        #TypeSelect = self.DataWidget.item(3,0).text()
        #RunFlag = self.DataWidget.item(4,0).text()
        #debug_TXT=(f" L:"+ ScreenLeft +" ,T:"+ ScreenTop +" ,R:"+ ScreenRight +" ,B:" + ScreenBottom +" ,stopF:" + StopFuntion + " ,fightC:" + FightCount + " ,TypeS:" + TypeSelect + " ,RunF:" + RunFlag)
        #self.Info_broswer.setText(debug_TXT)
        HWNS = win32gui.FindWindow(None, "グランブルーファンタジー - Google Chrome")
        left, top, right, bottom = win32gui.GetWindowRect(HWNS)
        posStr1 = str(left).rjust(4)+','+str(top).rjust(4)+','+str(right).rjust(4)+','+str(bottom).rjust(4)

        print("AppPos: ", posStr1)     
        print("StopFuntion: ", StopFuntion)
        print("FightCount: ", FightCount)
        print("IntFightCount: ", IntFightCount)
        print("TypeSelect: ", TypeSelect)
        print("RunFlag: ", RunFlag)     

       


    
