import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui.ui_stacked import Ui_MainWindow
from variable_define import variables
import datetime

class gui(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(gui, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.var = variables()

    def gopage_setting (self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def gopage_top(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def gopage_mdcn_info(self):
        self.ui.stackedWidget.setCurrentIndex(11)
        
    def gopage_mdcn_record(self):
        self.ui.stackedWidget.setCurrentIndex(12)


    def gopage_set_adress(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def gopage_set_mealtime(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def gopage_set_volume(self):
        self.ui.stackedWidget.setCurrentIndex(4)


    def slct_yes(self):
        #「薬を飲んだ」ボタンを押した処理
        self.var.tmp_mdcn_record.cond="薬を飲んだ";
        self.var.push_mdcn_record();

    def slct_yet(self):
        #「食事がまだ」ボタンを押した処理
        self.var.tmp_mdcn_record.cond="食事がまだ";
        self.var.push_mdcn_record();

    def slct_no(self):
        #「飲んでいない」ボタンを押した処理
        self.var.tmp_mdcn_record.cond="飲んでいない";
        # まだdbにはpushしない

    def set_snooze(self):
        #「薬を飲んだ」ボタンを押した処理
        a=1;

    def set_oparate_volume(self,value):
        #value -> 0~99でのスライダの値，操作音量
        self.var.operation_sound_volume = value;

    def set_alarm_volume(self,value):
        #value -> 0~99でのスライダの値，アラーム音量
        self.var.ararm_sound_volume = value;

    def set_mealtime_breakfast(self):
        a=1

    def set_mealtime_lanch(self):
        a=1

    def set_mealtime_dinner(self):
        a=1

    def reason_wkup_late(self):
        #「起床時間が遅い」ボタンを押した処理
        self.var.tmp_mdcn_record.reason="起床時間が遅い";
        self.var.push_mdcn_record();

    def reason_bad_condition(self):
        #「体調不良」ボタンを押した処理
        self.var.tmp_mdcn_record.reason="体調不良";
        self.var.push_mdcn_record();

    def reason_have_no_mdcn(self):
        #「薬がない，忘れた」ボタンを押した処理
        self.var.tmp_mdcn_record.reason="薬がない，忘れた";
        self.var.push_mdcn_record();

    def reason_other(self):
        #「その他」ボタンを押した処理
        self.var.tmp_mdcn_record.reason="その他";
        self.var.push_mdcn_record();

    def disp_mdcn_back(self):
        self.var.checking_count -= 1;
        if self.var.checking_count<0:
            self.var.checking_count = 0;
        self.var.tmp_mdcn_record.id = self.var.list_ararm_setting[self.var.checking_count][0];

    def disp_mdcn_next(self):
        self.var.checking_count += 1;
        if self.var.checking_count>10:
            # TODO : 上限の値指定
            self.var.checking_count = 10;
        self.var.tmp_mdcn_record.id = self.var.list_ararm_setting[self.var.checking_count][0]

    
    def updtTime(self):
        currentTime = QDateTime.currentDateTime().toString('hh:mm')
        self.lcdNumber_clock.display(currentTime)
        todaysdate = QDateTime.currentDateTime().toString('yyyy/MM/dd')
        todaysdate_jp = todaysdate[0:4]+'年'+todaysdate[5:7]+'月'+todaysdate[9:]+'日'
        self.label_date.setText(todaysdate_jp)

    def keyPressEvent(self, e):#escで終了
        if e.key() == Qt.Key_Escape: 
            sys.exit(app.exec_())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = gui()
    window.showFullScreen()
    window.show()
    sys.exit(app.exec_())
