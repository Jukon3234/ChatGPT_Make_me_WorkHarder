from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Homepage.ui_Setting import Ui_Setting
from PyQt5.QtCore import pyqtSignal,Qt
import Function.Foundation as Fun
from ctypes import windll, byref
from ctypes.wintypes import HWND, POINT
from win32gui import *
import win32gui
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
        self.WindowsComboBox.currentIndexChanged.connect(self.showDialog)

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
        elif sender == self.WindowsComboBox:
            self.SetScreenfuntion()

    def Init(self):        
        self.GetScreenFunc()
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
