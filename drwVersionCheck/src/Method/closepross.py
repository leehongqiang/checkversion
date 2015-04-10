# -*- coding: utf-8 -*-
import os

def check_exsit(process_name):
    import win32com.client
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
    if len(processCodeCov) > 0:
        print '%s is exists' % process_name
        command = 'taskkill /F /IM %s' %process_name #比如杀死QQ进程
        os.system(command)
    else:
        print '%s is not exists' % process_name
def kill_process(pro):
    for i in pro:
        check_exsit(i)