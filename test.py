from PyQt5 import QtWidgets
import cx_Oracle
import multiprocessing
import sys
import smtplib 
from email.mime.text import MIMEText
from typing import Awaitable
from PyQt5.QtGui import *

import paramiko
import pandas as pd
import random

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import os
import time
import pymysql
import subprocess
import string

from requests import get
from datetime import datetime
from socket import *
from select import *
import threading



now_file = os.getcwd()

form_class = uic.loadUiType(now_file +r"\uis\untitled.ui")[0]

np_user_class = uic.loadUiType(now_file +r"\uis\np_user.ui")[0]
reboot_class = uic.loadUiType(now_file +r"\uis\reboot_data.ui")[0]
se_list_class = uic.loadUiType(now_file +r"\uis\se_list.ui")[0]
newbie_class = uic.loadUiType(now_file +r"\uis\newbie.ui")[0]
find_id_class = uic.loadUiType(now_file +r"\uis\find_id.ui")[0]
find_pass_class = uic.loadUiType(now_file +r"\uis\find_pass.ui")[0]
# cx_Oracle.init_oracle_client(lib_dir=now_file+r"\instantclient_21_3") 
LOCATION = now_file+r"\instantclient_21_3"
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"] #환경변수 등록
# print(form_class)
# form_class = uic.loadUiType("untitled.ui")[0]
class np_user_co(QThread):
    ch_pass =0
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
    def run(self) :
        HOST = '210.179.24.204'
        PORT = 9998
        BUFSIZE = 1024
        ADDR = (HOST,PORT)

        clientSocket = socket(AF_INET, SOCK_STREAM)# 서버에 접속하기 위한 소켓을 생성한다.

        try:
            
            A="np_user|"
            new_pass= self.parent.pass_edit.text().strip()+"|"
            user_id = self.parent.user_id
            
            C=A+new_pass+user_id
            print(C)
            clientSocket.connect(ADDR)# 서버에 접속을 시도한다.            
            clientSocket.send(C.encode())	# 서버에 메시지 전달                    
            
            
                
        except  Exception as e:
            print("실패",'%s:%s'%ADDR)
            

        print('connect is success')
        clientSocket.close()
class find_pass_mail(QThread):
    ch_pass =0
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
    def run(self) :
        HOST = '210.179.24.204'
        PORT = 9998
        BUFSIZE = 1024
        ADDR = (HOST,PORT)

        clientSocket = socket(AF_INET, SOCK_STREAM)# 서버에 접속하기 위한 소켓을 생성한다.

        try:
            
            A="find_pass_mail|"
            new_pass= self.parent.new_pw +"|"
            user_name = self.parent.name_edit.text().strip()+ "|"
            user_mail = self.parent.email_edit.text().strip()+"|"
            user_id = self.parent.id_edit.text().strip()
            
            C=A+new_pass+user_name+user_mail+user_id
            clientSocket.connect(ADDR)# 서버에 접속을 시도한다.            
            clientSocket.send(C.encode())	# 서버에 메시지 전달                    
            data=clientSocket.recv(65535)
            self.ch_pass= int(data.decode())
            
                
        except  Exception as e:
            print("실패",'%s:%s'%ADDR)
            

        print('connect is success')
        clientSocket.close()

    
class find_pass_co(QThread):
    ch_pass =0
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
    def run(self) :
        HOST = '210.179.24.204'
        PORT = 9998
        BUFSIZE = 1024
        ADDR = (HOST,PORT)

        clientSocket = socket(AF_INET, SOCK_STREAM)# 서버에 접속하기 위한 소켓을 생성한다.

        try:
            
            A="find_pass|"
            user_name = self.parent.name_edit.text().strip()+ "|"
            user_mail = self.parent.email_edit.text().strip()+"|"
            user_id = self.parent.id_edit.text().strip()
            
            C=A+user_name+user_mail+user_id
            clientSocket.connect(ADDR)# 서버에 접속을 시도한다.            
            clientSocket.send(C.encode())	# 서버에 메시지 전달                    
            data=clientSocket.recv(65535)
            
            self.ch_pass = data.decode()
                
        except  Exception as e:
            print("실패",'%s:%s'%ADDR)
            

        print('connect is success')
        clientSocket.close()

    
class find_id_co(QThread):
    ch_id =''
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
    def run(self) :
        HOST = '210.179.24.204'
        PORT = 9998
        BUFSIZE = 1024
        ADDR = (HOST,PORT)

        clientSocket = socket(AF_INET, SOCK_STREAM)# 서버에 접속하기 위한 소켓을 생성한다.

        try:
            
            A="find_id|"
            user_name = self.parent.name_edit.text().strip()+ "|"            
            
            user_mail = self.parent.email_edit.text().strip()
            
            C=A+user_name+user_mail
            clientSocket.connect(ADDR)# 서버에 접속을 시도한다.            
            clientSocket.send(C.encode())	# 서버에 메시지 전달                    
            data=clientSocket.recv(65535)
            self.ch_id= data.decode()      
                
        except  Exception as e:
            print("실패",'%s:%s'%ADDR)
            

        print('connect is success')
        clientSocket.close()

    
        
    
class newbie_make(QThread):
    ch_id =0
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
    def run(self) :
        HOST = '210.179.24.204'
        PORT = 9998
        BUFSIZE = 1024
        ADDR = (HOST,PORT)

        clientSocket = socket(AF_INET, SOCK_STREAM)# 서버에 접속하기 위한 소켓을 생성한다.

        try:
            
            A="newbie_make|"
            user_name = self.parent.name_edit.text().strip()+ "|"
            user_id = self.parent.id_edit.text().strip()+ "|"
            user_pass = self.parent.pass_edit.text().strip()+ "|"            
            user_mail = self.parent.email_edit.text().strip()+ "|"
            user_mob = self.parent.mob_edit.text().strip()
            C=A+user_name+user_id+user_pass+user_mail+user_mob
            clientSocket.connect(ADDR)# 서버에 접속을 시도한다.            
            clientSocket.send(C.encode())	# 서버에 메시지 전달                    
            
                
        except  Exception as e:
            print("실패",'%s:%s'%ADDR)
            

        print('connect is success')
        clientSocket.close()
        
        
    def ex_ck(self):
        sys.exit()


class newbie_soc(QThread):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.ch_id =0    
        
    def run(self) :
        HOST = '210.179.24.204'
        PORT = 9998
        BUFSIZE = 1024
        ADDR = (HOST,PORT)

        clientSocket = socket(AF_INET, SOCK_STREAM)# 서버에 접속하기 위한 소켓을 생성한다.

        try:
            
            A="newbie_check|"
            B=self.parent.id_edit.text().strip()
            C=A+B
            clientSocket.connect(ADDR)# 서버에 접속을 시도한다.            
            clientSocket.send(C.encode())	# 서버에 메시지 전달                    
            data=clientSocket.recv(65535)
            clclcl= data.decode()                            
            self.ch_id = int(clclcl)
            
            
                
        except  Exception as e:
            print("실패",'%s:%s'%ADDR)
            

        print('connect is success')
        clientSocket.close()
    



class cli_ck(QThread):
    log_id=''
    t_log_id=''
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    def run(self) :
        HOST = '210.179.24.204'
        PORT = 9998
        BUFSIZE = 1024
        ADDR = (HOST,PORT)
        AFAF= datetime.now()
        ADAD = datetime.strftime(AFAF,'%H : %M')
        
    
        self.clientSocket = socket(AF_INET, SOCK_STREAM)# 서버에 접속하기 위한 소켓을 생성한다.
        self.clientSocket.connect(ADDR)# 서버에 접속을 시도한다.
        while True:
            try:
                
                ip=get("https://api.ipify.org").text.encode()                
                A = "user_ch|"+self.parent.lineEdit_2.text() + "|"
                D = A.encode()
                B = self.parent.lineEdit.text() + "|"
                F = ADAD.encode()
                E = B.encode()
                C= D+E+ip+"|".encode()+F
                self.clientSocket.send(C)	# 서버에 메시지 전달  
                data=self.clientSocket.recv(65535)
                clclcl= data.decode()         
                self.log_id = clclcl                
                if clclcl =="toom":
                    self.t_log_id = "toom"
            except  Exception as e:
                print("실패",'%s:%s'%ADDR)
                print("why")
                self.clientSocket.close()
                break
            print('connect is success')

    

    def ex_ck(self):
        sys.exit()

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
        
        if st_asd == 'error'or st_asd =='adb.e' or st_asd =="" or st_asd == "adb.:":
            asd = "핸드폰과 PC 연결 상태 확인 후 재시도 바람"
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
            for i in range(15):
                bbs=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
                bbs = bbs.read().decode('utf-8').strip()
                bbs= bbs.split("\n")
                csd = bbs[0][:5].strip()
                print(csd)
                if csd == 'error' or csd=='adb.e' or csd =="" or csd =='adb:' or csd == "adb.:"  or csd == "* dae":
                    time.sleep(5)
                    print(csd)        
                else:
                    print(csd)      
                    break
            if csd == 'error' or csd=='adb.e' or csd =="" or csd =='adb:' or csd == "adb.:"  or csd == "* dae":
                time.sleep(10)
                subprocess.run("adb shell input keyevent 3",shell=True)
                time.sleep(0.5)
                subprocess.run("adb shell input keyevent 3",shell=True)
                time.sleep(0.5)
                subprocess.run('adb shell input tap 0 0',shell=True)                
                asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
                asd = asd.read().decode('utf-8').strip()
                time.sleep(0.5)
                if asd =='SM-N750K' or asd == 'SM-G720N0' or asd=="SM-G900S":
                    subprocess.run('adb shell input swipe 170 1070 170 250 300',shell=True)
                elif asd == 'SM-G930S':
                    subprocess.run('adb shell input swipe 670 1450 670 750 300',shell=True)
                else :
                    subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)
                    subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)        
                self.parent.off_air()          
                time.sleep(0.5)
                subprocess.run("adb shell input keyevent 3",shell=True)
                time.sleep(3)        
                subprocess.run("adb shell am start -n com.android.settings/.TetherSettings",shell=True)  
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
                    if asd =='SM-N750K' or asd == 'SM-G720N0' or asd=="SM-G900S":
                        subprocess.run('adb shell input swipe 170 1070 170 250 300',shell=True)
                    elif asd == 'SM-G930S':
                        subprocess.run('adb shell input swipe 670 1450 670 750 300',shell=True)
                    else :
                        subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)
                        subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)        
                    self.parent.off_air()          
                    time.sleep(0.5)
                    subprocess.run("adb shell input keyevent 3",shell=True)
                    time.sleep(3)        
                    subprocess.run("adb shell am start -n com.android.settings/.TetherSettings",shell=True)  
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
                if asd =='SM-N750K' or asd == 'SM-G720N0' or asd=="SM-G900S":
                    subprocess.run('adb shell input swipe 170 1070 170 250 300',shell=True)
                elif asd == 'SM-G930S':
                    subprocess.run('adb shell input swipe 670 1450 670 750 300',shell=True)
                else :
                    subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)
                    subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)        
                self.parent.off_air()          
                time.sleep(0.5)
                subprocess.run("adb shell input keyevent 3",shell=True)
                time.sleep(3)        
                subprocess.run("adb shell am start -n com.android.settings/.TetherSettings",shell=True)  
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
                    except:
                        self.parent.textBrowser.append("모바일 데이터 연결 안 됨")
                        self.parent.s_max()
                        ip=""
                
                
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
        

class total_th(QThread):
    how_ip =[]
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    
        
                
    def run(self):
        self.parent.off_air()
        st_text3 = self.parent.lineEdit_3.text()
        print("|"+st_text3+"|")
        AAA= self.parent.AAA
        set_time =0
        bbb = 0
        print(AAA)
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
                    elif(self.how_ip[0] == self.how_ip [1]) != self.how_ip [2]:
                        cnrk  = self.how_ip [2]
                        self.how_ip.clear()
                        self.how_ip.append(cnrk)
                print(self.how_ip)
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

                print(AAA)
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
                print(AAA)
                if st_text3 =='' and AAA==0:
                    self.parent.off_air()
                    st_st = '300'
                    st_aa = "네트워크 미확인 "+st_st+"초 후 재확인"
                    self.parent.textBrowser.append(st_aa)
                    self.parent.s_max()
                    AAA= AAA+1
                    bbb=300
                    # adb root                     - restarts the adbd daemon with root permissions
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
                    if asd =='SM-N750K' or asd == 'SM-G720N0' or asd=="SM-G900S":
                        subprocess.run('adb shell input swipe 170 1070 170 250 300',shell=True)
                    elif asd == 'SM-G930S':
                        subprocess.run('adb shell input swipe 670 1450 670 750 300',shell=True)
                    else :
                        subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)
                        subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)   
                    time.sleep(0.5)
                    subprocess.run("adb shell input keyevent 3",shell=True)
                    time.sleep(3)                    
                    subprocess.run("adb shell am start -n com.android.settings/.TetherSettings",shell=True)                
                    time.sleep(1)
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
                        for i in range(15):
                            bbs=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
                            bbs = bbs.read().decode('utf-8').strip()
                            bbs= bbs.split("\n")
                            csd = bbs[0][:5].strip()
                            if csd == 'error' or csd=='adb.e' or csd =="" or csd =='adb:' or csd == "adb.:"  or csd == "* dae":
                                time.sleep(5)
                                print(csd)        
                            else:
                                print(csd)        
                                break
                        if csd == 'error' or csd=='adb.e' or csd =="" or csd =='adb:' or csd == "adb.:"  or csd == "* dae":
                            time.sleep(10)
                            subprocess.run("adb shell input keyevent 3",shell=True)
                            time.sleep(0.5)
                            subprocess.run("adb shell input keyevent 3",shell=True)
                            time.sleep(0.5)
                            subprocess.run('adb shell input tap 0 0',shell=True)                
                            asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
                            asd = asd.read().decode('utf-8').strip()
                            time.sleep(0.5)
                            if asd =='SM-N750K' or asd == 'SM-G720N0' or asd=="SM-G900S":
                                subprocess.run('adb shell input swipe 170 1070 170 250 300',shell=True)
                            elif asd == 'SM-G930S':
                                subprocess.run('adb shell input swipe 670 1450 670 750 300',shell=True)
                            else :
                                subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)
                                subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)        
                            self.parent.off_air()          
                            time.sleep(0.5)
                            subprocess.run("adb shell input keyevent 3",shell=True)
                            time.sleep(3)        
                            subprocess.run("adb shell am start -n com.android.settings/.TetherSettings",shell=True)  
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
                            if asd =='SM-N750K' or asd=='SM-G720N0' or asd == 'SM-G900S':
                                subprocess.run('adb shell input swipe 170 1070 170 250 300',shell=True)
                            elif asd == 'SM-G930S':
                                subprocess.run('adb shell input swipe 670 1450 670 750 300',shell=True)
                            else :
                                subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)
                                subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)        
                            self.parent.off_air()          
                            time.sleep(0.5)
                            subprocess.run("adb shell input keyevent 3",shell=True)
                            time.sleep(3)                    
                            subprocess.run("adb shell am start -n com.android.settings/.TetherSettings",shell=True)                
                            time.sleep(1)
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
                            td_ip="테더링 연결 됨 / " + ip
                            self.parent.textBrowser.append(td_ip)
                            self.parent.s_max()
                            # sh: resetreason: can't execute: Permission denied
                            
                        except:
                            
                            time.sleep(0.5)
                            subprocess.run("adb shell input keyevent 3",shell=True)
                            time.sleep(3)        
                            subprocess.run("adb shell am start -n com.android.settings/.TetherSettings",shell=True)  
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
                        print(AAA)
                        print(set_time)



class tethering(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):        
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
            # adb shell input touchscreen swipe  670 1450 660 750 300
            time.sleep(0.5)
            if asd =='SM-N750K' or asd == "SM-G720N0" or asd=="SM-G900S" :
                subprocess.run('adb shell input swipe 170 1070 170 250 300',shell=True)
            elif asd == 'SM-G930S':
                subprocess.run('adb shell input swipe 170 1070 170 250 300',shell=True)
            else :
                subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)
                subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)      
            time.sleep(0.5)

            subprocess.run("adb shell am start -n com.android.settings/.TetherSettings",shell=True)                
            time.sleep(0.5)
            subprocess.run("adb shell input keyevent 20",shell=True)                
            time.sleep(0.5)
            subprocess.run("adb shell input keyevent 20",shell=True)                
            time.sleep(0.5)
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

            now = datetime.now()
            nowDT = now.strftime("%H:%M")
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
        elif asd=='SM-G720N0':
            asd= "GRAND-MAX"
        elif st_asd == 'error' or st_asd=='adb.e' or st_asd =="" or st_asd =='adb:' or more=='adb.exe: m' or st_asd=="adb.:":
            print(st_asd)
            asd = ""
            dfs = ""
        
        if asd=="" and more!='adb.exe: m':
            all="USB 디버깅 허용 혹은 USB 연결 재확인 바람"
        elif asd=="" and  (more=='adb.exe: m' or more =="adb: more"):
            all ="하나의 기기만 연결해주세요"
        else:
            all = asd + " / " +dfs
        
        # self.parent.textBrowser.setText(all)
        self.parent.textBrowser.append(all)
        self.parent.pushButton.setStyleSheet('QPushButton')
        self.parent.s_max()
        
        
            

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
        
        if (st_asd == 'error'or st_asd =='adb.e' or st_asd =="") or st_asd =='adb:' or st_asd=="adb.:":
            asd = "USB 디버깅 허용 혹은 USB 연결 재확인 바람"
            if more=='adb.exe: m' or more == "adb: more":
                asd="핸드폰 하나만 연결해주세요"
        
        self.parent.textBrowser.append(asd)
        self.parent.s_max()
        self.parent.pushButton_2.setStyleSheet('QPushButton')

class st_sh_device(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):               
        asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd = st_asd.readline(5).decode('utf-8').strip()
        asd = asd.read().decode('utf-8').strip()
        
        if st_asd == 'error'or st_asd =='adb.e' or st_asd =='adb:' or st_asd=="adb.:":
            asd = ""
        else:
            self.parent.textBrowser.append(asd)
            self.parent.s_max()
        self.parent.pushButton_2.setStyleSheet('QPushButton')


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
        print(ip)
        now = datetime.now()
        nowDT = now.strftime(" / %m/%d %H:%M")
        nowip = "IP 변경 후 : " + ip + nowDT
        self.parent.textBrowser.append(nowip)
        time.sleep(0.5)
        self.parent.s_max()
        self.parent.pushButton_3.setStyleSheet('QPushButton')
        self.parent.all_de()

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

class newbie(QDialog,newbie_class):
    
    def __init__(self, parent):
        super(newbie,self).__init__(parent)
        
        self.setupUi(self)    
        self.show()
        self.pushButton.clicked.connect(self.ch_id)
        self.pushButton_2.clicked.connect(self.newnew)
        self.new_sco = newbie_soc(self)
        self.new_make = newbie_make(self)
        
        self.pushButton_2.setEnabled(False)
    def ch_id(self):        
        
        time.sleep(1)
        if self.id_edit.text().strip() =="":
            self.non_id()
        else:
            self.new_sco.start()
            time.sleep(2)
            if self.new_sco.ch_id !=0:                
                self.overlap()
            elif self.new_sco.ch_id ==0:
                self.ok_sign()
                self.pushButton_2.setEnabled(True)
        

    def newnew(self):
        
        user_name = self.name_edit.text().strip()
        user_id = self.id_edit.text().strip()
        user_pass = self.pass_edit.text().strip()
        user_cpass = self.cpass_edit.text().strip()
        user_mail = self.email_edit.text().strip()
        user_mob = self.mob_edit.text().strip()

        if user_cpass =="" or user_id == "" or user_mail =="" or user_mob =="" or user_name =="" or user_pass=="":
            
            self.plz_all()
        elif (user_cpass !="" or user_id != "" or user_mail !="" or user_mob !="" or user_name !="" or user_pass!="") and user_pass==user_cpass:            
            self.new_make.start()
            time.sleep(1)
            self.ok_id()
            self.close()
            self.new_make.terminate()
        elif (user_cpass !="" or user_id != "" or user_mail !="" or user_mob !="" or user_name !="" or user_pass!="") and user_pass != user_cpass:
            self.msg()
    def ok_sign(self):
        QtWidgets.QMessageBox.information(self,"QMessageBox", "가입 가능한 id 입니다.")
    def msg(self):
        QtWidgets.QMessageBox.information(self,"QMessageBox", "비밀번호를 확인해주세요")
    def plz_all(self):
        QtWidgets.QMessageBox.information(self,"QMessageBox", "빈칸없이 모두 입력해주세요")
    def overlap(self):
        QtWidgets.QMessageBox.information(self,"QMessageBox", "중복된 아이디 입니다.")
    def non_id(self):
        QtWidgets.QMessageBox.information(self,"QMessageBox", "아이디를 입력해주세요.")
    def ok_id(self):
        QtWidgets.QMessageBox.information(self,"QMessageBox", "회원가입에 성공했습니다.")
        
        
        
class find_id(QDialog,find_id_class):
    def __init__(self, parent):
        super(find_id,self).__init__(parent)
        self.setupUi(self)        
        self.show()
        self.pushButton.clicked.connect(self.fid)        
        self.pushButton_2.clicked.connect(self.fpass)
        self.fi_id=find_id_co(self)

    def fpass(self):
        find_pass(self)

    def fid(self):
        self.fi_id.start()
        time.sleep(1)
        if self.fi_id.ch_id !='':
            self.label_6.setText("찾으시는 아이디는 "+self.fi_id.ch_id+" 입니다.")
        else:
            self.label_6.setText("등록된 이름 혹은 이메일이 없습니다.")
        self.fi_id.terminate()

class find_pass(QDialog,find_pass_class):
    

    def __init__(self, parent):
        super(find_pass,self).__init__(parent)
        self.setupUi(self)        
        self.show()
        self.pushButton.clicked.connect(self.gogomail)
        self.fi_pass= find_pass_co(self)  
        self.fi_pass_mail = find_pass_mail(self)
        self.new_pw = ''

    def gogomail(self):
        self.fi_pass.start()
        time.sleep(1)
        self.fi_pass.terminate()
        if int(self.fi_pass.ch_pass) >=1:
            newpass=8
            newcode=string.ascii_letters + string.digits
            
            for i in range(newpass) :
                self.new_pw += random.choice(newcode)
            self.fi_pass_mail.start()
            time.sleep(1)
            self.fi_pass_mail.terminate()
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login('tjdwnd262@gmail.com','dkdldbxm262!@')
            msg= MIMEText("회원님의 비밀번호는 " +self.new_pw+ "입니다")
            msg['Subject']="비밀번호 초기화"
            s.sendmail("tjdwnd262@gmail.com",'skdi262@naver.com',msg.as_string())
            s.quit()            
            self.label_7.setText("등록된 이메일로 비밀번호를 보냈습니다.")
            self.label_8.setText("초기화된 비밀번호로 다시 로그인 해주세요.")
        else:
            self.label_7.setText("등록된 이름 혹은 이메일이 없습니다.")
        


class np_user(QDialog,np_user_class):
    
    def __init__(self, parent):
        super(np_user,self).__init__(parent)
        self.setupUi(self)        
        self.show()
        self.pushButton.clicked.connect(self.ch_pass)
        self.np_co = np_user_co(self)
        self.user_id = ''

    def ch_pass(self):
        
        mw= MyWindow()
        
        self.user_id = mw.user_id[0]        
        check_pass = self.pass_edit.text().strip()
        check_cpass = self.cpass_edit.text().strip()
        if (check_pass==check_cpass) and check_pass !="" :
            self.np_co.start()
            self.ok_pass()
            self.close()
            time.sleep(1)
            self.np_co.terminate()
        else:
            self.label_10.setText("비밀번호가 일치하지 않습니다.")
        
        

    def ok_pass(self):
        QtWidgets.QMessageBox.information(self,"QMessageBox", "비밀번호가 변경되었습니다.")





class se_list(QDialog,se_list_class):
    def __init__(self, parent):
        super(se_list,self).__init__(parent)
        self.setupUi(self)        
        self.show()
        

    # def asdasd(self):
        
        
        

class MyWindow(QMainWindow, form_class):
    
    
    def __init__(self):
        
        super().__init__()        
        
        self.setupUi(self)        
        self.total_th = total_th(self)
        
        self.sh_pro = sh_pro(self)
        self.rebooting = reboot(self)
        self.tether = tethering(self)
        self.sh_device = sh_device(self)

        self.cli_ck = cli_ck(self)
        self.ch_ip=ch_ip(self)
        self.st_sh_device = st_sh_device(self)
        self.pushButton.clicked.connect(self.show_product)
        self.pushButton_2.clicked.connect(self.product)
        self.pushButton_3.clicked.connect(self.change_ip)
        self.pushButton_4.clicked.connect(self.on_tether)
        self.pushButton_5.clicked.connect(self.reboot)
        self.pushButton_9.clicked.connect(self.check_user)
        self.pushButton_10.clicked.connect(self.newbie_window)
        self.pushButton_7.clicked.connect(self.plz_start)
        self.pushButton_6.clicked.connect(self.stop_all)
        self.pushButton_11.clicked.connect(self.reboot_window)
        self.lineEdit.returnPressed.connect(self.check_user)
        self.lineEdit_2.returnPressed.connect(lambda: self.focusNextChild())
        self.pushButton_12.clicked.connect(self.se_list_window)
        self.pushButton_13.clicked.connect(self.find_id_window)
        self.btn_all_stop.clicked.connect(self.all_stop)
        self.pushButton_12.hide()        
        self.setWindowTitle("준소프트/CH_NET_69")
        self.label_6.hide()
        self.pushButton_8.clicked.connect(self.reset)
        self.pushButton_8.hide()
        self.label_3.setStyleSheet("Color:red")
        self.label_3.hide()
        self.scrollBar = self.textBrowser.verticalScrollBar()
        self.btn_all_stop.setEnabled(False)
        
        

    reboot_time = []
    AAA = 0
    stop_time = 300
    XXX=0
    FFF=0
    user_id=[]
    
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
    def newbie_window(self):
        newbie(self)

    def se_list_window(self):
        se_list(self)

    def reboot_window(self):
        reboot_data(self)

    def find_id_window(self):
        find_id(self)

    def clear_3(self):
        self.lineEdit_3.text().clear()

    def check_user(self):
        self.cli_ck.start()
        time.sleep(3)
        
        if  self.cli_ck.log_id =='nok':
            self.cli_ck.terminate()
            self.user_id.append(self.lineEdit_2.text())
            print(self.user_id[0])
            np_user(self)
        if self.cli_ck.log_id =='ok':
            print('hi')
            self.all_de()
            self.lineEdit.hide()
            self.lineEdit_2.hide()
            self.label.hide()
            self.label_2.hide()
            self.pushButton_9.hide()
            self.pushButton_10.hide()
            self.pushButton_8.show()
            self.label_6.show()
            self.pushButton_12.show()
            self.pushButton_13.hide()
            self.label_3.hide()
            self.adb_dvices()
            self.show_product()    
            self.st_pro()
            self.show_ip()
        elif self.cli_ck.t_log_id =='toom':
            self.cli_ck.terminate()
            print("초과 확인")
            self.label_3.show()
            self.label_3.setText("이용가능 계정 수 가 초과되었습니다.")
            self.cli_ck.t_log_id=""
            
        else:
            
            
            self.cli_ck.terminate()
            self.label_3.show()
            self.label_3.setText("아이디 / 비밀번호를 확인해주세요.")
        
     
            
        
        


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
        

    def btn_clicked(self):
        QMessageBox.about(self,"message","clicked")
        asd = os.popen('adb devices').readline()[0:4]
        asd.strip()
        if(asd=='List'):
            print("예쓰")
        
        print(asd)
    def show_product(self):
        self.pushButton.setStyleSheet('QPushButton {background-color: red; color:white}')
        self.sh_pro.start()
        
        

    def product(self):
        self.pushButton_2.setStyleSheet('QPushButton {background-color: red; color:white}')
        self.sh_device.start()
        
    def st_pro(self):
        self.st_sh_device.start()

    def device_check(self):
        os.system('adb shell input tap 0 0')
        data=subprocess.Popen('adb devices',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        dout = data.read().decode('utf-8').strip()[25:35]
        dout=dout.strip()
        asd = os.popen('adb devices').readlines()[1].rstrip()
        asd = asd[0:8]
        asd.strip()
        print(asd)
        
        self.textBrowser.append(asd)
        self.s_max()


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
    def fail_reboot(self):
        self.pushButton_5.setStyleSheet('QPushButton {color:black}')

    def reboot(self):
        self.pushButton_5.setStyleSheet('QPushButton {background-color: red; color:white}')
        
        self.rebooting.start()
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
        

    def get_ip(self):
        s_ip = ''
        try:
            ip=get("https://api.ipify.org").text
            print(ip)
            self.AAA=0
        except:
            print("hi")        
    
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
    def ex_ck(self):
        self.cli_ck.ex_ck()
        
        
        
            
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    myWindow.st_time()
    myWindow.all_en()
    myWindow.off_air()    
    app.exec_()
    subprocess.run('adb kill-server',shell=True)
    myWindow.ex_ck()
    