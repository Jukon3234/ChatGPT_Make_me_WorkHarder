from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Homepage.ui_Help import Ui_Form
from PyQt5.QtCore import pyqtSignal,Qt


class HelpPageWindow(QWidget,Ui_Form):
    
    returnSignal = pyqtSignal()

    def __init__(self,parent=None):
        super(HelpPageWindow, self).__init__(parent)
        self.setupUi(self)
        self.ButtonAction()
    
    def ButtonAction(self):
        self.OKButton.clicked.connect(self.close)