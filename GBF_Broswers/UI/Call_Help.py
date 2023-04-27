from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Homepage.ui_Help import Ui_Form
from PyQt5.QtCore import pyqtSignal,Qt
import systemdata.icon.ICON


class HelpPageWindow(QWidget,Ui_Form):
    
    returnSignal = pyqtSignal()

    def __init__(self,parent=None):
        super(HelpPageWindow, self).__init__(parent)
        self.setupUi(self)
        self.SetIcon()
        self.ButtonAction()

    def SetIcon(self):
        WindowIcon = QtGui.QIcon()
        WindowIcon.addPixmap(QtGui.QPixmap(":/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(WindowIcon)
    
    def ButtonAction(self):
        self.OKButton.clicked.connect(self.close)