# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileList.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class FilList(object):
    def FileL(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(375, 127)
        self.Files = QtWidgets.QComboBox(Dialog)
        self.Files.setGeometry(QtCore.QRect(20, 50, 211, 22))
        self.Files.setObjectName("Files")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 141, 16))
        self.label.setObjectName("label")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Список Файлов"))
