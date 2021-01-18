
from PyQt5 import QtCore
import datetime

class format_mdcn_record:
    def __init__(self):
        self.date = 'yyyy/MM/dd hh:mm:ss';
        self.id = 0;
        self.cond = 'hoge';
        self.reason = ' ';
    def output(self):
        return [self.date, self.name, self.cond, self.reason];

class format_mdcn_information:
    # 使用されていないクラスだが，配列の中身の説明になるので一旦残す
    def __init__(self,id,name,image):
        self.id = id;
        self.name = name;
        self.image = image;

class format_ararm_setting:
    # 使用されていないクラスだが，配列の中身の説明になるので一旦残す
    def __init__(self,date,mdcn):
        self.date = date;
        # date = 'hh:mm'
        self.mdcn = mdcn;
        # mdcn = [ [id1, amount1],[id2,amount2],... ]

class variables:
    def __init__(self):
        self.ararm_sound_volume = 50;
        self.operation_sound_volume = 50;
        self.checking_mdcn_count = 0;
        # 服用記録の格納 一時保存変数に入れて，確定したらdbに入れる
        self.tmp_mdcn_record = format_mdcn_record();
        self.db_mdcn_record=[];
        # 薬のDB定
        self.db_mdcn_information = [];
        self.db_mdcn_information.append([1,"カロナール錠200","カロナール.jpg"]);
        self.db_mdcn_information.append([2,"ナテグリニド錠30mg「テバ」","ナテグリニド_テバ.jpg"]);
        self.db_mdcn_information.append([3,"ネキシウムカプセル20mg","ネキシウム.jpg"]);
        self.db_mdcn_information.append([4,"ユベラNカプセル100mg","ユベラN.jpg"]);
        self.db_mdcn_information.append([5,"レバミピド錠100mg「オーツカ」","レバミピド_オーツカ.jpg"]);
        self.db_mdcn_information.append([6,"ロスバスタチン錠2.5mg「DSEP」","ロスバスタチン_DSEP.jpg"]);
        # アラームの設定
        self.list_ararm_setting = [];
        self.list_ararm_setting.append(['7:00',[[1,3],[2,1],[3,2]]]);
        self.list_ararm_setting.append(['12:00',[[1,3],[4,1],[5,1]]]);
        self.list_ararm_setting.append(['17:00',[[1,3],[2,1],[3,2],[6,1]]]);

    def push_mdcn_record(self):
        # 一時保存されている服用記録をDBに入れる
        self.tmp_mdcn_record.date = QDateTime.currentDateTime().toString('yyyy/MM/dd hh:mm:ss');
        self.db_mdcn_record.append(self.tmp_mdcn_record.output());

