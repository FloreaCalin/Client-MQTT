from PyQt6 import QtCore, QtGui, QtWidgets
from ConnectWindow import Ui_ConnectWindow
from SubscribeWindow import Ui_SubscribeWindow
from UnsubscribeWindow import Ui_UnsubscribeWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 532)
        font = QtGui.QFont("bold")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.frame = QtWidgets.QFrame(MainWindow)
        self.frame.setGeometry(QtCore.QRect(10, 10, 431, 211))
        font = QtGui.QFont("bold")
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setStyleSheet("#frame { border: 1px solid lightGray; }")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 10, 91, 41))
        font = QtGui.QFont("bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 51, 21))
        font = QtGui.QFont("bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 90, 181, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 71, 21))
        font = QtGui.QFont("bold")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 160, 371, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(240, 90, 41, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(240, 60, 51, 21))
        font = QtGui.QFont("bold")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(310, 90, 91, 21))
        self.pushButton.setObjectName("pushButton")
        self.frame_2 = QtWidgets.QFrame(MainWindow)
        self.frame_2.setGeometry(QtCore.QRect(470, 10, 251, 211))
        self.frame_2.setStyleSheet("#frame_2 { border: 1px solid lightGray; }")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(30, 0, 151, 51))
        font = QtGui.QFont("bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 60, 191, 21))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(lambda:self.on_addNewTopicSubscription_button_clicked())

        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 90, 191, 21))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_4.clicked.connect(lambda:self.on_removeATopicSubscription_button_clicked())

        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 120, 191, 81))
        self.textEdit_2.setObjectName("textEdit_2")
        self.frame_3 = QtWidgets.QFrame(MainWindow)
        self.frame_3.setGeometry(QtCore.QRect(190, 240, 531, 281))
        self.frame_3.setStyleSheet("#frame_3 { border: 1px solid lightGray; }")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(30, 10, 111, 41))
        font = QtGui.QFont("bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit.setGeometry(QtCore.QRect(30, 60, 471, 191))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_3 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 350, 81, 51))
        font = QtGui.QFont("bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(lambda:self.on_connect_button_clicked())
        #self.pushButton_3.clicked.connect(lambda:self.write_msg(msg))
        #self.pushButton_3.clicked.connect(lambda:self.write_topic(topic))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MQTT Client"))
        self.label.setText(_translate("MainWindow", "Publish"))
        self.label_2.setText(_translate("MainWindow", "Topic"))
        self.label_3.setText(_translate("MainWindow", "Message"))
        self.comboBox.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "2"))
        self.label_4.setText(_translate("MainWindow", "QoS"))
        self.pushButton.setText(_translate("MainWindow", "Publish"))
        self.label_5.setText(_translate("MainWindow", "Subscriptions"))
        self.pushButton_2.setText(_translate("MainWindow", "Add New Topic Subscription"))
        self.pushButton_4.setText(_translate("MainWindow", "Remove a Topic Subscription"))
        self.label_6.setText(_translate("MainWindow", "Messages"))
        self.pushButton_3.setText(_translate("MainWindow", "Connect"))

    def on_connect_button_clicked(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_ConnectWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def on_addNewTopicSubscription_button_clicked(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_SubscribeWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def on_removeATopicSubscription_button_clicked(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_UnsubscribeWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def get_topic(self):
        topic = self.lineEdit.text()
        return topic

    def get_message(self):
        message = self.lineEdit_2.text()
        return message

    def get_qos(self):
        qos = self.comboBox.currentText()
        return qos

    def write_msg(self, msg_list):
        for msg in msg_list:
            self.textEdit.append(msg)

    def write_topic(self, topic_list):
        for topic in topic_list:
            self.textEdit_2.append(topic)

#msg=["Message1","Message2","Message3"]
#topic=["topic1","topic2"]

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
