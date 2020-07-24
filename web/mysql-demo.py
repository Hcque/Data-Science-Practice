from pymysql import cursors, connect

conn = connect(host='127.0.0.1',
               user='root',
               password='123456',
               charset='utf8mb4',
               cursorclass=cursors.DictCursor)
with conn.cursor() as cursor:
    print(cursor.execute('show databases;'))

