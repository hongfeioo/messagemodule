
#!/usr/bin/python
#coding=utf-8

import time
import messageMode


  
muti_mail = 'yhf@153.com,xxd@163.com,test@sina.com'
arg_msg = 'baby,Remember to drink water,mutou~'
begintime =  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
 
messageMode.sendtxtmail('hello baby',0,arg_msg,muti_mail,begintime)
