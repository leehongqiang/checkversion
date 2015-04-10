# -*- coding: utf-8 -*-
import _winreg
import os
import closepross
import checkgui
import ConfigParser
import codecs
from multiprocessing import Process
import threading
from time import sleep
import subprocess
class DrwUninstall:
    def __init__(self):
        self.getFiledialog()
        #closepross.kill_process(['_iu14D2N.tmp','firefox.exe'])
        
        
    def getFiledialog(self):
        self.path=checkgui.readIniFile()
        self.regPath=self.path.getPath('registry')
        self.checkpath = checkgui.Registry(self.regPath[0],self.regPath[1],self.regPath[2])
        self.regPath=self.path.getPath('registry')
        self.versionName=self.path.getPath('version')[0]
        self.drwuninstall = self.checkpath.getSubKey(self.versionName)
        try:
            self.uninstallkey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
                                                self.drwuninstall,
                                                0,_winreg.KEY_READ | _winreg.KEY_WOW64_64KEY)
            self.path_value, self.type = _winreg.QueryValueEx(self.uninstallkey, "UninstallString")
            return self.path_value
        except:
            self.uninstallkey = False
            
    def uninstall(self):
        if self.uninstallkey:
            #print self.getFiledialog()
            prosss = [self.getFiledialog(),os.getcwd()+'\\drw_uninstall.exe']
            for i in prosss:
                print i
                process = subprocess.Popen(i)
                pid = process.pid
            return 1
            
        else:   
            return False
            print '----please install drw----'

        