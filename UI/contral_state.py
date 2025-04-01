# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contral_state.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 704)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.top = QtWidgets.QWidget(self.centralwidget)
        self.top.setGeometry(QtCore.QRect(0, 0, 901, 91))
        self.top.setStyleSheet("background-image:url(:/pic/2b3042d398f6b628975e99cdaebf16d.png);\n"
"background-repeat:no-repeat;\n"
"background-attachment:fixed;")
        self.top.setObjectName("top")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 90, 441, 371))
        self.widget.setObjectName("widget")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(0, 0, 441, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.leftBrowser = QtWidgets.QTextBrowser(self.widget)
        self.leftBrowser.setGeometry(QtCore.QRect(0, 20, 221, 351))
        self.leftBrowser.setObjectName("leftBrowser")
        self.rightBrowser = QtWidgets.QTextBrowser(self.widget)
        self.rightBrowser.setGeometry(QtCore.QRect(220, 20, 221, 351))
        self.rightBrowser.setObjectName("rightBrowser")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 222, 21))
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setStyleSheet("color: rgb(0, 191, 243);\n"
"border-color: rgb(0, 191, 243);\n"
"border-width:1px;\n"
"border-style: solid;\n"
"background-color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(220, 0, 222, 21))
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_5.setStyleSheet("color: rgb(0, 191, 243);\n"
"border-color: rgb(0, 191, 243);\n"
"border-width:1px;\n"
"border-style: solid;\n"
"background-color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 470, 51, 20))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 460, 441, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(253, 470, 20, 231))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.com = QtWidgets.QComboBox(self.centralwidget)
        self.com.setGeometry(QtCore.QRect(340, 500, 69, 22))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.com.setFont(font)
        self.com.setObjectName("com")
        self.com.addItem("")
        self.com.addItem("")
        self.com.addItem("")
        self.com.addItem("")
        self.com.addItem("")
        self.com.addItem("")
        self.com.addItem("")
        self.com.addItem("")
        self.baudrate = QtWidgets.QComboBox(self.centralwidget)
        self.baudrate.setGeometry(QtCore.QRect(340, 530, 69, 22))
        self.baudrate.setObjectName("baudrate")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 500, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 532, 54, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.set_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_button.setGeometry(QtCore.QRect(270, 660, 75, 23))
        self.set_button.setObjectName("set_button")
        self.comBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.comBrowser.setGeometry(QtCore.QRect(270, 570, 161, 81))
        self.comBrowser.setObjectName("comBrowser")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(20, 480, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.openButton.setFont(font)
        self.openButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.openButton.setStyleSheet("background-color: rgb(0, 191, 243);\n"
"color: rgb(255, 255, 255);")
        self.openButton.setObjectName("openButton")
        self.swapButton = QtWidgets.QPushButton(self.centralwidget)
        self.swapButton.setGeometry(QtCore.QRect(20, 540, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.swapButton.setFont(font)
        self.swapButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.swapButton.setStyleSheet("background-color: rgb(0, 191, 243);\n"
"color: rgb(255, 255, 255);")
        self.swapButton.setObjectName("swapButton")
        self.foot = QtWidgets.QLabel(self.centralwidget)
        self.foot.setGeometry(QtCore.QRect(0, 690, 441, 16))
        self.foot.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"宋体\";\n"
"color: rgb(0, 0, 0);")
        self.foot.setObjectName("foot")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "控制台"))
        self.leftBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.rightBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Left Cap Pos"))
        self.label_5.setText(_translate("MainWindow", "Right Cap Pos"))
        self.label.setText(_translate("MainWindow", "串口配置"))
        self.com.setItemText(0, _translate("MainWindow", "com1"))
        self.com.setItemText(1, _translate("MainWindow", "com2"))
        self.com.setItemText(2, _translate("MainWindow", "com3"))
        self.com.setItemText(3, _translate("MainWindow", "com4"))
        self.com.setItemText(4, _translate("MainWindow", "com5"))
        self.com.setItemText(5, _translate("MainWindow", "com6"))
        self.com.setItemText(6, _translate("MainWindow", "com7"))
        self.com.setItemText(7, _translate("MainWindow", "com8"))
        self.baudrate.setItemText(0, _translate("MainWindow", "9600"))
        self.baudrate.setItemText(1, _translate("MainWindow", "19200"))
        self.baudrate.setItemText(2, _translate("MainWindow", "57600"))
        self.baudrate.setItemText(3, _translate("MainWindow", "115200"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#55007f;\">COM：</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#55007f;\">波特率</span></p></body></html>"))
        self.set_button.setText(_translate("MainWindow", "设置"))
        self.openButton.setText(_translate("MainWindow", "Open Cap"))
        self.swapButton.setText(_translate("MainWindow", "Swap Cap"))
        self.foot.setText(_translate("MainWindow", "                               @ 模拟搜救 2020"))

import pic_rc
