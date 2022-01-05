from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.uic.uiparser import WidgetStack
from socket import *
from select import *
import cx_Oracle
import multiprocessing
import sys
import smtplib 
from email.mime.text import MIMEText
from typing import Awaitable, Container
from PyQt5.QtGui import *

import paramiko
import pandas as pd
import random
from dateutil.relativedelta import relativedelta
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import os
import time
import pymysql
import subprocess
import string
from datetime import datetime, timedelta
from requests import get
from datetime import datetime
import threading



now_file = os.getcwd()

form_class = uic.loadUiType(now_file +r"\ad_uis\admin.ui")[0]

LOCATION = now_file+r"\instantclient_21_3"
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"] #환경변수 등록



class ch_th(QThread):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.clclcl=""
    def run(self):
        HOST = '210.179.24.204'

        PORT = 9998
        BUFSIZE = 1024
        ADDR = (HOST,PORT)
        clientSocket = socket(AF_INET, SOCK_STREAM)# 서버에 접속하기 위한 소켓을 생성한다.
        try:
            clientSocket.connect(ADDR)# 서버에 접속을 시도한다.    
            A = 'admin_user|user_ch'
            clientSocket.send(A.encode())
            data=clientSocket.recv(65535)
            self.clclcl= data.decode()
                    
        except  Exception as e:
            print("실패",'%s:%s'%ADDR)
        print('connect is success')
        clientSocket.close()

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()                
        self.setupUi(self)        
        

        
        self.ch_th = ch_th(self)
        
        self.pushButton.clicked.connect(self.update_user)        
        self.de_btn.clicked.connect(self.del_user)
        self.new_btn.clicked.connect(self.new_user)
        
        
        
        self.st_calendar.hide()
        self.new_calendar.hide()
        self.ex_calendar.hide()
        
        
        
        
        
        
        

        self.lineEdit_5.mousePressEvent = self.st_cal
        self.lineEdit_7.mousePressEvent = self.new_cal
        self.lineEdit_8.mousePressEvent = self.ex_cal

        self.st_calendar.clicked.connect(self.plus_st)
        self.ex_calendar.clicked.connect(self.plus_ex)
        self.new_calendar.clicked.connect(self.plus_new)

        

        self.btn_all_list.clicked.connect(self.user_list)
        self.btn_log_list.clicked.connect(self.log_list)
        self.btn_grade_list.clicked.connect(self.grade_list)
        self.btn_root_list.clicked.connect(self.root_list)
        self.plus_d.clicked.connect(self.st_plus_d)
        self.plus_w.clicked.connect(self.st_plus_w)
        self.plus_m.clicked.connect(self.st_plus_m)
        self.ex_plus_d.clicked.connect(self.ex_plus_df)
        self.ex_plus_w.clicked.connect(self.ex_plus_wf)
        self.ex_plus_m.clicked.connect(self.ex_plus_mf)

        self.sel_able.addItem("Y")
        self.sel_able.addItem("N")
        
        
        
        
        
        self.table.clicked.connect(self.cl)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.resizeColumnsToContents()
        self.btn_search.clicked.connect(self.search)
        
        self.sel_option.addItem("검색옵션")
        self.sel_option.addItem("아이디")
        self.sel_option.addItem("이메일")

    def st_plus_d(self):
        
        AAA = self.lineEdit_7.text()
        if AAA != '':
            format='%y/%m/%d'
            BBB= datetime.strptime(AAA,format)
            DDD=timedelta(days=1)
            BBB= BBB+DDD
            CCC= datetime.strftime(BBB,'%y/%m/%d')
            self.lineEdit_7.setText(CCC)
        if AAA == "":
            BBB=datetime.now()
            DDD=timedelta(days=1)
            BBB = BBB+ DDD
            CCC= datetime.strftime(BBB,'%y/%m/%d')
            self.lineEdit_7.setText(CCC)
    def st_plus_w(self):
        
        AAA = self.lineEdit_7.text()
        if AAA != '':
            format='%y/%m/%d'
            BBB= datetime.strptime(AAA,format)
            DDD=timedelta(weeks=1)
            BBB= BBB+DDD
            CCC= datetime.strftime(BBB,'%y/%m/%d')
            self.lineEdit_7.setText(CCC)
        if AAA == "":
            BBB=datetime.now()
            DDD=timedelta(weeks=1)
            BBB = BBB+ DDD
            CCC= datetime.strftime(BBB,'%y/%m/%d')
            self.lineEdit_7.setText(CCC)
    def st_plus_m(self):
        
        AAA = self.lineEdit_7.text()
        if AAA != '':
            format='%y/%m/%d'
            BBB= datetime.strptime(AAA,format)
            DDD= relativedelta(months=1)
            BBB= BBB+DDD
            CCC= datetime.strftime(BBB,'%y/%m/%d')
            self.lineEdit_7.setText(CCC)
        if AAA == "":
            BBB=datetime.now()
            DDD= relativedelta(months=1)
            BBB = BBB+ DDD
            CCC= datetime.strftime(BBB,'%y/%m/%d')
            self.lineEdit_7.setText(CCC)

    def ex_plus_df(self):
        
        AAA = self.lineEdit_8.text()
        if AAA != '':
            format='%y/%m/%d'
            BBB= datetime.strptime(AAA,format)
            DDD=timedelta(days=1)
            BBB= BBB+DDD
            CCC= datetime.strftime(BBB,'%y/%m/%d')
            self.lineEdit_8.setText(CCC)
            
        if AAA == "":
            BBB=datetime.now()
            DDD=timedelta(days=1)
            BBB = BBB+ DDD
            CCC= datetime.strftime(BBB,'%y/%m/%d')
            self.lineEdit_8.setText(CCC)

    def ex_plus_wf(self):
        
        AAA = self.lineEdit_8.text()
        if AAA != '':
            format='%y/%m/%d'
            BBB= datetime.strptime(AAA,format)
            DDD=timedelta(weeks=1)
            BBB= BBB+DDD
            CCC= datetime.strftime(BBB,'%y/%m/%d')
            self.lineEdit_8.setText(CCC)
        if AAA == "":
            BBB=datetime.now()
            DDD=timedelta(weeks=1)
            BBB = BBB+ DDD
            CCC= datetime.strftime(BBB,'%y/%m/%d')
            self.lineEdit_8.setText(CCC)

    def ex_plus_mf(self):
        
        AAA = self.lineEdit_8.text()
        if AAA != '':
            format='%y/%m/%d'
            BBB= datetime.strptime(AAA,format)
            DDD= relativedelta(months=1)
            BBB= BBB+DDD
            CCC= datetime.strftime(BBB,'%y/%m/%d')
            self.lineEdit_8.setText(CCC)
        if AAA == "":
            BBB=datetime.now()
            DDD= relativedelta(months=1)
            BBB = BBB+ DDD
            CCC= datetime.strftime(BBB,'%y/%m/%d')
            self.lineEdit_8.setText(CCC)


    def search(self):
        cb = self.sel_option.currentText()        
        
        cl_all=self.table.rowCount()
        
        A = self.sel_edit.text()
        while cl_all != 0:
            
            self.table.removeRow(cl_all-1)
            cl_all = cl_all-1

        if cb == "아이디":
            connection = cx_Oracle.connect(user='admin', password='Dkdldbxm262!@', dsn='db202111291512_high')
            cursor = connection.cursor()        
            cursor.execute("select user_seq,name,id,email,mobile,to_char(new_date,'YY/MM/DD'),grade,to_char(st_date,'YY/MM/DD'),to_char(ex_date,'YY/MM/DD'),able,root from joon where id='"+A+"'  order by user_seq")
            rows = cursor.fetchall()
            cursor.close()
            connection.close()
        elif cb =="이메일":
            connection = cx_Oracle.connect(user='admin', password='Dkdldbxm262!@', dsn='db202111291512_high')
            cursor = connection.cursor()        
            cursor.execute("select user_seq,name,id,email,mobile,to_char(new_date,'YY/MM/DD'),grade,to_char(st_date,'YY/MM/DD'),to_char(ex_date,'YY/MM/DD'),able,root from joon where email='"+A+"'  order by user_seq")
            rows = cursor.fetchall()
            cursor.close()
            connection.close()
        
        for i in range(len(rows)):            
            self.table.insertRow(i)
            
            for j in  range(len(rows[i])):
                strowsj=str(rows[i][j])
                self.table.setItem(i,j,QTableWidgetItem(strowsj))

    def cl(self):        
        
        for i in range(self.table.columnCount()):
            for j in range(self.table.rowCount()):                
                self.table.item(j,i).setBackground(QtGui.QColor(255,255,255))

        
        st_st = []
        for i in range(self.table.columnCount()):
            st_st.append(self.table.item(self.table.currentRow(),i).text())
            self.table.item(self.table.currentRow(),i)
            self.table.item(self.table.currentRow(),i).setBackground(QtGui.QColor(100,160,235))
            
        
            
        self.AAA= st_st[0].strip()
        self.lineEdit.setText(st_st[1].strip())    
        self.lineEdit_2.setText(st_st[2].strip())        
        self.lineEdit_3.setText(st_st[3].strip())        
        self.lineEdit_4.setText(st_st[4].strip())        
        self.lineEdit_5.setText(st_st[5].strip())        
        self.lineEdit_6.setText(st_st[6].strip())        
        self.lineEdit_7.setText(st_st[7].strip())        
        self.lineEdit_8.setText(st_st[8].strip())        
        self.sel_able.setCurrentText(st_st[9].strip())
        
        self.lineEdit_10.setText(st_st[10].strip())

    def root_list(self):
        
        cb = self.sel_root.text()    
        
        cl_all=self.table.rowCount()

        while cl_all != 0:
            self.table.removeRow(cl_all-1)
            cl_all = cl_all-1

            
        
        connection = cx_Oracle.connect(user='admin', password='Dkdldbxm262!@', dsn='db202111291512_high')
        cursor = connection.cursor()        
        cursor.execute("select user_seq,name,id,email,mobile,to_char(new_date,'YY/MM/DD'),grade,to_char(st_date,'YY/MM/DD'),to_char(ex_date,'YY/MM/DD'),able,root from joon  where root='"+cb+"'order by user_seq")
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        
        
        for i in range(len(rows)):            
            self.table.insertRow(i)
            
            for j in  range(len(rows[i])):
                strowsj=str(rows[i][j])
                self.table.setItem(i,j,QTableWidgetItem(strowsj))
                self.table.setItem(i,j+2,QTableWidgetItem(""))
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.resizeColumnsToContents()

    def grade_list(self):
        
        cb = self.sel_grade.text()
        
        cl_all=self.table.rowCount()

        while cl_all != 0:
            self.table.removeRow(cl_all-1)
            cl_all = cl_all-1

            
        
        connection = cx_Oracle.connect(user='admin', password='Dkdldbxm262!@', dsn='db202111291512_high')
        cursor = connection.cursor()        
        cursor.execute("select user_seq,name,id,email,mobile,to_char(new_date,'YY/MM/DD'),grade,to_char(st_date,'YY/MM/DD'),to_char(ex_date,'YY/MM/DD'),able,root from joon  where grade='"+cb+"'order by user_seq")
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        
        
        for i in range(len(rows)):            
            self.table.insertRow(i)
            
            for j in  range(len(rows[i])):
                strowsj=str(rows[i][j])
                self.table.setItem(i,j,QTableWidgetItem(strowsj))
                self.table.setItem(i,j+2,QTableWidgetItem(""))
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.resizeColumnsToContents()

    def plus_st(self):
        self.lineEdit_5.setText(self.st_calendar.selectedDate().toString("yy/MM/dd"))
        self.st_calendar.hide()
    def st_cal(self,event):
        self.st_calendar.show()
    def plus_ex(self):
        self.lineEdit_8.setText(self.ex_calendar.selectedDate().toString("yy/MM/dd"))
        self.ex_calendar.hide()
    def ex_cal(self,event):
        self.ex_calendar.show()
    def plus_new(self):
        self.lineEdit_7.setText(self.new_calendar.selectedDate().toString("yy/MM/dd"))
        self.new_calendar.hide()
    def new_cal(self,event):
        self.new_calendar.show()

    def sel_plus_st(self):
        self.sel_st_edit.setText(self.sel_st_calendar.selectedDate().toString("yy/MM/dd"))
        self.sel_st_calendar.hide()
    def sel_st_cal(self,event):
        self.sel_st_calendar.show()

    def sel_plus_ex(self):
        self.sel_ex_edit.setText(self.sel_ex_calendar.selectedDate().toString("yy/MM/dd"))
        self.sel_ex_calendar.hide()
    def sel_ex_cal(self,event):
        self.sel_ex_calendar.show()

    def sel_plus_new(self):
        self.sel_new_edit.setText(self.sel_new_calendar.selectedDate().toString("yy/MM/dd"))
        self.sel_new_calendar.hide()
    def sel_new_cal(self,event):
        self.sel_new_calendar.show()



    
        
        
        # self.sckck.start()
    def log_list(self):
        
        cl_all=self.table.rowCount()
        
        while cl_all != 0:
            self.table.removeRow(cl_all-1)
            cl_all = cl_all-1
        self.ch_th.start()
        time.sleep(3)
        one_harf = self.ch_th.clclcl.split("__")
        tow_con = one_harf[0].split("|")
        the_con = one_harf[1].split("|")
        four_con = one_harf[2].split("|")        
        for i in range(len(tow_con)):
            if tow_con[i] != "":
                print(tow_con[i])
                print(the_con[i])
                connection = cx_Oracle.connect(user='admin', password='Dkdldbxm262!@', dsn='db202111291512_high')
                cursor = connection.cursor()        
                cursor.execute("select user_seq,name,id,email,mobile,to_char(new_date,'YY/MM/DD'),grade,to_char(st_date,'YY/MM/DD'),to_char(ex_date,'YY/MM/DD'),able,root from joon where id = '"+tow_con[i].strip()+"'order by user_seq")
                rows = cursor.fetchall()
                cursor.close()
                connection.close()            
                for xy in range(len(rows)):
                    self.table.insertRow(xy)
                    for j in  range(len(rows[xy])):
                        strowsj=str(rows[xy][j])                    
                        self.table.setItem(xy,j,QTableWidgetItem(strowsj))
                        self.table.setItem(xy,j+1,QTableWidgetItem(the_con[i]))
                        self.table.setItem(xy,j+2,QTableWidgetItem(four_con[i]))
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.resizeColumnsToContents()
        
        self.ch_th.terminate()
        
        

    def user_list(self):
        
        cl_all=self.table.rowCount()

        while cl_all != 0:
            self.table.removeRow(cl_all-1)
            cl_all = cl_all-1        
        connection = cx_Oracle.connect(user='admin', password='Dkdldbxm262!@', dsn='db202111291512_high')
        cursor = connection.cursor()        
        cursor.execute("select user_seq,name,id,email,mobile,to_char(new_date,'YY/MM/DD'),grade,to_char(st_date,'YY/MM/DD'),to_char(ex_date,'YY/MM/DD'),able,root from joon order by user_seq")
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        
        
        for i in range(len(rows)):            
            self.table.insertRow(i)
            
            for j in  range(len(rows[i])):
                strowsj=str(rows[i][j])
                self.table.setItem(i,j,QTableWidgetItem(strowsj))
                self.table.setItem(i,j+2,QTableWidgetItem(""))
        
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.resizeColumnsToContents()
            
    def new_user(self):
        user_name = self.lineEdit.text()
        user_id = self.lineEdit_2.text()        
        user_mail=self.lineEdit_3.text()
        user_mob=self.lineEdit_4.text()
        grade=self.lineEdit_6.text()
        ud_st_date=self.lineEdit_7.text()
        ud_ex_date=self.lineEdit_8.text()
        st_date = ud_st_date.replace("/","")
        ex_date = ud_ex_date.replace("/","")
        connection = cx_Oracle.connect(user='admin', password='Dkdldbxm262!@', dsn='db202111291512_high')
        cursor = connection.cursor()
        
        cursor.execute("insert into joon values(USER_SEQ.nextval, '"+user_name+"',  '"+user_id+"',  'cow2468',  '"+user_mail+"',  '"+user_mob+"',  0,  sysdate,  '"+grade+"', to_date('"+st_date+"','YY/MM/DD'), to_date('"+ex_date+"','YY/MM/DD'), 'N',0,0)")
        
        cursor.close()
        connection.commit()
        connection.close()
        self.user_list()
        
        
        
        

        
    

    def del_user(self):
        result = self.de_msg()
        if result == QMessageBox.Yes:            
            connection = cx_Oracle.connect(user='admin', password='Dkdldbxm262!@', dsn='db202111291512_high')
            cursor = connection.cursor()
            cursor.execute("delete from joon where user_seq = '"+self.AAA+"'")
            connection.commit()
            cursor.close()            
            connection.close()
            self.user_list()

    def update_user(self):        
        result = self.ud_msg()
        if result == QMessageBox.Yes:
            
            ud_email=self.lineEdit_3.text()
            ud_mob=self.lineEdit_4.text()            
            ud_grade=self.lineEdit_6.text()
            
            ud_st_date=self.lineEdit_7.text()
            ud_ex_date=self.lineEdit_8.text()
            ud_able=self.sel_able.currentText()
            ud_root=self.lineEdit_10.text()
            st_date = ud_st_date.replace("/","")
            ex_date = ud_ex_date.replace("/","")
            
            
            connection = cx_Oracle.connect(user='admin', password='Dkdldbxm262!@', dsn='db202111291512_high')
            cursor = connection.cursor()
            cursor.execute("update joon set email='"+ud_email+"', mobile='"+ud_mob+"', grade='"+ud_grade+"', st_date= to_date('"+st_date+"','YYMMDD'), ex_date= to_date('"+ex_date+"','YYMMDD'), able='"+ud_able+"',root = '"+ud_root+"' where user_seq='"+self.AAA+"'")
            connection.commit()
            cursor.close()            
            connection.close()
            self.user_list()
            
        else:
            print("no")

    def de_msg(self):
        demsg= QMessageBox()
        demsg.setWindowTitle("회원삭제")
        demsg.setText("회원삭제")
        demsg.setInformativeText("정말 삭제하시겠습니까?")
        demsg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        return demsg.exec_()

    def ud_msg(self):
        udmsg= QMessageBox()
        udmsg.setWindowTitle("회원정보 수정")
        udmsg.setText("회원정보수정")
        udmsg.setInformativeText("정말 수정하시겠습니까?")
        udmsg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        return udmsg.exec_()
        

    def sel_user(self):
        
        connection = cx_Oracle.connect(user='admin', password='Dkdldbxm262!@', dsn='db202111291512_high')
        cursor = connection.cursor()        
        cursor.execute("select * from joon where user_seq ='"+self.AAA+"'")
        rows = cursor.fetchall()
        strows= ""
        for i in range(len(rows)):
            for j in  range(len(rows[i])):
                strowsj=str(rows[i][j])
                strows=strows + "  |  " +strowsj 
            
        cursor.close()
        connection.close()
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()






