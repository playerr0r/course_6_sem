# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TaskWindow(object):
    def setupUi(self, TaskWindow):
        TaskWindow.setObjectName("TaskWindow")
        TaskWindow.resize(688, 466)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TaskWindow.sizePolicy().hasHeightForWidth())
        TaskWindow.setSizePolicy(sizePolicy)
        TaskWindow.setMinimumSize(QtCore.QSize(688, 466))
        TaskWindow.setMaximumSize(QtCore.QSize(688, 466))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        TaskWindow.setFont(font)
        TaskWindow.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.task_num = QtWidgets.QLabel(TaskWindow)
        self.task_num.setGeometry(QtCore.QRect(20, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.task_num.setFont(font)
        self.task_num.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.task_num.setObjectName("task_num")
        self.task_name = QtWidgets.QLabel(TaskWindow)
        self.task_name.setGeometry(QtCore.QRect(20, 80, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.task_name.setFont(font)
        self.task_name.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.task_name.setObjectName("task_name")
        self.task_desc = QtWidgets.QLabel(TaskWindow)
        self.task_desc.setGeometry(QtCore.QRect(20, 150, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.task_desc.setFont(font)
        self.task_desc.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.task_desc.setObjectName("task_desc")
        self.task_num2 = QtWidgets.QLabel(TaskWindow)
        self.task_num2.setGeometry(QtCore.QRect(100, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.task_num2.setFont(font)
        self.task_num2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.task_num2.setObjectName("task_num2")
        self.task_name2 = QtWidgets.QLabel(TaskWindow)
        self.task_name2.setGeometry(QtCore.QRect(120, 80, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.task_name2.setFont(font)
        self.task_name2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.task_name2.setObjectName("task_name2")
        self.task_desc2 = QtWidgets.QLabel(TaskWindow)
        self.task_desc2.setGeometry(QtCore.QRect(160, 130, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.task_desc2.setFont(font)
        self.task_desc2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.task_desc2.setWordWrap(True)
        self.task_desc2.setObjectName("task_desc2")
        self.complete_button = QtWidgets.QPushButton(TaskWindow)
        self.complete_button.setGeometry(QtCore.QRect(550, 420, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.complete_button.setFont(font)
        self.complete_button.setStyleSheet("background-color: rgb(131, 180, 255);\n"
"border-radius: 9px;")
        self.complete_button.setObjectName("complete_button")
        self.ok_button = QtWidgets.QPushButton(TaskWindow)
        self.ok_button.setGeometry(QtCore.QRect(20, 420, 109, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ok_button.setFont(font)
        self.ok_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 9px;")
        self.ok_button.setFlat(True)
        self.ok_button.setObjectName("ok_button")
        self.widget = QtWidgets.QWidget(TaskWindow)
        self.widget.setGeometry(QtCore.QRect(-10, 0, 741, 61))
        self.widget.setStyleSheet("background-color: rgb(24, 54, 112);")
        self.widget.setObjectName("widget")
        self.date_to_complete = QtWidgets.QLabel(TaskWindow)
        self.date_to_complete.setGeometry(QtCore.QRect(20, 220, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.date_to_complete.setFont(font)
        self.date_to_complete.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.date_to_complete.setObjectName("date_to_complete")
        self.date_to_complete2 = QtWidgets.QLabel(TaskWindow)
        self.date_to_complete2.setGeometry(QtCore.QRect(160, 220, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.date_to_complete2.setFont(font)
        self.date_to_complete2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.date_to_complete2.setObjectName("date_to_complete2")
        self.new_report = QtWidgets.QLabel(TaskWindow)
        self.new_report.setGeometry(QtCore.QRect(380, 80, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.new_report.setFont(font)
        self.new_report.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.new_report.setObjectName("new_report")
        self.new_report_input = QtWidgets.QLineEdit(TaskWindow)
        self.new_report_input.setGeometry(QtCore.QRect(380, 130, 281, 241))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.new_report_input.setFont(font)
        self.new_report_input.setStyleSheet("border: 1px;\n"
"border-color: rgb(119, 119, 119);\n"
"border-style: outset;\n"
"border-radius: 8px;")
        self.new_report_input.setText("")
        self.new_report_input.setObjectName("new_report_input")
        self.status = QtWidgets.QLabel(TaskWindow)
        self.status.setGeometry(QtCore.QRect(20, 290, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.status.setFont(font)
        self.status.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.status.setObjectName("status")
        self.status2 = QtWidgets.QLabel(TaskWindow)
        self.status2.setGeometry(QtCore.QRect(110, 290, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.status2.setFont(font)
        self.status2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.status2.setObjectName("status2")
        self.complete_button_2 = QtWidgets.QPushButton(TaskWindow)
        self.complete_button_2.setGeometry(QtCore.QRect(420, 420, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.complete_button_2.setFont(font)
        self.complete_button_2.setStyleSheet("border-radius: 9px;\n"
"background-color: rgb(255, 255, 255);")
        self.complete_button_2.setObjectName("complete_button_2")
        self.report_button = QtWidgets.QPushButton(TaskWindow)
        self.report_button.setGeometry(QtCore.QRect(560, 380, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.report_button.setFont(font)
        self.report_button.setStyleSheet("border-radius: 9px;\n"
"background-color: rgb(255, 255, 255);")
        self.report_button.setObjectName("report_button")
        self.complete_button.raise_()
        self.task_name.raise_()
        self.task_desc.raise_()
        self.task_name2.raise_()
        self.task_desc2.raise_()
        self.ok_button.raise_()
        self.widget.raise_()
        self.task_num.raise_()
        self.task_num2.raise_()
        self.date_to_complete.raise_()
        self.date_to_complete2.raise_()
        self.new_report.raise_()
        self.new_report_input.raise_()
        self.status.raise_()
        self.status2.raise_()
        self.complete_button_2.raise_()
        self.report_button.raise_()

        self.retranslateUi(TaskWindow)
        QtCore.QMetaObject.connectSlotsByName(TaskWindow)

    def retranslateUi(self, TaskWindow):
        _translate = QtCore.QCoreApplication.translate
        TaskWindow.setWindowTitle(_translate("TaskWindow", "Task window"))
        self.task_num.setText(_translate("TaskWindow", "Task #"))
        self.task_name.setText(_translate("TaskWindow", "Task name"))
        self.task_desc.setText(_translate("TaskWindow", "Task description"))
        self.task_num2.setText(_translate("TaskWindow", "#"))
        self.task_name2.setText(_translate("TaskWindow", "Task name"))
        self.task_desc2.setText(_translate("TaskWindow", "Task description"))
        self.complete_button.setText(_translate("TaskWindow", "Task completed"))
        self.ok_button.setText(_translate("TaskWindow", "OK"))
        self.date_to_complete.setText(_translate("TaskWindow", "Date to complete"))
        self.date_to_complete2.setText(_translate("TaskWindow", "Date to complete"))
        self.new_report.setText(_translate("TaskWindow", "New report"))
        self.status.setText(_translate("TaskWindow", "Status"))
        self.status2.setText(_translate("TaskWindow", "Status"))
        self.complete_button_2.setText(_translate("TaskWindow", "Decrease status"))
        self.report_button.setText(_translate("TaskWindow", "Send report"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TaskWindow = QtWidgets.QDialog()
    ui = Ui_TaskWindow()
    ui.setupUi(TaskWindow)
    TaskWindow.show()
    sys.exit(app.exec_())
