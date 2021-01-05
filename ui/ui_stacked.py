# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_stacked.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 481, 320))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_0 = QtWidgets.QWidget()
        self.page_0.setObjectName("page_0")
        self.label = QtWidgets.QLabel(self.page_0)
        self.label.setGeometry(QtCore.QRect(140, 20, 311, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/title.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_setting = QtWidgets.QPushButton(self.page_0)
        self.pushButton_setting.setGeometry(QtCore.QRect(10, 20, 121, 71))
        self.pushButton_setting.setMouseTracking(False)
        self.pushButton_setting.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/capsule_setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_setting.setIcon(icon)
        self.pushButton_setting.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_setting.setCheckable(False)
        self.pushButton_setting.setFlat(True)
        self.pushButton_setting.setObjectName("pushButton_setting")
        self.lcdNumber_clock = QtWidgets.QLCDNumber(self.page_0)
        self.lcdNumber_clock.setGeometry(QtCore.QRect(110, 110, 231, 51))
        self.lcdNumber_clock.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_clock.setObjectName("lcdNumber_clock")
        self.label_date = QtWidgets.QLabel(self.page_0)
        self.label_date.setGeometry(QtCore.QRect(120, 160, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.pushButton_mdcn_info = QtWidgets.QPushButton(self.page_0)
        self.pushButton_mdcn_info.setGeometry(QtCore.QRect(10, 200, 221, 111))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_mdcn_info.setFont(font)
        self.pushButton_mdcn_info.setObjectName("pushButton_mdcn_info")
        self.pushButton_record = QtWidgets.QPushButton(self.page_0)
        self.pushButton_record.setGeometry(QtCore.QRect(250, 200, 221, 111))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_record.setFont(font)
        self.pushButton_record.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_record.setObjectName("pushButton_record")
        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.pushButton_return = QtWidgets.QPushButton(self.page_1)
        self.pushButton_return.setGeometry(QtCore.QRect(10, 20, 121, 71))
        self.pushButton_return.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/capsule_return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_return.setIcon(icon1)
        self.pushButton_return.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_return.setFlat(True)
        self.pushButton_return.setObjectName("pushButton_return")
        self.pushButton_setadress = QtWidgets.QPushButton(self.page_1)
        self.pushButton_setadress.setGeometry(QtCore.QRect(150, 20, 311, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_setadress.setFont(font)
        self.pushButton_setadress.setObjectName("pushButton_setadress")
        self.pushButton_set_mealtime = QtWidgets.QPushButton(self.page_1)
        self.pushButton_set_mealtime.setGeometry(QtCore.QRect(10, 110, 261, 201))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.pushButton_set_mealtime.setFont(font)
        self.pushButton_set_mealtime.setObjectName("pushButton_set_mealtime")
        self.pushButton_set_volume = QtWidgets.QPushButton(self.page_1)
        self.pushButton_set_volume.setGeometry(QtCore.QRect(310, 110, 151, 201))
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        font.setPointSize(30)
        font.setKerning(True)
        self.pushButton_set_volume.setFont(font)
        self.pushButton_set_volume.setObjectName("pushButton_set_volume")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton_return_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_return_2.setGeometry(QtCore.QRect(10, 20, 121, 71))
        self.pushButton_return_2.setText("")
        self.pushButton_return_2.setIcon(icon1)
        self.pushButton_return_2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_return_2.setFlat(True)
        self.pushButton_return_2.setObjectName("pushButton_return_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 411, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit.setGeometry(QtCore.QRect(40, 120, 371, 81))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(170, 30, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.pushButton_return_3 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_return_3.setGeometry(QtCore.QRect(10, 20, 121, 71))
        self.pushButton_return_3.setText("")
        self.pushButton_return_3.setIcon(icon1)
        self.pushButton_return_3.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_return_3.setFlat(True)
        self.pushButton_return_3.setObjectName("pushButton_return_3")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(170, 30, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(80, 120, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setGeometry(QtCore.QRect(80, 190, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(80, 260, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.timeEdit_breakfast = QtWidgets.QTimeEdit(self.page_3)
        self.timeEdit_breakfast.setGeometry(QtCore.QRect(180, 120, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.timeEdit_breakfast.setFont(font)
        self.timeEdit_breakfast.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 2), QtCore.QTime(0, 0, 0)))
        self.timeEdit_breakfast.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 2), QtCore.QTime(23, 59, 59)))
        self.timeEdit_breakfast.setObjectName("timeEdit_breakfast")
        self.timeEdit_lanch = QtWidgets.QTimeEdit(self.page_3)
        self.timeEdit_lanch.setGeometry(QtCore.QRect(180, 190, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.timeEdit_lanch.setFont(font)
        self.timeEdit_lanch.setObjectName("timeEdit_lanch")
        self.timeEdit_dinner = QtWidgets.QTimeEdit(self.page_3)
        self.timeEdit_dinner.setGeometry(QtCore.QRect(180, 260, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.timeEdit_dinner.setFont(font)
        self.timeEdit_dinner.setObjectName("timeEdit_dinner")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.pushButton_return_4 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_return_4.setGeometry(QtCore.QRect(10, 20, 121, 71))
        self.pushButton_return_4.setText("")
        self.pushButton_return_4.setIcon(icon1)
        self.pushButton_return_4.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_return_4.setFlat(True)
        self.pushButton_return_4.setObjectName("pushButton_return_4")
        self.label_8 = QtWidgets.QLabel(self.page_4)
        self.label_8.setGeometry(QtCore.QRect(170, 30, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_4)
        self.label_9.setGeometry(QtCore.QRect(40, 110, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_4)
        self.label_10.setGeometry(QtCore.QRect(80, 190, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalSlider = QtWidgets.QSlider(self.page_4)
        self.horizontalSlider.setGeometry(QtCore.QRect(190, 130, 221, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.page_4)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(190, 210, 221, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.label_11 = QtWidgets.QLabel(self.page_4)
        self.label_11.setGeometry(QtCore.QRect(190, 160, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setGeometry(QtCore.QRect(190, 240, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page_4)
        self.label_13.setGeometry(QtCore.QRect(400, 150, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page_4)
        self.label_14.setGeometry(QtCore.QRect(400, 230, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.stackedWidget.addWidget(self.page_4)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.lcdNumber_clock_2 = QtWidgets.QLCDNumber(self.page_8)
        self.lcdNumber_clock_2.setGeometry(QtCore.QRect(30, 10, 311, 61))
        self.lcdNumber_clock_2.setObjectName("lcdNumber_clock_2")
        self.label_disp_meal = QtWidgets.QLabel(self.page_8)
        self.label_disp_meal.setGeometry(QtCore.QRect(360, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_disp_meal.setFont(font)
        self.label_disp_meal.setObjectName("label_disp_meal")
        self.stackedWidget_disp_mdcn = QtWidgets.QStackedWidget(self.page_8)
        self.stackedWidget_disp_mdcn.setGeometry(QtCore.QRect(130, 90, 181, 131))
        self.stackedWidget_disp_mdcn.setObjectName("stackedWidget_disp_mdcn")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.graphicsView_disp_mdcn = QtWidgets.QGraphicsView(self.page)
        self.graphicsView_disp_mdcn.setGeometry(QtCore.QRect(0, 0, 181, 131))
        self.graphicsView_disp_mdcn.setObjectName("graphicsView_disp_mdcn")
        self.stackedWidget_disp_mdcn.addWidget(self.page)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget_disp_mdcn.addWidget(self.page_5)
        self.pushButton_disp_mdcn_back = QtWidgets.QPushButton(self.page_8)
        self.pushButton_disp_mdcn_back.setGeometry(QtCore.QRect(100, 140, 31, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_disp_mdcn_back.setFont(font)
        self.pushButton_disp_mdcn_back.setObjectName("pushButton_disp_mdcn_back")
        self.pushButton_disp_mdcn_next = QtWidgets.QPushButton(self.page_8)
        self.pushButton_disp_mdcn_next.setGeometry(QtCore.QRect(310, 140, 31, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_disp_mdcn_next.setFont(font)
        self.pushButton_disp_mdcn_next.setObjectName("pushButton_disp_mdcn_next")
        self.pushButton_slct_yes = QtWidgets.QPushButton(self.page_8)
        self.pushButton_slct_yes.setGeometry(QtCore.QRect(0, 220, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_slct_yes.setFont(font)
        self.pushButton_slct_yes.setObjectName("pushButton_slct_yes")
        self.pushButton_slct_yet = QtWidgets.QPushButton(self.page_8)
        self.pushButton_slct_yet.setGeometry(QtCore.QRect(160, 220, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_slct_yet.setFont(font)
        self.pushButton_slct_yet.setObjectName("pushButton_slct_yet")
        self.pushButton_slct_no = QtWidgets.QPushButton(self.page_8)
        self.pushButton_slct_no.setGeometry(QtCore.QRect(320, 220, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_slct_no.setFont(font)
        self.pushButton_slct_no.setObjectName("pushButton_slct_no")
        self.label_15 = QtWidgets.QLabel(self.page_8)
        self.label_15.setGeometry(QtCore.QRect(10, 120, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_disp_mdcn_typenum = QtWidgets.QLabel(self.page_8)
        self.label_disp_mdcn_typenum.setGeometry(QtCore.QRect(10, 160, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_disp_mdcn_typenum.setFont(font)
        self.label_disp_mdcn_typenum.setObjectName("label_disp_mdcn_typenum")
        self.label_disp_mdcn_num = QtWidgets.QLabel(self.page_8)
        self.label_disp_mdcn_num.setGeometry(QtCore.QRect(370, 130, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_disp_mdcn_num.setFont(font)
        self.label_disp_mdcn_num.setObjectName("label_disp_mdcn_num")
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.lcdNumber_clock_3 = QtWidgets.QLCDNumber(self.page_9)
        self.lcdNumber_clock_3.setGeometry(QtCore.QRect(30, 10, 311, 61))
        self.lcdNumber_clock_3.setObjectName("lcdNumber_clock_3")
        self.label_disp_meal_2 = QtWidgets.QLabel(self.page_9)
        self.label_disp_meal_2.setGeometry(QtCore.QRect(360, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_disp_meal_2.setFont(font)
        self.label_disp_meal_2.setObjectName("label_disp_meal_2")
        self.label_16 = QtWidgets.QLabel(self.page_9)
        self.label_16.setGeometry(QtCore.QRect(50, 80, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.page_9)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(70, 220, 331, 31))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.scrollArea = QtWidgets.QScrollArea(self.page_9)
        self.scrollArea.setGeometry(QtCore.QRect(70, 110, 331, 111))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 329, 109))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.graphicsView_hoge1 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_hoge1.setGeometry(QtCore.QRect(0, 0, 131, 111))
        self.graphicsView_hoge1.setObjectName("graphicsView_hoge1")
        self.graphicsView_hoge2 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_hoge2.setGeometry(QtCore.QRect(130, 0, 131, 111))
        self.graphicsView_hoge2.setObjectName("graphicsView_hoge2")
        self.graphicsView_hoge3 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_hoge3.setGeometry(QtCore.QRect(260, 0, 131, 111))
        self.graphicsView_hoge3.setObjectName("graphicsView_hoge3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_slct_yet_2 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_slct_yet_2.setGeometry(QtCore.QRect(50, 250, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_slct_yet_2.setFont(font)
        self.pushButton_slct_yet_2.setObjectName("pushButton_slct_yet_2")
        self.pushButton_slct_no_2 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_slct_no_2.setGeometry(QtCore.QRect(270, 250, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_slct_no_2.setFont(font)
        self.pushButton_slct_no_2.setObjectName("pushButton_slct_no_2")
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.pushButton_return_5 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_return_5.setGeometry(QtCore.QRect(10, 20, 121, 71))
        self.pushButton_return_5.setText("")
        self.pushButton_return_5.setIcon(icon1)
        self.pushButton_return_5.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_return_5.setFlat(True)
        self.pushButton_return_5.setObjectName("pushButton_return_5")
        self.lcdNumber_clock_4 = QtWidgets.QLCDNumber(self.page_10)
        self.lcdNumber_clock_4.setGeometry(QtCore.QRect(150, 20, 311, 61))
        self.lcdNumber_clock_4.setObjectName("lcdNumber_clock_4")
        self.stackedWidget_disp_mdcn_2 = QtWidgets.QStackedWidget(self.page_10)
        self.stackedWidget_disp_mdcn_2.setGeometry(QtCore.QRect(30, 120, 201, 141))
        self.stackedWidget_disp_mdcn_2.setObjectName("stackedWidget_disp_mdcn_2")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.graphicsView_disp_mdcn_2 = QtWidgets.QGraphicsView(self.page_6)
        self.graphicsView_disp_mdcn_2.setGeometry(QtCore.QRect(0, 0, 201, 141))
        self.graphicsView_disp_mdcn_2.setObjectName("graphicsView_disp_mdcn_2")
        self.stackedWidget_disp_mdcn_2.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.stackedWidget_disp_mdcn_2.addWidget(self.page_7)
        self.pushButton_disp_mdcn_back_2 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_disp_mdcn_back_2.setGeometry(QtCore.QRect(20, 261, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_disp_mdcn_back_2.setFont(font)
        self.pushButton_disp_mdcn_back_2.setObjectName("pushButton_disp_mdcn_back_2")
        self.pushButton_disp_mdcn_next_2 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_disp_mdcn_next_2.setGeometry(QtCore.QRect(150, 260, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_disp_mdcn_next_2.setFont(font)
        self.pushButton_disp_mdcn_next_2.setObjectName("pushButton_disp_mdcn_next_2")
        self.label_disp_mdcn_name = QtWidgets.QLabel(self.page_10)
        self.label_disp_mdcn_name.setGeometry(QtCore.QRect(270, 120, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_disp_mdcn_name.setFont(font)
        self.label_disp_mdcn_name.setObjectName("label_disp_mdcn_name")
        self.pushButton_slct_yes_3 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_slct_yes_3.setGeometry(QtCore.QRect(250, 150, 201, 61))
        self.pushButton_slct_yes_3.setObjectName("pushButton_slct_yes_3")
        self.pushButton_slct_no_3 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_slct_no_3.setGeometry(QtCore.QRect(250, 250, 201, 61))
        self.pushButton_slct_no_3.setObjectName("pushButton_slct_no_3")
        self.pushButton_slct_yet_3 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_slct_yet_3.setGeometry(QtCore.QRect(250, 200, 201, 61))
        self.pushButton_slct_yet_3.setObjectName("pushButton_slct_yet_3")
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.label_date_2 = QtWidgets.QLabel(self.page_11)
        self.label_date_2.setGeometry(QtCore.QRect(40, 10, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_date_2.setFont(font)
        self.label_date_2.setObjectName("label_date_2")
        self.label_bfr_brkfst = QtWidgets.QLabel(self.page_11)
        self.label_bfr_brkfst.setGeometry(QtCore.QRect(40, 80, 141, 61))
        self.label_bfr_brkfst.setObjectName("label_bfr_brkfst")
        self.label_bfr_lnch = QtWidgets.QLabel(self.page_11)
        self.label_bfr_lnch.setGeometry(QtCore.QRect(40, 140, 141, 61))
        self.label_bfr_lnch.setObjectName("label_bfr_lnch")
        self.label_bfr_dnr = QtWidgets.QLabel(self.page_11)
        self.label_bfr_dnr.setGeometry(QtCore.QRect(40, 200, 141, 61))
        self.label_bfr_dnr.setObjectName("label_bfr_dnr")
        self.label_aftr_brkfst = QtWidgets.QLabel(self.page_11)
        self.label_aftr_brkfst.setGeometry(QtCore.QRect(230, 80, 141, 61))
        self.label_aftr_brkfst.setObjectName("label_aftr_brkfst")
        self.label_aftr_lnch = QtWidgets.QLabel(self.page_11)
        self.label_aftr_lnch.setGeometry(QtCore.QRect(230, 140, 141, 61))
        self.label_aftr_lnch.setObjectName("label_aftr_lnch")
        self.label_aft_dnr = QtWidgets.QLabel(self.page_11)
        self.label_aft_dnr.setGeometry(QtCore.QRect(230, 200, 141, 61))
        self.label_aft_dnr.setObjectName("label_aft_dnr")
        self.label_bfr_slp = QtWidgets.QLabel(self.page_11)
        self.label_bfr_slp.setGeometry(QtCore.QRect(110, 250, 141, 61))
        self.label_bfr_slp.setObjectName("label_bfr_slp")
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.label_date_3 = QtWidgets.QLabel(self.page_12)
        self.label_date_3.setGeometry(QtCore.QRect(40, 10, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_date_3.setFont(font)
        self.label_date_3.setObjectName("label_date_3")
        self.lcdNumber_clock_5 = QtWidgets.QLCDNumber(self.page_12)
        self.lcdNumber_clock_5.setGeometry(QtCore.QRect(80, 70, 311, 61))
        self.lcdNumber_clock_5.setObjectName("lcdNumber_clock_5")
        self.label_17 = QtWidgets.QLabel(self.page_12)
        self.label_17.setGeometry(QtCore.QRect(110, 160, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.pushButton = QtWidgets.QPushButton(self.page_12)
        self.pushButton.setGeometry(QtCore.QRect(30, 240, 151, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_12)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 240, 151, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.page_12)
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setObjectName("page_13")
        self.label_date_4 = QtWidgets.QLabel(self.page_13)
        self.label_date_4.setGeometry(QtCore.QRect(40, 10, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_date_4.setFont(font)
        self.label_date_4.setObjectName("label_date_4")
        self.label_18 = QtWidgets.QLabel(self.page_13)
        self.label_18.setGeometry(QtCore.QRect(40, 60, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_13)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 110, 341, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_13)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 160, 341, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_13)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 210, 341, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_13)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 260, 341, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.stackedWidget.addWidget(self.page_13)
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setObjectName("page_15")
        self.pushButton_return_6 = QtWidgets.QPushButton(self.page_15)
        self.pushButton_return_6.setGeometry(QtCore.QRect(10, 20, 121, 71))
        self.pushButton_return_6.setText("")
        self.pushButton_return_6.setIcon(icon1)
        self.pushButton_return_6.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_return_6.setFlat(True)
        self.pushButton_return_6.setObjectName("pushButton_return_6")
        self.graphicsView_disp_mdcn_3 = QtWidgets.QGraphicsView(self.page_15)
        self.graphicsView_disp_mdcn_3.setGeometry(QtCore.QRect(30, 110, 231, 161))
        self.graphicsView_disp_mdcn_3.setObjectName("graphicsView_disp_mdcn_3")
        self.pushButton_disp_mdcn_back_3 = QtWidgets.QPushButton(self.page_15)
        self.pushButton_disp_mdcn_back_3.setGeometry(QtCore.QRect(10, 270, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_disp_mdcn_back_3.setFont(font)
        self.pushButton_disp_mdcn_back_3.setObjectName("pushButton_disp_mdcn_back_3")
        self.pushButton_disp_mdcn_next_3 = QtWidgets.QPushButton(self.page_15)
        self.pushButton_disp_mdcn_next_3.setGeometry(QtCore.QRect(190, 270, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_disp_mdcn_next_3.setFont(font)
        self.pushButton_disp_mdcn_next_3.setObjectName("pushButton_disp_mdcn_next_3")
        self.label_disp_mdcn_name_2 = QtWidgets.QLabel(self.page_15)
        self.label_disp_mdcn_name_2.setGeometry(QtCore.QRect(210, 70, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_disp_mdcn_name_2.setFont(font)
        self.label_disp_mdcn_name_2.setObjectName("label_disp_mdcn_name_2")
        self.label_disp_mdcn_time = QtWidgets.QLabel(self.page_15)
        self.label_disp_mdcn_time.setGeometry(QtCore.QRect(290, 120, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_disp_mdcn_time.setFont(font)
        self.label_disp_mdcn_time.setObjectName("label_disp_mdcn_time")
        self.label_disp_mdcn_num_2 = QtWidgets.QLabel(self.page_15)
        self.label_disp_mdcn_num_2.setGeometry(QtCore.QRect(340, 230, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_disp_mdcn_num_2.setFont(font)
        self.label_disp_mdcn_num_2.setObjectName("label_disp_mdcn_num_2")
        self.stackedWidget.addWidget(self.page_15)
        self.page_17 = QtWidgets.QWidget()
        self.page_17.setObjectName("page_17")
        self.pushButton_return_7 = QtWidgets.QPushButton(self.page_17)
        self.pushButton_return_7.setGeometry(QtCore.QRect(10, 20, 121, 71))
        self.pushButton_return_7.setText("")
        self.pushButton_return_7.setIcon(icon1)
        self.pushButton_return_7.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_return_7.setFlat(True)
        self.pushButton_return_7.setObjectName("pushButton_return_7")
        self.label_19 = QtWidgets.QLabel(self.page_17)
        self.label_19.setGeometry(QtCore.QRect(170, 30, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.stackedWidget.addWidget(self.page_17)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_disp_mdcn.setCurrentIndex(0)
        self.stackedWidget_disp_mdcn_2.setCurrentIndex(0)
        self.pushButton_return_6.pressed.connect(MainWindow.gopage_top)
        self.pushButton_return.pressed.connect(MainWindow.gopage_top)
        self.pushButton_set_mealtime.pressed.connect(MainWindow.gopage_set_mealtime)
        self.pushButton_setadress.pressed.connect(MainWindow.gopage_set_adress)
        self.pushButton_set_volume.pressed.connect(MainWindow.gopage_set_volume)
        self.pushButton_return_2.pressed.connect(MainWindow.gopage_top)
        self.timeEdit_breakfast.editingFinished.connect(MainWindow.set_mealtime_breakfast)
        self.timeEdit_lanch.editingFinished.connect(MainWindow.set_mealtime_lanch)
        self.timeEdit_dinner.editingFinished.connect(MainWindow.set_mealtime_dinner)
        self.pushButton_return_7.pressed.connect(MainWindow.gopage_top)
        self.pushButton_record.pressed.connect(MainWindow.gopage_mdcn_record)
        self.pushButton_return_4.pressed.connect(MainWindow.gopage_top)
        self.pushButton_setting.pressed.connect(MainWindow.gopage_setting)
        self.horizontalSlider.valueChanged['int'].connect(MainWindow.set_alarm_volume)
        self.horizontalSlider_2.valueChanged['int'].connect(MainWindow.set_oparate_volume)
        self.pushButton_disp_mdcn_back.pressed.connect(MainWindow.disp_mdcn_back)
        self.pushButton_disp_mdcn_next.pressed.connect(MainWindow.disp_mdcn_next)
        self.pushButton_return_5.pressed.connect(MainWindow.gopage_top)
        self.pushButton_disp_mdcn_back_2.pressed.connect(MainWindow.disp_mdcn_back)
        self.pushButton_disp_mdcn_next_2.pressed.connect(MainWindow.disp_mdcn_next)
        self.pushButton_slct_yes_3.pressed.connect(MainWindow.slct_yes)
        self.pushButton_slct_yet_3.pressed.connect(MainWindow.slct_yet)
        self.pushButton_slct_no_3.pressed.connect(MainWindow.slct_no)
        self.pushButton.pressed.connect(MainWindow.gopage_top)
        self.pushButton_2.pressed.connect(MainWindow.set_snooze)
        self.pushButton_slct_yet_2.pressed.connect(MainWindow.slct_yet)
        self.pushButton_slct_no_2.pressed.connect(MainWindow.slct_no)
        self.pushButton_slct_no.pressed.connect(MainWindow.slct_no)
        self.pushButton_slct_yes.pressed.connect(MainWindow.slct_yes)
        self.pushButton_slct_yet.pressed.connect(MainWindow.gopage_top)
        self.pushButton_return_3.pressed.connect(MainWindow.gopage_top)
        self.pushButton_3.pressed.connect(MainWindow.reason_wkup_late)
        self.pushButton_4.pressed.connect(MainWindow.reason_bad_condition)
        self.pushButton_5.pressed.connect(MainWindow.reason_have_no_mdcn)
        self.pushButton_6.pressed.connect(MainWindow.reason_other)
        self.pushButton_return_2.pressed.connect(MainWindow.gopage_top)
        self.pushButton_mdcn_info.pressed.connect(MainWindow.gopage_mdcn_info)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_date.setText(_translate("MainWindow", "2021年1月5日"))
        self.pushButton_mdcn_info.setText(_translate("MainWindow", "お薬情報"))
        self.pushButton_record.setText(_translate("MainWindow", "服薬記録"))
        self.pushButton_setadress.setText(_translate("MainWindow", "連絡先設定"))
        self.pushButton_set_mealtime.setText(_translate("MainWindow", "お食事時間設定"))
        self.pushButton_set_volume.setText(_translate("MainWindow", "音量設定"))
        self.label_2.setText(_translate("MainWindow", "メールアドレスを入力してください"))
        self.label_4.setText(_translate("MainWindow", "連絡先設定"))
        self.label_3.setText(_translate("MainWindow", "お食事時間設定"))
        self.label_5.setText(_translate("MainWindow", "朝食"))
        self.label_6.setText(_translate("MainWindow", "昼食"))
        self.label_7.setText(_translate("MainWindow", "夕食"))
        self.label_8.setText(_translate("MainWindow", "音量設定"))
        self.label_9.setText(_translate("MainWindow", "アラーム音量"))
        self.label_10.setText(_translate("MainWindow", "操作音量"))
        self.label_11.setText(_translate("MainWindow", "小"))
        self.label_12.setText(_translate("MainWindow", "小"))
        self.label_13.setText(_translate("MainWindow", "大"))
        self.label_14.setText(_translate("MainWindow", "大"))
        self.label_disp_meal.setText(_translate("MainWindow", "昼食後"))
        self.pushButton_disp_mdcn_back.setText(_translate("MainWindow", "◁"))
        self.pushButton_disp_mdcn_next.setText(_translate("MainWindow", "▷"))
        self.pushButton_slct_yes.setText(_translate("MainWindow", "薬を飲んだ"))
        self.pushButton_slct_yet.setText(_translate("MainWindow", "食事がまだ"))
        self.pushButton_slct_no.setText(_translate("MainWindow", "飲んでいない"))
        self.label_15.setText(_translate("MainWindow", "お薬"))
        self.label_disp_mdcn_typenum.setText(_translate("MainWindow", "n種類"))
        self.label_disp_mdcn_num.setText(_translate("MainWindow", "n錠"))
        self.label_disp_meal_2.setText(_translate("MainWindow", "昼食後"))
        self.label_16.setText(_translate("MainWindow", "飲んだ薬を選択"))
        self.pushButton_slct_yet_2.setText(_translate("MainWindow", "食事がまだ"))
        self.pushButton_slct_no_2.setText(_translate("MainWindow", "薬を飲まない"))
        self.pushButton_disp_mdcn_back_2.setText(_translate("MainWindow", "前"))
        self.pushButton_disp_mdcn_next_2.setText(_translate("MainWindow", "次"))
        self.label_disp_mdcn_name.setText(_translate("MainWindow", "名前："))
        self.pushButton_slct_yes_3.setText(_translate("MainWindow", "薬を飲んだ"))
        self.pushButton_slct_no_3.setText(_translate("MainWindow", "薬を飲まない"))
        self.pushButton_slct_yet_3.setText(_translate("MainWindow", "食事がまだ"))
        self.label_date_2.setText(_translate("MainWindow", "2020/12/28"))
        self.label_bfr_brkfst.setText(_translate("MainWindow", "朝食前"))
        self.label_bfr_lnch.setText(_translate("MainWindow", "昼食前"))
        self.label_bfr_dnr.setText(_translate("MainWindow", "夕食前"))
        self.label_aftr_brkfst.setText(_translate("MainWindow", "朝食後"))
        self.label_aftr_lnch.setText(_translate("MainWindow", "昼食後"))
        self.label_aft_dnr.setText(_translate("MainWindow", "夕食後"))
        self.label_bfr_slp.setText(_translate("MainWindow", "就寝前"))
        self.label_date_3.setText(_translate("MainWindow", "2020/12/28"))
        self.label_17.setText(_translate("MainWindow", "n 分後に再アラーム"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.pushButton_2.setText(_translate("MainWindow", "60分後に変更"))
        self.label_date_4.setText(_translate("MainWindow", "2020/12/28"))
        self.label_18.setText(_translate("MainWindow", "薬を飲まない理由を選択"))
        self.pushButton_3.setText(_translate("MainWindow", "起床時間が遅い"))
        self.pushButton_4.setText(_translate("MainWindow", "体調不良"))
        self.pushButton_5.setText(_translate("MainWindow", "薬がない・忘れた"))
        self.pushButton_6.setText(_translate("MainWindow", "その他"))
        self.pushButton_disp_mdcn_back_3.setText(_translate("MainWindow", "前"))
        self.pushButton_disp_mdcn_next_3.setText(_translate("MainWindow", "次"))
        self.label_disp_mdcn_name_2.setText(_translate("MainWindow", "名前："))
        self.label_disp_mdcn_time.setText(_translate("MainWindow", "朝・夕　お食事後"))
        self.label_disp_mdcn_num_2.setText(_translate("MainWindow", "n錠"))
        self.label_19.setText(_translate("MainWindow", "服薬記録送信履歴"))
