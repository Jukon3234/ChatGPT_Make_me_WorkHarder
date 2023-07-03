from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Homepage.ui_Setting import Ui_Setting
from PyQt5.QtCore import pyqtSignal,Qt
from ctypes import windll, byref
from ctypes.wintypes import HWND, POINT
from win32gui import *
from Function.Action import FCAction
import win32gui
import os
import Function.Foundation as Fun




class SettingPageWindow(QWidget,Ui_Setting):
    
    returnSignal = pyqtSignal()

    def __init__(self,parent=None):
        super(SettingPageWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.Init()
        self.ButtonSetup()
        self.ButtonDef()
            
    def ButtonDef(self):
        #視窗
        self.WindowsComboBox.currentIndexChanged.connect(self.showDialog)
        #Discord BOT 通風報信
        self.groupBox.toggled.connect(self.showDialog)
        #OKBUtton
        self.OKButton.clicked.connect(self.showDialog)
        self.CancelButton.clicked.connect(self.showDialog)

    def showDialog(self):
        sender = self.sender()
        #視窗選擇
        if sender == self.WindowsComboBox:
            self.SetScreenfuntion()            
        #DC        
        elif sender == self.groupBox:
            self.ButtonSetup()
        #Button
        elif sender == self.OKButton:
            self.SetupSet()
            self.Init()
            self.close()
        elif sender == self.CancelButton:
            self.Init()
            self.close()

    def Init(self):        
        self.GetScreenFunc()

        #點擊間距延遲(ms)
        self.stepspinBox.setValue(Fun.StepDelay)
        self.stepdelayran.setValue(Fun.StepdelayRandom)        
        Fun.NstepdelayRandom = self.setobset(Fun.StepdelayRandom)

        #迴圈延遲(ms)        
        self.RoundspinBox.setValue(Fun.RoundDelay)
        self.Rounddelayran.setValue(Fun.RounddelayRandom)
        Fun.NRounddelayRandom = self.setobset(Fun.RounddelayRandom)

        #移動時長(ms)        
        self.CurMoveTime.setValue(Fun.CurmoveTime)        
        self.CurMoveTimeRan.setValue(Fun.CurmoveTimeRandom)        
        Fun.NCurMoveTimeRan = self.setobset(Fun.CurmoveTimeRandom)        
        
        #正負偏移量(X/Y)        
        self.RandomXSpin.setValue(Fun.RandomX)        
        Fun.NRandomX = self.setobset(Fun.RandomX)
        self.RandomYSpin.setValue(Fun.RandomY)        
        Fun.NRandomY = self.setobset(Fun.RandomY)

        if Fun.DCBOT_EN == True:
            self.groupBox.setChecked(True)
        elif Fun.DCBOT_EN == False:
            self.groupBox.setChecked(False)

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
        self.WindowsComboBox.addItem(Fun.version)
        try:
            windowsgetstr = self.WindowsComboBox.currentText()
            Fun.WindowsHandle = win32gui.FindWindow(None, windowsgetstr)
            left, top, right, bottom = win32gui.GetWindowRect(Fun.WindowsHandle)
        except:
            print("沒有找到視窗")

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

    def ButtonSetup(self):
        if self.groupBox.isChecked() == False:
            Fun.DCBOT_EN = False
        else:
            Fun.DCBOT_EN = True
    
    def setobset(self,number):
        num = number - number*2
        return num

