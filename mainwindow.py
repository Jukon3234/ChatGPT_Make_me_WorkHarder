from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from Call_MainUi import MainPageWindow
from Call_Help import HelpPageWindow

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(411, 423)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        self.Stack = QStackedWidget()
        self.layout.addWidget(self.Stack)
        
        self.CallMainUi = MainPageWindow()
        self.CallHelpUi = HelpPageWindow()
        
        self.Stack.addWidget(self.CallMainUi)
        self.Stack.addWidget(self.CallHelpUi)

        self.CallMainUi.chooseSignal.connect(self.showDialog)

    def showDialog(self,msg):
        if msg == 'Help':
            self.Stack.setCurrentIndex(1)