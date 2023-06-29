from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Call_MainUi import MainPageWindow
from UI.Call_Help import HelpPageWindow
from UI.Call_Setting import SettingPageWindow
from UI.Call_BattleSetting import BattleSettingPageWindow
from PyQt5.QtGui import QPixmap
import systemdata.icon.ICON
import Function.Foundation as Fun

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initMainUI()
        self.initTitleUI_info()
    
    def initTitleUI_info(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ICON.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)
        self.setWindowTitle(Fun.version)

    def initMainUI(self):
        self.resize(953,700)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        
        self.Stack = QStackedWidget()
        self.layout.addWidget(self.Stack)
        
        self.CallMainUi = MainPageWindow()
        self.CallHelpUi = HelpPageWindow()
        self.CallSettingUI = SettingPageWindow()
        self.CallBattleSettingUI = BattleSettingPageWindow()
        
        self.Stack.addWidget(self.CallMainUi)

        self.CallMainUi.chooseSignal.connect(self.showDialog)
    
    def closeEvent(self, event):
        self.CallHelpUi.close()
        self.CallSettingUI.close()
        self.CallBattleSettingUI.close()

        

    def showDialog(self,msg):
        if msg == 'Help':
            #self.Stack.setCurrentIndex(1)
            self.CallHelpUi.show()
        elif msg == 'change':
            self.resize(953,700)
        elif msg == 'setting':
            self.CallSettingUI.show()
        elif msg == 'BattleSetting':
            self.CallBattleSettingUI.show()
        #if msg == 'Hide':
        #    self.groupBox_2.Hide()