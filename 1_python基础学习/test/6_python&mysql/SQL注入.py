import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='010920hei',
    database='mydb_1',
    charset='utf8mb4'
)

cursor = conn.cursor()
# #不安全的方式
# name = input("输入学生姓名：")
# sql = "select * from users where name='%s'" % name
# cursor.execute(sql)
# context = cursor.fetchall()
# print(context)
# cursor.close()
# conn.close()
#安全的方式
name = input("输入学生姓名：")
sql = "select * from emp1 where name=%s"

cursor.execute(sql,[name])
context = cursor.fetchall()
print(context)
cursor.close()
conn.close()