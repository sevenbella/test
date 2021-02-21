# 需求： 封装pymysql工具类

import pymysql

class DBUtil:
    @classmethod
    def get_conn(cls):        # 封装获取连接的参数  返回值connection  参数值暂不设置写死 后期从配置文件读取
        conn=pymysql.connect(host='127.0.0.1', port='3306', database='t_books',
                       user='root', password='root', charset='utf8')
        return conn

    @classmethod
    def get_cursor(cls, conn):     # 封装游标对象函数  参数： 连接对象  返回值：连接对象
        return conn.cursor()       # == cursor=conn.cursor  return cursor

    @classmethod
    def close_res(cls, cursor, conn):    # 封装资源释放函数  参数：cursor/ conn   返回值 无
        if cursor:                      #  加入None判断
            cursor.close()
            cursor=None
        if conn:                        #  加入None判断
            conn.close()
            conn=None


