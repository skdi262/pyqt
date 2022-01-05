from socket import *
from select import *
import time 
import threading
t = []
ind = 0
HOST = ''
PORT = 9998
BUFSIZE = 1024
ADDR = (HOST, PORT)

# 소켓 생성
serverSocket = socket(AF_INET, SOCK_STREAM)

# 소켓 주소 정보 할당 
serverSocket.bind(ADDR)
print('bind')

# 연결 수신 대기 상태
serverSocket.listen(100)
print('listen')
clientSocekt = "clientSocekt"

i=0
cl = {}



def read_msg():
    while 1:
        
        cl_list = list(cl.keys())
        
        
        for i in range(len(cl_list)):                    
            if i>= len(cl):
                break
            try:
                cli=cl_list[i]
                data = cli.recv(65535)
                
            except:
                print("실패")
                del cl[cli]
            print('recieve data : ',data.decode())
            time.sleep(5)
            
            


th_cli = threading.Thread(target=read_msg,daemon=True).start()

while True :    
    
    clientSocekt = "clientSocekt"
    clientSocekt = clientSocekt + str(i)
    clientSocekt, addr_info = serverSocket.accept()
    
    cl[clientSocekt] =""
    
    
    
    print("hi")
    
    i=i+1
    if i==10:
        break







# 소켓 종료 

serverSocket.close()
print('close')