# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetFileName.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class SetFName(object):
    def sfname(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 163)
        self.FileNameText = QtWidgets.QLineEdit(Dialog)
        self.FileNameText.setGeometry(QtCore.QRect(90, 60, 131, 20))
        self.FileNameText.setObjectName("FileNameText")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
