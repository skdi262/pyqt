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
import schedule

Socket_Singleton(address="127.0.0.1", port=1337, timeout=0, client=True, strict=True)
# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
#     return os.path.join(base_path, relative_path)

# form1 = resource_path("untitled3.ui")
# form2 = resource_path("np_user.ui")
# form3 = resource_path("reboot_data.ui")
# form4 = resource_path("newbie.ui")
# form5 = resource_path("find_id.ui")
# form6 = resource_path("ch_user.ui")
# form_class = uic.loadUiType(form1)[0]
# np_user_class = uic.loadUiType(form2)[0]
# reboot_class = uic.loadUiType(form3)[0]
# newbie_class = uic.loadUiType(form4)[0]
# find_id_class = uic.loadUiType(form5)[0]
# ch_class = uic.loadUiType(form6)[0]

now_file = os.getcwd()

form_class = uic.loadUiType(now_file +r"\uis\untitled3.ui")[0]
np_user_class = uic.loadUiType(now_file +r"\uis\np_user.ui")[0]
reboot_class = uic.loadUiType(now_file +r"\uis\reboot_data.ui")[0]
newbie_class = uic.loadUiType(now_file +r"\uis\newbie.ui")[0]
find_id_class = uic.loadUiType(now_file +r"\uis\find_id.ui")[0]
ch_class = uic.loadUiType(now_file +r"\uis\ch_user.ui")[0]

# 재부팅 방법
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

# 재부팅 

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
            self.parent.pushButton_3.setEnabled(False)                
            self.parent.pushButton_6.setEnabled(False)        
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
                subprocess.run('adb shell input tap 150 1550',shell=True)
                time.sleep(0.2)
                subprocess.run('adb shell input tap 150 1550',shell=True)
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
                    subprocess.run('adb shell input tap 150 1550',shell=True)
                    time.sleep(0.2)
                    subprocess.run('adb shell input tap 150 1550',shell=True)
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
                subprocess.run('adb shell input tap 150 1550',shell=True)
                time.sleep(0.2)
                subprocess.run('adb shell input tap 150 1550',shell=True)
                time.sleep(5)
                try:
                    
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
                    subprocess.run('adb shell input tap 150 1550',shell=True)
                    time.sleep(0.2)
                    subprocess.run('adb shell input tap 150 1550',shell=True)
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
                self.parent.re_black()
                self.parent.AAA=0
                self.parent.pushButton_7.setEnabled(False)                            
                self.parent.all_de()
        
# 인터넷 연결 확인 
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
                    if len(self.how_ip) >=3:
                        if self.how_ip[0] == self.how_ip[1] == self.how_ip[2] and self.parent.checkBox.isChecked():
                            self.how_ip.clear()
                            self.parent.reboot()
                            break
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
                        subprocess.run('adb shell input tap 150 1550',shell=True)
                        time.sleep(0.2)
                        subprocess.run('adb shell input tap 150 1550',shell=True)
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
                                subprocess.run('adb shell input tap 150 1550',shell=True)
                                time.sleep(0.2)
                                subprocess.run('adb shell input tap 150 1550',shell=True)
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
                                subprocess.run('adb shell input tap 150 1550',shell=True)
                                time.sleep(0.2)
                                subprocess.run('adb shell input tap 150 1550',shell=True)                 
                            
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
                                subprocess.run('adb shell input tap 150 1550',shell=True)
                                time.sleep(0.2)
                                subprocess.run('adb shell input tap 150 1550',shell=True)
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

# 아이피 변경
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
        self.parent.pushButton_3.setStyleSheet('QPushButton')
        

# 배터리
class battery(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        while True:
            time.sleep(10)
            
            asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
            st_asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
            st_asd = st_asd.readline(5).decode('utf-8').strip()
            asd = asd.read().decode('utf-8').strip()        
            bsd=subprocess.Popen('adb shell dumpsys battery',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
            bbaa = bsd.read()
            baba = bbaa.split()
            adbadb = []    
            if st_asd == 'error'or st_asd =='adb.e' or st_asd =='adb:' or st_asd=="adb.:" or st_asd =="ad: m":
                self.parent.label_5.setText("")
            else:
                for i in range(len(baba)):
                    adbadb.append(baba[i].decode('utf-8'))
                try:
                    AAA = adbadb.index('level:')
                    BBB =adbadb[AAA+1]
                    self.parent.label_5.setText(BBB)
                    if int(BBB) <=50 :
                        self.parent.bat_r.show()
                    else:
                        self.parent.bat_g.show()
                except:
                    self.parent.label_5.setText("")

            

class ch_user(QDialog,ch_class):    
    def __init__(self, parent):
        super(ch_user,self).__init__(parent)
        self.setupUi(self)                
        self.center()
        self.lineEdit.returnPressed.connect(self.check_user)
        self.lineEdit_2.returnPressed.connect(lambda: self.focusNextChild())
        self.pushButton_9.clicked.connect(self.check_user)
        self.label_3.hide()
        self.setWindowTitle("준소프트 휴대폰 도우미")
        

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def check_user(self):
        myWindow = MyWindow()
        check_id = self.lineEdit_2.text().strip()
        check_pass = self.lineEdit.text().strip()
        now = datetime.now()
        nowDT = now.strftime("%Y/%m/%d/%H/%M")
        nowp = time.strptime(nowDT,"%Y/%m/%d/%H/%M")
        exdate= myWindow.exdate
        exp = time.strptime(exdate,"%Y/%m/%d/%H/%M")
        
        if exp > nowp:
            
            # 로그인 유저 확인
            # 아이디 비밀번호 부여
            
            if (check_id=='xoqortksaor' and check_pass=='dkfmaekdnj') or (check_id=='skdi262' and check_pass=='dkdldbxm262!@'):                
                self.close()
                myWindow.show()
                myWindow.reserv_start()
            else:
                self.label_3.show()
        else:
            self.label_3.show()
            self.label_3.setText("이용기간이 만료되었습니다.")



# C버튼 디바이스 확인용
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
        ip=""

        if st_asd == 'error'or st_asd =='adb.e' or st_asd =='adb:' or st_asd=="adb.:" or st_asd =="ad: m":
            self.parent.yellow.show()            
        else:
            if asd =='SM-G906S' or asd == 'SM-G906K' or asd == 'SM-G900K'  or asd == 'SM-G900S' or asd == 'SM-G906L' or asd == 'SM-G900L':
                asd = '갤럭시S5->연결'
            elif asd=='SM-N900S' or asd =='SM-G930S' or asd == 'SM-N900K' or asd == 'SM-N750K':
                asd = '갤럭시노트3-> 연결'
            elif asd=='SM-G720N0':
                asd= "그랜드맥스->연결"
            elif asd=='SM-G928K':
                asd= "갤럭시edge->연결"
            elif asd=='LG-F650S':
                asd= "X Screen-> 연결"
            elif asd=='LM-Q725K':
                asd= "LG Q7->연결"
            elif asd=='SM-G960N':
                asd= "갤럭시S9->연결"
            elif asd=='SM-N916K':
                asd= "갤럭시노트4->연결"
            elif asd=='SM-G850K':
                asd= "갤럭시알파->연결"
            self.parent.lineEdit_4.setText(asd)
            try:
                ip=get("https://api.ipify.org").text  
                self.parent.green.show()        
            except:
                self.parent.red.show()
        time.sleep(0.2)
        self.parent.pushButton_6.setStyleSheet('QPushButton')


# 자정 재부팅 예약
class reboot_reserv(QThread):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
    def run(self):
        
        while 1:            
            now = datetime.now()
            nowDT = now.strftime("%H:%M")                
            nowPT = now.strftime("%Y/%m/%d/%H/%M")
            nowp = time.strptime(nowPT,"%Y/%m/%d/%H/%M")                   
            exp = time.strptime(self.parent.exdate,"%Y/%m/%d/%H/%M")
            AFAF = '매일 ' + nowDT
            if exp <= nowp:
                self.parent.close()                
            if self.parent.checkBox_2.isChecked():
                print(nowDT)
                print(self.parent.timelist.currentText(),AFAF)
                if self.parent.timelist.currentText() ==AFAF:
                    self.parent.reboot()
                elif self.parent.timelist.currentText() =='테스트1분':     
                    print("hello")               
                    time.sleep(60)
                    self.parent.reboot()
                    self.parent.checkBox_2.toggle()
            else:
                pass                
            time.sleep(5)
            
# 재부팅 기록 확인
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
        self.sh_device = sh_device(self)        
        self.ch_ip=ch_ip(self)        
        self.batt=battery(self)
        self.reboot_reserv=reboot_reserv(self)
        
        self.pushButton_3.clicked.connect(self.change_ip)        
        self.pushButton_5.clicked.connect(self.reboot)
        self.pushButton_6.clicked.connect(self.product)        
        self.pushButton_7.clicked.connect(self.plz_start)           
        self.pushButton_14.clicked.connect(self.reboot_data_window)        
        self.btn_all_stop.clicked.connect(self.all_stop)        
        self.checkBox.toggled.connect(self.same_ip_clear)
        
        self.red.hide()
        self.yellow.hide()
        self.green.hide()
        self.timelist.addItem('선택')
        self.timelist.addItem('테스트1분')
        self.timelist.addItem('매일 00:00')        
        self.timelist.addItem('매일 03:00')
        self.timelist.addItem('매일 06:00')
        self.timelist.addItem('매일 09:00')
        self.timelist.addItem('매일 12:00')              
        self.setWindowTitle("준소프트/CT_10")
        self.first()
        schedule.every(6).days.do(self.qldkrmfk)
        
    # close time 만료기간 exdate 날짜만 수정 해주셔야 합니다.
    exdate = "2022/01/31/1/20"

    reboot_time = []
    AAA = 0
    stop_time = 300
    XXX=0
    FFF=0    

    def qldkrmfk(self):
        self.all_stop()
        self.total_th.start()

        
        
        
    
    
    def greenshow(self):
        self.green.show()

    def same_ip_clear(self):
        self.total_th.how_ip.clear()
    def reserv_start(self):
        self.reboot_reserv.start()

    def product(self):
        self.pushButton_6.setStyleSheet('QPushButton {background-color: red; color:white}')
        self.sh_device.start()

    def time_kill(self):
        app.exec_()

    def reboot_data_window(self):
        reboot_data(self)    
    
    def stop_all(self):
        self.AAA=0        
        self.pushButton_7.setEnabled(True) 
        self.total_th.terminate()
        self.pushButton_7.setStyleSheet('QPushButton')
        self.label_9.setText("")
        self.lineEdit_3.clear()

    def all_stop(self):
        self.stop_all()
        self.rebooting.terminate()
        self.total_th.how_ip.clear()
        self.all_de()
        self.ch_ip.terminate()
        self.pushButton_5.setStyleSheet('QPushButton')
        self.pushButton_3.setStyleSheet('QPushButton')
        self.red.hide()
        self.yellow.hide()
        self.green.hide()

    def reset(self):        
        self.stop_all()
        self.AAA=0   

    def clear_3(self):
        self.lineEdit_3.text().clear()        
    
    def first(self):
        asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd = st_asd.readline(5).decode('utf-8').strip()
        asd = asd.read().decode('utf-8').strip()        
        self.batt.start()
        if st_asd == 'error'or st_asd =='adb.e' or st_asd =='adb:' or st_asd=="adb.:" or st_asd =="ad: m":
            self.red.show()
            self.yellow.show()
        else:
            
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

    def all_en(self):                
        self.pushButton_3.setEnabled(False)        
        self.pushButton_5.setEnabled(False)        
        self.pushButton_7.setEnabled(False)
        
    def all_de(self):                
        self.pushButton_3.setEnabled(True)        
        self.pushButton_5.setEnabled(True)        
        self.pushButton_6.setEnabled(True)    
        self.pushButton_7.setEnabled(True)        
        self.btn_all_stop.setEnabled(True)

    def stop_th(self):
        self.AAA=0        
        self.pushButton_7.setEnabled(False) 
        self.total_th.terminate()
        self.pushButton_7.setStyleSheet('QPushButton')
        self.label_9.setText("")

    def plz_start(self):        
        self.pushButton_7.setStyleSheet('QPushButton {background-color: red; color:white}')
        self.pushButton_7.setEnabled(False)
        self.total_th.start()        

    def adb_dvices(self):
        subprocess.run('adb devices',shell=True)
        time.sleep(0.5)        

    def on_air(self):
        subprocess.run('adb shell settings put global airplane_mode_on 1',shell=True)
        subprocess.run("adb shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true",shell=True)

    def off_air(self):
        subprocess.run('adb shell settings put global airplane_mode_on 0',shell=True)
        subprocess.run("adb shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false",shell=True)

    def change_ip(self):
        self.pushButton_3.setStyleSheet('QPushButton {background-color: red; color:white}')
        self.ch_ip.start()

    def killthem(self):        
        app.exec_()
        subprocess.run("taskkill /f /im adb.exe", shell=True)
    

    def reboot(self):
        self.pushButton_5.setStyleSheet('QPushButton {background-color: red; color:white}')
        self.rebooting.start()    

    def re_black(self):
        self.pushButton_5.setStyleSheet('QPushButton')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    chch= ch_user(myWindow)
    chch.show()
    myWindow.all_en()     
    myWindow.killthem()