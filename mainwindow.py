from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from Call_MainUi import MainPageWindow
from Call_Help import HelpPageWindow
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
        self.resize(702, 423)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        
        self.Stack = QStackedWidget()
        self.layout.addWidget(self.Stack)
        
        self.CallMainUi = MainPageWindow()
        self.CallHelpUi = HelpPageWindow()
        
        self.Stack.addWidget(self.CallMainUi)
        #self.Stack.addWidget(self.CallHelpUi)

        self.CallMainUi.chooseSignal.connect(self.showDialog)

        

    def showDialog(self,msg):
        if msg == 'Help':
            #self.Stack.setCurrentIndex(1)
            self.CallHelpUi.show()
        if msg == 'Hide':
            self.groupBox_2.Hide()