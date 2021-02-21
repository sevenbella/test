# 修改数据t_book数据

import pymysql
conn = pymysql.connect(host='127.0.0.1', port='3306', database='t_books',
                       user='root', password='root', charset='utf8', autocommit='True')

cursor = conn.cursor()
sql='update t_book set title = "游记" where id=4'
cursor.execute(sql)
print('修改的行数：', cursor.rowcount)

cursor.close()
conn.close()

