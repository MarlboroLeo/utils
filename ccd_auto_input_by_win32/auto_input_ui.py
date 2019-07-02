# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auto_input_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BaiduAutoInput(object):
    def setupUi(self, BaiduAutoInput):
        BaiduAutoInput.setObjectName("BaiduAutoInput")
        BaiduAutoInput.resize(392, 207)
        BaiduAutoInput.setWindowOpacity(8.0)
        self.title = QtWidgets.QLabel(BaiduAutoInput)
        self.title.setGeometry(QtCore.QRect(50, 10, 301, 31))
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.title_2 = QtWidgets.QLabel(BaiduAutoInput)
        self.title_2.setGeometry(QtCore.QRect(50, 40, 301, 31))
        self.title_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_2.setObjectName("title_2")
        self.pushButton = QtWidgets.QPushButton(BaiduAutoInput)
        self.pushButton.setGeometry(QtCore.QRect(140, 80, 101, 51))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.title_3 = QtWidgets.QLabel(BaiduAutoInput)
        self.title_3.setGeometry(QtCore.QRect(40, 170, 301, 31))
        self.title_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title_3.setAlignment(QtCore.Qt.AlignCenter)
        self.title_3.setObjectName("title_3")

        self.retranslateUi(BaiduAutoInput)
        QtCore.QMetaObject.connectSlotsByName(BaiduAutoInput)

    def retranslateUi(self, BaiduAutoInput):
        _translate = QtCore.QCoreApplication.translate
        BaiduAutoInput.setWindowTitle(_translate("BaiduAutoInput", "百度自动填写表单"))
        self.title.setText(_translate("BaiduAutoInput", "说明：自动从剪切板中读取数据，并粘贴至网页表单"))
        self.title_2.setText(_translate("BaiduAutoInput", "点击“粘贴”后，需脱离对鼠标键盘的控制"))
        self.pushButton.setText(_translate("BaiduAutoInput", "粘贴"))
        self.title_3.setText(_translate("BaiduAutoInput", "@copyright 2019, 不可用于商业用途"))

