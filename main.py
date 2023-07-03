from PyQt5.QtWidgets import *
from UI.Call_MainUi import MainPageWindow
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainPageWindow()
    mainWindow.show()
    sys.exit(app.exec_())