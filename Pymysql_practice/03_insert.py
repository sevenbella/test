#  需求 向t_book表插入一条数据
# 1. 整合第三方
import pymysql

# 2. 创建连接
conn = pymysql.Connect(host="127.0.0.1", port=3306, database="books",
                       user="root", password="YES", charset="utf8", autocommit = True)
                                            # 事务提交方法二 : 此处设置默认提交数据， 即 autocommit = True

# 3. 创建游标
cursor = conn.cursor()

# 4. 发送SQL
sql = 'insert into t-book values(4, "西游记", "1900-10-10" , 100, 50, 0)'
cursor.execute(sql)
print('新增行数为：', cursor.rowcount)

#  事务提交   pymysql默认sql不提交数据库 需设置为提交
conn.commit()


# 5. 释放资源
cursor.close()
conn.close()

### pymysql默认sql不提交数据库 需设置为提交
# 方式1  手动提交  conn.commit()
# 方式2   pymysql.Connect(.... autocommit = True)  默认为False

