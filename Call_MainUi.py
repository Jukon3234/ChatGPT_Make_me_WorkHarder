from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Homepage.ui_MainUI import Ui_GBF_MAIN
from PyQt5.QtCore import pyqtSignal,Qt
from PyQt5.QtGui import QPixmap
import systemdata.icon.ICON

class MainPageWindow(QtWidgets.QMainWindow,Ui_GBF_MAIN):
    
    chooseSignal = pyqtSignal(str)

    def __init__(self,parent=None):
        super(MainPageWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUiindex()
        self.initbuttonUI()
        self.change_group1()

    def initUiindex(self):
        titleicon = QtGui.QIcon()
        titleicon.addPixmap(QtGui.QPixmap(":/ICON.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Helpicon = QtGui.QIcon()
        Saveicon = QtGui.QIcon()
        Loadicon = QtGui.QIcon()
        Exiticon = QtGui.QIcon()
        self.setWindowIcon(titleicon)
        self.setWindowTitle('自動人 我的超人')#title
        Helpicon.addPixmap(QtGui.QPixmap(":/Heip.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionHelp.setIcon(Helpicon)#help
        Saveicon.addPixmap(QtGui.QPixmap(":/Save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionAdd.setIcon(Saveicon)#help
        Loadicon.addPixmap(QtGui.QPixmap(":/Load.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionOpen.setIcon(Loadicon)#help
        Exiticon.addPixmap(QtGui.QPixmap(":/door.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionEXIT.setIcon(Exiticon)#help



    def initbuttonUI(self):
        self.actionHelp.triggered.connect(self.showDialog)
        self.AddpushButton.clicked.connect(self.showDialog)
        self.changebutton.clicked.connect(self.showDialog)
    
    def showDialog(self):
        sender = self.sender()
        if sender == self.actionHelp:
            self.chooseSignal.emit('Help')
        if sender == self.AddpushButton:
            self.change_group1()
        if sender == self.changebutton:
            self.change_group2()

    def change_group1(self):
        #horizontalLayout_7.replaceWidget(self.groupBox_2,self.groupBox_7,self.groupBox_16)
        self.groupBox_2.setVisible(True) 
        self.groupBox_7.setVisible(False)
        self.groupBox_16.setVisible(False)

    def change_group2(self):
        #horizontalLayout_7.replaceWidget(self.groupBox_2,self.groupBox_7,self.groupBox_16)
        self.groupBox_2.setVisible(False)
        self.groupBox_7.setVisible(True) 
        self.groupBox_16.setVisible(False)

       


    
