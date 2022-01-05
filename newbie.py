
import subprocess
import time

while True:

    bbs=subprocess.Popen('adb shell getprop ro.product.model',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
    bbs = bbs.read().decode('utf-8').strip()
    bbs= bbs.split("\n")
    csd = bbs[0][:5]
    if csd == 'error' or csd=='adb.e' or csd =="" or csd =='adb:' or csd == "adb.:"  or csd == "* dae":
        time.sleep(1)
        print(csd)        
    else:
        break
print("hi")
