# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(609, 228)
        self.gridLayout = QtWidgets.QGridLayout(Setting)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Setting)
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(60, 36))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.DC_TOKEN = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DC_TOKEN.sizePolicy().hasHeightForWidth())
        self.DC_TOKEN.setSizePolicy(sizePolicy)
        self.DC_TOKEN.setMaximumSize(QtCore.QSize(16777215, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DC_TOKEN.setFont(font)
        self.DC_TOKEN.setText("")
        self.DC_TOKEN.setObjectName("DC_TOKEN")
        self.horizontalLayout_3.addWidget(self.DC_TOKEN)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMaximumSize(QtCore.QSize(60, 36))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.DC_CHID = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DC_CHID.sizePolicy().hasHeightForWidth())
        self.DC_CHID.setSizePolicy(sizePolicy)
        self.DC_CHID.setMaximumSize(QtCore.QSize(16777215, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DC_CHID.setFont(font)
        self.DC_CHID.setObjectName("DC_CHID")
        self.horizontalLayout_2.addWidget(self.DC_CHID)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(Setting)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.OKButton = QtWidgets.QPushButton(self.widget)
        self.OKButton.setMaximumSize(QtCore.QSize(123, 27))
        self.OKButton.setObjectName("OKButton")
        self.horizontalLayout.addWidget(self.OKButton)
        self.CancelButton = QtWidgets.QPushButton(self.widget)
        self.CancelButton.setMaximumSize(QtCore.QSize(123, 27))
        self.CancelButton.setObjectName("CancelButton")
        self.horizontalLayout.addWidget(self.CancelButton)
        self.gridLayout.addWidget(self.widget, 2, 0, 1, 1)

        self.retranslateUi(Setting)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "Form"))
        self.groupBox.setTitle(_translate("Setting", "Discord BOT 通風報信"))
        self.label_3.setText(_translate("Setting", "建立自己的DC機器人之後，提供機器人的Token以及房號ID填入對應欄位。"))
        self.label.setText(_translate("Setting", "Token"))
        self.label_2.setText(_translate("Setting", "ID"))
        self.OKButton.setText(_translate("Setting", "OK"))
        self.CancelButton.setText(_translate("Setting", "Cancel"))
