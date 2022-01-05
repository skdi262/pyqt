import sys
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import os
import time
import subprocess
from requests import get
from datetime import datetime
import schedule
from Socket_Singleton import Socket_Singleton
# Socket_Singleton(address="127.0.0.1", port=1337, timeout=0, client=True, strict=True)
# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
#     return os.path.join(base_path, relative_path)

# form1 = resource_path("untitled.ui")
# form2 = resource_path("np_user.ui")
# form3 = resource_path("reboot_data.ui")
# form4 = resource_path("newbie.ui")
# form5 = resource_path("find_id.ui")
# form6 = resource_path("ch_user.ui")
# form7 = resource_path("se_list.ui")

# form_class = uic.loadUiType(form1)[0]
# np_user_class = uic.loadUiType(form2)[0]
# reboot_class = uic.loadUiType(form3)[0]
# newbie_class = uic.loadUiType(form4)[0]
# find_id_class = uic.loadUiType(form5)[0]
# ch_class = uic.loadUiType(form6)[0]
# se_list_class = uic.loadUiType(form7)[0]

now_file = os.getcwd()

form_class = uic.loadUiType(now_file +r"\uis\untitled.ui")[0]
np_user_class = uic.loadUiType(now_file +r"\uis\np_user.ui")[0]
reboot_class = uic.loadUiType(now_file +r"\uis\reboot_data.ui")[0]
se_list_class = uic.loadUiType(now_file +r"\uis\se_list.ui")[0]
newbie_class = uic.loadUiType(now_file +r"\uis\newbie.ui")[0]
find_id_class = uic.loadUiType(now_file +r"\uis\find_id.ui")[0]
ch_class = uic.loadUiType(now_file +r"\uis\ch_user.ui")[0]



# 재부팅 
class reboot(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        self.parent.off_air()
        subprocess.run('adb shell input tap 0 0',shell=True)
        asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd = st_asd.readline(5).decode('utf-8').strip()
        asd = asd.read().decode('utf-8').strip()
        # 재부팅 시작 시 디바이스 확인
        if st_asd == 'error'or st_asd =='adb.e' or st_asd =="" or st_asd == "adb.:" or st_asd =='ad: m' :
            asd = "핸드폰과 pc연결 확인 및 on off 확인"
            self.parent.textBrowser.append(asd)
            self.parent.s_max()
            self.parent.ch_reboot()
        
        else:
            self.parent.textBrowser.append("재부팅 중") 
            self.parent.s_max()
            self.parent.stop_th()
            self.parent.all_en() 
            self.parent.label_9.setText("")
            nowrst = datetime.now()
            nst = "재부팅 시작 / " 
            npst = nowrst.strftime("%H:%M")
            nast = nst + npst
            self.parent.textBrowser.append(nast)
            now = datetime.now()
            nowRT = now.strftime("%m/%d %H:%M")
            self.parent.reboot_time.append(nowRT)
            self.parent.s_max()
            self.parent.off_air()
            time.sleep(0.5)
            subprocess.run("adb reboot",shell=True)
            time.sleep(20)
            self.parent.textBrowser.append("재부팅 후 테더링 연결 중") 
            self.parent.s_max()
            for i in range(15):
                bbs=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
                bbs = bbs.read().decode('utf-8').strip()
                bbs= bbs.split("\n")
                csd = bbs[0][:5].strip()
                
                if csd == 'error' or csd=='adb.e' or csd =="" or csd =='adb:' or csd == "adb.:"  or csd == "* dae" or csd =="ad: m":
                    time.sleep(5)
                    
                else:
                       
                    break
            # 재부팅 후 디바이스가 안 잡혔을 시 강제로 테더링 들어가는 곳
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
                # 테더링 후 인터넷확인
                try:

                    ip=get("https://api.ipify.org").text
                    td_ip="테더링 연결 됨 / " + ip
                    self.parent.textBrowser.append(td_ip)
                    self.parent.s_max()
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
                    # 테더링 후 인터넷확인
                    try:
                            
                        ip=get("https://api.ipify.org").text
                        td_ip="테더링 연결 됨 / " + ip
                        self.parent.textBrowser.append(td_ip)
                        self.parent.s_max()
                        self.parent.AAA=0
                        self.parent.plz_start()
                        self.parent.pushButton_7.setEnabled(False)            
                        self.parent.after_reboot()
                        self.parent.all_de()
                    except:
                        self.parent.textBrowser.append("핸드폰 연결 혹은 데이터 연결 안 됨")
                        self.parent.s_max()
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
                subprocess.run('adb shell input tap 150 1550',shell=True)
                time.sleep(0.2)
                subprocess.run('adb shell input tap 150 1550',shell=True)
                time.sleep(5)
                # 테더링 후 인터넷확인
                try:                        
                    time.sleep(3)
                    ip=get("https://api.ipify.org").text
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
                    time.sleep(5)
                    # 테더링 후 인터넷확인
                    try :
                        ip=get("https://api.ipify.org").text
                    except:
                        self.parent.textBrowser.append("모바일 데이터 연결 안 됨")
                        self.parent.s_max()
                        ip=""
                
                # 재부팅 끝
                now = datetime.now()
                nowDT = now.strftime("%H:%M")
                
                
                seven= "재부팅완료 / " +ip  + " / " + nowDT
                eight = "테더링완료 / "+ nowDT
                
                self.parent.textBrowser.append(eight)
                self.parent.s_max()
                self.parent.textBrowser.append(seven)
                self.parent.s_max()
                
                self.parent.AAA=0
                self.parent.plz_start()
                
                
                self.parent.pushButton_7.setEnabled(False)            
                self.parent.after_reboot()
                self.parent.all_de()
        
# 인터넷 연결 확인 
class total_th(QThread):
    how_ip =[]
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    

    def run(self):
        self.parent.off_air()
        st_text3 = self.parent.lineEdit_3.text()
        AAA= self.parent.AAA
        set_time =0
        bbb = 0
        
        while True:
            try:
                
                time.sleep(1)    
                ip=get("https://api.ipify.org").text
                if not self.parent.checkBox.isChecked():                    
                    self.how_ip.clear()
                
                if self.parent.checkBox.isChecked():
                    self.how_ip.append(ip)
                    if len(self.how_ip) ==1:
                        self.parent.textBrowser.append("ip 중복 체크 활성화, 2회 중복 시 재부팅")
                    
                if len(self.how_ip) >=3 and self.parent.checkBox.isChecked():
                    if self.how_ip[0] == self.how_ip[1] == self.how_ip[2]:
                        self.parent.textBrowser.append("ip 중복 2회, 재부팅 시작")
                        self.parent.s_max()
                        self.how_ip.clear()
                        self.parent.reboot()
                        break
                    elif(self.how_ip[0] == self.how_ip [1]) != self.how_ip [2]:
                        cnrk  = self.how_ip [2]
                        self.how_ip.clear()
                        self.how_ip.append(cnrk)
                
                now = datetime.now()
                nowDT = now.strftime(" / %m/%d %H:%M")
                nowipDt= "네트워크 : " +ip + nowDT
                self.parent.textBrowser.append(nowipDt)
                if len(self.how_ip) >1 and self.parent.checkBox.isChecked():
                    if self.how_ip[0] == self.how_ip [1]:
                        self.parent.textBrowser.append("ip 중복 1회.  2회 중복 시 재부팅")
                    elif self.how_ip[0] != self.how_ip [1]:
                        cnrk  = self.how_ip [1]
                        self.how_ip.clear()
                        self.how_ip.append(cnrk)
                    elif (self.how_ip[0] == self.how_ip [1]) != self.how_ip [2]:
                        cnrk  = self.how_ip [2]
                        self.how_ip.clear()
                        self.how_ip.append(cnrk)

                self.parent.s_max()

                AAA=0
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
                
                time.sleep(1)                
                if st_text3 =='' and AAA==0:
                    self.parent.off_air()
                    st_st = '300'
                    st_aa = "네트워크 미확인 "+st_st+"초 후 재확인"
                    self.parent.textBrowser.append(st_aa)
                    self.parent.s_max()
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
                    self.parent.textBrowser.append("네트워크 미확인 60초 후 재확인")
                    self.parent.s_max()
                    AAA= AAA+1
                    bbb=60
                    while bbb !=0:
                        bbb=str(bbb)
                        self.parent.label_9.setText(bbb)
                        bbb=int(bbb)
                        bbb=bbb-1
                        time.sleep(1)
                elif st_text3 !='' and AAA==0:
                    self.parent.off_air()
                    st_st = st_text3
                    st_aa = "네트워크 미확인 "+st_st+"초 후 재확인"
                    self.parent.textBrowser.append(st_aa)
                    self.parent.s_max()
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
                    self.parent.textBrowser.append("네트워크 미확인 60초 후 재확인")
                    self.parent.s_max()
                    AAA= AAA+1
                    bbb=60
                    while bbb !=0:
                        bbb=str(bbb)
                        self.parent.label_9.setText(bbb)
                        bbb=int(bbb)
                        bbb=bbb-1
                        time.sleep(1)
                elif AAA==2:
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
                    time.sleep(5)
                    self.parent.off_air()
                    
                    try :
                        
                        ip=get("https://api.ipify.org").text
                        
                    except:
                        self.parent.textBrowser.append("네트워크 연결 안 됨 재부팅 시작")
                        self.parent.textBrowser.append("재부팅 중")  
                        self.parent.s_max()         
                        now = datetime.now()
                        nowRT = now.strftime("%m/%d %H:%M")
                        self.parent.reboot_time.append(nowRT)

                        self.parent.net_reboot()
                        self.parent.all_en()                    
                        self.parent.label_9.setText("")                    
                        
                        self.parent.off_air()      

                        time.sleep(1)
                        subprocess.run("adb reboot",shell=True)         
                        time.sleep(20)       
                        self.parent.textBrowser.append("재부팅 후 테더링 연결 중") 
                        self.parent.s_max()
                        for i in range(15):
                            bbs=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
                            bbs = bbs.read().decode('utf-8').strip()
                            bbs= bbs.split("\n")
                            csd = bbs[0][:5].strip()
                            if csd == 'error' or csd=='adb.e' or csd =="" or csd =='adb:' or csd == "adb.:"  or csd == "* dae" or csd == "ad: m":
                                time.sleep(5)
                                     
                            else:
                                
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
                                td_ip="테더링 연결 됨 / " + ip
                                self.parent.textBrowser.append(td_ip)
                                self.parent.s_max()
                                self.parent.AAA=0
                                self.parent.plz_start()
                                self.parent.pushButton_7.setEnabled(False)            
                                self.parent.after_reboot()
                                self.parent.all_de()
                            except:
                                
                                self.parent.textBrowser.append("핸드폰 연결 혹은 데이터 연결 안 됨")
                                self.parent.s_max()
                                self.parent.pushButton_7.setEnabled(False)
                                self.parent.fail_reboot()                                  
                                self.parent.all_de()                            
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
                            time.sleep(5)
                        try:
                            
                            self.parent.all_en()
                            ip=get("https://api.ipify.org").text
                            td_ip="테더링 연결 됨 / " + ip
                            self.parent.textBrowser.append(td_ip)
                            self.parent.s_max()
                            
                            
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
                            except:
                                self.parent.textBrowser.append("모바일 데이터 연결 안 됨")
                                self.parent.s_max()
                                ip=""
                        AAA=0
                        now = datetime.now()
                        
                        nowDT = now.strftime("%H:%M")
                        seven= "재부팅완료 / " + nowDT
                        eight = "테더링완료 / "+ nowDT                    
                        self.parent.textBrowser.append(seven)
                        self.parent.s_max()
                        self.parent.textBrowser.append(eight)                               
                        self.parent.s_max()
                        set_time = self.parent.lineEdit_3.text()
                        
                        self.parent.after_reboot()
                        self.parent.all_de()
                        
                        

#테더링 

class tethering(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):        
        # 인터넷 연결확인 - 인터넷이 연결되어있으면 테더링으로 들어가지 않음
        try:
            self.parent.all_en()
            ip=get("https://api.ipify.org").text
            th_ip = "테더링 연결 됨 / " +ip
            self.parent.textBrowser.append(th_ip)
            self.parent.s_max()
            self.parent.after_tether()
            self.parent.all_de()
        except:
            self.parent.textBrowser.append("테더링 연결중")
            self.parent.s_max()
            self.parent.all_en()
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
            subprocess.run('adb shell input tap 150 1550',shell=True)
            time.sleep(0.2)
            subprocess.run('adb shell input tap 150 1550',shell=True)    
            now = datetime.now()
            nowDT = now.strftime("%H:%M")
            time.sleep(5)
            try :
                ip=get("https://api.ipify.org").text
                nowtether = "테더링 완료 / "+ip +" / "+nowDT
                self.parent.textBrowser.append(nowtether)
                self.parent.s_max()
            except:
                self.parent.textBrowser.append("모바일 데이터 연결 안 됨")
                self.parent.s_max()
            self.parent.all_de()
            self.parent.after_tether()
            self.parent.plz_start()
        


# 디바이스 모델명 확인
class sh_pro(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        
        subprocess.run('adb devices',shell=True)        
        asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        more=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        subprocess.run('adb shell input tap 0 0',shell=True)
        st_asd = st_asd.readline(5).decode('utf-8').strip()
        asd = asd.read().decode('utf-8').strip()        
        more = more.readline(10).decode('utf-8').strip()        
        dfs = subprocess.Popen('adb shell getprop ro.build.version.release',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        dfs= dfs.read().decode('utf-8').strip()
        if asd =='SM-G906S' or asd == 'SM-G906K' or asd == 'SM-G900K'  or asd == 'SM-G900S' or asd == 'SM-G906L' or asd == 'SM-G900L':
            asd = '갤럭시 S5'
        elif asd=='SM-N900S' or asd =='SM-G930S' or asd == 'SM-N900K' or asd == 'SM-N750K':
            asd = '갤럭시 노트3'
        elif asd=='SM-N916K':
            asd= "갤럭시 노트4"
        elif asd=='SM-G720N0':
            asd= "GRAND-MAX"
        elif asd=='SM-G928K':
            asd= "갤럭시edge"
        elif asd=='SM-G960N':
            asd= "갤럭시 S9"
        elif asd=='LG-F650S':
            asd= "LG X Screen"
        elif asd=='LM-Q725K':
            asd= "LG Q7"
        elif asd=='SM-G850K':
            asd= "갤럭시 알파"
        
        elif st_asd == 'error' or st_asd=='adb.e' or st_asd =="" or st_asd =='adb:' or more=='adb.exe: m' or more == "adb: more" or st_asd == "adb.:" or st_asd =="ad: m":            
            asd = ""
            dfs = ""
        
        if asd=="" and more!='adb.exe: m' :
            all="USB 디버깅 허용 혹은 USB 연결 재확인 바람"
        elif asd=="" and  (more=='adb.exe: m' or more == "adb: more"):
            all ="핸드폰 하나만 연결해주세요"
        else:
            all = asd + " / " +dfs
        
        self.parent.textBrowser.append(all)
        self.parent.s_max()
        self.parent.pushButton.setStyleSheet('QPushButton')
        
# 디바이스 연결확인

class sh_device(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        
        subprocess.run('adb shell input keyevent 26',shell=True)
        subprocess.run('adb shell input keyevent 3',shell=True)
        asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        more=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd = st_asd.readline(5).decode('utf-8').strip()
        asd = asd.read().decode('utf-8').strip()
        more = more.readline(10).decode('utf-8').strip()
        
        if (st_asd == 'error'or st_asd =='adb.e' or st_asd =="") or st_asd =='adb:' or st_asd=="adb.:" or st_asd =="ad: m":
            asd = "USB 디버깅 허용 혹은 USB 연결 재확인 바람"
            if more=='adb.exe: m' or more == "adb: more":
                asd="핸드폰 하나만 연결해주세요"
        
        self.parent.textBrowser.append(asd)
        self.parent.s_max()
        self.parent.pushButton_2.setStyleSheet('QPushButton')

# 시작시 디바이스 연결 확인
class st_sh_device(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):               
        asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd = st_asd.readline(5).decode('utf-8').strip()
        asd = asd.read().decode('utf-8').strip()
        
        if st_asd == 'error'or st_asd =='adb.e' or st_asd =='adb:' or st_asd=="adb.:" or st_asd =="ad: m":
            asd = ""
        else:
            self.parent.textBrowser.append(asd)
            self.parent.s_max()
        self.parent.pushButton_2.setStyleSheet('QPushButton')

# 아이피 변경
class ch_ip(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        self.parent.all_en()
        self.parent.on_air()
        time.sleep(5)
        self.parent.off_air()
        time.sleep(5)
        try:
            ip=get("https://api.ipify.org").text
        except:
            ip=("인터넷 연결 안 됨")
        
        now = datetime.now()
        nowDT = now.strftime(" / %m/%d %H:%M")
        nowip = "IP 변경 후 : " + ip + nowDT
        self.parent.textBrowser.append(nowip)
        self.parent.s_max()
        self.parent.pushButton_3.setStyleSheet('QPushButton')
        self.parent.all_de()

# 리부팅 한 시간 ui
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
            AAA = str(i+1) + " / " +str(RT[i])
            self.plainTextEdit.appendPlainText(AAA)


# 첫 시작 로그인화면
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
            if (check_id=='skdi262' and check_pass=='dkdldbxm262!@') or (check_id =="xoqortksaor" and check_pass =="dkfmaekdnj"): 
                self.close()
                myWindow.show()
                myWindow.show_product()    
                myWindow.st_pro()
                myWindow.reserv_start()
            else:
                self.label_3.show()
        else:
            self.label_3.show()
            self.label_3.setText("이용기간이 만료되었습니다.")

#재부팅 예약

class reboot_reserv(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        while True:
            now = datetime.now()
            nowDT = now.strftime("%H:%M")                
            nowPT = now.strftime("%Y/%m/%d/%H/%M")
            nowp = time.strptime(nowPT,"%Y/%m/%d/%H/%M")                   
            exp = time.strptime(self.parent.exdate,"%Y/%m/%d/%H/%M")
            AFAF = '매일 ' + nowDT
            if exp <= nowp:
                self.parent.close()
            if self.parent.checkBox_2.isChecked():
                if self.parent.timelist.currentText() ==AFAF:
                    self.parent.rebooting.start()
                elif self.parent.timelist.currentText() =='테스트1분':
                    time.sleep(60)
                    self.parent.reboot()
                    self.parent.checkBox_2.toggle()
            else:
                pass
            time.sleep(5)


# 사용가능 디바이스 ui
class se_list(QDialog,se_list_class):
    def __init__(self, parent):
        super(se_list,self).__init__(parent)
        self.setupUi(self)        
        self.show()



# 배터리

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
                try :
                    AAA = adbadb.index('level:')
                    BBB =adbadb[AAA+1]
                    self.parent.label_5.setText(BBB)
                    if int(BBB) <=50 :
                        self.parent.bat_r.show()
                    else:
                        self.parent.bat_g.show()
                except:
                    pass
                

            time.sleep(10)




class MyWindow(QMainWindow, form_class):
    
    
    def __init__(self):        
        super().__init__()        
        
        self.setupUi(self)        
        self.total_th = total_th(self)        
        self.sh_pro = sh_pro(self)
        self.rebooting = reboot(self)
        self.tether = tethering(self)
        self.sh_device = sh_device(self)        
        self.ch_ip=ch_ip(self)
        self.st_sh_device = st_sh_device(self)
        self.reboot_reserv=reboot_reserv(self)
        self.battery=battery(self)
        self.battery.start()
        

        
        
        self.pushButton.clicked.connect(self.show_product)
        self.pushButton_2.clicked.connect(self.product)
        self.pushButton_3.clicked.connect(self.change_ip)
        self.pushButton_4.clicked.connect(self.on_tether)
        self.pushButton_5.clicked.connect(self.reboot)        
        self.pushButton_7.clicked.connect(self.plz_start)
        self.pushButton_6.clicked.connect(self.stop_all)
        self.pushButton_11.clicked.connect(self.reboot_window)
        self.bat_r.hide()
        self.bat_g.hide()        
        self.pushButton_12.clicked.connect(self.se_list_window)
        
        self.btn_all_stop.clicked.connect(self.all_stop)

        self.timelist.addItem('선택')
        self.timelist.addItem('테스트1분')
        self.timelist.addItem('매일 00:00')        
        self.timelist.addItem('매일 03:00')
        self.timelist.addItem('매일 06:00')
        self.timelist.addItem('매일 09:00')
        self.timelist.addItem('매일 12:00')        
        
          
        
        self.pushButton_8.clicked.connect(self.reset)
        self.scrollBar = self.textBrowser.verticalScrollBar()
        
        self.setWindowTitle("준소프트/핸드폰도우미_V1_04")
        self.st_time()        
        self.show_ip()
        
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
        self.textBrowser.clear()
    
        
    def reserv_start(self):
        self.reboot_reserv.start()

    def all_stop(self):
        self.stop_all()
        self.rebooting.terminate()
        self.all_de()
        self.after_reboot()
        self.after_tether()
        self.pushButton_7.setStyleSheet('QPushButton')

    def s_max(self):
        time.sleep(0.5)
        self.scrollBar.setValue(self.scrollBar.maximum())

    def non_ip(self):
        self.textBrowser.append("인터넷 연결 안 됨")
        self.s_max()

    def check_net(self):
        ip=get("https://api.ipify.org").text
        now = datetime.now()
        nowDT = now.strftime(" / %m/%d %H:%M")
        nowipDt= ip + nowDT
        self.textBrowser.append(nowipDt)
        self.s_max()

    def reset(self):        
        self.stop_all()
        self.AAA=0   
        self.textBrowser.clear()
        

    def se_list_window(self):
        se_list(self)

    def reboot_window(self):
        reboot_data(self)
    
    
    def clear_3(self):
        self.lineEdit_3.text().clear()

    def all_en(self):
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        
        
        
    def all_de(self):
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.btn_all_stop.setEnabled(True)
        
        

    def stop_th(self):
        self.AAA=0        
        self.pushButton_7.setEnabled(False) 
        self.total_th.terminate()
        self.pushButton_7.setStyleSheet('QPushButton')
        self.label_9.setText("")

    def stop_all(self):
        self.AAA=0
        self.total_th.how_ip.clear()
        self.pushButton_7.setEnabled(True) 
        self.total_th.terminate()
        self.pushButton_7.setStyleSheet('QPushButton')
        self.label_9.setText("")
        self.lineEdit_3.clear()
        

    def plz_start(self):
        
        self.pushButton_7.setStyleSheet('QPushButton {background-color: red; color:white}')
        self.pushButton_7.setEnabled(False)
        self.total_th.start()
        

    def adb_dvices(self):
        subprocess.run('adb devices',shell=True)
        time.sleep(0.5)
        
    
    def show_product(self):
        self.pushButton.setStyleSheet('QPushButton {background-color: red; color:white}')
        self.sh_pro.start()
        
        

    def product(self):
        self.pushButton_2.setStyleSheet('QPushButton {background-color: red; color:white}')
        self.sh_device.start()
        
    def st_pro(self):
        self.st_sh_device.start()


    def on_air(self):

        subprocess.run('adb shell settings put global airplane_mode_on 1',shell=True)
        subprocess.run("adb shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true",shell=True)

    def off_air(self):

        subprocess.run('adb shell settings put global airplane_mode_on 0',shell=True)
        subprocess.run("adb shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false",shell=True)

    def change_ip(self):
        self.pushButton_3.setStyleSheet('QPushButton {background-color: red; color:white}')
        self.ch_ip.start()

    def ch_reboot(self):
        self.pushButton_5.setStyleSheet('QPushButton')
    

    def reboot(self):
        self.pushButton_5.setStyleSheet('QPushButton {background-color: red; color:white}')
        
        self.rebooting.start()
        
    def fail_reboot(self):
        self.pushButton_5.setStyleSheet('QPushButton {color:black}')

    def after_reboot(self):
        
        self.pushButton_7.setStyleSheet('QPushButton {background-color: red; color:white}')
        self.pushButton_5.setStyleSheet('QPushButton {color:black}')
    
    def net_reboot(self):       
        
        self.pushButton_5.setStyleSheet('QPushButton {background-color: red; color:white}')
        self.pushButton_7.setStyleSheet('QPushButton')

    def on_tether(self):        
        self.pushButton_4.setStyleSheet('QPushButton {background-color: red; color:white}')
        self.tether.start()
        
    def tether_btn(self):
        self.pushButton_4.setStyleSheet('QPushButton {background-color: red; color:white}')

    def after_tether(self):
        self.pushButton_4.setStyleSheet('QPushButton')
    
    
    def st_time(self):
        now = datetime.now()        
        nowRT = now.strftime("%m/%d %H:%M")
        self.textBrowser.append(nowRT)
        self.s_max()

    def show_ip(self):
        try:
            ip=get("https://api.ipify.org").text            
            self.textBrowser.append(ip)
            self.s_max()
        except:
            self.textBrowser.append("인터넷 연결 안 됨")    
            self.s_max()
    def killthem(self):
        
        app.exec_()
        subprocess.run("taskkill /f /im adb.exe", shell=True)
    

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    chch= ch_user(myWindow)
    chch.show()        
    myWindow.all_en()    
    myWindow.killthem()
    