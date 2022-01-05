import sqlalchemy as db
from sqlalchemy.sql.expression import table

engine = db.create_engine("mysql+pymysql://skdi262:tjdwnd262@skdi262.cafe24.com/skdi262")

con = engine.connect()
meta = db.MetaData()
table=db.Table('tbl_user',meta,autoload=True,autoload_with=engine)

print(table.columns.keys())