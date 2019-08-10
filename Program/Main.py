import time
import requests
import os

former=time.strftime("%Y%m%d%H%M%S",time.localtime())

def checkTime():
  return time.strftime("%Y%m%d%H%M%S",time.localtime())

def checkTimeIfOK(former,timedata):
    if eval(timedata)-eval(former)>15:
        return True
    else:
        return False

def sendAPIcheckRequest(BTCaddress):
    url='https://blockchain.info/q/addressbalance/'
    temp=url+BTCaddress
    answer=requests.get(temp)
    return answer.content

ReadFile=open("../Import/GeneratedAdd","r")
WriteFile=open("../Import/Hacked",'a')
CompFile=open("../Import/Comp.html",'r')
for eachline in ReadFile.readlines():
    flag=True
    count=-1
    while flag!=False:
        count=count+1
        if not eachline[count].isalnum():
            flag=False
    PublicKey=eachline[0:count-1]
    PrivKey=eachline[count+1:]
    while not checkTimeIfOK(former,checkTime()):
        pass
    amount=sendAPIcheckRequest(PublicKey)
    print(PublicKey+" Checked.")
    if amount==b'0':
        print("Nothing inside.")
    else:
        WriteFile.write(PrivKey+"\n")
        print("Have BTC")
    print("**********")
ReadFile.close()
WriteFile.close()
CompFile.close()

import smtplib
smtp=smtplib.SMTP("smtp.qq.com",25)
smtp.login("2821341767","jsqddzqumxgddhbc")
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
Words='''
Congratulations : BTC Address Searching completed.
Now you can go to " Hacked " file to check and get some EARNINGS.
For further information, go to this "https:www.blockchain.info/q/addressbalance/" link.
'''
sender = '2821341767@qq.com'
receivers = ['2821341767@qq.com','513044524@qq.com','cwtg@outlook.com']
message = MIMEText(Words, 'plain', 'utf-8')
message['From'] = Header("PythonCheckSystem", 'utf-8')
message['To'] = "iwtywai"
subject = 'Congratulations : BTC Address Searching completed.'
message['Subject'] = Header(subject, 'utf-8')
try:
    smtp.sendmail(sender,receivers,message.as_string())
    print ("Comfirmation Email Sent Successfully!")
except smtplib.SMTPException:
    print ("Error: Failed to send Confirmation email.")
