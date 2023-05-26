# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1091, 709)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(1091, 709))
        Dialog.setMaximumSize(QtCore.QSize(1091, 709))
        Dialog.setStyleSheet("")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(610, -1, 481, 711))
        self.widget.setStyleSheet("background-color: rgb(24, 54, 112);")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(30, 29, 421, 651))
        self.widget_2.setMinimumSize(QtCore.QSize(421, 651))
        self.widget_2.setMaximumSize(QtCore.QSize(421, 651))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.widget_2.setFont(font)
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.widget_2.setObjectName("widget_2")
        self.login_input = QtWidgets.QLineEdit(self.widget_2)
        self.login_input.setGeometry(QtCore.QRect(70, 210, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.login_input.setFont(font)
        self.login_input.setStyleSheet("border: 1px;\n"
"border-color: rgb(119, 119, 119);\n"
"border-style: outset;\n"
"border-radius: 8px;")
        self.login_input.setText("")
        self.login_input.setObjectName("login_input")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(70, 170, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(70, 280, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.login_button = QtWidgets.QPushButton(self.widget_2)
        self.login_button.setGeometry(QtCore.QRect(130, 412, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("background-color: rgb(24, 54, 112);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.login_button.setObjectName("login_button")
        self.create_acc_button = QtWidgets.QPushButton(self.widget_2)
        self.create_acc_button.setGeometry(QtCore.QRect(130, 450, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setUnderline(True)
        self.create_acc_button.setFont(font)
        self.create_acc_button.setStyleSheet("color: rgb(119, 119, 119);")
        self.create_acc_button.setObjectName("create_acc_button")
        self.pass_input = QtWidgets.QLineEdit(self.widget_2)
        self.pass_input.setGeometry(QtCore.QRect(70, 320, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.pass_input.setFont(font)
        self.pass_input.setStyleSheet("border: 1px;\n"
"border-color: rgb(119, 119, 119);\n"
"border-style: outset;\n"
"border-radius: 8px;")
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_input.setObjectName("pass_input")
        self.widget_3 = QtWidgets.QWidget(Dialog)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 751, 711))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(751, 711))
        self.widget_3.setMaximumSize(QtCore.QSize(751, 711))
        self.widget_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 186, 255, 255), stop:1 rgba(255, 255, 254, 255));\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setGeometry(QtCore.QRect(580, -20, 5, 850))
        self.widget_4.setStyleSheet("background-color: rgb(24, 54, 112);")
        self.widget_4.setObjectName("widget_4")
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setGeometry(QtCore.QRect(520, 390, 5, 351))
        self.widget_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_5.setObjectName("widget_5")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setGeometry(QtCore.QRect(70, 210, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(70, 270, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 652, 35, 25))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget_3.raise_()
        self.widget.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Login"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.login_button.setText(_translate("Dialog", "Log in"))
        self.create_acc_button.setText(_translate("Dialog", "Create account"))
        self.label.setText(_translate("Dialog", "Just On Time"))
        self.label_2.setText(_translate("Dialog", "Welcome to timezone"))
        self.pushButton_3.setText(_translate("Dialog", "RU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())