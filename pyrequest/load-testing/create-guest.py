import time
import sqlite3
db_name = './../db_fixture/db.sqlite3'

conn = sqlite3.connect(db_name)

c = conn.cursor()

toStr = lambda x: "'" + x + "'"
for i in range(1, 3001):
    eid = str(i)
    realname = 'Jack' + str(i)
    phone = str(13800018888 + i)
    email = realname.strip("'") + '@mail.com'
    sign = str(1)
    now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    L = [eid, realname, phone, email, sign, now]
    L = [str(toStr(i)) for i in L]
    L = ','.join(L)
    print(L)
    sql = "insert into sign_guest values (" + L + ")"
    # print(sql)

    c.execute(sql)
conn.close()
