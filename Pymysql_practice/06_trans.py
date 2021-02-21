# 先往t_book插入三国演义的信息，再向t_hero插入该书主角诸葛亮信息，要求要么都成功，要么都失败

import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, database='t_books',
                     user='root', password='root',charset='utf8')
                         # autocommit=True不能实现该事务需求，在某一条需求失败时另一条仍成功，手动提交事务

cursor = conn.cursor()

# 13-17运行正常，事务提交，否则，不执行提交，只回归 == 使用try语句实现分支
try:
    sql1 = 'insert into t_book values(5,"三国演义", '1999-01-20', 50, 500, 0)'
    cursor.execute(sql1)

    sql2 = 'insert into t_hero values(6,"诸葛亮", 1, "足智多谋", 0, 400'
    cursor.execute(sql2)

    conn.commit()   # 提交事务

except Exception as e:
    print(e)
    conn.rollback()

finally:   # 优化 try except通常跟finally 在finally中关闭资源
    cursor.close()
    conn.close()



