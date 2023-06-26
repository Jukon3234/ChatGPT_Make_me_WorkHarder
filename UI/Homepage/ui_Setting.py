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
        Setting.resize(502, 300)
        self.gridLayout = QtWidgets.QGridLayout(Setting)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(Setting)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.stepspinBox = QtWidgets.QSpinBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepspinBox.sizePolicy().hasHeightForWidth())
        self.stepspinBox.setSizePolicy(sizePolicy)
        self.stepspinBox.setMaximumSize(QtCore.QSize(60, 16777215))
        self.stepspinBox.setMaximum(999999999)
        self.stepspinBox.setObjectName("stepspinBox")
        self.gridLayout_4.addWidget(self.stepspinBox, 0, 1, 1, 2)
        self.RandomXSpin = QtWidgets.QSpinBox(self.groupBox_4)
        self.RandomXSpin.setObjectName("RandomXSpin")
        self.gridLayout_4.addWidget(self.RandomXSpin, 3, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 3, 0, 1, 1)
        self.RandomYSpin = QtWidgets.QSpinBox(self.groupBox_4)
        self.RandomYSpin.setObjectName("RandomYSpin")
        self.gridLayout_4.addWidget(self.RandomYSpin, 3, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 1, 3, 1, 1)
        self.stepdelayran = QtWidgets.QSpinBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepdelayran.sizePolicy().hasHeightForWidth())
        self.stepdelayran.setSizePolicy(sizePolicy)
        self.stepdelayran.setMaximum(90000000)
        self.stepdelayran.setObjectName("stepdelayran")
        self.gridLayout_4.addWidget(self.stepdelayran, 0, 4, 1, 1)
        self.RoundspinBox = QtWidgets.QSpinBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RoundspinBox.sizePolicy().hasHeightForWidth())
        self.RoundspinBox.setSizePolicy(sizePolicy)
        self.RoundspinBox.setMaximumSize(QtCore.QSize(60, 16777215))
        self.RoundspinBox.setMaximum(999999999)
        self.RoundspinBox.setObjectName("RoundspinBox")
        self.gridLayout_4.addWidget(self.RoundspinBox, 1, 1, 1, 2)
        self.CurMoveTime = QtWidgets.QSpinBox(self.groupBox_4)
        self.CurMoveTime.setMaximumSize(QtCore.QSize(60, 16777215))
        self.CurMoveTime.setMaximum(999999)
        self.CurMoveTime.setObjectName("CurMoveTime")
        self.gridLayout_4.addWidget(self.CurMoveTime, 2, 1, 1, 2)
        self.CurMoveTimeRan = QtWidgets.QSpinBox(self.groupBox_4)
        self.CurMoveTimeRan.setMaximum(9999999)
        self.CurMoveTimeRan.setObjectName("CurMoveTimeRan")
        self.gridLayout_4.addWidget(self.CurMoveTimeRan, 2, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 5, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 0, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 1, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 2, 3, 1, 1)
        self.Rounddelayran = QtWidgets.QSpinBox(self.groupBox_4)
        self.Rounddelayran.setMaximum(90000000)
        self.Rounddelayran.setObjectName("Rounddelayran")
        self.gridLayout_4.addWidget(self.Rounddelayran, 1, 4, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 2, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Setting)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.WindowsComboBox = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WindowsComboBox.sizePolicy().hasHeightForWidth())
        self.WindowsComboBox.setSizePolicy(sizePolicy)
        self.WindowsComboBox.setMaximumSize(QtCore.QSize(16777215, 23))
        self.WindowsComboBox.setObjectName("WindowsComboBox")
        self.gridLayout_2.addWidget(self.WindowsComboBox, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 2)
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
        self.gridLayout.addWidget(self.widget, 5, 0, 1, 2)
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
        font.setPointSize(15)
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
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)

        self.retranslateUi(Setting)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "Setting"))
        self.groupBox_4.setTitle(_translate("Setting", "延遲"))
        self.label_18.setText(_translate("Setting", "正負偏移量(X/Y)"))
        self.label_19.setText(_translate("Setting", "+-"))
        self.label_16.setText(_translate("Setting", "+-"))
        self.label_15.setText(_translate("Setting", "點擊間距延遲(ms)"))
        self.label_20.setText(_translate("Setting", "迴圈延遲(ms)"))
        self.label_22.setText(_translate("Setting", "+-"))
        self.label_21.setText(_translate("Setting", "移動時長(ms)"))
        self.groupBox_2.setTitle(_translate("Setting", "視窗"))
        self.label_17.setText(_translate("Setting", "執行視窗選擇"))
        self.OKButton.setText(_translate("Setting", "OK"))
        self.CancelButton.setText(_translate("Setting", "Cancel"))
        self.groupBox.setTitle(_translate("Setting", "Discord BOT 通風報信"))
        self.label_3.setText(_translate("Setting", "建立自己的DC機器人之後，提供機器人的Token以及房號ID填入對應欄位，並按下OK。"))
        self.label.setText(_translate("Setting", "Token"))
        self.label_2.setText(_translate("Setting", "ID"))
