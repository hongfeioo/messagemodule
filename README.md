# messagemodule
send mail or  message module










[调用方法]

import sys
if not "/root/messagemodule" in sys.path:
    sys.path.append("/root/messagemodule")
import messageMode

messageMode.sendtxtmail('hello baby mail title',0,mail_msg,muti_mail,begintime)
