# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PasswordError.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class PasError(object):
    def pe(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(633, 159)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 0, 165, 42))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 611, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.OkRegPasswordError = QtWidgets.QPushButton(Dialog)
        self.OkRegPasswordError.setGeometry(QtCore.QRect(270, 120, 75, 23))
        self.OkRegPasswordError.setObjectName("OkRegPasswordError")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ОШИБКА"))
        self.label_2.setText(_translate("Dialog", "Пароли не совпадают!"))
        self.OkRegPasswordError.setText(_translate("Dialog", "OK"))
