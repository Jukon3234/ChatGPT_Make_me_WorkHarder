from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Call_MainUi import MainPageWindow
from UI.Call_Help import HelpPageWindow
from UI.Call_Setting import SettingPageWindow
from PyQt5.QtGui import QPixmap
import systemdata.icon.ICON

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initMainUI()
        self.initTitleUI_info()
    
    def initTitleUI_info(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ICON.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)
        self.setWindowTitle('自動人 我的超人')

    def initMainUI(self):
        self.resize(953,700)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        
        self.Stack = QStackedWidget()
        self.layout.addWidget(self.Stack)
        
        self.CallMainUi = MainPageWindow()
        self.CallHelpUi = HelpPageWindow()
        self.CallSettingUI = SettingPageWindow()
        
        self.Stack.addWidget(self.CallMainUi)

        self.CallMainUi.chooseSignal.connect(self.showDialog)
    
    def closeEvent(self, event):
        self.CallHelpUi.close()
        self.CallSettingUI.close()

        

    def showDialog(self,msg):
        if msg == 'Help':
            #self.Stack.setCurrentIndex(1)
            self.CallHelpUi.show()
        elif msg == 'change':
            self.resize(953,700)
        elif msg == 'setting':
            self.CallSettingUI.show()
        #if msg == 'Hide':
        #    self.groupBox_2.Hide()