from PyQt6 import QtCore, QtGui, QtWidgets

subscriptions_list=[]

class Ui_SubscribeWindow(object):
    def setupUi(self, SubscribeWindow, client):

        self.client=client

        SubscribeWindow.setObjectName("SubscribeWindow")
        SubscribeWindow.resize(341, 195)
        self.label = QtWidgets.QLabel(SubscribeWindow)
        self.label.setGeometry(QtCore.QRect(80, 20, 191, 41))
        font = QtGui.QFont("bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(SubscribeWindow)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 41, 16))
        font = QtGui.QFont("bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(SubscribeWindow)
        self.lineEdit.setGeometry(QtCore.QRect(70, 90, 251, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(SubscribeWindow)
        self.comboBox.setGeometry(QtCore.QRect(70, 150, 51, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(SubscribeWindow)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 47, 13))
        font = QtGui.QFont("bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(SubscribeWindow)
        self.pushButton.setGeometry(QtCore.QRect(160, 150, 161, 21))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(lambda: self.on_subscribe_button())

        self.retranslateUi(SubscribeWindow)
        QtCore.QMetaObject.connectSlotsByName(SubscribeWindow)

    def retranslateUi(self, SubscribeWindow):
        _translate = QtCore.QCoreApplication.translate
        SubscribeWindow.setWindowTitle(_translate("SubscribeWindow", "MQTT Client"))
        self.label.setText(_translate("SubscribeWindow", "Subscription"))
        self.label_2.setText(_translate("SubscribeWindow", "Topic"))
        self.comboBox.setItemText(0, _translate("SubscribeWindow", "0"))
        self.comboBox.setItemText(1, _translate("SubscribeWindow", "1"))
        self.comboBox.setItemText(2, _translate("SubscribeWindow", "2"))
        self.label_3.setText(_translate("SubscribeWindow", "QoS"))
        self.pushButton.setText(_translate("SubscribeWindow", "Subscribe"))

    def get_topic(self):
        topic = self.lineEdit.text()
        return topic

    def get_qos(self):
        qos=self.comboBox.currentText()
        return qos

    def on_subscribe_button(self):
        topic=self.get_topic()
        qos=self.get_qos()
        subscriptions_list.append('topic: ' + topic +'\nQoS: ' + qos)
        self.client.subscribe([topic],[int(qos)])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SubscribeWindow = QtWidgets.QWidget()
    ui = Ui_SubscribeWindow()
    ui.setupUi(SubscribeWindow)
    SubscribeWindow.show()
    sys.exit(app.exec())
