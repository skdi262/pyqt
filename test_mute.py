import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import os
import subprocess
import time
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form1 = resource_path("mute.ui")

form_class = uic.loadUiType(form1)[0]

class mutal(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
        st_asd = st_asd.readline(5).decode('utf-8').strip()
        asd = asd.read().decode('utf-8').strip()
        
        if st_asd == 'error'or st_asd =='adb.e' or st_asd =='adb:' or st_asd=="adb.:" or st_asd =="ad: m":
            pass
        else:
            
            subprocess.run("adb shell input keyevent 3",shell=True)                    
            if asd =='SM-N750K' or asd == "SM-G720N0" or asd=="SM-G900S" or asd == 'SM-G930S' or asd =='LM-X410K' or asd == 'LG-F650S':
                subprocess.run('adb shell input swipe 170 1070 170 250 300',shell=True)
            elif asd == 'SM-G930S' or 'SM-G8550K':
                subprocess.run('adb shell input swipe 170 1070 170 250 300',shell=True)
            elif asd == 'LM-Q725K':
                subprocess.run('adb shell input swipe 170 1570 170 250 300',shell=True)
            else :
                subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)
                subprocess.run("adb shell input swipe 670 1450 670 750 300",shell=True)      
            time.sleep(0.3)
            subprocess.run("adb shell input keyevent 3",shell=True)        
            time.sleep(0.5)
            subprocess.run("adb shell am start -n com.android.settings/.SoundSettings",shell=True)
            time.sleep(0.3)
            
            print(asd)
            if asd == 'SM-N900S':                
                
                subprocess.run("adb shell input swipe 550 750 50 750 300",shell=True)
                time.sleep(0.3)                
                for i in range(6):
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input tap 900 1150",shell=True)
                for i in range(7):
                    subprocess.run("adb shell input keyevent 20",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input swipe 500 500 500 1500 300",shell=True)
                time.sleep(0.3)  
                subprocess.run("adb shell input swipe 500 500 500 1500 300",shell=True)
                time.sleep(0.3)  
                subprocess.run("adb shell input tap 880 380",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 4",shell=True) 
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 20",shell=True) 
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 20",shell=True) 
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                for i in range(7):
                    subprocess.run("adb shell input keyevent 20",shell=True)
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)                
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                subprocess.run("adb shell input keyevent 20",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 3",shell=True) 


            elif asd =='SM-G900S':
                for i in range(6):
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input tap 900 1150",shell=True)
                for i in range(7):
                    subprocess.run("adb shell input keyevent 20",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input swipe 500 500 500 1500 300",shell=True)
                time.sleep(0.3)  
                subprocess.run("adb shell input swipe 500 500 500 1500 300",shell=True)
                time.sleep(0.3)  
                subprocess.run("adb shell input tap 880 380",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 3",shell=True) 
                
            elif asd == 'SM-N900K':
                
                print("h")
                subprocess.run("adb shell input swipe 550 750 50 750 300",shell=True)
                time.sleep(0.3)                
                for i in range(5):
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input tap 900 1150",shell=True)
                for i in range(7):
                    subprocess.run("adb shell input keyevent 20",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input swipe 500 500 500 1500 300",shell=True)
                time.sleep(0.3)  
                subprocess.run("adb shell input swipe 500 500 500 1500 300",shell=True)
                time.sleep(0.3)  
                subprocess.run("adb shell input tap 880 380",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 4",shell=True) 
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 20",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 20",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                for i in range(7):
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 20",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 3",shell=True) 

            elif asd == "SM-G928K":
                
                subprocess.run("adb shell input tap 585 285",shell=True)
                time.sleep(0.3)  
                subprocess.run("adb shell input tap 175 560",shell=True)
                time.sleep(0.3)  
                for i in range(8):
                    subprocess.run("adb shell input keyevent 20",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)                
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)                
                subprocess.run("adb shell input keyevent 66",shell=True)
                
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 3",shell=True) 

            elif asd =='SM-G906S':
                
                for i in range(6):
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input tap 1200 1520",shell=True)
                for i in range(7):
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input swipe 750 800 750 2000 300",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input swipe 750 800 750 2000 300",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input tap 1210 500",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 3",shell=True) 


            elif asd=='SM-G906K':
                
                for i in range(5):
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input tap 1200 1520",shell=True)
                for i in range(7):
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input swipe 750 800 750 2000 300",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input swipe 750 800 750 2000 300",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input tap 1210 500",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 4",shell=True) 
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 20",shell=True) 
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 20",shell=True) 
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                for i in range(8):
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 3",shell=True) 
            

            elif asd =='LG-F650S':
                subprocess.run("adb shell input tap 200 350",shell=True)
                time.sleep(0.3)  
                subprocess.run("adb shell input tap 650 470",shell=True)
                time.sleep(0.3)  
                subprocess.run("adb shell input keyevent 20",shell=True)
                time.sleep(0.3)  
                subprocess.run("adb shell input keyevent 20",shell=True)
                time.sleep(0.3)  
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)  
                subprocess.run("adb shell input swipe 450 890 100 890 300",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 3",shell=True) 

            elif asd == 'SM-N750K':                
                for i in range(5):
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input tap 600 750",shell=True)
                for i in range(7):
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input swipe 350 300 350 1050 300",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input swipe 350 300 350 1050 300",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input tap 600 260",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 4",shell=True) 
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 20",shell=True) 
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 20",shell=True) 
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                for i in range(7):
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 3",shell=True) 

            elif asd =='SM-N916K':
                
                for i in range(5):
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input tap 1200 1520",shell=True)
                for i in range(7):
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input swipe 750 800 750 2000 300",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input swipe 750 800 750 2000 300",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input tap 1210 500",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 4",shell=True) 
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 20",shell=True) 
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 20",shell=True) 
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                
                subprocess.run("adb shell input keyevent 3",shell=True) 

            elif asd =='SM-G850K':
                
                for i in range(5):
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input tap 600 750",shell=True)
                for i in range(6):
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                
                subprocess.run('adb shell input swipe 170 300 170 1000 300',shell=True)
                time.sleep(0.3)
                subprocess.run('adb shell input swipe 170 300 170 1000 300',shell=True)
                time.sleep(0.3)
                
                subprocess.run("adb shell input tap 600 250",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 4",shell=True) 
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 20",shell=True) 
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 20",shell=True) 
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                for i in range(7):
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)                
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 20",shell=True)                
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 3",shell=True) 

            elif asd =="SM-G720N0":
                
                for i in range(10):
                    subprocess.run("adb shell input keyevent 25",shell=True)                
                    time.sleep(0.2)
                for i in range(3):
                    subprocess.run("adb shell input keyevent 20",shell=True)                
                    time.sleep(0.3)
                subprocess.run("adb shell input keyevent 66",shell=True)
                time.sleep(0.3)
                subprocess.run('adb shell input swipe 170 300 170 1000 300',shell=True)
                time.sleep(0.3)
                subprocess.run('adb shell input swipe 170 300 170 1000 300',shell=True)
                time.sleep(0.3)
                
                subprocess.run("adb shell input tap 630 200",shell=True)
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 4",shell=True) 
                time.sleep(0.3)
                subprocess.run("adb shell input keyevent 3",shell=True) 


            else:
                pass



class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)    
        self.mutal = mutal(self)
        self.pushButton.clicked.connect(self.timestart)
    def timestart(self):
        self.mutal.start()
    def adb_devices(self):
        subprocess.run("adb devices",shell=True)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.adb_devices()
    myWindow.show()
    app.exec_()
    subprocess.run('adb kill-server',shell=True)
    