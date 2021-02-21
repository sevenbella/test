# 演示 PyMySQL 的基本框架代码
# 1、导包PyMySQL
import pymysql

# 2、创建Python程序到数据库的连接 Connection 对象(桥)
conn = pymysql.Connect(host="127.0.0.1", port=3306, database="books", user="root", password="YES", charset="utf8")
# 配置数据库连接信息

# 3、在 Connection 上创建获取 Cursor 游标对象(小毛驴)
cursor = conn.cursor()

# 4、核心 通过 cursor 发送 SQL 语句，并接收响应结果
print(conn)
print(cursor)

sql = "select * from t_book"
cursor.execute(sql)      # cursor执行sql语句

# 解析结果（游标响应回来数据）
# 1. 获取响应的结果的行数
print('响应结果行数', cursor.rowcount)

# 2. 获取单条数据
row1 = cursor.fetchone()   # ferchone 一次调用获取一条，下一次调用获取下一条
row2 = cursor.fetchone()
print(row2)

# 3. 获取所有数据
rows = cursor.fetchall()

##  fetchone 与 ferchall尽量不要混合使用  不论二者谁在前面，都会先一步将数据卸掉显示，后者无法显示需要数据

# 遍历表中每一条数据
for row in rows:
    print(row)

for row in rows:
    print('-'*40)
    print('ID:',row[0])
    print('书名:', row[1])
    print('日期:', row[2])
    print('阅读数:', row[3])
    print('评论数:', row[4])
    print('状态:', row[5])

# 5、最后:释放资源,卸磨杀驴、过河拆桥
cursor.close()
conn.close()