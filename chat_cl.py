from socket import *
from select import *
import sys
import time
from requests import get

HOST = '210.179.24.204'
PORT = 9998
BUFSIZE = 1024
ADDR = (HOST,PORT)

clientSocket = socket(AF_INET, SOCK_STREAM)# 서버에 접속하기 위한 소켓을 생성한다.

try:
    clientSocket.connect(ADDR)# 서버에 접속을 시도한다.    
    while True:
        try:
            ip=get("https://api.ipify.org").text
            # clientSocket.send(.encode())	# 서버에 메시지 전달
            
            # clientSocket.send(ip.encode())
            A = 'user_ch|skdi262|tlqkf262|'+ip
            clientSocket.send(A.encode())
            data=clientSocket.recv(65535)
            clclcl= data.decode()
            print(clclcl)
            
        except:
            break
except  Exception as e:
    print("실패",'%s:%s'%ADDR)
sys.exit()


