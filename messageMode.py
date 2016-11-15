
#!/usr/bin/python
#coding=utf-8
#filename: messageMode.py
 
import telnetlib
import os,sys,commands,multiprocessing
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import urllib2


#---init---
begintime =  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
muti_phone='13521161000'
muti_mail='yhf@XXXX.com'
pythonlog ='/home/sms_mail.log'

sender = 'hxx@163.com'
smtpserver = 'hxx.163.com'
username = 'hxx@163.com'
password = 'password'
 
#----------
 

def sendtxtmail(_subject,_mail_off,_msg,_fuc_mail,_begintime):
    for mail_index in range(0, len(_fuc_mail.split(';'))):
        if _mail_off == 1:
            break
        _receiver =  _fuc_mail.split(';')[mail_index]
        if _receiver.find('null') == -1:
            try:
                msg = MIMEText('<html>'+_msg+'</html>','html','utf-8')
                msg['Subject'] =  _subject
                msg['to'] = _receiver
                smtp = smtplib.SMTP()
                smtp.connect(smtpserver)
                smtp.login(username, password)
                smtp.sendmail(sender,_receiver, msg.as_string())
                smtp.quit()
                os.system("echo "+_begintime+' '+_subject+' '+_receiver+" mail send successful >> "+pythonlog)
                print "mail send successful"
            except Exception,e:
                print "mail send fail"
                print e[1]
                os.system("echo "+_begintime+' '+_subject+' '+_receiver+" mail send fail ,Code: "+str(e[0])+' '+e[1].split()[0]+'- -! >>'+pythonlog)
    return 'mail func over'




def main(arg_msg):
    sendtxtmail('test_subject',0,arg_msg,muti_mail,begintime)
    return 'main func over'

        

if __name__ == "__main__":
   print main(sys.argv[1])
