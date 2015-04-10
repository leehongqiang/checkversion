# -*- coding: utf-8 -*-
import codecs
import re

class ReadIsl:
    def __init__(self,fileName,filePath):
        self.Ucs = {'BrazilianPortuguese':'1252',
               'Chinese':'936',
               'ChineseTrad':'950',
               'Dutch':'1252',
               'English':'utf-8',
               'French':'1252',
               'German':'1252',
               'Italian':'1252',
               'Japanese':'932',
               'Spanish':'1252'
               }
        self.fileName = fileName
        self.filePath = filePath
        self.listapp1 = []
        self.listapp2 = []
        
    def getfile(self,):
        strs = codecs.open(self.filePath,'r',self.Ucs[self.fileName])
        c = strs.readlines()
        lange = len(self.fileName)
        for i in c:
            restr = 'EaseUS'
            x = re.findall(restr, i,re.I)
            if x:
                applist = i.split('=')
                if applist[0][-lange:] == self.fileName:
                    self.listapp1.append(applist[0][:-lange])
                    self.listapp2.append(applist[1])
                else:
                    self.listapp1.append(applist[0])
                    self.listapp2.append(applist[1])
        dics = dict(zip(self.listapp1,self.listapp2))
        return dics
    
'''   
aa = readisl('French',r'C:\DRWStep\Languages\French.isl')
ada= aa.getfile()

for key in ada:
            print key,':',ada[key].encode('utf-8')
'''
#EaseusRegisterInfo
#EaseusLaunch
#InstallTalk
#SetupIsrunning
#EaseusAppName
#EaseusDirName
#EaseusCopyright
#EaseusRun
#EaseusUninstallComment
#ProgramOnTheWeb 