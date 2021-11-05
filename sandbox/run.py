import sqlite3
import akshare as ak
import pandas as pd
from workalendar.asia import China
from datetime import date, timedelta, datetime
from sqlalchemy import create_engine

engine = create_engine('sqlite:///../sqlite_data/fund.db', echo=False)
fund_size = pd.read_sql('szie',con=engine)
print(fund_size)
#fund_size['code']=pd.to_numeric(fund_size['code'])
#fund_size.to_sql('szie', con=engine)
# 连接
#con = sqlite3.connect("../sqlite_data/fund.db")
#cur = con.cursor()
# 创建size
#sql = "CREATE TABLE IF NOT EXISTS size(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)"
#cur.execute(sql)
#data = "1,'Desire',5"
#cur.execute('INSERT INTO test VALUES (%s)' % data)
# ②：添加单条数据
#cur.execute("INSERT INTO test values(?,?,?)", (6, "zgq", 20))
# ③：添加多条数据
#cur.executemany('INSERT INTO test VALUES (?,?,?)', [(3, 'name3', 19), (7, 'name4', 26)])
#cur.execute("select * from Test")
#print(cur.fetchall())