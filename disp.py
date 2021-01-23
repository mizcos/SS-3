import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui.ui_stacked import Ui_MainWindow
import datetime
import json
import copy
from sound_alarm.alarm_test import playTapSound,playAlarm,stopAlarm


class gui(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(gui, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.time_breakfast  = QTime()
        self.time_lunch      = QTime()
        self.time_dinner     = QTime()
        self.snooze = 0
        self.tapvol=30
        self.alarmvol=30
        self.mdcnlist_breakfast=[]
        self.mdcnlist_lunch=[]
        self.mdcnlist_dinner=[]
        self.mdcnlist_now=[]
        self.disp_mdcn_nowpage=0

        #毎秒実行される時計更新とアラーム分岐
        timer = QTimer(self)
        timer.timeout.connect(self.updtTime)
        self.ui.lcdNumber_clock.setSegmentStyle(QLCDNumber.Filled)
        self.ui.lcdNumber_clock.setDigitCount(6)
        self.updtTime()
        timer.start(1000)

    def gopage_setting (self):
        self.ui.stackedWidget.setCurrentIndex(1)
        playTapSound(self.tapvol)

    def gopage_top(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        playTapSound(self.tapvol)


    def gopage_mdcn_info(self):
        self.ui.stackedWidget.setCurrentIndex(11)
        playTapSound(self.tapvol)
        
    def gopage_mdcn_record(self):
        self.ui.stackedWidget.setCurrentIndex(12)
        playTapSound(self.tapvol)


    def gopage_set_adress(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        playTapSound(self.tapvol)

    def gopage_set_mealtime(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        playTapSound(self.tapvol)

    def gopage_set_volume(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        playTapSound(self.tapvol)


    def slct_yes(self):
        #「薬を飲んだ」ボタンを押した処理
        self.ui.stackedWidget.setCurrentIndex(7)
        self.snooze =0
        stopAlarm()

    def slct_yet(self):
        #「食事がまだ」ボタンを押した処理
        self.ui.stackedWidget.setCurrentIndex(9)
        self.snooze = self.snooze + 30*60
        stopAlarm()

    def slct_no(self):
        #「飲んでいない」ボタンを押した処理
        self.ui.stackedWidget.setCurrentIndex(10)
        self.snooze =0
        stopAlarm()

    def set_snooze(self):
        #60分後に再通知なので，default 30 +30 min
        self.snooze = self.snooze + 30*60

    def set_oparate_volume(self,value):
        self.tapvol=value
        #value -> 0~99でのスライダの値，操作音量

    def set_alarm_volume(self,value):
        self.alarmvol=value
        #value -> 0~99でのスライダの値，アラーム音量

    def set_mealtime_breakfast(self,time):
        self.time_breakfast = time
        print(time)

    def set_mealtime_lunch(self,time):
        self.time_lunch = time

    def set_mealtime_dinner(self,time):
        self.time_dinner = time

    def reason_wkup_late(self):
        #「起床時間が遅い」ボタンを押した処理
        a=1

    def reason_bad_condition(self):
        #「体調不良」ボタンを押した処理
        a=1

    def reason_have_no_mdcn(self):
        #「薬がない，忘れた」ボタンを押した処理
        a=1

    def reason_other(self):
        #「その他」ボタンを押した処理
        a=1

    def disp_mdcn_back(self):
        stopAlarm()
        if(self.disp_mdcn_nowpage>0):
            self.disp_mdcn_nowpage-=1
            self.ui.label_disp_mdcn_typenum.setText(str(len(self.mdcnlist_now))+'種類')
            self.ui.label_disp_mdcn_num.setText(str(self.mdcnlist_now[self.disp_mdcn_nowpage]['num'])+'錠')

            
            
    
    def disp_mdcn_next(self):
        stopAlarm()
        if(self.disp_mdcn_nowpage<len(self.mdcnlist_now)-1):
            self.disp_mdcn_nowpage +=1
            self.ui.label_disp_mdcn_typenum.setText(str(len(self.mdcnlist_now))+'種類')
            self.ui.label_disp_mdcn_num.setText(str(self.mdcnlist_now[self.disp_mdcn_nowpage]['num'])+'錠')

    

    def loadDatabase(self):
        dataop = open('medicine_data/data.json','r')
        data = json.load(dataop)

        for mdcn in data['mdcn_data']:#各薬についてのloop
            for t in mdcn['time']:#朝昼夜を確認
                if t =='朝':
                    self.mdcnlist_breakfast.append(mdcn)

                if t =='昼':
                    self.mdcnlist_lunch.append(mdcn)

                if t =='夜':
                    self.mdcnlist_dinner.append(mdcn)

        print(self.mdcnlist_dinner)


    def alarmStart(self,s):
        self.loadDatabase()
        #s=1:朝食，s=2,昼食，s=3 夕食
        if s==1:
            timing = "朝食後"
            self.mdcnlist_now=copy.deepcopy(self.mdcnlist_breakfast)

        elif s==2:
            timing = "昼食後"
            self.mdcnlist_now=copy.deepcopy(self.mdcnlist_lunch)

        elif s==3:
            timing = "夕食後"
            self.mdcnlist_now=copy.deepcopy(self.mdcnlist_dinner)
            
        self.ui.label_disp_meal.setText(timing)
        self.ui.label_disp_mdcn_typenum.setText(str(len(self.mdcnlist_now))+'種類')
        self.ui.label_disp_mdcn_num.setText(str(self.mdcnlist_now[self.disp_mdcn_nowpage]['num'])+'錠')

        self.ui.stackedWidget.setCurrentIndex(5)
        playAlarm(self.alarmvol)


    def updtTime(self):
        currentTime = QDateTime.currentDateTime().toString('hh:mm')
        self.ui.lcdNumber_clock.display(currentTime)
        self.ui.lcdNumber_clock_2.display(currentTime)
        todaysdate = QDateTime.currentDateTime().toString('yyyy/MM/dd')
        todaysdate_jp = todaysdate[0:4]+'年'+todaysdate[5:7]+'月'+todaysdate[8:]+'日'
        self.ui.label_date.setText(todaysdate_jp)
        nowtime =QDateTime.time(QDateTime.currentDateTime())

        #朝食
        dtBrkfst = QTime.secsTo(self.time_breakfast,nowtime)#設定時間との差
        dtBrkfst = dtBrkfst + self.snooze #snoozeが設定されていたならば，その時間に
        if (dtBrkfst==0 and QTime.isValid(self.time_breakfast)):
            #朝食アラームの処理をここで
            self.alarmStart(1)


        #昼食
        dtlnch = QTime.secsTo(self.time_lunch,nowtime)#設定時間との差
        dtlnch = dtlnch + self.snooze #snoozeが設定されていたならば，その時間に
        if (dtlnch==0 and QTime.isValid(self.time_lunch)):
            # 昼食アラームの処理をここで
            self.alarmStart(2)

        #夕食
        dtdnr = QTime.secsTo(self.time_dinner,nowtime)#設定時間との差
        dtdnr = dtdnr + self.snooze #snoozeが設定されていたならば，その時間に
        if (dtdnr==0 and QTime.isValid(self.time_dinner)):
            # 夕食アラームの処理をここで
            self.alarmStart(3)







    def keyPressEvent(self, e):#escで終了
        if e.key() == Qt.Key_Escape: 
            sys.exit(app.exec_())

        if e.key() ==Qt.Key_Space:
            self.ui.stackedWidget.setCurrentIndex(5)

    

        


 

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = gui()
    #window.showFullScreen()
    window.show()
    
    sys.exit(app.exec_())