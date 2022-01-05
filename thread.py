import subprocess


asd=subprocess.Popen('adb devices',stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,shell=True).stdout
i=0
ddd= []
while True:
    bbb=asd.readline().decode('utf-8').strip()
    # print(bbb)
    ddd.append(bbb)
    i=i+1
    if not bbb :
        break
del ddd[-1]
de_1 =ddd[-1][0:7]
de_2 = ddd[-2][0:7]
print("|"+de_2+"|",len(ddd))


    