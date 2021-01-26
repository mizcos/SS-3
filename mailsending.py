
# coding: utf-8

# In[3]:


from email.header import Header
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from datetime import datetime
dt=datetime.now()

class Email:

    def send_mail(self,record_contents):
        try:
            #mail server
            host_server = 'smtp.gmail.com'
            #mail user name
            sender_qq = 'CPI20.group1@gmail.com'
            # password
            pwd = 'CPI2020g1'
            # sender email
            sender_qq_mail = 'CPI20.group1@gmail.com'
            # receiver email
            receiver = 'CPI20.group1@gmail.com'

            # content
            mail_content = 'Titech様\n \n今日の服薬記録を送ります。\n \n名前:システム制御さん\n時間:' + dt.strftime( '%H:%M:%S' )        +'\n'+record_contents+'\n \n----\n服薬記録サービス'
            # title
            mail_title = '服薬記録送信'+dt.strftime( '%Y-%m-%d %H:%M:%S' )

            # ssl
            smtp = SMTP_SSL(host_server)
            # set_debuglevel()
            smtp.set_debuglevel(1)
            smtp.ehlo(host_server)
            smtp.login(sender_qq, pwd)

            msg = MIMEText(mail_content, "plain", 'utf-8')
            msg["Subject"] = Header(mail_title, 'utf-8')
            msg["From"] = sender_qq_mail
            msg["To"] = receiver
            smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
            smtp.quit()
            return True
        except Exception as e:
            print(e)
            return False
    if __name__ == '__main__':
        if send_mail():
            0

