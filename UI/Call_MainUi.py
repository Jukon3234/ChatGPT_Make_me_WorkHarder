from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Homepage.ui_MainUI import Ui_GBF_MAIN
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
import systemdata.icon.ICON
import systemdata.img.Arcarum.ARCARUM
from Function.Page1Function import RunFunction
from Function.DebugFunction import Debugfunction
from Function.Position import GBFPosition
import Function.Foundation as Fun
import json

from http import cookies
import datetime

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
        self.SetArcarumPIC()

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
            elif i == 1:#舔關
                item.setIcon(Icon_sort8) 
            elif i == 2:#1T天使關
                item.setIcon(Icon_sort25)
            elif i == 3:#十天眾天使關
                item.setIcon(Icon_sort21)
            elif i == 4:#古戰場
                item.setIcon(Icon_sort21)

    def SetArcarumPIC(self):
        PicGetIndex = self.FightcomboBox_2.currentIndex()
        Img_areascene = QtWidgets.QGraphicsScene()
        Img_areascene.setSceneRect(5 , 0, 140, 75)
        Img_areascene2 = QtWidgets.QGraphicsScene()
        Img_areascene2.setSceneRect(0 , 0, 400, 100)
        item_count = self.FightcomboBox_4.count()
        print("item_count",item_count)
        def SetComboBox1():
            print("item_count",item_count)
            if item_count == 0:
                for i in range(1,11):
                    self.FightcomboBox_4.addItem(str(i))
            else:
                for i in range(0,item_count):
                    self.FightcomboBox_4.removeItem(0)
                for j in range(1,11):
                    self.FightcomboBox_4.addItem(str(j))
        
        def SetComboBox2():
            print("item_count",item_count)
            if item_count == 0:
                for i in range(1,8):
                    self.FightcomboBox_4.addItem(str(i))
            else:
                for i in range(0,item_count):
                    self.FightcomboBox_4.removeItem(0)
                for j in range(1,8):
                    self.FightcomboBox_4.addItem(str(j))
        if PicGetIndex == 0:
            img = QtGui.QPixmap(":/area_2_cleared.png")
            img2 = QtGui.QPixmap(":/area2.jpg")
            img2H = 229*0.4
            img2W = 1024*0.4
            SetComboBox1()
        elif PicGetIndex == 1:
            img = QtGui.QPixmap(":/area_3_cleared.png")
            img2 = QtGui.QPixmap(":/area3.jpg")
            img2H = 229*0.4
            img2W = 1024*0.4
            SetComboBox1()
        elif PicGetIndex == 2:
            img = QtGui.QPixmap(":/area_4_cleared.png")
            img2 = QtGui.QPixmap(":/area4.jpg")
            img2H = 229*0.4
            img2W = 1024*0.4
            SetComboBox1()
        elif PicGetIndex == 3:
            img = QtGui.QPixmap(":/area_5_cleared.png")
            img2 = QtGui.QPixmap(":/area5.jpg")
            img2H = 229*0.4
            img2W = 1024*0.4
            SetComboBox1()
        elif PicGetIndex == 4:
            img = QtGui.QPixmap(":/area_6_cleared.png")
            img2 = QtGui.QPixmap(":/area6.jpg")
            img2H = 430*0.25
            img2W = 1280*0.25
            SetComboBox2()
        elif PicGetIndex == 5:
            img = QtGui.QPixmap(":/area_7_cleared.png")
            img2 = QtGui.QPixmap(":/area7.jpg")
            img2H = 430*0.25
            img2W = 1280*0.25
            SetComboBox2()
        elif PicGetIndex == 6:
            img = QtGui.QPixmap(":/area_8_cleared.png")
            img2 = QtGui.QPixmap(":/area8.jpg")
            img2H = 430*0.25
            img2W = 1280*0.25
            SetComboBox2()
        elif PicGetIndex == 7:
            img = QtGui.QPixmap(":/area_9_cleared.png")
            img2 = QtGui.QPixmap(":/area9.jpg")
            img2H = 430*0.25
            img2W = 1280*0.25
            SetComboBox2()
        elif PicGetIndex == 8:
            img = QtGui.QPixmap(":/area_10_cleared.png")
        img = img.scaled(150,80)
        Img_areascene.addPixmap(img)
        self.graphicsView.setScene(Img_areascene)
        img2 = img2.scaled(img2W,img2H)
        Img_areascene2.addPixmap(img2)
        self.graphicsView_2.setScene(Img_areascene2)

        
        

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
        self.FRWidge.clicked.connect(self.showDialog)
        self.FightcomboBox_2.currentIndexChanged.connect(self.showDialog)
    
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
            Fun.StopFunction = True
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
        elif sender == self.FRWidge:
            self.chooseSignal.emit('change')
        elif sender == self.FightcomboBox_2:
            self.SetArcarumPIC()

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
        Fun.Function1FightCount = self.Times_spinBox_2.value()
        if Fun.Function1FightCount == 0:
            self.label_10.setText("Set 無上限")
        else:
            self.label_10.setText("Set :"+str(Fun.Function1FightCount))

    def SaveFile(self):        
        Fun.Function1FightCount = self.Times_spinBox_2.value()
        Fun.Function2FightCount = self.Times_spinBox_3.value()
        Fun.Function3FightCount = self.Times_spinBox_5.value()
        Savedata = {}
        Savedata['function1'] = {'FightCount': Fun.Function1FightCount, 'TypeSelect': 0}
        Savedata['function2'] = {'FightCount': Fun.Function2FightCount, 'TypeSelect': 0}
        Savedata['function3'] = {'FightCount': Fun.Function3FightCount, 'TypeSelect': 0}

        with open('systemdata/datasave/data.json', 'w') as datafile:
            json.dump(Savedata,datafile)
        self.label_10.setText("set成功")
        print("set成功")

    

    def SetScreenfuntion(self):       
        try:
            windowsgetIndex = self.WindowsComboBox.currentIndex()
            windowsgetstr = self.WindowsComboBox.currentText()
            Fun.WindowsHandle = win32gui.FindWindow(None, windowsgetstr)
            left, top, right, bottom = win32gui.GetWindowRect(Fun.WindowsHandle)
            posStr1 = str(left).rjust(4)+','+str(top).rjust(4)+','+str(right).rjust(4)+','+str(bottom).rjust(4)
            print("AppPos: ", posStr1)
            width = right - left
            height = bottom - top
            print(width, height)
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
        self.WindowsComboBox.addItem("自動人 我的超人")
        print ("自動人 我的超人")
        try:
            windowsgetstr = self.WindowsComboBox.currentText()
            Fun.WindowsHandle = win32gui.FindWindow(None, windowsgetstr)
            left, top, right, bottom = win32gui.GetWindowRect(Fun.WindowsHandle)
        except:
            print("沒有找到視窗")
        

       


    
