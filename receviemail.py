
# coding: utf-8

# In[12]:


import imaplib , email , os , json
#mail id
emailuser = "CPI20.group1@gmail.com"
emailpasswd = "CPI2020g1"
 
conn = imaplib.IMAP4_SSL('imap.gmail.com', 993)
conn.login(emailuser,emailpasswd)
 
conn.list()     
#Inbox file
conn.select('INBOX')    
 
result , dataid = conn.uid ( 'search' , None , "ALL" )
 
mailidlist = dataid[0].split ()     

def get_body(msg):
    if msg.is_multipart ():
        return get_body ( msg.get_payload ( 0 ) )
    else:
        return msg.get_payload ( None , decode=True )

nnn = len(mailidlist)
result , data = conn.fetch ( mailidlist[nnn-7] , '(RFC822)' )
e = email.message_from_bytes ( data[0][1] )
subject = email.header.make_header ( email.header.decode_header ( e['SUBJECT'] ) )
mail_from = email.header.make_header ( email.header.decode_header ( e['From'] ) )

#メール内容
body = str ( get_body ( e ) , encoding='utf-8' )    # utf-8 gb2312 GB18030
conn.logout()

#key word
k1 = body.find(">")
k2 = body.find(" ",k1)
k3 = body.find("間")
k11 = body.find("錠",k1)
jsontext = {'mdcn_data':[{"name":body[k1+2:k2-2],"time":body[k3+2:k3+10],"num":int(body[k2-2:k2-1]),"img_path":"medicine_data/"+body[k1+2:k11]+".jpg"}]}
jsondata = json.dumps(jsontext,indent=4,separators=(',', ': '),ensure_ascii=False)


# make json file
f = open('data.json', 'w' ,  encoding='utf-8')
f.write(jsondata)
f.close()

