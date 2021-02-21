# 演示 PyMySQL 的基本框架代码
# 1、导包PyMySQL
import pymysql
# 2、创建Python程序到数据库的连接 Connection 对象(桥)
conn = pymysql.Connect(host="127.0.0.1", port=3306, database="books",
                       user="root", password="YES", charset="utf8")
                #如涉及中文 避免乱码需设置charset = 'utf8' 编码集在pymysql里无中间'-'

# 配置数据库连接信息
# 3、在 Connection 上创建获取 Cursor 游标对象(小毛驴)
cursor = conn.cursor()
# 4、核心 通过 cursor 发送 SQL 语句，并接收响应结果
print(conn)
print(cursor)

# 5、最后:释放资源,卸磨杀驴、过河拆桥
cursor.close()
conn.close()
