# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 281, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../untitled/pp.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-50, 30, 711, 381))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../untitled/oo.png"))
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(280, 0, 511, 481))
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 511, 481))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../untitled/timg.jpg"))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(140, 130, 51, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../untitled/opo.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 130, 51, 51))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../untitled/opi.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalSlider = QtWidgets.QSlider(self.widget)
        self.horizontalSlider.setGeometry(QtCore.QRect(260, 280, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setGeometry(QtCore.QRect(90, 240, 361, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(220, 280, 31, 21))
        self.label_4.setObjectName("label_4")
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setGeometry(QtCore.QRect(340, 320, 51, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../untitled/opi.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("../untitled/opo.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton.setIcon(icon2)
        self.toolButton.setIconSize(QtCore.QSize(30, 30))
        self.toolButton.setCheckable(False)
        self.toolButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(220, 140, 101, 41))
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(279, -1, 511, 481))
        self.widget_2.setObjectName("widget_2")
        self.Select = QtWidgets.QComboBox(self.widget_2)
        self.Select.setGeometry(QtCore.QRect(370, 390, 111, 31))
        self.Select.setStyleSheet("            QComboBox\n"
"            {\n"
"            font: 9pt \"微软雅黑\";\n"
"            background:rgb(255, 170, 0);\n"
"            border-radius:5px;\n"
"            }")
        self.Select.setObjectName("Select")
        self.Connect = QtWidgets.QPushButton(self.widget_2)
        self.Connect.setGeometry(QtCore.QRect(400, 430, 81, 31))
        self.Connect.setStyleSheet("            QPushButton\n"
"            {\n"
"            background:#F76677;\n"
"            border-radius:5px;\n"
"            }\n"
"            QPushButton:hover{background:pink;\n"
"            }")
        self.Connect.setObjectName("Connect")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 390, 331, 81))
        self.textBrowser.setObjectName("textBrowser")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 511, 481))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../untitled/LLL.jpg"))
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.Select.raise_()
        self.Connect.raise_()
        self.textBrowser.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolButton.clicked.connect(self.widget.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "TIME"))
        self.toolButton.setText(_translate("MainWindow", "go"))
        self.label_5.setToolTip(_translate("MainWindow", "ttt"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.Select.setToolTip(_translate("MainWindow", "select uart port"))
        self.Connect.setToolTip(_translate("MainWindow", "connect uart"))
        self.Connect.setText(_translate("MainWindow", "CONNECT"))

