#encoding=utf-8
import ConfigParser
import codecs
import os
import _winreg
import platform

#=================================================================
#读取Ini文件中的信息
class readIniFile():
    def __init__(self):
        self.cf=ConfigParser.ConfigParser()
        self.fpath_ini=codecs.open(os.getcwd()+'\\Info.ini','r','utf-16')
        self.cf.readfp(self.fpath_ini)

    def getPath(self,name):
        self.path=[]
        self.list1=self.cf.items(name)
        for i in self.list1:
            self.path.append(i[1])
        return self.path
    
#=================================================================
#获取注册表信息
class Registry():
    
    def __init__(self,basekey,subkey,valueName):
        self.basekey=basekey
        self.subkey=subkey
        self.valueName=valueName
        self.subkey1 = 'can not find the file'

    def getKey(self):
        self.sysBit=platform.machine().lower()
        if self.sysBit=='amd64':
            self.flag=_winreg.KEY_READ | _winreg.KEY_WOW64_64KEY
        else:
            self.flag=_winreg.KEY_READ
            
        HKLM=_winreg.HKEY_LOCAL_MACHINE
        self.key=_winreg.OpenKey(HKLM,self.subkey,0,self.flag)
        return self.key
#获取DRW在注册表的卸载路径    
    def getSubKey(self,versionName):
        self.PyHKEY=self.getKey()
        self.count=_winreg.QueryInfoKey(self.key)[0]
        self.valueName=versionName
        for index in range(self.count):
            self.name=_winreg.EnumKey(self.key,index)
            if self.valueName in self.name.decode('gbk'):
                self.subkey1=self.subkey+'\\'+self.name
        return self.subkey1
        
#获取DRW安装路径    
    def getKeyValue(self):
        self.PyHKEY=self.getKey()
        self.installPath=_winreg.QueryValueEx(self.PyHKEY,self.valueName)[0]
        _winreg.CloseKey(self.PyHKEY)
        return self.installPath
            
#=================================================================
class DATInfo():
    def __init__(self,language_path,version_flag,proPath,versionName):
        self.language_path=language_path
        self.flag1=version_flag[0]
        self.flag2=version_flag[1]
        self.tempVersion=[]
        self.proPath=proPath
        self.versionName=versionName
        self.ver_result=[]
        
    def getFileInfo(self):
        for item in self.language_path:
            self.fPath=self.proPath+item
            self.f=codecs.open(self.fPath,'r','utf-16')
            self.line = self.f.readlines()
            self.fileVersion=[]
            for i in self.line:
                if i[0:len(self.flag1)].lower()==self.flag1 or i[0:len(self.flag2)].lower()==self.flag2:            
                    self.fileVersion.append(i.strip('\r\n'))
            self.tempVersion.append([item[0:-4],self.fileVersion])
        return self.tempVersion
     
    def CompareVer(self):
        for item in self.getFileInfo():
            if item[1][0][len(self.flag1)+1:]==self.versionName and item[1][1][len(self.flag2)+1:] == self.versionName:
                self.ver_result.append([item[0],'Pass',item[1][0][len(self.flag1)+1:]])
            elif item[1][0][len(self.flag1)+1:]==self.versionName and item[1][1][len(self.flag2)+1:] != self.versionName:
                self.ver_result.append([item[0],'About',item[1][1][len(self.flag2)+1:]])
            elif item[1][0][len(self.flag1)+1:]!=self.versionName and item[1][1][len(self.flag2)+1:] == self.versionName:
                self.ver_result.append([item[0],'Title',item[1][0][len(self.flag1)+1:]])
            else:
                self.ver_result.append([item[0],'Both',[item[1][0][len(self.flag1)+1:],item[1][1][len(self.flag2)+1:]]])
        return self.ver_result
#=================================================================
def maincheckgui():
    path=readIniFile()
    regPath=path.getPath('registry')

    versionName=path.getPath('version')[0]

    language_path=path.getPath('DATFile')

    version_flag=path.getPath('version_flag')

    #Registry(PyHKEY,subkey,valueName)
    reg=Registry(regPath[0],regPath[1],regPath[2])
    versionPath=reg.getSubKey(versionName)    
    reg1=Registry(regPath[0],versionPath,regPath[2])
    proPath=reg1.getKeyValue()
    DRW_version=DATInfo(language_path,version_flag,proPath,versionName)
    return DRW_version.CompareVer()

    

    


        