# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import random
import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTextEdit, QLineEdit
from PyQt5.QtCore import Qt, QTimer


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 700))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fon = QtWidgets.QLabel(self.centralwidget)
        self.fon.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.fon.setStyleSheet("background-color: rgba(44, 43, 43, 1);")
        self.fon.setText("")
        self.fon.setObjectName("fon")
        self.test_label = QtWidgets.QLabel(self.centralwidget)
        self.test_label.setGeometry(QtCore.QRect(270, 200, 491, 78))
        self.test_label.setStyleSheet("font: 64px \"Impact\";\n"
"color: rgba(167, 169, 169, 1);")
        self.test_label.setObjectName("test_label")
        self.btn_n = QtWidgets.QPushButton(self.centralwidget)
        self.btn_n.setGeometry(QtCore.QRect(374, 350, 251, 71))
        self.btn_n.setStyleSheet("background-color: rgba(164, 164, 164, 1);\n"
"color: rgba(31, 90, 29, 1);\n"
"font: 36px \"Impact\";\n"
"border-radius: 35px;")
        self.btn_n.setObjectName("btn_n")
        self.btn_leave = QtWidgets.QPushButton(self.centralwidget)
        self.btn_leave.setGeometry(QtCore.QRect(374, 435, 251, 71))
        self.btn_leave.setStyleSheet("background-color: rgba(164, 164, 164, 1);\n"
"color: rgba(114, 20, 20, 1);\n"
"font: 36px \"Impact\";\n"
"border-radius: 35px;")
        self.btn_leave.setObjectName("btn_leave")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тест. Личностная готовность к риску (Шуберт)."))
        self.test_label.setText(_translate("MainWindow", "Android test game"))
        self.btn_n.setText(_translate("MainWindow", "Играть"))
        self.btn_leave.setText(_translate("MainWindow", "Выход"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
