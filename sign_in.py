# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_in.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignIn(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1091, 711)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(1091, 711))
        Dialog.setMaximumSize(QtCore.QSize(1091, 711))
        Dialog.setStyleSheet("")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1091, 711))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.511, y2:0, stop:0 rgba(155, 189, 255, 255), stop:0.664773 rgba(254, 255, 255, 255));")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(350, 80, 421, 531))
        self.widget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.widget_2.setFont(font)
        self.widget_2.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"border-radius: 20px;")
        self.widget_2.setObjectName("widget_2")
        self.login_input = QtWidgets.QLineEdit(self.widget_2)
        self.login_input.setGeometry(QtCore.QRect(70, 80, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.login_input.setFont(font)
        self.login_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px;\n"
"border-color: rgb(119, 119, 119);\n"
"border-style: outset;\n"
"border-radius: 8px;")
        self.login_input.setText("")
        self.login_input.setObjectName("login_input")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(70, 40, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(70, 230, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.signin_button = QtWidgets.QPushButton(self.widget_2)
        self.signin_button.setGeometry(QtCore.QRect(130, 440, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.signin_button.setFont(font)
        self.signin_button.setStyleSheet("background-color: rgb(24, 54, 112);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.signin_button.setObjectName("signin_button")
        self.name_input = QtWidgets.QLineEdit(self.widget_2)
        self.name_input.setGeometry(QtCore.QRect(70, 270, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.name_input.setFont(font)
        self.name_input.setStyleSheet("border: 1px;\n"
"border-color: rgb(119, 119, 119);\n"
"border-style: outset;\n"
"border-radius: 8px;\n"
"background-color: rgb(255, 255, 255);")
        self.name_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.name_input.setObjectName("name_input")
        self.empl_code_input = QtWidgets.QLineEdit(self.widget_2)
        self.empl_code_input.setGeometry(QtCore.QRect(70, 370, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.empl_code_input.setFont(font)
        self.empl_code_input.setStyleSheet("border: 1px;\n"
"border-color: rgb(119, 119, 119);\n"
"border-style: outset;\n"
"border-radius: 8px;\n"
"background-color: rgb(255, 255, 255);")
        self.empl_code_input.setObjectName("empl_code_input")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(70, 330, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(70, 130, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.pass_input_2 = QtWidgets.QLineEdit(self.widget_2)
        self.pass_input_2.setGeometry(QtCore.QRect(70, 170, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.pass_input_2.setFont(font)
        self.pass_input_2.setStyleSheet("border: 1px;\n"
"border-color: rgb(119, 119, 119);\n"
"border-style: outset;\n"
"border-radius: 8px;\n"
"background-color: rgb(255, 255, 255);")
        self.pass_input_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_input_2.setObjectName("pass_input_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Login"))
        self.label_4.setText(_translate("Dialog", "Full name"))
        self.signin_button.setText(_translate("Dialog", "Sign in"))
        self.label_5.setText(_translate("Dialog", "Employee code"))
        self.label_6.setText(_translate("Dialog", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_SignIn()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())