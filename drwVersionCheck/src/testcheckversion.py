# -*- coding: utf-8 -*-
from Method.isislversion import ReadIsl
from Method.checkgui import maincheckgui
import Method.drwuninstall
from Method.drwinstall import DrwStep
import Resource
import unittest
import HTMLTestRunner
import re
import os
import ConfigParser
import time
from time import sleep
from Method import closepross



class DrwCheckVersion(unittest.TestCase):
    
    def setUp(self):
        self.idlist=['EaseusRegisterInfo',
                     'EaseusLaunch',
                     'InstallTalk',
                     'SetupIsrunning',
                     'EaseusAppName',
                     'EaseusDirName',
                     'EaseusCopyright',
                     'EaseusRun',
                     'EaseusUninstallComment',
                     'ProgramOnTheWeb ',
                     'EaseusPublish'
                     ]
        self.versionlist = [
                            'EaseusRegisterInfo',
                            'EaseusAppName',
                            'EaseusUninstallComment'
                            ]
        self.CompareVersionNum = '9.0'
        self.CompareAppName = 'EaseUS'
        self.newidlist=[]
        self.newversionlist = []
        
    def test_step_check_appname(self):
        #print u"结果"
        print u'对比字段总数为',len(self.idlist)
        getfilename,getstepname = getiInfo()
        for path,dics,files in getfilename:
            lispath =os.listdir(path)
            for fn in lispath:
                filelist = os.path.splitext(fn)
                if  filelist[1] == '.isl':
                    filename = filelist[0]
                    filepath = os.path.abspath(path+'\\'+fn)
                    print filename
                    readisl = ReadIsl(filename,filepath)
                    aa = readisl.getfile()
                    #print u'对比字段总数为',len(self.idlist)
                    for key in aa:
                        for ids in self.idlist:
                            if ids == key:
                                try:
                                    self.assertIn(self.CompareAppName,aa[key].encode('utf-8'))
                                    #print key,':',aa[key]
                                    self.newidlist.append(ids)
                                except :
                                    print 'NOPASS',id,key,':',aa[key]
                            else:
                                pass

        for ids in self.idlist: 
            self.assertIn(ids, self.newidlist)
            
    def test_step_check_appversion(self):
        #print u"结果"
        print u'对比字段总数为',len(self.versionlist)
        getfilename,getstepname = getiInfo()
        for path,dics,files in getfilename:
            lispath =os.listdir(path)
            for fn in lispath:
                filelist = os.path.splitext(fn)
                if  filelist[1] == '.isl':
                    filename = filelist[0]
                    filepath = os.path.abspath(path+'\\'+fn)
                    print filename
                    readisl = ReadIsl(filename,filepath)
                    aa = readisl.getfile()
                    #print u'对比字段总数为',len(self.idlist)
                    for key in aa:
                        for ids in self.versionlist:
                            if ids == key:
                                try:
                                    self.assertIn(self.CompareVersionNum,aa[key].encode('utf-8'))
                                    #print key,':',aa[key]
                                    self.newversionlist.append(ids)
                                except :
                                    print 'NOPASS',id,key,':',aa[key]
                            else:
                                pass
        #print self.newversionlist
        for ids in self.versionlist: 
            self.assertIn(ids, self.newversionlist)
        
    def test_gui_check_appversion(self):
        self.gui_check_appversion()
    
    def test_gui_check_appname(self):
        self.gui_check_appname()
        
    def test_step_check_stepversion(self):
        pass
    
    def gui_check_appversion(self):
        resut = maincheckgui()
        #print resut
        print u'检查语言共%s种' % len(resut)
        for list1 in range(len(resut)):
            ispass = resut[list1][1]
            languages = resut[list1][0]
            compaerResult = resut[list1][2]
            if ispass == 'Pass':
                try:
                    self.assertIn(self.CompareVersionNum, compaerResult)
                    print 'PASS',languages,'<<%s>>' % ispass,compaerResult
                except:
                    print 'PASS',languages,'<<%s>>' % ispass,compaerResult
            elif ispass == 'Both':
                
                try:
                    self.assertIn(self.CompareVersionNum, compaerResult[0])
                except:
                    print 'NOPASS',languages,'<<Title>>',compaerResult[0]
                try:
                    #check about version
                    self.assertIn(self.CompareVersionNum, compaerResult[1])
                except:
                    print 'NOPASS',languages,'<<About>>',compaerResult[1]
            elif ispass == 'Title':
                try:
                    self.assertIn(self.CompareVersionNum, compaerResult)
                except:
                    print 'NOPASS',languages,'<<%s>>' % ispass,compaerResult
            elif ispass == 'About':
                try:
                    self.assertIn(self.CompareVersionNum, compaerResult)
                except:
                    print 'NOPASS',languages,'<<%s>>' % ispass,compaerResult
                    
    def gui_check_appname(self):
        resut = maincheckgui()
        #print resut
        print u'检查语言共%s种' % len(resut)
        for list1 in range(len(resut)):
            ispass = resut[list1][1]
            languages = resut[list1][0]
            compaerResult = resut[list1][2]
            if ispass == 'Both':
                try:
                    self.assertIn(self.CompareAppName, compaerResult[0])
                    print 'PASS',languages,'<<Title>>',compaerResult[0]
                except:
                    print 'NOPASS',languages,'<<Title>>',compaerResult[0]
                try:
                    #check about version
                    self.assertIn(self.CompareAppName, compaerResult[1])
                    print 'PASS',languages,'<<About>>',compaerResult[1]
                except:
                    print 'NOPASS',languages,'<<About>>',compaerResult[1]
            else:
                try:
                    self.assertIn(self.CompareAppName, compaerResult)
                    print 'PASS',languages,'<<%s>>' % ispass,compaerResult
                except:
                    print 'NOPASS',languages,'<<%s>>' % ispass,compaerResult
                    
    def tearDown(self):
        pass
    
def appstep():
    config=ConfigParser.ConfigParser()
    config.readfp(open('drw_info.ini'))
    appLanguage = config.get("Language","DRW_Language")
    
    getfilename,getstepname = getiInfo()
    for path,dics,files in getstepname:
        lispath =os.listdir(path)
        for fn in lispath:
            filelist = os.path.splitext(fn)
            if  filelist[1] == '.exe' and filelist[0].split('_')[1] =='Free':
                filename = filelist[0]
                filepath = os.path.abspath(path+'\\'+fn)
                aa = Method.drwuninstall.DrwUninstall().uninstall()
                sleep(10)
                closepross.kill_process(['_iu14D2N.tmp'])
                nowStep = DrwStep(filepath,appLanguage,filename)
                nowStep.isOS()
                nowStep.freeInstall()
            else:
                pass

def getiInfo():
    
    filePath = os.getcwd()+'\\Resource\\\Languages\\'
    stepPath = os.getcwd()+'\\Resource\\\drw\\'
    #print filePath
    getfilename = os.walk(filePath)# 遍历路径下的文件
    getstepname = os.walk(stepPath)
    '''
    for path,dics,files in getfilename:
            lispath =os.listdir(path)
            for fn in lispath:
                filelist = os.path.splitext(fn)
                if  filelist[1] == '.isl':
                    filename = filelist[0]
                    filepath = os.path.abspath(path+'\\'+fn)
                    print filepath,'---',filename
    '''
    return getfilename,getstepname


    

if __name__ == "__main__":
    
    #appstep()
    

    testunit = unittest.TestSuite()
    testunit.addTest(DrwCheckVersion("test_step_check_appname"))
    testunit.addTest(DrwCheckVersion("test_step_check_appversion"))
    testunit.addTest(DrwCheckVersion("test_gui_check_appversion"))
    testunit.addTest(DrwCheckVersion("test_gui_check_appname"))
    tiems = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    filename = os.getcwd()+u'\\report\\%s测试报告.html'% tiems
    fp = file(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(
                                          stream=fp,
                                          title=u'DRW产品名称和版本号检测',
                                          description=u'用例执行情况：')
    #运行测试用例
    runner.run(testunit)
    #关闭报告文件
    fp.close()

