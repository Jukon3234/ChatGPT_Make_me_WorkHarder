# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\temp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Data(object):
    def setupUi(self, Data):
        Data.setObjectName("Data")
        Data.resize(415, 348)
        self.gridLayout = QtWidgets.QGridLayout(Data)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Data)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Data)
        QtCore.QMetaObject.connectSlotsByName(Data)

    def retranslateUi(self, Data):
        _translate = QtCore.QCoreApplication.translate
        Data.setWindowTitle(_translate("Data", "Form"))
