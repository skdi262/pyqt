import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import os
import time
import subprocess
from requests import get
from datetime import datetime
from Socket_Singleton import Socket_Singleton

Socket_Singleton(address="127.0.0.1", port=1337, timeout=0, client=True, strict=True)

now_file = os.getcwd()
form_class = uic.loadUiType(now_file +r"\uis\untitled2.ui")[0]
np_user_class = uic.loadUiType(now_file +r"\uis\np_user.ui")[0]
reboot_class = uic.loadUiType(now_file +r"\uis\reboot_data.ui")[0]
se_list_class = uic.loadUiType(now_file +r"\uis\se_list.ui")[0]
newbie_class = uic.loadUiType(now_file +r"\uis\newbie.ui")[0]
find_id_class = uic.loadUiType(now_file +r"\uis\find_id.ui")[0]


class reboot_data(QDialog,reboot_class):
    def __init__(self, parent):
        super(reboot_data,self).__init__(parent)
        self.setupUi(self)
        self.asdasd()
        self.show()
        

    def asdasd(self):
        mw = MyWindow()
        RT = mw.reboot_time
        for i in range(len(RT)):
            print(RT[i])
            AAA = str(i+1) + " / " +str(RT[i])
            self.plainTextEdit.appendPlainText(AAA)



class reboot(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        
        self.parent.yellow.hide()
        self.parent.red.hide()
        self.parent.green.hide()
        self.parent.off_air()
        subprocess.run('adb shell input tap 0 0',shell=True)        
        st_asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd = st_asd.readline(5).decode('utf-8').strip()        
        
        if st_asd == 'error'or st_asd =='adb.e' or st_asd =="" or st_asd == "adb.:" or st_asd =='ad: m' :
            self.parent.yellow.show()
            self.parent.red.show()            
            
        else:
            self.parent.yellow.show()
            self.parent.red.show()
            self.parent.stop_th()
            self.parent.pushButton_2.setEnabled(False)
            self.parent.pushButton_3.setEnabled(False)
            self.parent.pushButton_4.setEnabled(False)            
            self.parent.pushButton_7.setEnabled(False)
            
            self.parent.label_9.setText("")
            self.parent.off_air()
            now = datetime.now()
            nowRT = now.strftime("%m/%d %H:%M")
            self.parent.reboot_time.append(nowRT)
            time.sleep(0.5)
            subprocess.run("adb reboot",shell=True)
            time.sleep(20)
            for i in range(15):
                bbs=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
                bbs = bbs.read().decode('utf-8').strip()
                bbs= bbs.split("\n")
                csd = bbs[0][:5].strip()
                print(csd)
                if csd == 'error' or csd=='adb.e' or csd =="" or csd =='adb:' or csd == "adb.:"  or csd == "* dae" or csd =="ad: m":
                    time.sleep(5)
                    print(csd)        
                else:
                    print(csd)
                    break
            if csd == 'error' or csd=='adb.e' or csd =="" or csd =='adb:' or csd == "adb.:"  or csd == "* dae" or csd =="ad: m":
                time.sleep(10)
                subprocess.run("adb shell input keyevent 3",shell=True)
                time.sleep(0.5)
                subprocess.run("adb shell input keyevent 3",shell=True)
                time.sleep(0.5)
                subprocess.run('adb shell input tap 0 0',shell=True)                
                asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
                asd = asd.read().decode('utf-8').strip()
                time.sleep(0.5)
                if asd =='SM-N750K' or asd == "SM-G720N0" or asd=="SM-G900S" or asd == 'SM-G930S' or asd =='LM-X410K' or asd == 'LG-F650S':
                    subprocess.run('adb shell input swipe 170 1070 170 250 300',shell=True)
                elif asd == 'SM-G930S':
                    subprocess.run('adb shell input swipe 670 1450 670 750 300',shell=True)
                elif asd == 'LM-Q725K':
                    subprocess.run('adb shell input swipe 170 1570 170 250 300',shell=True)
                else :
                    subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)
                    subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)        
                self.parent.off_air()          
                time.sleep(0.5)
                subprocess.run("adb shell input keyevent 3",shell=True)
                time.sleep(3)        
                subprocess.run("adb shell am start -n com.android.settings/.TetherSettings",shell=True)
                if asd =='SM-G928K':
                    
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 66",shell=True)                
                    time.sleep(5)        
                    time.sleep(0.5)
                elif asd == 'LG-F650S':
                    time.sleep(1)
                    subprocess.run('adb shell input tap 50 130',shell=True)      
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 66",shell=True)                
                    time.sleep(5)        
                    time.sleep(0.5)
                elif asd=='SM-G960N':            
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 66",shell=True)                
                    time.sleep(5)        
                    time.sleep(0.5)
                else:
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)      
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 66",shell=True)      
                    time.sleep(5)        
                    time.sleep(0.5)
                if asd =='SM-N750K' or asd == 'SM-G720N0' :
                    subprocess.run('adb shell input tap 150 1000',shell=True)    
                    time.sleep(0.2)
                    subprocess.run('adb shell input tap 150 1000',shell=True)    
                subprocess.run('adb shell input tap 150 1500',shell=True)
                time.sleep(0.2)
                subprocess.run('adb shell input tap 150 1500',shell=True)
                time.sleep(5)
                try:                            
                    ip=get("https://api.ipify.org").text
                    self.lineEdit_4.setText(ip)                    
                    now = datetime.now()
                    nowDT = now.strftime("%H:%M")
                    self.parent.label_14.setText(nowDT)
                    self.parent.red.hide()
                    self.parent.yellow.hide()
                    self.parent.green.show()
                    self.parent.AAA=0
                    self.parent.plz_start()
                    self.parent.pushButton_7.setEnabled(False)            
                    self.parent.after_reboot()
                    self.parent.all_de()

                except:                    
                    subprocess.run("adb shell input keyevent 3",shell=True)
                    time.sleep(0.5)
                    subprocess.run("adb shell input keyevent 3",shell=True)
                    time.sleep(0.5)
                    subprocess.run('adb shell input tap 0 0',shell=True)                
                    asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
                    asd = asd.read().decode('utf-8').strip()
                    time.sleep(0.5)
                    if asd =='SM-N750K' or asd == "SM-G720N0" or asd=="SM-G900S" or asd == 'SM-G930S' or asd =='LM-X410K' or asd == 'LG-F650S':
                        subprocess.run('adb shell input swipe 170 1070 170 250 300',shell=True)
                    elif asd == 'SM-G930S':
                        subprocess.run('adb shell input swipe 670 1450 670 750 300',shell=True)
                    elif asd == 'LM-Q725K':
                        subprocess.run('adb shell input swipe 170 1570 170 250 300',shell=True)
                    else :
                        subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)
                        subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)        
                    self.parent.off_air()          
                    time.sleep(0.5)
                    subprocess.run("adb shell input keyevent 3",shell=True)
                    time.sleep(3)        
                    subprocess.run("adb shell am start -n com.android.settings/.TetherSettings",shell=True)  
                    time.sleep(1)
                    if asd =='SM-G928K':
                        
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 20",shell=True)                
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 20",shell=True)                
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 20",shell=True)                
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 66",shell=True)                
                        time.sleep(5)        
                        time.sleep(0.5)
                    elif asd == 'LG-F650S':
                        time.sleep(1)
                        subprocess.run('adb shell input tap 50 130',shell=True)      
                        subprocess.run("adb shell input keyevent 20",shell=True)                
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 66",shell=True)                
                        time.sleep(5)        
                        time.sleep(0.5)
                    elif asd=='SM-G960N':            
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 20",shell=True)                
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 20",shell=True)                
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 20",shell=True)                
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 20",shell=True)                
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 66",shell=True)                
                        time.sleep(5)        
                        time.sleep(0.5)
                    else:
                        subprocess.run("adb shell input keyevent 20",shell=True)
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 20",shell=True)      
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 66",shell=True)      
                        time.sleep(5)        
                        time.sleep(0.5)
                    if asd =='SM-N750K' or asd == 'SM-G720N0' :
                        subprocess.run('adb shell input tap 150 1000',shell=True)    
                        time.sleep(0.2)
                        subprocess.run('adb shell input tap 150 1000',shell=True)    
                    subprocess.run('adb shell input tap 150 1500',shell=True)
                    time.sleep(0.2)
                    subprocess.run('adb shell input tap 150 1500',shell=True)
                    time.sleep(5)

                    
                    try:                            
                        ip=get("https://api.ipify.org").text                        
                        self.parent.lineEdit_4.setText(ip)                        
                        self.parent.red.hide()
                        self.parent.yellow.hide()
                        self.parent.green.show()
                        self.parent.AAA=0
                        self.parent.plz_start()
                        self.parent.pushButton_7.setEnabled(False)            
                        self.parent.after_reboot()
                        self.parent.all_de()
                        
                        now = datetime.now()
                        nowDT = now.strftime("%H:%M")
                        self.parent.label_14.setText(nowDT)
                    except:                        
                        self.parent.red.show()
                        self.parent.yellow.show()
                        self.parent.green.hide()
                        self.parent.pushButton_7.setEnabled(False)
                        self.parent.fail_reboot()                                  
                        self.parent.all_de()
            else:
                time.sleep(30)
                subprocess.run("adb shell input keyevent 3",shell=True)
                time.sleep(0.5)
                subprocess.run("adb shell input keyevent 3",shell=True)
                time.sleep(0.5)
                subprocess.run('adb shell input tap 0 0',shell=True)                
                asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
                asd = asd.read().decode('utf-8').strip()
                time.sleep(0.5)
                if asd =='SM-N750K' or asd == "SM-G720N0" or asd=="SM-G900S" or asd == 'SM-G930S' or asd =='LM-X410K' or asd == 'LG-F650S':
                    subprocess.run('adb shell input swipe 170 1070 170 250 300',shell=True)
                elif asd == 'SM-G930S':
                    subprocess.run('adb shell input swipe 670 1450 670 750 300',shell=True)
                elif asd == 'LM-Q725K':
                    subprocess.run('adb shell input swipe 170 1570 170 250 300',shell=True)
                else :
                    subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)
                    subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)        
                self.parent.off_air()          
                time.sleep(0.5)
                subprocess.run("adb shell input keyevent 3",shell=True)
                time.sleep(3)        
                subprocess.run("adb shell am start -n com.android.settings/.TetherSettings",shell=True)  
                time.sleep(1)
                if asd =='SM-G928K':                                 
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 66",shell=True)                
                    time.sleep(5)        
                    time.sleep(0.5)
                elif asd == 'LG-F650S':
                    time.sleep(1)
                    subprocess.run('adb shell input tap 50 130',shell=True)      
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 66",shell=True)                
                    time.sleep(5)        
                    time.sleep(0.5)
                elif asd=='SM-G960N':            
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 66",shell=True)                
                    time.sleep(5)        
                    time.sleep(0.5)
                else:
                    subprocess.run("adb shell input keyevent 20",shell=True)
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)      
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 66",shell=True)      
                time.sleep(5)        
                time.sleep(0.5)
                if asd =='SM-N750K' or asd == 'SM-G720N0' :
                    subprocess.run('adb shell input tap 150 1000',shell=True)    
                    time.sleep(0.2)
                    subprocess.run('adb shell input tap 150 1000',shell=True)    
                subprocess.run('adb shell input tap 150 1500',shell=True)
                time.sleep(0.2)
                subprocess.run('adb shell input tap 150 1500',shell=True)
                time.sleep(5)
                try:
                    print("123123123")
                    ip=get("https://api.ipify.org").text
                    self.parent.lineEdit_4.setText(ip)
                    self.parent.red.hide()
                    self.parent.yellow.hide()
                    self.parent.green.show()
                    self.parent.plz_start()
                    
                    now = datetime.now()
                    nowDT = now.strftime("%H:%M")
                    self.parent.label_14.setText(nowDT)
                except:
                    self.parent.off_air()
                    time.sleep(0.5)
                    subprocess.run("adb shell input keyevent 3",shell=True)
                    time.sleep(3)        
                    subprocess.run("adb shell am start -n com.android.settings/.TetherSettings",shell=True)  
                    time.sleep(1)
                    if asd =='SM-G928K':
                               
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 20",shell=True)                
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 20",shell=True)                
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 20",shell=True)                
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 66",shell=True)                
                        time.sleep(5)        
                        time.sleep(0.5)
                    elif asd == 'LG-F650S':
                        time.sleep(1)
                        subprocess.run('adb shell input tap 50 130',shell=True)      
                        subprocess.run("adb shell input keyevent 20",shell=True)                
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 66",shell=True)                
                        time.sleep(5)        
                        time.sleep(0.5)
                    elif asd=='SM-G960N':            
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 20",shell=True)                
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 20",shell=True)                
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 20",shell=True)                
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 20",shell=True)                
                        time.sleep(1)
                        subprocess.run("adb shell input keyevent 66",shell=True)                
                        time.sleep(5)        
                        time.sleep(0.5)
                    else:
                            subprocess.run("adb shell input keyevent 20",shell=True)
                            time.sleep(1)
                            subprocess.run("adb shell input keyevent 20",shell=True)      
                            time.sleep(1)
                            subprocess.run("adb shell input keyevent 66",shell=True)      
                            time.sleep(5)        
                    time.sleep(0.5)
                    if asd =='SM-N750K' or asd == 'SM-G720N0' :
                        subprocess.run('adb shell input tap 150 1000',shell=True)    
                        time.sleep(0.2)
                        subprocess.run('adb shell input tap 150 1000',shell=True) 
                    subprocess.run('adb shell input tap 150 1500',shell=True)
                    time.sleep(0.2)
                    subprocess.run('adb shell input tap 150 1500',shell=True)
                    try :
                        ip=get("https://api.ipify.org").text
                        self.parent.lineEdit_4.setText(ip)
                        self.parent.red.hide()
                        self.parent.yellow.hide()
                        self.parent.green.show()
                        self.parent.plz_start()
                        
                        now = datetime.now()
                        nowDT = now.strftime("%H:%M")
                        self.parent.label_14.setText(nowDT)
                    except:
                        ip=""
                        self.parent.lineEdit_4.setText(ip)
                        self.parent.red.show()
                        self.parent.yellow.hide()
                        self.parent.green.hide()
                self.parent.AAA=0
                self.parent.pushButton_7.setEnabled(False)                            
                self.parent.all_de()
        

class total_th(QThread):
    
    how_ip =[]
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    
        
                
    def run(self):
        self.parent.red.hide()
        self.parent.yellow.hide()
        self.parent.green.hide()
        self.parent.off_air()

        st_text3 = self.parent.lineEdit_3.text()        
        AAA= self.parent.AAA        
        bbb = 0
        subprocess.run('adb shell input tap 0 0',shell=True)        
        st_asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd = st_asd.readline(5).decode('utf-8').strip()        
        
        if st_asd == 'error'or st_asd =='adb.e' or st_asd =="" or st_asd == "adb.:" or st_asd =='ad: m' :
            self.parent.yellow.show()
        else:
            while True:
                try:
                    ip=get("https://api.ipify.org").text
                    self.parent.lineEdit_4.setText(ip)
                    AAA=0                
                    self.parent.green.show()


                    self.how_ip.append(ip)
                    if len(self.how_ip) >=4:
                        if self.how_ip[0] == self.how_ip[1] == self.how_ip[2] == self.how_ip[3]:
                            self.how_ip.clear()
                            self.parent.reboot()
                        else:
                            self.how_ip.clear()


                    now = datetime.now()
                    nowDT = now.strftime("%H:%M")
                    self.parent.label_14.setText(nowDT)
                    if st_text3 =='':
                       self.set_time = 300
                    elif st_text3 != '':
                       self.set_time = self.parent.lineEdit_3.text()

                    CCC=self.set_time
                    while CCC!=0:
                        CCC=str(CCC)
                        self.parent.label_9.setText(CCC)
                        CCC=int(CCC)
                        CCC= CCC-1
                        time.sleep(1)
                    
                except:
                    print(AAA)
                    self.parent.red.show()
                    self.parent.green.hide()
                    
                    time.sleep(1)                    
                    if st_text3 =='' and AAA==0:
                        self.parent.off_air()                        
                        AAA= AAA+1
                        bbb=300                    
                        while bbb !=0:
                            bbb=str(bbb)
                            self.parent.label_9.setText(bbb)
                            bbb=int(bbb)
                            bbb=bbb-1
                            time.sleep(1)
                    elif st_text3=='' and AAA ==1:
                        self.parent.off_air()
                        AAA= AAA+1
                        bbb=60
                        while bbb !=0:
                            bbb=str(bbb)
                            self.parent.label_9.setText(bbb)
                            bbb=int(bbb)
                            bbb=bbb-1
                            time.sleep(1)
                    elif st_text3 !='' and AAA==0 :
                        self.parent.off_air()
                        AAA= AAA+1
                        bbb=st_text3
                        while bbb !=0:
                            bbb=str(bbb)
                            self.parent.label_9.setText(bbb)
                            bbb=int(bbb)
                            bbb=bbb-1
                            time.sleep(1)
                    elif st_text3 !='' and AAA==1:
                        self.parent.off_air()
                        AAA= AAA+1
                        bbb=st_text3
                        while bbb !=0:
                            bbb=str(bbb)
                            self.parent.label_9.setText(bbb)
                            bbb=int(bbb)
                            bbb=bbb-1
                            time.sleep(1)
                    elif st_text3 !='' and AAA==2:
                        self.parent.off_air()
                        AAA= AAA+1
                        bbb=60
                        while bbb !=0:
                            bbb=str(bbb)
                            self.parent.label_9.setText(bbb)
                            bbb=int(bbb)
                            bbb=bbb-1
                            time.sleep(1)
                    elif st_text3 !='' and AAA==2:
                        self.parent.off_air()
                        AAA= AAA+1
                        bbb=60
                        while bbb !=0:
                            bbb=str(bbb)
                            self.parent.label_9.setText(bbb)
                            bbb=int(bbb)
                            bbb=bbb-1
                            time.sleep(1)
                    if AAA==3:
                        self.parent.off_air()
                        asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
                        asd = asd.read().decode('utf-8').strip()
                        if asd =='SM-N750K' or asd == "SM-G720N0" or asd=="SM-G900S" or asd == 'SM-G930S' or asd =='LM-X410K' or asd == 'LG-F650S':
                            subprocess.run('adb shell input swipe 170 1070 170 250 300',shell=True)
                        elif asd == 'SM-G930S':
                            subprocess.run('adb shell input swipe 670 1450 670 750 300',shell=True)
                        elif asd == 'LM-Q725K':
                            subprocess.run('adb shell input swipe 170 1570 170 250 300',shell=True)
                        else :
                            subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)
                            subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)   
                        time.sleep(0.5)
                        subprocess.run("adb shell input keyevent 3",shell=True)
                        time.sleep(3)                    
                        subprocess.run("adb shell am start -n com.android.settings/.TetherSettings",shell=True)
                        time.sleep(1)
                        if asd =='SM-G928K':
                                        
                            time.sleep(1)
                            subprocess.run("adb shell input keyevent 20",shell=True)                
                            time.sleep(1)
                            subprocess.run("adb shell input keyevent 20",shell=True)                
                            time.sleep(1)
                            subprocess.run("adb shell input keyevent 20",shell=True)                
                            time.sleep(1)
                            subprocess.run("adb shell input keyevent 66",shell=True)                
                            time.sleep(5)        
                            time.sleep(0.5)
                        elif asd == 'LG-F650S':
                            time.sleep(1)
                            subprocess.run('adb shell input tap 50 130',shell=True)      
                            subprocess.run("adb shell input keyevent 20",shell=True)                
                            time.sleep(1)
                            subprocess.run("adb shell input keyevent 66",shell=True)                
                            time.sleep(5)        
                            time.sleep(0.5)
                        elif asd=='SM-G960N':            
                            time.sleep(1)
                            subprocess.run("adb shell input keyevent 20",shell=True)                
                            time.sleep(1)
                            subprocess.run("adb shell input keyevent 20",shell=True)                
                            time.sleep(1)
                            subprocess.run("adb shell input keyevent 20",shell=True)                
                            time.sleep(1)
                            subprocess.run("adb shell input keyevent 20",shell=True)                
                            time.sleep(1)
                            subprocess.run("adb shell input keyevent 66",shell=True)                
                            time.sleep(5)        
                            time.sleep(0.5)
                        else:
                            subprocess.run("adb shell input keyevent 20",shell=True)                
                            time.sleep(1)
                            subprocess.run("adb shell input keyevent 20",shell=True)                
                            time.sleep(1)
                            subprocess.run("adb shell input keyevent 66",shell=True)                
                            time.sleep(5)        
                        time.sleep(0.5)
                        if asd =='SM-N750K' or asd =='SM-G720N0' :
                            subprocess.run('adb shell input tap 150 1000',shell=True)    
                            time.sleep(0.2)
                            subprocess.run('adb shell input tap 150 1000',shell=True)    
                        subprocess.run('adb shell input tap 150 1500',shell=True)
                        time.sleep(0.2)
                        subprocess.run('adb shell input tap 150 1500',shell=True)
                        time.sleep(0.2)
                        self.parent.off_air()
                        time.sleep(5)                        
                        try :
                            
                            ip=get("https://api.ipify.org").text
                            self.parent.lineEdit_4.setText(ip)
                            self.parent.green.show()                            
                            self.parent.red.hide()
                            AAA=0               
                            now = datetime.now()
                            nowDT = now.strftime("%H:%M")
                            self.parent.label_14.setText(nowDT)
                            
                        except:
                            
                            self.parent.yellow.show()  
                            
                            self.parent.all_en()                    
                            self.parent.label_9.setText("")
                            self.parent.off_air()
                            now = datetime.now()
                            nowRT = now.strftime("%m/%d %H:%M")
                            
                            
                            self.parent.reboot_time.append(nowRT)
                            time.sleep(1)
                            subprocess.run("adb reboot",shell=True)         
                            time.sleep(20)       
                            for i in range(15):
                                bbs=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
                                bbs = bbs.read().decode('utf-8').strip()
                                bbs= bbs.split("\n")
                                csd = bbs[0][:5].strip()
                                if csd == 'error' or csd=='adb.e' or csd =="" or csd =='adb:' or csd == "adb.:"  or csd == "* dae" or csd == "ad: m":
                                    time.sleep(5)
                                    print(csd)        
                                else:
                                    print(csd)        
                                    break
                            if csd == 'error' or csd=='adb.e' or csd =="" or csd =='adb:' or csd == "adb.:"  or csd == "* dae" or csd =="ad: m":
                                time.sleep(10)
                                subprocess.run("adb shell input keyevent 3",shell=True)
                                time.sleep(0.5)
                                subprocess.run("adb shell input keyevent 3",shell=True)
                                time.sleep(0.5)
                                subprocess.run('adb shell input tap 0 0',shell=True)                
                                asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
                                asd = asd.read().decode('utf-8').strip()
                                time.sleep(0.5)
                                if asd =='SM-N750K' or asd == "SM-G720N0" or asd=="SM-G900S" or asd == 'SM-G930S' or asd =='LM-X410K' or asd == 'LG-F650S':
                                    subprocess.run('adb shell input swipe 170 1070 170 250 300',shell=True)
                                elif asd == 'SM-G930S':
                                    subprocess.run('adb shell input swipe 670 1450 670 750 300',shell=True)
                                elif asd == 'LM-Q725K':
                                    subprocess.run('adb shell input swipe 170 1570 170 250 300',shell=True)
                                else :
                                    subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)
                                    subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)        
                                self.parent.off_air()          
                                time.sleep(0.5)
                                subprocess.run("adb shell input keyevent 3",shell=True)
                                time.sleep(3)        
                                subprocess.run("adb shell am start -n com.android.settings/.TetherSettings",shell=True)  
                                time.sleep(1)
                                if asd =='SM-G928K':
                                                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 66",shell=True)                
                                    time.sleep(5)        
                                    time.sleep(0.5)
                                elif asd == 'LG-F650S':
                                    time.sleep(1)
                                    subprocess.run('adb shell input tap 50 130',shell=True)      
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 66",shell=True)                
                                    time.sleep(5)        
                                    time.sleep(0.5)
                                elif asd=='SM-G960N':            
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 66",shell=True)                
                                    time.sleep(5)        
                                    time.sleep(0.5)
                                else:
                                    subprocess.run("adb shell input keyevent 20",shell=True)
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)      
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 66",shell=True)      
                                    time.sleep(5)        
                                    time.sleep(0.5)
                                if asd =='SM-N750K' or asd == 'SM-G720N0' :
                                    subprocess.run('adb shell input tap 150 1000',shell=True)    
                                    time.sleep(0.2)
                                    subprocess.run('adb shell input tap 150 1000',shell=True)    
                                subprocess.run('adb shell input tap 150 1500',shell=True)
                                time.sleep(0.2)
                                subprocess.run('adb shell input tap 150 1500',shell=True)
                                time.sleep(5)
                                try:
                                
                                    ip=get("https://api.ipify.org").text
                                    self.parent.lineEdit_4.setText(ip)
                                    self.parent.green.show()
                                    self.parent.yellow.hide()
                                    self.parent.red.hide()
                                    self.parent.AAA=0
                                    AAA=0               
                                    self.parent.plz_start()
                                    self.parent.pushButton_7.setEnabled(False)            
                                    self.parent.after_reboot()
                                    self.parent.all_de()                                
                                    now = datetime.now()
                                    nowDT = now.strftime("%H:%M")
                                    self.parent.label_14.setText(nowDT)
                                except:
                                    self.parent.pushButton_7.setEnabled(False)
                                    self.parent.fail_reboot()                                  
                                    self.parent.all_de()
                                    
                                    self.parent.yellow.hide()                                
                                    break
                                
                                
                            else:
                                time.sleep(30)
                                subprocess.run("adb shell input keyevent 3",shell=True)
                                time.sleep(0.5)
                                subprocess.run("adb shell input keyevent 3",shell=True)
                                time.sleep(0.5)
                                subprocess.run('adb shell input tap 0 0',shell=True)                
                                asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
                                asd = asd.read().decode('utf-8').strip()
                                
                                time.sleep(0.5)
                                if asd =='SM-N750K' or asd == "SM-G720N0" or asd=="SM-G900S" or asd == 'SM-G930S' or asd =='LM-X410K' or asd == 'LG-F650S':
                                    subprocess.run('adb shell input swipe 170 1070 170 250 300',shell=True)
                                elif asd == 'SM-G930S':
                                    subprocess.run('adb shell input swipe 670 1450 670 750 300',shell=True)
                                elif asd == 'LM-Q725K':
                                    subprocess.run('adb shell input swipe 170 1570 170 250 300',shell=True)
                                else :
                                    subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)
                                    subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)        
                                self.parent.off_air()          
                                time.sleep(0.5)
                                subprocess.run("adb shell input keyevent 3",shell=True)
                                time.sleep(3)                    
                                subprocess.run("adb shell am start -n com.android.settings/.TetherSettings",shell=True)                
                                time.sleep(1)
                                if asd =='SM-G928K':
                                                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 66",shell=True)                
                                    time.sleep(5)        
                                    time.sleep(0.5)
                                elif asd == 'LG-F650S':
                                    time.sleep(1)
                                    subprocess.run('adb shell input tap 50 130',shell=True)      
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 66",shell=True)                
                                    time.sleep(5)        
                                    time.sleep(0.5)
                                elif asd=='SM-G960N':            
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 66",shell=True)                
                                    time.sleep(5)        
                                    time.sleep(0.5)
                                else:
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 66",shell=True)                
                                    time.sleep(5)
                                if asd =='SM-N750K' or asd == 'SM-G720N0' :
                                    subprocess.run('adb shell input tap 150 1000',shell=True)    
                                    time.sleep(0.2)
                                    subprocess.run('adb shell input tap 150 1000',shell=True)         
                                time.sleep(0.5)
                                subprocess.run('adb shell input tap 150 1500',shell=True)
                                time.sleep(0.2)
                                subprocess.run('adb shell input tap 150 1500',shell=True)                 
                            
                            try:
                                
                                self.parent.all_en()
                                ip=get("https://api.ipify.org").text
                                self.parent.lineEdit_4.setText(ip)
                                self.parent.green.show()
                                self.parent.red.hide()
                                self.parent.yellow.hide()
                                self.parent.AAA=0
                                AAA=0               
                                now = datetime.now()
                                nowDT = now.strftime("%H:%M")
                                self.parent.label_14.setText(nowDT)
                                
                                
                                
                            except:
                                
                                time.sleep(0.5)
                                subprocess.run("adb shell input keyevent 3",shell=True)
                                time.sleep(3)        
                                subprocess.run("adb shell am start -n com.android.settings/.TetherSettings",shell=True)  
                                time.sleep(1)
                                if asd =='SM-G928K':
                                                    
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 66",shell=True)                
                                    time.sleep(5)        
                                    time.sleep(0.5)
                                elif asd == 'LG-F650S':
                                    time.sleep(1)
                                    subprocess.run('adb shell input tap 50 130',shell=True)      
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 66",shell=True)                
                                    time.sleep(5)        
                                    time.sleep(0.5)
                                elif asd=='SM-G960N':            
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)                
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 66",shell=True)                
                                    time.sleep(5)        
                                    time.sleep(0.5)
                                else:
                                    subprocess.run("adb shell input keyevent 20",shell=True)
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 20",shell=True)      
                                    time.sleep(1)
                                    subprocess.run("adb shell input keyevent 66",shell=True)      
                                    time.sleep(5)        
                                    time.sleep(0.5)
                                if asd =='SM-N750K' or asd == 'SM-G720N0' :
                                    subprocess.run('adb shell input tap 150 1000',shell=True)    
                                    time.sleep(0.2)
                                    subprocess.run('adb shell input tap 150 1000',shell=True) 
                                subprocess.run('adb shell input tap 150 1500',shell=True)
                                time.sleep(0.2)
                                subprocess.run('adb shell input tap 150 1500',shell=True)
                                time.sleep(5)
                                try :
                                    ip=get("https://api.ipify.org").text
                                    self.parent.lineEdit_4.setText(ip)
                                    self.parent.green.show()
                                    self.parent.red.hide()
                                    self.parent.yellow.hide()
                                    self.parent.AAA=0
                                    AAA=0               
                                    now = datetime.now()
                                    nowDT = now.strftime("%H:%M")
                                    self.parent.label_14.setText(nowDT)
                                    
                                except:
                                    ip=""
                        
                    self.parent.all_de()
                    
                    



class tethering(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):        
        
        self.parent.red.hide()
        self.parent.yellow.hide()
        self.parent.green.hide()
        asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd = st_asd.readline(5).decode('utf-8').strip()
        asd = asd.read().decode('utf-8').strip()
        
        if st_asd == 'error'or st_asd =='adb.e' or st_asd =='adb:' or st_asd=="adb.:" or st_asd =="ad: m":
            self.parent.red.show()
            self.parent.yellow.show()
            self.parent.all_de()
        else:
            try:            
                self.parent.pushButton_2.setEnabled(False)
                self.parent.pushButton_3.setEnabled(False)
                self.parent.pushButton_5.setEnabled(False)        
                self.parent.pushButton_7.setEnabled(False)
                
                ip=get("https://api.ipify.org").text
                self.parent.lineEdit_4.setText("-----")
                self.parent.lineEdit_4.setText(ip)                
                now = datetime.now()
                nowDT = now.strftime("%H:%M")
                self.parent.label_14.setText(nowDT)
                self.parent.all_de()
                self.parent.green.show()
            except:
                self.parent.red.show()
                self.parent.pushButton_2.setEnabled(False)
                self.parent.pushButton_3.setEnabled(False)
                self.parent.pushButton_5.setEnabled(False)        
                self.parent.pushButton_7.setEnabled(False)
                
                subprocess.run("adb shell input keyevent 3",shell=True)        
                time.sleep(0.5)
                asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
                asd = asd.read().decode('utf-8').strip()            
                time.sleep(0.5)
                if asd =='SM-N750K' or asd == "SM-G720N0" or asd=="SM-G900S" or asd == 'SM-G930S' or asd =='LM-X410K' or asd == 'LG-F650S':
                    subprocess.run('adb shell input swipe 170 1070 170 250 300',shell=True)
                elif asd == 'SM-G930S':
                    subprocess.run('adb shell input swipe 170 1070 170 250 300',shell=True)
                elif asd == 'LM-Q725K':
                    subprocess.run('adb shell input swipe 170 1570 170 250 300',shell=True)
                else :
                    subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)
                    subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)      
                time.sleep(0.5)
                subprocess.run("adb shell am start -n com.android.settings/.TetherSettings",shell=True)        
                if asd =='SM-G928K':                        
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 66",shell=True)                
                    time.sleep(5)        
                    time.sleep(0.5)
                elif asd == 'LG-F650S':
                    time.sleep(1)
                    subprocess.run('adb shell input tap 50 130',shell=True)      
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 66",shell=True)                
                    time.sleep(5)        
                    time.sleep(0.5)
                elif asd=='SM-G960N':            
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 66",shell=True)                
                    time.sleep(5)        
                    time.sleep(0.5)
                elif asd=='SM-G960N':            
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 66",shell=True)                
                    time.sleep(5)        
                    time.sleep(0.5)
                else:                            
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(1)
                    subprocess.run("adb shell input keyevent 66",shell=True)                
                    time.sleep(5)        
                    time.sleep(0.5)
                if asd =='SM-N750K' or asd == 'SM-G720N0' :
                        subprocess.run('adb shell input tap 150 1000',shell=True)    
                        time.sleep(0.2)
                        subprocess.run('adb shell input tap 150 1000',shell=True) 
                subprocess.run('adb shell input tap 150 1500',shell=True)
                time.sleep(0.2)
                subprocess.run('adb shell input tap 150 1500',shell=True)    
                
                time.sleep(5)
                try :
                    
                    ip=get("https://api.ipify.org").text
                    self.parent.lineEdit_4.setText(ip)                    
                    now = datetime.now()
                    nowDT = now.strftime("%H:%M")
                    self.parent.label_14.setText(nowDT)
                    self.parent.red.hide()                    
                    self.parent.green.show()
                    
                except:                    
                    self.parent.green.hide()
                self.parent.all_de()
                
            




class sh_device(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        self.parent.yellow.hide()
        self.parent.red.hide()
        self.parent.green.hide()
        subprocess.run('adb shell input keyevent 26',shell=True)
        subprocess.run('adb shell input keyevent 3',shell=True)     
        asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd = st_asd.readline(5).decode('utf-8').strip()
        asd = asd.read().decode('utf-8').strip()
        

        


        if st_asd == 'error'or st_asd =='adb.e' or st_asd =='adb:' or st_asd=="adb.:" or st_asd =="ad: m":
            self.parent.yellow.show()            
        else:
            if asd =='SM-G906S' or asd == 'SM-G906K' or asd == 'SM-G900K'  or asd == 'SM-G900S' or asd == 'SM-G906L' or asd == 'SM-G900L':
                asd = '갤럭시S5 연결'
            elif asd=='SM-N900S' or asd =='SM-G930S' or asd == 'SM-N900K' or asd == 'SM-N750K':
                asd = '갤럭시노트3 연결'
            elif asd=='SM-G720N0':
                asd= "그랜드맥스 연결"
            elif asd=='SM-G928K':
                asd= "갤럭시S6 연결"
            elif asd=='SM-G960N':
                asd= "갤럭시S9 연결"
            elif asd=='LG-F650S':
                asd= "X Screen 연결"
            elif asd=='LM-Q725K':
                asd= "Q7 연결"

            self.parent.red.hide()
            self.parent.yellow.hide()            
            self.parent.lineEdit_4.setText(asd)
            try:
                ip=get("https://api.ipify.org").text  
                self.parent.green.show()                
            except:
                print("hi")  
                time.sleep(0.5)
                self.parent.red.show()
        
            
        
            
            
        


class ch_ip(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        self.parent.red.hide()
        self.parent.yellow.hide()
        self.parent.green.hide()

        asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd = st_asd.readline(5).decode('utf-8').strip()
        asd = asd.read().decode('utf-8').strip()        
        if st_asd == 'error'or st_asd =='adb.e' or st_asd =='adb:' or st_asd=="adb.:" or st_asd =="ad: m":
            self.parent.yellow.show()
            self.parent.red.show()
            ip=("")
            self.parent.lineEdit_4.setText(ip)
        else:      
            self.parent.green.show()      
            self.parent.pushButton_2.setEnabled(False)            
            self.parent.pushButton_4.setEnabled(False)
            self.parent.pushButton_5.setEnabled(False)        
            self.parent.pushButton_7.setEnabled(False)   
            
            self.parent.on_air()
            time.sleep(5)
            self.parent.off_air()
            time.sleep(5)
            try:
                ip="변경: " + get("https://api.ipify.org").text  
                self.parent.lineEdit_4.setText(ip)
                now = datetime.now()
                nowDT = now.strftime("%H:%M")
                self.parent.label_14.setText(nowDT)
                self.parent.green.show()                
            except:
                ip=("")                
                self.parent.red.show()
                self.parent.green.hide()     
                self.parent.lineEdit_4.setText(ip)
        self.parent.all_de()

class battery(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        while True:
            asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
            st_asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
            st_asd = st_asd.readline(5).decode('utf-8').strip()
            asd = asd.read().decode('utf-8').strip()        
            bsd=subprocess.Popen('adb shell dumpsys battery',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
            bbaa = bsd.read()
            baba = bbaa.split()
            adbadb = []    
            


            if st_asd == 'error'or st_asd =='adb.e' or st_asd =='adb:' or st_asd=="adb.:" or st_asd =="ad: m":
                pass
            else:
                for i in range(len(baba)):
                    adbadb.append(baba[i].decode('utf-8'))
                AAA = adbadb.index('level:')
                BBB =adbadb[AAA+1]
                self.parent.label_5.setText(BBB)
                if int(BBB) <=50 :
                    self.parent.bat_r.show()
                else:
                    self.parent.bat_g.show()

            time.sleep(10)



class se_list(QDialog,se_list_class):
    def __init__(self, parent):
        super(se_list,self).__init__(parent)
        self.setupUi(self)        
        self.show()

class reboot_reserv(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        while True:
            now = datetime.now()
            nowDT = now.strftime("%H:%M")
            
            if self.parent.checkBox.isChecked():
                print(nowDT)
                print(self.parent.timelist.currentText())
                if self.parent.timelist.currentText() ==nowDT:
                    
                    self.parent.rebooting.start()
                if self.parent.timelist.currentText() =='00:01':
                    time.sleep(60)
                    self.parent.reboot()
                    self.parent.checkBox.toggle()
                    break
            else:
                print("언체크")   
            time.sleep(5)


            

class reboot_data(QDialog,reboot_class):
    def __init__(self, parent):
        super(reboot_data,self).__init__(parent)
        self.setupUi(self)
        self.asdasd()
        self.show()
        

    def asdasd(self):
        mw = MyWindow()
        RT = mw.reboot_time
        for i in range(len(RT)):
            print(RT[i])
            AAA = str(i+1) + " / " +str(RT[i])
            self.plainTextEdit.appendPlainText(AAA)



class MyWindow(QMainWindow, form_class):
    
    
    def __init__(self):
        
        super().__init__()        
        
        self.setupUi(self)        
        self.total_th = total_th(self)                
        self.rebooting = reboot(self)
        self.tether = tethering(self)
        self.sh_device = sh_device(self)        
        self.ch_ip=ch_ip(self)        
        self.batt=battery(self)
        self.reboot_reserv=reboot_reserv(self)
        # self.mutal = mutal(self)
        
        self.pushButton_2.clicked.connect(self.product)
        self.pushButton_3.clicked.connect(self.change_ip)
        self.pushButton_4.clicked.connect(self.tether_man)
        self.pushButton_5.clicked.connect(self.reboot)
        self.pushButton_9.clicked.connect(self.check_user)
        self.pushButton_7.clicked.connect(self.plz_start)
        self.lineEdit.returnPressed.connect(self.check_user)
        self.lineEdit_2.returnPressed.connect(lambda: self.focusNextChild())
        self.pushButton_12.clicked.connect(self.se_list_window)
        self.pushButton_14.clicked.connect(self.reboot_data_window)
        
        self.btn_all_stop.clicked.connect(self.all_stop)
        self.timelist.addItem("00:01")
        self.timelist.addItem("00:00")
        self.timelist.addItem("01:00")
        self.timelist.addItem("02:00")
        self.timelist.addItem("03:00")
        self.timelist.addItem("04:00")
        self.timelist.addItem("05:00")
        self.timelist.addItem("06:00")
        self.checkBox.toggled.connect(self.ch_func)
        
        self.red.hide()
        self.yellow.hide()
        self.green.hide()
        self.red2.hide()
        self.yellow2.hide()
        self.green2.hide()
        self.bat_r.hide()
        self.bat_g.hide()
        
        
        self.label_3.setStyleSheet("Color:red")
        self.label_3.hide()
        
        self.btn_all_stop.setEnabled(False)
        self.setWindowTitle("준소프트/V2_12")
        

    reboot_time = []
    AAA = 0
    stop_time = 300
    XXX=0
    FFF=0    

    def reboot_data_window(self):
        reboot_data(self)
    def ch_func(self):
        if self.checkBox.isChecked():
            self.reboot_reserv.start()
        else:
            self.reboot_reserv.terminate()
    def tether_man(self):
        self.tether.start()

    def all_stop(self):
        self.stop_all()
        self.rebooting.terminate()
        self.total_th.how_ip.clear()
        self.all_de()
        
        
        
        self.red.hide()
        self.yellow.hide()
        self.green.hide()

    def reset(self):        
        self.stop_all()
        self.AAA=0   

    def se_list_window(self):
        se_list(self)
    
    
    def clear_3(self):
        self.lineEdit_3.text().clear()

    def check_user(self):

        check_id = self.lineEdit_2.text().strip()
        check_pass = self.lineEdit.text().strip()

        if (check_id=='cowboy' or 'skdi262') and (check_pass=='cow2468' or 'tlqkf262'):
            print('hi')
            self.all_de()
            self.lineEdit.hide()
            self.lineEdit_2.hide()
            self.label.hide()
            self.label_2.hide()
            self.pushButton_9.hide()
            self.pushButton_10.hide()
            self.pushButton_13.hide()
            self.label_3.hide()
            self.adb_dvices()
            self.red2.show()
            self.yellow2.show()
            self.green2.show()
            
            self.resize(341, 255)
            self.bat_r.setGeometry(290,210,21,21)
            self.bat_r2.setGeometry(290,210,21,21)
            self.bat_g.setGeometry(290,210,21,21)
            self.pushButton_2.setGeometry(130,150,31,23)
            self.pushButton_5.setGeometry(80,150,31,23)
            self.pushButton_4.setGeometry(30,150,31,23)
            self.pushButton_3.setGeometry(30,120,131,23)
            self.pushButton_7.setGeometry(180,60,131,23)
            self.pushButton_12.setGeometry(180,30,131,23)
            self.pushButton_14.setGeometry(190,180,121,23)
            
            self.btn_all_stop.setGeometry(180,90,131,23)
            self.label_4.setGeometry(180,210,71,21)
            self.label_5.setGeometry(260,210,21,21)
            self.label_9.setGeometry(120,80,41,47)
            self.label_10.setGeometry(140,50,31,47)
            self.label_11.setGeometry(140,80,21,47)
            self.label_12.setGeometry(30,80,91,47)
            self.label_13.setGeometry(180,140,131,47)
            self.label_14.setGeometry(260,140,51,47)
            self.label_7.setGeometry(30,63,71,16)
            self.lineEdit_3.setGeometry(100,60,41,25)
            self.lineEdit_4.setGeometry(180,120,131,25)
            self.timelist.setGeometry(30,180,61,22)
            self.checkBox.setGeometry(100,180,91,21)
            asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
            st_asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
            st_asd = st_asd.readline(5).decode('utf-8').strip()
            asd = asd.read().decode('utf-8').strip()        

            if st_asd == 'error'or st_asd =='adb.e' or st_asd =='adb:' or st_asd=="adb.:" or st_asd =="ad: m":
                self.red.show()
                self.yellow.show()
            else:
                self.batt.start()
                try:
                    ip=get("https://api.ipify.org").text
                    now = datetime.now()
                    nowDT = now.strftime("%H:%M")
                    self.label_14.setText(nowDT)
                    self.lineEdit_4.setText(ip)
                    self.green.show()
                except:
                    ip=""
                    self.lineEdit_4.setText(ip)
                    self.red.show()

        else:
            self.label_3.show()


    def all_en(self):        
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)        
        self.pushButton_7.setEnabled(False)
        
        
        
    def all_de(self):        
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)        
        self.pushButton_7.setEnabled(True)        
        self.btn_all_stop.setEnabled(True)
        
        

    def stop_th(self):
        self.AAA=0        
        self.pushButton_7.setEnabled(False) 
        self.total_th.terminate()
        
        self.label_9.setText("")

    def stop_all(self):
        self.AAA=0        
        self.pushButton_7.setEnabled(True) 
        self.total_th.terminate()
        
        self.label_9.setText("")
        self.lineEdit_3.clear()
        

    def plz_start(self):
        
        
        self.pushButton_7.setEnabled(False)
        self.total_th.start()
        

    def adb_dvices(self):
        subprocess.run('adb devices',shell=True)
        time.sleep(0.5)
        
    
    
        

    def product(self):
        
        self.sh_device.start()
        
    
        


    def on_air(self):

        subprocess.run('adb shell settings put global airplane_mode_on 1',shell=True)
        subprocess.run("adb shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true",shell=True)

    def off_air(self):

        subprocess.run('adb shell settings put global airplane_mode_on 0',shell=True)
        subprocess.run("adb shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false",shell=True)

    def change_ip(self):
        
        self.ch_ip.start()

    
    

    def reboot(self):
        
        
        self.rebooting.start()
        
    

    
        
    
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()    
    myWindow.all_en()
    myWindow.off_air()    
    app.exec_()
    subprocess.run('adb kill-server',shell=True)
    
    