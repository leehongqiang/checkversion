# -*- coding: utf-8 -*-
from pywinauto import application
import closepross
import locale
import pywinauto.controls.win32_controls as combox
from time import sleep
import shutil

class DrwStep:
    
    def __init__(self,appPath,appLanguage,appName):
        closepross.kill_process(['DRW.exe','DRWUI.exe'])
        application.Application.Start(appPath)
        self.appLanguage = appLanguage
        self.appName = appName
        sleep(5)
    def freeInstall(self):

        self.filedialog.TWizardForm.Next.Click()
        self.filedialog.TWizardForm.Accept.Click()
        try:
            self.setuppath=combox.EditWrapper(self.filedialog.TWizardForm.TEdit).GetProperties()['Texts'][0]
            print self.setuppath
            shutil.rmtree(self.setuppath)
        except:
            pass
        self.filedialog.TWizardForm.Confirm.DoubleClick()
        self.filedialog.TWizardForm.Install.Click()
        while 1:
            try:
                self.filedialog.TWizardForm.TNewCheckBox2.Click()
                self.filedialog.TWizardForm.Finish.Click()
                break
            except:
                pass
        return self.appName,1
    def trailInstall(self):
        self.filedialog.TWizardForm.Next.Click()
        self.filedialog.TWizardForm.Accept.Click()
        try:
            self.setuppath=combox.EditWrapper(self.filedialog.TWizardForm.TEdit).GetProperties()['Texts'][0]
            shutil.rmtree(self.setuppath)
        except:
            pass
        self.filedialog.TWizardForm.Confirm.DoubleClick()
        self.filedialog.TWizardForm.Next.DoubleClick()
        self.filedialog.TWizardForm.Install.Click()
        self.filedialog.TWizardForm.Install.Click()
        while 1:
            try:
                self.filedialog.TWizardForm.TNewCheckBox2.Click()
                self.filedialog.TWizardForm.Finish.Click()
                break
            except:
                pass
        return self.appName,1
    
    def xagonFreeInstall(self):
        self.xagonfiledialog[u'EaseUS Data Recovery Wizard 9.0 セットアップ'][u'次へ(&N) >'].Click()
        self.xagonfiledialog[u'EaseUS Data Recovery Wizard 9.0 セットアップ'][u'同意'].Click()
        try:
            self.setuppath=combox.EditWrapper(self.xagonfiledialog.TWizardForm.TEdit).GetProperties()['Texts'][0]
            print self.setuppath
            shutil.rmtree(self.setuppath)
            
        except:
            pass
        self.xagonfiledialog[u'EaseUS Data Recovery Wizard 9.0 セットアップ'][u'確認'].DoubleClick()
        self.xagonfiledialog[u'EaseUS Data Recovery Wizard 9.0 セットアップ'][u'インストール'].Click()
        while 1:
            try:
                self.xagonfiledialog.TWizardForm.TNewCheckBox2.Click()
                self.xagonfiledialog[u'EaseUS Data Recovery Wizard 9.0 セットアップ'][u'完了'].Click()
                break
            except:
                pass
        return self.appName,1
    def xagontTrailInstall(self):
        self.xagonfiledialog[u'EaseUS Data Recovery Wizard 9.0 セットアップ'][u'次へ(&N) >'].Click()
        self.xagonfiledialog[u'EaseUS Data Recovery Wizard 9.0 セットアップ'][u'同意'].Click()
        try:
            self.setuppath=combox.EditWrapper(self.xagonfiledialog.TWizardForm.TEdit).GetProperties()['Texts'][0]
            print self.setuppath
            shutil.rmtree(self.setuppath)
            
        except:
            pass
        self.xagonfiledialog[u'EaseUS Data Recovery Wizard 9.0 セットアップ'][u'確認'].DoubleClick()
        try:
            self.xagonfiledialog[u'EaseUS Data Recovery Wizard 9.0 セットアップ'][u'次へ(&N) >'].Click()
        except:
            pass
        self.xagonfiledialog[u'EaseUS Data Recovery Wizard 9.0 セットアップ'][u'インストール'].DoubleClick()
        #self.xagonfiledialog.TWizardForm.TNewButton3.DoubleClick()
        self.xagonfiledialog[u'EaseUS Data Recovery Wizard 9.0 セットアップ'][u'インストール(&I)'].Click()
        while 1:
            try:
                self.xagonfiledialog.TWizardForm.TNewCheckBox2.Click()
                self.xagonfiledialog[u'EaseUS Data Recovery Wizard 9.0 セットアップ'][u'完了'].Click()
                break
            except:
                pass
        return self.appName,1
    def isOS(self):
        
        if locale.getdefaultlocale()[0] == 'zh_CN':
            print locale.getdefaultlocale()[0]
            sleep(1)
            self.filedialog = application.Application().Connect_(title_re=ur'选择安装语言')
            combox.ComboBoxWrapper(self.filedialog.TSelectLanguageForm.TNewComboBox).Select(self.appLanguage)
            self.filedialog[u'选择安装语言'][u'确定'].Click()
        else:
            self.filedialog = application.Application().Connect_(title_re=ur'Select Setup Language')
            combox.ComboBoxWrapper(self.filedialog.TSelectLanguageForm.TNewComboBox).Select(self.appLanguage)
            self.filedialog.TSelectLanguageForm.OK.Click()
    def xagonDialog(self):
        self.xagonfiledialog = application.Application().Connect_(title_re=ur'EaseUS Data Recovery Wizard 9.0 セットアップ')
        
