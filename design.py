# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prooogekt227.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("BTC BALANCE CHECKER")
        Dialog.resize(802, 539)
        Dialog.setStyleSheet("background-color: rgb(12, 24, 41);\n"
"background-color: rgb(30, 60, 102);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 351, 21))
        self.label.setStyleSheet("color: rgb(158, 203, 247);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 434, 181, 21))
        self.label_3.setStyleSheet("color: rgb(158, 203, 247);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 462, 631, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setStyleSheet("color: rgb(158, 203, 247);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    background-color: rgb(158, 203, 247);\n"
"    background: #0000; \n"
"    color: #000;\n"
"    padding: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QComboBox:hover {\n"
"    background: silver; \n"
"}\n"
"QComboBox:pressed {\n"
"    background: dark;\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setStyleSheet("color: rgb(158, 203, 247);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setStyleSheet("color: rgb(158, 203, 247);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background: #9ECBF7; \n"
"    color: #0C1829;\n"
"    padding: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"    background: silver; \n"
"}\n"
"QPushButton:pressed {\n"
"    background: dark;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(310, 60, 481, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setStyleSheet("color: rgb(158, 203, 247);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setStyleSheet("color: rgb(158, 203, 247);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setStyleSheet("color: rgb(158, 203, 247);")
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setStyleSheet("color: rgb(158, 203, 247);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 271, 40))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setStyleSheet("color: rgb(158, 203, 247);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    background-color: rgb(158, 203, 247);\n"
"    background: #0000; \n"
"    color: #000;\n"
"    padding: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QComboBox:hover {\n"
"    background: silver; \n"
"}\n"
"QComboBox:pressed {\n"
"    background: dark;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background: #9ECBF7; \n"
"    color: #0C1829;\n"
"    padding: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"    background: silver; \n"
"}\n"
"QPushButton:pressed {\n"
"    background: dark;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(680, 469, 111, 51))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background: #9ECBF7; \n"
"    color: #0C1829;\n"
"    padding: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"    background: silver; \n"
"}\n"
"QPushButton:pressed {\n"
"    background: dark;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(70, 90, 151, 16))
        self.label_10.setStyleSheet("color: rgb(158, 203, 247);")
        self.label_10.setObjectName("label_10")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(60, 120, 164, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_12.setStyleSheet("color: rgb(158, 203, 247);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setStyleSheet("color: rgb(158, 203, 247);")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_14.setStyleSheet("color: rgb(158, 203, 247);")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background: #9ECBF7; \n"
"    color: #0C1829;\n"
"    padding: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"    background: silver; \n"
"}\n"
"QPushButton:pressed {\n"
"    background: dark;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(580, 10, 171, 16))
        self.label_15.setStyleSheet("color: rgb(158, 203, 247);")
        self.label_15.setObjectName("label_15")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(490, 30, 101, 41))
        self.label_6.setStyleSheet("color: rgb(158, 203, 247);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(311, 399, 481, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    background: #9ECBF7; \n"
"    color: #0C1829;\n"
"    padding: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"    background: silver; \n"
"}\n"
"QPushButton:pressed {\n"
"    background: dark;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background: #9ECBF7; \n"
"    color: #0C1829;\n"
"    padding: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"    background: silver; \n"
"}\n"
"QPushButton:pressed {\n"
"    background: dark;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background: #9ECBF7; \n"
"    color: #0C1829;\n"
"    padding: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"    background: silver; \n"
"}\n"
"QPushButton:pressed {\n"
"    background: dark;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "BTC BALANCE CHECKER"))
        self.label_3.setText(_translate("Dialog", "?????????????????????????? ????????????????????"))
        self.label_4.setText(_translate("Dialog", "???????????????? ????????????????????????"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "BTC"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "ETH"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "LTC"))
        self.label_5.setText(_translate("Dialog", "?????????????? ?????????????? ??????????????????????"))
        self.pushButton.setText(_translate("Dialog", "??????????????????"))
        self.label_8.setText(_translate("Dialog", "?? ?????? {btc}BTC ?????? ???????????????? {btcv} {valute},?????????? ?????? ????????{}{valute}"))
        self.label_7.setText(_translate("Dialog", "?? ?????? {eth}ETH ?????? ???????????????? {ethv} {valute},?????????? ?????? ????????{}{valute}"))
        self.label_9.setText(_translate("Dialog", "?? ?????? {ltc}LTC ?????? ???????????????? {ltcv} {valute},?????????? ?????? ????????{}{valute}"))
        self.label_11.setText(_translate("Dialog", "??????????:{btcv+ethv+ltcv}{valute},?????????? ?? ?????? ???????? {}{valute}"))
        self.label_2.setText(_translate("Dialog", "???????? ????????????"))
        self.comboBox.setItemText(0, _translate("Dialog", "Rub"))
        self.comboBox.setItemText(1, _translate("Dialog", "Dollar"))
        self.comboBox.setItemText(2, _translate("Dialog", "Euro"))
        self.comboBox.setItemText(3, _translate("Dialog", "Hryvnia"))
        self.pushButton_2.setText(_translate("Dialog", "??????????????????"))
        self.pushButton_3.setText(_translate("Dialog", "????????????????!"))
        self.label_10.setText(_translate("Dialog", "???????? ???? ???????????? ????????????"))
        self.label_12.setText(_translate("Dialog", "1 BTC = "))
        self.label_13.setText(_translate("Dialog", "1 LTC = "))
        self.label_14.setText(_translate("Dialog", "1 ETH ="))
        self.pushButton_6.setText(_translate("Dialog", "?????????????????? ????????????????????"))
        self.label_15.setText(_translate("Dialog", "??????????:"))
        self.label_6.setText(_translate("Dialog", "???????? ??????????????"))
        self.pushButton_7.setText(_translate("Dialog", "???????????????? ????????????????????"))
        self.pushButton_5.setText(_translate("Dialog", "?????????????? ???????????????????? ????????????"))
        self.pushButton_4.setText(_translate("Dialog", "??????????????????????????"))
