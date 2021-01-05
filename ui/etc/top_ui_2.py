# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'top.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



class Ui_TopWindow(QWidget):
    def setupUi(self, TopWindow):
        TopWindow.setObjectName("TopWindow")
        TopWindow.resize(480, 320)
        TopWindow.setMouseTracking(False)
        TopWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(TopWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_setting = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_setting.setGeometry(QtCore.QRect(10, 10, 121, 71))
        self.pushButton_setting.setMouseTracking(False)
        self.pushButton_setting.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/capsule_setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_setting.setIcon(icon)
        self.pushButton_setting.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_setting.setCheckable(False)
        self.pushButton_setting.setFlat(True)
        self.pushButton_setting.setObjectName("pushButton_setting")
        self.pushButton_mdcn_info = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mdcn_info.setGeometry(QtCore.QRect(10, 200, 221, 111))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_mdcn_info.setFont(font)
        self.pushButton_mdcn_info.setObjectName("pushButton_mdcn_info")
        self.pushButton_record = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_record.setGeometry(QtCore.QRect(250, 200, 221, 111))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_record.setFont(font)
        self.pushButton_record.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_record.setObjectName("pushButton_record")
        self.lcdNumber_clock = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_clock.setGeometry(QtCore.QRect(130, 90, 231, 51))
        self.lcdNumber_clock.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_clock.setObjectName("lcdNumber_clock")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(130, 150, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")


        #時間の更新
        timer = QTimer(self)
        timer.timeout.connect(self.updtTime)
        self.lcdNumber_clock.setSegmentStyle(QLCDNumber.Filled)
        self.lcdNumber_clock.setDigitCount(6)
        self.updtTime()
        timer.start(1000)

        self.retranslateUi(TopWindow)
        self.pushButton_setting.pressed.connect(TopWindow.pressed_setting)
        self.pushButton_mdcn_info.pressed.connect(TopWindow.pressed_mdcn_info)
        self.pushButton_record.pressed.connect(TopWindow.pressed_mdcn_record)
        QtCore.QMetaObject.connectSlotsByName(TopWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 311, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/title.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        TopWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TopWindow)
        self.pushButton_mdcn_info.pressed.connect(TopWindow.pressed_mdcn_info)
        self.pushButton_record.pressed.connect(TopWindow.pressed_mdcn_record)
        self.pushButton_setting.pressed.connect(TopWindow.pressed_setting)
        QtCore.QMetaObject.connectSlotsByName(TopWindow)

    def retranslateUi(self, TopWindow):
        _translate = QtCore.QCoreApplication.translate
        TopWindow.setWindowTitle(_translate("TopWindow", "TopWindow"))
        self.pushButton_mdcn_info.setText(_translate("TopWindow", "お薬情報"))
        self.pushButton_record.setText(_translate("TopWindow", "服薬記録"))
        self.label_date.setText(_translate("TopWindow", "TextLabel"))

    def updtTime(self):
        currentTime = QDateTime.currentDateTime().toString('hh:mm')
        self.lcdNumber_clock.display(currentTime)
        todaysdate = QDateTime.currentDateTime().toString('yyyy/MM/dd')
        todaysdate_jp = todaysdate[0:4]+'年'+todaysdate[5:7]+'月'+todaysdate[9:]+'日'
        self.label_date.setText(todaysdate_jp)