import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPalette, QPixmap
from ui.ui_stacked import Ui_MainWindow
from record import RecordData
import datetime
import json
import copy
from sound_alarm.alarm_test import playTapSound,playAlarm,stopAlarm,playCancelSound,playSelectSound


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
        self.mdcnlist_all=[]
        self.mdcnlist_breakfast=[]
        self.mdcnlist_lunch=[]
        self.mdcnlist_dinner=[]
        self.mdcnlist_now=[]

        self.record = RecordData() # 服薬履歴記録用
        
        self.disp_mdcn_nowpage=0
        self.disp_mdcn_all_nowpage=0
        self.loadDatabase()
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
        playCancelSound(self.tapvol)


    def gopage_mdcn_info(self):
        self.ui.stackedWidget.setCurrentIndex(11)
        playTapSound(self.tapvol)
        
        self.ui.label_disp_mdcn_num_3.setText(str(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['num'])+'錠')
        dispimg = QImage(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['img_path'])
        self.ui.label_disp_mdcn_name_3.setText(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['name'])
        self.ui.label_disp_mdcn_time_3.setText(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['time']+' 食後')
        self.ui.label_page_3.setText(str(self.disp_mdcn_all_nowpage+1)+'/'+str(len(self.mdcnlist_all)))
        Qdisp = QPixmap.fromImage(dispimg)
        QdispResized = Qdisp.scaled(240,150)
        self.ui.label_disp_mdcn_img_3.setPixmap(QdispResized)
        
    def gopage_mdcn_record(self):
        self.ui.stackedWidget.setCurrentIndex(12)
        playTapSound(self.tapvol)


    def gopage_set_adress(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        playTapSound(self.tapvol)

    def gopage_set_mealtime(self):
        self.ui.stackedWidget.setCurrentIndex(13)
        playTapSound(self.tapvol)

    def gopage_set_volume(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        playTapSound(self.tapvol)




    def slct_yes(self):
        #「薬を飲んだ」ボタンを押した処理
        #self.ui.stackedWidget.setCurrentIndex(7)
        self.snooze =0
        stopAlarm()
        self.disp_mdcn_nowpage=0
        dispimg = QImage(self.mdcnlist_now[self.disp_mdcn_nowpage]['img_path'])
        Qdisp = QPixmap.fromImage(dispimg)
        QdispResized = Qdisp.scaled(180,130)
        self.ui.label_disp_mdcn_img_4.setPixmap(QdispResized)
        self.ui.label_disp_mdcn_name_4.setText(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['name'])
        self.ui.stackedWidget.setCurrentIndex(7)
        playTapSound(self.tapvol)



    def slct_yet(self):
        #「食事がまだ」ボタンを押した処理
        self.ui.stackedWidget.setCurrentIndex(9)
        self.snooze = self.snooze + 30*60
        stopAlarm()
        playTapSound(self.tapvol)

    def slct_no(self):
        #「飲んでいない」ボタンを押した処理
        self.ui.stackedWidget.setCurrentIndex(10)
        self.snooze =0
        stopAlarm()
        playTapSound(self.tapvol)

    def set_snooze(self):
        #60分後に再通知なので，default 30 +30 min
        self.snooze = self.snooze + 30*60
        playTapSound(self.tapvol)

    def set_oparate_volume(self,value):
        self.tapvol=value
        #value -> 0~99でのスライダの値，操作音量

    def set_alarm_volume(self,value):
        self.alarmvol=value
        #value -> 0~99でのスライダの値，アラーム音量

    def set_mealtime_breakfast(self,time):
        self.time_breakfast = time
        #print(time)

    def set_mealtime_lunch(self,time):
        self.time_lunch = time

    def set_mealtime_dinner(self,time):
        self.time_dinner = time



    def slider_breakfast(self,val):
        self.time_breakfast = QTime(5, 0, 0).addSecs(15*val*60)
        #print(self.time_breakfast)
        self.ui.timeEdit_breakfast_3.setDateTime(QDateTime(QDate(2000, 1, 2), self.time_breakfast))

            

    def slider_lunch(self,val):
        self.time_lunch = QTime(10, 0, 0).addSecs(15*val*60)
        print(self.time_lunch)
        self.ui.timeEdit_lunch_3.setDateTime(QDateTime(QDate(2000, 1, 2), self.time_lunch))


    def slider_dinner(self,val):
        self.time_dinner = QTime(17, 0, 0).addSecs(15*val*60)
        print(self.time_dinner)
        self.ui.timeEdit_dinner_3.setDateTime(QDateTime(QDate(2000, 1, 2), self.time_dinner))


        











#--------------------------------------------------------
#
#   全て飲まないを選択ー＞一括で飲まない操作
#   薬を飲んだ　　　　　ー＞1つずつの薬に対して飲む・飲まない（理由）を選択
#　 選択したら次の薬を表示，
#　 全て飲み終えたらトップに戻る
#   取り消しボタンで前の薬に戻る
#
#変数説明
#   self.mdcnlist_now       :その時点で飲むべき薬のリスト
#   self.disp_mdcn_nowpage  :表示されている薬のインデックス
#
#   例　self.mdcnlist[self.disp_mdcn_nowpage] で現在表示されている薬の情報を取得できる
#       listはjsonの中身と同じで，name,time, num,img_pathを持つ
#
#  例　self.mdcnlist[self.disp_mdcn_nowpage]['name']で表示されている薬の名前取得
#
#
#すでに書かれているコードは画像と変更と画面の遷移についてです．
#以下の10の関数について，実装をお願いします．
#
#---------------------------------------------------------------


   #「全て飲まない」を選択したあとの操作です

    def reason_wkup_late(self):
        #「起床時間が遅い」ボタンを押した処理
        self.record.setNotTakeReasonAll("wkup_late") #全部飲まない＆理由選択
        self.record.sendEmail() #Email発送
        self.ui.stackedWidget.setCurrentIndex(0) #top画面に戻る
        playTapSound(self.tapvol)
        

    def reason_bad_condition(self):
        #「体調不良」ボタンを押した処理
        self.record.setNotTakeReasonAll("bad_condition")
        self.record.sendEmail()
        self.ui.stackedWidget.setCurrentIndex(0)
        playTapSound(self.tapvol)

    def reason_have_no_mdcn(self):
        #「薬がない，忘れた」ボタンを押した処理
        self.record.setNotTakeReasonAll("have_no_mdcn")
        self.record.sendEmail()
        self.ui.stackedWidget.setCurrentIndex(0)
        playTapSound(self.tapvol)

    def reason_other(self):
        #「その他」ボタンを押した処理
        self.record.setNotTakeReasonAll("other")
        self.record.sendEmail()
        self.ui.stackedWidget.setCurrentIndex(0)
        playTapSound(self.tapvol)

    #以下は「薬を飲んだ」　あとの各薬に対しての操作です
    def mdcn_reset(self):
        #取り消しボタンを押した処理，前の薬に戻ります
        if(self.disp_mdcn_nowpage>0):
            self.disp_mdcn_nowpage-=1
            dispimg = QImage(self.mdcnlist_now[self.disp_mdcn_nowpage]['img_path'])
            Qdisp = QPixmap.fromImage(dispimg)
            QdispResized = Qdisp.scaled(180,130)
            self.ui.label_disp_mdcn_img_4.setPixmap(QdispResized)
            self.ui.label_disp_mdcn_name_4.setText(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['name'])
            playTapSound(self.tapvol)


    def mdcn_taken(self):
        #「薬を飲んだ」ボタンを押した処理
        self.record.setTakeEach(self.disp_mdcn_nowpage)
        playTapSound(self.tapvol)
        if(self.disp_mdcn_nowpage<len(self.mdcnlist_now)-1):
            self.disp_mdcn_nowpage+=1
            dispimg = QImage(self.mdcnlist_now[self.disp_mdcn_nowpage]['img_path'])
            Qdisp = QPixmap.fromImage(dispimg)
            QdispResized = Qdisp.scaled(180,130)
            self.ui.label_disp_mdcn_img_4.setPixmap(QdispResized)
            self.ui.label_disp_mdcn_name_4.setText(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['name'])

        else:
            self.disp_mdcn_nowpage = 0
            self.record.sendEmail()
            self.ui.stackedWidget.setCurrentIndex(0)

        


    def mdcn_no_late(self):
        #薬を飲まないー起床が遅い」ボタン
        playTapSound(self.tapvol)
        self.record.setNotTakeReasonEach(self.disp_mdcn_nowpage,"wkup_late")
        if(self.disp_mdcn_nowpage<len(self.mdcnlist_now)-1):
            self.disp_mdcn_nowpage+=1
            dispimg = QImage(self.mdcnlist_now[self.disp_mdcn_nowpage]['img_path'])
            Qdisp = QPixmap.fromImage(dispimg)
            QdispResized = Qdisp.scaled(180,130)
            self.ui.label_disp_mdcn_img_4.setPixmap(QdispResized)
            self.ui.label_disp_mdcn_name_4.setText(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['name'])
        
        else:
            self.disp_mdcn_nowpage = 0
            self.record.sendEmail()
            self.ui.stackedWidget.setCurrentIndex(0)



    def mdcn_no_badcon(self):
        #薬を飲まないー体調が悪い」ボタン
        playTapSound(self.tapvol)
        self.record.setNotTakeReasonEach(self.disp_mdcn_nowpage, "bad_condition")
        if(self.disp_mdcn_nowpage<len(self.mdcnlist_now)-1):
            self.disp_mdcn_nowpage+=1
            dispimg = QImage(self.mdcnlist_now[self.disp_mdcn_nowpage]['img_path'])
            Qdisp = QPixmap.fromImage(dispimg)
            QdispResized = Qdisp.scaled(180,130)
            self.ui.label_disp_mdcn_img_4.setPixmap(QdispResized)
            self.ui.label_disp_mdcn_name_4.setText(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['name'])
        
        else:
            self.disp_mdcn_nowpage = 0
            self.record.sendEmail()
            self.ui.stackedWidget.setCurrentIndex(0)



    def mdcn_no_havezero(self):
        playTapSound(self.tapvol)
        #「薬を飲まないー薬がない・忘れた」ボタン
        self.record.setNotTakeReasonEach(self.disp_mdcn_nowpage, "have_no_mdcn")
        if(self.disp_mdcn_nowpage<len(self.mdcnlist_now)-1):
            self.disp_mdcn_nowpage+=1
            dispimg = QImage(self.mdcnlist_now[self.disp_mdcn_nowpage]['img_path'])
            Qdisp = QPixmap.fromImage(dispimg)
            QdispResized = Qdisp.scaled(180,130)
            self.ui.label_disp_mdcn_img_4.setPixmap(QdispResized)
            self.ui.label_disp_mdcn_name_4.setText(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['name'])

        else:
            self.disp_mdcn_nowpage = 0
            self.record.sendEmail()
            self.ui.stackedWidget.setCurrentIndex(0)



    def mdcn_no_other(self):
        playTapSound(self.tapvol)
        #「薬を飲まないーその他」ボタン
        self.record.setNotTakeReasonEach(self.disp_mdcn_nowpage, "reason_other")
        if(self.disp_mdcn_nowpage<len(self.mdcnlist_now)-1):
            self.disp_mdcn_nowpage+=1
            dispimg = QImage(self.mdcnlist_now[self.disp_mdcn_nowpage]['img_path'])
            Qdisp = QPixmap.fromImage(dispimg)
            QdispResized = Qdisp.scaled(180,130)
            self.ui.label_disp_mdcn_img_4.setPixmap(QdispResized)
            self.ui.label_disp_mdcn_name_4.setText(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['name'])

        else:
            self.disp_mdcn_nowpage = 0
            self.record.sendEmail()
            self.ui.stackedWidget.setCurrentIndex(0)


#ボタン処理，ここまで
#------------------------------------------------------------------------

    def disp_mdcn_back(self):
        stopAlarm()
        playSelectSound(self.tapvol)
        if(self.disp_mdcn_nowpage>0):
            self.disp_mdcn_nowpage-=1
            self.ui.label_disp_mdcn_typenum.setText(str(len(self.mdcnlist_now))+'種類')
            self.ui.label_disp_mdcn_num.setText(str(self.mdcnlist_now[self.disp_mdcn_nowpage]['num'])+'錠')
            self.ui.label_page.setText(str(self.disp_mdcn_nowpage+1)+'/'+str(len(self.mdcnlist_now)))

            dispimg = QImage(self.mdcnlist_now[self.disp_mdcn_nowpage]['img_path'])
            Qdisp = QPixmap.fromImage(dispimg)
            QdispResized = Qdisp.scaled(180,130)
            self.ui.label_disp_mdcn_img.setPixmap(QdispResized)

            
            
    
    def disp_mdcn_next(self):
        stopAlarm()
        playSelectSound(self.tapvol)
        if(self.disp_mdcn_nowpage<len(self.mdcnlist_now)-1):
            self.disp_mdcn_nowpage +=1
            self.ui.label_disp_mdcn_typenum.setText(str(len(self.mdcnlist_now))+'種類')
            self.ui.label_disp_mdcn_num.setText(str(self.mdcnlist_now[self.disp_mdcn_nowpage]['num'])+'錠')
            self.ui.label_page.setText(str(self.disp_mdcn_nowpage+1)+'/'+str(len(self.mdcnlist_now)))
            dispimg = QImage(self.mdcnlist_now[self.disp_mdcn_nowpage]['img_path'])
            Qdisp = QPixmap.fromImage(dispimg)
            QdispResized = Qdisp.scaled(180,130)
            self.ui.label_disp_mdcn_img.setPixmap(QdispResized)


    #お薬情報表示
    def disp_mdcn_back_3(self):
        playSelectSound(self.tapvol)
        if(self.disp_mdcn_all_nowpage>0):
            self.disp_mdcn_all_nowpage -=1
            self.ui.label_disp_mdcn_num_3.setText(str(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['num'])+'錠')
            dispimg = QImage(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['img_path'])
            self.ui.label_disp_mdcn_name_3.setText(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['name'])
            self.ui.label_disp_mdcn_time_3.setText(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['time']+' 食後')
            self.ui.label_page_3.setText(str(self.disp_mdcn_all_nowpage+1)+'/'+str(len(self.mdcnlist_all)))
            Qdisp = QPixmap.fromImage(dispimg)
            QdispResized = Qdisp.scaled(240,150)
            self.ui.label_disp_mdcn_img_3.setPixmap(QdispResized)


    def disp_mdcn_next_3(self):
        playSelectSound(self.tapvol)
        if(self.disp_mdcn_all_nowpage<len(self.mdcnlist_all)-1):
            self.disp_mdcn_all_nowpage +=1
            self.ui.label_disp_mdcn_num_3.setText(str(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['num'])+'錠')
            dispimg = QImage(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['img_path'])
            self.ui.label_disp_mdcn_name_3.setText(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['name'])
            self.ui.label_disp_mdcn_time_3.setText(self.mdcnlist_all[self.disp_mdcn_all_nowpage]['time']+' 食後')
            self.ui.label_page_3.setText(str(self.disp_mdcn_all_nowpage+1)+'/'+str(len(self.mdcnlist_all)))

            Qdisp = QPixmap.fromImage(dispimg)
            QdispResized = Qdisp.scaled(240,150)
            self.ui.label_disp_mdcn_img_3.setPixmap(QdispResized)

    

    def loadDatabase(self):
        dataop = open('medicine_data/data.json','r', encoding='utf-8')
        data = json.load(dataop)

        self.mdcnlist_all=data['mdcn_data']
        self.mdcnlist_breakfast=[]
        self.mdcnlist_lunch=[]
        self.mdcnlist_dinner=[]

        for mdcn in data['mdcn_data']:#各薬についてのloop
            for t in mdcn['time']:#朝昼夜を確認
                if t =='朝':
                    self.mdcnlist_breakfast.append(mdcn)

                if t =='昼':
                    self.mdcnlist_lunch.append(mdcn)

                if t =='夜':
                    self.mdcnlist_dinner.append(mdcn)

        #print(self.mdcnlist_dinner)


    def alarmStart(self,s):
        self.loadDatabase()
        self.mdcnlist_now=[]
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
        dispimg = QImage(self.mdcnlist_now[self.disp_mdcn_nowpage]['img_path'])
        Qdisp = QPixmap.fromImage(dispimg)
        QdispResized = Qdisp.scaled(180,130)
        self.ui.label_disp_mdcn_img.setPixmap(QdispResized)
        self.ui.stackedWidget.setCurrentIndex(5)
        playAlarm(self.alarmvol)
        self.record.clearRecords() #以前までの服薬記録消去
        self.record.setRequiredMdcns(self.mdcnlist_now)  # 薬データ受け取り

    def updtTime(self):
        currentTime = QDateTime.currentDateTime().toString('hh:mm')
        self.ui.lcdNumber_clock.display(currentTime)
        self.ui.lcdNumber_clock_2.display(currentTime)
        self.ui.lcdNumber_clock_4.display(currentTime)
        self.ui.lcdNumber_clock_5.display(currentTime)

        todaysdate = QDateTime.currentDateTime().toString('yyyy/MM/dd')
        todaysdate_jp = todaysdate[0:4]+'年'+todaysdate[5:7]+'月'+todaysdate[8:]+'日'
        self.ui.label_date.setText(todaysdate_jp)
        self.ui.label_date_4.setText(todaysdate_jp)
        self.ui.label_date_2.setText(todaysdate_jp)
        self.ui.label_date_3.setText(todaysdate_jp)

        nowtime =QDateTime.time(QDateTime.currentDateTime())

        #朝食
        dtBrkfst = QTime.secsTo(self.time_breakfast,nowtime)#設定時間との差
        dtBrkfst = dtBrkfst - self.snooze #snoozeが設定されていたならば，その時間に
        if (dtBrkfst==0 and QTime.isValid(self.time_breakfast)):
            #朝食アラームの処理をここで
            self.alarmStart(1)

        #昼食
        dtlnch = QTime.secsTo(self.time_lunch,nowtime)#設定時間との差
        dtlnch = dtlnch - self.snooze #snoozeが設定されていたならば，その時間に
        if (dtlnch==0 and QTime.isValid(self.time_lunch)):
            # 昼食アラームの処理をここで
            self.alarmStart(2)

        #夕食
        dtdnr = QTime.secsTo(self.time_dinner,nowtime)#設定時間との差
        dtdnr = dtdnr - self.snooze #snoozeが設定されていたならば，その時間に
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
    window.showFullScreen()
    #swindow.show()
    
    sys.exit(app.exec_())
