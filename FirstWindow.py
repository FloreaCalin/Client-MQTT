from PyQt6 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow

class Ui_FirstWindow(object):
    def setupUi(self, FirstWindow):
        FirstWindow.setObjectName("FirstWindow")
        FirstWindow.resize(400, 252)
        self.label = QtWidgets.QLabel(FirstWindow)
        self.label.setGeometry(QtCore.QRect(120, 20, 171, 61))
        font = QtGui.QFont("bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(FirstWindow)
        self.pushButton.setGeometry(QtCore.QRect(40, 200, 141, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(lambda:self.on_createAccount_button_clicked())

        self.pushButton_2 = QtWidgets.QPushButton(FirstWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 200, 141, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(lambda:self.on_logIn_button_clicked())

        self.label_2 = QtWidgets.QLabel(FirstWindow)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 81, 16))
        font = QtGui.QFont("bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(FirstWindow)
        self.lineEdit.setGeometry(QtCore.QRect(120, 100, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(FirstWindow)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 81, 16))
        font = QtGui.QFont("bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(FirstWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 140, 231, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(FirstWindow)
        QtCore.QMetaObject.connectSlotsByName(FirstWindow)

    def retranslateUi(self, FirstWindow):
        _translate = QtCore.QCoreApplication.translate
        FirstWindow.setWindowTitle(_translate("FirstWindow", "MQTT Client"))
        self.label.setText(_translate("FirstWindow", "MQTT Client"))
        self.pushButton.setText(_translate("FirstWindow", "Create Account"))
        self.pushButton_2.setText(_translate("FirstWindow", "Log in"))
        self.label_2.setText(_translate("FirstWindow", "Username"))
        self.label_3.setText(_translate("FirstWindow", "Password "))

    def on_createAccount_button_clicked(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        FirstWindow.hide()
        self.window.show()

    def on_logIn_button_clicked(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        FirstWindow.hide()
        self.window.show()

    def get_username(self):
        username=self.lineEdit.text()
        return username

    def get_password(self):
        password=self.lineEdit_2.text()
        return password

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FirstWindow = QtWidgets.QWidget()
    ui = Ui_FirstWindow()
    ui.setupUi(FirstWindow)
    FirstWindow.show()
    sys.exit(app.exec())
