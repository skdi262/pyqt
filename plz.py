from numpy import empty
from sshtunnel import SSHTunnelForwarder, check_address
from sqlalchemy import create_engine
import pandas as pd

class plz():

    def selec_all():
        server = SSHTunnelForwarder(
            ('skdi262.cafe24.com', 22),
            ssh_username="skdi262",
            ssh_password="tjdwnd262",
            remote_bind_address=('210.179.24.204', 3306)
        )
        server.start()
        local_port = str(server.local_bind_port)
        engine = create_engine('mysql+pymysql://skdi262:tjdwnd262@skdi262.cafe24.com/skdi262')
        dataDF = pd.read_sql("select * from tbl_user", engine)
        print(dataDF)
        server.stop()

    def check_user(user_id,user_pass):
        server = SSHTunnelForwarder(
            ('skdi262.cafe24.com', 22),
            ssh_username="skdi262",
            ssh_password="tjdwnd262",
            remote_bind_address=('localhost', 3306)
        )
        server.start()
        # local_port = str(server.local_bind_port)
        engine = create_engine('mysql+pymysql://skdi262:tjdwnd262@skdi262.cafe24.com/skdi262')
        dataDF = pd.read_sql("select name from tbl_user where user_id = '"+user_id+"' and passcode ='"+user_pass+"'", engine)
        if dataDF.empty:
            print("없수다")
        else:
            return 1
        server.stop()
    print(check_user("skdi262","tlqkf262"))

