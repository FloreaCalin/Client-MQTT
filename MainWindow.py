import threading

from PyQt6 import QtCore, QtGui, QtWidgets

from Back.client import listOfMessages
from ConnectWindow import Ui_ConnectWindow
from SubscribeWindow import Ui_SubscribeWindow
from UnsubscribeWindow import Ui_UnsubscribeWindow
from OsResources.OsResources import OS_Resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, id, user, password):
        self.__threadForViewMessages = threading.Thread (target = self.write_msg, args = ())
        self.__threadForViewMessages.start()

        self.id = id
        self.user = user
        self.password = password
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 611)
        font = QtGui.QFont("bold")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.frame = QtWidgets.QFrame(MainWindow)
        self.frame.setGeometry(QtCore.QRect(10, 10, 431, 281))
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
        self.label_2.setGeometry(QtCore.QRect(30, 130, 51, 21))
        font = QtGui.QFont("bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 160, 181, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 200, 71, 21))
        font = QtGui.QFont("bold")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 230, 371, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(240, 160, 41, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(240, 130, 51, 21))
        font = QtGui.QFont("bold")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(310, 160, 91, 21))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 90, 251, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 90, 91, 23))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_5.clicked.connect(lambda: self.complete_msg_from_comboBox())

        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 60, 251, 21))
        font = QtGui.QFont("bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.frame_2 = QtWidgets.QFrame(MainWindow)
        self.frame_2.setGeometry(QtCore.QRect(470, 10, 251, 281))
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
        self.pushButton_2.setGeometry(QtCore.QRect(30, 70, 191, 21))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(lambda: self.on_addNewTopicSubscription_button_clicked())

        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 100, 191, 21))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_4.clicked.connect(lambda: self.on_removeATopicSubscription_button_clicked())

        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 160, 191, 91))
        self.textEdit_2.setObjectName("textEdit_2")
        self.frame_3 = QtWidgets.QFrame(MainWindow)
        self.frame_3.setGeometry(QtCore.QRect(190, 320, 531, 281))
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
        self.pushButton_3.setGeometry(QtCore.QRect(50, 430, 81, 51))
        font = QtGui.QFont("bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(lambda: self.on_connect_button_clicked())

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
        self.pushButton_5.setText(_translate("MainWindow", "Choose"))
        self.label_7.setText(_translate("MainWindow", "Choose OS Resource"))
        self.label_5.setText(_translate("MainWindow", "Subscriptions"))
        self.pushButton_2.setText(_translate("MainWindow", "Add New Topic Subscription"))
        self.pushButton_4.setText(_translate("MainWindow", "Remove a Topic Subscription"))
        self.label_6.setText(_translate("MainWindow", "Messages"))
        self.pushButton_3.setText(_translate("MainWindow", "Connect"))

    def on_connect_button_clicked(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_ConnectWindow()
        self.ui.setupUi(self.window, self.id, self.user, self.password)
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

    def write_msg(self):
        while 1:
            while (len (listOfMessages) != 0):
                self.textEdit.append(listOfMessages[0])
                listOfMessages.pop(0)

    def write_topic(self, topic_list):
        for topic in topic_list:
            self.textEdit_2.append(topic)

    def add_elements_to_comboBox(self):
        vector=OS_Resources().get_function_name()
        for fct_name in vector:
            self.comboBox_2.addItem(fct_name)

    def complete_msg_from_comboBox(self):
        fct_name = self.comboBox_2.currentText()

        if(fct_name == "get_cpu_percent"):
            ceva=OS_Resources().get_cpu_percent(1, True)
            ceva1=str(ceva)
            self.lineEdit_2.setText(ceva1)
        elif(fct_name == "get_cpu_times"):
            ceva=OS_Resources().get_cpu_times(False)
            ceva1=str(ceva)
            self.lineEdit_2.setText(ceva1)
        elif (fct_name == "get_cpu_times_percent"):
            ceva = OS_Resources().get_cpu_times_percent(1,False)
            ceva1 = str(ceva)
            self.lineEdit_2.setText(ceva1)
        elif (fct_name == "get_cpu_count"):
            ceva = OS_Resources().get_cpu_count(True)
            ceva1 = str(ceva)
            self.lineEdit_2.setText(ceva1)
        elif (fct_name == "get_cpu_freq"):
            ceva = OS_Resources().get_cpu_freq(False)
            ceva1 = str(ceva)
            self.lineEdit_2.setText(ceva1)
        elif (fct_name == "get_cpu_stats"):
            ceva = OS_Resources().get_cpu_stats()
            ceva1 = str(ceva)
            self.lineEdit_2.setText(ceva1)
        elif (fct_name == "get_load_avg"):
            ceva = OS_Resources().get_load_avg()
            ceva1 = str(ceva)
            self.lineEdit_2.setText(ceva1)
        elif (fct_name == "get_virtual_memory"):
            ceva = OS_Resources().get_virtual_memory()
            ceva1 = str(ceva)
            self.lineEdit_2.setText(ceva1)
        elif (fct_name == "get_swap_memory"):
            ceva = OS_Resources().get_swap_memory()
            ceva1 = str(ceva)
            self.lineEdit_2.setText(ceva1)
        elif (fct_name == "get_disk_partitions"):
            ceva = OS_Resources().get_disk_partitions(True)
            ceva1 = str(ceva)
            self.lineEdit_2.setText(ceva1)
        elif (fct_name == "get_disk_usage"):
            ceva = OS_Resources().get_disk_usage('/')
            ceva1 = str(ceva)
            self.lineEdit_2.setText(ceva1)
        elif (fct_name == "get_disk_io_counters"):
            ceva = OS_Resources().get_disk_io_counters(True, True)
            ceva1 = str(ceva)
            self.lineEdit_2.setText(ceva1)
        elif (fct_name == "get_net_io_counters"):
            ceva = OS_Resources().get_net_io_counters(False, False)
            ceva1 = str(ceva)
            self.lineEdit_2.setText(ceva1)
        elif (fct_name == "get_net_connections"):
            ceva = OS_Resources().get_net_connections('inet')
            ceva1 = str(ceva)
            self.lineEdit_2.setText(ceva1)
        elif (fct_name == "get_sensors_temperatures"):
            ceva = OS_Resources().get_sensors_temperatures(False)
            print(ceva)
            ceva1 = str(ceva)
            self.lineEdit_2.setText(ceva1)
        elif (fct_name == "get_sensors_fans"):
            ceva = OS_Resources().get_sensors_fans()
            ceva1 = str(ceva)
            self.lineEdit_2.setText(ceva1)
        elif (fct_name == "get_sensors_battery"):
            ceva = OS_Resources().get_sensors_battery()
            ceva1 = str(ceva)
            self.lineEdit_2.setText(ceva1)
        elif (fct_name == "get_boot_time"):
            ceva = OS_Resources().get_boot_time()
            ceva1 = str(ceva)
            self.lineEdit_2.setText(ceva1)
        else:
            ceva = OS_Resources().get_users()
            ceva1 = str(ceva)
            self.lineEdit_2.setText(ceva1)

#msg=["Message1","Message2","Message3"]
#topic=["topic1","topic2"]

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.add_elements_to_comboBox()
    MainWindow.show()
    sys.exit(app.exec())
