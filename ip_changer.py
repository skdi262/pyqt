


import sys




from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import os
import time
from requests import get
from datetime import datetime
import subprocess
now_file = os.getcwd()
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """ 
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))) 
    return os.path.join(base_path, relative_path)



form=resource_path("ip_change.ui")
form_class = uic.loadUiType(form)[0]
adb_bat = resource_path("adb_reset.bat")
adb = resource_path("adb.exe")
adb_dll_1 = resource_path("AdbWinApi.dll")
adb_dll_2 = resource_path("AdbWinUsbApi.dll")
subprocess.run(adb_bat,shell=True)
subprocess.run(adb,shell=True)
class ip_run(QThread):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        
    def run(self) :
        self.parent.on_air()
        time.sleep(3)
        self.parent.off_air()
        time.sleep(3)
        try:
            ip=get("https://api.ipify.org").text
            print(ip)
            now = datetime.now()        
            nowRT = now.strftime(" / %m/%d %H:%M")
            now_get = ip + nowRT
            self.parent.textBrowser.append(now_get)
            self.parent.pushButton.setEnabled(True)  
            self.parent.pushButton.setText("IP 변경")
            self.parent.s_max()
            
        except:
            print("hi")
            self.parent.pushButton.setEnabled(True)  
            
            self.parent.pushButton.setText("IP 변경") 
            self.parent.s_max()


class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        
        super().__init__()        
        
        self.setupUi(self)    
        self.pushButton.clicked.connect(self.ipappend)
        self.pushButton_3.clicked.connect(self.now_ip)
        self.iprun=ip_run(self)
        self.scrollBar = self.textBrowser.verticalScrollBar()
        self.setWindowTitle("IP변경/준소프트")
        self.now_ip()

    def now_ip(self):
        
        try:
            ip=get("https://api.ipify.org").text
            adad= "현재 IP : "
            afaf = adad + ip
            self.label.setText(afaf)
        except:
            print("no")

    def ipappend(self):
        self.iprun.start()
        self.pushButton.setEnabled(False)  
        self.pushButton.setText("IP 변경 중") 
        

    def s_max(self):
        time.sleep(0.5)
        self.scrollBar.setValue(self.scrollBar.maximum())
    def on_air(self):

        subprocess.run('adb shell settings put global airplane_mode_on 1',shell=True)
        subprocess.run("adb shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true",shell=True)

    def off_air(self):

        subprocess.run('adb shell settings put global airplane_mode_on 0',shell=True)
        subprocess.run("adb shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false",shell=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    
    myWindow.show()
    app.exec_()
    subprocess.run('adb kill-server',shell=True)
    