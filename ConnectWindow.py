from PyQt6 import QtCore, QtGui, QtWidgets

from Back.client import getConnectResponse, Client

class Ui_ConnectWindow(object):
    def setupUi(self, ConnectWindow, id, user, password):
        self.id = id
        self.user = user
        self.password = password
        ConnectWindow.setObjectName("ConnectWindow")
        ConnectWindow.resize(337, 445)
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
        self.pushButton.setGeometry(QtCore.QRect(80, 400, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(ConnectWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 400, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(ConnectWindow)
        self.label_3.setGeometry(QtCore.QRect(110, 10, 121, 51))
        font = QtGui.QFont("bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ConnectWindow)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 111, 21))
        font = QtGui.QFont("bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(ConnectWindow)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 240, 181, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(ConnectWindow)
        self.label_7.setGeometry(QtCore.QRect(10, 280, 91, 21))
        font = QtGui.QFont("bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(ConnectWindow)
        self.comboBox.setGeometry(QtCore.QRect(140, 280, 41, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_8 = QtWidgets.QLabel(ConnectWindow)
        self.label_8.setGeometry(QtCore.QRect(10, 320, 91, 21))
        font = QtGui.QFont("bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.checkBox = QtWidgets.QCheckBox(ConnectWindow)
        self.checkBox.setGeometry(QtCore.QRect(140, 320, 51, 21))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.label_9 = QtWidgets.QLabel(ConnectWindow)
        self.label_9.setGeometry(QtCore.QRect(10, 360, 91, 21))
        font = QtGui.QFont("bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.checkBox_2 = QtWidgets.QCheckBox(ConnectWindow)
        self.checkBox_2.setGeometry(QtCore.QRect(140, 360, 51, 21))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.textEdit = QtWidgets.QTextEdit(ConnectWindow)
        self.textEdit.setGeometry(QtCore.QRect(170, 320, 151, 61))


        self.textEdit.setObjectName("textEdit")

        self.pushButton.clicked.connect(lambda:self.insert_text())

        self.pushButton_2.clicked.connect(lambda:self.on_disconnect_button_clicked())

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
        self.label_4.setText(_translate("ConnectWindow", "Last Will Topic"))
        self.label_7.setText(_translate("ConnectWindow", "Last Will QoS"))
        self.comboBox.setItemText(0, _translate("ConnectWindow", "0"))
        self.comboBox.setItemText(1, _translate("ConnectWindow", "1"))
        self.comboBox.setItemText(2, _translate("ConnectWindow", "2"))
        self.label_8.setText(_translate("ConnectWindow", "Clean Session"))
        self.label_9.setText(_translate("ConnectWindow", "Last Will Retain"))

    def get_host(self):
        host = self.lineEdit.text()
        return host

    def get_port(self):
        port = self.lineEdit_2.text()
        return port

    def get_keep_alive(self):
        keep_alive = self.lineEdit_5.text()
        return keep_alive

    def get_last_will_message(self):
        last_will_message = self.lineEdit_6.text()
        return last_will_message

    def get_last_will_topic(self):
        last_will_topic = self.lineEdit_3.text()
        return last_will_topic

    def get_last_will_qos(self):
        last_will_qos = self.comboBox.currentText()
        return last_will_qos

    def get_clean_session(self):
        clean_session=self.checkBox.isChecked()
        return clean_session

    def get_last_will_retain(self):
        last_will_retain=self.checkBox_2.isChecked()
        return last_will_retain

    def insert_text(self):
        host = self.get_host()
        port = int(self.get_port())
        keepAlive = int (self.get_keep_alive())
        lastWillMessage = self.get_last_will_message()
        lastWillTopic = self.get_last_will_topic()
        lastWillQos = int (self.get_last_will_qos())
        cleanSession = self.get_clean_session()
        lastWillRetain = self.get_last_will_retain()

        if lastWillMessage == '' or lastWillTopic == '':
            lastWillMessage = None
            lastWillTopic = None
            lastWillQos = None

        if cleanSession == False:
            cleanSession = None

        if lastWillRetain == False:
            lastWillRetain = None

        client = Client (self.id, self.user, self.password)
        client.connect (host, port, keepAlive, cleanSession, lastWillTopic, lastWillMessage,
                         lastWillQos, lastWillRetain)

        client.subscribe(['testtopic/foarte/interesant/poate/merge/#'], [2])

        self.textEdit.setText(getConnectResponse ())

    def on_disconnect_button_clicked(self):
        msg="Disconnected"
        self.textEdit.setText(msg)


connection_msg = "Connection accepted"

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConnectWindow = QtWidgets.QWidget()
    ui = Ui_ConnectWindow()
    ui.setupUi(ConnectWindow)
    ConnectWindow.show()
    sys.exit(app.exec())
