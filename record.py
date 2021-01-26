
import mailsending

class RecordData:
    records = [{}]# 各薬についての服用記録
    all_records = {}# 全薬を一括で扱った場合について
    reasons = {"wkup_late": "起床時間が遅い",
               "bad_condition": "体調不良", "have_no_mdcn": "薬がない，忘れた", "reason_other": "その他"}
    states = {"take":"飲みました","not_take":"飲みませんでした"}

    def sendEmail(self):
        print(self.records)
        print(self.all_records)
        self.clearRecords()
        a = 0

    def clearRecords(self):
        self.records = [{}]
        self.all_records = []

    def setRequiredMdcns(self, li):
        self.records=li

    def setNotTakeReasonAll(self,reason):
        self.all_records = {"state":self.states["not_take"],"reason":self.reasons[reason]}

    def setNotTakeReasonEach(self,index,reason):
        self.records[index].update({"state": self.states["not_take"],"reason": self.reasons[reason]})
        #self.records[index].append({"state": self.states["not_take"], "reason": self.reasons[reason]})
        
    def setTakeEach(self,index):
        self.records[index].update({"state": self.states["take"]})
        #self.records[index].append({"state": self.states["take"]})
