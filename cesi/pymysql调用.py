#使用自定义的pymysql工具类
from Pymysql_practice.MyUtils import DUBtil

# 获取连接
conn = DBUtil.get_conn()

# 获取游标
cursor = DUBtil.get_cursor(conn)

#核心 SQL语句
sql = 'select * from t_book'
cursor.excute(sql)

rows=cursor.fetchall()
for row in rows:
    print(row)

#释放资源
DUBtil.close_res(cursor,conn)



