from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ConnectWindow(object):
    def setupUi(self, ConnectWindow):
        ConnectWindow.setObjectName("ConnectWindow")
        ConnectWindow.resize(337, 293)
        self.label = QtWidgets.QLabel(ConnectWindow)
        self.label.setGeometry(QtCore.QRect(10, 80, 61, 21))
        font = QtGui.QFont("bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(ConnectWindow)
        self.lineEdit.setGeometry(QtCore.QRect(140, 80, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(ConnectWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 120, 181, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(ConnectWindow)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 61, 21))
        font = QtGui.QFont("bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(ConnectWindow)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 160, 181, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(ConnectWindow)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 81, 21))
        font = QtGui.QFont("bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(ConnectWindow)
        self.lineEdit_6.setGeometry(QtCore.QRect(140, 200, 181, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_6 = QtWidgets.QLabel(ConnectWindow)
        self.label_6.setGeometry(QtCore.QRect(10, 190, 121, 41))
        font = QtGui.QFont("bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(ConnectWindow)
        self.pushButton.setGeometry(QtCore.QRect(80, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(ConnectWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 250, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(ConnectWindow)
        self.label_3.setGeometry(QtCore.QRect(110, 10, 121, 51))
        font = QtGui.QFont("bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(ConnectWindow)
        QtCore.QMetaObject.connectSlotsByName(ConnectWindow)

    def retranslateUi(self, ConnectWindow):
        _translate = QtCore.QCoreApplication.translate
        ConnectWindow.setWindowTitle(_translate("ConnectWindow", "MQTT Client"))
        self.label.setText(_translate("ConnectWindow", "Host"))
        self.label_2.setText(_translate("ConnectWindow", "Port"))
        self.label_5.setText(_translate("ConnectWindow", "KeepAlive"))
        self.label_6.setText(_translate("ConnectWindow", "Last Will Message"))
        self.pushButton.setText(_translate("ConnectWindow", "Connect"))
        self.pushButton_2.setText(_translate("ConnectWindow", "Disconnect"))
        self.label_3.setText(_translate("ConnectWindow", "Connect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConnectWindow = QtWidgets.QWidget()
    ui = Ui_ConnectWindow()
    ui.setupUi(ConnectWindow)
    ConnectWindow.show()
    sys.exit(app.exec())