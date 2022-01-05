
import multiprocessing
import sys

from typing import Awaitable
from PyQt5.QtGui import *

import paramiko
import pandas as pd
# from plz import *
from newbie import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import os
import time
import pymysql
import subprocess
from multiprocessing import Process
import threading
from requests import get
from datetime import datetime




# conn = None
# cur = None
# sql=""
# conn=pymysql.connect(host="localhost",port=3306,user="skdi262",passwd="tjdwnd262",db="skdi262",charset="utf8")
# cur = conn.cursor()

# sql = "select name from tbl_user where user_id='skdi262'"
# cur.execute("set names utf8")
# cur.execute(sql)


# rows=cur.fetchall()
# for data in rows:
#     print(data)

# conn.commit
# conn.close()

now_file = os.getcwd()
print(now_file)
form_class = uic.loadUiType(now_file +r"\untitled_2.ui")[0]

class MyWindow(QMainWindow, form_class):
    
    
    def __init__(self):
        
        super().__init__()        
        
        self.setupUi(self)        

        # self.label_5.setText(self.get_ip())
        self.pushButton.clicked.connect(self.show_product)


        
        
        
        
    def adb_dvices(self):
        subprocess.run('adb devices')
        subprocess.run('adb shell input tap 0 0')
    def show_product(self):


        subprocess.run('adb devices', env=None,shell=True)
        
        
    
        




            
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    
    myWindow.adb_dvices
    myWindow.show_product()
    


    
    
    app.exec_()
    subprocess.run('adb kill-server')
    
    