from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Homepage.ui_Help import Ui_Form
from PyQt5.QtCore import pyqtSignal,Qt


class HelpPageWindow(QtWidgets.QMainWindow,Ui_Form):
    
    returnSignal = pyqtSignal()

    def __init__(self,parent=None):
        super(HelpPageWindow, self).__init__(parent)
        self.setupUi(self)
        #self.initUI()

   # def initUI(self):
   #     self.setLayout(self.gridLayout)
   #     self.returnButton.clicked.connect(self.returnSignal)
      