# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Reg(object):
    def regist(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(525, 205)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 481, 105))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.loginReg = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.loginReg.setFont(font)
        self.loginReg.setObjectName("loginReg")
        self.verticalLayout.addWidget(self.loginReg)
        self.passwordReg = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordReg.setFont(font)
        self.passwordReg.setObjectName("passwordReg")
        self.verticalLayout.addWidget(self.passwordReg)
        self.passwordReg_2 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordReg_2.setFont(font)
        self.passwordReg_2.setObjectName("passwordReg_2")
        self.verticalLayout.addWidget(self.passwordReg_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(250, 160, 230, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(40)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.RegPushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.RegPushButton.setObjectName("RegPushButton")
        self.horizontalLayout_3.addWidget(self.RegPushButton)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Логин:"))
        self.label_3.setText(_translate("Dialog", "Пароль: "))
        self.label_4.setText(_translate("Dialog", "Подтвердите пароль: "))
        self.RegPushButton.setText(_translate("Dialog", "Зарегестрироваться"))
        self.pushButton.setText(_translate("Dialog", "ОТМЕНА"))
