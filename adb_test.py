import cx_Oracle
import os
now_file = os.getcwd()
# cx_Oracle.init_oracle_client(lib_dir=now_file+r"\instantclient_21_3")
LOCATION = now_file+r"\instantclient_21_3"
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"] #환경변수 등록
# 본인이 Instant Client 넣어놓은 경로를 입력해준다

connection = cx_Oracle.connect(user='admin', password='Dkdldbxm262!@', dsn='db202111291512_high')
# 본인이 접속할 오라클 클라우드 DB 사용자이름, 비밀번호, dsn을 넣어준다.
cursor = connection.cursor()
cursor.execute("select * from joon where id='cowboy'")
rows = cursor.fetchall()
for row in rows:
    print(row[0])
    

