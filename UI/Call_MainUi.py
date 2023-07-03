from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Homepage.ui_MainUI import Ui_GBF_MAIN
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
import systemdata.icon.ICON
import systemdata.img.Arcarum.ARCARUM
from Function.Page1Function import RunFunction1
from Function.Page4Function import RunFunction4
from Function.DebugFunction import Debugfunction
from Function.Position import GBFPosition
from Function.DiscordBlockDet import GetBlockDET
from Function.Picture import GetPicFunction
import Function.Foundation as Fun
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
from Function.Action import FCAction
import keyboard


from UI.Call_Help import HelpPageWindow
from UI.Call_Setting import SettingPageWindow
from UI.Call_BattleSetting import BattleSettingPageWindow

class MainPageWindow(QtWidgets.QMainWindow,Ui_GBF_MAIN):
    chooseSignal = pyqtSignal(str)

    def __init__(self,parent=None):#起始位置
        super().__init__()
        self.setupUi(self)
        self.initUiindex()
        self.initbuttonUI()
        self.default()
        self.SetArcarumPIC()
        self.SetSommonValue()
        self.SRadio()
        self.CloseRadio()


    def initMainUI(self):
        self.CallMainUi.chooseSignal.connect(self.showDialog)
        

    def initUiindex(self):#UI框架基礎設定
        self.resize(Fun.resizeX,Fun.resizeY)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.CallHelpUi = HelpPageWindow()
        self.CallSettingUI = SettingPageWindow()
        self.CallBattleSettingUI = BattleSettingPageWindow()

        titleicon = QtGui.QIcon()
        titleicon.addPixmap(QtGui.QPixmap(":/ICON.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Helpicon = QtGui.QIcon()
        Icon_sort30 = QtGui.QIcon()#轉世
        Icon_sort25 = QtGui.QIcon()#天司
        Icon_sort8 = QtGui.QIcon()#方陣
        Icon_sort7 = QtGui.QIcon()#方陣2.0
        Icon_sort21 = QtGui.QIcon()#十天眾
        self.setWindowIcon(titleicon)
        self.setWindowTitle(Fun.version)#title
        Helpicon.addPixmap(QtGui.QPixmap(":/Heip.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Icon_sort30.addPixmap(QtGui.QPixmap(":/icon_sort_wepon_30.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Icon_sort25.addPixmap(QtGui.QPixmap(":/icon_sort_wepon_25.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Icon_sort8.addPixmap(QtGui.QPixmap(":/icon_sort_wepon_08.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Icon_sort7.addPixmap(QtGui.QPixmap(":/icon_sort_wepon_07.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Icon_sort21.addPixmap(QtGui.QPixmap(":/icon_sort_wepon_21.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)

        #set icon
        self.actionHelp.setIcon(Helpicon)#help

    def default(self):#框架預設#最初全域變數歸檔
        x = FCAction()
        x.LoadFile()
        
        self.Times_spinBox_2.setValue(Fun.Function1FightCount)
        self.SaveText.setText("")
        self.PageTitle.setText("轉世沙盒")
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
        #副視窗
        self.actionHelp.triggered.connect(lambda: self.CallHelpUi.show())
        self.actionsetting.triggered.connect(lambda: self.CallSettingUI.show())
        #執行腳本
        self.Screptrun.clicked.connect(self.showDialog)
        #停止
        self.FuncStopButton.clicked.connect(self.showDialog)
        self.AllstopButton.clicked.connect(self.showDialog)
        #儲存
        self.SetButton.clicked.connect(self.showDialog)
        #次數
        self.Times_spinBox_2.valueChanged.connect(self.showDialog)
        #分頁
        self.tabWidget.currentChanged.connect(self.showDialog)

        #self.PositionButton.clicked.connect(self.showDialog)
        #重整大小
        self.FRWidge.clicked.connect(lambda: self.resize(Fun.resizeX,Fun.resizeY))
        self.FunctionBox.currentIndexChanged.connect(self.showDialog)
        #地區及關卡
        self.FightcomboBox_2.currentIndexChanged.connect(self.showDialog)
        self.FightcomboBox_4.currentIndexChanged.connect(self.showDialog)
        #self.DebugButton.clicked.connect(self.showDialog)
        #手動設定腳色腳本
        self.AddButton.clicked.connect(self.showDialog)
        self.DelButton.clicked.connect(self.showDialog)
        self.FightcomboBox.currentIndexChanged.connect(self.showDialog)
        self.Battle_TbW.cellClicked.connect(self.showDialog)
        #執行方式
        self.ScreptRadio.toggled.connect(self.showDialog)
        self.HandRadio.toggled.connect(self.showDialog)
        self.TSommonRadio.toggled.connect(self.showDialog)
        self.AutoRadio.toggled.connect(self.showDialog)
        #結束判定
        self.OneTradio.toggled.connect(self.showDialog)
        self.QuestClearradio.toggled.connect(self.showDialog)
        self.Scoreradio.toggled.connect(self.showDialog)
        #hotkey
        keyboard.add_hotkey('F2', self.on_hotkey_triggered)
        keyboard.add_hotkey('Esc', self.on_hotkey_Stop)
        #存讀檔
        self.SaveSCButton.clicked.connect(self.showDialog)
        self.LoadSCButton.clicked.connect(self.showDialog)
        #User存讀檔
        self.UserSaveButton.clicked.connect(self.showDialog)
        self.UserLoadButton.clicked.connect(self.showDialog)
    
    def showDialog(self):#按鈕function
        sender = self.sender()
        #換頁
        if sender == self.FunctionBox:
            self.change_Page()
        #跑腳本
        elif sender == self.Screptrun:
            if Fun.TabPage == 0:
                self.Info_broswer.setText("腳本執行中")
                x = RunFunction()
                x.RunFGscrept()
            elif Fun.TabPage == 1:
                print("執行Page2的 Funciton")
        #停止
        elif sender == self.FuncStopButton or sender == self.AllstopButton:
            Fun.StopFunction = True
            self.Info_broswer.clear()
        #存檔
        elif sender == self.SetButton:
            self.SaveFile()
        elif sender == self.Times_spinBox_2:
            self.settingtext()
        #地區
        elif sender == self.FightcomboBox_2:
            self.SetArcarumPIC()
            Fun.Map = self.FightcomboBox_2.currentText()
        #關卡
        elif sender == self.FightcomboBox_4:
            Fun.challenge = self.FightcomboBox_4.currentText()
        #動態增減欄位
        elif sender == self.AddButton:
            self.addRow()
        elif sender == self.DelButton:
            self.delRow()
            self.DelButton.setEnabled(False)
            
        elif sender == self.FightcomboBox:
            self.SetSommonValue()
        elif sender == self.Battle_TbW:
            self.DelButton.setEnabled(True)
        elif sender == self.ScreptRadio or sender == self.HandRadio or sender == self.TSommonRadio or sender == self.AutoRadio:
            self.SRadio()
        elif sender == self.Scoreradio or sender == self.OneTradio or sender == self.QuestClearradio:
            self.CloseRadio()
        elif sender == self.tabWidget:
            current_index = self.tabWidget.currentIndex()
            if current_index == 0:
                self.change_Page()
                Fun.TabPage = 0
            elif current_index == 1:
                self.PageTitle.setText("自訂點擊")
                Fun.TabPage = 1
        #存讀檔
        elif sender == self.SaveSCButton:
            self.saveFile()
        elif sender == self.LoadSCButton:
            self.loadFile()
        #自訂存讀檔
        elif sender == self.UserSaveButton:
            self.UserSaveFile()
        elif sender == self.UserLoadButton:
            self.UserLoadFile()

        #elif sender == self.DebugButton:
        #    x=FCAction()
        #    Picture = cv2.imread("./systemdata/img/systemimg/Arcarum_New_Title.PNG")
        #    x.ClickPIC(Picture)
            
        #    
        #    x.MoveCurtoGamePage()
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

    def on_hotkey_triggered(self):
        if Fun.RunFlag == False:
            QMetaObject.invokeMethod(self.Info_broswer, 'setText', Qt.QueuedConnection, Q_ARG(str, "腳本執行中"))

            if Fun.Type == 0:
                x = RunFunction1()
            elif Fun.Type == 1:
                x = RunFunction1()
            elif Fun.Type == 2:
                x = RunFunction1()
            elif Fun.Type == 3:
                x = RunFunction1()
            elif Fun.Type == 4:
                x = RunFunction4()

            x.RunFGscrept()
            if Fun.BroswerText != " ":
                QMetaObject.invokeMethod(self.Info_broswer, 'setText', Qt.QueuedConnection, Q_ARG(str, Fun.BroswerText))
    
    def on_hotkey_Stop(self):
        if Fun.StopFunction == False:
            Fun.StopFunction = True
            QMetaObject.invokeMethod(self.Info_broswer, 'setText', Qt.QueuedConnection, Q_ARG(str, "中斷程序"))
            self.Mbox('終止', '緊急終止', 0)

    def change_Page(self):
        Fun.Type = self.FunctionBox.currentIndex()
        self.Arcarum_1.hide()
        self.Arcarum_2.hide()
        self.Sommon.hide()
        if Fun.Type == 0:
            self.PageTitle.setText("轉世沙盒")
            self.Arcarum_1.show()
            self.Arcarum_2.show()
        elif Fun.Type == 1:
            self.PageTitle.setText("外放舔關")
            self.Sommon.show()
        elif Fun.Type == 2:
            self.PageTitle.setText("1T天使關")
            self.Sommon.show()
        elif Fun.Type == 3:
            self.PageTitle.setText("大天使關")
            self.Sommon.show()
        elif Fun.Type == 4:
            self.PageTitle.setText("星之古戰場")
            self.Sommon.show()

    def settingtext(self):
        Fun.Function1FightCount = self.Times_spinBox_2.value()
        if Fun.Function1FightCount == 0:
            self.label_1.setText("Set 無上限")
        else:
            self.label_1.setText("Set :"+str(Fun.Function1FightCount))

    def SaveFile(self):
        x = FCAction()
        Fun.Function1FightCount = self.Times_spinBox_2.value()
        x.SaveChange()
        self.SaveText.setText("set成功")
        print("set成功")    

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

    def CloseRadio(self):
        if self.OneTradio.isChecked():
            self.ScoreSpin.setEnabled(False)
        elif self.QuestClearradio.isChecked():
            self.ScoreSpin.setEnabled(False)
        elif self.Scoreradio.isChecked():
            self.ScoreSpin.setEnabled(True)

    def addRow(self):
        # 在表格中新增一行
        row_count = self.Battle_TbW.rowCount()
        self.Battle_TbW.setRowCount(row_count + 1)

        # 添加下拉選項列        
        combo_box = QComboBox()
        combo_box.addItems([str(i) for i in range(1, 100)])
        RowBotton = QPushButton("...")
        
        self.Battle_TbW.setCellWidget(row_count, 0, combo_box)
        self.Battle_TbW.setCellWidget(row_count, 1, RowBotton)
        self.Battle_TbW.setCellWidget(row_count, 2, None)
        def setting():             
            Fun.Currenttable = self.Battle_TbW.currentRow()
            print("Currenttable",Fun.Currenttable)
            self.CallBattleSettingUI.show()
        RowBotton.clicked.connect(setting)        

    def delRow(self):
        # 删除所選行
        current_row = self.Battle_TbW.currentRow()
        if current_row >= 0:
            self.Battle_TbW.removeRow(current_row)

    def saveFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "./systemdata/datasave/BattleScrept", "Text Files (*.json)", options=options)
        if fileName:
            with open(fileName, "w") as file:
                file.write("Hello, World!")

    def loadFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "./systemdata/datasave/BattleScrept", "Text Files (*.json)", options=options)
        if fileName:
            with open(fileName, "r") as file:
                content = file.read()
                print(content)

    def UserSaveFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "./systemdata/datasave/UserScrept", "Text Files (*.json)", options=options)
        if fileName:
            with open(fileName, "w") as file:
                file.write("Hello, World!")

    def UserLoadFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "./systemdata/datasave/UserScrept", "Text Files (*.json)", options=options)
        if fileName:
            with open(fileName, "r") as file:
                content = file.read()
                print(content)