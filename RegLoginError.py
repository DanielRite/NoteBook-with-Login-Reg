from PyQt5 import QtCore, QtGui, QtWidgets


class RegLogError(object):
    def rle(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(196, 159)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, -20, 165, 117))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 165, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.OkRegLoginError = QtWidgets.QPushButton(Dialog)
        self.OkRegLoginError.setGeometry(QtCore.QRect(50, 120, 75, 23))
        self.OkRegLoginError.setObjectName("OkRegLoginError")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ОШИБКА"))
        self.label_2.setText(_translate("Dialog", "Логин занят!"))
        self.OkRegLoginError.setText(_translate("Dialog", "OK"))
