
from mailsending import Email

class RecordData:
    records = [{}]# 各薬についての服用記録
    all_records = {}# 全薬を一括で扱った場合について
    reasons = {"wkup_late": "起床時間が遅い",
               "bad_condition": "体調不良", "have_no_mdcn": "薬がない，忘れた", "reason_other": "その他"}
    states = {"take":"飲みました","not_take":"飲みませんでした"}
    record_contents = ""# メールの服薬記録部分
    email = Email()

    def sendEmail(self):
        print(self.records)
        print(self.all_records)
        self.makeMailRecordContent()
        print(self.record_contents)
        #self.email.send_mail(self.record_contents)
        self.clearRecords()
        a = 0

    def clearRecords(self):
        self.records = [{}]
        self.all_records = []
        self.record_contents = []

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

    def makeMailRecordContent(self):
        if self.all_records:#全記録が空か判定
            self.record_contents += "全ての薬を飲みませんでした．理由は「" +self.all_records["reason"]+ "」です．\n"
            self.record_contents += "<飲むべきだった薬>\n"
            for mdcn in self.records:
                self.record_contents += mdcn["name"]+"　"+str(mdcn["num"])+"錠\n"
        else:
            self.record_contents += "<服薬情報>\n"
            for mdcn in self.records:
                self.record_contents += mdcn["name"]+"　"+str(mdcn["num"]) + "錠 : "+mdcn["state"]
                if "reason" in mdcn:
                    self.record_contents += "("+mdcn["reason"]+")\n"
                else:
                    self.record_contents += "\n"
