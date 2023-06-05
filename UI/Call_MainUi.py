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
from Function.DiscordBlockDet import GetBlockDET
from Function.Picture import GetPicFunction
import Function.Foundation as Fun
import json
import datetime
from win32gui import *
from ctypes import windll, byref
from ctypes.wintypes import HWND, POINT
import time
import sys
import win32gui
import os
import pyautogui as pag
import cv2

class MainPageWindow(QtWidgets.QMainWindow,Ui_GBF_MAIN):
    chooseSignal = pyqtSignal(str)

    def __init__(self,parent=None):#起始位置
        super(MainPageWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUiindex()
        self.initbuttonUI()
        self.default()
        self.SetArcarumPIC()
        self.SetSommonValue()
        self.SRadio()
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
            elif i == 1:#舔關
                item.setIcon(Icon_sort8) 
            elif i == 2:#1T天使關
                item.setIcon(Icon_sort25)
            elif i == 3:#十天眾天使關
                item.setIcon(Icon_sort21)
            elif i == 4:#古戰場
                item.setIcon(Icon_sort21)

    def default(self):#框架預設#最初全域變數歸檔
        if os.path.exists('./systemdata/datasave/data.json'):
            SaveFile = open('systemdata/datasave/data.json')
        else:
            SaveFile = open('systemdata/datasave/Default.json')
        savedata= json.load(SaveFile)
        Fun.DCBOT_Token = savedata['Bot']['TOKEN']
        Fun.DCBOT_ChannalID = savedata['Bot']['Channal_ID']
        self.Times_spinBox_2.setValue(savedata['function']['FightCount'])
        self.PageTitle.setText("轉世")
        self.Arcarum_1.show()
        self.Arcarum_2.show() 
        self.Sommon.hide()

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
        def SetComboBox3():
            print("item_count",item_count)
            if item_count == 0:
                for i in range(1,14):
                    self.FightcomboBox_4.addItem(str(i))
            else:
                for i in range(0,item_count):
                    self.FightcomboBox_4.removeItem(0)
                for j in range(1,14):
                    self.FightcomboBox_4.addItem(str(j))
        if PicGetIndex == 0:
            img = QtGui.QPixmap(":/area_2_cleared.png")
            img2 = QtGui.QPixmap(":/area2.jpg")
            Fun.ReadArcarumPIC = cv2.imread("./systemdata/img/systemimg/Area2.PNG")
            img2H = 229*0.4
            img2W = 1024*0.4
            SetComboBox1()
        elif PicGetIndex == 1:
            img = QtGui.QPixmap(":/area_3_cleared.png")
            img2 = QtGui.QPixmap(":/area3.jpg")            
            Fun.ReadArcarumPIC = cv2.imread("./systemdata/img/systemimg/Area3.PNG")
            img2H = 229*0.4
            img2W = 1024*0.4
            SetComboBox1()
        elif PicGetIndex == 2:
            img = QtGui.QPixmap(":/area_4_cleared.png")
            img2 = QtGui.QPixmap(":/area4.jpg")
            Fun.ReadArcarumPIC = cv2.imread("./systemdata/img/systemimg/Area4.PNG")
            img2H = 229*0.4
            img2W = 1024*0.4
            SetComboBox1()
        elif PicGetIndex == 3:
            img = QtGui.QPixmap(":/area_5_cleared.png")
            img2 = QtGui.QPixmap(":/area5.jpg")
            Fun.ReadArcarumPIC = cv2.imread("./systemdata/img/systemimg/Area5.PNG")
            img2H = 229*0.4
            img2W = 1024*0.4
            SetComboBox1()
        elif PicGetIndex == 4:
            img = QtGui.QPixmap(":/area_6_cleared.png")
            img2 = QtGui.QPixmap(":/area6.jpg")
            Fun.ReadArcarumPIC = cv2.imread("./systemdata/img/systemimg/Area6.PNG")
            img2H = 430*0.25
            img2W = 1280*0.25
            SetComboBox2()
        elif PicGetIndex == 5:
            img = QtGui.QPixmap(":/area_7_cleared.png")
            img2 = QtGui.QPixmap(":/area7.jpg")
            Fun.ReadArcarumPIC = cv2.imread("./systemdata/img/systemimg/Area7.PNG")
            img2H = 430*0.25
            img2W = 1280*0.25
            SetComboBox2()
        elif PicGetIndex == 6:
            img = QtGui.QPixmap(":/area_8_cleared.png")
            img2 = QtGui.QPixmap(":/area8.jpg")
            Fun.ReadArcarumPIC = cv2.imread("./systemdata/img/systemimg/Area8.PNG")
            img2H = 430*0.25
            img2W = 1280*0.25
            SetComboBox2()
        elif PicGetIndex == 7:
            img = QtGui.QPixmap(":/area_9_cleared.png")
            img2 = QtGui.QPixmap(":/area9.jpg")
            Fun.ReadArcarumPIC = cv2.imread("./systemdata/img/systemimg/Area9.PNG")
            img2H = 430*0.25
            img2W = 1280*0.25
            SetComboBox2()
        elif PicGetIndex == 8:
            img = QtGui.QPixmap(":/area_10_cleared.png")
            img2 = QtGui.QPixmap(":/area10.png")
            Fun.ReadArcarumPIC = cv2.imread("./systemdata/img/systemimg/Area10.PNG")
            img2H = 319*0.3
            img2W = 1326*0.3
            SetComboBox3()

        img = img.scaled(150,80)
        self.PicLable.setPixmap(img)
        img2 = img2.scaled(int(img2W),int(img2H))
        self.PicLable_2.setPixmap(img2)


    def initbuttonUI(self):#按鈕設定
        self.actionHelp.triggered.connect(self.showDialog)
        self.actionsetting.triggered.connect(self.showDialog)
        self.Funtionlist.clicked.connect(self.showDialog)
        self.Screptrun.clicked.connect(self.showDialog)
        self.FuncStopButton.clicked.connect(self.showDialog)
        self.AllstopButton.clicked.connect(self.showDialog)
        self.SetButton.clicked.connect(self.showDialog)
        self.Times_spinBox_2.valueChanged.connect(self.showDialog)
        self.WindowsComboBox.currentIndexChanged.connect(self.showDialog)
        self.PositionButton.clicked.connect(self.showDialog)
        self.FRWidge.clicked.connect(self.showDialog)
        #地區及關卡
        self.FightcomboBox_2.currentIndexChanged.connect(self.showDialog)
        self.FightcomboBox_4.currentIndexChanged.connect(self.showDialog)
        #self.DebugButton.clicked.connect(self.showDialog)
        #手動設定腳色腳本
        self.AddButton.clicked.connect(self.showDialog)
        self.DelButton.clicked.connect(self.showDialog)
        self.FightcomboBox.currentIndexChanged.connect(self.showDialog)
        self.tableWidget.cellClicked.connect(self.showDialog)
        #執行方式
        self.ScreptRadio.toggled.connect(self.showDialog)
        self.HandRadio.toggled.connect(self.showDialog)
        self.TSommonRadio.toggled.connect(self.showDialog)
        self.AutoRadio.toggled.connect(self.showDialog)
    
    def showDialog(self):#按鈕function
        sender = self.sender()
        if sender == self.actionHelp:
            self.chooseSignal.emit('Help')
        elif sender == self.actionsetting:
            self.chooseSignal.emit('setting')
        elif sender == self.Funtionlist:
            self.change_Page()
        elif sender == self.Screptrun:
            self.Info_broswer.setText("腳本執行中")
            x=RunFunction()
            x.RunFGscrept()
        elif sender == self.FuncStopButton or sender == self.AllstopButton:
            Fun.StopFunction = True
            self.Info_broswer.clear()
        elif sender == self.SetButton:
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
            Fun.Map = self.FightcomboBox_2.currentText()
            self.ReadMap()
        elif sender == self.FightcomboBox_4:
            Fun.challenge = self.FightcomboBox_4.currentText()
            self.ReadMap()
        elif sender == self.AddButton:
            self.addRow()
        elif sender == self.DelButton:
            self.delRow()
            self.DelButton.setEnabled(False)
        elif sender == self.FightcomboBox:
            self.SetSommonValue()
        elif sender == self.tableWidget:
            self.DelButton.setEnabled(True)
        elif sender == self.ScreptRadio or sender == self.HandRadio or sender == self.TSommonRadio or sender == self.AutoRadio:
            self.SRadio()
        #elif sender == self.DebugButton:
        #   if Fun.DCBOT_EN == True:
        #       DET = GetPicFunction()
        #       DET2 = GetBlockDET()
        #       Picture = cv2.imread('./systemdata/img/systemimg/BLOCK.PNG')
        #       if DET.PicDetTF(Picture) == True:
        #           DET2.SysGetPic()
        #           DET2.DC_Get_Verify()
        #    else:
        #       print("no Function")
        #elif sender == self.DebugButton:
        #    self.SetScreenfuntion()
        #    x=Debugfunction()
        #    x.debugLog()

    def change_Page(self):
        text = self.Funtionlist.currentItem().text()
        self.Arcarum_1.hide()
        self.Arcarum_2.hide()
        self.Sommon.hide()
        if text == "轉世":
            self.PageTitle.setText("轉世")
            self.Arcarum_1.show()
            self.Arcarum_2.show()
        if text == "十天眾天使關":
            self.PageTitle.setText("十天眾天使關")
            self.Sommon.show()
        if text == "刷巴哈角":
            self.PageTitle.setText("刷巴哈角")
            self.Sommon.show()
        if text == "古戰場":
            self.PageTitle.setText("古戰場")
            self.Sommon.show()

    def settingtext(self):
        Fun.Function1FightCount = self.Times_spinBox_2.value()
        if Fun.Function1FightCount == 0:
            self.label_10.setText("Set 無上限")
        else:
            self.label_10.setText("Set :"+str(Fun.Function1FightCount))

    def SaveFile(self):
        Fun.Function1FightCount = self.Times_spinBox_2.value()
        Savedata = {}
        Savedata['function'] = {'FightCount': Fun.Function1FightCount, 'TypeSelect': 0}
        Savedata['Bot'] = {'TOKEN': Fun.DCBOT_Token,'Channal_ID': Fun.DCBOT_ChannalID,'Enabled' : Fun.DCBOT_EN}

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
            if t == "GBF Broswers":
                self.WindowsComboBox.addItem(t)
                self.WindowsComboBox.setCurrentText(t)
            else:
                self.WindowsComboBox.addItem(t)
            print (t)
        self.WindowsComboBox.addItem("自動人 我的超人")
        try:
            windowsgetstr = self.WindowsComboBox.currentText()
            Fun.WindowsHandle = win32gui.FindWindow(None, windowsgetstr)
            left, top, right, bottom = win32gui.GetWindowRect(Fun.WindowsHandle)
        except:
            print("沒有找到視窗")

    def SetSommonValue(self):
        Index = self.FightcomboBox.currentIndex()
        item_count = self.sommonCombox.count()
        def insertindex():
            if Index == 6:#特殊
                self.sommonCombox.addItem("黃龍")
                self.sommonCombox.addItem("天照")
                self.sommonCombox.addItem("黑麒麟")
            else:        
                self.sommonCombox.addItem("方陣80%")
                self.sommonCombox.addItem("方陣100%")
                self.sommonCombox.addItem("方陣120%")
                self.sommonCombox.addItem("方陣140%")
                self.sommonCombox.addItem("主神80%")
                self.sommonCombox.addItem("主神100%")
                self.sommonCombox.addItem("主神120%")
                self.sommonCombox.addItem("主神150%")
                if Index == 0:#火
                    self.sommonCombox.addItem("濕婆100%")
                    self.sommonCombox.addItem("濕婆120%")
                    self.sommonCombox.addItem("濕婆140%")
                if Index == 1:#水
                    self.sommonCombox.addItem("歐羅巴100%")
                    self.sommonCombox.addItem("歐羅巴120%")
                    self.sommonCombox.addItem("歐羅巴140%")
                if Index == 2:#風
                    self.sommonCombox.addItem("軍神120%")
                    self.sommonCombox.addItem("軍神140%")
                if Index == 3:#土
                    self.sommonCombox.addItem("猩猩110%")
                if Index == 4:#光
                    self.sommonCombox.addItem("路西法100%")
                    self.sommonCombox.addItem("路西法150%")
                    self.sommonCombox.addItem("路西法200UP")
                if Index == 5:#暗
                    self.sommonCombox.addItem("巴哈姆特100%")
                    self.sommonCombox.addItem("巴哈姆特120%")
                    self.sommonCombox.addItem("巴哈姆特150%")
                    self.sommonCombox.addItem("巴哈姆特200UP")
        if item_count == 0:
            insertindex()
        else:
            for i in range(0,item_count):
                self.sommonCombox.removeItem(0)
            insertindex()

    def Blockdet(slef):
        DET = GetBlockDET()
        if DET.FuncBlockPicDet() == True:
            DET.SysGetPic()
            DET.DC_Get_Verify()
    
    def SRadio(self):
        if self.ScreptRadio.isChecked():
            self.AutoGroupBox.setEnabled(True)
            self.UserSetgroupBox.setEnabled(False)
        elif self.HandRadio.isChecked():
            self.UserSetgroupBox.setEnabled(True)
            self.AutoGroupBox.setEnabled(False)
        elif self.TSommonRadio.isChecked() or self.AutoRadio.isChecked():
            self.AutoGroupBox.setEnabled(False)
            self.UserSetgroupBox.setEnabled(False)


    def ReadMap(self):
        if Fun.Map == "1":
            if Fun.challenge == "1":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "2":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "3":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "4":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "5":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "6":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "7":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "8":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "9":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "10":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
        elif Fun.Map == "2":
            if Fun.challenge == "1":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "2":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "3":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "4":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "5":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "6":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "7":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "8":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "9":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "10":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
        elif Fun.Map == "3":
            if Fun.challenge == "1":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "2":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "3":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "4":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "5":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "6":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "7":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "8":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "9":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "10":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
        elif Fun.Map == "4":
            if Fun.challenge == "1":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "2":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "3":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "4":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "5":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "6":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "7":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "8":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "9":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "10":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
        elif Fun.Map == "5":
            if Fun.challenge == "1":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "2":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "3":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "4":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "5":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "6":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "7":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
        elif Fun.Map == "6":
            if Fun.challenge == "1":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "2":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "3":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "4":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "5":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "6":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "7":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
        elif Fun.Map == "7":
            if Fun.challenge == "1":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "2":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "3":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "4":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "5":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "6":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "7":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
        elif Fun.Map == "8":
            if Fun.challenge == "1":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "2":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "3":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "4":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "5":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "6":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "7":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
        elif Fun.Map == "9":
            if Fun.challenge == "1":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "2":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "3":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "4":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "5":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "6":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "7":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "8":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "9":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "10":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "11":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "12":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "13":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
            elif Fun.challenge == "14":
                print(f"Map:{Fun.Map}-{Fun.challenge}")
        else:
            print("Error")

    def addRow(self):
        # 在表格中新增一行
        row_count = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row_count + 1)

        # 添加下拉選項列
        for col in range(6):
            self.tableWidget.setCellWidget(row_count, col, None)

    def delRow(self):
        # 删除所選行
        current_row = self.tableWidget.currentRow()
        if current_row >= 0:
            self.tableWidget.removeRow(current_row)