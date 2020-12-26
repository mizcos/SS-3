import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from top_ui import Ui_TopWindow
import datetime

class gui(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(gui, self).__init__(parent)
        self.ui = Ui_TopWindow()
        self.ui.setupUi(self)

    def pressed_setting (self):
        a=1#設定ボタンが押されたときの処理

    def pressed_mdcn_info(self):
        a=1#お薬情報ボタンが押されたときの処理
    
    def pressed_mdcn_record(self):
        a=1#服薬記録ボタンが押されたときの処理

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


