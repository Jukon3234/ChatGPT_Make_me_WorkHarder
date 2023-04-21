from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Homepage.ui_MainUI import Ui_GBF_MAIN
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
import systemdata.icon.ICON
from Function.Page1Function import RunFunction
from Function.DebugFunction import Debugfunction
from Function.Position import GBFPosition
import Function.Foundation
import json

from win32gui import *

from ctypes import windll, byref
from ctypes.wintypes import HWND, POINT
import time
import sys
import win32gui
import os
import pyautogui as pag

class MainPageWindow(QtWidgets.QMainWindow,Ui_GBF_MAIN):
    
    chooseSignal = pyqtSignal(str)    

    def __init__(self,parent=None):#起始位置
        super(MainPageWindow, self).__init__(parent)        
        self.setupUi(self)
        self.initUiindex()
        self.initbuttonUI()
        self.default()
        self.GetScreenFunc()

    def initUiindex(self):#UI框架基礎設定
        titleicon = QtGui.QIcon()
        titleicon.addPixmap(QtGui.QPixmap(":/ICON.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Helpicon = QtGui.QIcon()
        Icon_sort30 = QtGui.QIcon()#轉世
        Icon_sort25 = QtGui.QIcon()#天司
        Icon_sort8 = QtGui.QIcon()#方陣
        Icon_sort7 = QtGui.QIcon()#方陣2.0
        Icon_sort21 = QtGui.QIcon()#十天眾
        self.setWindowIcon(titleicon)
        self.setWindowTitle('自動人 我的超人 V0.0.1')#title
        Helpicon.addPixmap(QtGui.QPixmap(":/Heip.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Icon_sort30.addPixmap(QtGui.QPixmap(":/icon_sort_wepon_30.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Icon_sort25.addPixmap(QtGui.QPixmap(":/icon_sort_wepon_25.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Icon_sort8.addPixmap(QtGui.QPixmap(":/icon_sort_wepon_08.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Icon_sort7.addPixmap(QtGui.QPixmap(":/icon_sort_wepon_07.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Icon_sort21.addPixmap(QtGui.QPixmap(":/icon_sort_wepon_21.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        
        #set icon
        self.actionHelp.setIcon(Helpicon)#help
        for i in range(0, 8):
            item = self.Funtionlist.item(i)
            if i == 0:#轉世
                item.setIcon(Icon_sort30)
            elif i == 1:#1T轉世
                item.setIcon(Icon_sort30)
            elif i == 2:#方陣
                item.setIcon(Icon_sort8)    
            elif i == 3:#方陣速刷
                item.setIcon(Icon_sort8)
            elif i == 4:#1T天使關
                item.setIcon(Icon_sort25)
            elif i == 5:#十天眾天使關
                item.setIcon(Icon_sort21)
            elif i == 6:#古戰場
                item.setIcon(Icon_sort21)
            elif i == 7:#1T古戰場
                item.setIcon(Icon_sort21)


    def initbuttonUI(self):#按鈕設定
        self.actionHelp.triggered.connect(self.showDialog)
        self.Funtionlist.clicked.connect(self.showDialog)
        self.DebugButton.clicked.connect(self.showDialog)
        self.Screptrun_2.clicked.connect(self.showDialog)
        self.FuncStopButton.clicked.connect(self.showDialog)
        self.AllstopButton.clicked.connect(self.showDialog)
        self.SetButton_2.clicked.connect(self.showDialog)
        self.Times_spinBox_2.valueChanged.connect(self.showDialog)
        self.WindowsComboBox.currentIndexChanged.connect(self.showDialog)
        self.PositionButton.clicked.connect(self.showDialog)
        #self.changebutton.clicked.connect(self.showDialog)
    
    def showDialog(self):#按鈕function
        sender = self.sender()
        if sender == self.actionHelp:
            self.chooseSignal.emit('Help')        
        elif  sender == self.Funtionlist:
            self.change_Page()
        elif sender == self.DebugButton:           
            self.SetScreenfuntion()
            x=Debugfunction()
            x.debugLog()
        elif sender == self.Screptrun_2:
            self.Info_broswer.setText("腳本執行中")
            x=RunFunction()
            x.RunFGscrept()
        elif sender == self.FuncStopButton or sender == self.AllstopButton:
            Function.Foundation.StopFunction = True
            self.Info_broswer.clear()
        elif sender == self.SetButton_2:
            self.SaveFile()
        elif sender == self.Times_spinBox_2:            
            self.settingtext()
        elif sender == self.WindowsComboBox:            
            self.SetScreenfuntion()
        elif sender == self.PositionButton:
            x=GBFPosition()
            x.postion()
            
        

    def default(self):#框架預設
        SaveFile = open('systemdata/datasave/data.json')
        savedata= json.load(SaveFile)
        self.Times_spinBox_2.setValue(savedata['function1']['FightCount'])
        self.Times_spinBox_3.setValue(savedata['function2']['FightCount'])
        self.Times_spinBox_5.setValue(savedata['function3']['FightCount'])
        self.Page1.show() 
        self.Page2.hide()
        self.Page3.hide()

    def change_Page(self):
        text = self.Funtionlist.currentItem().text()
        self.Page1.hide()
        self.Page2.hide()
        self.Page3.hide()
        if text == "轉世":
            self.Page1.show()
        if text == "古戰場":            
            self.Page2.show()
        if text == "方陣速刷":
            self.Page3.show()


    def settingtext(self):
        Function.Foundation.Function1FightCount = self.Times_spinBox_2.value()
        if Function.Foundation.Function1FightCount == 0:
            self.label_10.setText("Set 無上限")
        else:
            self.label_10.setText("Set :"+str(Function.Foundation.Function1FightCount))

    def SaveFile(self):
        
        Function.Foundation.Function1FightCount = self.Times_spinBox_2.value()
        Function.Foundation.Function2FightCount = self.Times_spinBox_3.value()
        Function.Foundation.Function3FightCount = self.Times_spinBox_5.value()
        Savedata = {}
        Savedata['function1'] = {'FightCount': Function.Foundation.Function1FightCount, 'TypeSelect': 0}
        Savedata['function2'] = {'FightCount': Function.Foundation.Function2FightCount, 'TypeSelect': 0}
        Savedata['function3'] = {'FightCount': Function.Foundation.Function3FightCount, 'TypeSelect': 0}

        with open('systemdata/datasave/data.json', 'w') as datafile:
            json.dump(Savedata,datafile)
        self.label_10.setText("set成功")
        print("set成功")

    

    def SetScreenfuntion(self):       
        try:
            windowsgetIndex = self.WindowsComboBox.currentIndex()
            windowsgetstr = self.WindowsComboBox.currentText()
            Function.Foundation.WindowsHandle = win32gui.FindWindow(None, windowsgetstr)
            left, top, right, bottom = win32gui.GetWindowRect(Function.Foundation.WindowsHandle)
            posStr1 = str(left).rjust(4)+','+str(top).rjust(4)+','+str(right).rjust(4)+','+str(bottom).rjust(4)
            print("AppPos: ", posStr1)
        except:
            def Mbox(title, text, style):
                return windll.user32.MessageBoxW(0, text, title, style)
            Mbox('沒有找到視窗', '請選擇GBF的視窗標題', 0)        


    def GetScreenFunc(self):
        titles = set()
        def foo(hwnd,mouse):
            if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
                titles.add(GetWindowText(hwnd))
        EnumWindows(foo, 0)
        lt = [t for t in titles if t]
        lt.sort()
        print("#Sortting Windows-------------")
        for t in lt:
            if t == "グランブルーファンタジー - Google Chrome":
                self.WindowsComboBox.addItem(t)
                self.WindowsComboBox.setCurrentText(t)
            else:
                self.WindowsComboBox.addItem(t)
            print (t)
        try:
            windowsgetstr = self.WindowsComboBox.currentText()
            Function.Foundation.WindowsHandle = win32gui.FindWindow(None, windowsgetstr)
            left, top, right, bottom = win32gui.GetWindowRect(Function.Foundation.WindowsHandle)
        except:
            print("沒有找到視窗")
        

       


    
