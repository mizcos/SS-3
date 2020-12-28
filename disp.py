import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui.ui_stacked import Ui_MainWindow
import datetime

class gui(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(gui, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def gopage_setting (self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def gopage_top(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def gopage_mdcn_info(self):
        a=1
        
    def gopage_mdcn_record(self):
        a=1#服薬記録ボタンが押されたときの処理


    def gopage_set_adress(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def gopage_set_mealtime(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def gopage_set_volume(self):
        self.ui.stackedWidget.setCurrentIndex(4)


    def slct_yes(self):
        a=1

    def slct_yet(self):
        a=1

    def slct_no(self):
        a=1

    def set_snooze(self):
        a=1

    def set_oparate_volume(self):
        a=1

    def set_alarm_volume(self):
        a=1

    def set_mealtime_breakfast(self):
        a=1

    def set_mealtime_lanch(self):
        a=1

    def set_mealtime_dinner(self):
        a=1

    def reason_wkup_late(self):
        a=1

    def reason_bad_condition(self):
        a=1

    def reason_have_no_mdcn(self):
        a=1

    def reason_other(self):
        a=1

    def disp_mdcn_back(self):
        a=1
    
    def disp_mdcn_next(self):
        a=1

    
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
    #window.showFullScreen()
    window.show()
    sys.exit(app.exec_())


