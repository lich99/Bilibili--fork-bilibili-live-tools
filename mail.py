# -*- coding: utf-8 -*-

import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

'''
############################################################################################################
'''
mail_host =
mail_user =
mail_pass =
 
From = 
To = 
'''
############################################################################################################
'''
msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header(From, 'utf-8')
msgRoot['To'] =  Header(To, 'utf-8')
subject = '[Bilibili] Report'
msgRoot['Subject'] = Header(subject, 'utf-8')

sender = From
receivers = [To] 

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

with open(r'./stat/daliy_total.txt','r') as f:
    amount = f.readline()

def send():
    mail_msg = '<p>'+ 'Got  ' + amount + '  lotteries' +'</p>' + '<p>' + datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S") + '</p>'
    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host,25)    
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, msgRoot.as_string())
        print ("Success")
    except smtplib.SMTPException:
        print ("Error: Fail")
