# 删除t_book中的id为4的数据
import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, database='books',
                       user='root', password='root', charset='utf8', autocommit=True)
cursor=conn.cursor()
sql='delete from t_book where id=4'
cursor.execute(sql)
print('被删除的行数',cursor.rowcount)

cursor.close()
conn.close()
