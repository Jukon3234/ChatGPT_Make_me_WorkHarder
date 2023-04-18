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
        self.change_Page1()#預設為page1

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
        self.Funtionlist.clicked.connect(self.showDialog)
        #self.AddpushButton.clicked.connect(self.showDialog)
        #self.changebutton.clicked.connect(self.showDialog)
    
    def showDialog(self):
        sender = self.sender()
        if sender == self.actionHelp:
            self.chooseSignal.emit('Help')        
        if  sender == self.Funtionlist:
            text = self.Funtionlist.currentItem().text()
            if text == "轉世":
                self.Info_broswer.setText("轉世")
                self.change_Page1()
            if text == "方陣":
                self.Info_broswer.setText("方陣")
                self.change_Page2()
            if text == "方陣速刷":
                self.Info_broswer.setText("方陣速刷")
                self.change_Page3()

    def change_Page1(self):
        #horizontalLayout_7.replaceWidget(self.groupBox_2,self.groupBox_7,self.groupBox_16)
        self.Page1.show() 
        self.Page2.hide()
        self.Page3.hide()

    def change_Page2(self):
        #horizontalLayout_7.replaceWidget(self.groupBox_2,self.groupBox_7,self.groupBox_16)
        self.Page1.hide()
        self.Page2.show() 
        self.Page3.hide()

    def change_Page3(self):
        #horizontalLayout_7.replaceWidget(self.groupBox_2,self.groupBox_7,self.groupBox_16)
        self.Page1.hide()
        self.Page2.hide() 
        self.Page3.show()

       


    
