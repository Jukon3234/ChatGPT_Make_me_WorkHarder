from PyQt5.QtWidgets import *
from gbfBroswersWindow import WebPageWindow
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gbfBroswers = WebPageWindow()
    gbfBroswers.show()
    sys.exit(app.exec_())