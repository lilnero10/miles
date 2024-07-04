from pymysql import Connection

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='010920hei',
    autocommit=True      #自动提交
)

#获取游标对象
cursor = conn.cursor()

#选择数据库
conn.select_db("mydb_optimize")

#使用游标对象，执行sql语句
cursor.execute("load data local infile 'Users/chenzhiyong/Downloads/sql1.log' into table tb_user fields terminated by ',' lines terminated by '\n';")

#获取查询数据打印
# results = cursor.fetchall()
# for r in results:
#     print(r)

#通过commit确认
conn.commit()
# #关闭数据库
# conn.close()

